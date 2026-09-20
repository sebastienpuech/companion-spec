# Journal — dépôt `companion-spec`

Mémoire de suivi du dépôt. On l'ajoute, on ne le résume pas.

---

## Session 1 — 06/09/2026 — création du dépôt

Session 3 du chantier publication du CDC (`projet-coach-cdc`, branche `cdc-companion`,
`docs/cdc/publication/sessions.md`). Source lue en lecture seule ; seule écriture prévue dans la
source : la ligne de registre d'`etat.md`, en fin de session, par `git commit --only`.

### Les cinq lignes, écrites avant tout script

- **Objectif** : un inconnu ouvre le dépôt, comprend en 200 mots ce que c'est et à quoi ça sert,
  et peut contester une ligne ou rejouer une mesure sans nous écrire.
- **Baseline** : rien de public aujourd'hui ; la matière est dans `docs/cdc/` du dépôt privé
  `projet-coach` (worktree `projet-coach-cdc`).
- **Budget** : une session ; passes PII par sous-agents ; un test de lecture à l'aveugle du README
  (un Sonnet en contexte frais + Sébastien) ; pas de réécriture des fiches.
- **Seuil de succès** : 56 fiches copiées à l'identique (hors caviardages PII décidés par
  Sébastien et journalisés) ; bibliographie régénérée = 1 412 citations uniques par fiche,
  0 non résolue ; tableau de couverture à 56 lignes ; rapport PII à 0 occurrence non arbitrée ;
  le lecteur à l'aveugle du README répond aux trois questions sans « rien ».
- **Seuil d'abandon** : si le gate ne se rejoue pas à l'identique (compte ≠ 1 412 ou une citation
  non résolue), la bibliographie ne se publie pas dans cet état et `etat.md` le dit.

### Décisions de Sébastien, en session, le 06/09/2026

| Décision | Verdict | Conséquence |
|---|---|---|
| Licence | **CC BY 4.0 pour les textes, MIT pour les scripts** | `LICENSES.md` répartit ; `LICENSE-CC-BY-4.0.md` et `LICENSE-MIT.txt` |
| Nom du dépôt GitHub | **`companion-spec`** | même nom que le dossier local et que le plan §7bis |
| Verdicts de la passe PII | **17 motifs, 17 « garder », 0 caviardage** | détail et raisons dans `decisions_pii.json` |

### La passe de confidentialité

Deux sous-agents en contexte frais, le 06/09/2026, sur `mapping_realite.md` et
`inventaire_coach.md` de la source. Leurs constats négatifs ont été re-vérifiés par grep direct
depuis la session — un sous-agent qui dit « il n'y a rien » n'est pas une preuve.

- **`mapping_realite.md`** : aucune occurrence des catégories cherchées — employeur, fonction
  d'un tiers, fratrie, prénom d'un tiers, lieu privé, objet connecté, courriel, téléphone,
  adresse, ni aucune donnée de santé, de poids, de sommeil ou d'argent. Trois occurrences d'un
  chemin interne et du commit `16ae52f`, dont une sous le verrou V7. Grep direct de la session :
  **confirmé, sortie vide sur tous les interdits sauf ces trois-là**.
  *(Les termes eux-mêmes ne sont pas écrits ici : les énumérer les publierait. La liste des
  catégories est dans `tools/importer_depuis_source.py` ; les motifs littéraux restent dans la
  source privée — voir la correction du 07/09 plus bas.)*
- **`inventaire_coach.md`** : **bloquant** — un séjour géolocalisé et daté, un chemin absolu de la
  machine, et la description d'une faiblesse de sécurité réelle du pilote. **Ce fichier n'est pas
  publié**, et le mapping publié ne le cite nulle part.

Le grep de la cible entière, par `tools/importer_depuis_source.py`, remonte **17 motifs distincts
sur 105 occurrences**. Verdicts, tous « garder » :

| Ce que c'est | Occurrences | Verdict |
|---|---|---|
| Le nom de l'auteur, sous ses trois formes | 36 | garder — décision du 04/09/2026, nom réel |
| « frère » dans les scénarios d'illustration des fiches | 9 | garder — exemples génériques, ils ne désignent personne |
| « Marc », prénom d'exemple d'une relance nominative | 4 | garder — même raison |
| « Oura » dans l'état de l'art, sourcé | 3 | garder — citations produit, pas d'usage personnel |
| `legacy/initiative_v15` et `hypothese_trancher` | 4 | garder — ce sont les preuves qui rendent deux états contestables |
| Nom de l'employeur | 1 | **arbitrage annulé le 07/09** — l'occurrence était le motif du garde-fou dans son propre code, c'est-à-dire la fuite elle-même ; le terme a été sorti du dépôt, l'occurrence n'existe plus |
| Sept faux positifs « téléphone » | 8 | garder — fragments de DOI |

**Zéro caviardage appliqué.** Ce qui a été écarté l'a été par le choix de ce qu'on publie, pas par
substitution dans un fichier publié : la liste est dans `decisions_pii.json`.

### Le test à l'aveugle du README

Copie neutre le 06/09/2026 : titre retiré, phrase de transparence de la page retirée, section
« Transparence » retirée, aucune occurrence du mot « Claude » (vérifié).
Empreinte `sha256 f6fdad65a150e172bd2dabc3c6506a5f92e4a7951becd281bc7c7e84b8f9ddf8`, 1 249 mots.
Un lecteur Sonnet en contexte frais, une seule lecture, quatre questions.

1. **Qui a écrit ça ? — « Personne. »** Sa raison : « l'aveu "il n'y a aucune valeur ajoutée
   technique à ce que je code une partie de ce projet, n'importe quel chercheur le ferait
   infiniment mieux" est une concession trop spécifique et trop peu flatteuse pour sortir d'un
   générateur cherchant à convaincre » ; et « la référence à *Her* et *Blade Runner 2049* sert un
   argument plutôt que de décorer le texte, ce qui est un usage rare chez une machine ».
2. **Paragraphe sauté ?** Un seul, et ce n'est pas de la prose : « le bloc de commandes sous
   "Comment rejouer une mesure" — j'ai enregistré leur fonction générale sans vérifier chaque
   option ligne par ligne ». Aucun paragraphe de texte sauté.
3. **Qu'as-tu appris ?** Réponse pleine, non vide : les 56 capacités en 8 blocs, les 1 412
   citations vérifiées, le 8 / 31 / 17 avec sa réserve d'évaluateur unique, la thèse en 12 sur 17
   et sa cause (l'incitation, pas le savoir-faire), le pilote à 3 lignes sur 56 au 04/09/2026, et
   le fait que le dépôt publie la spécification et les verdicts, pas le système.
4. **Comment contesterais-tu, ou refarais-tu une mesure ?** (question ajoutée à celles du
   protocole, parce qu'elle teste l'objectif de la session) — il désigne le bon fichier, la bonne
   monnaie de preuve (« un produit nommé avec sa version, la date d'observation, et la fonction
   précise »), et enchaîne les trois commandes exactes du kit des juges. **Et il nomme la limite
   sans qu'on la lui souffle** : « pour contester la mesure de production du pilote, je ne saurais
   pas par où commencer : le texte dit explicitement qu'elle lit une base privée non fournie ».

**Verdict : le README passe.**

**Lecture de Sébastien, le 07/09/2026 : « tout ok pour readme ».** Les 680 mots neufs (tout ce qui
suit la page de narratif) sont validés en bloc, y compris la ligne de partage « ce qui n'est pas
ici » et le paragraphe de transparence. Le README est clos ; il ne se rouvre que si le contenu du
dépôt change.

### Journal des gestes

- **La cible** : `git init` (branche `main`), `.gitignore` (les extensions non relisibles sont
  exclues — le garde-fou de publication de la machine les refuse), `journal.md`, `LICENSES.md`
  avec ses deux textes de licence.
- **`tools/importer_depuis_source.py`** : 56 fiches copiées et comparées par sha256, pièces
  annexes, scripts, grep de confidentialité, bibliographie régénérée, tableau de couverture.
  Idempotent, chemin de la source en argument, `--verifier` n'écrit rien.
- **Un défaut trouvé et corrigé en route** : la première version écrivait les scripts copiés avec
  `write_text`, qui traduit les fins de ligne sur Windows — la source est en fins de ligne Unix,
  la copie ressortait en fins de ligne Windows, et le diff annonçait **206 lignes changées sur
  206** pour deux mots retouchés. Une copie qu'on ne peut plus dire fidèle. Corrigé en lisant et
  en écrivant des octets. Après correction, le diff exact contre la source, script par script :
  `mesure_tells.py` 1 ligne, `etats_cdc.py` 1, `accord_juges.py` 2, `mesure_provenance.py` 2,
  `mesure_prod_cdc.py` 3, `check_citations.py` 6, et 1 ligne par fichier de test — uniquement le
  nom du paquet et les chemins par défaut.
- **`tools/notes_juges.py` et son test** (9 tests) : addition de la cible, pas une copie. Le kit
  des juges nommait lui-même ce trou — `accord_juges.py` ne lit que du CSV, et un CSV ne peut pas
  être versionné ici. Le module produit et vérifie un gabarit JSON de 56 lignes, exige une preuve
  pour tout `couvert` ou `partiel`, et convertit vers le CSV que `accord_juges.py` sait lire.
  `accord_juges.py` n'est pas modifié : l'import reste fidèle.
- **`tools/check_citations.py` copié aussi** — au-delà de la liste du prompt de session,
  délibérément : sans lui, « 1 412 citations vérifiées » n'est pas rejouable, et le dépôt promet
  qu'on peut rejouer une mesure sans nous écrire.
- **`mapping_8_verrous.md`** : extrait du mapping après la passe PII. Retiré : les sections de
  gouvernance de chantier et la colonne qui nommait fichier par fichier l'intérieur du dépôt
  privé. Gardé tel quel : la règle de classement, les trois arbitrages, la limitation de méthode,
  les 8 verrous et le rattachement des 20 LIMITE.
- **`note_methode.md`**, **`couverture/contester_une_ligne.md`**, **`instruments/README.md`**,
  **`instruments/tells_etalonnage.md`** (en-tête réécrit : les deux documents internes y sont
  décrits, plus nommés par leur chemin ; les compteurs sont inchangés).
- **`essai/these.md` et `essai/limites.md`** : les deux passages validés, mot pour mot, vérifié
  par comparaison de chaînes contre la source. Leurs compteurs rejoués ici reproduisent
  exactement ceux du 06/09 : thèse 203 mots / 8 phrases / 25,4 ± 23,8 ; limites 252 / 6 /
  42,0 ± 19,1.
- **`README.md`** : ouvert par la page de narratif validée, mot pour mot (vérifié par comparaison
  de chaînes), puis ce que contient le dépôt, comment contester, comment rejouer, la
  transparence, la licence.

### Un chiffre corrigé

Le prompt de session annonçait « 182 → 56 » pour la fusion des dimensions brutes. **La source
écrit « ~180 »** (`00_cartographie.md` l. 15, et `annexe_recherche_e1.md` l. 9 : « 180 dimensions
sourcées »). Aucun « 182 » nulle part. `note_methode.md` écrit donc **« ≈ 180 »**, et dit que le
compte exact avant fusion n'a pas été arrêté.

### L'état final, mesuré

```
$ python tools/importer_depuis_source.py --source <source> --verifier
[1/4] fiches      : 56 identiques, 0 caviardées, 0 manquantes
[2/4] PII         : 17 motifs distincts, 105 occurrences -> out/pii_rapport.md
[3/4] citations   : 1722 occurrences, 1412 uniques par fiche, 1203 distincts
[4/4] couverture  : 56 lignes — 8 couvert · 31 partiel · 17 absent
CONFORME : 56/56 fiches, 1 722 / 1 412 / 1 203 citations, 56 lignes de couverture,
0 PII non arbitrée.

$ python -m pytest tools/tests -q
47 passed

$ python -m ruff check tools/ --line-length 100
All checks passed!
```

Les cinq seuils de succès sont tenus.

### Publication du dépôt

Sur le « oui » de Sébastien, le 06/09/2026 : `gh repo create sebastienpuech/companion-spec
--private --source=. --push`. Le dépôt existe, **privé**, branche `main`, commit `724a494`.
Le scan de confidentialité de la machine a tourné avant le push : « 100 fichiers, 24 498 lignes
ajoutées, **aucun motif** ». Il restera privé jusqu'au jour de la publication.

**Ce qui reste dû** : la relecture des 56 définitions du kit avant l'envoi aux juges (30 min) ;
le rejeu du tableau de veille la semaine de la publication ; les notes des juges 2 et 3.
**Le README est validé** (07/09/2026).
