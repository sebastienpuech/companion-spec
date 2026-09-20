"""Tests de la mesure de provenance (tools/mesure_provenance.py) — garde 2 de l'audit §6 bis.

Fixture connue : une dictée de cinq phrases ; un candidat qui en reprend trois mot pour mot, une
légèrement réécrite (un mot changé sur douze : 8 4-grammes sur 9 restent dans la dictée, soit
0,89), une inventée. Avec SEUIL_4GRAMMES = 0,6 l'attendu est **4 / 5** : la phrase légèrement
réécrite compte comme dictée. Une réécriture profonde (aucun 4-gramme commun) compte comme Claude.
"""

import json

import tools.mesure_provenance as mp

DICTEE = """# Dictée fixture

> Note de Claude en blockquote : cette phrase n'est pas de Sébastien et ne compte pas.

## Partie 1

Je te le fais à l'oral de façon un peu désordonnée, on verra pour ordonner ensuite. Un compagnon pour moi ça va être une sorte d'assistant avec qui je travaillerai depuis déjà dix ans. Je voulais savoir jusqu'où on peut aller dans ce projet de compagnon.

## Partie 2

Il ne doit surtout pas rendre dépendant, ne pas flatter. Et je n'attends strictement rien du lecteur.
"""  # noqa: E501

CANDIDAT = """# Page de narratif (candidat fixture)

Je te le fais à l'oral de façon un peu désordonnée, on verra pour ordonner ensuite. Un compagnon pour moi ça va être une sorte d'assistant avec qui je travaillerai depuis déjà dix ans. Je voulais savoir jusqu'où on peut aller dans ce projet de mémoire.

Et je n'attends strictement rien du lecteur. ⟦Le marché ne livre pas ces briques faute d'incitation économique.⟧
"""  # noqa: E501

INVENTEE = "Le marché ne livre pas ces briques faute d'incitation économique."


def _prov(candidat: str, dictee: str = DICTEE) -> dict:
    return mp.mesurer_provenance(candidat, dictee)


def test_fixture_connue_quatre_sur_cinq():
    r = _prov(CANDIDAT)
    assert r["phrases"] == 5
    assert r["phrases_dictee"] == 4
    assert r["part_dictee"] == 0.8
    assert [p["phrase"] for p in r["phrases_claude"]] == [INVENTEE]


def test_un_mot_change_sur_douze_reste_dictee():
    r = _prov("Je voulais savoir jusqu'où on peut aller dans ce projet de mémoire.")
    assert r["phrases_dictee"] == 1
    assert r["phrases_claude"] == []


def test_reecriture_profonde_compte_claude():
    r = _prov("Je voulais comprendre jusqu'où un tel projet peut aller.")
    assert r["phrases_dictee"] == 0
    assert r["phrases_claude"][0]["part_4grammes"] == 0.0


def test_coupe_de_la_dictee_compte_dictee():
    r = _prov("Je voulais savoir jusqu'où on peut aller.")
    assert r["phrases_dictee"] == 1


def test_seuil_60_pour_cent_inclus():
    dictee = "Le coach parle le premier quarante quatre jours."
    # 3 4-grammes sur 5 dans la dictée = 0,6 : au seuil, compte comme dictée
    assert (
        mp.mesurer_provenance("Le coach parle le premier quarante deux fois.", dictee)[
            "phrases_dictee"
        ]
        == 1
    )
    # 2 sur 5 = 0,4 : sous le seuil, compte comme Claude
    assert (
        mp.mesurer_provenance("Le coach parle le premier vingt deux fois.", dictee)[
            "phrases_dictee"
        ]
        == 0
    )


def test_normalisation_casse_accents_ponctuation():
    r = mp.mesurer_provenance(
        "bien evidemment quand on voit les derives actuelles",
        "Bien évidemment, quand on voit les dérives actuelles !",
    )
    assert r["part_dictee"] == 1.0


def test_phrase_courte_sous_quatre_mots():
    assert mp.mesurer_provenance("Okay.", "Voilà. Okay.")["phrases_dictee"] == 1
    assert mp.mesurer_provenance("Non.", "Voilà. Okay.")["phrases_dictee"] == 0


def test_blockquote_de_la_dictee_exclu():
    note = "Note de Claude en blockquote : cette phrase n'est pas de Sébastien et ne compte pas."
    assert _prov(note)["phrases_dictee"] == 0


def test_marqueurs_et_ecart():
    non_marquee = "Douze lignes sont à portée de main et personne ne les livre."
    cand = f"Et je n'attends strictement rien du lecteur. ⟦{INVENTEE}⟧ {non_marquee}"
    r = _prov(cand)
    assert r["marqueurs"] == 1
    assert r["phrases_claude_mesurees"] == 2
    assert r["ecart_marqueurs_mesure"] == 1
    assert [p["phrase"] for p in r["phrases_claude"] if not p["marquee"]] == [non_marquee]


def test_dictee_contre_elle_meme_cent_pour_cent():
    r = _prov(DICTEE)
    assert r["part_dictee"] == 1.0
    assert r["phrases_claude"] == []


def test_main_ecrit_le_json(tmp_path):
    (tmp_path / "dictee.md").write_text(DICTEE, encoding="utf-8")
    (tmp_path / "candidat.md").write_text(CANDIDAT, encoding="utf-8")
    sortie = tmp_path / "prov.json"
    code = mp.main(
        [str(tmp_path / "candidat.md"), str(tmp_path / "dictee.md"), "--json", str(sortie)]
    )
    assert code == 0
    m = json.loads(sortie.read_text(encoding="utf-8"))
    assert m["part_dictee"] == 0.8
    assert m["seuil_4grammes"] == mp.SEUIL_4GRAMMES
