"""Tests de tools/etats_cdc.py : import du tableau de couverture, règles des cinq états, kit."""

import json
from datetime import date, timedelta
from pathlib import Path

import pytest

import tools.etats_cdc as ec


def _mesures(base_prod=True, date_mesure=None, **valeurs):
    return {
        "base_prod": base_prod,
        "date_mesure": date_mesure or date.today().isoformat(),
        "mesures": [{"cle": k, "valeur": v, "statut": "mesuré"} for k, v in valeurs.items()],
    }


JUSTIF = "justification de test, assez longue pour franchir le seuil des quarante"


def _dims_complets(etat="à construire", justification=JUSTIF, **surcharges):
    dims = []
    for i in ec.IDS:
        d = {
            "id": i,
            "nom": f"nom {i}",
            "etat": etat,
            "justification": justification,
            "mesure": None,
            "artefact": None,
        }
        d.update(surcharges.get(i, {}))
        dims.append(d)
    return {"dimensions": dims}


def test_blocs_couvrent_exactement_les_56():
    ids = [d for ds in ec.BLOCS.values() for d in ds]
    assert sorted(ids) == ec.IDS and len(ids) == 56
    assert sum(len(v) for v in ec.ABSENTES_E4.values()) == 17


def test_importer_couverture_depuis_texte(tmp_path):
    txt = (
        "| Bloc | Dimension | Ce qui s’en approche le plus | Couverture |\n"
        "| Le cadre | GARDE-FOUS (D00) | politiques de sécurité | Partiel |\n"
        "| Le cadre | Loyauté fiduciaire (D47) | aucun acteur | Absent |\n"
        "| Mauvais bloc | MÉMOIRE (D01) | Letta, Mem0 | Couvert |\n"
        "| pas | une | ligne | valide | ici |\n"
    )
    f = tmp_path / "B.txt"
    f.write_text(txt, encoding="utf-8")
    r = ec.importer_couverture(f)
    assert r["nb_lignes"] == 3
    assert r["comptes"] == {"partiel": 1, "absent": 1, "couvert": 1}
    assert r["lignes"][1] == {
        "id": "D47",
        "bloc": "Le cadre",
        "nom": "Loyauté fiduciaire",
        "approche": "aucun acteur",
        "couverture": "absent",
    }
    assert len(r["manquantes"]) == 53 and r["doublons"] == []
    assert r["ecarts_blocs"] == [
        "D01 : « Mauvais bloc » ≠ « Mémoire et connaissance de la personne »"
    ]


def test_regles_des_etats():
    etats = _dims_complets(
        **{
            "D01": {
                "etat": "en service",
                "mesure": "notes_memoire",
                "artefact": "memory/retrieval.py:120",
            },
            "D45": {
                "etat": "outillé sans usage",
                "mesure": "hypotheses",
                "artefact": "table hypothese",
            },
            "D34": {"etat": "amorcé", "mesure": "jours_coach_premier"},
            "D47": {"etat": "acquis sans code"},
        }
    )
    v = ec.verifier(etats, _mesures(notes_memoire=247, hypotheses=0, jours_coach_premier=44))
    assert v["ok"], v["erreurs"]
    assert v["par_etat"] == {
        "en service": 1,
        "acquis sans code": 1,
        "outillé sans usage": 1,
        "amorcé": 1,
        "à construire": 52,
    }
    assert v["par_bloc"]["Le cadre"]["acquis sans code"] == 1
    assert sum(sum(c.values()) for c in v["par_bloc"].values()) == 56


def test_en_service_sans_mesure_non_nulle_est_refuse():
    etats = _dims_complets(
        **{
            "D01": {"etat": "en service", "mesure": "hypotheses"},
            "D02": {"etat": "en service", "mesure": None},
            "D03": {"etat": "en service", "mesure": "inconnue_ici"},
        }
    )
    v = ec.verifier(etats, _mesures(hypotheses=0))
    assert not v["ok"]
    assert any("D01 en service" in e and "nulle" in e for e in v["erreurs"])
    assert any("D02 en service sans mesure" in e for e in v["erreurs"])
    assert any("D03 en service" in e and "absente" in e for e in v["erreurs"])


def test_outille_avec_mesure_non_nulle_et_etat_inconnu_refuses():
    etats = _dims_complets(
        **{
            "D45": {"etat": "outillé sans usage", "mesure": "notes_memoire", "artefact": "x"},
            "D46": {"etat": "en cours"},
        }
    )
    v = ec.verifier(etats, _mesures(notes_memoire=3))
    assert any("D45 outillé sans usage" in e and "non nulle" in e for e in v["erreurs"])
    assert any("D46" in e and "hors liste" in e for e in v["erreurs"])


def test_couverture_par_bloc_et_absentes():
    etats = _dims_complets()
    lignes = []
    absentes = [i for ids in ec.ABSENTES_E4.values() for i in ids]
    for i in ec.IDS:
        lignes.append(
            {
                "id": i,
                "bloc": ec.BLOC_DE[i],
                "nom": "",
                "approche": "",
                "couverture": "absent"
                if i in absentes
                else ("couvert" if i == "D01" else "partiel"),
            }
        )
    v = ec.verifier(etats, _mesures(), {"lignes": lignes})
    assert v["ok"], v["erreurs"]
    assert v["couverture_evaluateur1_par_bloc"]["Mémoire et connaissance de la personne"] == {
        "couvert": 1,
        "partiel": 4,
        "absent": 1,
    }
    assert len(v["absentes"]) == 17
    p = ec.bloc_le_plus_couvert(v["couverture_evaluateur1_par_bloc"])
    assert p["plus_de_couvert"] == "Mémoire et connaissance de la personne" and p["couvert"] == 1
    md = ec.rapport_markdown(v, etats)
    assert "Bloc le plus couvert" in md and "| terrain de recherche | D14" in md


def test_absentes_differentes_de_e4_signalees():
    etats = _dims_complets()
    lignes = [
        {
            "id": i,
            "bloc": ec.BLOC_DE[i],
            "nom": "",
            "approche": "",
            "couverture": "absent" if i == "D01" else "couvert",
        }
        for i in ec.IDS
    ]
    v = ec.verifier(etats, _mesures(), {"lignes": lignes})
    assert any("≠ les 17" in e for e in v["erreurs"])


def test_definition_et_kit(tmp_path):
    fiches = tmp_path / "dimensions"
    fiches.mkdir()
    (fiches / "D01-memoire.md").write_text(
        "# D01 — MÉMOIRE\n\ncorps\n\n## FICHE SYNTHÈSE\n\n**D01 — MÉMOIRE (architecture)** (capacité). Le compagnon "  # noqa: E501
        "n'a pas de trou de mémoire : registres multiples (a, b). Critère central : zéro re-briefing.\n",  # noqa: E501
        encoding="utf-8",
    )
    defs = ec.definitions(fiches)
    assert defs == {"D01": "Le compagnon n'a pas de trou de mémoire : registres multiples (a, b)."}
    etats = _dims_complets()
    couv = {
        "lignes": [
            {
                "id": "D01",
                "bloc": "x",
                "nom": "",
                "approche": "Letta | Mem0",
                "couverture": "couvert",
            }
        ]
    }
    md = ec.kit_markdown(etats, couv, defs)
    assert "| D01 | nom D01 | Le compagnon n'a pas de trou de mémoire" in md
    assert "Letta ／ Mem0" in md  # la barre verticale ne casse pas le tableau
    assert md.count("\n| D") == 56
    assert "(fiche introuvable)" in md  # les 55 autres n'ont pas de fiche dans ce test


def test_main_verifier_code_retour(tmp_path):
    etats = tmp_path / "etats.json"
    etats.write_text(json.dumps(_dims_complets()), encoding="utf-8")
    mesures = tmp_path / "mesures.json"
    mesures.write_text(json.dumps(_mesures()), encoding="utf-8")
    assert ec.main(["verifier", "--etats", str(etats), "--mesures", str(mesures)]) == 0


# --- Durcissements D8 de la session 0 du plan des 11 briques (20/09/2026) ---------------------
# (a) « en service » exige un artefact, comme « outillé sans usage » le fait déjà.
# (d) justification d'au moins 40 caractères, artefact porteur d'une ancre repérable.


def test_en_service_sans_artefact_est_refuse():
    """(a) — la dissymétrie relevée au §0.2 de spec_produit.md : :184-193 contre :206-207."""
    etats = _dims_complets(**{"D01": {"etat": "en service", "mesure": "notes_memoire"}})
    v = ec.verifier(etats, _mesures(notes_memoire=247))
    assert not v["ok"]
    assert any("D01" in e and "artefact" in e for e in v["erreurs"]), v["erreurs"]


def test_en_service_avec_artefact_reste_accepte():
    etats = _dims_complets(
        **{
            "D01": {
                "etat": "en service",
                "mesure": "notes_memoire",
                "artefact": "memory/retrieval.py:120",
            }
        }
    )
    v = ec.verifier(etats, _mesures(notes_memoire=247))
    assert v["ok"], v["erreurs"]


def test_justification_trop_courte_est_refusee():
    """(d) — une justification de complaisance tient en trois mots ; le seuil est à 40."""
    etats = _dims_complets(**{"D02": {"justification": "parce que"}})
    v = ec.verifier(etats, _mesures())
    assert not v["ok"]
    assert any("D02" in e and "justification" in e and "40" in e for e in v["erreurs"]), v[
        "erreurs"
    ]


def test_artefact_sans_ancre_est_refuse():
    """(d) — « il y a du code quelque part » n'est pas un artefact : rien ne s'y ouvre."""
    etats = _dims_complets(
        **{
            "D45": {
                "etat": "outillé sans usage",
                "mesure": "hypotheses",
                "artefact": "il y a du code quelque part dans le depot",
            }
        }
    )
    v = ec.verifier(etats, _mesures(hypotheses=0))
    assert not v["ok"]
    assert any("D45" in e and "ancre" in e for e in v["erreurs"]), v["erreurs"]


@pytest.mark.parametrize(
    "artefact",
    [
        "kb/ingestion et kb/runtime, tools kb_search et kb_pivot",  # noms de DOSSIER — c'est D39
        "bot/telegram_bot.py:2313 _ground_reply",
        "table hypothese",
        "tool memory_extract",
        "scripts/scheduled/briefing_matinal.py",
    ],
)
def test_artefact_avec_ancre_est_accepte(artefact):
    """(d) — refuser les noms de DOSSIER ferait tomber D39 : c'est la réserve du patch v2.1."""
    etats = _dims_complets(
        **{"D45": {"etat": "outillé sans usage", "mesure": "hypotheses", "artefact": artefact}}
    )
    v = ec.verifier(etats, _mesures(hypotheses=0))
    assert v["ok"], v["erreurs"]


def test_les_56_lignes_reelles_passent_les_durcissements_a_et_d():
    """Le contrôle qui compte : aucune des 56 lignes publiées ne tombe (vérifié le 20/09/2026)."""
    racine = Path(__file__).resolve().parents[2]
    etats = json.loads((racine / "etats/etats.json").read_text(encoding="utf-8"))
    mesures = json.loads(
        (racine / "instruments/mesures_prod.json").read_text(encoding="utf-8")
    )
    v = ec.verifier(etats, mesures)
    fautifs = [e for e in v["erreurs"] if "artefact" in e or "justification" in e or "ancre" in e]
    assert fautifs == [], fautifs


# --- Durcissement (b) : d'où vient ce fichier de mesures, et de quand date-t-il ? ------------


def test_mesures_hors_prod_sont_refusees():
    """Le trou (b) du §0.2 : --db acceptait n'importe quelle base, personne ne le voyait."""
    v = ec.verifier(_dims_complets(), _mesures(base_prod=False))
    assert not v["ok"]
    assert any("prod" in e for e in v["erreurs"]), v["erreurs"]


def test_mesures_sans_cle_de_provenance_sont_refusees():
    """Un fichier d'avant le durcissement n'a pas la clé : il ne passe pas pour autant."""
    mesures = _mesures()
    del mesures["base_prod"]
    v = ec.verifier(_dims_complets(), mesures)
    assert not v["ok"]
    assert any("base_prod" in e for e in v["erreurs"]), v["erreurs"]


def test_mesures_d_hier_sont_refusees():
    """Un COUNT cumulatif d'hier ne dit rien de l'état d'aujourd'hui."""
    hier = (date.today() - timedelta(days=1)).isoformat()
    v = ec.verifier(_dims_complets(), _mesures(date_mesure=hier))
    assert not v["ok"]
    assert any("date_mesure" in e or "jour" in e for e in v["erreurs"]), v["erreurs"]


def test_le_jour_de_reference_est_injectable():
    """Pour rejouer une vérification d'une autre date sans mentir sur celle du jour."""
    hier = (date.today() - timedelta(days=1)).isoformat()
    v = ec.verifier(_dims_complets(), _mesures(date_mesure=hier), jour=hier)
    assert v["ok"], v["erreurs"]


def test_le_fichier_de_mesures_reel_porte_sa_provenance():
    """Le contrôle sur le vrai fichier régénéré en session 0."""
    racine = Path(__file__).resolve().parents[2]
    m = json.loads((racine / "instruments/mesures_prod.json").read_text(encoding="utf-8"))
    assert m["base_prod"] is True
    assert m["date_mesure"] == "2026-09-20"


# --- Durcissement (c) : une ligne peut-elle redescendre sans que personne ne le voie ? --------


def _instantane(**etats):
    base = {i: "à construire" for i in ec.IDS}
    base.update(etats)
    return {"date": "2026-09-20", "motif": "test", "etats": base}


def test_comparer_detecte_une_retrogradation():
    """A5 : « en service » est irréversible de fait, faute de quoi que ce soit qui le regarde."""
    avant = _instantane(D01="en service")
    apres = _dims_complets(**{"D01": {"etat": "amorcé"}})
    r = ec.comparer(apres, avant)
    assert not r["ok"]
    assert [x["id"] for x in r["retrogradees"]] == ["D01"]
    assert r["retrogradees"][0]["avant"] == "en service"
    assert r["retrogradees"][0]["apres"] == "amorcé"


def test_comparer_accepte_une_progression():
    avant = _instantane(D01="outillé sans usage")
    apres = _dims_complets(**{"D01": {"etat": "en service"}})
    r = ec.comparer(apres, avant)
    assert r["ok"], r["retrogradees"]
    assert [x["id"] for x in r["promues"]] == ["D01"]


def test_comparer_signale_une_ligne_disparue():
    avant = _instantane(D01="en service")
    apres = _dims_complets()
    apres["dimensions"] = [d for d in apres["dimensions"] if d["id"] != "D01"]
    r = ec.comparer(apres, avant)
    assert not r["ok"]
    assert any("D01" in x for x in r["erreurs"]), r["erreurs"]


def test_comparer_ne_voit_pas_de_retrogradation_sur_le_reel():
    """L'instantané de départ et etats.json disent la même chose le jour où on l'écrit."""
    racine = Path(__file__).resolve().parents[2]
    etats = json.loads((racine / "etats/etats.json").read_text(encoding="utf-8"))
    avant = json.loads(
        (racine / "couverture/instantane_etats_2026-09-20.json").read_text(
            encoding="utf-8"
        )
    )
    r = ec.comparer(etats, avant)
    assert r["ok"], r["retrogradees"]
    assert r["retrogradees"] == [] and r["promues"] == []


def test_instantane_porte_les_comptes_attendus_de_l_annexe():
    """D2 : les deux constantes sortent du code d'annexe_56.py pour devenir modifiables exprès."""
    racine = Path(__file__).resolve().parents[2]
    avant = json.loads(
        (racine / "couverture/instantane_etats_2026-09-20.json").read_text(
            encoding="utf-8"
        )
    )
    assert avant["attendu_couverture"] == {"couvert": 8, "partiel": 31, "absent": 17}
    assert avant["attendu_etats"] == {
        "en service": 3,
        "acquis sans code": 2,
        "outillé sans usage": 3,
        "amorcé": 16,
        "à construire": 32,
    }
    assert len(avant["etats"]) == 56


def test_main_comparer_code_retour(tmp_path):
    racine = Path(__file__).resolve().parents[2]
    avant = tmp_path / "avant.json"
    avant.write_text(
        json.dumps(_instantane(D01="en service"), ensure_ascii=False), encoding="utf-8"
    )
    apres = tmp_path / "etats.json"
    apres.write_text(
        json.dumps(_dims_complets(**{"D01": {"etat": "amorcé"}}), ensure_ascii=False),
        encoding="utf-8",
    )
    assert ec.main(["comparer", "--etats", str(apres), "--avant", str(avant)]) == 1
    assert (
        ec.main(
            [
                "comparer",
                "--etats",
                str(racine / "etats/etats.json"),
                "--avant",
                str(racine / "couverture/instantane_etats_2026-09-20.json"),
            ]
        )
        == 0
    )
