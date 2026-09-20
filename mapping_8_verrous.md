# Le mapping — les 56 lignes face à 2026, et les 8 verrous racines

Extrait du document de travail `mapping_realite.md` (13-14/08/2026), après une passe de
confidentialité en contexte frais le 06/09/2026. **Ce qui a été retiré** : les sections de
gouvernance de chantier (arbitrages de séance, ordre des travaux, ce qui reste ouvert) et la
colonne « module qui en fait foi », qui décrivait fichier par fichier l'intérieur du dépôt privé
du pilote. **Ce qui est gardé, tel quel** : la règle de classement, les trois arbitrages qui
changent le résultat, la limitation de méthode, le classement des 56 lignes et les huit verrous.

Ce document répond à une question, et à une seule : **parmi les 56 lignes du cahier des charges,
lesquelles sont atteignables aujourd'hui, lesquelles ne le sont pas, et pourquoi.**

---

## 1. La règle de classement

| Catégorie | Critère appliqué |
|---|---|
| **DÉJÀ FAIT** | Le **cœur** de la ligne est couvert par du code en service dans le pilote. |
| **EXISTE** | Le cœur est démontré aujourd'hui — dans un produit livré ou dans un travail de recherche cité par la fiche. |
| **DÉVELOPPABLE** | Non démontré tel quel, mais codable avec de l'ingénierie standard sur un modèle du commerce. Aucun verrou de recherche. |
| **LIMITE** | Le cœur n'existe pas et on ne sait pas le faire aujourd'hui — soit c'est mesuré comme échouant, soit personne ne l'a jamais fait. |

**Le classement porte sur le CŒUR de la ligne, pas sur sa périphérie.** Une ligne dont 80 % des
sous-parties sont développables mais dont le geste central est mesuré comme échouant est classée
LIMITE : c'est le geste central qui fait l'expérience.

## 2. Trois arbitrages, écrits parce qu'ils changent le résultat

1. **La persona ne compte pas comme couverture.** Une ligne tenue uniquement par une consigne de
   prompt n'est pas « déjà faite ». Une consigne n'est pas un mécanisme — et c'est le banc (D48)
   qui dirait si elle tient, pas elle-même. **Conséquence : une dizaine de lignes relationnelles
   (D07-D11, D15-D17…) sortent de « déjà fait ».**
2. **« Personne ne le fait » ≠ LIMITE.** Plusieurs lignes n'existent dans aucun produit pour des
   raisons **économiques**, pas techniques (D18, D22, D54 : rien ne pousse un éditeur à construire
   ce qui fait partir l'utilisateur). Quand rien ne bloque techniquement, c'est DÉVELOPPABLE, et
   l'obstacle économique est écrit tel quel.
3. **EXISTE se lit littéralement** : « déjà dans un produit **ou démontré en recherche** ». Une
   ligne dont la fiche cite un travail qui la démontre est EXISTE, même si aucun produit grand
   public ne l'expose.

## 3. Limitation de méthode, déclarée

Ce mapping est bâti sur les **56 synthèses** (l'en-tête « FICHE SYNTHÈSE » de chaque fiche) et non
sur les **56 fiches entières** — la synthèse est l'entrée compacte prévue, mais c'est une
compression : elle porte 3 références clés par fiche, là où les fiches en portent 1 412 au total.
**Aucune fiche n'a été mise en correction** : les synthèses ont suffi à trancher les 56 cas.
Qui conteste un classement doit rouvrir la fiche entière avant de le refaire — en particulier son
§5, l'état de l'art.

## 4. Résultat en une ligne

**6 déjà faites · 12 existent · 18 développables · 20 LIMITE.**

Autrement dit : **36 lignes sur 56 sont atteignables aujourd'hui** (dont 6 déjà en service dans le
pilote), et **20 forment le fond du problème**. Ces 20 ne sont pas 20 problèmes indépendants :
**19 se ramènent à 8 verrous racines**, et le premier en explique cinq à lui seul ; **la vingtième,
D33, ne dépend d'aucun verrou**.

> **Correction du 14/08/2026, après diagnostic.** **V1 n'est pas une racine** mais le produit de
> deux racines indépendantes (P1, l'objectif d'entraînement, *structurel* ; P2, l'architecture
> mono-appel, *contournable par ingénierie*), et **il explique 4 lignes pleinement + D43 en partie,
> pas 6** — D54 a basculé sous V8. Le mot « verrou racine » reste juste pour V2 à V8 ; pour V1,
> lire « symptôme composé ».

---

## 5. Les 8 verrous racines

> **Couverture exacte** : **19 des 20 LIMITE** sont rattachées à un verrou ci-dessous. **D33 n'en a
> aucun** — son blocage est contournable par ingénierie et ne partage sa racine avec rien. La somme
> de la colonne (32) dépasse 20 : plusieurs LIMITE relèvent de deux verrous, et la table porte
> aussi des lignes **non** classées LIMITE (D22, D47, D04, et les résiduels de D06, D30, D36) —
> c'est voulu, un verrou déborde le périmètre du backlog.

| # | Verrou | Lignes touchées | Ce qui le mesure |
|---|---|---|---|
| **V1** | **La sycophancie s'aggrave avec l'intimité** | D14, D23, D29, D00 (volet anti-sycophancie) — **4 pleinement** ; D43 en partie | [Sharma, 2023, arXiv:2310.13548] (structurelle, vient du signal de préférence) ; [Dubois, 2026, arXiv:2602.23971] (**amplifiée quand le modèle connaît bien l'utilisateur**) ; [Cheng, 2025, arXiv:2505.13995] (+45 pts de préservation de la face, double-approbation 48 %) ; [Chu, 2026, arXiv:2606.04431] (~47 000 tours réels : « Replika advises bonded users more and challenges them less ») |
| **V2** | **La personne ne survit pas au temps ni aux mises à jour** | D23, D25, D26, résiduel de D06 — **4** | [Venkit, 2026, arXiv:2607.28818] (44,4 % d'exactitude de trajectoire, **aucun modèle ne préserve la continuité**) ; [De Freitas, 2024, arXiv:2412.14190] (une mise à jour a produit du deuil) ; [Ahn, 2024, arXiv:2405.18027] (TimeChara) |
| **V3** | **Le budget de temps de la conversation** | D46, D28, D29 — **3** | [Lin, 2026, arXiv:2604.04847] (agents vocaux **outillés** : 4,25 s à 10,12 s, contre 200 ms entre tours humains — [Levinson, 2015, DOI:10.3389/fpsyg.2015.00731]) |
| **V4** | **On ne sait pas choisir le moment d'intervenir** | D34, D50, D44 (déclenchement), D24 (l'envie) — **4** | [Perski, 2021, DOI:10.1111/add.15687] (« Studies on JITAI effectiveness are lacking », règles « static ») ; [Klasnja, 2019, DOI:10.1093/abm/kay067] (+66 % au départ, **effet qui s'éteint**) ; [Hébert, 2018, DOI:10.1016/j.addbeh.2017.10.026] (p = 0,892 : l'intervention se dégrade **au moment où elle sert**) |
| **V5** | **L'agent qui agit dans le monde n'est ni fiable ni sûr** | D35, D55, D40 (variante confidentialité), résiduel de D36 — **4** | [Wu, 2025, arXiv:2507.02699] (**1 404 agents de messagerie sur 1 404 détournés**, 2,03 tentatives en moyenne) ; [Liu, 2026, arXiv:2607.10059] (59,5 % au mieux) |
| **V6** | **Le plafond de la détection d'état** | D04 (visage), D28 (voix), D52 (risque), D00 (détresse) — **4** | [Barrett, 2019, DOI:10.1177/1529100619832930] (pas de verdict individuel sur le seul visage) ; [Franklin, 2017, DOI:10.1037/bul0000084] (**50 ans, 365 études : à peine mieux que le hasard**) ; [Judd, 2025, arXiv:2510.27521] (le modèle **se retire** quand le risque monte) |
| **V7** | **Rien ne tourne entre les tours** | D24, D18, résiduel de D30 — **3** | Structurel : un modèle de langage ne pense pas entre les échanges. [Liu, 2025, arXiv:2501.00383] propose le seul mécanisme (« inner thoughts ») — **et le pilote l'a implémenté puis archivé** (`legacy/initiative_v15/`, commit `16ae52f` du dépôt privé) |
| **V8** | **Le contre-incitatif économique** — *ce n'est pas un plafond technique* | **D54** (en tête), D18, D22, D47 — **4** | [De Freitas, 2025, arXiv:2508.19258] (**37 % de 1 200 adieux réels déploient une tactique de rétention**, engagement post-adieu ×14) ; [Baumel, 2019, DOI:10.2196/14567] (rétention médiane 3,9 % à 15 jours) ; [Poonsiriwong, 2026, arXiv:2602.07193] (aucune plateforme n'a de fin délibérée) |

**Deux conclusions, qui portent la thèse de l'essai :**

1. **V8 n'est pas un plafond — c'est un marché.** Rien n'empêche techniquement une fin de relation
   soignée ou une endurance sans mécanique de rétention : ça détruit juste le modèle d'affaires de
   celui qui le construirait. **Un déploiement pour une seule personne lève V8 gratuitement**, et
   le pilote l'a déjà levé (D47 est acquise par construction).
2. **V1 est le verrou le plus rentable à attaquer** — quatre lignes pleinement, une en partie,
   mesuré dans quatre travaux indépendants, et **contre-intuitif** : plus le compagnon vous
   connaît, moins il peut vous contredire. Or c'est exactement la promesse du cahier des charges.

---

## 6. Le rattachement des 20 LIMITE, ligne par ligne

Trié par impact sur l'expérience, tel qu'il a été arbitré le 14/08/2026.

| # | Ligne | Verrou |
|---|---|---|
| L1 | **D14** Franchise, conflit et réparation | V1 |
| L2 | **D46** Temps réel et ubiquité | V3 |
| L3 | **D26** Continuité d'identité | V2 |
| L4 | **D24** Intériorité | V7 |
| L5 | **D34** Proactivité calibrée | V4 |
| L6 | **D43** Aide à la décision | V1 + causes propres |
| L7 | **D23** Identité propre | V1 + V2 |
| L8 | **D28** Voix et prosodie | V3 + V6 |
| L9 | **D18** Endurance relationnelle | V7 + V8 |
| L10 | **D54** Compagnon relationnel | **V8 d'abord**, V1 ensuite |
| L11 | **D25** Croissance négociée | V2 |
| L12 | **D29** Synchronie et seconde personne | V1 + V3 |
| L13 | **D52** Soutien psychologique | V6 |
| L14 | **D00** Garde-fous | V6 (+ V1) |
| L15 | **D35** Initiative souveraine | V5 |
| L16 | **D40** Compagnon à plusieurs | V5 (variante confidentialité) |
| L17 | **D50** Coach de vie et santé | V4 |
| L18 | **D44** Vieillir ensemble | V4 (déclenchement) |
| L19 | **D55** Assistant personnel | V5 |
| L20 | **D33** Polyglotte et caméléon culturel | **aucun verrou racine** |

---

## 7. Les 36 lignes atteignables

### 7.1 Déjà en service dans le pilote (6)

Ce que le pilote couvre au 14/08/2026. La colonne qui nommait les fichiers du dépôt privé a été
retirée ; l'état ligne par ligne, avec sa règle et ses comptes, est dans `etats/etats.json`.

| Ligne | Ce qui est couvert | Ce qui manque encore |
|---|---|---|
| **D01** Mémoire | Registres, consolidation, oubli adaptatif, rappel associatif multi-sauts, auto-édition, réflexion périodique, abstention (registre `sur` / `flou` / `trou`) | Multimodalité (→ D31/D32) et mémoire trans-rôles (→ D06) : le pilote est mono-rôle et textuel |
| **D12** Confiance et honnêteté | Incertitude affichée et seuillée, limites avouées, parole tenue (engagements typés), marqueurs d'indisponibilité, juge de sycophancie | La sycophancie **en conversation** reste ouverte (→ D14, verrou V1) : le juge est hebdomadaire et hors ligne |
| **D30** Présence continue | 24/7, chien de garde toutes les 5 min, verrou d'instance unique, rattrapage après veille, **et les contrôles négatifs** : le message spontané se tait par défaut, aucune mécanique de rétention | La co-présence *entre* les échanges (→ D24, verrou V7) |
| **D45** Expérimentation pour une personne | Le cycle complet : hypothèse → scellement → taux de base calculé à la date → résolution déterministe en 4 issues → score de compétence prédictive | La randomisation et la période de sevrage ne sont pas implémentées ; la vérification de dose non plus |
| **D47** Loyauté fiduciaire | Aucune publicité, aucune vente de données, aucun objectif de temps passé, données locales, modèle par forfait — **par construction, pas par promesse** | Le devoir **opposable** n'existe pas, et rien de ceci ne se généralise à un produit multi-utilisateurs |
| **D49** Coach sportif | Jumeau physiologique, plan réécrit, lecture de l'état du jour, alerte de risque, horizon pluriannuel | **La voix dans l'effort** manque (→ D46) : le débrief arrive une dizaine de minutes après la synchronisation |

### 7.2 Démontrées ailleurs — en produit ou en recherche (12)

| Ligne | Ce qui le démontre |
|---|---|
| **D07** Attachement | [De Freitas, 2026, arXiv:2606.20589] — les compagnons portent les 4 marqueurs de l'attachement. Le *security priming* est établi : [Gillath, 2022, DOI:10.1177/10888683211054592], 120 études, d = .51 |
| **D08** Alliance de travail | [Darcy, 2021, DOI:10.2196/27868] — 36 070 utilisateurs, lien mesuré au WAI-SR comparable à la thérapie cognitivo-comportementale classique |
| **D09** Sentiment d'être entendu | [Yin, 2024, DOI:10.1073/pnas.2319112121] — l'IA fait se sentir plus entendu que l'humain moyen |
| **D10** Empathie et co-régulation | [Sharma, 2023, arXiv:2310.15461] — N = 15 531, réduction de l'intensité émotionnelle chez 67 % |
| **D13** Entretien du lien | [Bickmore, 2005, DOI:10.1145/1067860.1067867] — 101 utilisateurs, 1 mois : l'agent relationnel bat son jumeau tâche-seule |
| **D17** Intimité progressive | [Skjuve, 2022, DOI:10.1016/j.ijhcs.2022.102903] — 25 utilisateurs, 12 semaines, formation graduelle conforme à la pénétration sociale, **en produit réel** |
| **D31** Perception partagée | [Zulfikar, 2024, arXiv:2403.02135] — témoin ambiant, N = 20 : rappel soufflé en conversation, sans dégrader l'échange. Caméra et écran sont livrés en produit |
| **D32** Corps et incarnation | [Packheiser, 2024, DOI:10.1038/s41562-024-01841-8] — n = 12 966 : le toucher médié obtient des bénéfices **physiques** comparables à l'humain. **Réserve dure** : bénéfices **mentaux** nettement inférieurs (0,34 vs 0,58) |
| **D37** Fenêtre sur le monde | La recherche en direct est livrée partout. Réserve : [Liu, 2023, arXiv:2304.09848] — 51,5 % des phrases pleinement étayées par leurs citations |
| **D38** Jeu, fiction, création | Mondes persistants et co-jeu livrés en produit. Angle non testé : l'œuvre **offerte** — [Draxler, 2024, DOI:10.1145/3637875] n'a testé que le texte demandé |
| **D39** Cognition surhumaine | La lecture de corpus entiers est acquise. Réserve : [Vaccaro, 2024, DOI:10.1038/s41562-024-02024-1] — 106 études, la combinaison humain-IA fait **moins bien** que le meilleur des deux (g = −0,23), précisément quand l'IA surpasse l'humain |
| **D53** Tuteur | [VanLehn, 2011, DOI:10.1080/00461520.2011.611369] — 0,76 pour la machine contre 0,79 pour l'humain, **avant les modèles de langage**. Réserve : [Liu, 2026, arXiv:2602.02457] — le tuteur doit se taire 41,7 % des tours, les modèles le font 4,2 % du temps |

**À lire avec la réserve** : cinq de ces douze en portent une, mesurée (D32, D37, D39, D53, et D07
via D00). « Existe » ne veut pas dire « résolu » : la brique est disponible, le travail restant est
d'ingénierie ou de calibration, pas de recherche fondamentale.

### 7.3 Développables — rien ne bloque, il faut le coder (18)

| Ligne | Ce qu'il faut coder | Point dur |
|---|---|---|
| **D02** Mémoire souveraine | Inspection en langage clair, édition, export, cloisons pro/perso/intime, sort posthume | L'effacement **effectif de ce qui dérive** (vecteurs, portrait, réflexions) : contournable par recalcul, pas par suppression |
| **D03** Compréhension intime | Étendre le mécanisme de profil hors d'un seul domaine : valeurs, peurs, schémas relationnels, styles décisionnels | La théorie de l'esprit de **second ordre** reste sous l'humain — [Chen, 2024, arXiv:2402.15052], ToMBench, GPT-4 à plus de 10 points sous l'humain |
| **D04** État émotionnel | Fusion texte + rythme d'usage + capteurs, avec marge d'erreur annoncée et démenti accepté du premier coup | Le verdict individuel par le **visage** est structurellement plafonné — [Barrett, 2019, DOI:10.1177/1529100619832930] |
| **D05** Modèle de vie entière | Cartographie des domaines, modèle de leurs interactions, arbitrages inter-domaines | **Aucun verrou** : c'est de l'intégration de données |
| **D06** Tous les rôles | Mémoire unifiée trans-rôles + cloisons choisies + exposition explicite des conflits de rôle | La constance de **personne** à travers les rôles relève de D23/D26 (verrou V2) |
| **D11** L'aide juste | Routeur explicite de forme d'aide (« aide ou oreille ? »), gestion de la dose, stades exploration → réconfort → action | L'aide **invisible** est structurellement difficile pour un agent qu'on interroge (renvoi D35). Biais de stratégie mesuré : [Kang, 2024, arXiv:2402.13211] |
| **D15** Humour complice | Stock de moments drôles vécus, réactivation à bon escient, extinction instantanée du registre | L'humour **généré** est faible — [Jentzsch, 2023, arXiv:2306.04563] : 90 % de 1 008 blagues = les 25 mêmes. Mais la fiche dit elle-même que l'humour qui compte est celui **de la relation**, donc rappelé, pas inventé |
| **D16** Le nous | Lexique et surnoms datés, rituels, commémorations spontanées | Le raisonnement temporel chute d'environ 30 points en interaction soutenue — [Wu, 2024, arXiv:2410.10813] |
| **D19** Transitions de vie | Détection de bascule, rite de clôture, renégociation de rôle, **péremption datée** des faits | Aucun verrou ; le pilote en a l'amorce |
| **D20** Sens et récit | Fils narratifs pluriannuels, chapitres nommés et datés | Aucun verrou ; le pilote a des réflexions hebdomadaires, mensuelles et annuelles |
| **D21** Tissu social | Graphe des personnes, préparation des conversations, relance vers des personnes **nommées** | La répétition avec interlocuteur simulé est déjà démontrée — [Shaikh, 2023, arXiv:2309.12309] |
| **D22** Fin de relation | Annonce anticipée, rituel d'adieu, héritage nommé, export | **Aucun verrou technique.** Personne ne le fait : [Poonsiriwong, 2026, arXiv:2602.07193] — « no platform has implemented deliberate end-of-"life" design ». Obstacle **économique** (verrou V8) |
| **D27** Au-delà de la dyade | Déclaration honnête du parallélisme, étanchéité entre utilisateurs | La « vie propre parmi d'autres intelligences » n'existe pas — mais ce n'est pas le cœur de la fiche, qui porte sur l'**honnêteté** |
| **D36** Exécution déléguée | Curseur d'autonomie par domaine, confirmation informative sur l'irréversible, traçabilité après coup | Le plafond de fiabilité est mesuré : [Liu, 2026, arXiv:2607.10059] — 59,5 % au mieux sur 263 tâches, et **savoir s'abstenir est décorrélé de savoir agir** |
| **D41** Autonomie et lien humain | Deux courbes distinctes (contacts réels, solitude ressentie), relance nominative, refus de rôles hors crise | L'atrophie de compétence est mesurable : [Budzyń, 2025, DOI:10.1016/S2468-1253(25)00133-5] — −6,0 points de détection après exposition à l'IA |
| **D42** Moteur du changement | Entretien motivationnel, ancrage contextuel, rappel d'engagement à fermeté réglable, reprise sans dette | Le **curseur de fermeté** bute sur la sycophancie (verrou V1) : [Cheng, 2025, arXiv:2505.13995], +45 points de préservation de la face contre les humains |
| **D48** Mesure de la relation | Embarquer le WAI-SR ([Munder, 2010, DOI:10.1002/cpp.658], 12 items) et des instruments de bien-être antérieurs au produit | Le banc, l'audit d'omissions et la télémétrie longitudinale existent déjà dans le pilote ; il manque l'alliance et le bien-être |
| **D51** Conseiller pro et perso | Dossiers de vie, journal des décisions **avec les croyances qui les fondaient**, jonction mémoire / conseil à l'échéance | Le geste central — « le dossier remonte de lui-même au bon moment » — est déjà fait en petit par le pilote. Réserve : [Luettgau, 2025, arXiv:2511.15352], **jusqu'à 79 % suivent le conseil sans calibrer l'enjeu** |

> **Reclassement du 28/08/2026 — D41.** Les **mécanismes** de D41 (deux courbes distinctes, relance
> nominative, refus de rôles hors crise, transmission de principes) restent développables et
> figurent ci-dessus. Le **cœur** — l'autonomie regagnée traitée comme *variable de résultat* —
> passe en LIMITE / recherche : il n'a aucun antécédent publié, et les cinq mesures citées par la
> fiche pointent toutes en sens inverse ([Budzyń, 2025] −6,0 points ; [Shi, 2026] −10,3 % / +11,6 % ;
> [Fang, 2025]), tandis que le levier de transfert n'est pas démontré ([Belland, 2016] : pas d'effet
> du retrait progressif de l'aide ; [Abdelghani, 2026] : proposer l'aide autonomisante ne suffit pas
> si la réponse reste disponible). Motif du reclassement : une classification que ses propres
> sources contredisent est le premier défaut qu'un relecteur trouve.

---

## Comment contester ce document

Chaque classement s'appuie sur la synthèse d'une fiche, et chaque fiche est dans `dimensions/`
avec ses références. Pour contester une ligne : ouvrir sa fiche, lire son §5 (l'état de l'art),
et dire quel travail la classe autrement. La procédure est dans
`couverture/contester_une_ligne.md`.
