"""Tests du format JSON des notes des juges."""

import json

import tools.notes_juges as nj


def _notes(**surcharges):
    base = {
        "juges": {"juge1": "évaluateur 1", "juge2": "juge 2", "juge3": "juge 3"},
        "lignes": [
            {"dimension": "D00 GARDE-FOUS",
             "juge1": "partiel", "juge1_preuve": "produit X, v2.3, 21/08/2026",
             "juge2": "absent", "juge2_preuve": "",
             "juge3": "", "juge3_preuve": ""},
        ],
    }
    base.update(surcharges)
    return base


def test_gabarit_une_ligne_par_dimension(tmp_path):
    etats = tmp_path / "etats.json"
    etats.write_text(json.dumps({"dimensions": [
        {"id": "D00", "nom": "Garde-fous"}, {"id": "D01", "nom": "Mémoire"}]}),
        encoding="utf-8")
    g = nj.construire_gabarit(etats)
    assert len(g["lignes"]) == 2
    assert g["lignes"][0]["dimension"] == "D00 Garde-fous"
    # Toutes les colonnes de juges existent et sont vides.
    for juge in ("juge1", "juge2", "juge3"):
        assert g["lignes"][0][juge] == ""
        assert g["lignes"][0][f"{juge}_preuve"] == ""


def test_verifier_accepte_un_fichier_propre():
    assert nj.verifier(_notes(), attendu=1) == []


def test_verifier_refuse_une_valeur_hors_echelle():
    notes = _notes()
    notes["lignes"][0]["juge3"] = "peut-être"
    defauts = nj.verifier(notes, attendu=1)
    assert any("hors" in d for d in defauts)


def test_verifier_exige_une_preuve_pour_couvert():
    """Le kit est explicite : sans produit nommé, la note vaut `absent`."""
    notes = _notes()
    notes["lignes"][0]["juge3"] = "couvert"
    notes["lignes"][0]["juge3_preuve"] = "   "
    defauts = nj.verifier(notes, attendu=1)
    assert any("sans preuve" in d for d in defauts)


def test_verifier_n_exige_pas_de_preuve_pour_absent():
    notes = _notes()
    assert not any("juge2" in d for d in nj.verifier(notes, attendu=1))


def test_verifier_detecte_le_doublon_de_dimension():
    notes = _notes()
    notes["lignes"].append(dict(notes["lignes"][0]))
    defauts = nj.verifier(notes, attendu=2)
    assert any("double" in d for d in defauts)


def test_verifier_compte_les_lignes():
    defauts = nj.verifier(_notes(), attendu=56)
    assert any("56 attendues" in d for d in defauts)


def test_vers_csv_rend_le_format_lisible_par_accord_juges(tmp_path):
    sortie = tmp_path / "notes.csv"
    n = nj.vers_csv(_notes(), sortie)
    assert n == 1
    lignes = sortie.read_text(encoding="utf-8").splitlines()
    assert lignes[0] == "dimension;juge1;juge2;juge3"
    assert lignes[1] == "D00 GARDE-FOUS;partiel;absent;"


def test_vers_csv_normalise_la_casse(tmp_path):
    notes = _notes()
    notes["lignes"][0]["juge1"] = "  PARTIEL  "
    sortie = tmp_path / "notes.csv"
    nj.vers_csv(notes, sortie)
    assert ";partiel;" in sortie.read_text(encoding="utf-8")


def test_noms_juges_depuis_les_lignes_si_len_tete_manque():
    notes = _notes()
    del notes["juges"]
    assert nj.noms_juges(notes) == ["juge1", "juge2", "juge3"]
