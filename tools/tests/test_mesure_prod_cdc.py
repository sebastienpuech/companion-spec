"""Tests de tools/mesure_prod_cdc.py sur une base SQLite en mémoire à 3 lignes connues."""

import sqlite3
from datetime import date

import tools.mesure_prod_cdc as mp


def _base_memoire() -> sqlite3.Connection:
    c = sqlite3.connect(":memory:")
    c.executescript(
        """
        create table message_chat (id integer primary key, date text, acteur text, contenu text);
        insert into message_chat (date, acteur, contenu) values
            ('2026-05-01 08:00:00', 'coach', 'bonjour'),
            ('2026-05-01 09:00:00', 'sebastien', 'salut'),
            ('2026-05-02 07:00:00', 'sebastien', 'séance faite');
        create table memoire_note (id integer primary key, date_creation text, statut text);
        insert into memoire_note (date_creation, statut) values
            ('2026-06-28T17:52:23', 'actif'), ('2026-07-01T10:00:00', 'actif'),
            ('2026-07-02T10:00:00', 'sanctuarisé');
        create table memory_link (id integer primary key);
        """
    )
    return c


def _par_cle(r: dict) -> dict:
    return {m["cle"]: m for m in r["mesures"]}


def test_mesures_connues():
    r = mp.mesurer(_base_memoire(), date(2026, 5, 4), base="test.db")
    m = _par_cle(r)
    assert m["messages"]["valeur"] == 3
    assert m["messages_coach"]["valeur"] == 1
    assert m["jours_actifs"]["valeur"] == 2
    assert m["premier_message"]["valeur"] == "2026-05-01"
    assert m["jours_calendaires"]["valeur"] == 4  # du 01/05 au 04/05 inclus
    assert m["jours_coach_premier"]["valeur"] == 1  # le 01/05 seulement
    assert m["part_coach_premier_jours_actifs"]["valeur"] == 0.5
    assert m["part_coach_premier_jours_calendaires"]["valeur"] == 0.25
    assert m["notes_memoire"]["valeur"] == 3
    assert m["notes_sanctuarisees"]["valeur"] == 1
    assert m["notes_par_statut"]["valeur"] == {"actif": 2, "sanctuarisé": 1}
    assert m["plus_ancienne_note"]["valeur"] == "2026-06-28"
    assert m["liens_notes"]["valeur"] == 0 and m["liens_notes"]["statut"] == mp.MESURE


def test_table_absente_donne_non_mesurable_jamais_un_chiffre():
    r = mp.mesurer(_base_memoire(), date(2026, 5, 4))
    m = _par_cle(r)
    assert m["hypotheses"]["statut"] == mp.NON_MESURABLE
    assert m["hypotheses"]["valeur"] is None
    assert "absente" in m["hypotheses"]["note"]
    assert m["derives_factuelles"]["statut"] == mp.NON_MESURABLE
    assert m["derives_factuelles"]["table"] is None


def test_chaque_mesure_a_une_table_ou_est_non_mesurable():
    r = mp.mesurer(_base_memoire(), date(2026, 5, 4))
    for m in r["mesures"]:
        assert m["table"] or m["statut"] == mp.NON_MESURABLE, m["cle"]


def test_tables_et_vides():
    r = mp.mesurer(_base_memoire(), date(2026, 5, 4))
    assert r["nb_tables"] == 3
    assert r["tables"]["message_chat"] == 3
    assert r["tables_vides"] == ["memory_link"]
    assert r["tables_annoncees_vides"] == []
    assert set(r["tables_annoncees_absentes"]) == set(mp.TABLES_ANNONCEES)


def test_logs_comptent_les_divergences(tmp_path):
    (tmp_path / "bot.log").write_text(
        "x\n[GROUNDING] divergence type=a source=b\nrien\n[GROUNDING] divergence type=c source=d\n",
        encoding="utf-8",
    )
    r = mp.mesurer(_base_memoire(), date(2026, 5, 4), logs=tmp_path)
    m = _par_cle(r)
    assert m["derives_factuelles"]["valeur"] == 2
    assert m["derives_factuelles"]["statut"] == "mesuré hors base (logs)"


def test_tableau_markdown_liste_tout():
    r = mp.mesurer(_base_memoire(), date(2026, 5, 4), base="test.db")
    md = mp.tableau_markdown(r)
    assert md.count("\n| ") == len(mp.MESURES) + 1  # une ligne par mesure + l'en-tête
    assert "non mesurable" in md
