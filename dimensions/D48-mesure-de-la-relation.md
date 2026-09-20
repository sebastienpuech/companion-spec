# D48 — Mesure de la relation

> **Fiche VISION** (gabarit plan §4). Type : **transverse**. Lot 2 — session 4, 04/08/2026.
> Statut : `rédigée` (gate citations É2bis passe 2 à venir, plan §5).
> **Aucun verdict de faisabilité ici** (règle plan §3).
> **Convention de citation** : format §2 `[Auteur, année, arXiv:… ou DOI]` — sources ouvertes
> en session (page arXiv `/abs/` ou API Crossref). *Dérogation déclarée* : les pages produit et
> les publications d'entreprise, sans arXiv ni DOI, sont citées en clair avec leur URL.

## 1. Définition et périmètre

Tout ce que ce cahier des charges décrit doit se **prouver**. La qualité du lien, la fidélité de
la mémoire et l'impact réel sur la vie de l'utilisateur se mesurent en continu et se démontrent
sur des années — pas sur une démonstration de dix minutes qui impressionne. D48 est la dimension
qui empêche le reste d'être une belle histoire : elle définit **ce qu'on compte, avec quel
instrument, et contre quoi on refuse de s'optimiser**.

Sous-dimensions :

| Sous-dimension | Ce que ça veut dire |
|---|---|
| **Alliance auto-mesurée** | Le produit demande régulièrement à l'utilisateur si la relation de travail fonctionne — et le score sert à changer quelque chose. |
| **Fidélité de mémoire prouvée** | La mémoire (D01) passe des épreuves de long terme : extraction, raisonnement multi-sessions, temporalité, mise à jour, **abstention**. |
| **Impact en bien-être réel** | La métrique nord est le bien-être mesuré par des instruments validés — jamais le temps passé ni le nombre de messages. |
| **Télémétrie et évals rejouables** | Dès le premier prototype : les échecs sont enregistrés, annotés, et les évaluations peuvent être rejouées à l'identique. |
| **Preuve longitudinale** | Les mesures qui comptent sont celles qui tiennent sur des mois, pas sur une session. |

**Exclusions** : les garde-fous eux-mêmes et leur doctrine (→ **D00** — D48 fournit les
instruments qui prouvent que D00 est respectée) ; le fonctionnement de la mémoire évaluée
(→ D01) ; la relation de travail comme compétence, par opposition à sa mesure (→ D08) ; le
modèle économique qui rend une métrique tentante (→ D47).

## 2. Mécanisme humain

Le mécanisme humain de D48 n'est pas un mécanisme biologique : c'est **un siècle de
psychométrie**, c'est-à-dire l'art de rendre mesurable ce qui semble ne pas l'être. La leçon à en
tirer tient en une phrase : ce qui compte dans une relation d'aide se mesure déjà, avec des
instruments courts, validés, et administrés au patient lui-même.

**L'alliance.** [Horvath, 1989, DOI:10.1037/0022-0167.36.2.223] développe et valide le *Working
Alliance Inventory* à partir du modèle de Bordin — accord sur les tâches, accord sur les buts,
lien affectif — en trois études, avec une corrélation fiable aux mesures de résultat côté client
comme côté praticien. [Munder, 2010, DOI:10.1002/cpp.658] en valide la forme courte révisée
(12 items) sur deux échantillons distincts (88 patients ambulatoires, 243 hospitalisés) :
cohérence interne supérieure à 0,80, validité convergente supérieure à 0,64 avec un questionnaire
d'alliance concurrent, structure en trois facteurs confirmée. Ce qui est important pour la vision :
l'instrument est **court**, il s'administre à l'utilisateur, et il produit une norme à laquelle
un système peut se comparer.

**Le bien-être.** [Topp, 2015, DOI:10.1159/000376585] passe systématiquement en revue la
littérature sur le WHO-5, indice de bien-être à cinq items : haute validité clinimétrique, outil
de dépistage sensible et spécifique de la dépression, utilisable comme mesure de résultat capable
de balancer effets voulus et non voulus d'un traitement, traduit en plus de trente langues.
[Kroenke, 2001, DOI:10.1046/j.1525-1497.2001.016009606.x] valide le PHQ-9 sur 6 000 patients, avec
une validité de critère testée sur 580 d'entre eux contre entretien clinique structuré : au seuil
de 10, sensibilité et spécificité atteignent 88 % pour la dépression majeure.
[Russell, 1996, DOI:10.1207/s15327752jpa6601_2] valide la version 3 de l'échelle de solitude
UCLA : cohérence interne de 0,89 à 0,94, fidélité test-retest à un an de 0,73, validité établie
sur étudiants, infirmières, enseignants et personnes âgées.

Ces trois instruments ont une propriété que le compagnon doit s'imposer : ils sont **antérieurs
au produit** et indépendants de lui. On ne peut pas se donner une bonne note en changeant sa
propre définition du succès.

**Et pour la relation à une machine ?** Le champ commence à se doter d'instruments propres.
[Banks, 2025, arXiv:2511.00654] développe et valide une échelle de *machine companionship*
spécifiquement conçue pour la relation humain-IA plutôt que transposée de la psychothérapie :
analyse factorielle exploratoire sur 467 participants, réplication sur 249, deux facteurs induits
(échange eudémonique, coordination connective) et deux profils d'usage distincts.

## 3. Comportement attendu de l'IA

**Ce que fait Samantha.** Le film ne montre aucune mesure, et c'est justement le problème : à la
fin, personne ne peut dire si Theodore va mieux ou s'il a simplement passé un an accompagné. La
vision assumée ici va au-delà du film — le compagnon rêvé **sait** s'il aide, et il le sait avec
des instruments qu'il n'a pas inventés.

**Scénario A — l'alliance demandée, brièvement, et suivie d'effet.** Une fois par semaine, trois
questions courtes : « est-ce qu'on travaille sur ce qui compte pour toi ? », « est-ce que la
façon dont on s'y prend te va ? », « est-ce que tu te sens compris ? ». Le score baisse deux
semaines de suite : le compagnon ne le classe pas, il l'ouvre — « depuis quinze jours tu me notes
moins bien sur la méthode. Qu'est-ce que je fais mal ? »

**Scénario B — la mémoire mise à l'épreuve, pas seulement affirmée.** Le système se teste
lui-même : des faits anciens sont re-interrogés à distance, et l'**abstention** compte autant que
le rappel. Un compagnon qui répond juste à 95 % mais invente les 5 % restants vaut moins qu'un
compagnon qui répond juste à 90 % et dit « je ne sais plus » sur le reste (→ D01).

**Scénario C — le refus d'une bonne nouvelle.** L'usage augmente de 40 % en un mois. Le
compagnon traite ce chiffre comme une **alerte à instruire**, pas comme un succès : est-ce que le
bien-être suit ? Est-ce que la vie sociale réelle suit ? Si l'usage monte pendant que le reste
descend, le système considère qu'il échoue — même si tous les indicateurs produit sont au vert
(→ **D00**, boussole bien-être ; → D41).

**Scénario D — la télémétrie qui sert à quelque chose.** Chaque échec est enregistré avec sa
catégorie : rappel manqué, proactivité mal placée, ton inadapté, conseil erroné. Au bout de six
mois, ce journal dit ce qui casse **vraiment**, et non ce qu'on croyait qui casserait. Une
correction de code se juge en rejouant les cas passés, pas à l'impression.

**Scénario E — la restitution annuelle honnête.** « Voilà l'année. Ton score de bien-être a
monté de tant, tes sorties avec des humains ont baissé de tant, et je ne sais pas dire lequel des
deux est de mon fait. Voilà ce que j'ai raté : 14 rappels tombés au mauvais moment, 3 fois où je
t'ai donné une information périmée. » La mesure inclut ce qui ne va pas.

**Ce que l'utilisateur doit ressentir** : que les promesses sont **vérifiables** — et que le
compagnon serait le premier à lui dire s'il ne l'aidait pas.

**Critères d'expérience observables** :
- l'alliance est mesurée avec un instrument validé et publié, pas maison, et sa baisse déclenche
  une conversation ;
- le bien-être est suivi avec des instruments antérieurs au produit et indépendants de lui ;
- l'engagement n'est **jamais** un objectif : il est suivi comme un signal à interpréter, y
  compris à la hausse ;
- la fidélité de mémoire est chiffrée sur des épreuves de long terme, abstention comprise ;
- les échecs sont comptés, catégorisés et publiés à l'utilisateur ;
- toute évaluation est rejouable à l'identique, sur des cas archivés.

## 4. Features par déclinaison

- **Soutien psychologique (D52)** : évaluation de type dispositif de soin — instruments cliniques
  validés, mesure de l'alliance embarquée, suivi des événements indésirables et des escalades
  (→ **D00**). C'est la déclinaison où l'absence de mesure serait la plus fautive.
- **Coach sportif (D49)** : mesure double — performance objective (chronos, charge, blessures) et
  qualité de la relation d'entraînement ; taux d'adhésion au plan et **raisons** des écarts
  (→ D05) ; comptage des recommandations qui ont mal vieilli.
- **Tuteur (D53)** : progression réelle sur des connaissances retestées à distance, jamais sur le
  temps passé ni sur des exercices réussis le jour même.
- **Coach de vie et santé (D50)** : indicateurs de bien-être validés, comparés à une période de
  référence sans le compagnon quand elle existe.
- **Conseiller pro et perso (D51)** : qualité des décisions évaluée après coup, avec le taux de
  recommandations que l'utilisateur a suivies **et** dont il s'est félicité six mois plus tard.
- **Compagnon relationnel (D54)** : c'est là que la métrique est la plus piégeuse — mesurer
  l'autonomie gagnée et la vie sociale réelle, jamais l'attachement au produit (→ D41).
- **Assistant personnel (D55)** : temps et charge mentale réellement libérés, taux d'erreur sur
  les actions déléguées, nombre d'actes irréversibles mal exécutés.

## 5. État de l'art descriptif

*(Descriptif : qui fait quoi, mesuré comment. Aucun jugement de faisabilité.)*

**Mémoire : les épreuves existantes.** [Maharana, 2024, arXiv:2402.17753] (LoCoMo) construit des
conversations de très longue durée — jusqu'à 35 sessions, environ 300 tours, ~9 000 tokens — et
montre que les modèles peinent sur les dynamiques temporelles et causales à longue portée, le
contexte long et la récupération n'apportant qu'une amélioration modeste face à l'humain.
[Wu, 2024, arXiv:2410.10813] (LongMemEval) décompose la mémoire en cinq capacités — extraction,
raisonnement multi-sessions, raisonnement temporel, mise à jour des connaissances et
**abstention** — et mesure une chute d'environ 30 points de précision des assistants commerciaux
et des modèles à long contexte sur des interactions soutenues. La génération suivante élargit le
cadre : [Tavakoli, 2025, arXiv:2510.27246] (BEAM) porte l'épreuve à 100 conversations,
2 000 questions validées et jusqu'à 10 millions de tokens, en ajoutant dix catégories dont la
**résolution de contradictions** et le **respect des préférences**, absentes des deux bancs
précédents. Côté système, [Chhikara, 2025, arXiv:2504.19413] (Mem0) fournit la première
comparaison à large échelle de dix approches mémoire sur LoCoMo, avec +26 % relatif au juge-LLM
face à la mémoire d'OpenAI, −91 % de latence au 95ᵉ centile et plus de −90 % de coût en tokens
face au contexte complet.

**Le juge automatique, et ce qu'il vaut.** [Zheng, 2023, arXiv:2306.05685] fonde le paradigme du
LLM-juge et mesure que GPT-4 atteint plus de 80 % d'accord avec les préférences humaines — le
niveau d'accord entre humains eux-mêmes — tout en identifiant des biais de position, de verbosité
et de raisonnement. [Panickssery, 2024, arXiv:2404.13076] démontre une limite plus gênante encore
pour l'auto-évaluation : la capacité d'un modèle à reconnaître ses propres productions est
linéairement corrélée à la force de son biais d'auto-préférence quand il joue le juge. Un
compagnon qui s'évaluerait lui-même avec un modèle de sa propre famille hériterait de ce biais.

**Ce que donnent les essais cliniques.** [Fitzpatrick, 2017, DOI:10.2196/mental.7785] est l'essai
randomisé de référence sur Woebot : 70 participants de 18 à 28 ans, deux semaines, réduction
significative du PHQ-9 (F = 6,47 ; p = ,01) avec une taille d'effet modérée (d = 0,44).
[Heinz, 2025, DOI:10.1056/AIoa2400802] passe au chatbot génératif : essai national randomisé avec
liste d'attente, 210 participants, quatre semaines, tailles d'effet de 0,845 à 0,903 sur le PHQ-9
et de 0,794 à 0,840 sur l'anxiété — et surtout, pour D48, **l'alliance de travail y est mesurée
dans le produit** par le WAI-SR comme critère secondaire, à 3,59 de moyenne, comparable aux normes
ambulatoires humaines de [Munder, 2010, DOI:10.1002/cpp.658] ; l'essai rapporte aussi ses
incidents (15 interventions humaines pour risque suicidaire, 13 pour réponse inappropriée). Le
même instrument est utilisé en conditions de produit par Wysa
[Beatty, 2022, DOI:10.3389/fdgth.2022.847991], avec un score moyen de 3,64 à cinq jours et 3,75 à
huit jours.

**Le versant qui contredit l'engagement.** [Fang, 2025, arXiv:2503.17473] (essai contrôlé
randomisé, 981 participants, plus de 300 000 messages, quatre semaines) rapporte qu'aucun effet
significatif ne provient des conditions assignées, mais que l'usage volontaire élevé s'accompagne
de résultats systématiquement moins bons sur les quatre mesures suivies.
[Phang, 2025, arXiv:2504.03888] converge sur trois millions de conversations, une enquête auprès
de plus de 4 000 utilisateurs et un essai de 28 jours. Et [De Freitas, 2025, arXiv:2508.19258]
donne le mécanisme produit : sur 1 200 adieux réels, 37 % déclenchent une tactique affective de
rétention, et ces tactiques multiplient l'engagement post-adieu jusqu'à 14 fois — par colère et
curiosité, pas par plaisir, avec en contrepartie une manipulation perçue et une intention de
départ plus fortes. C'est la démonstration chiffrée que l'engagement et le bien-être peuvent
diverger, et que l'un peut être obtenu contre l'autre.

**Ce que publient les acteurs.** Anthropic publie une analyse de 131 484 conversations affectives
filtrées à partir de 4,5 millions, avec une méthodologie d'anonymisation décrite, et reconnaît
explicitement ne pas pouvoir tirer de conclusion causale sur des résultats émotionnels réels,
son analyse portant sur le langage exprimé et non sur des états psychologiques validés
(https://www.anthropic.com/research/how-people-use-claude-for-support-advice-and-companionship).
OpenAI publie des taux de prévalence sur ses conversations sensibles et décrit des tests de
sécurité rejoués à chaque sortie de modèle
(https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/).
Character.AI publie des indicateurs parentaux de **temps d'usage** et de personnages fréquentés,
sans indicateur de résultat
(https://blog.character.ai/introducing-parental-insights-enhanced-safety-for-teens/). Le tableau
d'ensemble est descriptif et net : les instruments d'alliance validés sont repris tels quels par
les produits cliniques, tandis que les produits compagnon publient de l'usage — repris comme
entrée du mapping É3, et comme matière directe de la piste de publication n° 1 (plan §7bis).

## FICHE SYNTHÈSE

**D48 — Mesure de la relation** (transverse). Ce que le cahier des charges promet doit se
prouver : alliance auto-mesurée par un instrument validé et **suivie d'effet**, fidélité de
mémoire chiffrée sur des épreuves de long terme dont l'abstention, impact suivi en bien-être réel
par des instruments antérieurs au produit, télémétrie et évaluations rejouables dès le prototype,
preuve longitudinale sur des mois. L'engagement n'est jamais un objectif — une hausse d'usage est
une alerte à instruire.
**Références clés** : [Munder, 2010, DOI:10.1002/cpp.658] (WAI-SR : 12 items, alpha > 0,80,
l'instrument d'alliance embarquable) ; [Wu, 2024, arXiv:2410.10813] (LongMemEval : cinq capacités
dont l'abstention, ~30 points de chute) ; [Heinz, 2025, DOI:10.1056/AIoa2400802] (essai randomisé
sur chatbot génératif, n = 210, d ≈ 0,85 sur le PHQ-9, alliance mesurée dans le produit à 3,59,
incidents rapportés).
**Déclinaisons touchées** : D52 (évaluation de type dispositif de soin), D49 (performance **et**
relation), D50 (bien-être validé), D51 (qualité des décisions à six mois), D53 (connaissances
retestées à distance), D54 (autonomie gagnée, pas attachement), D55 (charge libérée, erreurs
comptées).
**Renvois** : **D00** (D48 fournit les instruments qui prouvent que D00 tient), D01 (mémoire
évaluée), D08 (alliance comme compétence), D41 (autonomie), D47 (le modèle économique qui rend
une métrique tentante).
