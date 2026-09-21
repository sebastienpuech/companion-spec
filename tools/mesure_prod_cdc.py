#!/usr/bin/env python3
"""Mesure de production du coach pour la publication du CDC (correction 4, audit du 03/09/2026).

Lecture seule (URI `mode=ro`) sur la base de production. Chaque mesure est rattachée à UNE
table ; si la table n'existe pas dans la base, la mesure s'écrit « non mesurable » — jamais un
chiffre inventé. La liste complète des tables (avec leur nombre de lignes) est écrite dans le
JSON, ainsi que les tables vides.

Sorties : un JSON daté (défaut instruments/mesures_prod.json) et un tableau markdown
(stdout, ou --md).

Usage :
  python tools/mesure_prod_cdc.py [--db CHEMIN] [--date AAAA-MM-JJ] [--json SORTIE]
                                    [--md SORTIE] [--logs DOSSIER]

Chemin de la base : --db, sinon COACH_DATA_PATH/coach.db, sinon ~/coach-data/coach.db (le dossier
runtime documenté dans CLAUDE.md). Dérogation déclarée à « passer par data.env » : ce script ne
fait que lire, et data.env exige COACH_ENV plus un .env de prod absent du worktree.

--logs DOSSIER : compte, hors base, les divergences de grounding journalisées par le bot
(`[GROUNDING] divergence` dans *.log) — c'est la seule trace des « dérives factuelles », qui
n'ont pas de table.
"""

from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
from datetime import date, datetime
from pathlib import Path

COUNT = "count"
NON_MESURABLE = "non mesurable"
MESURE = "mesuré"

# Les six tables « outillées » que le rapport du 21/08 annonçait comme capacités : si elles sont
# vides, l'aveu reste dans la sortie tant qu'il est vrai (correction 4).
TABLES_ANNONCEES = (
    "hypothese",
    "conviction",
    "feedback_explicite",
    "initiative_coach",
    "poids_releve",
    "situation_event",
)

COACH_PREMIER_SQL = """
select count(distinct p.jour) from (
    select substr(date, 1, 10) as jour, min(date) as d0
    from message_chat group by substr(date, 1, 10)
) p join message_chat m on m.date = p.d0
where m.acteur = 'coach'
"""

# (clé, libellé, table, requête ou dérivation). `sql=COUNT` = count(*) sur la table.
# Jointure des rappels declenches par une question (hors briefing systematique) avec les notes
# qu'ils ont servies. `note_ids` est un tableau JSON : json_each le deplie.
RAPPELS_NOTES = (
    "from memory_recall_log r, json_each(r.note_ids) j"
    " join memoire_note n on n.id = j.value"
    " where r.source in ('auto_recall','tool')"
    " and r.note_ids is not null and r.note_ids <> '[]'"
)
RAPPELS_DECLENCHES = (
    "select count(*) from memory_recall_log where source in ('auto_recall','tool')"
    " and note_ids is not null and note_ids <> '[]'"
)

MESURES: list[dict] = [
    dict(cle="messages", libelle="messages échangés", table="message_chat", sql=COUNT),
    dict(
        cle="messages_coach",
        libelle="messages émis par le coach",
        table="message_chat",
        sql="select count(*) from message_chat where acteur = 'coach'",
    ),
    dict(
        cle="messages_utilisateur",
        libelle="messages émis par l'utilisateur",
        table="message_chat",
        sql="select count(*) from message_chat where acteur <> 'coach'",
    ),
    dict(
        cle="jours_actifs",
        libelle="jours actifs (au moins un échange)",
        table="message_chat",
        sql="select count(distinct substr(date, 1, 10)) from message_chat",
    ),
    dict(
        cle="premier_message",
        libelle="date du premier message",
        table="message_chat",
        sql="select substr(min(date), 1, 10) from message_chat",
    ),
    dict(
        cle="dernier_message",
        libelle="date du dernier message",
        table="message_chat",
        sql="select substr(max(date), 1, 10) from message_chat",
    ),
    dict(
        cle="jours_calendaires",
        libelle="jours calendaires depuis le premier message (inclus, jusqu'à la date de mesure)",
        table="message_chat",
        derive="jours_calendaires",
    ),
    dict(cle="notes_memoire", libelle="notes de mémoire", table="memoire_note", sql=COUNT),
    dict(
        cle="notes_par_statut",
        libelle="notes de mémoire par statut",
        table="memoire_note",
        sql="select statut, count(*) from memoire_note group by statut",
        groupe=True,
    ),
    dict(
        cle="plus_ancienne_note",
        libelle="plus ancienne note",
        table="memoire_note",
        sql="select substr(min(date_creation), 1, 10) from memoire_note",
    ),
    dict(cle="liens_notes", libelle="liens entre notes", table="memory_link", sql=COUNT),
    dict(cle="rappels", libelle="rappels journalisés", table="memory_recall_log", sql=COUNT),
    dict(
        cle="rappels_par_source",
        libelle="rappels journalisés par canal",
        table="memory_recall_log",
        sql="select source, count(*) from memory_recall_log group by source",
        groupe=True,
    ),
    dict(
        cle="seances_importees",
        libelle="séances importées (Strava)",
        table="seance_reelle",
        sql=COUNT,
    ),
    dict(cle="seances_planifiees", libelle="séances planifiées", table="seance_prevue", sql=COUNT),
    dict(
        cle="premiere_seance",
        libelle="première séance importée",
        table="seance_reelle",
        sql="select substr(min(date), 1, 10) from seance_reelle",
    ),
    dict(cle="principes", libelle="principes indexés (KB)", table="principe", sql=COUNT),
    dict(cle="audits_omission", libelle="audits d'omission", table="omission_audit", sql=COUNT),
    dict(
        cle="affirmations_dossier",
        libelle="affirmations du Dossier",
        table="dossier_claim",
        sql=COUNT,
    ),
    dict(
        cle="observations_dossier",
        libelle="observations du Dossier",
        table="dossier_observation",
        sql=COUNT,
    ),
    dict(
        cle="predictions_dossier",
        libelle="prédictions scellées du Dossier",
        table="dossier_prediction",
        sql=COUNT,
    ),
    dict(
        cle="instantanes_modele_mental",
        libelle="instantanés du modèle mental",
        table="user_mental_model",
        sql=COUNT,
    ),
    dict(
        cle="entrees_memoire_coeur",
        libelle="entrées de mémoire de cœur",
        table="core_memory",
        sql=COUNT,
    ),
    dict(cle="intentions", libelle="intentions suivies", table="intention", sql=COUNT),
    dict(
        cle="notes_sanctuarisees",
        libelle="notes sanctuarisées",
        table="memoire_note",
        sql="select count(*) from memoire_note where statut like 'sanctuaris%'",
    ),
    dict(
        cle="retours_explicites",
        libelle="retours explicites",
        table="feedback_explicite",
        sql=COUNT,
    ),
    dict(
        cle="derives_factuelles",
        libelle="dérives factuelles journalisées",
        table=None,
        note="aucune table : le bot les écrit dans ses logs (`_log_grounding_divergence`) — voir --logs",  # noqa: E501
    ),
    dict(cle="convictions", libelle="convictions (table dédiée)", table="conviction", sql=COUNT),
    dict(
        cle="initiatives", libelle="initiatives journalisées", table="initiative_coach", sql=COUNT
    ),
    dict(
        cle="hypotheses",
        libelle="hypothèses N-of-1 tranchées",
        table="hypothese",
        sql="select count(*) from hypothese where verdict is not null",
    ),
    dict(cle="releves_poids", libelle="relevés de poids", table="poids_releve", sql=COUNT),
    dict(cle="chantiers", libelle="chantiers", table="chantier", sql=COUNT),
    dict(
        cle="evenements_situation",
        libelle="événements de situation",
        table="situation_event",
        sql=COUNT,
    ),
    dict(
        cle="anomalies_situation",
        libelle="anomalies de situation détectées",
        table="situation_anomaly",
        sql=COUNT,
    ),
    dict(
        cle="jours_coach_premier",
        libelle="jours où le coach parle le premier (premier message du jour émis par le coach)",
        table="message_chat",
        sql=COACH_PREMIER_SQL,
    ),
    dict(
        cle="part_coach_premier_jours_actifs",
        libelle="part des jours actifs où le coach parle le premier",
        table="message_chat",
        derive="ratio",
        num="jours_coach_premier",
        den="jours_actifs",
    ),
    dict(
        cle="part_coach_premier_jours_calendaires",
        libelle="part des jours calendaires où le coach parle le premier",
        table="message_chat",
        derive="ratio",
        num="jours_coach_premier",
        den="jours_calendaires",
    ),
    dict(
        cle="rappels_declenches",
        libelle="rappels déclenchés par une question (hors briefing systématique)",
        table="memory_recall_log",
        sql=RAPPELS_DECLENCHES,
    ),
    dict(
        cle="notes_servies",
        tables_jointes=("memoire_note",),
        libelle="notes servies par ces rappels",
        table="memory_recall_log",
        sql=f"select count(*) {RAPPELS_NOTES}",
    ),
    dict(
        cle="age_median_note_servie",
        tables_jointes=("memory_recall_log",),
        libelle="âge médian d'une note servie, en jours",
        table="memoire_note",
        sql=(
            "select cast(julianday(r.date) - julianday(n.date_creation) as int) as age "
            f"{RAPPELS_NOTES} order by age limit 1 "
            f"offset (select count(*) {RAPPELS_NOTES})/2"
        ),
    ),
    dict(
        cle="part_notes_servies_plus_30j",
        tables_jointes=("memory_recall_log",),
        libelle="part des notes servies créées il y a plus de 30 jours",
        table="memoire_note",
        sql=(
            "select round(1.0*sum(case when julianday(r.date)-julianday(n.date_creation) > 30 "
            f"then 1 else 0 end)/count(*), 4) {RAPPELS_NOTES}"
        ),
    ),
    dict(
        cle="notes_retour_explicite",
        colonnes_requises=("tags",),
        libelle="notes portant le tag du retour explicite (la table dédiée est vide)",
        table="memoire_note",
        sql="select count(*) from memoire_note where tags like '%feedback_explicite%'",
    ),
    dict(
        cle="predictions_scellees_resolues",
        colonnes_requises=("resolution",),
        libelle="prédictions scellées puis résolues (la table `hypothese` est vide)",
        table="dossier_prediction",
        sql="select count(*) from dossier_prediction where resolution is not null",
    ),
]


def chemin_base_defaut() -> Path:
    env = os.environ.get("COACH_DATA_PATH")
    if env:
        return Path(env) / "coach.db"
    return Path.home() / "coach-data" / "coach.db"


def est_base_de_prod(chemin: Path) -> bool:
    """Vrai si c'est bien COACH_DATA_PATH/coach.db — la seule base qui mesure la réalité.

    Le fichier produit ne porte QU'UN BOOLÉEN, jamais le chemin : `mesures_prod.json` est
    destiné à un dépôt qui peut sortir, et un chemin absolu y publierait le nom du compte.
    """
    try:
        return chemin.resolve() == chemin_base_defaut().resolve()
    except OSError:
        return False


def ouvrir_lecture_seule(chemin: Path) -> sqlite3.Connection:
    """Ouverture en lecture seule (règle de fer n°2) : la base de prod ne s'écrit jamais d'ici."""
    if not chemin.exists():
        raise FileNotFoundError(f"base introuvable : {chemin}")
    return sqlite3.connect(f"file:{chemin.as_posix()}?mode=ro", uri=True)


def lister_tables(conn: sqlite3.Connection) -> dict[str, int | None]:
    noms = [
        r[0]
        for r in conn.execute("select name from sqlite_master where type = 'table' order by name")
    ]
    tables: dict[str, int | None] = {}
    for n in noms:
        try:
            tables[n] = conn.execute(f'select count(*) from "{n}"').fetchone()[0]
        except sqlite3.DatabaseError:
            tables[n] = None  # table virtuelle sqlite-vec : count(*) non supporté
    return tables


def _valeur(conn: sqlite3.Connection, m: dict):
    if m["sql"] == COUNT:
        return conn.execute(f'select count(*) from "{m["table"]}"').fetchone()[0]
    if m.get("groupe"):
        return {str(k): v for k, v in conn.execute(m["sql"]).fetchall()}
    return conn.execute(m["sql"]).fetchone()[0]


def compter_divergences_logs(dossier: Path) -> int | None:
    if not dossier.is_dir():
        return None
    total = 0
    for f in dossier.glob("*.log*"):
        try:
            with f.open(encoding="utf-8", errors="replace") as fh:
                total += sum(1 for ligne in fh if "[GROUNDING] divergence" in ligne)
        except OSError:
            continue
    return total


def mesurer(
    conn: sqlite3.Connection,
    date_mesure: date,
    logs: Path | None = None,
    base: str = "",
    base_prod: bool = True,
) -> dict:
    tables = lister_tables(conn)
    resultats: list[dict] = []
    valeurs: dict[str, object] = {}

    for m in MESURES:
        entree = {"cle": m["cle"], "libelle": m["libelle"], "table": m["table"]}
        if m["table"] is None:
            entree.update(valeur=None, statut=NON_MESURABLE, note=m.get("note", "aucune table"))
        elif manquante := next(
            (n for n in [m["table"], *m.get("tables_jointes", ())] if n not in tables), None
        ):
            entree.update(
                valeur=None, statut=NON_MESURABLE, note=f"table `{manquante}` absente de la base"
            )
        elif col := next(
            (
                c
                for c in m.get("colonnes_requises", ())
                if c not in {r[1] for r in conn.execute(f'pragma table_info("{m["table"]}")')}
            ),
            None,
        ):
            entree.update(
                valeur=None,
                statut=NON_MESURABLE,
                note=f"colonne `{col}` absente de `{m['table']}`",
            )
        elif "derive" in m:
            entree.update(valeur=None, statut=MESURE)  # calculé après, depuis les autres mesures
        else:
            entree.update(valeur=_valeur(conn, m), statut=MESURE)
        resultats.append(entree)
        valeurs[m["cle"]] = entree["valeur"]

    # Dérivations (après les lectures)
    for entree, m in zip(resultats, MESURES):
        if m.get("derive") == "jours_calendaires":
            premier = valeurs.get("premier_message")
            if premier:
                d0 = datetime.strptime(str(premier)[:10], "%Y-%m-%d").date()
                entree["valeur"] = (date_mesure - d0).days + 1
            else:
                entree.update(valeur=None, statut=NON_MESURABLE, note="aucun message")
        elif m.get("derive") == "ratio":
            num, den = valeurs.get(m["num"]), valeurs.get(m["den"])
            if isinstance(num, int) and isinstance(den, int) and den > 0:
                entree["valeur"] = round(num / den, 3)
            else:
                entree.update(valeur=None, statut=NON_MESURABLE, note="dénominateur nul ou absent")
        valeurs[m["cle"]] = entree["valeur"]

    if logs is not None:
        n = compter_divergences_logs(logs)
        for entree in resultats:
            if entree["cle"] == "derives_factuelles" and n is not None:
                entree.update(valeur=n, statut="mesuré hors base (logs)", source=str(logs))

    vides = [n for n, c in tables.items() if c == 0 and not n.startswith("vec_")]
    return {
        "date_mesure": date_mesure.isoformat(),
        "base": base,
        "base_prod": base_prod,
        "nb_tables": len(tables),
        "tables": tables,
        "tables_vides": vides,
        "tables_annoncees_vides": [t for t in TABLES_ANNONCEES if tables.get(t) == 0],
        "tables_annoncees_absentes": [t for t in TABLES_ANNONCEES if t not in tables],
        "mesures": resultats,
    }


def _fmt(v) -> str:
    if v is None:
        return "—"
    if isinstance(v, dict):
        return ", ".join(f"{k} {n}" for k, n in v.items()) or "aucune"
    if isinstance(v, float):
        return f"{v:.1%}".replace(".", ",")
    if isinstance(v, int) and v >= 1000:
        return f"{v:,}".replace(",", " ")
    return str(v)


def tableau_markdown(r: dict) -> str:
    lignes = [
        f"Mesure de production du {r['date_mesure']} — base `{r['base']}`, {r['nb_tables']} tables, lecture seule.",  # noqa: E501
        "",
        "| # | Mesure | Table | Valeur | Statut |",
        "|---|---|---|---|---|",
    ]
    for i, m in enumerate(r["mesures"], 1):
        table = f"`{m['table']}`" if m["table"] else "—"
        statut = m["statut"] + (f" ({m['note']})" if m.get("note") else "")
        lignes.append(f"| {i} | {m['libelle']} | {table} | {_fmt(m['valeur'])} | {statut} |")
    lignes.append("")
    annoncees = ", ".join(f"`{t}`" for t in r["tables_annoncees_vides"]) or "aucune"
    lignes.append(
        f"Tables annoncées comme capacités et toujours vides ({len(r['tables_annoncees_vides'])}) : {annoncees}."  # noqa: E501
    )
    lignes.append(
        f"Tables vides au total (hors index vectoriels) : {len(r['tables_vides'])} — "
        + ", ".join(f"`{t}`" for t in r["tables_vides"])
        + "."
    )
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
    p.add_argument(
        "--db", default=None, help="chemin de coach.db (défaut : COACH_DATA_PATH ou ~/coach-data)"
    )
    p.add_argument("--date", default=None, help="date de mesure AAAA-MM-JJ (défaut : aujourd'hui)")
    p.add_argument("--json", default="instruments/mesures_prod.json")
    p.add_argument("--md", default=None, help="écrire aussi le tableau markdown dans ce fichier")
    p.add_argument(
        "--logs", default=None, help="dossier des logs du bot, pour les divergences de grounding"
    )
    p.add_argument(
        "--hors-prod",
        action="store_true",
        help=(
            "mesurer une base hors production ; le JSON portera base_prod: false "
            "et le verificateur le refusera"
        ),
    )
    args = p.parse_args(argv)

    chemin = Path(args.db) if args.db else chemin_base_defaut()
    base_prod = est_base_de_prod(chemin)
    if not base_prod and not args.hors_prod:
        print(
            "REFUS — cette base n'est pas celle de production (COACH_DATA_PATH/coach.db).\n"
            "Un chiffre tiré d'ailleurs ne mesure rien de réel. Relancer avec --hors-prod "
            "si c'est un essai assumé : le JSON portera base_prod: false.",
            file=sys.stderr,
        )
        return 2
    date_mesure = date.fromisoformat(args.date) if args.date else date.today()
    conn = ouvrir_lecture_seule(chemin)
    try:
        r = mesurer(
            conn,
            date_mesure,
            Path(args.logs) if args.logs else None,
            base=chemin.name,
            base_prod=base_prod,
        )
    finally:
        conn.close()
    md = tableau_markdown(r)
    print(md)
    Path(args.json).write_text(json.dumps(r, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nJSON écrit : {args.json}")
    if args.md:
        Path(args.md).write_text(md + "\n", encoding="utf-8")
        print(f"Markdown écrit : {args.md}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
