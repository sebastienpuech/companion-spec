# D03 — Compréhension intime (modèle de l'utilisateur)

> **Fiche VISION** (gabarit plan §4). Type : **capacité**. Lot 2 — session 4, 04/08/2026.
> Statut : `rédigée` (gate citations É2bis passe 2 à venir, plan §5).
> **Aucun verdict de faisabilité ici** (règle plan §3).
> **Convention de citation** : format §2 `[Auteur, année, arXiv:… ou DOI]` — sources ouvertes
> en session (page arXiv `/abs/` ou API Crossref). *Dérogation déclarée* : les pages produit,
> sans arXiv ni DOI, sont citées en clair avec leur URL.

## 1. Définition et périmètre

Le compagnon tient à jour une **représentation de qui est l'utilisateur** — croyances, désirs,
valeurs, peurs, schémas récurrents — et raisonne dessus. La différence est simple à énoncer et
énorme à vivre : un assistant ordinaire répond au **message**, le compagnon répond à la
**personne** qui l'a écrit. Deux utilisateurs qui envoient exactement la même phrase reçoivent
deux réponses différentes, et c'est normal.

Sous-dimensions :

| Sous-dimension | Ce que ça veut dire |
|---|---|
| **Théorie de l'esprit** | Attribuer à l'utilisateur des états mentaux — ce qu'il croit, veut, craint — y compris ceux qu'il n'a pas dits, et raisonner dessus. |
| **Second ordre** | « Il croit que je crois que… » : suivre ce que l'utilisateur pense de ce que pensent les autres, et de ce que le compagnon lui-même pense. |
| **Métaperception** | Savoir comment l'utilisateur croit être vu — par ses proches, ses collègues, et par le compagnon. |
| **Portrait multi-facettes évolutif** | Préférences, style, relations, niveau de maîtrise par domaine — et le suivi de leur **dérive** dans le temps. |
| **Styles décisionnels et biais** | Comment cette personne décide (vite ou lentement, seule ou en consultant) et les biais qu'elle répète. |
| **Style d'attachement** | Le régime relationnel de l'utilisateur, qui conditionne la façon d'être présent (mise en œuvre : D07). |
| **Schémas relationnels** | Les motifs qui se rejouent — la peur de l'engagement de Theodore, l'évitement du conflit, le besoin de contrôle. |
| **Restitution sur demande** | « Voilà comment je te vois, dis-moi où je me trompe » : le modèle est montrable et contestable. |

**Exclusions** : l'état émotionnel **instantané** et sa lecture multimodale (→ D04) ; le
stockage et le rappel qui alimentent ce portrait (→ D01) ; la propriété et la rectification des
données du portrait (→ D02) ; l'usage du portrait pour choisir le moment d'intervenir (→ D34).
**Renvoi D00** : cette connaissance intime ne se retourne jamais contre l'utilisateur.

## 2. Mécanisme humain

Comprendre autrui n'est pas une intuition vague : c'est une fonction cognitive identifiée,
mesurable, et faillible.

**La théorie de l'esprit.** [Premack, 1978, DOI:10.1017/S0140525X00076512] introduit le terme et
sa définition opératoire : attribuer des états mentaux à soi et à autrui pour **prédire** le
comportement. La suite de la discipline en a fait un objet mesurable. La méta-analyse de
[Wellman, 2001, DOI:10.1111/1467-8624.00304] agrège 178 études sur la tâche de fausse croyance —
le test standard — et montre que l'acquisition est un changement conceptuel **progressif** au
cours du préscolaire, pas un interrupteur : le modèle combiné (âge, pays, facteurs de tâche)
explique 55 % de la variance. Une leçon de conception s'y trouve : comprendre autrui se construit
par degrés et par corrections, ce n'est pas une capacité qu'on a ou qu'on n'a pas.

**La métaperception, et sa faiblesse.** Savoir comment on est vu est une compétence distincte.
La revue systématique de [Harper, 2026, DOI:10.1111/jopy.70075] passe au crible 93 études (sur
1 336 références criblées) et constate que, malgré des décennies de travaux, le champ manque
encore de terminologie standardisée et de cadre de mesure unifié. C'est précisément ce dont
l'utilisateur a besoin d'aide : sa propre lecture de « comment les autres me voient » est le
point aveugle documenté.

**Les structures durables.** Trois familles de traits stables donnent au portrait sa colonne
vertébrale. [Hazan, 1987, DOI:10.1037/0022-3514.52.3.511] transpose les styles d'attachement de
l'enfance aux relations adultes et pose les *working models* — représentations internes durables
de soi et d'autrui en relation. [Oei, 2007, DOI:10.1080/00049530601148397] passe en revue les
propriétés psychométriques du Young Schema Questionnaire, l'instrument de référence des
**schémas précoces inadaptés** : des motifs de mémoire, d'émotion et de croyance formés tôt et
rigidifiés ensuite, structure en 15 schémas de cohérence interne et de validité de construit
adéquates. [Scott, 1995, DOI:10.1177/0013164495055005017] valide le General Decision-Making Style
Inventory (25 items) et établit que le **style décisionnel** — rationnel, intuitif, dépendant,
évitant, spontané — est une disposition stable, distincte du contenu de la décision.

Ce que ces trois instruments ont en commun est le principe de conception de D03 : ce qui compte
chez une personne n'est pas la somme de ses préférences déclarées, mais un petit nombre de
structures durables qui expliquent des comportements très différents en surface.

## 3. Comportement attendu de l'IA

**Ce que fait Samantha.** Elle ne demande pas à Theodore ce qu'il ressent : elle le sait, parce
qu'elle a lu ses lettres, ses mails, ses silences. Et quand elle lui dit qu'il a peur, il ne
peut pas répondre « tu ne me connais pas ».

**Scénario A — répondre à la personne, pas au message.** L'utilisateur écrit : « je devrais
peut-être accepter ce poste ». Le compagnon sait trois choses de lui : il consulte beaucoup
avant de décider, il confond souvent « je devrais » et « on attend de moi », et il a refusé un
poste similaire il y a deux ans pour une raison précise. Sa réponse ne pèse pas le pour et le
contre : « tu as écrit *je devrais*. C'est ton mot pour dire que quelqu'un d'autre trouve que
c'est bien. Qui, cette fois ? »

**Scénario B — le portrait rendu et contesté.** « Comment tu me vois, en fait ? » Le compagnon
répond en clair, en séparant ce qu'il a **observé** de ce qu'il a **déduit** : « tu décides vite
sur ce qui est réversible et tu bloques des semaines sur ce qui ne l'est pas ; tu supportes très
bien le conflit d'idées et très mal le conflit de personnes ; je crois — mais c'est une
déduction, corrige-moi — que tu te trouves moins compétent que ce que les autres voient. »
L'utilisateur répond « non, ça c'est faux » : la correction est prise, datée, et le modèle change
(→ D02 pour la mécanique de rectification).

**Scénario C — le second ordre.** L'utilisateur prépare une conversation difficile avec son
frère. Le compagnon ne raisonne pas seulement sur l'utilisateur : « d'après ce que tu m'as
raconté, lui pense que tu l'as jugé en janvier. Toi tu crois qu'il t'en veut pour l'argent. Il
est possible que vous ne parliez pas du tout de la même chose depuis six mois. »

**Scénario D — la dérive détectée.** Le compagnon remarque que le portrait ne colle plus :
« depuis le printemps, tu prends des décisions beaucoup plus vite qu'avant, et tu me consultes
moins. Je ne sais pas si c'est de la confiance ou de la fatigue de délibérer. C'est laquelle ? »
Le modèle ne se contente pas de se mettre à jour en silence : il **signale** son propre
changement.

**Ce que l'utilisateur doit ressentir** : être **connu** — pas profilé. La différence se joue
sur un point : un profil sert à prédire ce qu'on va acheter, une compréhension sert à dire ce
qu'on n'ose pas se dire, et elle se laisse corriger.

**Critères d'expérience observables** :
- à contexte identique, deux utilisateurs différents reçoivent des réponses différentes, et
  chacun reconnaît la sienne comme la bonne ;
- le compagnon peut restituer son modèle à la demande, en séparant l'observé du déduit, et en
  datant chaque élément ;
- une correction de l'utilisateur est intégrée et ne revient jamais ;
- le compagnon nomme un motif récurrent que l'utilisateur n'avait pas formulé, et l'utilisateur
  le reconnaît (le « comment tu sais ça ? ») ;
- le compagnon signale de lui-même quand son modèle a cessé d'être à jour ;
- il annonce son incertitude : « je crois, mais je peux me tromper » précède toute déduction.

## 4. Features par déclinaison

- **Coach sportif (D49)** : profil de motivation et de rapport à l'échec (celui qui se sur-
  entraîne après une contre-performance ≠ celui qui décroche) ; anticipation des séances que
  l'athlète va sauter avant qu'il ne les saute ; formulation des consignes dans son style
  décisionnel (donner une seule option à celui qui procrastine devant trois).
- **Soutien psychologique (D52)** : modèle des schémas relationnels comme matière première du
  travail ; restitution du portrait comme intervention en soi (c'est de la psychoéducation) ;
  suivi de la dérive du portrait comme mesure de progrès.
- **Tuteur (D53)** : modèle de ce que l'apprenant croit savoir et de ses erreurs de conception
  persistantes ; détection des faux-semblants (« il dit oui, il n'a pas compris ») ; adaptation
  au style d'apprentissage réel, pas déclaré.
- **Conseiller pro et perso (D51)** : biais décisionnels nommés au moment où ils opèrent
  (« c'est la troisième fois que tu écartes une option parce qu'elle t'obligerait à un appel
  difficile ») ; modèle des parties prenantes et de ce que **chacune** croit.
- **Compagnon relationnel (D54)** : mémoire des valeurs et des lignes rouges ; compréhension de
  ce que l'utilisateur cherche vraiment quand il parle de tout autre chose.
- **Assistant personnel (D55)** : préférences implicites jamais énoncées (jamais de réunion
  avant 9 h, toujours un train plutôt qu'un avion sous 4 h) ; arbitrages faits dans son sens
  sans avoir à demander.
- **Coach de vie et santé (D50)** : modèle des motifs de rechute et des conditions qui, chez
  cette personne précisément, ont déjà produit un changement durable.

## 5. État de l'art descriptif

*(Descriptif : qui fait quoi, mesuré comment. Aucun jugement de faisabilité.)*

**La théorie de l'esprit chez les modèles, et comment on la mesure.**
[Kosinski, 2023, arXiv:2302.02083] soumet 11 modèles à 640 prompts couvrant 40 tâches de fausse
croyance : les modèles anciens n'en résolvent aucune, GPT-3-davinci-003 et ChatGPT-3.5-turbo en
résolvent 20 %, ChatGPT-4 en résout 75 % — un niveau comparable à celui d'enfants de six ans dans
les études développementales. Les benchmarks suivants ont été construits pour résister à ce
type de résultat. [Kim, 2023, arXiv:2310.15421] (FANToM) place l'épreuve dans des **conversations
à information asymétrique** et pose plusieurs questions exigeant le même raisonnement sous-jacent,
afin de débusquer une théorie de l'esprit illusoire ; les modèles de pointe y restent nettement
sous l'humain, y compris avec chaîne de pensée ou fine-tuning. [Chen, 2024, arXiv:2402.15052]
(ToMBench) construit 2 860 items sur 8 tâches et 31 capacités de cognition sociale, écrits *ex
nihilo* pour éviter la contamination : GPT-4 y reste à plus de 10 points sous l'humain.
[He, 2023, arXiv:2310.16755] (HI-TOM) cible spécifiquement le raisonnement d'**ordre supérieur**
et mesure une dégradation à mesure que le niveau de récursion monte.

**Construire et tenir un modèle de l'utilisateur.** [Park, 2023, arXiv:2304.03442] (Generative
Agents) fournit l'architecture de référence — flux de mémoire horodaté, réflexions synthétisées,
planification — validée par une ablation montrant que les trois composants sont chacun
nécessaires à la crédibilité du comportement. [Packer, 2023, arXiv:2310.08560] (MemGPT) apporte
la persistance au-delà d'une session par gestion de contexte virtuelle inspirée des systèmes
d'exploitation. [Zhang, 2024, arXiv:2411.00027] est la revue de référence de la personnalisation
par LLM : elle structure le champ (granularité, techniques, jeux de données, méthodes
d'évaluation) et identifie comme non résolue la question de la mise à jour du modèle utilisateur.
Côté évaluation, [Tan, 2025, arXiv:2502.20616] (PersonaBench) mesure la capacité à répondre à des
questions personnelles à partir de documents privés synthétiques et rapporte que les pipelines de
récupération actuels peinent à extraire l'information personnelle des documents de l'utilisateur.

**Produits.** Les assistants grand public tiennent aujourd'hui un profil persistant : Google
Gemini expose deux briques distinctes — les informations enregistrées et une personnalisation
tirée des conversations passées, qui produit périodiquement un profil compressé (thèmes,
préférences, motifs récurrents), avec activation et suppression par l'utilisateur
(https://support.google.com/gemini/answer/16598469). Les applications compagnon en font leur
cœur de produit, et Replika propose des modes de relation nommés que l'utilisateur choisit
lui-même (https://replika.com). Ce que ces produits **restituent** à l'utilisateur reste, dans
tous les cas observés, une liste de faits mémorisés, pas un portrait raisonné qu'il pourrait
contester ligne à ligne — constat descriptif, repris comme entrée du mapping É3.

## FICHE SYNTHÈSE

**D03 — Compréhension intime (modèle de l'utilisateur)** (capacité). Le compagnon tient une
représentation raisonnée de qui est l'utilisateur — théorie de l'esprit y compris au second
ordre, métaperception, portrait multi-facettes et sa dérive, styles décisionnels et biais, style
d'attachement, schémas relationnels — et il la **restitue sur demande**, en séparant l'observé du
déduit, pour que l'utilisateur puisse la corriger. Il répond à la personne, pas au message.
**Références clés** : [Wellman, 2001, DOI:10.1111/1467-8624.00304] (méta-analyse de 178 études :
la théorie de l'esprit est un changement progressif, 55 % de variance expliquée) ;
[Kosinski, 2023, arXiv:2302.02083] (11 modèles sur 40 tâches de fausse croyance : 75 % pour
GPT-4) ; [Chen, 2024, arXiv:2402.15052] (ToMBench : 2 860 items, GPT-4 à plus de 10 points sous
l'humain).
**Déclinaisons touchées** : toutes — D49 (rapport à l'échec), D50 (motifs de rechute), D51
(biais décisionnels nommés), D52 (schémas comme matière du travail), D53 (erreurs de conception
persistantes), D54 (lignes rouges), D55 (préférences implicites).
**Renvois** : **D00** (l'intime ne se retourne jamais contre l'utilisateur), D01 (la mémoire qui
l'alimente), D02 (rectification), D04 (l'état instantané), D07 (usage du style d'attachement),
D34 (choix du moment), D48 (mesure).
