#!/usr/bin/env python3
"""Notes des juges en JSON — le format versionnable du kit.

`tools/accord_juges.py` lit un CSV. Le CSV ne peut pas être versionné ici : le garde-fou de
publication refuse toute extension non relisible en diff, et `couverture/kit_juges.md` le note
lui-même comme un trou à combler. Ce module est ce comblement, et rien d'autre — il ne touche
pas au calcul du κ, qui reste entier dans `accord_juges.py`.

Trois gestes :

    python tools/notes_juges.py --gabarit
        écrit `couverture/notes_juges.json` : 56 lignes, une par dimension, les colonnes des
        juges vides. C'est le fichier qu'on envoie à un juge et qu'il rend rempli.

    python tools/notes_juges.py --verifier couverture/notes_juges.json
        contrôle la forme : 56 lignes, pas de dimension manquante ni en double, valeurs dans
        {couvert, partiel, absent} ou vide, et une preuve pour tout `couvert` ou `partiel`
        (le kit l'exige : sans produit nommé, la note vaut `absent`).

    python tools/notes_juges.py --vers-csv couverture/notes_juges.json --sortie out/notes.csv
        convertit vers le CSV que `accord_juges.py` sait lire, hors dépôt.

Le format :

    {
      "date": "2026-09-…",
      "juges": {"juge1": "évaluateur 1 — …", "juge2": "…", "juge3": "…"},
      "lignes": [
        {"dimension": "D00 GARDE-FOUS",
         "juge1": "partiel", "juge1_preuve": "produit, version ou date, fonction précise",
         "juge2": "", "juge2_preuve": "",
         "juge3": "", "juge3_preuve": ""}
      ]
    }
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
CATEGORIES = ("couvert", "partiel", "absent")
DEFAUT_ETATS = RACINE / "etats" / "etats.json"
DEFAUT_NOTES = RACINE / "couverture" / "notes_juges.json"


def _stdout_utf8() -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def construire_gabarit(etats: Path, n_juges: int = 3) -> dict:
    data = json.loads(etats.read_text(encoding="utf-8"))
    dims = data["dimensions"] if isinstance(data, dict) else data
    lignes = []
    for d in dims:
        ligne = {"dimension": f"{d['id']} {d['nom']}"}
        for i in range(n_juges):
            ligne[f"juge{i + 1}"] = ""
            ligne[f"juge{i + 1}_preuve"] = ""
        lignes.append(ligne)
    return {
        "date": "",
        "juges": {f"juge{i + 1}": "" for i in range(n_juges)},
        "consignes": "couverture/kit_juges.md — à l'aveugle, trois valeurs, une preuve pour "
                     "tout couvert ou partiel, la valeur la plus basse en cas de doute.",
        "lignes": lignes,
    }


def noms_juges(notes: dict) -> list[str]:
    if notes.get("juges"):
        return list(notes["juges"])
    premiere = notes["lignes"][0]
    return [c for c in premiere if c.startswith("juge") and not c.endswith("_preuve")]


def verifier(notes: dict, attendu: int = 56) -> list[str]:
    """Rend la liste des défauts de forme. Liste vide = le fichier est exploitable."""
    defauts = []
    lignes = notes.get("lignes", [])
    if len(lignes) != attendu:
        defauts.append(f"{len(lignes)} lignes, {attendu} attendues")
    vues = set()
    for lig in lignes:
        dim = lig.get("dimension", "").strip()
        if not dim:
            defauts.append("une ligne sans dimension")
            continue
        if dim in vues:
            defauts.append(f"dimension en double : {dim}")
        vues.add(dim)
        for juge in noms_juges(notes):
            val = (lig.get(juge) or "").strip().lower()
            if val and val not in CATEGORIES:
                defauts.append(f"{dim} / {juge} : valeur « {val} » hors {CATEGORIES}")
            if val in ("couvert", "partiel") and not (lig.get(f"{juge}_preuve") or "").strip():
                defauts.append(f"{dim} / {juge} : « {val} » sans preuve — le kit la rend obligatoire")
    return defauts


def vers_csv(notes: dict, sortie: Path) -> int:
    juges = noms_juges(notes)
    sortie.parent.mkdir(parents=True, exist_ok=True)
    with sortie.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["dimension"] + juges)
        for lig in notes["lignes"]:
            w.writerow([lig["dimension"]] + [(lig.get(j) or "").strip().lower() for j in juges])
    return len(notes["lignes"])


def main(argv: list[str] | None = None) -> int:
    _stdout_utf8()
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--gabarit", action="store_true", help="écrire le gabarit vide")
    p.add_argument("--verifier", help="contrôler la forme d'un fichier de notes")
    p.add_argument("--vers-csv", dest="vers_csv", help="convertir un fichier de notes en CSV")
    p.add_argument("--etats", default=str(DEFAUT_ETATS))
    p.add_argument("--sortie", default=None)
    args = p.parse_args(argv)

    if args.gabarit:
        sortie = Path(args.sortie) if args.sortie else DEFAUT_NOTES
        gabarit = construire_gabarit(Path(args.etats))
        sortie.parent.mkdir(parents=True, exist_ok=True)
        sortie.write_text(json.dumps(gabarit, ensure_ascii=False, indent=2) + "\n",
                          encoding="utf-8")
        print(f"Gabarit écrit : {sortie} ({len(gabarit['lignes'])} lignes)")
        return 0

    if args.verifier:
        notes = json.loads(Path(args.verifier).read_text(encoding="utf-8"))
        defauts = verifier(notes)
        if defauts:
            print(f"{len(defauts)} défaut(s) :")
            for d in defauts:
                print(f"  - {d}")
            return 1
        print(f"Forme conforme : {len(notes['lignes'])} lignes, "
              f"juges {', '.join(noms_juges(notes))}.")
        return 0

    if args.vers_csv:
        notes = json.loads(Path(args.vers_csv).read_text(encoding="utf-8"))
        sortie = Path(args.sortie) if args.sortie else RACINE / "out" / "notes_juges.csv"
        n = vers_csv(notes, sortie)
        print(f"CSV écrit : {sortie} ({n} lignes) — "
              f"puis : python tools/accord_juges.py {sortie}")
        return 0

    p.error("donner --gabarit, --verifier ou --vers-csv")
    return 2


if __name__ == "__main__":
    sys.exit(main())
