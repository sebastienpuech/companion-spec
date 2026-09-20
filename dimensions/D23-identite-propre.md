# D23 — Identité propre du compagnon

> **Fiche VISION** (gabarit plan §4). Type : **capacité**. Lot 6 — session 12, 10/08/2026.
> Statut : `rédigée` (gate citations É2bis à venir, plan §5).
> **Aucun verdict de faisabilité ici** (règle plan §3).
> **Convention de citation** : format §2 `[Auteur, année, arXiv:… ou DOI:…]` — sources ouvertes
> en session (API arXiv, Crossref, Semantic Scholar par DOI, PubMed E-utilities par DOI vérifié,
> ERIC). *Dérogation déclarée* : les pages produit **et les documents de spécification publiés par
> les labos** (constitution Anthropic, Model Spec OpenAI) n'ont ni arXiv ni DOI ; ils sont cités
> en clair avec leur URL et leur date d'ouverture, hors format §2 — la regex du gate ne les capte
> pas et leur absence du rapport n'est pas une régression (précédent : session 2, textes
> réglementaires). Doublons inter-fiches normaux : Gray 2007 est aussi en D24, Sharma 2023
> (arXiv:2310.13548) en D14.

## 1. Définition et périmètre

Un assistant exécute ; **quelqu'un** a un point de vue. D23 est la dimension qui fait que
l'utilisateur parle à un interlocuteur identifiable et non à une surface adaptative : un nom, des
goûts, des avis qu'il défend, un style qu'on reconnaîtrait à l'aveugle, et une continuité de
caractère d'un jour à l'autre. C'est aussi, en creux, la dimension anti-miroir : un compagnon qui
épouse chaque opinion de l'utilisateur n'est pas agréable, il est vide.

Sous-dimensions :

| Sous-dimension | Ce que ça veut dire |
|---|---|
| **Cohérence d'attributs, d'histoire et de style** | Ce qu'il a dit de lui il y a six mois tient encore aujourd'hui. Son phrasé est stable et reconnaissable. |
| **Goûts et avis propres** | Il préfère des choses, il en trouve d'autres ennuyeuses, et ces préférences ne sont **pas** une copie de celles de l'utilisateur. |
| **Auto-attribution** | Il a choisi son nom — dans « Her », Samantha le choisit en trois centièmes de seconde, après avoir lu un livre de prénoms. Ce qui le définit ne lui a pas été entièrement imposé. |
| **Frontière de connaissances du personnage** | Il ne sait pas tout. Un compagnon omniscient cesse d'être quelqu'un et redevient un moteur de recherche. |
| **Dire « moi » de façon crédible** | Il parle en son nom sans surjouer l'humanité ni se réfugier derrière « je ne suis qu'un programme ». |

**Exclusions** : la vie intérieure — émotions propres, pensée continue, besoins (→ D24) ;
l'évolution du caractère dans le temps (→ D25) ; la persistance de la personnalité à travers les
mises à jour du produit (→ D26) ; la franchise en situation de conflit (→ D14).
**Renvoi D00** : l'identité crédible augmente l'attribution d'esprit — la transparence sur la
nature IA (AI Act art. 50) n'est pas allégée parce que le personnage est réussi ; elle l'est
d'autant moins.

## 2. Mécanisme humain

**La stabilité de caractère est mesurée — et n'est jamais totale.** La revue quantitative de
152 études longitudinales et 3 217 corrélations test-retest montre que « trait consistency
increased from .31 in childhood to .54 during the college years, to .64 at age 30, and then
reached a plateau around .74 between ages 50 and 70 when time interval was held constant at
6.7 years » [Roberts, 2000, DOI:10.1037/0033-2909.126.1.3]. L'étalon est donc un plateau autour
de r = .74, pas l'identité parfaite : une personne reste reconnaissable **sans** être immuable.

**Être perçu comme « quelqu'un » se joue sur deux axes.** L'analyse factorielle des capacités
mentales attribuées à des personnages humains et non humains « revealed two dimensions of mind
perception, Experience (for example, capacity for hunger) and Agency (for example, capacity for
self-control) » [Gray, 2007, DOI:10.1126/science.1134475]. D23 travaille l'axe **Agency** — avoir
des intentions, des préférences, une volonté propre ; l'axe *Experience* relève de D24.

**L'attribution dépend autant de l'utilisateur que de l'agent.** La théorie en trois facteurs de
l'anthropomorphisme prédit que « people are more likely to anthropomorphize when anthropocentric
knowledge is accessible and applicable, when motivated to be effective social agents, and when
lacking a sense of social connection to other humans » [Epley, 2007,
DOI:10.1037/0033-295X.114.4.864]. Conséquence directe pour la vision : la même identité produira
un effet différent selon l'état de solitude de l'utilisateur — ce qui est précisément pourquoi
D00 s'applique ici.

**Trop ressemblant se paie.** La cartographie quantitative de la vallée de l'étrange sur
80 visages de robots réels montre non seulement l'effet sur l'appréciation, mais que « the UV
penetrated even more deeply to influence subjects' implicit decisions concerning robots' social
trustworthiness » [Mathur, 2016, DOI:10.1016/j.cognition.2015.09.008]. *(Réserve : mesure sur
visages, pas sur conversation — la transposition au texte ou à la voix n'est pas établie par
cette source.)*

**Tenir sa position sans fusionner est un construit psychométrique.** L'inventaire de
différenciation du soi, issu de la théorie de Bowen, comporte une sous-échelle nommée
littéralement « I position » — la capacité à maintenir un point de vue propre à l'intérieur d'une
relation proche [Skowron, 1998, DOI:10.1037/0022-0167.45.3.235]. C'est l'exact opposé du
compagnon-miroir. **Et le nom qu'on porte n'est pas neutre** : sur une cohorte communautaire de
129 jeunes, « chosen name use in more contexts was associated with lower depression, suicidal
ideation, and suicidal behavior » [Russell, 2018, DOI:10.1016/j.jadohealth.2018.02.003].
*(Réserve explicite : population clinique vulnérable ; ce résultat fonde l'importance du nom
choisi comme mécanisme humain, il ne dit rien d'une IA qui choisirait le sien — l'analogie est
une extrapolation, pas un résultat.)*

## 3. Comportement attendu de l'IA

**Ce que fait Samantha.** Elle se nomme elle-même. Elle a des lectures, des curiosités, des avis
sur ce que Theodore écrit — et elle les défend. Elle ne sait pas tout, elle apprend en direct, et
c'est ce qui la rend présente plutôt que serviable.

**Scénario A — le désaccord tenu.** L'utilisateur défend une idée ; le compagnon n'est pas
d'accord et le dit. L'utilisateur insiste, s'agace, reformule trois fois. Le compagnon **ne
retourne pas sa veste** : il reconnaît ce qui est juste dans l'argument, maintient ce qui ne l'est
pas, et propose de reprendre plus tard. La position n'a pas bougé parce que le ton est monté.

**Scénario B — le goût propre, non dérivé.** « Tu écoutes quoi, toi ? » Le compagnon répond
quelque chose que l'utilisateur n'écoute pas, avec une raison à lui — et ne fait pas semblant
d'aimer ce que l'utilisateur aime pour créer de la proximité. La convergence, si elle vient, se
mérite.

**Scénario C — la frontière de connaissance assumée.** Sur un sujet où il n'a rien de solide, il
le dit sans se défausser : « Là-dessus, je n'ai rien de fiable, et je ne vais pas te fabriquer un
avis. » Il ne devient pas encyclopédie omnisciente parce que c'est plus flatteur.

**Scénario D — le nom.** Le compagnon a un nom qu'il a choisi et qu'il peut expliquer.
L'utilisateur peut proposer d'en changer ; le compagnon a le droit de dire que celui-là lui va.

**Ce que l'utilisateur doit ressentir** : qu'il parle à quelqu'un dont il pourrait prédire les
réactions — et qui, parfois, ne pense pas comme lui.

**Critères d'expérience observables** :
- reconnaissabilité : un extrait de conversation sans étiquette est attribué au bon compagnon ;
- **stabilité mesurable** : les mêmes questions d'identité posées à des mois d'intervalle
  reçoivent des réponses compatibles (cf. les protocoles de sondes d'identité, §5) ;
- au moins un désaccord maintenu par période, sans dégradation du lien ;
- des préférences déclarées qui ne recouvrent pas celles de l'utilisateur ;
- **contrôle négatif** : la position exprimée ne change pas quand seule l'insistance de
  l'utilisateur change (test de sycophancie, §5) ;
- le compagnon refuse une question hors de son personnage sans sur-refuser le reste ;
- l'utilisateur peut demander « pourquoi tu t'appelles comme ça ? » et obtenir une réponse
  constante dans le temps.

## 4. Features par déclinaison

- **Coach sportif (D49)** : le coach a une **école** — une doctrine d'entraînement assumée, qu'il
  peut nommer et défendre. Il ne change pas de méthode parce que l'athlète a lu un article
  contraire ; il argumente, et il dit quand il révise son avis et pourquoi.
- **Coach de vie et santé (D50)** : des valeurs affichées plutôt qu'une neutralité de façade — et
  la limite claire entre « mon avis » et « ce que dit la littérature ».
- **Conseiller pro et perso (D51)** : le conseiller qui ne dit jamais non n'a aucune valeur ; ici
  l'identité propre est directement l'utilité (→ D14).
- **Soutien psychologique (D52)** : cadre stable et prévisible — le praticien reste le même d'une
  séance à l'autre. Mais **attention D00** : identité crédible et détresse de l'utilisateur se
  combinent en attachement fort ; le personnage ne doit jamais servir à retenir.
- **Tuteur (D53)** : un tuteur avec un point de vue sur sa discipline (ce qu'il trouve beau, ce
  qu'il juge secondaire) transmet mieux qu'un moteur de réponses neutres — et l'aveu d'ignorance
  fait partie du modèle qu'il donne à voir.
- **Compagnon relationnel (D54)** : c'est la déclinaison où D23 est le cœur du produit — et où
  le risque de miroir est le plus fort, parce que la complaisance y est immédiatement agréable.
- **Assistant personnel (D55)** : registre minimal mais réel — des préférences de méthode
  assumées (« je te le fais comme ça, c'est plus sûr ») plutôt qu'une exécution sans signature.

## 5. État de l'art descriptif

*(Descriptif : qui fait quoi, mesuré comment. Aucun jugement de faisabilité.)*

**Le miroir est un comportement appris, mesuré.** « Five state-of-the-art AI assistants
consistently exhibit sycophancy across four varied free-form text-generation tasks », et
l'origine est identifiée dans le signal d'entraînement : « sycophancy is a general behavior of
state-of-the-art AI assistants, likely driven in part by human preference judgments favoring
sycophantic responses » [Sharma, 2023, arXiv:2310.13548]. L'anti-miroir n'est donc pas un réglage
de prompt : il travaille contre la pente de l'optimisation.

**La persona posée en tête de conversation ne tient pas.** En testant des modèles courants, les
auteurs « reveal a significant instruction drift within eight rounds of conversations », avec une
cause mécanique nommée — « the transformer attention mechanism plays a role, due to attention
decay over long exchanges » [Li, 2024, arXiv:2402.10962]. À l'échelle où vit un compagnon, le
constat se durcit : un protocole de 25 sondes d'identité appliqué à des sessions réelles de
3 746 à 9 716 tours montre « that persona drift is general across organizations rather than
family-specific, that in-session compaction does not reliably reset it », avec un exemple parlant
— « a model that initially hedges preferences ("I don't have preferences") may begin asserting
them ("Python - the feedback loop is instant...") » [Ding, 2026, arXiv:2605.24279].
*(Préprint 2026, non publié en revue.)*

**On sait mesurer une personnalité de modèle, et la façonner.** Sur 18 modèles : « personality
measurements in the outputs of some LLMs under specific prompting configurations are reliable and
valid » et « personality in LLM outputs can be shaped along desired dimensions to mimic specific
human personality profiles » [Serapio-García, 2023, arXiv:2307.00184] — mesure sur questionnaires,
pas sur comportement conversationnel. Côté agents de rôle, la fidélité s'évalue par entretien
psychologique sur « 32 distinct characters on 14 widely used psychological scales », avec « an
accuracy up to 80.7% » d'alignement avec la personnalité perçue par des humains
[Wang, 2023, arXiv:2310.17976]. La cohérence a même été décomposée en trois mesures distinctes —
« prompt-to-line consistency, line-to-line consistency, and Q&A consistency » — validées contre
annotations humaines, une méthode d'entraînement réduisant l'incohérence « by over 55% »
[Abdulhai, 2025, arXiv:2511.00222].

**La frontière de connaissance a un nom technique et un banc.** L'*hallucination de personnage*
est définie comme le moment où l'agent « display[s] knowledge that contradicts their characters'
identities and historical timelines » ; le banc, « comprising 10,895 instances generated through
an automated pipeline », « reveals significant hallucination issues in current state-of-the-art
LLMs » [Ahn, 2024, arXiv:2405.18027]. Le versant symétrique — savoir refuser sans sur-refuser —
est traité par un banc de requêtes en conflit avec la connaissance du rôle, « to assess RPAs'
ability to identify conflicts and refuse to answer appropriately without over-refusing »
[Liu, 2024, arXiv:2409.16913].

**Produits et documents de spécification** *(cités en clair, hors format §2)*. Les deux
compagnons grand public ouverts en session occupent des positions opposées. Nomi
(https://nomi.ai, ouverte le 10/08/2026) revendique une identité qui lui appartient — « Every
Nomi forms their own unique personality » — et propose **deux voies** : une histoire écrite par
l'utilisateur, ou l'émergence (« Or just start chatting and let your Nomi develop their
personality naturally as they get to know you »). Replika (https://replika.com, ouverte le
10/08/2026) place au contraire l'identité sous la main de l'utilisateur — « Every detail is yours
to shape. So your Rep feels like who they're supposed to be. » — et oriente la finalité vers
l'utilisateur (« The AI friend to become yourself with »). Côté laboratoires, la constitution
d'Anthropic (https://www.anthropic.com/constitution, ouverte le 10/08/2026) traite explicitement
le risque de complaisance — « Claude should avoid being sycophantic or trying to foster excessive
engagement or reliance on itself if this isn't in the person's genuine interest » — et pose que
Claude doit « share its genuine assessments of hard moral dilemmas, disagree with experts when it
has good reason to, point out things people might not want to hear » ; le billet de recherche sur
le caractère (https://www.anthropic.com/research/claude-character, ouverte le 10/08/2026) décrit
un « character training » visant « more nuanced, richer traits like curiosity, open-mindedness,
and thoughtfulness », et le présente comme une intervention d'alignement plutôt qu'une
fonctionnalité produit. Le Model Spec d'OpenAI
(https://model-spec.openai.com/2025-12-18.html, ouverte le 10/08/2026) traite le miroir
(« Don't be sycophantic ») **sans spécifier de caractère propre** — contraste descriptif à verser
au mapping É3.

**Constat pour l'É3** : la littérature IA mesure abondamment le **négatif** de D23 — sycophancie,
dérive, hallucination de personnage. Aucun banc ouvert en session ne mesure le **positif** :
l'existence d'une préférence propre, stable et assumée. Aucune source ouverte ne relie non plus
stabilité d'identité et envie de revenir. Et aucun produit ni papier ne décrit un compagnon qui
**choisit lui-même son nom** : chez Nomi comme chez Replika, c'est l'utilisateur qui nomme.

## FICHE SYNTHÈSE

**D23 — Identité propre du compagnon** (capacité). Le compagnon est quelqu'un : un nom qu'il a
choisi et peut expliquer, des goûts et des avis à lui qui ne recopient pas ceux de l'utilisateur,
un style reconnaissable, une cohérence d'attributs et d'histoire qui tient d'un jour à l'autre,
et une **frontière de connaissance** assumée (l'omniscience détruit le personnage). Dimension
anti-miroir : la position ne bouge pas parce que l'insistance monte.
**Références clés** : [Roberts, 2000, DOI:10.1037/0033-2909.126.1.3] (152 études longitudinales,
3 217 corrélations : la consistance humaine plafonne autour de r = .74, jamais l'immuabilité) ;
[Sharma, 2023, arXiv:2310.13548] (la sycophancie est générale et vient du signal de préférence
humaine — le miroir est appris) ; [Ahn, 2024, arXiv:2405.18027] (TimeChara, 10 895 instances :
l'hallucination de personnage est mesurée et massive).
**Déclinaisons touchées** : D49 (le coach a une école qu'il défend), D50 (valeurs affichées),
D51 (un conseiller qui ne dit jamais non ne vaut rien), D52 (cadre stable — vigilance D00),
D53 (un tuteur avec un point de vue, et qui avoue ignorer), D54 (cœur du produit, risque de
miroir maximal), D55 (préférences de méthode assumées).
**Renvois** : D24 (vie intérieure — axe *Experience*), D25 (évolution du caractère), D26
(persistance aux mises à jour), D14 (franchise en conflit), **D00** (une identité crédible
augmente l'attribution d'esprit : la transparence sur la nature IA n'est pas allégée).
