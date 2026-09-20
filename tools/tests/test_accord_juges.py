"""Tests de tools/accord_juges.py — κ de Fleiss sur un exemple publié et dépouillement CSV."""

import math

import tools.accord_juges as aj

# Exemple canonique (Fleiss 1971, repris par Wikipedia « Fleiss' kappa ») :
# 10 sujets, 14 juges, 5 catégories → P̄ = 0,378, P̄e = 0,213, κ = 0,210.
MATRICE_FLEISS = [
    [0, 0, 0, 0, 14],
    [0, 2, 6, 4, 2],
    [0, 0, 3, 5, 6],
    [0, 3, 9, 2, 0],
    [2, 2, 8, 1, 1],
    [7, 7, 0, 0, 0],
    [3, 2, 6, 3, 0],
    [2, 5, 3, 2, 2],
    [6, 5, 2, 1, 0],
    [0, 2, 2, 3, 7],
]


def test_kappa_exemple_publie():
    assert abs(aj.kappa_fleiss(MATRICE_FLEISS) - 0.210) < 0.001


def test_kappa_accord_parfait_et_desaccord():
    assert aj.kappa_fleiss([[3, 0, 0], [0, 3, 0], [0, 0, 3]]) == 1.0
    # tout le monde dit toujours la même catégorie : P̄e = 1, accord parfait par convention
    assert aj.kappa_fleiss([[3, 0, 0], [3, 0, 0]]) == 1.0
    # désaccord total à 3 juges / 3 catégories : κ négatif
    assert aj.kappa_fleiss([[1, 1, 1], [1, 1, 1]]) < 0


def test_kappa_refuse_lignes_inegales():
    try:
        aj.kappa_fleiss([[2, 1, 0], [1, 1, 0]])
    except ValueError:
        return
    raise AssertionError("une matrice à n inégal doit être refusée")


def test_analyse_csv(tmp_path):
    csv_txt = (
        "dimension;juge1;juge2;juge3\n"
        "D01 Mémoire;couvert;couvert;couvert\n"
        "D02 Souveraine;partiel;Partiel;absent\n"
        "D03 Intime;couvert;partiel;absent\n"
        "D04 Emotion;absent;;absent\n"
    )
    chemin = tmp_path / "notes.csv"
    chemin.write_text(csv_txt, encoding="utf-8")
    juges, lignes = aj.lire_notes(chemin)
    assert juges == ["juge1", "juge2", "juge3"]
    r = aj.analyser(juges, lignes)
    assert r["lignes_notees"] == 3
    assert r["lignes_incompletes"] == ["D04 Emotion"]
    assert r["unanimite"] == 1
    assert r["majorite"] == 1
    assert r["desaccord"] == ["D03 Intime"]
    assert r["comptes_vote_majoritaire"] == {"couvert": 1, "partiel": 1, "sans majorité": 1}
    assert r["comptes_par_juge"]["juge1"] == {"couvert": 2, "partiel": 1, "absent": 0}
    assert r["kappa_fleiss"] is not None and not math.isnan(r["kappa_fleiss"])
    assert "κ de Fleiss" in aj.rapport_markdown(r)


def test_gabarit(tmp_path):
    etats = tmp_path / "etats.json"
    etats.write_text(
        '{"dimensions": [{"id": "D00", "nom": "Garde-fous"}, {"id": "D01", "nom": "Mémoire"}]}',
        encoding="utf-8",
    )
    sortie = tmp_path / "notes.csv"
    assert aj.ecrire_gabarit(etats, sortie) == 2
    contenu = sortie.read_text(encoding="utf-8").splitlines()
    assert contenu[0] == "dimension;juge1;juge2;juge3"
    assert contenu[1] == "D00 Garde-fous;;;"
