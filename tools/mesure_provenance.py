"""Mesure de provenance : quelle part d'un texte candidat vient de la dictée de Sébastien.

Garde 2 de l'audit de publiabilité (§6 bis) : « la voix de Sébastien d'abord — Claude coupe,
vérifie, ordonne ; il n'invente pas la phrase ». Cible : plus de la moitié des phrases du narratif
issues de la dictée. Ce script rend une mesure, pas une impression.

Règle. Une phrase du candidat « vient de la dictée » si au moins SEUIL_4GRAMMES (60 %) de ses
4-grammes de mots, après normalisation (minuscules, accents et ponctuation retirés), figurent
dans la dictée. Une phrase de moins de 4 mots est jugée sur son n-gramme unique (la phrase
entière). Les lignes en blockquote (« > ») sont exclues des deux textes : dans
dictee_narratif.md ce sont les notes de Claude, pas les mots de Sébastien.

Pourquoi des 4-grammes et pourquoi 60 % (choix de la constante, à ne pas modifier sans
re-étalonner) :
- n = 4 : mesuré le 05/09/2026 entre la page « L'ambition » du document d'arbitrage (prose de
  Claude sur le même sujet) et la dictée — n-grammes de la page présents dans la dictée :
  49,0 % des mots, 4,3 % des bigrammes, 0,2 % des trigrammes, 0,0 % des 4-grammes et des
  5-grammes. n = 4 est le plus petit n sans recouvrement par hasard ; un 5-gramme punirait plus
  vite la moindre correction d'une phrase courte. Étalonnage au niveau des phrases : la dictée
  contre elle-même = 100 %, la page « L'ambition » = 0 % (chiffres collés dans
  docs/cdc/relectures.md).
- 60 % : une coupe franche garde 100 % de ses 4-grammes ; recoller deux fragments coûte au plus
  3 4-grammes de couture ; changer un mot en coûte au plus 4. Une phrase de la longueur typique
  de la dictée (≈ 30 mots, 27 4-grammes) survit donc à une correction (≈ 0,85) ; une phrase courte
  (12 mots, 9 4-grammes) avec un mot changé au milieu tombe à 0,56 et compte comme Claude. L'erreur
  est du côté strict : la mesure sous-estime la part de dictée, jamais l'inverse — c'est le bon
  sens pour une garde dont la cible est un plancher.

Sortie : la part des phrases venant de la dictée, la liste des phrases « de Claude » (avec leur
part de 4-grammes et si le rédacteur les avait marquées ⟦ ⟧), le compte des marqueurs posés et
l'écart entre phrases de Claude mesurées et marqueurs.

Usage :
    python tools/mesure_provenance.py CANDIDAT DICTEE [--plages 6-49] [--plages-dictee 7-30]
                                        [--json sortie.json]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.mesure_tells import (  # noqa: E402
    _stdout_utf8,
    appliquer_plages,
    charger_lignes,
    mots,
    paragraphes,
    phrases,
)

SEUIL_4GRAMMES = 0.6
N_GRAMME = 4
MARQUEUR_OUVRANT = "⟦"
MARQUEUR_FERMANT = "⟧"
SEGMENT_MARQUE_RE = re.compile(r"⟦(.*?)⟧", re.DOTALL)
NON_ALNUM_RE = re.compile(r"[^a-z0-9]")


def normaliser_mot(mot: str) -> str:
    """minuscules, accents retirés (décomposition NFKD), tout sauf lettres et chiffres retiré."""
    decompose = unicodedata.normalize("NFKD", mot.lower())
    sans_accents = "".join(c for c in decompose if not unicodedata.combining(c))
    return NON_ALNUM_RE.sub("", sans_accents)


def jetons(texte: str) -> list[str]:
    return [j for j in (normaliser_mot(m) for m in mots(texte)) if j]


def paragraphes_utiles(texte: str) -> list[str]:
    """Paragraphes du texte, blockquotes exclus, marqueurs ⟦ ⟧ retirés."""
    sans_marqueurs = texte.replace(MARQUEUR_OUVRANT, "").replace(MARQUEUR_FERMANT, "")
    lignes = [li for li in sans_marqueurs.splitlines() if not li.lstrip().startswith(">")]
    return paragraphes(lignes)


def ngrammes_dictee(dictee: str, n: int = N_GRAMME) -> dict[int, set[tuple[str, ...]]]:
    """Tous les k-grammes (1 ≤ k ≤ n) de chaque paragraphe de la dictée."""
    index: dict[int, set[tuple[str, ...]]] = {k: set() for k in range(1, n + 1)}
    for para in paragraphes_utiles(dictee):
        j = jetons(para)
        for k in range(1, n + 1):
            for i in range(len(j) - k + 1):
                index[k].add(tuple(j[i : i + k]))
    return index


def part_ngrammes(jetons_phrase: list[str], index: dict[int, set], n: int = N_GRAMME) -> float:
    k = min(n, len(jetons_phrase))
    grams = [tuple(jetons_phrase[i : i + k]) for i in range(len(jetons_phrase) - k + 1)]
    return sum(g in index[k] for g in grams) / len(grams)


def _segments_marques(texte: str) -> list[str]:
    return [s for s in (" ".join(jetons(seg)) for seg in SEGMENT_MARQUE_RE.findall(texte)) if s]


def detailler(candidat: str, dictee: str, n: int = N_GRAMME) -> list[dict]:
    """Toutes les phrases du candidat, dans l'ordre : numéro, phrase sans marqueurs, part de
    n-grammes dans la dictée, marquée ⟦ ⟧ par le rédacteur ou non, venant de la dictée ou non."""
    index = ngrammes_dictee(dictee, n)
    segments = _segments_marques(candidat)
    detail: list[dict] = []
    numero = 0
    for para in paragraphes_utiles(candidat):
        for phrase in phrases(para):
            j = jetons(phrase)
            if not j:
                continue
            numero += 1
            part = part_ngrammes(j, index, n)
            cle = " ".join(j)
            detail.append(
                {
                    "numero": numero,
                    "phrase": phrase,
                    "part_4grammes": round(part, 3),
                    "marquee": any(cle in s or s in cle for s in segments),
                    "dictee": part >= SEUIL_4GRAMMES,
                }
            )
    return detail


def mesurer_provenance(candidat: str, dictee: str, n: int = N_GRAMME) -> dict:
    detail = detailler(candidat, dictee, n)
    total = len(detail)
    venant_dictee = sum(d["dictee"] for d in detail)
    de_claude = [
        {k: d[k] for k in ("numero", "phrase", "part_4grammes", "marquee")}
        for d in detail
        if not d["dictee"]
    ]
    marqueurs = candidat.count(MARQUEUR_OUVRANT)
    return {
        "phrases": total,
        "phrases_dictee": venant_dictee,
        "part_dictee": round(venant_dictee / total, 3) if total else 0.0,
        "seuil_4grammes": SEUIL_4GRAMMES,
        "n_gramme": n,
        "marqueurs": marqueurs,
        "marqueurs_fermants": candidat.count(MARQUEUR_FERMANT),
        "phrases_claude_mesurees": len(de_claude),
        "ecart_marqueurs_mesure": len(de_claude) - marqueurs,
        "phrases_claude_non_marquees": sum(not p["marquee"] for p in de_claude),
        "phrases_claude": de_claude,
    }


def rapport_markdown(titre: str, m: dict) -> str:
    pct = round(100 * m["part_dictee"], 1)
    lignes = [
        f"| Mesure ({titre}) | Valeur | Cible §6 bis |",
        "|---|---|---|",
        f"| Phrases venant de la dictée | {m['phrases_dictee']} / {m['phrases']} = {pct} % | > 50 % |",  # noqa: E501
        f"| Seuil (part de {m['n_gramme']}-grammes) | {m['seuil_4grammes']} | — |",
        f"| Marqueurs ⟦ ⟧ posés par le rédacteur | {m['marqueurs']} (fermants : {m['marqueurs_fermants']}) | = phrases de Claude |",  # noqa: E501
        f"| Phrases de Claude mesurées | {m['phrases_claude_mesurees']} | — |",
        f"| Écart mesure − marqueurs | {m['ecart_marqueurs_mesure']} | 0 |",
        f"| Phrases de Claude non marquées | {m['phrases_claude_non_marquees']} | 0 |",
    ]
    if m["phrases_claude"]:
        lignes.append("")
        lignes.append("Phrases de Claude (numéro, part de 4-grammes, marquage) :")
        for p in m["phrases_claude"]:
            etat = "marquée" if p["marquee"] else "NON MARQUÉE"
            lignes.append(f"{p['numero']}. ({p['part_4grammes']}, {etat}) {p['phrase']}")
    return "\n".join(lignes)


def main(argv: list[str] | None = None) -> int:
    _stdout_utf8()
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    p.add_argument("candidat", help="texte candidat (.md / .txt / .docx)")
    p.add_argument("dictee", help="la dictée (.md)")
    p.add_argument("--plages", default=None, help="lignes du candidat à garder, ex. 6-49")
    p.add_argument("--plages-dictee", default=None, help="lignes de la dictée à garder")
    p.add_argument("--json", default=None, help="écrire les mesures dans ce fichier JSON")
    args = p.parse_args(argv)
    chemin = Path(args.candidat)
    candidat = "\n".join(appliquer_plages(charger_lignes(chemin), args.plages))
    dictee = "\n".join(appliquer_plages(charger_lignes(Path(args.dictee)), args.plages_dictee))
    m = mesurer_provenance(candidat, dictee)
    m["fichier"] = chemin.name
    m["plages"] = args.plages
    m["dictee"] = Path(args.dictee).name
    print(rapport_markdown(chemin.name, m))
    if m["marqueurs"] != m["marqueurs_fermants"]:
        print("\nATTENTION : marqueurs ouvrants et fermants en nombre différent.")
    if args.json:
        Path(args.json).write_text(json.dumps(m, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\nJSON écrit : {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
