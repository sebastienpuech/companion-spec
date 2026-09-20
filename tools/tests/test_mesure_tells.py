"""Tests du compteur de tells (tools/mesure_tells.py) sur un texte-fixture aux comptes connus."""

import zipfile

import tools.mesure_tells as mt

FIXTURE = """# Titre exclu du comptage

Paragraphe un : le coach a écrit 12 notes le 03/09 — et il a relu — sans tiret de trop.
Ce n'est pas un style, c'est une preuve.

Il est important de dire que ceci est vide. Il parle. Il se tait. Il parle encore, pas trop.

| tableau | exclu |
|---|---|

Un paragraphe sans aucune ancre, qui parle de mémoire et de relation sans jamais donner un fait,
une date, un fichier, une citation, ni un chiffre, ni un nom, pour tester le détecteur de
paragraphe vide qui doit le compter comme tel. Fin.
"""


def _mesures(texte: str) -> dict:
    return mt.mesurer(mt.paragraphes(texte.splitlines()))


def test_paragraphes_excluent_titres_et_tableaux():
    paras = mt.paragraphes(FIXTURE.splitlines())
    assert len(paras) == 3
    assert not any(p.startswith("#") or p.startswith("|") for p in paras)


def test_comptes_connus():
    m = _mesures(FIXTURE)
    assert m["tirets_cadratins"] == 2
    assert m["ce_nest_pas_x_cest_y"] == 1
    assert m["antitheses_virgule_pas"] == 1
    assert m["tournures_vides"]["il est important"] == 1
    assert m["tournures_vides_total"] == 1
    assert m["triades_fin_de_phrase"] == 0
    # « Il est important… / Il parle. / Il se tait. / Il parle encore… » : une séquence de 3+
    assert m["debuts_de_phrase_repetes_3"] == 1
    # « Fin. » et « Il parle encore, pas trop. » : deux dernières phrases de ≤ 5 mots sans chiffre
    assert m["chutes_slogans"] == 2
    # paragraphes 1 et 3 ont ≥ 25 mots ; seul le 3 n'a ni chiffre, ni fichier, ni citation
    assert m["paragraphes_consideres_pour_ancre"] == 2
    assert m["paragraphes_sans_ancre"] == 1
    assert m["paragraphes_sans_ancre_debuts"][0].startswith("Un paragraphe sans aucune ancre")
    assert m["mots"] > 0
    assert m["tirets_cadratins_pour_300_mots"] == round(2 / m["mots"] * 300, 2)


def test_ancre_par_fichier_ou_citation():
    assert mt.a_une_ancre("un paragraphe qui nomme bot/telegram_bot.py et rien d'autre")
    assert mt.a_une_ancre("il a dit « une phrase entière entre guillemets » sans chiffre")
    assert not mt.a_une_ancre("rien ici qui ancre quoi que ce soit")


def test_runs_repetes():
    assert mt.runs_repetes(["il", "il", "il", "le", "il", "il"]) == 1
    assert mt.runs_repetes(["il", "il", "le", "il", "il"]) == 0
    assert mt.runs_repetes(["", "", "", "a"]) == 0


def test_plages():
    lignes = ["l1", "l2", "l3", "l4", "l5"]
    assert mt.appliquer_plages(lignes, "1-2,5-5") == ["l1", "l2", "", "l5", ""]


def test_lecture_docx(tmp_path):
    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        "<w:body>"
        '<w:p><w:pPr><w:pStyle w:val="Heading1"/></w:pPr><w:r><w:t>Un titre</w:t></w:r></w:p>'
        "<w:p><w:r><w:t>Première phrase — avec un tiret.</w:t></w:r></w:p>"
        "<w:p><w:r><w:t>Seconde phrase, pas de tiret.</w:t></w:r></w:p>"
        "</w:body></w:document>"
    )
    chemin = tmp_path / "mini.docx"
    with zipfile.ZipFile(chemin, "w") as z:
        z.writestr("word/document.xml", xml)
    lignes = mt.charger_lignes(chemin)
    assert lignes[0] == "# Un titre"
    m = mt.mesurer(mt.paragraphes(lignes))
    assert m["paragraphes"] == 1  # les deux paragraphes Word sont consécutifs, sans ligne vide
    assert m["tirets_cadratins"] == 1
    assert m["antitheses_virgule_pas"] == 1
