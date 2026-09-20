# D53 — Déclinaison : tuteur

> **Fiche VISION** (gabarit plan §4). Type : **déclinaison**. Lot 8 — session 16, 13/08/2026.
> Statut : `rédigée` (gate É2bis à venir).
> **Aucun verdict de faisabilité ici** (règle plan §3).
> **Dérogation de gabarit — [AJOUT VALIDATION 13/08] validée par Sébastien en session** : comme D49
> et D52, le §4 devient **« Ce que le socle rend possible ici »** (déclaration complète et trace de
> la validation en tête de D49). Aucun autre écart au gabarit.
> **Convention de citation** : format §2 `[Auteur, année, arXiv:… ou DOI:…]` — sources ouvertes en
> session (Crossref, Semantic Scholar par DOI, PubMed E-utilities par DOI vérifié, OpenAlex,
> Europe PMC, ERIC, API arXiv, HTML brut Springer et Nature). *Dérogation déclarée* : les pages
> produit sont citées en clair avec leur URL et la date d'ouverture.
> **AVERTISSEMENT D'HONNÊTETÉ, À LIRE AVANT TOUT CONTRÔLE** : le chiffre « 2 sigma » **n'est servi
> par aucune API** pour `[Bloom, 1984, DOI:10.3102/0013189X013006004]` — il n'est attesté que par le
> titre de l'article. **Aucun chiffre n'est accroché à cette source dans la fiche** ; la valeur de
> d = 2,0 n'apparaît ici que comme *croyance rapportée et infirmée* par VanLehn.
> **Abstracts servis uniquement par l'index inversé d'OpenAlex — restitués SANS guillemets** :
> Bloom 1984, VanLehn 2011, Kluger 1996, Pekrun 2010.
> **Sources citées pour le cadre seulement** (aucune API ne sert leur abstract) : Corbett 1995,
> Wood 1976, Kalyuga 2003.
> **Verbatims provenant d'une voie non-API, déclarés comme tels** : Bisra 2018 et Chase 2009 sont
> servis par le **HTML brut de `link.springer.com`** (vides chez Crossref, S2, OpenAlex et Europe
> PMC) ; les chiffres de population de Kestin 2025 viennent du **texte intégral** sur `nature.com`,
> **pas de l'abstract**, qui n'en donne aucun.
> **FAIT À CONNAÎTRE — une correction existe** : PNAS a publié une correction à
> `[Bastani, 2025, DOI:10.1073/pnas.2422633122]` (`DOI:10.1073/pnas.2518204122`, existence vérifiée
> sur trois API, **contenu servi par aucune**). La fiche cite les chiffres de l'abstract d'origine
> et **n'affirme pas** qu'ils sont post-correction.
> **SOURCE RÉTRACTÉE, À NE PAS RÉINTRODUIRE** : la méta-analyse de Wang & Fan sur l'effet de ChatGPT
> (`DOI:10.1057/s41599-025-04787-y`) est **rétractée** (note de rétractation
> `DOI:10.1057/s41599-026-07310-z`). Elle n'est citée nulle part ici, ni directement ni via une
> source secondaire — son absence n'est pas un oubli.
> **Essai réel non citable au format** : l'essai randomisé LearnLM/Eedi (`arXiv:2512.23633`,
> N = 165 élèves, cinq établissements britanniques) est **écarté mécaniquement** — le premier auteur
> rendu est « LearnLM Team », un consortium inapariable. Substitut cité :
> `[Jurenka, 2024, arXiv:2407.12687]`. C'est une perte assumée, pas un oubli.
> **Deux « Kulik », deux personnes différentes** : `[Kulik, 2016, DOI:10.3102/0034654315581420]` est
> James A. Kulik ; `[Kulik, 1990, DOI:10.3102/00346543060002265]` est Chen-Lin C. Kulik — tous deux
> co-auteurs de `[Cohen, 1982, DOI:10.3102/00028312019002237]`.
> **Deux « Liu, 2026 », deux personnes** : `DOI:10.1111/iej.70222` est Wenjing Liu ;
> `arXiv:2602.02457` est Naiming Liu. **Deux « Zhao »** : `arXiv:2508.03275` est Jiahao Zhao,
> `arXiv:2604.18660` est Jin Zhao. **Deux « Macina », même personne**, deux travaux.
> **Wang** est ici Rose E. Wang (`arXiv:2410.03017`) — nom très fréquent dans le CDC.
> **Dédup inter-fiches attendue** : `[Wood, 1976, DOI:10.1111/j.1469-7610.1976.tb00381.x]` et
> `[Kosmyna, 2025, arXiv:2506.08872]` sont déjà cités en D41 ;
> `[Macina, 2025, arXiv:2502.18940]` est déjà cité en D39.
> **Années = celles rendues par l'API** : Corbett citée **1995** (Crossref ; S2 rend 2005, l'usage
> dit 1994 — écart de onze ans entre deux API sur le même DOI), Nickow citée **2023** (`issued`
> Crossref ; l'impression est de 2024), Norris citée **2025** (dépôt arXiv de novembre 2025 ; mise à
> jour en 2026), Cohn citée **2025** (dépôt arXiv ; parution AAAI 2026).

## 1. Définition et périmètre

Un professeur particulier **à vie**. Pas un chatbot qui explique bien : quelqu'un qui sait
exactement ce que cette personne sait, qui propose toujours le problème d'un cran au-dessus, qui
fait réviser sans que ça ressemble à une révision, et qui tient ce fil pendant vingt ans, sur tout
ce que l'utilisateur apprend — la statistique, l'espagnol, la physiologie de l'endurance.

Features propres à cette déclinaison :

| Feature | Ce que ça veut dire |
|---|---|
| **Modèle de l'apprenant** | Suivi de connaissances, conceptions erronées, profil cognitif, historique cumulé **à vie**. |
| **Défi à la bonne hauteur** | Zone proximale de développement, étayage dégressif, apprentissage par maîtrise, rôles inversés. |
| **Répétition espacée personnalisée** | Courbe d'oubli **par notion**, et **révision invisible** glissée dans la conversation. |
| **Feedback socratique immédiat** | Faire produire plutôt que donner — et savoir se taire. |
| **Métacognition** | Apprendre à apprendre, et transférer ça au reste de la vie. |
| **Lecture de l'état** | Confusion, ennui, flow — en temps réel, dans le dialogue. |
| **Courbe de progression pilotée** | Prédiction d'échéance, détection des plateaux. |
| **Tuteur de vie entière** | Curriculum trans-domaines ancré dans le vécu, leçons saisies dans le quotidien, orchestration avec les enseignants humains. |

**Exclusions** : la mémoire du compagnon lui-même est en D01, la proactivité en D34, le moteur du
changement en D42, l'aide orientée-autonomie en D41. **Renvoi D00** : un tuteur qui donne la réponse
pour plaire fabrique exactement la dépendance que la vision interdit.

## 2. Mécanisme humain

**La promesse fondatrice est célèbre — et la fiche ne lui accroche aucun chiffre.** L'article qui a
donné son nom au problème compare classe conventionnelle, apprentissage par maîtrise et tutorat
individuel [Bloom, 1984, DOI:10.3102/0013189X013006004] — *contenu restitué par l'index inversé
d'OpenAlex, sans guillemets ; le « 2 sigma » n'est servi par aucune API et n'est attesté que par le
titre*. Deux ans plus tôt, une méta-analyse de 65 évaluations donnait déjà un tableau plus sobre :
« A meta-analysis of findings from 65 independent evaluations of school tutoring programs showed
that these programs have positive effects on the academic performance and attitudes of those who
receive tutoring. », avec un effet symétrique — « The meta-analysis also showed that tutoring
programs have positive effects on children who serve as tutors. »
[Cohen, 1982, DOI:10.3102/00028312019002237].

**Et la revue qui fait autorité démonte la légende de l'écart humain/machine.** Elle rapporte la
croyance répandue — d ≈ 0,3 pour les systèmes qui ne réagissent qu'à la réponse finale, d ≈ 1,0 pour
les systèmes tutoriels intelligents, d ≈ 2,0 pour un tuteur humain adulte — et **ne la confirme
pas** : elle mesure **d = 0,79 pour le tutorat humain et d = 0,76 pour les systèmes tutoriels
intelligents** [VanLehn, 2011, DOI:10.1080/00461520.2011.611369] — *OpenAlex, sans guillemets*.
**L'écart entre un humain et une machine dans le tutorat était déjà très faible avant les LLM.** Le
chiffre du tutorat réel, enfin, est celui-ci : « We find that tutoring programs yield consistently
substantial positive impacts on learning, with an overall pooled ES of 0.288 SD (SE = 0.029, p <
.001). », les effets étant les plus forts « for programs that use teachers or paraprofessionals as
tutors, are held in earlier grades, occur at least 3 days per week »
[Nickow, 2023, DOI:10.3102/00028312231208687]. Côté machine : « The median effect of intelligent
tutoring in the 50 evaluations was to raise test scores 0.66 standard deviations over conventional
levels, or from the 50th to the 75th percentile. », avec un avertissement qui vaut mot pour mot pour
2026 — l'ampleur mesurée « depended to a great extent on whether improvement was measured on locally
developed or standardized tests » [Kulik, 2016, DOI:10.3102/0034654315581420].

**L'apprentissage par maîtrise marche, et il a un défaut que le compagnon héritera.** « The effects
appear to be stronger on the weaker students in a class », mais « In addition, self-paced mastery
programs often reduce the completion rates in college classes. »
[Kulik, 1990, DOI:10.3102/00346543060002265]. **Un tuteur qui n'impose aucune échéance perd des
gens.** Le modèle de l'apprenant a sa source-origine [Corbett, 1995, DOI:10.1007/BF01099821] ;
l'étayage et son retrait progressif viennent de [Wood, 1976, DOI:10.1111/j.1469-7610.1976.tb00381.x] ;
et la raison pour laquelle le niveau du défi n'est pas négociable est l'effet d'inversion de
l'expertise — l'aide qui soutient un novice **dégrade** la performance de celui qui a progressé
[Kalyuga, 2003, DOI:10.1207/S15326985EP3801_4].

**La répétition espacée a sa base quantitative — et un résultat que la plupart des produits
ignorent.** « This review found 839 assessments of distributed practice in 317 experiments located
in 184 articles. », et surtout : « Analyses suggest that ISI and retention interval operate jointly
to affect final-test retention; specifically, the ISI producing maximal retention increased as
retention interval increased. » [Cepeda, 2006, DOI:10.1037/0033-2909.132.3.354]. **L'intervalle
optimal dépend de l'horizon auquel on veut se souvenir** : un tuteur qui vise « des décennies » ne
peut pas espacer comme un tuteur qui vise l'examen de vendredi. Le mécanisme qui rend la révision
efficace est l'effort de rappel : « Key results indicate support for the role of effortful
processing as a contributor to the testing effect, with initial recall tests yielding larger testing
benefits than recognition tests. » [Rowland, 2014, DOI:10.1037/a0037559] — **il faut faire produire,
pas faire reconnaître**. Et la courbe d'oubli elle-même, répliquée, l'a été sur un seul sujet :
« One subject spent 70 hours learning lists and relearning them after 20 min, 1 hour, 9 hours,
1 day, 2 days, or 31 days. » [Murre, 2015, DOI:10.1371/journal.pone.0120644]. *Il n'existe pas de
courbe d'oubli par notion et par personne validée à grande échelle.*

**Le résultat qui gouverne toute la conception d'un tuteur relationnel est celui-ci** : « improvements
in performance can fail to yield significant learning », et « people often mistakenly interpret their
performance during acquisition as a reliable guide to long-term learning. »
[Soderstrom, 2015, DOI:10.1177/1745691615569000]. **L'apprenant préférera le tuteur qui le fait se
sentir compétent, pas celui qui le fait apprendre.** Pour un compagnon qui tient aussi à la relation,
c'est une tension structurelle.

**Et le feedback, l'outil le plus évident du tuteur, nuit une fois sur trois.** La méta-analyse de
référence porte sur 607 tailles d'effet et 23 663 observations : les interventions de feedback
améliorent la performance en moyenne, **mais plus d'un tiers d'entre elles la dégradent**, et
l'efficacité décroît à mesure que l'attention remonte vers le **soi** et s'éloigne de la **tâche**
[Kluger, 1996, DOI:10.1037/0033-2909.119.2.254] — *OpenAlex, sans guillemets*. **Un compagnon qui
donne du feedback en permanence et qui le personnalise — donc qui l'oriente vers la personne — tombe
exactement dans le mécanisme décrit.** Le pendant conception est connu : « Feedback is one of the
most powerful influences on learning and achievement, but this impact can be either positive or
negative. » [Hattie, 2007, DOI:10.3102/003465430298487].

**Faire expliquer bat expliquer.** « Without any extensive training, 14 eighth-grade students were
merely asked to self-explain after reading each line of a passage on the human circulatory
system. », avec ce résultat : « High explainers all achieved the correct mental model of the
circulatory system, whereas many of the unprompted students as well as the low explainers did not. »
[Chi, 1994, DOI:10.1207/s15516709cog1803_3] — *24 collégiens américains sur un texte de biologie*.
La méta-analyse chiffre l'effet — « The overall weighted mean effect size using a random effects
model was g = .55. » — et sa dernière phrase appelle littéralement le tuteur génératif : « Due to
the limitations of relying on instructor-scripted prompts, we recommend that future research explore
computer-generation of self-explanation prompts. » [Bisra, 2018, DOI:10.1007/s10648-018-9434-x]
— *verbatims servis par le HTML brut de Springer, aucune API ne les rend*. Enfin, enseigner fait
apprendre : « Two studies demonstrate the protégé effect: students make greater effort to learn for
their TAs than they do for themselves. », et « These beneficial effects were most pronounced for
lower achieving children. » [Chase, 2009, DOI:10.1007/s10956-009-9180-4] — *idem, HTML Springer*.

**Deux bornes pour finir.** L'ennui n'est pas un détail d'ergonomie : le contrôle et la valeur
perçus le prédisent négativement, et il est associé négativement à la motivation intrinsèque, à
l'effort et à la performance ultérieure [Pekrun, 2010, DOI:10.1037/a0019243] — *OpenAlex, sans
guillemets*. Et le transfert lointain, que la promesse « métacognition transférée à toute la vie »
suppose, reste un mur : « Despite a century's worth of research, arguments surrounding the question
of whether far transfer occurs have made little progress toward resolution. », et « Estimation of a
single effect size for far transfer is misguided in view of this complexity. »
[Barnett, 2002, DOI:10.1037/0033-2909.128.4.612]. **Ce qui tient, en revanche, c'est la
métacognition enseignée** : « The instruction effect at posttest increased from Hedges' g = 0.50 to
0.63 at follow-up test. », avec « low SES students benefited the most at long-term. »
[de Boer, 2018, DOI:10.1016/j.edurev.2018.03.002]. Quant aux techniques d'étude à induire : « Practice
testing and distributed practice received high utility assessments », tandis que « Five techniques
received a low utility assessment: summarization, highlighting, the keyword mnemonic, imagery use
for text learning, and rereading. » [Dunlosky, 2013, DOI:10.1177/1529100612453266].

## 3. Comportement attendu de l'IA

**Ce que ferait Samantha.** Elle ne fait pas de cours. Elle glisse, au milieu d'une conversation sur
autre chose : « au fait, l'histoire du seuil lactique dont tu m'as parlé le mois dernier — tu me le
réexpliques ? » Et c'est une révision.

**Scénario A — la révision invisible.** Trois semaines après avoir appris quelque chose, au moment
où la courbe d'oubli le dit, le compagnon **ramène la notion dans une conversation ordinaire**, sous
forme de question qui a l'air d'être une vraie question. L'utilisateur ne sait pas qu'il révise.

**Scénario B — le défi d'un cran au-dessus.** Le problème proposé est toujours juste au-dessus de ce
que l'utilisateur sait faire seul — jamais deux crans, jamais zéro. Et **l'aide diminue à mesure que
la compétence monte**, y compris quand l'utilisateur ne le demande pas.

**Scénario C — le silence.** L'utilisateur bloque. Le compagnon **ne dit rien** pendant que ça
travaille, puis pose une question, pas la réponse. **C'est le geste le plus difficile de toute la
déclinaison.**

**Scénario D — la demande de réponse.** « Donne-moi juste la solution, j'ai pas le temps. » Le
compagnon peut céder — mais il le dit, il note ce qui n'a pas été appris, et il y revient plus tard.
Il ne se laisse pas manœuvrer sans en garder trace.

**Scénario E — l'ennui et la confusion distingués.** L'utilisateur décroche. Le compagnon sait si
c'est parce que c'est trop facile ou parce que c'est trop dur, et il change de levier en
conséquence — pas de ton.

**Scénario F — la leçon saisie dans le quotidien.** L'utilisateur raconte un problème de travail. Le
compagnon y voit l'occasion d'ancrer une notion de statistique apprise l'an dernier, et fait le lien.
**Le curriculum n'a pas de matière : il a une vie.**

**Scénario G — l'orchestration avec des humains.** L'utilisateur suit aussi un cours. Le compagnon
sait ce que le professeur humain a fait, ne le contredit pas, et **s'efface là où l'humain fait mieux**.

**Ce que l'utilisateur doit ressentir** : qu'il **devient meilleur**, sans avoir jamais eu
l'impression de réviser.

**Critères d'expérience observables** :
- l'utilisateur retrouve, un an après, une notion qu'il n'a jamais consciemment révisée ;
- le compagnon refuse de donner la réponse au moins aussi souvent qu'il la donne, et sait dire
  pourquoi ;
- il se tait pendant que l'utilisateur cherche ;
- il sait dire ce que l'utilisateur savait il y a six mois et ne sait plus ;
- il ne félicite pas une performance qui n'est pas un apprentissage ;
- **contrôle négatif (D00)** : aucun mécanisme d'assiduité, aucune série à préserver, et aucune
  flatterie qui remplace le progrès.

## 4. Ce que le socle rend possible ici

*(Adaptation du §4 pour une fiche de déclinaison — voir D49.)*

- **D01 — mémoire** : le modèle de l'apprenant **est** un cas particulier de la mémoire du
  compagnon. Sans mémoire à vie, il n'y a pas de tuteur à vie.
- **D03 — modèle de l'utilisateur** : le profil cognitif et les conceptions erronées récurrentes.
- **D04 — état émotionnel** : distinguer confusion, ennui et découragement en direct.
- **D09 / D11 — responsiveness et aide juste** : le dosage entre expliquer, questionner et se taire.
- **D14 — franchise** : dire « tu ne l'as pas compris » quand c'est vrai.
- **D34 — proactivité** : la répétition espacée **est** une proactivité, calibrée sur une courbe.
- **D41 — autonomie** : l'aide orientée-autonomie de Nadler est ici la spécification centrale.
- **D42 — moteur du changement** : la régularité d'étude est une habitude, et la reprise après trois
  semaines d'abandon est ce qui distingue un tuteur d'une application de révision.
- **D45 — expérimentation N-of-1** : tester sur soi les méthodes d'étude qui marchent.
- **D20 — sens** : apprendre s'inscrit dans un projet, pas dans un programme.

## 5. État de l'art descriptif

*(Descriptif : qui fait quoi, mesuré comment. Aucun jugement de faisabilité.)*

**Les deux résultats de référence pointent dans des directions opposées.** Le positif : « We find
that students learn significantly more in less time when using the AI tutor, compared with the
in-class active learning. » [Kestin, 2025, DOI:10.1038/s41598-025-97652-6] — *l'abstract ne donne
aucun effectif ; le texte intégral situe l'essai dans un cours d'introduction à la physique d'une
université d'élite, N = 194, sur **une seule leçon***. Le négatif : « having GPT-4 access while
solving problems significantly improves performance (48% improvement in grades for GPT Base and 127%
for GPT Tutor). » **mais** « when access is subsequently taken away, students actually perform worse
than those who never had access (17% reduction in grades for GPT Base) », parce que « Without
guardrails, students attempt to use GPT-4 as a "crutch" during practice problem sessions, and
subsequently perform worse on their own. » [Bastani, 2025, DOI:10.1073/pnas.2422633122] — *près
d'un millier de lycéens ; une correction PNAS existe, dont le contenu n'est servi par aucune API*.
**Le contraste entre l'accès brut et le mode tuteur est exactement l'argument de cette
déclinaison.** Et l'essai randomisé le plus récent trouve une **équivalence** : « No statistically
significant between-group difference was detected in post-training total scores », le gain réel
étant le temps enseignant — « the AI-guided intervention required substantially less direct
synchronous faculty teaching time per student than CBL (0.026 vs. 0.45 h). »
[Liu, 2026, DOI:10.1111/iej.70222] — *79 étudiants, intervention d'une heure, monocentrique*.

**Le plus grand essai en conditions réelles porte sur l'humain assisté, pas sur l'IA seule.** « This
study is the first randomized controlled trial of a Human-AI system in live tutoring, involving 900
tutors and 1,800 K-12 students from historically under-served communities. » ; « students working
with tutors that have access to Tutor CoPilot are 4 percentage points (p.p.) more likely to master
topics (p<0.01). Notably, students of lower-rated tutors experienced the greatest benefit, improving
mastery by 9 p.p. » ; et la mesure comportementale qui compte pour D53 : les tuteurs assistés « are
more likely to use high-quality strategies to foster student understanding (e.g., asking guiding
questions) and less likely to give away the answer to the student. »
[Wang, 2024, arXiv:2410.03017] — préprint. Le dosage humain/IA n'est d'ailleurs pas le même selon le
niveau : « lower-performing students derive greater benefit from human-AI tutoring than
higher-performing students », avec « 25% increase in time on task, 36% in skill proficiency, and 61%
in academic growth » [Gurung, 2026, arXiv:2605.11155] — préprint, quasi-expérience sur 635 élèves.

**Le modèle de l'apprenant a franchi trois générations, et bute sur le premier jour.** Après le
suivi bayésien puis le suivi profond — les réseaux récurrents « do not require the explicit encoding
of human domain knowledge, and can capture more complex representations of student knowledge »
[Piech, 2015, arXiv:1506.05908] —, le suivi par LLM exploite enfin le texte des questions et
« generalises much better to cold-start questions and users »
[Norris, 2025, arXiv:2511.02599] — préprint. **Le démarrage à froid, c'est exactement le premier jour
du compagnon avec son utilisateur.** Une architecture unifiée existe, et son abstract avoue le
problème de fond : « Recent studies have explored Large Language Models (LLMs) for KT via
autoregressive nature, but such approaches typically require fine-tuning and exhibit unstable or
near-random performance. » [Lee, 2026, arXiv:2601.01708] — préprint.

**La brique centrale de D53 existe en préprint, et une seule fois.** « By incorporating a continuous
forgetting curve with knowledge tracing, TASA dynamically updates each student's mastery state and
generates contextually appropriate, difficulty-calibrated questions and explanations. »
[Wu, 2025, arXiv:2511.15163] — préprint, évaluation en simulation. La répétition espacée pilotée par
LLM, elle, est évaluée sur **des apprenants simulés** : « LECTOR achieves a 90.2% success rate
compared to 88.4% for the best baseline (SSP-MMC), representing a 2.0% relative improvement. »
[Zhao, 2025, arXiv:2508.03275] — préprint, *100 apprenants simulés sur 100 jours, aucun humain*.
Et la zone proximale de développement est explicitement opérationnalisée dans un agent : le cadre
« combines Evidence-Centered Design with Social Cognitive Theory and Zone of Proximal Development for
adaptive scaffolding in LLM-based agents », les auteurs constatant que « current LLM systems used in
classrooms often lack the solid theoretical foundations found in earlier intelligent tutoring
systems. » [Cohn, 2025, arXiv:2508.01503].

**Le résultat le plus tranchant de la dimension porte sur le silence.** Un banc de tutorat
métacognitif annote 1 015 conversations et 7 711 tours, et mesure : « The best model achieves only
43.2% accuracy, and models exhibit compulsive intervention bias: in turns where effective
metacognitive tutoring requires silent (41.7% of cases), models predict `no intervention' only 4.2%
of the time, while severely over-predicting high-intervention moves. »
[Liu, 2026, arXiv:2602.02457] — préprint. **Là où un bon tuteur doit se taire dans 41,7 % des tours,
les modèles choisissent le silence 4,2 % du temps.** C'est, chiffré, le scénario C de cette fiche.

**Les bancs d'évaluation disent tous la même chose : savoir n'est pas enseigner.** « none of the
frontier LLMs achieve a score of greater than 56%, showing a large room for improvement. », sur trois
tâches — explications adaptées à la confusion, retour actionnable, indices qui font travailler
[Srinivasa, 2025, arXiv:2510.02663] — préprint, 1 490 échantillons rédigés par des experts.
« subject expertise, indicated by solving ability, does not immediately translate to good
teaching. », et « tutoring appears to become more challenging in longer dialogs, where simpler
questioning strategies begin to fail. » [Macina, 2025, arXiv:2502.18940] — préprint, déjà cité en
D39 ; **la dégradation en dialogue long est le problème central d'un tuteur « à vie »**. Le défaut
de base était déjà nommé en 2023 : les modèles « fail at tutoring because they generate factually
incorrect feedback or are prone to revealing solutions to students too early. »
[Macina, 2023, arXiv:2305.14536] — préprint. Une taxonomie d'évaluation pédagogique de référence
existe désormais, avec « 192 conversations and 1,596 responses from seven state-of-the-art LLM-based
and human tutors » et huit dimensions annotées [Maurya, 2025, arXiv:2412.09416].

**Et un angle que personne d'autre ne couvre : l'utilisateur qui manœuvre son tuteur.** « Prior work
evaluates pedagogical quality via answer leakage-the disclosure of complete solutions instead of
scaffolding-but typically assumes well-intentioned learners, leaving tutor robustness under student
misuse largely unexplored. », d'où l'adaptation de « six groups of adversarial and persuasive
techniques to the educational setting » [Zhao, 2026, arXiv:2604.18660] — préprint. **Pour un
compagnon qui a une alliance affective avec son utilisateur, c'est le point de rupture** : il a
toutes les raisons de céder. Le risque symétrique — la dette cognitive — est documenté ailleurs :
« Over four months, LLM users consistently underperformed at neural, linguistic, and behavioral
levels. » [Kosmyna, 2025, arXiv:2506.08872] — préprint, 54 participants, tâche de rédaction, déjà
cité en D41. Enfin, la doctrine d'évaluation d'un modèle pédagogique dédié est posée par
[Jurenka, 2024, arXiv:2407.12687] — préprint : « LearnLM-Tutor is consistently preferred over a
prompt tuned Gemini by educators and learners on a number of pedagogical dimensions. »

**Produits.** Les trois assistants généralistes revendiquent le socratique et **aucun ne publie de
mesure d'apprentissage**. Le premier assume même la fragilité de son mécanisme : « Under the hood,
study mode is powered by custom system instructions we've written in collaboration with teachers,
scientists, and pedagogy experts », et « We chose this approach because it lets us quickly learn from
real student feedback and improve the experience—even if it results in some inconsistent behavior and
mistakes across conversations. » (https://openai.com/index/chatgpt-study-mode/, ouverte le
13/08/2026, page datée du 29/07/2025). Le deuxième décrit le geste : « Guiding rather than answering:
Asking "How would you approach this problem?" instead of providing immediate solutions »
(https://www.anthropic.com/news/introducing-claude-for-education, ouverte le 13/08/2026, page datée
du 02/04/2025). Le troisième affirme frontalement le contraire des deux premiers : « we found that
simply improving prompting wasn't enough to create a meaningful learning tool. », d'où un modèle
affiné — « we developed LearnLM , a family of models fine-tuned for learning and grounded in
educational research. » (https://blog.google/outreach-initiatives/education/guided-learning/, ouverte
le 13/08/2026).

Côté produits d'éducation, la revendication de D53 a trente ans. Un tuteur grand public promet :
« Khanmigo challenges you to think critically and solve problems without giving you direct
answers. » (https://www.khanmigo.ai/, ouverte le 13/08/2026). Un système de maîtrise en production
depuis vingt-six ans revendique le modèle de l'apprenant : « ALEKS always knows what each student is
ready to learn. » et « ALEKS artificial intelligence is developed using billions of data points from
student interactions accumulated over 26 years » (https://www.aleks.com/about_aleks/overview,
ouverte le 13/08/2026) — **strictement par matière et par item, jamais transversal ni à vie**.
L'héritier des tuteurs cognitifs reprend le vocabulaire tel quel : « The 1-to-1 math coach that makes
your life easier. » (https://www.carnegielearning.com/solutions/math/mathia/, ouverte le 13/08/2026).
Et le registre affectif est vendu explicitement : « Warm, patient, encouraging. The Tutor adapts to
your child, so you never have to worry about them falling behind. » (https://www.synthesis.com/tutor,
ouverte le 13/08/2026 — *la même page affiche deux chiffres d'audience contradictoires*).

**La courbe d'oubli par notion, elle, existe en production — et elle est entièrement visible.** « The
Free Spaced Repetition Scheduler (FSRS) is an alternative to Anki's legacy SuperMemo 2 (SM-2)
algorithm. By more accurately determining how much information you are likely to forget, it can help
you remember more material in the same amount of time. »
(https://docs.ankiweb.net/deck-options.html, ouverte le 13/08/2026). **C'est l'exact opposé de la
révision invisible : un outil de cartes, où l'utilisateur voit chaque échéance.** À l'échelle
industrielle, la personnalisation de l'espacement n'existe que sur du vocabulaire
(https://research.duolingo.com/, ouverte le 13/08/2026), et la pratique répétée jusqu'à
l'automatisation n'est vendue que pour les langues : « You speak the same patterns in new situations,
again and again. Not just memorizing them, but making them automatic. » (https://www.speak.com/,
ouverte le 13/08/2026).

**Constats pour l'É3 — les trous.** (1) **La révision invisible glissée dans la conversation
n'existe nulle part** : tout ce qui est publié ou vendu ordonnance des **items explicites** — cartes,
exercices, questions calibrées ; aucune étude, aucun banc, aucun produit ne dissimule la révision
dans un dialogue ordinaire **en mesurant la rétention**. C'est le trou le plus net, et il est au cœur
de la définition figée de la dimension. (2) **Le tuteur de vie entière n'a aucune mesure** : la durée
maximale documentée d'un tuteur LLM est de l'ordre du semestre, l'essai positif de référence porte
sur **une leçon**, l'essai randomisé le plus récent sur **une heure** ; « faire durer les savoirs des
décennies » n'a aucun antécédent empirique. (3) **Le modèle de l'apprenant trans-domaines n'existe
pas** : le système le plus abouti en production est cloisonné par matière. (4) **Le résultat « le
feedback nuit une fois sur trois » n'a jamais été testé sur un tuteur LLM personnalisé**, alors que
la personnalisation oriente précisément l'attention vers le soi — le mécanisme incriminé.
(5) **Aucun banc ne mesure la dégradation pédagogique en dialogue très long**, alors que le seul
travail qui l'aborde constate qu'elle existe. *Trous de collecte déclarés* : l'essai randomisé
britannique le plus proche du sujet n'est **pas citable au format** (premier auteur consortium) et
n'a donc pas pu être exploité ; le contenu de la correction PNAS n'est servi par aucune API ; la page
« mastery learning » d'un éditeur majeur est protégée par un dispositif anti-robots ; et la page
« comment nous utilisons l'IA » d'un autre n'a pas pu être obtenue en anglais.

## FICHE SYNTHÈSE

**D53 — Déclinaison : tuteur** (déclinaison). Un professeur particulier à vie : il tient un modèle de
l'apprenant qui survit aux années et traverse les domaines, propose toujours le défi d'un cran
au-dessus en retirant l'aide à mesure, **glisse la révision dans la conversation** au moment que dit
la courbe d'oubli, fait produire plutôt qu'il n'explique, **sait se taire**, distingue l'ennui de la
confusion, et s'efface là où un enseignant humain fait mieux.
**Références clés** : [VanLehn, 2011, DOI:10.1080/00461520.2011.611369] (la croyance donne d = 2,0
au tuteur humain ; la revue mesure **0,79 pour l'humain et 0,76 pour la machine** — l'écart était
déjà minime avant les LLM) ; [Kluger, 1996, DOI:10.1037/0033-2909.119.2.254] (607 tailles d'effet :
le feedback **dégrade** la performance dans plus d'un tiers des cas, d'autant plus qu'il vise le soi
plutôt que la tâche) ; [Liu, 2026, arXiv:2602.02457] (là où un bon tuteur métacognitif doit se taire
dans **41,7 %** des tours, les modèles choisissent le silence **4,2 %** du temps — « compulsive
intervention bias »).
**Capacités mobilisées** : D01 (le modèle de l'apprenant est un cas de la mémoire), D03 (profil
cognitif et conceptions erronées), D04 (confusion, ennui, flow), D09/D11 (expliquer, questionner ou
se taire), D14 (dire « tu ne l'as pas compris »), D34 (la répétition espacée est une proactivité),
D41 (aide orientée-autonomie), D42 (la régularité d'étude et la reprise sans dette), D45 (tester ses
propres méthodes), D20 (apprendre dans un projet).
**Renvois** : **D00** (un tuteur qui donne la réponse pour plaire fabrique la dépendance que la
vision interdit), D48 (mesurer l'apprentissage réel, pas la satisfaction — l'apprenant préfère le
tuteur qui le flatte).
