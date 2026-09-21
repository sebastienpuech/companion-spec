# Les instruments

Ce que ce dépôt mesure, avec quoi, et ce qu'un tiers peut rejouer ou non.

| Instrument | Ce qu'il mesure | Rejouable par un tiers ? |
|---|---|---|
| `tools/check_citations.py` | Résout chaque citation des fiches chez arXiv, Crossref ou Semantic Scholar, et vérifie que le premier auteur et l'année concordent | **Oui**, avec un accès réseau (~20 min) |
| `tools/importer_depuis_source.py --verifier` | Recompte les fiches, les citations, les lignes de couverture, et rejoue le grep de confidentialité | **Oui** pour les comptes de citations et de couverture ; la comparaison de sha256 exige la source privée |
| `tools/mesure_tells.py` | Les marques d'écriture de modèle dans un texte (voir `tells_etalonnage.md`) | **Oui**, sur n'importe quel `.md`, `.txt` ou `.docx` |
| `tools/mesure_provenance.py` | Quelle part d'un texte vient mot pour mot d'un texte source (4-grammes) | **Oui** |
| `tools/notes_juges.py` + `tools/accord_juges.py` | Le gabarit de notation des 56 lignes, sa vérification de forme, puis le κ de Fleiss à trois juges | **Oui** — c'est fait pour |
| `tools/etats_cdc.py` | Vérifie les cinq états des 56 lignes et calcule les comptes par état et par bloc | **Partiellement** : la vérification de forme tourne sur `etats/etats.json`, le contrôle « en service ⇒ mesure non nulle » a besoin de `mesures_prod.json` |
| `tools/mesure_prod_cdc.py` | 43 mesures de la production du pilote, chacune rattachée à sa table, en lecture seule | **Non — nécessite la base du pilote, qui n'est pas fournie.** Le script et ses sorties datées sont publiés ; la base ne l'est pas |

## Les sorties datées

- `mesures_prod.json` et `mesures_prod.md` — les 43 mesures du **20/09/2026**, chacune avec sa
  table d'origine et son statut. Six tables annoncées par la spécification du pilote y sont
  **toujours vides** : c'est ce qui fait basculer trois lignes en « outillé sans usage » plutôt
  qu'en « en service ». Le fichier dit ce qui est en base ; `../note_methode.md` dit ce que ça
  vaut.
- `tells_these.json`, `tells_limites.json` — les compteurs des deux passages publiés, du
  **06/09/2026**, reproductibles par les deux commandes de `tells_etalonnage.md`.

## Trois choses à savoir avant de lire les chiffres

1. **Un nom de table porte le prénom de l'auteur** (`retour_sebastien`), et une valeur de la base
   vaut `sebastien`. Ce sont des identifiants d'un système à une seule personne, écrits en mai
   2026 ; ils sont publiés tels quels, comme le reste du dépôt, l'auteur ayant tranché le
   04/09/2026 pour son nom réel. Rien n'y est renommé après coup : un identifiant réécrit pour la
   publication rendrait les mesures non rejouables.
2. **`etats/etats.json` nomme son script par son chemin d'origine** (`scripts/etats_cdc.py`).
   Dans ce dépôt, le script est à `tools/etats_cdc.py`. Le fichier de données n'a pas été retouché
   — il est copié octet pour octet depuis la source, et c'est ce qui permet de comparer son
   empreinte.
3. **Les scripts copiés portent deux retouches, et deux seulement** : le nom du paquet
   (`scripts.` devient `tools.`) et les chemins par défaut, adaptés à la disposition de ce dépôt.
   Aucune logique de mesure n'a été touchée, et `tools/tests/` le vérifie — 106 tests au
   21/09/2026.

```bash
python -m pytest tools/tests -q
```
