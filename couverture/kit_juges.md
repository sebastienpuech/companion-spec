# Kit des juges — couverture des 56 lignes par les systèmes publics

Correction 3 de l'audit de publiabilité du 03/09/2026. Écrit le 04/09/2026.
**Réécrit le 07/09/2026** (session 4) : les 56 définitions ont été reprises une à une pour nommer
le geste à noter, et la colonne d'exemples a été vidée de tout verdict. Ce qui a changé et
pourquoi : `docs/cdc/publication/kit_relecture.md`.

## Pourquoi ce kit

Le tableau de couverture de départ (**8 couvert / 31 partiel / 17 absent**) est la notation
d'**un seul évaluateur** (Claude, rapport du 21/08/2026). Le 20/09/2026, un juge modèle
a noté les 56 lignes, puis 55 le 21/09 (D28 sans note au second passage), à la place de juge 3
(point 5) ; la thèse s'appuie désormais sur
les 9 lignes absentes pour les trois notations, et la place de juge 2 reste à un humain. Le travail publiera l'accord de trois
juges, **tel quel, même mauvais** (audit §6.3). Les juges sont choisis par l'orchestrateur ; la
notation se fait hors session, sans Claude.

## Les pièces

| Pièce | Fichier | Produit par |
|---|---|---|
| Le tableau des 56 lignes à noter : dimension, **le cœur à noter** (une phrase), **les sous-parties** (qui ne déterminent pas la note), **les pistes à examiner** (des produits, sans verdict), colonne vide | `docs/cdc/publication/kit_juges_tableau.md` | `scripts/etats_cdc.py kit --definitions` (rejouable) |
| La source relue des 56 lignes : pour chaque ligne, sa définition, ses sous-parties, ses pistes, **et la ligne de la fiche d'où sort son cœur** | `docs/cdc/publication/kit_definitions.json` | relecture ligne à ligne, 07/09/2026 |
| Le contrôle mécanique du kit : longueur et nombre de phrases des définitions, détection des formules de verdict dans la colonne « pistes », numérotation figée | `scripts/verifie_kit.py` (tests : `tests/test_verifie_kit.py`) | — |
| La feuille de notation, une ligne par dimension, colonnes `juge1;juge2;juge3` vides — **générée à la demande, non versionnée** : le garde-fou pre-push refuse toute extension `.csv` | `python scripts/accord_juges.py --gabarit docs/cdc/publication/etats.json --sortie kit_juges_notes.csv` | `scripts/accord_juges.py --gabarit` |
| Le dépouillement : κ de Fleiss à trois juges, accord par paire, unanimité / majorité / désaccord, comptes par juge et par vote majoritaire | `scripts/accord_juges.py` (tests : `tests/test_accord_juges.py`, dont l'exemple publié de Fleiss 1971, κ = 0,210) | — |
| Les fiches complètes (définition, mécanisme humain, comportement attendu, état de l'art) — la référence en cas de doute sur une ligne | `docs/cdc/dimensions/Dnn-*.md` | étape 2, validées le 13/08 |
| La notation de l'évaluateur 1, **à ne pas montrer aux juges** | `docs/cdc/publication/couverture_evaluateur1_2026-08-21.json` | `scripts/etats_cdc.py importer-couverture` |

## Comment lire une ligne du tableau

Trois colonnes, et une seule décide de la note.

- **« Ce qui est noté : le cœur de la ligne »** — c'est la colonne qui décide. Une phrase, qui nomme
  le geste central. C'est sur ce geste-là, et sur rien d'autre, que porte votre note.
- **« Sous-parties »** — ce que la fiche complète détaille. Elles disent où regarder. **Elles ne
  déterminent pas la note** : un produit qui coche plusieurs sous-parties sans faire le geste
  central n'est pas `couvert`, et un produit qui fait le geste central sans cocher toutes les
  sous-parties peut l'être.
- **« Pistes à examiner »** — des produits par où commencer. **Cette liste ne porte aucun jugement
  et n'est pas exhaustive.** Elle ne dit pas que ces produits couvrent la ligne, ni qu'ils ne la
  couvrent pas. Un juge qui note à partir d'un produit absent de la liste fait exactement son
  travail ; un juge qui recopie la liste ne le fait pas.

## Consignes aux juges (à recopier telles quelles)

1. **À l'aveugle.** Vous ne voyez ni les notes de l'évaluateur 1, ni celles des autres juges. La
   colonne « pistes à examiner » est un point de départ, pas une proposition de réponse.
2. **L'échelle, trois valeurs.** `couvert` : un système public déployé, disponible aujourd'hui au
   grand public, fait le **cœur** de la ligne tel que la première colonne le définit. `partiel` :
   un système fait une partie du cœur, ou le fait sans la durée, la profondeur ou l'initiative que
   le cœur exige. `absent` : aucun système public ne le fait — un papier de recherche, une démo ou
   une brique pour développeurs ne comptent pas.
3. **La preuve.** Pour toute ligne notée `couvert` ou `partiel` : le **produit**, sa **version ou la
   date** à laquelle vous l'avez observé, et la **fonction précise** qui fait la couverture (une
   colonne `preuve` ajoutée au CSV, ou une note numérotée). Sans produit nommé, la note vaut
   `absent`.
4. **Le doute.** En cas d'hésitation entre deux valeurs, prenez la plus basse et écrivez pourquoi :
   l'accord se calcule sur ce que vous avez écrit, pas sur ce que vous auriez voulu dire.
5. **Le temps, et le biais qu'il porte.** Comptez **5 à 8 heures** pour les 56 lignes, en deux ou
   trois séances ; datez chaque séance en tête du fichier. Ce n'est pas une estimation de confort :
   **le temps que vous prendrez change la note.** Chercher un produit prend du temps ; ne pas le
   trouver conduit à `absent` (point 3). Un juge pressé produit donc mécaniquement des `absent`.
   **Si vous manquez de temps sur une ligne, écrivez-le au lieu de la noter** — une ligne non notée
   est une donnée exploitable, une ligne notée à la va-vite ne l'est pas. Aucune aide d'un modèle de
   langage pour noter. **Un modèle peut servir de juge 3** à la place d'un humain — seul, sans
   contexte, et déclaré comme tel — mais il ne produit pas le même objet : chronométré le
   07/09/2026 sur cinq lignes tirées au sort, un juge modèle avec recherche web a noté en **50
   secondes par ligne** (≈ 46 minutes pour 56), en s'appuyant sur des résumés de recherche plutôt
   que sur les pages primaires — 4 pages ouvertes pour 15 recherches. **Si un modèle est juge 3, le
   κ mélange deux régimes de preuve, et la publication doit le dire.**
6. **Une ligne mêle plusieurs choses ?** C'est possible : la numérotation des 56 lignes est figée
   et publiée, aucune n'a été scindée. Notez le **cœur** nommé dans la première colonne, signalez
   la gêne en commentaire, et passez. La gêne signalée est une donnée, pas un échec.
7. **Les sept dernières lignes (D49 à D55) se notent sur leur geste propre, et sur lui seul.** Ce
   sont des déclinaisons : elles appliquent à un domaine des capacités déjà notées ailleurs dans la
   grille. **N'y rejugez pas les capacités génériques.** D51 (« ressort le bon dossier au bon
   moment ») ne se note pas sur la qualité de la mémoire en général — celle-là est D01, et vous
   l'avez déjà notée. Sans cette règle, deux juges peuvent diverger sur la seule façon de pondérer
   des critères hérités, ce qui abaisse l'accord sans rien dire des produits.
8. **Certaines lignes peuvent vous paraître impossibles à couvrir : notez ce que vous constatez, sans chercher pourquoi.** Quelques-unes décrivent un comportement dont aucun produit grand public ne se réclame aujourd'hui — mesurer qu'on réduit son propre usage, s'engager par un devoir opposable, être disponible sans aucune mécanique de rétention. **Les raisons de cette absence ne vous sont pas demandées et ne doivent pas entrer dans votre note** : elles font l'objet d'un débat que votre notation doit pouvoir trancher, non confirmer. Un contre-exemple est précieux. Signalez toute ligne qui vous paraît invérifiable de l'extérieur : c'est une donnée.

   *Point 8 réécrit le 20/09/2026. Les deux passages du juge modèle des 20 et 21/09/2026 ont
   été notés avec la version précédente, qui titrait : « Certaines lignes ne peuvent pas être
   `couvert`, et ce n'est pas un piège. »*

### D'où vient le « 5 à 8 heures »

Le kit annonçait **2 à 3 heures** jusqu'au 07/09/2026. Un juge à blanc, en contexte frais, a estimé
qu'il en faut **5 à 8** pour respecter la règle de preuve du point 3, et que 2-3 h ne tiennent
« qu'en sautant la preuve ou en recopiant la colonne d'exemples ».

**Arbitrage tranché le 07/09** : on annonce le temps réel et on garde la règle de preuve intacte.
L'option écartée était de garder 2-3 h en assouplissant la preuve (un `couvert` sans produit nommé
serait devenu `à vérifier` plutôt qu'`absent`) : elle faisait passer l'échelle à quatre valeurs et
obligeait à publier un κ calculé sur une échelle modifiée. Le coût du choix retenu est un
recrutement plus difficile, pas une perte de validité.

## Le dépouillement (par l'orchestrateur, après réception des deux feuilles)

1. Fusionner : la colonne `juge1` reçoit la notation de l'évaluateur 1
   (`couverture_evaluateur1_2026-08-21.json`), `juge2` et `juge3` les deux feuilles reçues.
2. Lancer :

```bash
python scripts/accord_juges.py docs/cdc/publication/kit_juges_notes.csv --json docs/cdc/publication/accord_juges.json
```

3. Lire : le κ de Fleiss (repères de Landis & Koch pour la lecture, le chiffre se publie tel quel),
   l'accord par paire, les lignes en désaccord. Les lignes en désaccord se discutent en séance
   **après** la première passe, et se re-notent une fois ; **les deux passes sont gardées et la
   publication porte le κ de la première**.
4. Les comptes publiés (couvert / partiel / absent) sont ceux du **vote majoritaire** ; une ligne
   sans majorité est publiée comme telle.

## Le biais de l'instrument, déclaré

Deux choix de conception tirent la notation vers le bas, et il vaut mieux le dire que le laisser
jouer en silence sur 56 lignes.

- **La règle du doute** (point 4 : hésitation → valeur basse) s'applique à des définitions qui
  emploient des absolus — « jamais », « toujours », « sans aucune » (D01, D12, D30, D41). Un seul
  contre-exemple documenté suffit alors à faire descendre une ligne autrement `couvert`.
- **La règle de preuve** (point 3 : sans produit nommé, la note vaut `absent`) transforme tout
  manque de temps en note basse. C'est pourquoi le point 5 demande d'écrire « pas eu le temps »
  plutôt que de noter à la va-vite.

L'instrument est donc **pessimiste par construction**. C'est assumé — mieux vaut sous-estimer la
couverture du marché que la surestimer quand on publie une thèse qui affirme un manque. Mais le
chiffre publié doit porter cette mention.

## Ce que le kit ne règle pas

- Il mesure l'accord, pas la vérité : trois juges peuvent se tromper ensemble. Le gate fraîcheur
  (rejouer le panorama la semaine de publication) reste dû.
- **Le contrôle mécanique est un plancher, pas une preuve d'aveugle.** `verifie_kit.py` refuse les
  formules de verdict, mais une phrase peut orienter sans en employer aucune — « Recherche web
  intégrée dans tous les assistants » n'affirme rien de faux et suggère pourtant une réponse. Seul
  un juge à blanc en contexte frais peut dire si l'aveugle tient ; ses réponses sont dans
  `kit_relecture.md`.
- Les définitions ont été réécrites pour tenir en une phrase. **Le détail est dans la fiche**, pas
  perdu : chaque ligne de `kit_definitions.json` cite le passage de sa fiche dont elle sort. Le juge
  qui veut le détail ouvre la fiche, c'est prévu.
- Les feuilles **remplies** par les juges ne pourront pas être versionnées en `.csv` (garde-fou
  pre-push) : avant le dépouillement, versionner les notes en JSON
  (`[{"dimension": …, "juge1": …}]`) et ne garder les CSV que hors dépôt.

## Rejouer le tableau

```bash
python scripts/etats_cdc.py kit --etats docs/cdc/publication/etats.json --definitions docs/cdc/publication/kit_definitions.json --sortie docs/cdc/publication/kit_juges_tableau.md
python scripts/verifie_kit.py
```

Le second doit rendre `CONFORME`. L'ancien tableau du 04/09 (définitions extraites des fiches par
expression régulière, colonne de l'évaluateur 1) se rejoue avec `--couverture` et `--fiches` à la
place de `--definitions`.
