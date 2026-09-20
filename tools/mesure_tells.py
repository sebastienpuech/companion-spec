#!/usr/bin/env python3
"""Compteur de tells — garde 4 de la garantie anti-slop (audit du 03/09/2026, §6 bis).

Compte, de façon déterministe et sans appel modèle, les marqueurs qui trahissent un texte
généré sans relecture :
  - tirets cadratins (—) pour 300 mots (cible ≤ 1) ; tirets demi-cadratins (–) comptés à part ;
  - « ce n'est pas X, c'est Y » (cible 0) ;
  - antithèses « , pas » pour 1 000 mots (cible ≤ 1) ;
  - triades en fin de phrase « X, Y et Z. » (cible 0) ;
  - chutes-slogans : dernière phrase d'un paragraphe de 5 mots ou moins, sans chiffre (cible 0) ;
  - débuts de phrase répétés : trois phrases de suite qui commencent par le même mot ;
    et trois paragraphes de suite qui commencent par le même mot ;
  - écart-type de la longueur des phrases (une prose humaine varie ; un gabarit ne varie pas) ;
  - tournures vides : « il est important », « au fil de », « dans un monde où » (cible 0) ;
  - paragraphes sans ancre : aucun chiffre (donc aucune date, aucun #N, aucun Dnn, aucun
    arXiv/DOI), aucun nom de fichier, aucune citation entre guillemets — sur les paragraphes
    de 25 mots ou plus (cible 0).

Usage :
  python tools/mesure_tells.py TEXTE [--plages 1-140,1182-1321] [--json SORTIE] [--titre NOM]
TEXTE : .md, .txt ou .docx (le .docx est lu sans dépendance, par zipfile + xml.etree). Les titres
(#…), les lignes de tableau (| … |) et les blocs de code sont exclus des paragraphes comptés.
--plages restreint le comptage à des lignes (1-based, inclusives) du texte extrait, pour isoler
par exemple la prose de cadrage d'un document qui contient aussi des fiches générées.
"""

from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

MOT_RE = re.compile(r"[\w'’-]+", re.UNICODE)
PHRASE_SPLIT_RE = re.compile(r"(?<=[.!?…])\s+")
CE_NEST_PAS_RE = re.compile(r"ce n[’']est pas [^.;!?]{1,120}?[,:] c[’']est ", re.IGNORECASE)
VIRGULE_PAS_RE = re.compile(r",\s+pas\s", re.IGNORECASE)
TRIADE_FIN_RE = re.compile(r"\b[\w'’-]+, [\w'’-]+(?:,| et) [\w'’-]+\s*[.!?…]", re.UNICODE)
TOURNURES = ("il est important", "au fil de", "dans un monde où")
FICHIER_RE = re.compile(r"\b[\w./-]+\.(?:py|md|json|db|ya?ml|txt|docx|csv|ps1)\b")
CITATION_RE = re.compile(r"[«\"“][^»\"”]{12,}[»\"”]")
CHIFFRE_RE = re.compile(r"\d")
SEUIL_MOTS_PARAGRAPHE = 25
SEUIL_MOTS_CHUTE = 5


# ---------------------------------------------------------------- lecture des textes


def _para_text(p) -> str:
    parts = []
    for node in p.iter():
        if node.tag == W + "t" and node.text:
            parts.append(node.text)
        elif node.tag in (W + "tab", W + "br", W + "cr"):
            parts.append(" ")
    return "".join(parts)


def _para_style(p) -> str:
    ppr = p.find(W + "pPr")
    if ppr is None:
        return ""
    ps = ppr.find(W + "pStyle")
    return "" if ps is None else ps.get(W + "val", "")


def _niveau_titre(style: str) -> int:
    s = style.lower()
    for prefix in ("heading", "titre", "title"):
        if s.startswith(prefix):
            digits = "".join(ch for ch in s if ch.isdigit())
            return int(digits) if digits else 1
    return 0


def lignes_docx(chemin: Path) -> list[str]:
    """Un paragraphe Word = une ligne ; titres préfixés de '#', rangées de tableau de '| '."""
    with zipfile.ZipFile(chemin) as z:
        root = ET.fromstring(z.read("word/document.xml"))
    body = root.find(W + "body")
    lignes: list[str] = []
    for child in body:
        if child.tag == W + "p":
            txt = _para_text(child).strip()
            lvl = _niveau_titre(_para_style(child))
            if lvl:
                lignes.append("#" * lvl + " " + txt)
            elif txt:
                lignes.append(txt)
            else:
                lignes.append("")
        elif child.tag == W + "tbl":
            for tr in child.iter(W + "tr"):
                cells = [
                    " ".join(_para_text(p).strip() for p in tc.iter(W + "p")).strip()
                    for tc in tr.findall(W + "tc")
                ]
                lignes.append("| " + " | ".join(cells) + " |")
            lignes.append("")
    return lignes


def lignes_texte(chemin: Path) -> list[str]:
    return chemin.read_text(encoding="utf-8").splitlines()


def charger_lignes(chemin: Path) -> list[str]:
    if chemin.suffix.lower() == ".docx":
        return lignes_docx(chemin)
    return lignes_texte(chemin)


def appliquer_plages(lignes: list[str], plages: str | None) -> list[str]:
    """--plages '1-140,1182-1321' : garde ces lignes (1-based, inclusives), dans l'ordre."""
    if not plages:
        return lignes
    gardees: list[str] = []
    for morceau in plages.split(","):
        debut, fin = morceau.split("-")
        a, b = int(debut), int(fin)
        gardees.extend(lignes[a - 1 : b])
        gardees.append("")
    return gardees


def paragraphes(lignes: list[str]) -> list[str]:
    """Blocs séparés par une ligne vide ; titres, tableaux, code et blockquote-marqueurs exclus."""
    paras: list[str] = []
    courant: list[str] = []
    dans_code = False
    for brut in lignes:
        ligne = brut.rstrip()
        if ligne.startswith("```"):
            dans_code = not dans_code
            continue
        if dans_code:
            continue
        if ligne.startswith("#") or ligne.startswith("|"):
            if courant:
                paras.append(" ".join(courant))
                courant = []
            continue
        if ligne.startswith(">"):
            ligne = ligne.lstrip("> ").rstrip()
        if not ligne.strip():
            if courant:
                paras.append(" ".join(courant))
                courant = []
            continue
        courant.append(ligne.strip())
    if courant:
        paras.append(" ".join(courant))
    return paras


# ---------------------------------------------------------------- mesures


def mots(texte: str) -> list[str]:
    return MOT_RE.findall(texte)


def phrases(texte: str) -> list[str]:
    return [p.strip() for p in PHRASE_SPLIT_RE.split(texte) if p.strip()]


def premier_mot(phrase: str) -> str:
    m = MOT_RE.search(phrase)
    return m.group(0).lower() if m else ""


def runs_repetes(mots_initiaux: list[str], longueur: int = 3) -> int:
    """Nombre de séquences d'au moins `longueur` éléments identiques consécutifs (non vides)."""
    runs = 0
    i = 0
    n = len(mots_initiaux)
    while i < n:
        j = i
        while j + 1 < n and mots_initiaux[j + 1] == mots_initiaux[i] and mots_initiaux[i]:
            j += 1
        if j - i + 1 >= longueur:
            runs += 1
        i = j + 1
    return runs


def a_une_ancre(para: str) -> bool:
    return bool(CHIFFRE_RE.search(para) or FICHIER_RE.search(para) or CITATION_RE.search(para))


def mesurer(paras: list[str]) -> dict:
    texte = "\n".join(paras)
    n_mots = len(mots(texte))
    toutes_phrases: list[str] = []
    longueurs: list[int] = []
    chutes = 0
    sans_ancre: list[str] = []
    n_consideres = 0
    for para in paras:
        ph = phrases(para)
        toutes_phrases.extend(ph)
        longueurs.extend(len(mots(p)) for p in ph)
        if len(ph) >= 2:
            derniere = ph[-1]
            if len(mots(derniere)) <= SEUIL_MOTS_CHUTE and not CHIFFRE_RE.search(derniere):
                chutes += 1
        if len(mots(para)) >= SEUIL_MOTS_PARAGRAPHE:
            n_consideres += 1
            if not a_une_ancre(para):
                sans_ancre.append(para[:80])
    tirets = texte.count("—")
    demi_tirets = texte.count("–")
    tournures = {t: len(re.findall(re.escape(t), texte, flags=re.IGNORECASE)) for t in TOURNURES}
    par_300 = (tirets / n_mots * 300) if n_mots else 0.0
    virgule_pas = len(VIRGULE_PAS_RE.findall(texte))
    return {
        "mots": n_mots,
        "paragraphes": len(paras),
        "phrases": len(toutes_phrases),
        "tirets_cadratins": tirets,
        "tirets_cadratins_pour_300_mots": round(par_300, 2),
        "tirets_demi_cadratins": demi_tirets,
        "ce_nest_pas_x_cest_y": len(CE_NEST_PAS_RE.findall(texte)),
        "antitheses_virgule_pas": virgule_pas,
        "antitheses_virgule_pas_pour_1000_mots": round(virgule_pas / n_mots * 1000, 2)
        if n_mots
        else 0.0,
        "triades_fin_de_phrase": len(TRIADE_FIN_RE.findall(texte)),
        "chutes_slogans": chutes,
        "debuts_de_phrase_repetes_3": runs_repetes([premier_mot(p) for p in toutes_phrases]),
        "debuts_de_paragraphe_repetes_3": runs_repetes([premier_mot(p) for p in paras]),
        "longueur_phrase_moyenne": round(statistics.fmean(longueurs), 1) if longueurs else 0.0,
        "longueur_phrase_ecart_type": round(statistics.pstdev(longueurs), 1)
        if len(longueurs) > 1
        else 0.0,
        "tournures_vides": tournures,
        "tournures_vides_total": sum(tournures.values()),
        "paragraphes_consideres_pour_ancre": n_consideres,
        "paragraphes_sans_ancre": len(sans_ancre),
        "paragraphes_sans_ancre_debuts": sans_ancre[:10],
    }


def tableau_markdown(titre: str, m: dict) -> str:
    lignes = [
        f"| Mesure ({titre}) | Valeur | Cible §6 bis |",
        "|---|---|---|",
        f"| Mots / paragraphes / phrases | {m['mots']} / {m['paragraphes']} / {m['phrases']} | — |",
        f"| Tirets cadratins pour 300 mots (total) | {m['tirets_cadratins_pour_300_mots']} ({m['tirets_cadratins']}) | ≤ 1 |",  # noqa: E501
        f"| Tirets demi-cadratins (total) | {m['tirets_demi_cadratins']} | — |",
        f"| « ce n'est pas X, c'est Y » | {m['ce_nest_pas_x_cest_y']} | 0 |",
        f"| Antithèses « , pas » pour 1 000 mots (total) | {m['antitheses_virgule_pas_pour_1000_mots']} ({m['antitheses_virgule_pas']}) | ≤ 1 |",  # noqa: E501
        f"| Triades en fin de phrase | {m['triades_fin_de_phrase']} | 0 |",
        f"| Chutes-slogans (≤ {SEUIL_MOTS_CHUTE} mots, sans chiffre) | {m['chutes_slogans']} | 0 |",
        f"| Débuts de phrase répétés (3 de suite) | {m['debuts_de_phrase_repetes_3']} | 0 |",
        f"| Débuts de paragraphe répétés (3 de suite) | {m['debuts_de_paragraphe_repetes_3']} | 0 |",  # noqa: E501
        f"| Longueur de phrase : moyenne / écart-type | {m['longueur_phrase_moyenne']} / {m['longueur_phrase_ecart_type']} | varie |",  # noqa: E501
        f"| Tournures vides (il est important / au fil de / dans un monde où) | {m['tournures_vides_total']} | 0 |",  # noqa: E501
        f"| Paragraphes sans ancre (sur ≥ {SEUIL_MOTS_PARAGRAPHE} mots) | {m['paragraphes_sans_ancre']} / {m['paragraphes_consideres_pour_ancre']} | 0 |",  # noqa: E501
    ]
    return "\n".join(lignes)


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
    p.add_argument("texte", help="fichier .md / .txt / .docx")
    p.add_argument("--plages", default=None, help="lignes à garder, ex. 1-140,1182-1321")
    p.add_argument("--json", default=None, help="écrire les mesures dans ce fichier JSON")
    p.add_argument(
        "--titre", default=None, help="libellé dans le tableau (défaut : nom du fichier)"
    )
    args = p.parse_args(argv)
    chemin = Path(args.texte)
    lignes = appliquer_plages(charger_lignes(chemin), args.plages)
    m = mesurer(paragraphes(lignes))
    m["fichier"] = chemin.name
    m["plages"] = args.plages
    titre = args.titre or chemin.name
    print(tableau_markdown(titre, m))
    if args.json:
        Path(args.json).write_text(json.dumps(m, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\nJSON écrit : {args.json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
