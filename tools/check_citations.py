#!/usr/bin/env python3
"""Gate citations É2bis — chantier CDC companion (plan §5).

Vérifie que chaque citation au format §2 `[Auteur, année, arXiv:XXXX.XXXXX ou DOI:10.x/...]`
des fiches `dimensions/*.md` résout vers un papier réel dont le premier auteur et
l'année concordent.

Chaîne de résolution : arXiv → Crossref (DOI) → Semantic Scholar.
Statuts :
  - RESOLUE      : identifiant trouvé, premier auteur ET année concordent ;
  - DISCORDANTE  : identifiant trouvé mais premier auteur OU année ne matchent pas
                   (NB : le format §2 ne porte pas de titre — le titre résolu est affiché
                   dans le rapport pour contrôle humain, le match porte auteur + année ;
                   la concordance sémantique est couverte par le spot-check) ;
  - INTROUVABLE  : identifiant inconnu des trois sources, OU échec réseau
                   (un échec réseau n'est JAMAIS compté RESOLUE).

Sorties :
  - docs/cdc/citations_report.md   : rapport détaillé de la passe (réécrit à chaque passe) ;
  - docs/cdc/citations_count.json  : compte par fiche et par passe (append ; une passe par
    jour — relancer le même jour remplace la passe du jour, pas d'inflation de passes).
    `--nouvelle-passe` : [AJOUT VALIDATION 10/08] force une entrée NEUVE même si la dernière
    passe porte la date du jour. Sans elle, deux passes le même jour font perdre la ligne de
    la première — donc sa baseline anti-gaming (défaut ouvert depuis la session 5, corrigé
    sur accord explicite de Sébastien le 10/08/2026, avant la passe 6).
Anti-gaming : si le compte de citations UNIQUES d'une fiche baisse entre deux passes,
la passe marque REGRESSION pour cette fiche (plan §5).

Hors périmètre (dérogation déclarée par la session 2, note dans etat.md) : les textes
réglementaires (AI Act, RGPD) cités en clair avec URL EUR-Lex, hors format §2 — la regex
ne les capte pas, leur absence du rapport n'est pas une régression.

`--spot-check` : tire N citations (défaut 5) — graine = date du jour (reproductible le même
jour, échantillon opposable) — et affiche pour chacune la fiche, le contexte d'appel dans la
fiche, le titre résolu et l'abstract, pour le jugement humain OUI/NON (spot_check_<lot>.md).

RÈGLE (plan §5) : première passe = la session écrit ce script, le committe, l'exécute.
Passes suivantes : EXÉCUTION SEULE — toute modification de ce script exige une validation
humaine explicite de Sébastien.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIM_DIR = ROOT / "dimensions"
REPORT_PATH = ROOT / "out" / "citations_report.md"
COUNT_PATH = ROOT / "out" / "citations_count.json"

# Crossref demande un User-Agent identifiable (polite pool)
USER_AGENT = "projet-coach-cdc/check_citations (mailto:contact-via-github)"

# Format §2 : [Auteur, année, arXiv:XXXX.XXXXX] ou [Auteur, année, DOI:10.x/...]
# Les classes de caractères acceptent les retours à la ligne : une citation peut être
# coupée par le retour à la ligne du markdown ([Jiménez\nGutiérrez, ...]).
#
# [AJOUT VALIDATION 11/08] Deux angles morts fermés, trouvés par la session 15 au gate du
# lot 7 : **5 sources réellement citées n'avaient JAMAIS été soumises au gate depuis la
# passe 1**, et leur absence était invisible (une citation non captée ne sort pas en
# INTROUVABLE — elle n'existe pas pour le rapport).
#   1. **Crochet groupé** « [A, an, DOI:x ; B, an, DOI:y] » : l'ancienne regex exigeait le
#      « ] » collé à l'identifiant et ne captait donc AUCUNE des deux citations. Une citation
#      peut désormais s'ouvrir sur « [ » ou « ; » et se fermer sur « ] » ou « ; » (lookahead,
#      pour qu'un « ; » serve à la fois de fin à l'une et de début à l'autre).
#   2. **Coupure par le préfixe « > »** du bloc-citation d'en-tête, qui insérait un « > » au
#      milieu du motif ([Bailey, 2006,\n> DOI:...]). Les séparateurs tolèrent « > ».
# Accord explicite de Sébastien le 11/08/2026 (plan §5). Vérifié avant commit : sur les
# 43 fiches, la nouvelle regex capte **exactement les 762 anciennes citations, à l'identique,
# plus les 7 invisibles** (5 sources réellement portées + 2 renvois d'homonymie d'en-tête) —
# **0 perdue, 0 modifiée, 0 faux positif**. Le script redevient « exécution seule ».
CITATION_RE = re.compile(
    r"[\[;]\s*([^,;\[\]]+?)\s*,[\s>]*(\d{4})\s*,[\s>]*"
    r"((?:arXiv:[\s>]*\d{4}\.\d{4,5}(?:v\d+)?)|(?:DOI:[\s>]*10\.[^\];\s>]+))[\s>]*(?=[;\]])",
    re.IGNORECASE,
)

_last_arxiv_call = 0.0


def norm_text(s: str) -> str:
    """Minuscules, sans diacritiques, tirets = espaces, blancs normalisés."""
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return " ".join(s.replace("-", " ").lower().split())


def author_matches(cited: str, resolved_names: list[str]) -> bool:
    """Le nom cité doit apparaître comme suite contiguë de mots du 1er auteur résolu.

    `resolved_names` : variantes du premier auteur (nom complet, nom de famille seul).
    Ex. « Jiménez Gutiérrez » ⊂ « Bernal Jiménez Gutiérrez » ; « Wu » ⊂ « Di Wu ».
    """
    cited_tokens = norm_text(cited).split()
    if not cited_tokens:
        return False
    for name in resolved_names:
        tokens = norm_text(name).split()
        n = len(cited_tokens)
        for i in range(len(tokens) - n + 1):
            if tokens[i : i + n] == cited_tokens:
                return True
    return False


def http_get(url: str, timeout: int = 25) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


# [AJOUT VALIDATION 10/08] Attentes avant chaque nouvel essai après un HTTP 429.
BACKOFF_429 = (5, 20, 45)


def fetch(url: str) -> tuple[bytes | None, str]:
    """Retourne (contenu, "") ou (None, motif). 404 = inconnu ; le reste = échec réseau.

    Un seul retry sur erreur réseau ordinaire. **429 : 4 tentatives espacées de 5 s, 20 s puis
    45 s** — [AJOUT VALIDATION 10/08], accord explicite de Sébastien avant la passe 6. arXiv et
    Semantic Scholar limitent par fenêtre glissante ; avec l'unique réessai à 5 s d'origine, une
    saturation passagère fabriquait des INTROUVABLE en masse sur des fiches inchangées (70 à la
    première passe 6 du 10/08). Temporisation mesurée par la session 12. Seule la politique de
    réessai change : la chaîne de résolution et la logique de verdict sont identiques, les
    passes restent comparables.
    """
    n = len(BACKOFF_429) + 1
    for attempt in range(1, n + 1):
        try:
            return http_get(url), ""
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None, "inconnu"
            if e.code == 429 and attempt < n:
                time.sleep(BACKOFF_429[attempt - 1])
                continue
            if attempt >= 2:
                return None, f"echec reseau (HTTP {e.code})"
        except Exception as e:  # URLError, timeout, SSL…
            if attempt >= 2:
                return None, f"echec reseau ({type(e).__name__})"
        time.sleep(2)
    return None, "echec reseau"


def resolve_arxiv(arxiv_id: str) -> tuple[dict | None, str]:
    """API arXiv. Respecte ~3 s entre appels (consigne arXiv)."""
    global _last_arxiv_call
    wait = 3.0 - (time.time() - _last_arxiv_call)
    if wait > 0:
        time.sleep(wait)
    _last_arxiv_call = time.time()

    url = f"https://export.arxiv.org/api/query?id_list={arxiv_id}&max_results=1"
    raw, err = fetch(url)
    if raw is None:
        return None, err
    try:
        ns = {"a": "http://www.w3.org/2005/Atom"}
        entry = ET.fromstring(raw).find("a:entry", ns)
        if entry is None:
            return None, "inconnu"
        title = " ".join((entry.findtext("a:title", "", ns)).split())
        authors = [a.findtext("a:name", "", ns) for a in entry.findall("a:author", ns)]
        if not title or title.lower() == "error" or not authors:
            return None, "inconnu"
        years = set()
        for field in ("a:published", "a:updated"):
            v = entry.findtext(field, "", ns)
            if len(v) >= 4 and v[:4].isdigit():
                years.add(int(v[:4]))
        return {"title": title, "first_author": authors[0], "years": years,
                "abstract": " ".join((entry.findtext("a:summary", "", ns)).split()),
                "api": "arxiv"}, ""
    except ET.ParseError:
        return None, "reponse illisible (arxiv)"


def resolve_crossref(doi: str) -> tuple[dict | None, str]:
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    raw, err = fetch(url)
    if raw is None:
        return None, err
    try:
        msg = json.loads(raw)["message"]
        titles = msg.get("title") or []
        authors = msg.get("author") or []
        years = set()
        for field in ("issued", "published-print", "published-online", "created"):
            parts = (msg.get(field) or {}).get("date-parts") or []
            if parts and parts[0] and parts[0][0]:
                years.add(int(parts[0][0]))
        if not authors:
            return None, "inconnu"
        first = authors[0]
        family = first.get("family", "")
        full = f"{first.get('given', '')} {family}".strip()
        abstract = re.sub(r"<[^>]+>", " ", msg.get("abstract") or "")
        return {"title": titles[0] if titles else "(sans titre)",
                "first_author": full or family, "family": family, "years": years,
                "abstract": " ".join(abstract.split()), "api": "crossref"}, ""
    except (json.JSONDecodeError, KeyError, TypeError):
        return None, "reponse illisible (crossref)"


def resolve_s2(external_id: str) -> tuple[dict | None, str]:
    """Semantic Scholar — external_id : 'arXiv:XXXX.XXXXX' ou 'DOI:10.x/...'."""
    url = ("https://api.semanticscholar.org/graph/v1/paper/"
           + urllib.parse.quote(external_id, safe=":/")
           + "?fields=title,year,authors,abstract")
    raw, err = fetch(url)
    if raw is None:
        return None, err
    try:
        data = json.loads(raw)
        authors = data.get("authors") or []
        if not data.get("title") or not authors:
            return None, "inconnu"
        years = {int(data["year"])} if data.get("year") else set()
        return {"title": data["title"], "first_author": authors[0].get("name", ""),
                "years": years, "abstract": data.get("abstract") or "", "api": "s2"}, ""
    except (json.JSONDecodeError, TypeError, ValueError):
        return None, "reponse illisible (s2)"


def resolve_citation(kind: str, ident: str) -> tuple[dict | None, str]:
    """Chaîne de résolution du plan §5 : arXiv → Crossref/DOI → Semantic Scholar."""
    motifs = []
    if kind == "arxiv":
        meta, err = resolve_arxiv(ident)
        if meta:
            return meta, ""
        motifs.append(f"arxiv: {err}")
        meta, err = resolve_s2(f"arXiv:{ident}")
    else:
        meta, err = resolve_crossref(ident)
        if meta:
            return meta, ""
        motifs.append(f"crossref: {err}")
        meta, err = resolve_s2(f"DOI:{ident}")
    if meta:
        return meta, ""
    motifs.append(f"s2: {err}")
    return None, " ; ".join(motifs)


def extract_citations(text: str) -> list[dict]:
    """Extrait les citations format §2 d'un texte de fiche."""
    out = []
    for m in CITATION_RE.finditer(text):
        # [AJOUT VALIDATION 11/08] le « > » du bloc-citation peut tomber dans le nom quand la
        # citation est coupée en fin de ligne d'en-tête : on le traite comme un blanc.
        author = " ".join(m.group(1).replace(">", " ").split())
        year = int(m.group(2))
        raw_id = "".join(m.group(3).split())
        if raw_id.lower().startswith("arxiv:"):
            kind, ident = "arxiv", raw_id[6:]
            # v1, v2… : la résolution se fait sur l'identifiant nu
            ident = re.sub(r"v\d+$", "", ident)
        else:
            kind, ident = "doi", raw_id[4:]
        out.append({
            "author": author, "year": year, "kind": kind, "ident": ident,
            "key": (norm_text(author), year, kind, ident.lower()),
            "display": f"[{author}, {year}, {'arXiv:' if kind == 'arxiv' else 'DOI:'}{ident}]",
            "pos": m.start(),
        })
    return out


def paragraph_around(text: str, pos: int, max_len: int = 700) -> str:
    """Le paragraphe (bloc entre lignes vides) contenant la position pos."""
    start = text.rfind("\n\n", 0, pos)
    start = 0 if start == -1 else start + 2
    end = text.find("\n\n", pos)
    end = len(text) if end == -1 else end
    para = " ".join(text[start:end].split())
    if len(para) > max_len:
        center = max(0, pos - start - max_len // 2)
        para = "…" + para[center : center + max_len] + "…"
    return para


def classify(cit: dict, meta: dict | None, motif: str) -> tuple[str, str]:
    """Retourne (statut, détail)."""
    if meta is None:
        return "INTROUVABLE", motif
    names = [meta["first_author"]]
    if meta.get("family"):
        names.append(meta["family"])
    problems = []
    if not author_matches(cit["author"], names):
        problems.append(f"1er auteur resolu « {meta['first_author']} » ≠ cite « {cit['author']} »")
    if meta["years"] and cit["year"] not in meta["years"]:
        problems.append(f"annee resolue {sorted(meta['years'])} ≠ citee {cit['year']}")
    if problems:
        return "DISCORDANTE", " ; ".join(problems)
    return "RESOLUE", f"{meta['title']} — {meta['first_author']} ({meta['api']})"


def load_counts() -> dict:
    if COUNT_PATH.exists():
        return json.loads(COUNT_PATH.read_text(encoding="utf-8"))
    return {"passes": []}


def run_gate(force_new_pass: bool = False) -> int:
    files = sorted(DIM_DIR.glob("*.md"))
    if not files:
        print(f"Aucune fiche dans {DIM_DIR}", file=sys.stderr)
        return 2

    today = date.today().isoformat()
    per_fiche: dict[str, dict] = {}
    cache: dict[tuple, tuple] = {}  # key -> (statut, detail, meta)

    for f in files:
        text = f.read_text(encoding="utf-8")
        cits = extract_citations(text)
        uniques: dict[tuple, dict] = {}
        for c in cits:
            uniques.setdefault(c["key"], c)
        non_verifie = len(re.findall(r"\[NON V[EÉ]RIFI[EÉ]", text, re.IGNORECASE))
        rows = []
        for key, c in sorted(uniques.items(), key=lambda kv: kv[1]["pos"]):
            if key not in cache:
                print(f"  resolution {c['display']} …", flush=True)
                meta, motif = resolve_citation(c["kind"], c["ident"])
                cache[key] = (*classify(c, meta, motif), meta)
            statut, detail, _ = cache[key]
            rows.append({"citation": c["display"], "statut": statut, "detail": detail})
        counts = {s: sum(1 for r in rows if r["statut"] == s)
                  for s in ("RESOLUE", "DISCORDANTE", "INTROUVABLE")}
        per_fiche[f.name] = {
            "occurrences": len(cits), "uniques": len(uniques),
            "non_verifie_markers": non_verifie, "rows": rows, **counts,
            "validable": counts["RESOLUE"] == len(uniques) and non_verifie == 0,
        }

    # ---- citations_count.json : une passe par jour, regression si baisse du compte unique
    data = load_counts()
    passes = data["passes"]
    if passes and passes[-1]["date"] == today and not force_new_pass:
        previous = passes[:-1]
        pass_num = passes[-1]["pass"]
        passes.pop()
    else:
        previous = list(passes)
        pass_num = (passes[-1]["pass"] + 1) if passes else 1
    regressions = []
    if previous:
        prev_fiches = previous[-1]["fiches"]
        for name, info in per_fiche.items():
            if name in prev_fiches and info["uniques"] < prev_fiches[name]["uniques"]:
                regressions.append(
                    f"{name} : {prev_fiches[name]['uniques']} → {info['uniques']} citations uniques")
    passes.append({
        "pass": pass_num, "date": today,
        "fiches": {n: {k: v for k, v in i.items() if k != "rows"}
                   for n, i in per_fiche.items()},
        "regressions": regressions,
    })
    COUNT_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                          encoding="utf-8")

    # ---- citations_report.md
    lines = [
        "# Rapport gate citations — É2bis (généré par tools/check_citations.py)",
        "",
        f"> Passe {pass_num} — {datetime.now().strftime('%d/%m/%Y %H:%M')}. "
        "Ne pas éditer à la main : relancer le script.",
        "> Match : identifiant résolu + 1er auteur + année (le format §2 ne porte pas de",
        "> titre — le titre résolu est affiché pour contrôle ; le sens est couvert par le",
        "> spot-check). Échec réseau = INTROUVABLE, jamais RESOLUE.",
        "> Dérogation (etat.md, session 2) : AI Act / RGPD cités en clair hors format §2,",
        "> volontairement absents de ce rapport.",
        "",
    ]
    if regressions:
        lines += ["## ⚠ REGRESSIONS", ""] + [f"- {r}" for r in regressions] + ["", ]
    lines += ["## Synthèse", "",
              "| Fiche | Citations uniques (occurrences) | RESOLUE | DISCORDANTE | "
              "INTROUVABLE | [NON VÉRIFIÉ] | Gate |",
              "|---|---|---|---|---|---|---|"]
    for name, info in per_fiche.items():
        gate = "**VALIDABLE**" if info["validable"] else "**NON-VERIFIE**"
        lines.append(
            f"| {name} | {info['uniques']} ({info['occurrences']}) | {info['RESOLUE']} "
            f"| {info['DISCORDANTE']} | {info['INTROUVABLE']} "
            f"| {info['non_verifie_markers']} | {gate} |")
    for name, info in per_fiche.items():
        lines += ["", f"## {name}", "", "| Citation | Statut | Détail (titre résolu — 1er auteur (api) / motif) |",
                  "|---|---|---|"]
        for r in info["rows"]:
            lines.append(f"| `{r['citation']}` | {r['statut']} | {r['detail']} |")
    REPORT_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")

    all_ok = all(i["validable"] for i in per_fiche.values())
    print(f"\nRapport : {REPORT_PATH.relative_to(ROOT)}")
    print(f"Comptes : {COUNT_PATH.relative_to(ROOT)}")
    for name, info in per_fiche.items():
        verdict = "VALIDABLE" if info["validable"] else "NON-VERIFIE"
        print(f"  {name}: {info['RESOLUE']}/{info['uniques']} RESOLUE -> {verdict}")
    if regressions:
        print("REGRESSIONS :", *regressions, sep="\n  ")
    return 0 if all_ok and not regressions else 1


def run_spot_check(n: int, seed: str | None) -> int:
    seed = seed or date.today().isoformat()
    files = sorted(DIM_DIR.glob("*.md"))
    pool: dict[tuple, dict] = {}
    for f in files:
        text = f.read_text(encoding="utf-8")
        for c in extract_citations(text):
            if c["key"] not in pool:
                c["fiche"] = f.name
                c["context"] = paragraph_around(text, c["pos"])
                pool[c["key"]] = c
    ordered = [pool[k] for k in sorted(pool)]
    import random
    sample = random.Random(seed).sample(ordered, min(n, len(ordered)))

    print(f"# Spot-check — graine « {seed} », {len(sample)} citations tirées "
          f"sur {len(ordered)} uniques\n")
    for i, c in enumerate(sample, 1):
        meta, motif = resolve_citation(c["kind"], c["ident"])
        print(f"## {i}. {c['display']}  — fiche {c['fiche']}")
        print(f"Contexte d'appel : {c['context']}")
        if meta:
            print(f"Titre résolu ({meta['api']}) : {meta['title']}")
            print(f"1er auteur : {meta['first_author']} — années : {sorted(meta['years'])}")
            print(f"Abstract : {meta['abstract'] or '(non fourni par l’API)'}")
        else:
            print(f"NON RÉSOLU : {motif}")
        print()
    return 0


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--spot-check", action="store_true",
                   help="tire N citations (graine = date) pour le jugement humain")
    p.add_argument("-n", type=int, default=5, help="taille du tirage spot-check (défaut 5)")
    p.add_argument("--seed", default=None,
                   help="graine du tirage (défaut : date du jour AAAA-MM-JJ)")
    p.add_argument("--nouvelle-passe", action="store_true",
                   help="force une passe NEUVE même si la dernière porte la date du jour "
                        "(sinon la passe du jour est remplacée et sa baseline perdue)")
    args = p.parse_args()
    if args.spot_check:
        return run_spot_check(args.n, args.seed)
    return run_gate(force_new_pass=args.nouvelle_passe)


if __name__ == "__main__":
    sys.exit(main())
