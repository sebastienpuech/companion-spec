"""Tests de la copie de l'essai par l'import.

Chaque test monte une source et une cible jetables : le vrai dépôt n'est jamais touché.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from tools.importer_depuis_source import ESSAI, copier_essai


def _source(tmp_path: Path, contenu: bytes = b"# Essai\n\nUne ligne.\n") -> Path:
    src = tmp_path / "source" / ESSAI[0]
    src.parent.mkdir(parents=True)
    src.write_bytes(contenu)
    return tmp_path / "source"


def test_import_copie_puis_identique(tmp_path):
    source, cible = _source(tmp_path), tmp_path / "cible"
    assert copier_essai(source, cible, ecrire=True) == "identique"
    assert (cible / ESSAI[1]).read_bytes() == (source / ESSAI[0]).read_bytes()


def test_import_garde_les_fins_de_ligne(tmp_path):
    source, cible = _source(tmp_path, b"a\nb\n"), tmp_path / "cible"
    copier_essai(source, cible, ecrire=True)
    assert b"\r\n" not in (cible / ESSAI[1]).read_bytes()


def test_verifier_voit_un_ecart_sans_ecrire(tmp_path):
    source, cible = _source(tmp_path), tmp_path / "cible"
    copier_essai(source, cible, ecrire=True)
    (source / ESSAI[0]).write_bytes(b"# Essai\n\nUne ligne retouchee.\n")
    avant = (cible / ESSAI[1]).read_bytes()
    assert copier_essai(source, cible, ecrire=False) == "différent"
    assert (cible / ESSAI[1]).read_bytes() == avant


def test_verifier_cible_absente(tmp_path):
    assert copier_essai(_source(tmp_path), tmp_path / "cible", ecrire=False) == "absent"


def test_source_absente_arrete(tmp_path):
    with pytest.raises(SystemExit):
        copier_essai(tmp_path / "vide", tmp_path / "cible", ecrire=True)
