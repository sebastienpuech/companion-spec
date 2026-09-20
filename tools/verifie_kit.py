#!/usr/bin/env python
"""Contrôle mécanique du kit des juges — définitions et colonne « pistes ».

Le kit part à trois juges qui notent 56 lignes sans voir la notation de l'évaluateur 1.
Deux défauts mesurés le 07/09/2026 rendaient ce kit inutilisable : des définitions trop
longues qui mêlaient plusieurs capacités (36 / 56), et une colonne « ce qui s'en approche »
qui portait un verdict (48 / 56) — sur les 25 lignes qui annonçaient une absence,
l'évaluateur 1 avait mis « couvert » 0 fois. Ce script refuse le kit tant qu'un de ces deux
défauts subsiste.

Usage :
  python tools/verifie_kit.py
  python tools/verifie_kit.py --definitions FICHIER.json --tableau FICHIER.md
  python tools/verifie_kit.py --json rapport.json

Code de retour : 0 si tout passe, 1 si un seuil est franchi.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
DEFINITIONS = RACINE / "couverture" / "kit_definitions.json"
TABLEAU = RACINE / "couverture" / "kit_juges_tableau.md"

MAX_MOTS = 35
NB_LIGNES = 56

# Les 56 identifiants, figés depuis le 04/08/2026 : aucune ligne n'est scindée, ajoutée
# ni fusionnée — « 56 » est publié dans le narratif, le README et la bibliographie.
IDS_ATTENDUS = frozenset(f"D{n:02d}" for n in range(56))

# Formules qui livrent un verdict au juge au lieu de lui donner une piste. Chacune vient
# d'une occurrence réelle mesurée dans la colonne « ce qui s'en approche » du 04/09.
VERDICTS = [
    (r"\baucun(?:e|s|es)?\b", "aucun / aucune"),
    (r"\bpersonne\b", "personne"),
    (r"\brien\b", "rien"),
    (r"\bn['’]existe\b", "n'existe"),
    (r"\bne\s+\w+(?:\s+\w+)?\s+(?:pas|jamais|plus)\b", "ne … pas / jamais / plus"),
    (r"\bacquis\b", "acquis"),
    (r"\ben production\b", "en production"),
    (r"\bpar construction\b", "par construction"),
    (r"\bexactement le produit\b", "exactement le produit"),
    (r",\s*(?:mais|non)\b", ", mais / , non"),
    (r"\bseul(?:e|s|es)?\b", "seul"),
    (r"\breste (?:un sujet|dans|hors)\b", "reste un sujet / dans / hors"),
    # Négation elliptique, sans « ne » : c'est la forme la plus fréquente de la colonne du
    # 04/09 (« …, pas la qualité du lien », « sans mémoire longue », « hors socle relationnel »).
    # Un premier jeu de motifs sans elle mesurait 35 / 56 orientées là où la relecture du 07/09
    # en comptait 48 : c'est ce trou-là qui manquait.
    (r",\s*(?:pas|jamais|plus|sans)\b", ", pas / jamais / sans"),
    (r"\bsans\b", "sans"),
    (r"\bni\b", "ni"),
    (r"\bhors\b", "hors"),
    (r"\bnon\b", "non"),
]

MOT = re.compile(r"[0-9A-Za-zÀ-ÿ]")
# Une phrase de plus : un point (ou ! ?) suivi d'une espace et d'une majuscule.
COUPURE = re.compile(r"[.!?]\s+[A-ZÀ-Ý]")


def compte_mots(texte: str) -> int:
    """Les jetons qui portent au moins une lettre ou un chiffre. Un tiret seul n'en est pas un."""
    return sum(1 for j in texte.split() if MOT.search(j))


def phrases(texte: str) -> int:
    return 1 + len(COUPURE.findall(texte))


def verdicts_dans(texte: str) -> list[str]:
    trouves = []
    for motif, nom in VERDICTS:
        if re.search(motif, texte, re.IGNORECASE):
            trouves.append(nom)
    return trouves


def charge(chemin: Path) -> dict:
    return json.loads(chemin.read_text(encoding="utf-8"))


def controle(donnees: dict, tableau: str | None = None) -> dict:
    lignes = donnees["lignes"]
    ids = [ligne["id"] for ligne in lignes]
    rapport: dict = {
        "nb_lignes": len(lignes),
        "ids_manquants": sorted(IDS_ATTENDUS - set(ids)),
        "ids_en_trop": sorted(set(ids) - IDS_ATTENDUS),
        "ids_dupliques": sorted({i for i in ids if ids.count(i) > 1}),
        "trop_longues": [],
        "plusieurs_phrases": [],
        "verdicts": {},
        "sans_pistes": [],
        "absentes_du_tableau": [],
        "mots": {},
    }

    for ligne in lignes:
        ident = ligne["id"]
        definition = ligne["definition"]
        nb = compte_mots(definition)
        rapport["mots"][ident] = nb
        if nb > MAX_MOTS:
            rapport["trop_longues"].append((ident, nb))
        if phrases(definition) > 1:
            rapport["plusieurs_phrases"].append(ident)

        pistes = ligne.get("pistes", "").strip()
        if not pistes:
            rapport["sans_pistes"].append(ident)
        else:
            trouves = verdicts_dans(pistes)
            if trouves:
                rapport["verdicts"][ident] = trouves

        if tableau is not None and definition not in tableau:
            rapport["absentes_du_tableau"].append(ident)

    valeurs = sorted(rapport["mots"].values())
    milieu = len(valeurs) // 2
    rapport["mediane_mots"] = (
        0
        if not valeurs
        else (
            valeurs[milieu]
            if len(valeurs) % 2
            else (valeurs[milieu - 1] + valeurs[milieu]) / 2
        )
    )
    rapport["max_mots"] = max(valeurs) if valeurs else 0
    rapport["conforme"] = not (
        rapport["ids_manquants"]
        or rapport["ids_en_trop"]
        or rapport["ids_dupliques"]
        or rapport["nb_lignes"] != NB_LIGNES
        or rapport["trop_longues"]
        or rapport["plusieurs_phrases"]
        or rapport["verdicts"]
        or rapport["sans_pistes"]
        or rapport["absentes_du_tableau"]
    )
    return rapport


def texte_rapport(r: dict) -> str:
    out = [
        f"lignes : {r['nb_lignes']} / {NB_LIGNES}",
        f"définitions : médiane {r['mediane_mots']} mots, max {r['max_mots']} "
        f"(plafond {MAX_MOTS})",
        f"au-dessus du plafond : {len(r['trop_longues'])}",
        f"en plusieurs phrases : {len(r['plusieurs_phrases'])}",
        f"colonnes « pistes » portant un verdict : {len(r['verdicts'])} / {r['nb_lignes']}",
        f"colonnes « pistes » vides : {len(r['sans_pistes'])}",
    ]
    if r["ids_manquants"]:
        out.append(f"IDS MANQUANTS : {', '.join(r['ids_manquants'])}")
    if r["ids_en_trop"]:
        out.append(f"IDS EN TROP : {', '.join(r['ids_en_trop'])}")
    if r["ids_dupliques"]:
        out.append(f"IDS EN DOUBLE : {', '.join(r['ids_dupliques'])}")
    for ident, nb in r["trop_longues"]:
        out.append(f"  trop longue — {ident} : {nb} mots")
    for ident in r["plusieurs_phrases"]:
        out.append(f"  plusieurs phrases — {ident}")
    for ident, motifs in r["verdicts"].items():
        out.append(f"  verdict — {ident} : {', '.join(motifs)}")
    for ident in r["sans_pistes"]:
        out.append(f"  pistes vides — {ident}")
    for ident in r["absentes_du_tableau"]:
        out.append(f"  définition absente du tableau publié — {ident}")
    out.append("CONFORME" if r["conforme"] else "NON CONFORME")
    return "\n".join(out)


def page_de_relecture(donnees: dict, avant: dict, etats: dict) -> str:
    """Avant / après, ligne par ligne — la page que Sébastien lit pour valider les 56 cœurs."""
    ancienne = {lig["id"]: lig["approche"] for lig in avant["lignes"]}
    noms = {d["id"]: d["nom"] for d in etats["dimensions"]}
    out = [
        "# Les 56 définitions réécrites — à relire",
        "",
        "> Généré par `python tools/verifie_kit.py --relecture <sortie>`. Page de lecture, pas",
        "> une source : la source est `kit_definitions.json`, le tableau envoyé aux juges est",
        "> `kit_juges_tableau.md`.",
        "",
        "Pour chaque ligne : **ce qui sera noté** (le cœur, une phrase), puis en dessous ce que le",
        "juge lisait avant. Une seule question à se poser : *est-ce bien ça, le geste central ?*",
        "",
    ]
    for lig in donnees["lignes"]:
        i = lig["id"]
        out += [
            f"### {i} — {noms.get(i, '')}",
            "",
            f"**{lig['definition']}**",
            "",
            f"- *sous-parties (ne décident pas la note)* : {lig.get('sous_parties', '')}",
            f"- *pistes* : {lig.get('pistes', '')}",
            f"- *cœur pris dans* : `{lig['source']}`",
            f"- *avant, la colonne d'exemples disait* : « {ancienne.get(i, '—')} »",
            "",
        ]
    return "\n".join(out)


def main(argv: list[str] | None = None) -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    p.add_argument("--definitions", default=str(DEFINITIONS))
    p.add_argument("--tableau", default=str(TABLEAU))
    p.add_argument("--json", dest="sortie_json", default=None)
    p.add_argument("--relecture", default=None, help="écrit la page avant / après à relire")
    args = p.parse_args(argv)

    donnees = charge(Path(args.definitions))
    if args.relecture:
        pub = DEFINITIONS.parent
        page = page_de_relecture(
            donnees,
            charge(pub / "couverture_evaluateur1_2026-08-21.json"),
            charge(pub / "etats.json"),
        )
        Path(args.relecture).write_text(page + "\n", encoding="utf-8")
        print(f"page de relecture écrite : {args.relecture}")
    chemin_tableau = Path(args.tableau)
    tableau = chemin_tableau.read_text(encoding="utf-8") if chemin_tableau.exists() else None
    r = controle(donnees, tableau)
    print(texte_rapport(r))
    if args.sortie_json:
        Path(args.sortie_json).write_text(
            json.dumps(r, ensure_ascii=False, indent=2), encoding="utf-8"
        )
    return 0 if r["conforme"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
