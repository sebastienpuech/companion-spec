"""Rend la racine du dépôt importable pour les tests (`import tools.X`)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
