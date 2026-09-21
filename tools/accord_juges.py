#!/usr/bin/env python3
"""Accord entre juges sur le tableau de couverture (correction 3 de l'audit du 03/09/2026).

Trois juges notent chacune des 56 dimensions du cahier des charges en « couvert », « partiel »
ou « absent » (couverture par les systèmes publics déployés). Ce script calcule :
  - le κ de Fleiss (n juges, k catégories) ;
  - l'accord brut moyen par paire de juges ;
  - l'accord ligne à ligne : unanimité / majorité / désaccord, avec la liste des lignes
    en désaccord ;
  - le compte couvert / partiel / absent par juge, et par vote majoritaire.

Entrée : un CSV (séparateur « ; », encodage UTF-8) avec l'en-tête `dimension;juge1;juge2;juge3`
(autant de colonnes juge que de juges), une ligne par dimension. Casse ignorée. Une cellule vide
= dimension non notée par ce juge : la ligne est écartée du κ et comptée à part.

Usage :
  python tools/accord_juges.py NOTES.csv [--json SORTIE]
  python tools/accord_juges.py --gabarit etats/etats.json --sortie NOTES.csv
    (écrit un CSV vide à remplir, une ligne par dimension, dans l'ordre D00…D55)
"""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from collections import Counter
from itertools import combinations
from pathlib import Path

CATEGORIES = ("couvert", "partiel", "absent")


def kappa_fleiss(matrice: list[list[int]]) -> float:
    """κ de Fleiss depuis la matrice n_ij (une ligne par sujet, une colonne par catégorie).

    Toutes les lignes doivent porter le même nombre de notes n ≥ 2.
    """
    if not matrice:
        return float("nan")
    n = sum(matrice[0])
    if n < 2 or any(sum(lig) != n for lig in matrice):
        raise ValueError("chaque sujet doit porter le même nombre de notes (n ≥ 2)")
    N = len(matrice)
    k = len(matrice[0])
    p_j = [sum(lig[j] for lig in matrice) / (N * n) for j in range(k)]
    P_i = [(sum(x * x for x in lig) - n) / (n * (n - 1)) for lig in matrice]
    P_bar = sum(P_i) / N
    P_e = sum(p * p for p in p_j)
    if math.isclose(P_e, 1.0):
        return 1.0 if math.isclose(P_bar, 1.0) else float("nan")
    return (P_bar - P_e) / (1 - P_e)


def lire_notes(chemin: Path) -> tuple[list[str], list[dict[str, str]]]:
    with chemin.open(encoding="utf-8", newline="") as f:
        lecteur = csv.DictReader(f, delimiter=";")
        juges = [c for c in lecteur.fieldnames if c.lower() != "dimension"]
        lignes = []
        for row in lecteur:
            notes = {j: (row.get(j) or "").strip().lower() for j in juges}
            lignes.append({"dimension": row["dimension"].strip(), **notes})
    return juges, lignes


def analyser(juges: list[str], lignes: list[dict[str, str]], categories: tuple[str, ...] = CATEGORIES) -> dict:  # noqa: E501
    completes, incompletes, invalides = [], [], []
    for lig in lignes:
        notes = [lig[j] for j in juges]
        if any(n == "" for n in notes):
            incompletes.append(lig["dimension"])
        elif any(n not in categories for n in notes):
            invalides.append(lig["dimension"])
        else:
            completes.append(lig)
    matrice = [[sum(1 for j in juges if lig[j] == c) for c in categories] for lig in completes]
    kappa = kappa_fleiss(matrice) if completes else float("nan")

    accord_paires = {}
    for a, b in combinations(juges, 2):
        d = sum(1 for lig in completes if lig[a] == lig[b])
        accord_paires[f"{a}~{b}"] = round(d / len(completes), 3) if completes else None
    accord_brut_moyen = (
        round(sum(v for v in accord_paires.values()) / len(accord_paires), 3)
        if accord_paires and completes
        else None
    )

    unanimite, majorite, desaccord = 0, 0, []
    vote_majoritaire = Counter()
    for lig in completes:
        c = Counter(lig[j] for j in juges)
        cat, n = c.most_common(1)[0]
        if n == len(juges):
            unanimite += 1
        elif n > len(juges) / 2:
            majorite += 1
        else:
            desaccord.append(lig["dimension"])
        if n > len(juges) / 2:
            vote_majoritaire[cat] += 1
        else:
            vote_majoritaire["sans majorité"] += 1

    par_juge = {j: {c: sum(1 for lig in completes if lig[j] == c) for c in categories} for j in juges}  # noqa: E501
    return {
        "juges": juges,
        "categories": list(categories),
        "lignes_notees": len(completes),
        "lignes_incompletes": incompletes,
        "lignes_invalides": invalides,
        "kappa_fleiss": None if math.isnan(kappa) else round(kappa, 3),
        "accord_par_paire": accord_paires,
        "accord_brut_moyen": accord_brut_moyen,
        "unanimite": unanimite,
        "majorite": majorite,
        "desaccord": desaccord,
        "comptes_par_juge": par_juge,
        "comptes_vote_majoritaire": dict(vote_majoritaire),
    }


def verifier_completude(
    juges: list[str],
    lignes: list[dict[str, str]],
    categories: tuple[str, ...] = CATEGORIES,
    seuil: float = 0.9,
) -> dict:
    """G14 — refus de publier un κ si moins de 90 % des lignes attendues portent une entrée
    par juge (BUD-4). N'entre PAS dans le calcul de kappa_fleiss ni de `analyser()` : c'est une
    vérification à part, appliquée par l'appelant (CLI) avant publication.

    `lignes_attendues` est le nombre total de lignes du fichier d'entrée (une ligne = une
    dimension attendue). Pour chaque juge, `lignes_classees_par_juge` compte les entrées à
    catégorie valide (non vide, dans `categories`). `publiable` est faux dès qu'un seul juge
    est sous le seuil.
    """
    lignes_attendues = len(lignes)
    lignes_classees_par_juge = {
        j: sum(1 for lig in lignes if lig.get(j, "") in categories) for j in juges
    }
    publiable = lignes_attendues > 0 and all(
        (lignes_classees_par_juge[j] / lignes_attendues) >= seuil for j in juges
    )
    return {
        "lignes_attendues": lignes_attendues,
        "lignes_classees_par_juge": lignes_classees_par_juge,
        "seuil": seuil,
        "publiable": publiable,
    }


def rapport_ou_partiel(r: dict, completude: dict) -> str:
    """G14 : si `completude['publiable']` est faux, publie UNIQUEMENT « κ partiel, n=<compte> »
    (BUD-4) — jamais le tableau complet, qui laisserait croire à un classement achevé. `n` est
    le nombre de lignes notées par TOUS les juges (`r['lignes_notees']`), la seule quantité
    encore fiable dans un classement interrompu à mi-parcours."""
    if not completude["publiable"]:
        return f"κ partiel, n={r['lignes_notees']}"
    return rapport_markdown(r)


def lecture_kappa(k: float | None) -> str:
    """Repères de Landis & Koch (1977) — indicatifs, publiés tels quels avec le chiffre."""
    if k is None:
        return "non calculable"
    if k < 0:
        return "pire que le hasard"
    if k < 0.2:
        return "faible"
    if k < 0.4:
        return "passable"
    if k < 0.6:
        return "modéré"
    if k < 0.8:
        return "substantiel"
    return "quasi parfait"


def rapport_markdown(r: dict) -> str:
    cats = r.get("categories", list(CATEGORIES))
    entete_cats = " / ".join(cats)
    lignes = [
        "| Mesure | Valeur |",
        "|---|---|",
        f"| Juges | {', '.join(r['juges'])} |",
        f"| Lignes notées par tous / incomplètes / invalides | {r['lignes_notees']} / {len(r['lignes_incompletes'])} / {len(r['lignes_invalides'])} |",  # noqa: E501
        f"| κ de Fleiss | {r['kappa_fleiss']} ({lecture_kappa(r['kappa_fleiss'])}) |",
        f"| Accord brut moyen par paire | {r['accord_brut_moyen']} |",
        f"| Unanimité / majorité / désaccord | {r['unanimite']} / {r['majorite']} / {len(r['desaccord'])} |",  # noqa: E501
        f"| Vote majoritaire {entete_cats} | "
        + " / ".join(str(r["comptes_vote_majoritaire"].get(c, 0)) for c in cats)
        + f" (sans majorité : {r['comptes_vote_majoritaire'].get('sans majorité', 0)}) |",
    ]
    for j, c in r["comptes_par_juge"].items():
        lignes.append(f"| {j} : {entete_cats} | " + " / ".join(str(c.get(cat, 0)) for cat in cats) + " |")  # noqa: E501
    if r["desaccord"]:
        lignes.append(f"| Lignes en désaccord | {', '.join(r['desaccord'])} |")
    if r["lignes_incompletes"]:
        lignes.append(f"| Lignes incomplètes | {', '.join(r['lignes_incompletes'])} |")
    return "\n".join(lignes)


def ecrire_gabarit(etats: Path, sortie: Path, n_juges: int = 3) -> int:
    data = json.loads(etats.read_text(encoding="utf-8"))
    dims = data["dimensions"] if isinstance(data, dict) else data
    with sortie.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["dimension"] + [f"juge{i + 1}" for i in range(n_juges)])
        for d in dims:
            w.writerow([f"{d['id']} {d['nom']}"] + [""] * n_juges)
    return len(dims)


def _stdout_utf8() -> None:
    """Console Windows en cp1252 : forcer UTF-8 pour les caractères du tableau."""
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, ValueError):
        pass


def main(argv: list[str] | None = None) -> int:
    _stdout_utf8()
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    p.add_argument("notes", nargs="?", help="CSV des notes (dimension;juge1;juge2;juge3)")
    p.add_argument("--json", default=None, help="écrire le résultat dans ce fichier JSON")
    p.add_argument("--gabarit", default=None, help="etats.json : écrire un CSV vide à remplir")
    p.add_argument("--sortie", default="kit_juges_notes.csv", help="chemin du CSV gabarit")
    p.add_argument(
        "--categories",
        default=None,
        help="catégories, séparées par des virgules (défaut : couvert,partiel,absent)",
    )
    p.add_argument(
        "--seuil-completude",
        type=float,
        default=0.9,
        help="seuil de remplissage par juge sous lequel le κ n'est pas publiable (G14, défaut 0,9)",
    )
    args = p.parse_args(argv)
    if args.gabarit:
        n = ecrire_gabarit(Path(args.gabarit), Path(args.sortie))
        print(f"Gabarit écrit : {args.sortie} ({n} lignes)")
        return 0
    if not args.notes:
        p.error("donner le CSV des notes, ou --gabarit")
    categories = (
        tuple(c.strip().lower() for c in args.categories.split(",")) if args.categories else CATEGORIES  # noqa: E501
    )
    juges, lignes = lire_notes(Path(args.notes))
    r = analyser(juges, lignes, categories=categories)
    completude = verifier_completude(juges, lignes, categories=categories, seuil=args.seuil_completude)  # noqa: E501
    print(rapport_ou_partiel(r, completude))
    if args.json:
        if completude["publiable"]:
            a_ecrire = r
        else:
            # G14 : rien d'autre que « κ partiel, n=… » ne se publie.
            a_ecrire = {
                "kappa_fleiss": None,
                "publiable": False,
                "message": rapport_ou_partiel(r, completude),
                "completude": completude,
            }
        Path(args.json).write_text(json.dumps(a_ecrire, ensure_ascii=False, indent=2), encoding="utf-8")  # noqa: E501
        print(f"\nJSON écrit : {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
