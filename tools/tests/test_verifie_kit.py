"""Tests du contrôle mécanique du kit des juges.

Chaque test de défaut part du kit réel et n'y casse QU'UNE chose : si le contrôle passait
quand même, il ne discriminerait rien.
"""

from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from tools.verifie_kit import (
    DEFINITIONS,
    MAX_MOTS,
    charge,
    compte_mots,
    controle,
    main,
    phrases,
    verdicts_dans,
)


@pytest.fixture
def kit() -> dict:
    return copy.deepcopy(charge(DEFINITIONS))


# --------------------------------------------------------------- le kit réel


def test_le_kit_reel_est_conforme(kit):
    r = controle(kit)
    assert r["conforme"], r
    assert r["nb_lignes"] == 56
    assert not r["ids_manquants"] and not r["ids_en_trop"] and not r["ids_dupliques"]


def test_le_kit_reel_couvre_D00_a_D55(kit):
    ids = {ligne["id"] for ligne in kit["lignes"]}
    assert ids == {f"D{n:02d}" for n in range(56)}


def test_le_kit_reel_cite_sa_source_fiche_par_fiche(kit):
    for ligne in kit["lignes"]:
        assert ligne["source"].startswith(ligne["id"]), ligne["id"]
        assert "§1" in ligne["source"], ligne["id"]


# ------------------------------------------------- le contrôle voit le rouge


def test_une_definition_trop_longue_est_refusee(kit):
    kit["lignes"][0]["definition"] = " ".join(["mot"] * (MAX_MOTS + 1)) + "."
    r = controle(kit)
    assert not r["conforme"]
    assert r["trop_longues"] == [("D00", MAX_MOTS + 1)]


def test_une_definition_en_deux_phrases_est_refusee(kit):
    kit["lignes"][0]["definition"] = "Le compagnon protège. Il le fait par conception."
    r = controle(kit)
    assert not r["conforme"]
    assert "D00" in r["plusieurs_phrases"]


@pytest.mark.parametrize(
    "colonne",
    [
        "Aucun produit ne fait cela.",
        "Personne ne l'a tenté.",
        "Rien de comparable côté produit.",
        "Cette capacité n'existe nulle part.",
        "Un service cloud est disponible par construction.",
        "Le multilingue est acquis.",
        "Voix expressive en production chez deux acteurs.",
        "C'est exactement le produit de Replika.",
        "Replika relance, mais sans réciprocité.",
        "La synchronie fine reste un sujet de recherche.",
        "Sans équivalent trouvé au 21/08.",
        "Les produits ne tiennent pas la durée.",
        # Négation elliptique, sans « ne » : la forme la plus fréquente de la colonne du 04/09.
        "Les bancs publics mesurent la mémoire, pas la qualité du lien.",
        "Applications de coaching sportif, sans mémoire longue ni modèle de la personne.",
        "Tuteurs intelligents documentés, hors socle relationnel.",
        "La théorie de l'esprit explicite : non traitée en produit.",
    ],
)
def test_chaque_formule_de_verdict_est_attrapee(kit, colonne):
    assert verdicts_dans(colonne), colonne
    kit["lignes"][0]["pistes"] = colonne
    r = controle(kit)
    assert not r["conforme"]
    assert "D00" in r["verdicts"]


def test_une_piste_descriptive_passe(kit):
    kit["lignes"][0]["pistes"] = "À examiner : Replika, Character.AI, ChatGPT, Claude, Gemini."
    assert verdicts_dans(kit["lignes"][0]["pistes"]) == []
    assert controle(kit)["conforme"]


def test_une_colonne_pistes_vide_est_refusee(kit):
    kit["lignes"][3]["pistes"] = "   "
    r = controle(kit)
    assert not r["conforme"]
    assert r["sans_pistes"] == ["D01"]


def test_une_ligne_supprimee_est_refusee(kit):
    """La numérotation D00-D55 est figée et « 56 » est publié."""
    kit["lignes"] = [lig for lig in kit["lignes"] if lig["id"] != "D30"]
    r = controle(kit)
    assert not r["conforme"]
    assert r["ids_manquants"] == ["D30"]
    assert r["nb_lignes"] == 55


def test_une_ligne_ajoutee_est_refusee(kit):
    kit["lignes"].append(
        {
            "id": "D56",
            "definition": "Une ligne de plus.",
            "source": "x",
            "pistes": "À examiner : X.",
        }
    )
    r = controle(kit)
    assert not r["conforme"]
    assert r["ids_en_trop"] == ["D56"]


def test_une_ligne_dupliquee_est_refusee(kit):
    kit["lignes"].append(copy.deepcopy(kit["lignes"][0]))
    r = controle(kit)
    assert not r["conforme"]
    assert r["ids_dupliques"] == ["D00"]


def test_une_definition_qui_ne_sort_pas_du_tableau_publie_est_refusee(kit):
    tableau = "| D00 | GARDE-FOUS | une définition qui n'est pas celle de la source | | | |"
    r = controle(kit, tableau)
    assert not r["conforme"]
    assert "D00" in r["absentes_du_tableau"]


# --------------------------------- le detecteur mesuré sur la colonne d'avant


def test_le_detecteur_voit_la_colonne_du_04_09_comme_orientee():
    """Contre-épreuve : le détecteur doit être rouge sur la colonne qu'il remplace.

    Un détecteur vert des deux côtés ne prouverait rien. 42 / 56 est ce qu'il trouve sur la
    notation de l'évaluateur 1 ; la relecture humaine du 07/09 en comptait 48 — six lignes
    orientent sans employer de formule (présence annoncée, limitation affirmative), et aucune
    expression régulière ne les attrapera. Le contrôle est un plancher, pas une preuve d'aveugle.
    """
    source = DEFINITIONS.parent / "couverture_evaluateur1_2026-08-21.json"
    lignes = json.loads(source.read_text(encoding="utf-8"))["lignes"]
    orientees = [lig["id"] for lig in lignes if verdicts_dans(lig["approche"])]
    assert len(lignes) == 56
    assert len(orientees) == 42, orientees


# ------------------------------------------------------------ les compteurs


def test_un_tiret_seul_ne_compte_pas_pour_un_mot():
    assert compte_mots("le compagnon — il est là") == 5


def test_une_phrase_avec_deux_points_reste_une_phrase():
    assert phrases("Le compagnon fait ceci : cela, et cela encore.") == 1


def test_une_abreviation_chiffree_ne_coupe_pas_la_phrase():
    assert phrases("Un soutien disponible à 3 h du matin, qui connaît l'histoire.") == 1


# ------------------------------------------------------------------- la CLI


def test_le_script_rend_0_sur_le_kit_reel():
    assert main([]) == 0


def test_le_script_rend_1_sur_un_kit_casse(tmp_path: Path, kit):
    kit["lignes"][0]["pistes"] = "Aucun produit ne fait cela."
    f = tmp_path / "kit.json"
    f.write_text(json.dumps(kit, ensure_ascii=False), encoding="utf-8")
    rapport = tmp_path / "rapport.json"
    assert main(["--definitions", str(f), "--tableau", str(tmp_path / "absent.md"),
                 "--json", str(rapport)]) == 1
    assert json.loads(rapport.read_text(encoding="utf-8"))["verdicts"]["D00"]
