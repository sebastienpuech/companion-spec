"""Tests de tools/etats_cdc.py : import du tableau de couverture, règles des cinq états, kit."""

import json

import tools.etats_cdc as ec


def _mesures(**valeurs):
    return {"mesures": [{"cle": k, "valeur": v, "statut": "mesuré"} for k, v in valeurs.items()]}


def _dims_complets(etat="à construire", **surcharges):
    dims = []
    for i in ec.IDS:
        d = {
            "id": i,
            "nom": f"nom {i}",
            "etat": etat,
            "justification": "test",
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
            "D01": {"etat": "en service", "mesure": "notes_memoire"},
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
