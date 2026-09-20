#!/usr/bin/env python3
"""Les cinq états des 56 dimensions — vérification, comptes par bloc, kit des juges.

Corrections 2, 3 et 9 de l'audit de publiabilité du 03/09/2026. Tout ce qui est compté ici sort
du script, jamais de la main (le rapport du 21/08 écrivait « 1 + 0 + 3 + 4 = 10 »).

Sous-commandes :
  importer-couverture SOURCE --sortie JSON
      Lit le tableau « Ligne à ligne » du rapport du 21/08/2026 (fichier .docx ou son texte
      extrait) et l'écrit en JSON comme NOTATION DE L'ÉVALUATEUR 1 (Claude, 21/08) — pas comme
      une source de faits (règle de fer n°6) : c'est la colonne que deux juges de plus vont
      contester avec le kit. Vérifie au passage que ses 8 blocs sont ceux de BLOCS.
  verifier --etats JSON --mesures JSON [--couverture JSON] [--md SORTIE]
      Vérifie etats.json (56 lignes D00-D55, états autorisés, « en service » ⇒ mesure non
      nulle, « outillé sans usage » ⇒ mesure nulle, « amorcé » ⇒ mesure non nulle) et calcule :
      comptes par état, par bloc et par état, couverture par bloc de l'évaluateur 1 (quel bloc
      l'industrie couvre le plus), les lignes « absent » avec leur état ici. Code de retour 1 si
      une règle est violée.
  kit --etats JSON --definitions JSON --sortie MD
      Écrit le tableau des 56 lignes du kit des juges : dimension, définition au cœur nommé,
      sous-parties non déterminantes, pistes à examiner, colonne vide « couvert / partiel /
      absent ». La source est kit_definitions.json, relu ligne à ligne (session 4 du 07/09/2026).
      **Pourquoi une source et non plus la fiche** : jusqu'au 07/09 cette sous-commande extrayait
      la première phrase de la « FICHE SYNTHÈSE » par une regex (`--fiches`, toujours acceptée
      pour rejouer l'ancien tableau). Cette extraction n'a jamais été relue : elle a produit
      36 / 56 définitions qui ne permettaient pas de trancher, et une colonne « ce qui s'en
      approche » qui portait un verdict sur 48 / 56 lignes. Nommer le cœur d'une capacité est un
      travail de jugement, pas une regex — il se versionne, il ne se devine pas.

La règle des cinq états (écrite ici parce que le rapport du 21/08 ne l'avait pas) :
  1. en service — le cœur de la dimension (mapping É3b §0.1) est couvert par du code en service
     ET une mesure de production NON NULLE (mesures_prod.json) en porte la trace.
  2. acquis sans code — obtenu par construction du cadre n = 1 (payeur = utilisateur =
     opérateur), sans artefact dédié ; aucune mesure ne peut le prouver ni l'infirmer : il se
     déclare, avec sa raison.
  3. outillé sans usage — un artefact dédié au cœur de la dimension existe dans le dépôt (table,
     tool, protocole, nommé dans inventaire_coach.md) et la mesure attachée est NULLE.
  4. amorcé — du code touche la dimension (inventaire « amorce » / « partiel ») avec une mesure
     non nulle, mais ne couvre pas son cœur.
  5. à construire — aucun artefact dédié, aucun code qui touche la dimension.
  Départage outillé / à construire : l'existence d'un artefact NOMMÉ dans le dépôt, à mesure
  nulle. Une consigne de prompt seule (persona) n'est pas un artefact (arbitrage du 13/08).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, OrderedDict
from pathlib import Path

ETATS = ("en service", "acquis sans code", "outillé sans usage", "amorcé", "à construire")
COUVERTURES = ("couvert", "partiel", "absent")

# Regroupement de lecture du rapport du 21/08 (8 blocs), repris tel quel comme ordre de lecture.
BLOCS: "OrderedDict[str, list[str]]" = OrderedDict(
    [
        ("Le cadre", ["D00", "D47", "D48"]),
        ("Mémoire et connaissance de la personne", ["D01", "D02", "D03", "D04", "D05", "D06"]),
        (
            "La qualité du lien",
            ["D07", "D08", "D09", "D10", "D11", "D12", "D13", "D14", "D15", "D16", "D17"],
        ),
        ("Tenir dans la durée", ["D18", "D19", "D20", "D21", "D22", "D26", "D40"]),
        ("Le compagnon comme sujet", ["D23", "D24", "D25", "D27"]),
        (
            "Présence : voix, corps, temps réel",
            ["D28", "D29", "D30", "D31", "D32", "D33", "D37", "D46"],
        ),
        ("Agir sur la vie", ["D34", "D35", "D36", "D38", "D39", "D41", "D42", "D43", "D44", "D45"]),
        ("Les sept incarnations", ["D49", "D50", "D51", "D52", "D53", "D54", "D55"]),
    ]
)
BLOC_DE = {d: b for b, ds in BLOCS.items() for d in ds}
IDS = [f"D{i:02d}" for i in range(56)]

# Répartition des 17 lignes absentes selon l'arbitrage É4 (audit du 03/09, §2.2) : la thèse en 12 / 17.  # noqa: E501
ABSENTES_E4 = OrderedDict(
    [
        ("acquise ou déjà en production", ["D45", "D47"]),
        (
            "faisable maintenant",
            ["D48", "D05", "D08", "D16", "D19", "D21", "D22", "D27", "D41", "D42"],
        ),
        ("terrain de recherche", ["D14", "D24", "D25"]),
        ("hors de portée", ["D35", "D44"]),
    ]
)

DIM_ID_RE = re.compile(r"\((D\d\d)\)")


# ---------------------------------------------------------------- lecture du tableau de B


def _lignes_source(chemin: Path) -> list[str]:
    if chemin.suffix.lower() == ".docx":
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        from mesure_tells import lignes_docx  # lecteur .docx sans dépendance

        return lignes_docx(chemin)
    return chemin.read_text(encoding="utf-8").splitlines()


def importer_couverture(chemin: Path) -> dict:
    lignes: list[dict] = []
    for lig in _lignes_source(chemin):
        if not lig.startswith("|"):
            continue
        cellules = [c.strip() for c in lig.strip().strip("|").split("|")]
        if len(cellules) != 4:
            continue
        m = DIM_ID_RE.search(cellules[1])
        if not m or cellules[3].lower() not in COUVERTURES:
            continue
        lignes.append(
            {
                "id": m.group(1),
                "bloc": cellules[0],
                "nom": DIM_ID_RE.sub("", cellules[1]).strip(),
                "approche": cellules[2],
                "couverture": cellules[3].lower(),
            }
        )
    ids = [lig["id"] for lig in lignes]
    ecarts_blocs = [
        f"{lig['id']} : « {lig['bloc']} » ≠ « {BLOC_DE.get(lig['id'])} »"
        for lig in lignes
        if lig["bloc"] != BLOC_DE.get(lig["id"])
    ]
    return {
        "source": chemin.name,
        "evaluateur": "évaluateur 1 — Claude, rapport du 21/08/2026 (évaluateur unique)",
        "date": "2026-08-21",
        "statut": "notation à contester par deux juges de plus (kit_juges.md) ; pas une source de faits",  # noqa: E501
        "nb_lignes": len(lignes),
        "manquantes": [d for d in IDS if d not in ids],
        "doublons": [d for d, n in Counter(ids).items() if n > 1],
        "ecarts_blocs": ecarts_blocs,
        "comptes": dict(Counter(lig["couverture"] for lig in lignes)),
        "lignes": lignes,
    }


# ---------------------------------------------------------------- vérification des états


def _valeur_mesure(mesures: dict, cle: str | None):
    if not cle:
        return None, None
    for m in mesures.get("mesures", []):
        if m["cle"] == cle:
            return m.get("valeur"), m.get("statut")
    return None, "inconnue"


def _non_nulle(v) -> bool:
    if isinstance(v, bool):
        return v
    if isinstance(v, (int, float)):
        return v > 0
    if isinstance(v, dict):
        return sum(v.values()) > 0
    return bool(v)


def verifier(etats: dict, mesures: dict, couverture: dict | None = None) -> dict:
    dims = etats["dimensions"]
    erreurs: list[str] = []
    ids = [d["id"] for d in dims]
    if sorted(ids) != IDS:
        erreurs.append(
            f"il faut exactement D00-D55 : {len(ids)} lignes, manquantes "
            f"{[d for d in IDS if d not in ids]}, doublons {[d for d, n in Counter(ids).items() if n > 1]}"  # noqa: E501
        )
    for d in dims:
        e = d.get("etat")
        if e not in ETATS:
            erreurs.append(f"{d['id']} : état « {e} » hors liste {ETATS}")
            continue
        v, statut = _valeur_mesure(mesures, d.get("mesure"))
        if e == "en service":
            if not d.get("mesure"):
                erreurs.append(f"{d['id']} en service sans mesure attachée")
            elif statut == "inconnue":
                erreurs.append(
                    f"{d['id']} en service : mesure « {d['mesure']} » absente de mesures_prod.json"
                )
            elif not _non_nulle(v):
                erreurs.append(
                    f"{d['id']} en service : mesure « {d['mesure']} » nulle ({v!r}) — règle : aucune mesure non nulle ⇒ pas « en service »"  # noqa: E501
                )
        elif e == "outillé sans usage":
            if not d.get("mesure"):
                erreurs.append(f"{d['id']} outillé sans usage : la mesure nulle doit être nommée")
            elif statut == "inconnue":
                erreurs.append(
                    f"{d['id']} outillé : mesure « {d['mesure']} » absente de mesures_prod.json"
                )
            elif _non_nulle(v):
                erreurs.append(
                    f"{d['id']} outillé sans usage : mesure « {d['mesure']} » non nulle ({v!r}) — c'est « amorcé » ou « en service »"  # noqa: E501
                )
            if not d.get("artefact"):
                erreurs.append(f"{d['id']} outillé sans usage : aucun artefact nommé")
        elif e == "amorcé":
            if not d.get("mesure"):
                erreurs.append(f"{d['id']} amorcé sans mesure attachée")
            elif statut == "inconnue":
                erreurs.append(
                    f"{d['id']} amorcé : mesure « {d['mesure']} » absente de mesures_prod.json"
                )
            elif not _non_nulle(v):
                erreurs.append(
                    f"{d['id']} amorcé : mesure « {d['mesure']} » nulle ({v!r}) — c'est « outillé sans usage »"  # noqa: E501
                )
        elif e == "acquis sans code" and not d.get("justification"):
            erreurs.append(f"{d['id']} acquis sans code : la raison doit être écrite")
        if not d.get("justification"):
            erreurs.append(f"{d['id']} : justification manquante")

    par_etat = Counter(d["etat"] for d in dims if d.get("etat") in ETATS)
    par_bloc: "OrderedDict[str, Counter]" = OrderedDict((b, Counter()) for b in BLOCS)
    for d in dims:
        b = BLOC_DE.get(d["id"])
        if b and d.get("etat") in ETATS:
            par_bloc[b][d["etat"]] += 1

    couverture_bloc = None
    absentes = None
    if couverture:
        couv_de = {lig["id"]: lig["couverture"] for lig in couverture["lignes"]}
        couverture_bloc = OrderedDict()
        for b, ds in BLOCS.items():
            c = Counter(couv_de.get(d, "non notée") for d in ds)
            couverture_bloc[b] = {k: c.get(k, 0) for k in COUVERTURES}
        etat_de = {d["id"]: d.get("etat") for d in dims}
        absentes = [{"id": i, "etat": etat_de.get(i)} for i in IDS if couv_de.get(i) == "absent"]
        attendues = [i for ids_ in ABSENTES_E4.values() for i in ids_]
        trouvees = [a["id"] for a in absentes]
        if sorted(trouvees) != sorted(attendues):
            erreurs.append(
                f"lignes « absent » de l'évaluateur 1 ≠ les 17 de l'arbitrage É4 : "
                f"en plus {sorted(set(trouvees) - set(attendues))}, en moins {sorted(set(attendues) - set(trouvees))}"  # noqa: E501
            )

    return {
        "ok": not erreurs,
        "erreurs": erreurs,
        "nb_dimensions": len(dims),
        "par_etat": {e: par_etat.get(e, 0) for e in ETATS},
        "par_bloc": {b: {e: c.get(e, 0) for e in ETATS} for b, c in par_bloc.items()},
        "couverture_evaluateur1_par_bloc": couverture_bloc,
        "absentes": absentes,
    }


def bloc_le_plus_couvert(couverture_bloc: dict) -> dict:
    """Le bloc où l'industrie couvre le plus : d'abord en « couvert », puis en couvert + partiel."""
    if not couverture_bloc:
        return {}
    par_couvert = sorted(
        couverture_bloc.items(),
        key=lambda kv: (-kv[1]["couvert"], -(kv[1]["couvert"] + kv[1]["partiel"])),
    )
    par_non_absent = sorted(
        couverture_bloc.items(),
        key=lambda kv: (-(kv[1]["couvert"] + kv[1]["partiel"]), -kv[1]["couvert"]),
    )
    max_c = par_couvert[0][1]["couvert"]
    ex_aequo = [b for b, c in couverture_bloc.items() if c["couvert"] == max_c]
    return {
        "plus_de_couvert": par_couvert[0][0],
        "couvert": max_c,
        "ex_aequo_couvert": ex_aequo,
        "plus_de_couvert_ou_partiel": par_non_absent[0][0],
        "couvert_ou_partiel": par_non_absent[0][1]["couvert"] + par_non_absent[0][1]["partiel"],
    }


def rapport_markdown(v: dict, etats: dict) -> str:
    lignes = [
        f"Vérification de `etats.json` ({v['nb_dimensions']} lignes) : "
        + ("**conforme**" if v["ok"] else f"**{len(v['erreurs'])} règle(s) violée(s)**"),
        "",
    ]
    for e in v["erreurs"]:
        lignes.append(f"- {e}")
    if v["erreurs"]:
        lignes.append("")
    lignes += ["| État | Dimensions |", "|---|---|"]
    for e in ETATS:
        lignes.append(f"| {e} | {v['par_etat'][e]} |")
    lignes.append(f"| **total** | {sum(v['par_etat'].values())} |")
    lignes += [
        "",
        "| Bloc | " + " | ".join(ETATS) + " | total |",
        "|---|" + "---|" * (len(ETATS) + 1),
    ]
    for b, c in v["par_bloc"].items():
        lignes.append(
            f"| {b} | " + " | ".join(str(c[e]) for e in ETATS) + f" | {sum(c.values())} |"
        )
    if v["couverture_evaluateur1_par_bloc"]:
        lignes += [
            "",
            "Couverture par les systèmes publics, notation de l'évaluateur 1 (21/08/2026, à contester) :",  # noqa: E501
            "",
            "| Bloc | couvert | partiel | absent |",
            "|---|---|---|---|",
        ]
        for b, c in v["couverture_evaluateur1_par_bloc"].items():
            lignes.append(f"| {b} | {c['couvert']} | {c['partiel']} | {c['absent']} |")
        p = bloc_le_plus_couvert(v["couverture_evaluateur1_par_bloc"])
        ex = (
            f" (ex æquo : {', '.join(p['ex_aequo_couvert'])})"
            if len(p["ex_aequo_couvert"]) > 1
            else ""
        )
        lignes += [
            "",
            f"Bloc le plus couvert (« couvert ») : **{p['plus_de_couvert']}** avec {p['couvert']}{ex}. "  # noqa: E501
            f"Bloc le moins absent (couvert + partiel) : **{p['plus_de_couvert_ou_partiel']}** avec {p['couvert_ou_partiel']}.",  # noqa: E501
        ]
    if v["absentes"]:
        etat_de = {d["id"]: d for d in etats["dimensions"]}
        lignes += [
            "",
            f"Les {len(v['absentes'])} lignes « absent » de tout système public (évaluateur 1), avec leur état ici :",  # noqa: E501
            "",
            "| Catégorie É4 | Dimension | État ici |",
            "|---|---|---|",
        ]
        for cat, ids in ABSENTES_E4.items():
            for i in ids:
                d = etat_de.get(i, {})
                lignes.append(f"| {cat} | {i} {d.get('nom', '')} | {d.get('etat', '?')} |")
    return "\n".join(lignes)


# ---------------------------------------------------------------- kit des juges

SYNTHESE_RE = re.compile(r"\*\*(D\d\d)[^*]*\*\*\s*\([^)]*\)\.?\s*(.+)", re.S)
PHRASE_RE = re.compile(r"^(.*?\.)(?=\s+(?:[A-ZÀ-Ý«*]|$))", re.S)


def definition_depuis_fiche(chemin: Path) -> str:
    txt = chemin.read_text(encoding="utf-8")
    i = txt.find("## FICHE SYNTHÈSE")
    bloc = txt[i:] if i >= 0 else txt
    m = SYNTHESE_RE.search(bloc)
    corps = " ".join((m.group(2) if m else bloc).split())
    m2 = PHRASE_RE.search(corps)
    return (m2.group(1) if m2 else corps[:300]).strip()


def definitions(dossier: Path) -> dict[str, str]:
    defs = {}
    for f in sorted(dossier.glob("D[0-9][0-9]-*.md")):
        defs[f.name[:3]] = definition_depuis_fiche(f)
    return defs


def kit_markdown(etats: dict, couverture: dict, defs: dict[str, str]) -> str:
    """Ancien tableau (extraction par regex depuis les fiches). Gardé pour rejouer le 04/09."""
    approche = {lig["id"]: lig["approche"] for lig in couverture["lignes"]}
    noms = {d["id"]: d["nom"] for d in etats["dimensions"]}
    lignes = [
        "| # | Dimension | Définition en une phrase (fiche) | Ce qui s'en approche le plus (proposition de l'évaluateur 1, 21/08 — à contester) | Couvert / partiel / absent |",  # noqa: E501
        "|---|---|---|---|---|",
    ]
    for b, ids in BLOCS.items():
        lignes.append(f"| | **{b}** | | | |")
        for i in ids:
            d = defs.get(i, "(fiche introuvable)").replace("|", "／")
            a = approche.get(i, "(non notée)").replace("|", "／")
            lignes.append(f"| {i} | {noms.get(i, '')} | {d} | {a} | |")
    return "\n".join(lignes)


def kit_markdown_relu(etats: dict, source: dict) -> str:
    """Tableau du kit depuis kit_definitions.json — définitions relues, colonne sans verdict."""
    par_id = {lig["id"]: lig for lig in source["lignes"]}
    noms = {d["id"]: d["nom"] for d in etats["dimensions"]}
    lignes = [
        "| # | Dimension | Ce qui est noté : le cœur de la ligne | Sous-parties (ne déterminent pas la note) | Pistes à examiner (liste non exhaustive, sans verdict) | Couvert / partiel / absent |",  # noqa: E501
        "|---|---|---|---|---|---|",
    ]
    manquants = []
    for b, ids in BLOCS.items():
        lignes.append(f"| | **{b}** | | | | |")
        for i in ids:
            lig = par_id.get(i)
            if lig is None:
                manquants.append(i)
                lignes.append(f"| {i} | {noms.get(i, '')} | (définition manquante) | | | |")
                continue
            d = lig["definition"].replace("|", "／")
            s = lig.get("sous_parties", "").replace("|", "／")
            p = lig.get("pistes", "").replace("|", "／")
            lignes.append(f"| {i} | {noms.get(i, '')} | {d} | {s} | {p} | |")
    if manquants:
        raise SystemExit(f"kit_definitions.json : lignes manquantes {', '.join(manquants)}")
    return "\n".join(lignes)


# ---------------------------------------------------------------- entrée


def _charger(p: str) -> dict:
    return json.loads(Path(p).read_text(encoding="utf-8"))


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
    sub = p.add_subparsers(dest="cmd", required=True)
    s1 = sub.add_parser("importer-couverture")
    s1.add_argument("source")
    s1.add_argument("--sortie", required=True)
    s2 = sub.add_parser("verifier")
    s2.add_argument("--etats", required=True)
    s2.add_argument("--mesures", required=True)
    s2.add_argument("--couverture", default=None)
    s2.add_argument("--md", default=None)
    s3 = sub.add_parser("kit")
    s3.add_argument("--etats", required=True)
    s3.add_argument("--definitions", default=None, help="kit_definitions.json (source relue)")
    s3.add_argument("--couverture", default=None, help="ancien mode : notation de l'évaluateur 1")
    s3.add_argument(
        "--fiches", default="dimensions", help="ancien mode : extraction regex"
    )
    s3.add_argument("--sortie", required=True)
    args = p.parse_args(argv)

    if args.cmd == "importer-couverture":
        r = importer_couverture(Path(args.source))
        Path(args.sortie).write_text(json.dumps(r, ensure_ascii=False, indent=2), encoding="utf-8")
        print(
            f"{r['nb_lignes']} lignes importées, comptes {r['comptes']}, manquantes {r['manquantes']}, "  # noqa: E501
            f"doublons {r['doublons']}, écarts de bloc {len(r['ecarts_blocs'])} → {args.sortie}"
        )
        return 0 if r["nb_lignes"] == 56 and not r["ecarts_blocs"] else 1
    if args.cmd == "verifier":
        etats = _charger(args.etats)
        v = verifier(
            etats, _charger(args.mesures), _charger(args.couverture) if args.couverture else None
        )
        md = rapport_markdown(v, etats)
        print(md)
        if args.md:
            Path(args.md).write_text(md + "\n", encoding="utf-8")
        return 0 if v["ok"] else 1
    if args.cmd == "kit":
        etats = _charger(args.etats)
        if args.definitions:
            md = kit_markdown_relu(etats, _charger(args.definitions))
        elif args.couverture:
            md = kit_markdown(etats, _charger(args.couverture), definitions(Path(args.fiches)))
        else:
            print("kit : donner --definitions (source relue) ou --couverture (ancien mode)")
            return 2
        Path(args.sortie).write_text(md + "\n", encoding="utf-8")
        print(
            f"kit écrit : {args.sortie} ({md.count(chr(10)) - 1 - len(BLOCS)} lignes de dimension)"
        )
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
