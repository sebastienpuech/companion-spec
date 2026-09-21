#!/usr/bin/env python3
"""Import du dépôt `companion-spec` depuis la source privée.

Ce script est la seule voie d'entrée de la matière : rien ne se copie à la main. Il est
**idempotent** — le relancer sur une cible déjà remplie doit rendre exactement le même état —
et il prend le chemin de la source en argument, pour qu'un tiers puisse lire ce qu'il fait
sans avoir la source.

Quatre gestes, dans cet ordre :

1. **Copie** des 56 fiches `docs/cdc/dimensions/*.md` vers `dimensions/`, plus les pièces
   annexes (couverture, états, instruments, scripts). Le sha256 de chaque fiche est comparé
   entre source et cible : « identique » ou « caviardé (n substitutions) », jamais autre chose.
   L'essai (`docs/cdc/publication/narratif/essai.md` → `essai/essai.md`) est copié et
   comparé de la même manière, sans caviardage possible : tout écart est un défaut.
2. **Grep des interdits et des motifs PII** sur TOUTE la cible → `out/pii_rapport.md`. Le
   script **refuse de finir** tant qu'un motif trouvé n'est pas arbitré dans
   `decisions_pii.json` (verdict `garder` ou `caviarder`, avec sa raison). Chaque caviardage
   est journalisé.
3. **Régénération de la bibliographie** depuis les fiches de la CIBLE, avec la regex et la
   normalisation de `tools/check_citations.py` (le gate É2bis, copié tel quel aux chemins
   près). Comptes attendus, écrits dans le fichier produit : 1 722 occurrences,
   1 412 citations uniques par fiche, 1 203 identifiants distincts après dédup inter-fiches.
4. **Tableau de couverture** à 56 lignes depuis `couverture_evaluateur1_2026-08-21.json`.

Usage :

    python tools/importer_depuis_source.py --source C:/chemin/vers/projet-coach-cdc
    python tools/importer_depuis_source.py --source C:/chemin/vers/projet-coach-cdc --verifier

`--verifier` n'écrit rien : il recompare les sha256, recompte les citations, recompte les
lignes de couverture et rejoue le grep. C'est la commande à lancer pour contester l'état du
dépôt.

Ce que le script NE fait PAS : il ne relance aucune résolution réseau des citations (le gate
du 13/08/2026 est un résultat daté, rejouable par `tools/check_citations.py`), il n'ouvre
aucune base de données, et il ne réécrit jamais le contenu d'une fiche hors caviardage arbitré.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RACINE))

# Console Windows en cp1252 par défaut : sans ça, la première flèche « → » du compte rendu
# fait tomber le script sur un UnicodeEncodeError, après avoir déjà écrit dans la cible.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Comptes attendus — passe 11 du gate É2bis, 13/08/2026 (source : citations_count.json).
ATTENDU_OCCURRENCES = 1722
ATTENDU_UNIQUES_PAR_FICHE = 1412
ATTENDU_DISTINCTS = 1203
ATTENDU_FICHES = 56
ATTENDU_LIGNES_COUVERTURE = 56

# ------------------------------------------------------------------ ce qui se copie

# (chemin relatif dans la source, chemin relatif dans la cible)
PIECES = [
    ("docs/cdc/publication/couverture_evaluateur1_2026-08-21.json",
     "couverture/couverture_evaluateur1_2026-08-21.json"),
    ("docs/cdc/publication/kit_juges.md", "couverture/kit_juges.md"),
    ("docs/cdc/publication/kit_juges_tableau.md", "couverture/kit_juges_tableau.md"),
    ("docs/cdc/publication/kit_definitions.json", "couverture/kit_definitions.json"),
    ("docs/cdc/publication/etats.json", "etats/etats.json"),
    ("docs/cdc/publication/etats_rapport.md", "etats/etats_rapport.md"),
    ("docs/cdc/publication/mesures_prod.json", "instruments/mesures_prod.json"),
    ("docs/cdc/publication/mesures_prod.md", "instruments/mesures_prod.md"),
    ("docs/cdc/publication/instantane_etats_2026-09-20.json",
     "couverture/instantane_etats_2026-09-20.json"),
]

# L'essai se copie à part : comme les fiches, son sha256 est recomparé à chaque passage,
# `--verifier` compris. Trois recopies à la main le 21/09/2026 ont motivé ce geste.
ESSAI = ("docs/cdc/publication/narratif/essai.md", "essai/essai.md")

# Scripts copiés dans `tools/`. Deux retouches déclarées, et deux seulement :
#   - `from scripts.X import` devient `from tools.X import` (le paquet change de nom) ;
#   - les chemins par défaut pointent vers la disposition de CE dépôt.
# La logique de mesure n'est pas touchée ; `--verifier` recompare les comptes.
SCRIPTS = [
    "check_citations.py",
    "mesure_prod_cdc.py",
    "mesure_tells.py",
    "mesure_provenance.py",
    "accord_juges.py",
    "etats_cdc.py",
    "verifie_kit.py",
]

TESTS = [
    "test_mesure_prod_cdc.py",
    "test_mesure_tells.py",
    "test_mesure_provenance.py",
    "test_accord_juges.py",
    "test_etats_cdc.py",
    "test_verifie_kit.py",
]

# Réécritures appliquées aux scripts copiés (motif → remplacement), journalisées.
RETOUCHES_SCRIPTS = [
    (r"\bfrom scripts\.", "from tools."),
    (r"\bimport scripts\.", "import tools."),
    (r"\bscripts/([a-z_]+\.py)", r"tools/\1"),
    (r"\btests/([a-z_]+\.py)", r"tools/tests/\1"),
    (r"docs/cdc/dimensions", "dimensions"),
    (r"docs/cdc/publication/etats\.json", "etats/etats.json"),
    (r"docs/cdc/publication/mesures_prod\.json", "instruments/mesures_prod.json"),
    (r"docs/cdc/publication/", "couverture/"),
    (r'ROOT / "docs" / "cdc" / "dimensions"', 'ROOT / "dimensions"'),
    (r'RACINE / "docs" / "cdc" / "publication"', 'RACINE / "couverture"'),
    (r'ROOT / "docs" / "cdc" / "citations_report\.md"', 'ROOT / "out" / "citations_report.md"'),
    (r'ROOT / "docs" / "cdc" / "citations_count\.json"', 'ROOT / "out" / "citations_count.json"'),
    (r"mailto:[\w.+-]+@[\w-]+\.[\w.-]{2,}", "mailto:contact-via-github"),
]

# Réécriture propre aux tests : dans la source ils vivent dans `tests/`, ici dans
# `tools/tests/` ; la racine du dépôt est donc un cran plus haut (constaté le 21/09/2026,
# 5 tests en échec sur `etats.json` introuvable après l'import).
RETOUCHES_TESTS = [
    (r"Path\(__file__\)\.resolve\(\)\.parents\[1\]", "Path(__file__).resolve().parents[2]"),
]

# ------------------------------------------------------------------ interdits et PII

# LES MOTIFS NE SONT PAS DANS CE FICHIER, ET C'EST VOLONTAIRE.
#
# Jusqu'au 07/09/2026 ils y étaient écrits en clair : le nom de l'employeur, un prénom de
# tiers, un lieu privé, des chemins internes, et une phrase intime. Ce fichier étant copié
# dans le dépôt publié, le garde-fou publiait exactement les termes qu'il protège. Le défaut
# a été trouvé en relançant l'import le 07/09 ; le dépôt était encore privé, rien n'a fuité.
#
# La liste vit maintenant dans la source privée, en JSON (--motifs, par défaut
# `docs/cdc/publication/motifs_prives.json` sous la source). Ce dépôt-ci garde l'outil, sa
# logique et les CATÉGORIES cherchées, ce qui suffit pour auditer la méthode ; il ne garde
# aucun terme littéral. Un tiers qui veut rejouer le scan fournit sa propre liste, au même
# format : une liste d'objets {categorie, motif, casse_exacte}.
#
# Règle de fermeture : sans liste, l'import S'ARRÊTE. Il ne scanne jamais à vide, parce
# qu'un scan à vide rendrait « aucun motif trouvé » et signerait une cible non vérifiée.

CATEGORIES_ATTENDUES = (
    "employeur",
    "directeur-pays",
    "fratrie",
    "prenom-tiers",
    "lieu-prive",
    "phrase-intime",
    "chemin-interne",
    "objet-connecte",
    "courriel",
    "telephone",
    "adresse-postale",
    "nom-de-l-auteur",
)

MOTIFS: list[tuple[str, "re.Pattern[str]"]] = []


def charger_motifs(chemin: Path) -> list[tuple[str, "re.Pattern[str]"]]:
    """Lit la liste privée. Toute anomalie arrête l'import : jamais de scan à vide."""
    if not chemin.exists():
        raise SystemExit(
            f"ARRÊT : liste des motifs introuvable — {chemin}\n"
            "  Le scan de confidentialité ne tourne pas sans elle, et il ne tourne pas à vide.\n"
            "  Donner --motifs <fichier.json>, ou remettre le fichier à sa place dans la source."
        )
    donnees = json.loads(chemin.read_text(encoding="utf-8"))
    brut = donnees.get("motifs") or []
    if not brut:
        raise SystemExit(f"ARRÊT : liste des motifs vide — {chemin}")
    compiles = []
    for m in brut:
        drapeaux = 0 if m.get("casse_exacte") else re.IGNORECASE
        compiles.append((m["categorie"], re.compile(m["motif"], drapeaux)))
    manquantes = sorted(set(CATEGORIES_ATTENDUES) - {c for c, _ in compiles})
    if manquantes:
        raise SystemExit(
            f"ARRÊT : catégories absentes de la liste — {', '.join(manquantes)}\n"
            "  La liste fournie ne couvre pas ce que ce dépôt doit vérifier."
        )
    return compiles


EXTENSIONS_SCANNEES = {".md", ".json", ".py", ".txt", ".yml", ".yaml", ".toml"}
DOSSIERS_IGNORES = {".git", "out", "__pycache__", ".pytest_cache", ".venv"}


def sha256(chemin: Path) -> str:
    return hashlib.sha256(chemin.read_bytes()).hexdigest()


def fichiers_scannes(racine: Path) -> list[Path]:
    trouves = []
    for p in sorted(racine.rglob("*")):
        if not p.is_file() or p.suffix.lower() not in EXTENSIONS_SCANNEES:
            continue
        if any(part in DOSSIERS_IGNORES for part in p.relative_to(racine).parts):
            continue
        trouves.append(p)
    return trouves


# ------------------------------------------------------------------ 1. copie


def copier_fiches(source: Path, cible: Path, ecrire: bool) -> dict:
    src_dir = source / "docs" / "cdc" / "dimensions"
    dst_dir = cible / "dimensions"
    fiches = sorted(src_dir.glob("*.md"))
    if len(fiches) != ATTENDU_FICHES:
        raise SystemExit(f"ARRÊT : {len(fiches)} fiches dans la source, {ATTENDU_FICHES} attendues.")
    if ecrire:
        dst_dir.mkdir(parents=True, exist_ok=True)
    rapport = {"copiees": 0, "identiques": 0, "caviardees": [], "manquantes": []}
    for f in fiches:
        dst = dst_dir / f.name
        if ecrire:
            shutil.copy2(f, dst)
            rapport["copiees"] += 1
        if not dst.exists():
            rapport["manquantes"].append(f.name)
            continue
        if sha256(dst) == sha256(f):
            rapport["identiques"] += 1
        else:
            rapport["caviardees"].append(dst.name)
    return rapport


def copier_pieces(source: Path, cible: Path, ecrire: bool) -> list[str]:
    faits = []
    for rel_src, rel_dst in PIECES:
        src = source / rel_src
        dst = cible / rel_dst
        if not src.exists():
            raise SystemExit(f"ARRÊT : pièce absente de la source — {rel_src}")
        if ecrire:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)
        faits.append(rel_dst)
    return faits


def copier_essai(source: Path, cible: Path, ecrire: bool) -> str:
    """Copie l'essai (en mode import) puis compare : « identique », « différent » ou « absent »."""
    src = source / ESSAI[0]
    dst = cible / ESSAI[1]
    if not src.exists():
        raise SystemExit(f"ARRÊT : essai absent de la source — {ESSAI[0]}")
    if ecrire:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
    if not dst.exists():
        return "absent"
    return "identique" if sha256(dst) == sha256(src) else "différent"


def _retoucher(src: Path, en_plus: tuple = ()) -> tuple[bytes, int]:
    """Applique les retouches déclarées, en OCTETS.

    Passer par `read_text` / `write_text` retraduirait les fins de ligne : la source est en
    fins de ligne Unix, et sur Windows la copie ressortait en fins de ligne Windows — donc un
    diff de 206 lignes sur 206 pour deux mots changés, et une copie qu'on ne peut plus dire
    fidèle. On lit et on écrit des octets ; les retouches ne touchent aucun saut de ligne.
    """
    texte = src.read_bytes().decode("utf-8")
    retouches = 0
    for motif, remplacement in [*RETOUCHES_SCRIPTS, *en_plus]:
        texte, n = re.subn(motif, remplacement, texte)
        retouches += n
    return texte.encode("utf-8"), retouches


def copier_scripts(source: Path, cible: Path, ecrire: bool) -> list[dict]:
    faits = []
    for nom in SCRIPTS:
        src = source / "scripts" / nom
        dst = cible / "tools" / nom
        if not src.exists():
            raise SystemExit(f"ARRÊT : script absent de la source — scripts/{nom}")
        texte, retouches = _retoucher(src)
        if ecrire:
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(texte)
        faits.append({"fichier": f"tools/{nom}", "retouches": retouches})
    for nom in TESTS:
        src = source / "tests" / nom
        dst = cible / "tools" / "tests" / nom
        if not src.exists():
            raise SystemExit(f"ARRÊT : test absent de la source — tests/{nom}")
        texte, retouches = _retoucher(src, tuple(RETOUCHES_TESTS))
        if ecrire:
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(texte)
        faits.append({"fichier": f"tools/tests/{nom}", "retouches": retouches})
    return faits


# ------------------------------------------------------------------ 2. PII


def charger_decisions(cible: Path) -> dict:
    chemin = cible / "decisions_pii.json"
    if not chemin.exists():
        return {"verdicts": {}}
    return json.loads(chemin.read_text(encoding="utf-8"))


def scanner_pii(cible: Path) -> dict:
    """Groupe les occurrences par (motif, texte trouvé). Rien n'est modifié ici."""
    trouve: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for f in fichiers_scannes(cible):
        rel = f.relative_to(cible).as_posix()
        for num, ligne in enumerate(f.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            for nom, motif in MOTIFS:
                for m in motif.finditer(ligne):
                    trouve[(nom, m.group(0))].append(
                        {"fichier": rel, "ligne": num, "extrait": ligne.strip()[:160]}
                    )
    return trouve


def appliquer_caviardages(cible: Path, decisions: dict, ecrire: bool) -> list[dict]:
    """Applique les verdicts `caviarder`. Chaque substitution est rendue, jamais silencieuse."""
    journal = []
    a_caviarder = {
        cle: v for cle, v in decisions.get("verdicts", {}).items()
        if v.get("verdict") == "caviarder"
    }
    if not a_caviarder:
        return journal
    for f in fichiers_scannes(cible):
        texte = f.read_text(encoding="utf-8")
        original = texte
        for cle, v in a_caviarder.items():
            _, trouve = cle.split("::", 1)
            texte, n = re.subn(re.escape(trouve), v["remplacement"], texte)
            if n:
                journal.append({
                    "fichier": f.relative_to(cible).as_posix(),
                    "trouve": trouve,
                    "remplacement": v["remplacement"],
                    "occurrences": n,
                    "raison": v.get("raison", ""),
                })
        if ecrire and texte != original:
            f.write_text(texte, encoding="utf-8")
    return journal


def ecrire_rapport_pii(cible: Path, trouve: dict, decisions: dict) -> list[str]:
    """Écrit `out/pii_rapport.md` et rend la liste des motifs NON arbitrés."""
    verdicts = decisions.get("verdicts", {})
    non_arbitres = []
    lignes = [
        f"# Rapport PII et interdits — {date.today().isoformat()}",
        "",
        "Produit par `tools/importer_depuis_source.py`. Une ligne par (motif, texte trouvé).",
        "Le script refuse de finir tant qu'une ligne n'est pas arbitrée dans `decisions_pii.json`.",
        "",
        "| Motif | Texte trouvé | Occurrences | Fichiers | Verdict | Raison |",
        "|---|---|---|---|---|---|",
    ]
    for (nom, texte), occs in sorted(trouve.items()):
        cle = f"{nom}::{texte}"
        v = verdicts.get(cle)
        fichiers = sorted({o["fichier"] for o in occs})
        resume = ", ".join(fichiers[:4]) + (f" (+{len(fichiers) - 4})" if len(fichiers) > 4 else "")
        if v is None:
            non_arbitres.append(cle)
            verdict, raison = "**NON ARBITRÉ**", "—"
        else:
            verdict, raison = v["verdict"], v.get("raison", "")
        lignes.append(
            f"| {nom} | `{texte}` | {len(occs)} | {resume} | {verdict} | {raison} |"
        )
    lignes += ["", "## Détail des occurrences", ""]
    for (nom, texte), occs in sorted(trouve.items()):
        lignes.append(f"### {nom} — `{texte}` ({len(occs)})")
        lignes.append("")
        for o in occs[:40]:
            lignes.append(f"- `{o['fichier']}:{o['ligne']}` — {o['extrait']}")
        if len(occs) > 40:
            lignes.append(f"- … et {len(occs) - 40} autres")
        lignes.append("")
    (cible / "out").mkdir(exist_ok=True)
    (cible / "out" / "pii_rapport.md").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return non_arbitres


# ------------------------------------------------------------------ 3. bibliographie


def extraire_citations(dossier: Path) -> tuple[list, dict]:
    """Rejoue l'extraction du gate É2bis sur les fiches de la CIBLE.

    Rend (entrées dédupliquées, comptes). La clé d'unicité est celle du gate :
    (auteur normalisé, année, identifiant en minuscules).
    """
    # Import tardif, et voulu : `tools/check_citations.py` est lui-même copié par ce script
    # quelques lignes plus haut, au premier import du dépôt. L'importer en tête de fichier
    # rendrait le tout premier passage impossible.
    from tools.check_citations import CITATION_RE, norm_text

    par_cle: dict[tuple[str, str, str], dict] = {}
    occurrences = 0
    uniques_par_fiche = 0
    for f in sorted(dossier.glob("*.md")):
        texte = f.read_text(encoding="utf-8")
        vues = set()
        for m in CITATION_RE.finditer(texte):
            auteur, annee, ident = m.group(1), m.group(2), m.group(3)
            ident = re.sub(r"[\s>]+", "", ident)
            cle = (norm_text(auteur), annee, ident.lower())
            occurrences += 1
            vues.add(cle)
            entree = par_cle.setdefault(cle, {
                "auteur": auteur.strip(), "annee": annee, "identifiant": ident, "fiches": set()
            })
            entree["fiches"].add(f.stem)
        uniques_par_fiche += len(vues)
    comptes = {
        "occurrences": occurrences,
        "uniques_par_fiche": uniques_par_fiche,
        "distincts": len(par_cle),
    }
    return sorted(par_cle.values(), key=lambda e: (norm_text(e["auteur"]), e["annee"])), comptes


def ecrire_bibliographie(cible: Path, entrees: list, comptes: dict, ecrire: bool) -> dict:
    ecarts = []
    if comptes["occurrences"] != ATTENDU_OCCURRENCES:
        ecarts.append(f"occurrences {comptes['occurrences']} ≠ {ATTENDU_OCCURRENCES}")
    if comptes["uniques_par_fiche"] != ATTENDU_UNIQUES_PAR_FICHE:
        ecarts.append(
            f"uniques par fiche {comptes['uniques_par_fiche']} ≠ {ATTENDU_UNIQUES_PAR_FICHE}")
    if comptes["distincts"] != ATTENDU_DISTINCTS:
        ecarts.append(f"distincts {comptes['distincts']} ≠ {ATTENDU_DISTINCTS}")
    if not ecrire:
        return {"comptes": comptes, "ecarts": ecarts}

    arxiv = sum(1 for e in entrees if e["identifiant"].lower().startswith("arxiv"))
    doi = len(entrees) - arxiv
    lignes = [
        "# Bibliographie",
        "",
        "Régénérée depuis `dimensions/` par `tools/importer_depuis_source.py`, avec la regex et la",
        "normalisation de `tools/check_citations.py` — le gate qui a vérifié ces citations une à une.",
        "Ce fichier ne s'édite pas à la main : il se régénère.",
        "",
        "## Les comptes",
        "",
        "| Compte | Valeur | Ce que c'est |",
        "|---|---|---|",
        f"| Occurrences | {comptes['occurrences']} | chaque fois qu'une citation apparaît dans une fiche |",
        f"| Citations uniques par fiche | {comptes['uniques_par_fiche']} | dédupliquées à l'intérieur de chaque fiche, additionnées sur les 56 |",
        f"| Identifiants distincts | {comptes['distincts']} | dédupliqués entre les fiches — les entrées ci-dessous |",
        f"| dont arXiv / DOI | {arxiv} / {doi} | |",
        "",
        "**Résolution.** Les 1 412 citations uniques par fiche ont été résolues par le gate le",
        "13/08/2026 (passe 11) : **1 412 RESOLUE, 0 DISCORDANTE, 0 INTROUVABLE, 0 REGRESSION**.",
        "« Résolue » veut dire : l'identifiant existe chez arXiv, Crossref ou Semantic Scholar, et",
        "le premier auteur ET l'année concordent avec ce que la fiche écrit. Un échec réseau n'a",
        "jamais compté comme résolu. Ce statut est un résultat **daté**, pas une promesse : pour le",
        "rejouer aujourd'hui, `python tools/check_citations.py` (il faut un accès réseau, comptez",
        "une vingtaine de minutes).",
        "",
        "**Ce que le gate ne vérifie pas** : le titre (le format de citation n'en porte pas) ni",
        "l'adéquation entre ce que la fiche affirme et ce que le papier dit. Cette seconde",
        "vérification a été faite par tirage au sort à chaque lot (les `spot_check`), pas sur les",
        "1 412. Voir `note_methode.md`.",
        "",
        "## Les entrées",
        "",
        "Format : `[Auteur, année, identifiant]`, puis les fiches qui la citent.",
        "",
        "| Auteur (tel que cité) | Année | Identifiant | Fiches |",
        "|---|---|---|---|",
    ]
    for e in entrees:
        fiches = ", ".join(sorted(f.split("-")[0] for f in e["fiches"]))
        lignes.append(f"| {e['auteur']} | {e['annee']} | `{e['identifiant']}` | {fiches} |")
    lignes.append("")
    (cible / "bibliographie.md").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return {"comptes": comptes, "ecarts": ecarts}


# ------------------------------------------------------------------ 4. couverture


def ecrire_tableau_couverture(cible: Path, ecrire: bool) -> dict:
    src = cible / "couverture" / "couverture_evaluateur1_2026-08-21.json"
    d = json.loads(src.read_text(encoding="utf-8"))
    lignes_src = d["lignes"]
    comptes = {"couvert": 0, "partiel": 0, "absent": 0}
    for lig in lignes_src:
        comptes[lig["couverture"]] += 1
    if not ecrire:
        return {"nb_lignes": len(lignes_src), "comptes": comptes}

    out = [
        "# Tableau de couverture — les 56 lignes contre les systèmes publics",
        "",
        "**Notation d'un seul évaluateur** : Claude, le 21/08/2026, source",
        "`couverture/couverture_evaluateur1_2026-08-21.json`. Ce n'est pas un fait établi, c'est",
        "un verdict à contester : deux juges de plus doivent noter les mêmes 56 lignes à l'aveugle",
        "(`couverture/kit_juges.md`), et les comptes publiés seront ceux du vote majoritaire.",
        "La colonne « ce qui s'en approche le plus » est la proposition de l'évaluateur 1 ; elle se",
        "contredit (`couverture/contester_une_ligne.md`).",
        "",
        "**L'échelle, trois valeurs.** `couvert` : un système public déployé, disponible aujourd'hui",
        "au grand public, fait le **cœur** de la ligne tel que la fiche le définit. `partiel` : il en",
        "fait une partie, ou le fait sans la durée, la profondeur ou l'initiative que la fiche exige.",
        "`absent` : aucun système public ne le fait — un papier de recherche ou une démo ne comptent",
        "pas.",
        "",
        f"**Comptes de l'évaluateur 1** : {comptes['couvert']} couvert · {comptes['partiel']} partiel"
        f" · {comptes['absent']} absent, sur {len(lignes_src)} lignes.",
        "",
        "| # | Bloc | Ligne | Ce qui s'en approche le plus (à contester) | Évaluateur 1 | Juge 2 | Juge 3 |",
        "|---|---|---|---|---|---|---|",
    ]
    for lig in lignes_src:
        approche = lig.get("approche", "").replace("|", "\\|")
        out.append(
            f"| {lig['id']} | {lig['bloc']} | {lig['nom']} | {approche} | "
            f"{lig['couverture']} | | |"
        )
    out += [
        "",
        "## Comment ce tableau se rejoue",
        "",
        "```bash",
        "python tools/importer_depuis_source.py --source <chemin/vers/la/source> --verifier",
        "```",
        "",
        "Le dépouillement des trois juges, une fois les deux feuilles reçues :",
        "",
        "```bash",
        "python tools/accord_juges.py couverture/notes_juges.json --json couverture/accord_juges.json",
        "```",
        "",
        "Il rend le κ de Fleiss, l'accord par paire et les lignes en désaccord. Le κ publié sera",
        "celui de la **première** passe, avant toute discussion — c'est écrit dans `kit_juges.md`.",
    ]
    (cible / "couverture" / "tableau_couverture.md").write_text("\n".join(out) + "\n",
                                                                encoding="utf-8")
    return {"nb_lignes": len(lignes_src), "comptes": comptes}


# ------------------------------------------------------------------ orchestration


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--source", required=True,
                   help="racine du dépôt source (worktree projet-coach-cdc)")
    p.add_argument("--verifier", action="store_true",
                   help="ne rien écrire ; recomparer, recompter, rejouer le grep")
    p.add_argument("--motifs", default=None,
                   help="liste privée des motifs du scan (JSON) ; par défaut "
                        "docs/cdc/publication/motifs_prives.json sous la source. "
                        "Sans elle, l'import s'arrête : il ne scanne jamais à vide.")
    args = p.parse_args()

    source = Path(args.source).resolve()
    cible = RACINE
    if not (source / "docs" / "cdc" / "dimensions").is_dir():
        raise SystemExit(f"ARRÊT : pas de docs/cdc/dimensions sous {source}")

    global MOTIFS
    chemin_motifs = (
        Path(args.motifs).resolve()
        if args.motifs
        else source / "docs" / "cdc" / "publication" / "motifs_prives.json"
    )
    MOTIFS = charger_motifs(chemin_motifs)
    ecrire = not args.verifier
    mode = "IMPORT" if ecrire else "VÉRIFICATION"
    print(f"== {mode} == source : {source}\n== cible  : {cible}\n")

    fiches = copier_fiches(source, cible, ecrire)
    print(f"[1/4] fiches      : {fiches['identiques']} identiques, "
          f"{len(fiches['caviardees'])} caviardées, {len(fiches['manquantes'])} manquantes")
    if fiches["caviardees"]:
        for nom in fiches["caviardees"]:
            print(f"        caviardée : {nom}")

    essai = copier_essai(source, cible, ecrire)
    print(f"        essai     : {essai} ({ESSAI[1]})")

    if ecrire:
        copier_pieces(source, cible, ecrire)
        retouches = copier_scripts(source, cible, ecrire)
        total = sum(r["retouches"] for r in retouches)
        print(f"        pièces et scripts copiés ({total} retouches de chemin, déclarées)")

    decisions = charger_decisions(cible)
    caviardages = appliquer_caviardages(cible, decisions, ecrire)
    for c in caviardages:
        print(f"        caviardage : {c['fichier']} — « {c['trouve']} » → "
              f"« {c['remplacement'] }» ({c['occurrences']}×)")

    trouve = scanner_pii(cible)  # MOTIFS chargé plus haut ; jamais vide (charger_motifs)
    non_arbitres = ecrire_rapport_pii(cible, trouve, decisions)
    print(f"[2/4] PII         : {len(trouve)} motifs distincts, "
          f"{sum(len(v) for v in trouve.values())} occurrences → out/pii_rapport.md")

    entrees, comptes = extraire_citations(cible / "dimensions")
    biblio = ecrire_bibliographie(cible, entrees, comptes, ecrire)
    print(f"[3/4] citations   : {comptes['occurrences']} occurrences, "
          f"{comptes['uniques_par_fiche']} uniques par fiche, "
          f"{comptes['distincts']} distincts")

    couv = ecrire_tableau_couverture(cible, ecrire)
    print(f"[4/4] couverture  : {couv['nb_lignes']} lignes — "
          + " · ".join(f"{v} {k}" for k, v in couv["comptes"].items()))

    print()
    defauts = []
    if fiches["manquantes"]:
        defauts.append(f"{len(fiches['manquantes'])} fiches manquantes")
    if essai != "identique":
        defauts.append(f"essai {essai} de la source")
    if biblio["ecarts"]:
        defauts += biblio["ecarts"]
    if couv["nb_lignes"] != ATTENDU_LIGNES_COUVERTURE:
        defauts.append(f"couverture {couv['nb_lignes']} lignes ≠ {ATTENDU_LIGNES_COUVERTURE}")
    if non_arbitres:
        print(f"ARRÊT : {len(non_arbitres)} motif(s) PII non arbitré(s) dans decisions_pii.json :")
        for cle in non_arbitres:
            print(f"  - {cle}")
        print("\nSébastien tranche chaque ligne (garder / caviarder + raison), puis on relance.")
        return 2
    if defauts:
        print("ARRÊT : " + " ; ".join(defauts))
        return 1
    print("CONFORME : 56/56 fiches, essai identique, 1 722 / 1 412 / 1 203 citations, 56 lignes de couverture, "
          "0 PII non arbitrée.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
