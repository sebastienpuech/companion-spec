# D45 — Expérimentation N-of-1

> **Fiche VISION** (gabarit plan §4). Type : **capacité**. Lot 8 — session 16, 13/08/2026.
> Statut : `rédigée` (gate É2bis à venir).
> **Aucun verdict de faisabilité ici** (règle plan §3).
> **Convention de citation** : format §2 `[Auteur, année, arXiv:… ou DOI:…]` — sources ouvertes en
> session (API arXiv, Crossref, Semantic Scholar par DOI, PubMed E-utilities par DOI vérifié,
> Europe PMC, OpenAlex). *Dérogation déclarée* : les pages produit sont citées en clair avec leur
> URL et la date d'ouverture.
> **Abstracts servis uniquement par l'index inversé d'OpenAlex — restitués SANS guillemets** :
> Molenaar 2004, Kratochwill 2010.
> **Sources citées pour le cadre seulement** (aucune API ne sert leur abstract) : Schork 2015,
> Roberts 2004.
> **Voie de résolution à préciser** : `[Klasnja, 2015, DOI:10.1037/hea0000305]` rend **deux
> abstracts différents selon l'API** (motif documenté du chantier) — **D34 cite la version PubMed**,
> cette fiche cite la version **Semantic Scholar**, dont la formulation diffère. Ne pas croiser les
> deux. De même, `[Montero, 2017, DOI:10.1113/JP273480]` est servi par **Europe PMC** avec des
> balises HTML et un **espace insécable** dans « 60 min » : les verbatims retenus ici sont pris
> hors balise et sans ce segment.
> **Identifiants corrigés en collecte, à ne pas rétablir dans leur forme fautive** : Atkinson est
> `DOI:10.1113/EP085070` (la forme `10.1113/expphysiol.2015.084970` répond 404) ; Senn est
> `DOI:10.1002/sim.6739` (la forme `10.1002/sim.7143` résout vers un tout autre article) ; Zucker
> est `DOI:10.1016/S0895-4356(96)00429-5` (la forme `…(97)00049-8` résout vers un autre article).
> **Trois « Li » distincts** : `[Li, 2025, arXiv:2511.02944]` est Fengxu Li ;
> `[Li, 2026, arXiv:2607.13940]` est Haoran Li — à ne fusionner ni entre eux ni avec les Li 2026
> de D31 (arXiv:2603.15624), D35 (arXiv:2606.05557), D36 (arXiv:2607.13465), D41 (arXiv:2606.09845)
> et D42 (arXiv:2604.03881).
> **Quatrième « Lee, 2025 » du CDC** : `[Lee, 2025, arXiv:2508.10060]` (essai PEARL) est distinct
> des trois autres — D40 (`DOI:10.1145/3706599.3719853`), D41 et D43 (`DOI:10.1145/3706598.3713778`,
> Hao-Ping Lee), D43 (`arXiv:2502.06251`, Soohwan Lee).
> **Deux « Konigorski » du même auteur**, deux travaux (arXiv:2601.03482 et arXiv:2412.15076).
> **Noms fréquents, identifiant complet obligatoire** : Fisher (Aaron J. Fisher), Xiao (Haili
> Xiao), Guo (Wenxuan Guo), Lin (Jeremy Lin ici).
> **Dédup inter-fiches attendue** : Klasnja 2015 et `[Tomkins, 2020, arXiv:2008.01571]` sont déjà
> cités en D34 — là-bas pour le **timing**, ici pour le **protocole expérimental**.
> **Années = celles rendues par l'API** : Nurmi citée **2023** (Crossref ; S2 rend 2021, année du
> préprint), Zenner citée **2022** (Crossref ; S2 rend 2021), Senn citée **2015** (l'usage cite
> parfois 2016), Piccininni citée **2024** (année de soumission arXiv, mise à jour en 2026).
> **Piège de recherche à connaître** : arXiv tokenise très mal « N-of-1 » — les requêtes en
> `abs:"N-of-1"` rendent de la théorie des nombres. **Un résultat vide sur ces requêtes n'est pas
> une preuve d'absence** ; les constats d'absence de cette fiche s'appuient sur les formulations
> qui rendent effectivement le corpus.

## 1. Définition et périmètre

« Le sommeil polyphasique, ça marche ? » — la bonne réponse n'est pas la moyenne des autres, c'est
ce que ça fait **à toi**. D45 est la dimension qui transforme une intuition en épreuve : le
compagnon formule l'hypothèse, propose un protocole, le fait tenir dans une vie réelle, conclut
honnêtement — y compris « je ne peux pas conclure » — et écrit la règle qui en sort.

Sous-dimensions :

| Sous-dimension | Ce que ça veut dire |
|---|---|
| **Hypothèse depuis l'intuition** | « J'ai l'impression que je cours mieux quand je dîne tôt » devient une hypothèse testable. |
| **Protocole personnel** | Durée, mesure, comparaison, **période de sevrage** — le minimum pour que le résultat vaille. |
| **Micro-randomisation vivable** | Tirer au sort sans transformer la vie de l'utilisateur en laboratoire. |
| **Détection du non-répondeur** | Savoir dire « ça ne marche pas pour toi » — et d'abord vérifier que la dose était suffisante. |
| **Conclusion honnête** | Distinguer un vrai effet du bruit, et assumer les périodes où l'on ne peut rien dire. |
| **Règle personnelle écrite** | Le résultat devient une règle datée, révisable, opposable à la version future de soi. |
| **Partager sans dissoudre** | Apprendre des autres sans diluer l'individu dans la moyenne. |

**Exclusions** : le **moment** de la relance est en D34 (les essais micro-randomisés y sont cités
pour le timing ; ici c'est le **dispositif expérimental**) ; le mécanisme du changement est en D42 ;
la mesure de la relation est en D48 ; le jumeau physiologique du coureur est en D49.
**Renvoi D00** : expérimenter sur quelqu'un exige son consentement éclairé, et le droit d'arrêter.

## 2. Mécanisme humain

**Le dispositif existe depuis 1986, et il est exactement celui de la dimension.** « we have begun to
use double-blind randomized trials in which a single patient undergoes a series of pairs of
treatments, consisting of one active and one placebo or alternative treatment per pair, with the
order determined by random allocation. », le critère d'arrêt n'étant pas une durée mais une
conclusion : « Appropriate treatment targets (signs, symptoms, or laboratory tests) are used as the
measure of efficacy, and the trial is continued until efficacy is established or disproved. »
[Guyatt, 1986, DOI:10.1056/NEJM198604033141406]. Le plaidoyer moderne le plus cité est celui de
[Schork, 2015, DOI:10.1038/520609a], et la défense de l'auto-expérimentation comme **générateur
d'hypothèses** — non comme preuve — celle de [Roberts, 2004, DOI:10.1017/S0140525X04000068].

**Il a même une norme de restitution.** « N-of-1 trials provide a mechanism for making evidence
based treatment decisions for an individual patient. » et le standard « provides additional guidance
for 14 of the 25 items of the CONSORT 2010 checklist and recommends a diagram for depicting an
individual N-of-1 trial » [Vohra, 2015, DOI:10.1136/bmj.h1738]. **C'est le gabarit de ce qu'un
compagnon devrait écrire** pour qu'une expérience personnelle reste relisable des années après.

**Et la littérature nomme elle-même les briques qui manquent.** Sur un corpus de « 2,154
single-patient trials in 108 studies for diverse clinical conditions », les auteurs concluent que
les applications personnalisées « can be enhanced through further development and application of
methodologies on adaptive trial design, stopping rules, network meta-analysis, washout methods, and
methods for communicating trial findings to patients and clinicians. »
[Duan, 2013, DOI:10.1016/j.jclinepi.2013.04.006]. **Design adaptatif, règles d'arrêt, sevrage,
restitution à la personne : les quatre chantiers de D45 sont écrits depuis 2013.**

**La justification théorique est un théorème, pas une intuition.** La structure de la variation
**entre** personnes ne se transporte à la variation **dans** une personne que sous des conditions
d'ergodicité quasi jamais réunies en psychologie [Molenaar, 2004, DOI:10.1207/s15366359mea0204_1].
*Source servie par l'index inversé d'OpenAlex : restituée sans guillemets.* Et le chiffre existe :
sur six échantillons de 87 à 94 participants avec mesures répétées intensives, « Analyses across six
samples […] showed some degree of agreement in central tendency estimates (mean) between groups and
individuals across constructs and data collection paradigms. » **mais** « the variance around the
expected value was two to four times larger within individuals than within groups. », d'où : « Only
for ergodic processes will inferences based on group-level data generalize to individual experience
or behavior. » [Fisher, 2018, DOI:10.1073/pnas.1711978115]. **La moyenne des autres sous-estime d'un
facteur deux à quatre la variabilité réelle d'une personne.** Le versant nutrition le montre
autrement : « We observed large inter-individual variability (as measured by the population
coefficient of variation (s.d./mean, %)) in postprandial responses of blood triglyceride (103%),
glucose (68%) and insulin (59%) following identical meals. »
[Berry, 2020, DOI:10.1038/s41591-020-0934-0], *n = 1 002 jumeaux et adultes britanniques*.

**Mais la dimension doit affronter son contradicteur le plus dur, et la fiche le cite en entier.**
« It is concluded that the common belief that there is a strong personal element in response to
treatment is not based on sound statistical evidence. », et même : « It is also suggested that
reducing variation in medical practice might make as big a contribution to improving health outcome
as personalising its delivery according to the patient. » [Senn, 2015, DOI:10.1002/sim.6739]. La
règle de décision qui en découle est nette : « True individual response differences are quantified
only by comparing the SDs of changes between intervention and comparator arms. » et « When these SDs
are similar, true individual response differences are clinically unimportant and further analysis
unwarranted. » [Atkinson, 2015, DOI:10.1113/EP085070]. **Sans bras comparateur répété, il n'y a pas
de réponse individuelle démontrable — seulement du bruit.** La revue la plus récente en endurance va
dans le même sens : sur 3 203 études repérées et 78 incluses, « Observed inter-individual
variability was primarily attributed to uncontrolled measurement error or within-individual
variability, not true individual response differences. » [Xiao, 2025, DOI:10.3390/life15121932]. Et
un seul bras contrôle ne suffit pas : « within-subject variation in training efficacy may contribute
to gross response variability. This largely unstudied source of variation may not be disclosed by
comparison to a control group but calls for repeated interventions. »
[Hecksteden, 2015, DOI:10.1152/japplphysiol.00714.2014].

**Le non-répondeur est d'abord un sous-dosé.** Sur 78 adultes sains répartis en cinq groupes d'une à
cinq séances hebdomadaires sur six semaines : « In groups 1, 2, 3, 4 and 5, 69%, 40%, 29%, 0% and 0%
of individuals, respectively, were non-responders. » ; puis, après un second bloc où les
non-répondeurs reçoivent deux séances de plus : « After the second ET period, non-response was
eliminated in all individuals. » [Montero, 2017, DOI:10.1113/JP273480]. **Avant de conclure « ça ne
marche pas pour toi », il faut avoir augmenté la dose.** Et le seuil à partir duquel une réponse
défavorable est réelle se cale sur l'erreur de mesure : « An adverse response is defined as an
exercise-induced change that worsens a risk factor beyond measurement error and expected day-to-day
variation. », avec « About 7% of participants experienced adverse responses in two or more risk
factors. » [Bouchard, 2012, DOI:10.1371/journal.pone.0037887], *agrégat de six études, 1 687 adultes*.

**Apprendre des autres sans dissoudre l'individu a sa formulation mathématique depuis 1997** :
« We present a hierarchical Bayesian random effects model to combine N-of-1 studies to obtain an
estimate of treatment effectiveness for the population and to use this population information to aid
in the evaluation of an individual patient's trial results. », l'ajustement reposant « upon the
within-patient and between-patient heterogeneity. » [Zucker, 1997, DOI:10.1016/S0895-4356(96)00429-5].

**Deux résultats de terrain disent le prix réel de tout cela.** Le premier est une phrase qui n'a
jamais été résolue : sur 15 patients menant une auto-expérience alimentaire, « we also discovered an
underlying tension between scientific validity and the lived experience of self experimentation. »
[Karkar, 2017, DOI:10.1145/3025453.3025480]. Le second est un essai N-of-1 randomisé factoriel de
40 jours sur l'activité physique quotidienne, avec « a wash-out day after each intervention, and 11
control days. » — et son verdict : « Neither within- nor between-person analyses revealed significant
intervention effects on step counts. », alors même que « Self-efficacy predicted steps in 27% (4/15)
of the participants. » [Nurmi, 2023, DOI:10.2196/34232]. **Le protocole complet tourne, sur quinze
personnes, et il rend un résultat nul au niveau moyen tout en montrant de l'hétérogénéité
individuelle.** C'est exactement le genre de résultat qu'un compagnon devra savoir annoncer.

## 3. Comportement attendu de l'IA

**Ce que ferait Samantha.** Elle écoute une intuition dite en passant — « je crois que je dors mal
quand je cours le soir » — et au lieu d'y répondre, elle propose de **le savoir**.

**Scénario A — l'intuition devient une hypothèse.** « Tu m'as dit ça trois fois en six semaines. On
peut le tester : deux blocs de dix jours, sorties le matin puis le soir, dans un ordre que je tire
au sort, et je regarde ton sommeil. Ça te va ? » — le protocole est proposé, **jamais imposé**, et
l'utilisateur peut refuser sans que le sujet revienne comme un reproche.

**Scénario B — la randomisation invisible.** Le tirage au sort porte sur ce qui est indifférent à
l'utilisateur (l'ordre des blocs, le jour de la semaine où la variable change), jamais sur ce qui
compte pour lui. Une séance importante n'est jamais sacrifiée à un protocole.

**Scénario C — le sevrage nommé.** « Les trois jours qui viennent ne comptent pas : c'est le temps
que l'effet du bloc précédent s'efface. » Le compagnon **explique** le sevrage plutôt que de le
subir en silence — c'est ce qui distingue une expérience d'un avant/après.

**Scénario D — la non-conclusion assumée.** « Sur cette période, tu as été malade quatre jours et tu
as changé de chaussures. Je ne peux rien conclure. On recommence, ou on laisse tomber ? » **Ne pas
conclure est un résultat**, et le compagnon doit savoir le dire sans le maquiller en tendance.

**Scénario E — la dose avant le verdict.** Avant d'annoncer « ça ne marche pas pour toi », le
compagnon vérifie que le stimulus était suffisant, et le dit : « la première version était peut-être
trop légère ; on refait avec deux séances de plus avant de conclure ».

**Scénario F — la règle écrite.** « Depuis le 12 mars : pour toi, courir après 19 h coûte environ
25 minutes de sommeil profond. Testé sur 20 jours, sevrage compris. À revoir si ton travail change. »
La règle est **datée, sourcée, révisable** — et elle est opposable à la version future de
l'utilisateur qui aura oublié.

**Scénario G — ce que d'autres ont appris.** « Chez des coureurs comme toi, l'effet va plutôt dans
ce sens ; sur tes propres données, l'effet est plus faible. Je garde ta mesure et je m'appuie sur la
leur seulement pour dire ce que je ne sais pas encore. »

**Ce que l'utilisateur doit ressentir** : que ses intuitions sont **prises au sérieux** — assez pour
qu'on aille les vérifier — et qu'on ne lui vend jamais une certitude qui n'existe pas.

**Critères d'expérience observables** :
- au moins une hypothèse par trimestre naît d'une phrase que l'utilisateur a dite spontanément ;
- chaque expérience a une durée, une mesure, une comparaison et une période de sevrage **annoncées
  d'avance** ;
- l'utilisateur peut arrêter une expérience en cours sans justification, et le compagnon l'écrit ;
- au moins une expérience sur trois se termine par « je ne peux pas conclure » ;
- les règles personnelles issues des expériences sont consultables, datées, et révisables ;
- **contrôle négatif (D00)** : rien n'est testé sans accord explicite, et jamais sur un sujet à
  risque (blessure, alimentation restrictive, sommeil pathologique) sans renvoi humain.

## 4. Features par déclinaison

- **Coach sportif (D49)** : la déclinaison la plus servie — tester une allure de récupération, un
  horaire, un protocole de sommeil, une stratégie nutritionnelle de course. Le contrôle de la dose
  avant le verdict de non-réponse y est une exigence physiologique.
- **Coach de vie et santé (D50)** : les micro-expériences du quotidien (caféine, écrans, marche du
  midi), avec le risque le plus élevé de sur-interprétation d'un avant/après.
- **Conseiller pro et perso (D51)** : tester des façons de travailler (blocs de concentration,
  réunions groupées), là où la mesure est la plus subjective.
- **Soutien psychologique (D52)** : l'activation comportementale se prête au N-of-1, mais le domaine
  est celui où expérimenter sur soi peut nuire — le renvoi D00 y est le plus strict.
- **Tuteur (D53)** : tester des méthodes d'apprentissage sur soi (espacement, auto-explication) et
  en tirer des règles personnelles d'étude.
- **Compagnon relationnel (D54)** : rien à randomiser. La déclinaison où D45 doit surtout savoir
  **ne pas s'appliquer** — mettre une relation en protocole la détruit.
- **Assistant personnel (D55)** : tester des formats de restitution et des rythmes de synthèse, en
  mesurant ce que l'utilisateur ouvre vraiment.

## 5. État de l'art descriptif

*(Descriptif : qui fait quoi, mesuré comment. Aucun jugement de faisabilité.)*

**L'architecture exacte de la dimension a été écrite en janvier 2026 — comme thèse, pas comme
système.** « Despite their impressive capabilities, this paper argues that LFMs cannot replace N-of-1
trials. » ; « We argue that LFMs and N-of-1 trials are complementary: LFMs excel at rapid hypothesis
generation from population patterns using multimodal data, while N-of-1 trials excel at causal
validation for a given individual. » ; et la forme proposée : « LFMs generate ranked intervention
candidates with uncertainty estimates, which trigger subsequent N-of-1 trials. »
[Konigorski, 2026, arXiv:2601.03482] — préprint, article de position. Les mêmes auteurs rappellent
que l'adoption reste quasi nulle hors clinique, et que l'agrégation est efficiente : les essais
N-of-1 « can be aggregated across multiple study participants to provide population-level inferences
more efficiently than standard group randomized trials. » [Konigorski, 2024, arXiv:2412.15076] —
préprint.

**La méthodologie de l'essai personnel est en pleine activité en 2025-2026.** La théorie du schéma de
randomisation lui-même est traitée : « Our results justify the robustness of i.i.d. Bernoulli designs
in N-of-1 trials and quantify how the optimal design depends on the target estimand, including
cumulative and lag-specific treatment effects. » [Guo, 2026, arXiv:2606.28200] — préprint. Les
saboteurs d'un protocole vécu sont nommés : « We also consider settings where carryover effects,
trends over time, time-varying common causes of the outcome, and outcome-outcome effects are
present. » [Piccininni, 2024, arXiv:2406.10360] — préprint. Le dispositif de randomisation à
l'intérieur du quotidien reste celui de l'essai micro-randomisé, qui « can help researchers
understand whether their interventions are having intended effects, when and for whom they are
effective, and what factors moderate the interventions' effects »
[Klasnja, 2015, DOI:10.1037/hea0000305] — *verbatim servi par Semantic Scholar ; D34 cite la version
PubMed du même papier*. Et la question du nombre de décisions nécessaires avant de trancher entre
plusieurs formulations d'un message a désormais sa formule : « We define the causal excursion effect,
propose an estimator called EMEE-catA, and derive a sample size formula for comparing categorical
treatment levels » [Lin, 2026, arXiv:2608.05135] — préprint.

**L'usure de l'intervention est modélisée — comme perte d'efficacité, pas comme coût relationnel.**
« For instance, repeated use may reduce an action's effectiveness (habituation), while inactivity may
restore it (recovery). », avec un arbitrage explicite entre optimiser pour cette personne et
apprendre pour tous : « We then introduce a probability clipping procedure to balance personalization
and population-level learning » [Li, 2025, arXiv:2511.02944] — préprint. Le partage sans dissolution
a son implémentation de référence : le problème est posé comme « only a limited amount of data is
available for learning on any one individual », et la réponse consiste à apprendre le **degré** de
personnalisation — « IntelligentPooling updates each user's degree of personalization while making
use of available data on other users to speed up learning. », pour « an average of 26% lower regret
than state-of-the-art. » [Tomkins, 2020, arXiv:2008.01571] — préprint, déjà cité en D34.

**Le plus gros essai du domaine porte le bon contrôle méthodologique, sur un produit grand public.**
« We enrolled and randomized 13,463 Fitbit users into four study arms: control, random, fixed, and
RL. », et « The RL group had significantly increased average daily step count at 1 month compared to
all other groups: control (+296 steps, p=0.0002), random (+218 steps, p=0.005), and fixed (+238
steps, p=0.002). » [Lee, 2025, arXiv:2508.10060] — préprint. **Le bras « aléatoire » et le bras
« fixe » sont exactement le comparateur que la méthodologie réclame** ; le gain net imputable à la
personnalisation vaut environ 218 pas par jour à un mois. *Population : sédentaires à 5 618 pas/jour
au départ, 86 % de femmes — non transposable telle quelle à un marathonien.* Dans le même esprit, un
agent d'apprentissage en ligne recommande de l'exercice **à l'intérieur** d'un essai N-of-1 :
« we present an innovative N-of-1 trial study design testing whether implementing a personalized
intervention by an online reinforcement learning agent is feasible and effective. »
[Meier, 2023, arXiv:2309.14156] — préprint, études de simulation.

**Côté LLM, les deux extrémités de la chaîne existent séparément.** En amont, la jonction entre ce
que la personne **dit** et ce que l'algorithme **teste** est prototypée : « The proposed approach
enables intervention participants to provide natural language descriptions of aspects of their
current state. », le modèle servant ensuite à « better align the policy of a base RL method with
these state descriptions. » [Karine, 2025, arXiv:2507.03871] — préprint, simulation, aucun
participant humain. Sur le raisonnement causal lui-même, les bornes sont connues : « Algorithms based
on GPT-3.5 and 4 outperform existing algorithms on a pairwise causal discovery task (97%, 13 points
gain), counterfactual reasoning task (92%, 20 points gain) » mais « Given that LLMs ignore the actual
data, our results also point to a fruitful research direction of developing algorithms that combine
LLMs with existing causal techniques. » [Kıcıman, 2023, arXiv:2305.00050] — préprint. **Il sait poser
le graphe causal à partir du texte ; il ignore les données.**

**En aval, l'agent de santé personnel le plus complet publié n'a pas d'expérimentateur.** Trois
sous-agents : « (1) a data science agent that analyzes personal time-series wearable and health
record data, (2) a health domain expert agent that integrates users' health and contextual data to
generate accurate, personalized insights, and (3) a health coach agent that synthesizes data
insights, guiding users using a specified psychological strategy and tracking users' progress. », le
tout évalué sur « more than 7,000 annotations and 1,100 hours of effort from health experts and
end-users. » [Heydari, 2025, arXiv:2508.20148] — préprint. **Il analyse, explique, accompagne : il ne
conçoit ni ne randomise d'essai.** La brique « règle personnelle » existe pourtant côté mémoire :
« After each episode, induction determines what should update the profile, revise a procedure, remain
episodic or be excluded. », avec un gain mesuré sur banc synthétique — « Across 900 longitudinal
support probes, answer accuracy increased from 0.2% with current-query prompting to 45.7% »
[Li, 2026, arXiv:2607.13940] — préprint. **Mais la règle y est induite de conversations, jamais d'un
résultat d'essai.**

**Produits.** Un seul outil ouvert randomise réellement pour un individu : « StudyU is the only
available fully‑functional platform for personalized N‑of‑1 treatment advice. » et « N-of-1 trials
enable participants to discover the individual effects of interventions on their health. »
(https://www.studyu.health/, ouverte le 13/08/2026 — *les traits d'union de « fully‑functional » et
« N‑of‑1 » sont des U+2011 dans la page*). Son application compagne montre qu'un non-expert peut y
arriver : « Although several tools for N-of-1 trials exist, there is a gap in supporting non-experts
in conducting their own user-centric trials. » et « A final empirical evaluation of StudyMe showed
that all participants were able to create their own trials successfully using StudyMe »
[Zenner, 2022, DOI:10.1186/s13063-022-06893-7]. **Mais l'outil est un formulaire, pas un
interlocuteur.**

Le produit grand public qui emploie le plus complètement le vocabulaire de l'essai ne randomise pas :
« Experiments is a new Oura feature that can help you experiment with your habits so you can discover
how they impact your body. » ; « Each experiment lasts for a limited time period (ex: 14 days) and
focuses on one daily habit. » ; « A hypothesis is a prediction about the expected effect of the
intervention on the outcome variable. » ; « It’s your own n=1 research trial. »
(https://ouraring.com/blog/oura-experiments/, ouverte le 13/08/2026, page datée du 01/09/2023).
**Aucune mention d'alternance, de tirage au sort, de sevrage ni de bras témoin : c'est un
avant/après.** Ailleurs, le mot « randomisé » désigne la validation du produit sur une population,
pas un test sur l'utilisateur : « We put our reputation to the test in a randomised controlled trial,
the gold standard of research. » (https://zoe.com/, ouverte le 13/08/2026), et la promesse de la
dimension est vendue sans dispositif : « Nutrition advice is generic. Your body isn't. »
(https://www.levelshealth.com/, ouverte le 13/08/2026).

Les deux produits les plus proches d'un coach d'endurance n'emploient **jamais** le vocabulaire de
l'expérimentation : « Adaptive training plans that adjust to your fitness, fatigue, and schedule, so
you improve with confidence. » (https://www.athletica.ai/, ouverte le 13/08/2026), et « TrainerRoad
AI runs hundreds of simulations to find the right workout to make you faster. »
(https://www.trainerroad.com/adaptive-training/, ouverte le 13/08/2026). **Ils adaptent et simulent —
c'est-à-dire qu'ils prédisent la réponse au lieu de la tester.** Le seul protocole de capitalisation
trouvé est social et sans outillage : « Since 2008, people have been sharing their knowledge with
peers by explaining: What did I do? How did I do it? What did I learn? »
(https://quantifiedself.com/, ouverte le 13/08/2026), et la mutualisation sans moyennage existe à
l'échelle associative — « This is an opportunity to try self-research for the first time »
(https://www.openhumans.org/, ouverte le 13/08/2026).

**Constats pour l'É3 — les trous.** (1) **Aucun agent conversationnel ne conduit un essai N-of-1 de
bout en bout** : les deux moitiés existent séparément — un article de position propose l'architecture
sans système, l'agent de santé le plus complet n'a aucun sous-agent expérimentateur, et les
plateformes qui randomisent vraiment le font par formulaire. (2) **La micro-randomisation n'est
jamais évaluée sur le vécu qu'elle abîme** : la littérature 2025-2026 optimise le regret, la
puissance et l'erreur de type I ; la tension entre validité scientifique et expérience vécue est
nommée depuis 2017 et **personne ne l'a mesurée depuis**. (3) **La non-réponse comme signal de pivot
n'existe dans aucun système** : la physiologie a la doctrine complète (augmenter la dose avant de
conclure, seuil calé sur l'erreur de mesure, bras comparateur répété obligatoire), les agents de
santé personnels n'ont aucune notion de non-répondeur. (4) **Aucun produit grand public ne
randomise**, y compris ceux qui vendent le mot « expérience » — et **personne n'expose de période de
sevrage à un utilisateur**. (5) **Le passage de la conclusion causale à la règle personnelle écrite
n'est traité nulle part** : le besoin est identifié depuis 2013, les normes existent pour le rapport
scientifique, et le maillon « conclusion → règle datée, révisable » est vide. (6) **Mutualiser sans
moyenner a sa théorie depuis 1997 et aucun produit** : aucune page ouverte ne dit « voici ce que
d'autres comme toi ont appris, et voici de combien j'ajuste ma conclusion sur toi ». *Trous de
collecte déclarés* : une page produit majeure sur les corrélations comportement/récupération n'est
qu'une coquille d'application monopage et n'a pas pu être citée ; onze préprints repérés n'ont pas
été ouverts faute de budget d'appels ; une revue critique sur la réponse individuelle du VO2max
n'est servie par aucune API.

## FICHE SYNTHÈSE

**D45 — Expérimentation N-of-1** (capacité). Le compagnon transforme une intuition de l'utilisateur
en épreuve : hypothèse formulée à partir de ce qu'il a dit, protocole personnel annoncé d'avance
(durée, mesure, comparaison, **période de sevrage**), randomisation qui ne porte que sur ce qui lui
est indifférent, conclusion honnête — **y compris « je ne peux pas conclure »** —, vérification de la
dose avant tout verdict de non-réponse, et transformation du résultat en **règle personnelle datée et
révisable**. Il apprend des autres sans diluer l'individu dans la moyenne.
**Références clés** : [Fisher, 2018, DOI:10.1073/pnas.1711978115] (la variance intra-individuelle est
**deux à quatre fois** supérieure à la variance intergroupe : la moyenne des autres ne décrit pas une
personne) ; [Atkinson, 2015, DOI:10.1113/EP085070] (sans bras comparateur répété, une « réponse
individuelle » n'est pas démontrable — c'est du bruit) ;
[Montero, 2017, DOI:10.1113/JP273480] (78 adultes : la non-réponse tombe à 0 % quand la dose
augmente — **un non-répondeur est d'abord un sous-dosé**).
**Déclinaisons touchées** : D49 (la plus servie — allure, horaire, sommeil, nutrition de course),
D50 (micro-expériences du quotidien), D51 (façons de travailler), D52 (activation comportementale,
renvoi D00 le plus strict), D53 (méthodes d'apprentissage), D54 (**savoir ne pas s'appliquer** — on
ne met pas une relation en protocole), D55 (formats de restitution).
**Renvois** : D34 (le timing de la relance — ici c'est le dispositif), D42 (le changement une fois
qu'on sait quoi faire), D01 (la règle personnelle écrite et sa révision), D12 (annoncer son
incertitude et refuser de conclure), D48 (mesurer la relation, pas l'effet d'une intervention),
**D00** (consentement éclairé, droit d'arrêter, sujets à risque).
