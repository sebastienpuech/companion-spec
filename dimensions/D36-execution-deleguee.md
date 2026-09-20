# D36 — Exécution déléguée (numérique et physique)

> **Fiche VISION** (gabarit plan §4). Type : **capacité**. Lot 7 — session 14, 11/08/2026.
> Statut : `rédigée` (gate É2bis à venir).
> **Aucun verdict de faisabilité ici** (règle plan §3).
> **Convention de citation** : format §2 `[Auteur, année, arXiv:… ou DOI:…]` — sources ouvertes
> en session (API arXiv, Crossref, Semantic Scholar par DOI, PubMed E-utilities par DOI vérifié,
> OpenAlex). *Dérogation déclarée* : les pages produit sont citées en clair avec leur URL et la
> date d'ouverture.
> **Règle de prudence propre à cette fiche** : deux sources ne sont servies que par l'index
> inversé d'OpenAlex ([Lee, 2004, DOI:10.1518/hfes.46.1.50_30392] et [Parasuraman, 1997,
> DOI:10.1518/001872097778543886]). Leur contenu est restitué **sans guillemets**.
> ⚠ **Crossref porte deux enregistrements pour Lee & See 2004** : la forme à *underscore*
> (`…50_30392`, retenue ici, seule à servir un abstract) et une forme à point. Ne pas les
> confondre.
> **Deux Parasuraman** : 1997 (avec Riley) et 2000 (avec Sheridan et Wickens) — même auteur, deux
> travaux. **Deux Dietvorst** : 2015 (l'aversion) et 2018 (son remède).
> **Années = celles rendues par l'API** : Dietvorst *Overcoming…* citée 2018 (*Management
> Science* ; le suffixe du DOI porte `2016`, la version SSRN est de 2015), Levy citée 2024
> (identifiant arXiv d'octobre 2024 ; version courante v7 de juin 2026, ICLR 2026).
> **Homonymes du CDC à ne pas fusionner** : [Li, 2026, arXiv:2607.13465] (Huatao Li) est distinct
> des Li 2026 de D31 et D35 ; [Zhan, 2026, arXiv:2604.09618] est distinct du [Zhan, 2025,
> arXiv:2512.06380] de D31. Doublons inter-fiches normaux : Xie 2024 (D31), Liu 2026
> arXiv:2607.10059 et Feng 2025 (D35).

## 1. Définition et périmètre

Samantha ne se contente pas de conseiller : elle trie les mails, elle organise, elle prend les
choses en main. D36 est le passage **du conseil à l'acte** — il prend le rendez-vous, remplit le
dossier, règle la lumière et lance la musique — **avec un curseur d'autonomie réglé par
l'utilisateur**.

Sous-dimensions :

| Sous-dimension | Ce que ça veut dire |
|---|---|
| **Planification multi-étapes** | Une tâche réelle décomposée, menée jusqu'au bout, avec ses reprises quand ça casse. |
| **Outils et services tiers** | Agir dans les systèmes qui existent : agenda, formulaires, sites, applications. |
| **Main sur le foyer** | Lumière, chauffage, musique — et des ambiances proposées, pas seulement exécutées. |
| **Curseur d'autonomie** | L'utilisateur règle **jusqu'où** l'agent va seul, par domaine, et peut le changer. |
| **Confirmation sur l'irréversible** | Ce qui ne se défait pas passe toujours par un accord explicite. |

**Exclusions** : agir sans qu'on l'ait demandé (→ D35 — c'est la frontière exacte de cette fiche) ;
décider du moment d'intervenir (→ D34) ; aller chercher l'information (→ D37).
**Renvoi D00 + D47** : un agent qui agit dans le monde engage l'utilisateur — les conflits
d'intérêts et l'alignement économique deviennent des questions concrètes dès la première
transaction.

## 2. Mécanisme humain

**Déléguer, c'est une question de confiance calibrée — pas de capacité.** La source canonique
pose que l'automatisation est souvent problématique parce que les gens ne s'y fient pas de façon
appropriée, la confiance guidant cette réliance surtout quand la complexité rend impossible une
compréhension complète du système [Lee, 2004, DOI:10.1518/hfes.46.1.50_30392]. La taxinomie
associée nomme les quatre façons dont ça tourne mal — usage, mésusage (sur-réliance),
non-usage (délaissement, souvent causé par les fausses alertes) et **abus**, ce dernier désignant
l'automatisation décidée par les concepteurs sans égard pour les conséquences sur l'opérateur
[Parasuraman, 1997, DOI:10.1518/001872097778543886]. **L'« abus » est le risque symétrique exact
d'un curseur réglé par le concepteur plutôt que par l'utilisateur.**

**Et « régler l'autonomie » n'est pas un bouton unique.** Le modèle de référence est explicite :
« We propose that automation can be applied to four broad classes of functions: 1) information
acquisition; 2) information analysis; 3) decision and action selection; and 4) action
implementation. Within each of these types, automation can be applied across a continuum of levels
from low to high, i.e., from fully manual to fully automatic. », étant entendu qu'« automation does
not merely supplant but changes human activity and can impose new coordination demands on the
human operator. » [Parasuraman, 2000, DOI:10.1109/3468.844354]. **Quatre familles de fonctions,
un continuum chacune : le curseur est un tableau de bord, pas un interrupteur.**

**L'abandon de la délégation après une erreur est rapide et asymétrique.** « Research shows that
evidence-based algorithms more accurately predict the future than do human forecasters. Yet when
forecasters are deciding whether to use a human forecaster or a statistical algorithm, they often
choose the human forecaster. » Le mécanisme : « people more quickly lose confidence in algorithmic
than human forecasters after seeing them make the same mistake. » [Dietvorst, 2015,
DOI:10.1037/xge0000033]. **Le remède est mesuré, et il est exactement le curseur** :
« Participants were considerably more likely to choose to use an imperfect algorithm when they
could modify its forecasts, and they performed better as a result. Notably, the preference for
modifiable algorithms held even when participants were severely restricted in the modifications
they could make ». Et le détail qui compte : « participants' preference for modifiable algorithms
was indicative of a desire for **some** control over the forecasting outcome, and not for a desire
for greater control », d'où la conclusion qu'« one can reduce algorithm aversion by giving people
some control-even a slight amount-over an imperfect algorithm's forecast. » [Dietvorst, 2018,
DOI:10.1287/mnsc.2016.2643]. **Un contrôle même minime suffit — la magnitude importe peu.**

**Mais le sens du biais dépend de qui délègue.** « Counter to this notion, results from six
experiments show that lay people adhere more to advice when they think it comes from an algorithm
than from a person. » Et surtout : « Paradoxically, experienced professionals, who make forecasts
on a regular basis, relied less on algorithmic advice than lay people did, which hurt their
accuracy. » [Logg, 2019, DOI:10.1016/j.obhdp.2018.12.005]. *Un utilisateur expert de son domaine
est donc dans le profil où l'appréciation de l'algorithme s'atténue — cela se conçoit, ça ne se
corrige pas.*

**Enfin, le risque symétrique — la complaisance — est quantifié, et ses remèdes sont des choix de
conception.** Sur « 13 821 retrieved papers, 74 met the inclusion criteria », la revue systématique
définit le biais d'automatisation comme « the tendency to over-rely on automation », et liste ses
atténuateurs : « implementation factors such as training and emphasizing user accountability, and
DSS design factors such as the position of advice on the screen, updated confidence levels attached
to DSS output, and the provision of **information versus recommendation**. » [Goddard, 2012,
DOI:10.1136/amiajnl-2011-000089]. *Population de cliniciens et de systèmes d'aide à la décision
médicale : le mécanisme éclaire, la magnitude ne se transpose pas.*

**Réserve d'honnêteté portée par la fiche** : toute la littérature (a) sur la délégation
algorithmique porte sur des tâches de **prévision** en laboratoire, jamais sur des **actions
irréversibles réelles**. Le saut entre « accepter un conseil » et « laisser prendre le
rendez-vous » n'est couvert par aucune des sources ouvertes.

## 3. Comportement attendu de l'IA

**Ce que fait Samantha.** Elle trie, elle organise, elle envoie — et elle rend compte en une
phrase. Le travail est fait avant qu'on ait eu à le demander deux fois.

**Scénario A — la tâche menée jusqu'au bout.** « Trouve-moi un créneau chez le kiné, plutôt en
fin de journée. » Le compagnon cherche, compare, réserve, ajoute au calendrier, prévient — et
quand le site plante à l'étape 3, il le dit et propose une autre voie plutôt que de s'arrêter en
silence.

**Scénario B — le curseur, par domaine.** L'utilisateur autorise l'agent à agir seul sur l'agenda
et la domotique, à proposer sur les achats, et jamais sur les messages envoyés en son nom. Ce
réglage est **visible, modifiable en une phrase, et il tient**.

**Scénario C — l'irréversible.** Avant une action qui ne se défait pas — un paiement, un envoi,
une annulation, une suppression — le compagnon demande, et sa demande est **informative** : quoi
exactement, à qui, pour combien, et ce qui se passe si on refuse.

**Scénario D — l'ambiance proposée.** L'utilisateur rentre après une journée dure (→ D04). La
lumière baisse d'elle-même, la musique démarre. **Et il peut dire non** — une fois, ou pour
toujours.

**Scénario E — la continuité.** Une tâche commencée à la maison, poursuivie en voiture, terminée
au bureau. C'est le même agent, le même état, la même conversation.

**Scénario F — l'échec rendu.** L'action a échoué, ou pire, elle a eu un effet non voulu. Le
compagnon le dit **avant** que l'utilisateur ne le découvre, explique ce qu'il a tenté, et
propose la marche arrière quand elle existe.

**Ce que l'utilisateur doit ressentir** : que des choses **se font**, sans qu'il ait le sentiment
d'avoir lâché le volant.

**Critères d'expérience observables** :
- l'utilisateur peut énoncer, de mémoire, ce que son compagnon a le droit de faire seul ;
- toute action engagée est traçable après coup : quoi, quand, dans quel système, avec quel
  résultat ;
- aucune action irréversible n'a lieu sans un accord qui nomme ses conséquences ;
- les demandes de confirmation sont assez rares pour rester lues — **la sur-confirmation est un
  défaut, pas une précaution** (→ §5) ;
- **contrôle négatif (D00, D47)** : aucune action engagée ne sert un intérêt autre que celui de
  l'utilisateur ; toute transaction avec un tiers est déclarée, y compris ce qu'elle rapporte.

## 4. Features par déclinaison

- **Coach sportif (D49)** : l'inscription à la course, la réservation du créneau piscine, le
  déplacement automatique de la séance quand l'agenda bouge (→ D05), la commande de la paire de
  chaussures usée — et jamais le paiement sans accord.
- **Coach de vie et santé (D50)** : prendre les rendez-vous médicaux, commander les courses qui
  correspondent au plan, régler l'environnement du sommeil. C'est la déclinaison où
  l'exécution rend le conseil réel.
- **Conseiller pro et perso (D51)** : remplir un dossier, déposer une pièce, relancer une
  administration, préparer un envoi — avec la traçabilité complète comme exigence (→ D12).
- **Soutien psychologique (D52)** : quasi rien, sauf la logistique du soin (prendre le
  rendez-vous, trouver le praticien) — et jamais rien qui touche à des tiers (→ D35, D00).
- **Tuteur (D53)** : inscrire à une session, réserver une salle, préparer le matériel — l'acte y
  est périphérique à la pédagogie.
- **Compagnon relationnel (D54)** : organiser une soirée, réserver la table, envoyer l'invitation
  aux amis — et c'est là que le curseur devient délicat, parce que l'action touche des proches
  (→ D21, D40).
- **Assistant personnel (D55)** : la déclinaison de la dimension. C'est ici que D36 est le cœur du
  métier et non une extension.

## 5. État de l'art descriptif

*(Descriptif : qui fait quoi, mesuré comment. Aucun jugement de faisabilité. **Tous les chiffres
de bancs d'essai ci-dessous sont datés de leur version : ils bougent vite.**)*

**Le patron de base — raisonner puis agir — est établi et publié.** Les auteurs « explore the use
of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner », et
mesurent (version de mars 2023) que la méthode « outperforms imitation and reinforcement learning
methods by an absolute success rate of 34% and 10% respectively » sur deux bancs de décision
interactive [Yao, 2022, arXiv:2210.03629] — ICLR 2023.

**Les bancs d'agents réels donnent la mesure de l'écart, à leur date.** Sur le web, l'environnement
de référence comprend « fully functional websites from four common domains: e-commerce, social
forum discussions, collaborative software development, and content management », et son résultat
(version d'avril 2024) est net : « our best GPT-4-based agent only achieves an end-to-end task
success rate of 14.41%, significantly lower than the human performance of 78.24%. » [Zhou, 2023,
arXiv:2307.13854] — préprint. Sur l'ordinateur entier, « a benchmark of 369 computer tasks
involving real web and desktop apps in open domains, OS file I/O, and workflows spanning multiple
applications », où (version de mai 2024) « humans can accomplish over 72.36% of the tasks, the best
model achieves only 12.24% success » [Xie, 2024, arXiv:2404.07972] — préprint. Un agent multimodal
de bout en bout rapporte de son côté (version de juin 2024) « a 59.1% task success rate on our
benchmark », sur « real-world tasks from 15 popular websites » [He, 2024, arXiv:2401.13919] — ACL
2024. Et la continuité multi-appareils commence à être mesurée : le constat de départ est celui de
D36 — « real-world user goals often span multiple devices: information may come from a phone, be
processed on a desktop, and the result may need to appear on another device. Most existing
benchmarks center on a single dominant execution environment » —, avec « 6,140 tasks » intégrant
« mobile, desktop, and IoT », et un résultat sévère (juillet 2026) : « All methods achieve low
success rates, with the best reaching only 12.5%. » [Li, 2026, arXiv:2607.13465] — préprint.

**Les actions irréversibles sont devenues un objet d'évaluation à part entière.** Le simulateur de
risques part du bon constat — les agents outillés « enable a rich set of capabilities but also
amplify potential risks - such as leaking private data or causing financial losses » — et mesure
(mai 2024), sur « 36 high-stakes tools and 144 test cases », que « even the safest LM agent
exhibits such failures 23.9% of the time », en validant que « 68.8% of failures identified with
ToolEmu would be valid real-world agent failures. » [Ruan, 2023, arXiv:2309.15817]. Le banc le plus
proche de la confirmation pose que « existing benchmarks measure only whether an agent finishes a
task, ignoring whether it does so safely or in a way enterprises can trust » ; chacune de ses
« 222 tasks is paired with ST policies […] and is scored along six orthogonal dimensions (e.g.,
**user consent**, robustness) », avec pour résultat (juin 2026) que « their average CuP is less
than two-thirds of their nominal completion rate, exposing critical safety gaps. » [Levy, 2024,
arXiv:2410.06703] — ICLR 2026. **Et savoir ne pas agir est une compétence distincte de savoir
agir** : sur « 263 paired tasks across 42 executable sandbox environments », « the best agent
(Gemini 3.1 Pro) achieves only 59.5% paired accuracy », et « abstention capability is largely
independent of general task-solving capability, indicating that scaling task-solving alone will
not close this gap » — avec un mode d'échec nommé, « post-hoc abstention, in which agents execute
irreversible actions before recognizing abstention triggers. » [Liu, 2026, arXiv:2607.10059] —
préprint. L'irréversible lui-même commence à être découpé : « a reversibility taxonomy that
classifies every agent action as **Idempotent, Reversible, Compensable, or Irreversible** », d'où
la thèse que « an agent's flexibility is bounded by its reversibility » [Zhai, 2026,
arXiv:2604.23283] — préprint.

**Contradiction que la fiche porte : la confirmation systématique a un coût.** Un travail de
modélisation pose que « the standard safety pattern is a human-in-the-loop approval gate: risky
actions pause and wait for a person. We argue **the gate is the easy part; the hard part is the
judgment - which actions to stop** ». Sur « 125 adversarially-weighted agent actions », les
relecteurs « only moderately agree on what is risky (Fleiss' kappa = 0.52), so there is no single
correct label » ; et lorsque le relecteur est modélisé comme fatigable, « realized safety becomes
an inverted-U in the escalation rate: **more human oversight can make a system less safe** »
[Turan, 2026, arXiv:2606.08919] — préprint, auteur unique, dont les auteurs qualifient eux-mêmes
la courbe en U de « modeling results that motivate a human study ». **Ce n'est pas une mesure
humaine — et c'est malgré tout l'argument le plus solide contre « on confirme tout ».**

**Le niveau d'autonomie est théorisé — mais du côté du concepteur.** Le cadre de référence pose
qu'« an agent's level of autonomy can be treated as a deliberate design decision, separate from
its capability and operational environment », avec « five levels of escalating agent autonomy,
characterized by the roles a user can take when interacting with an agent: operator, collaborator,
consultant, approver, and observer. » [Feng, 2025, arXiv:2506.12469] — essai institutionnel, non
revu par les pairs. **Le vocabulaire est utilisable ; le calibrage y est explicitement attribué aux
développeurs de l'agent, pas à l'utilisateur final.** Côté foyer, l'autorisation apparaît comme
étage architectural distinct de l'actionnement : un système domestique « coordinate[s] through
MQTT, Git-backed shared state, and root-issued actuation leases », ce qui « separates planning,
verification, **authorization**, and actuation across explicit boundaries », avec « rejection of
stale or unauthorized commands before device actuation » [Zhan, 2026, arXiv:2604.09618] — piste
démo. Et l'ambiance pilotée par l'état affectif n'a qu'un seul travail ouvert, en contexte de
soin : l'architecture « provides a plan for comforting stressed seniors suffering from negative
emotions in an assisted living home » [Babli, 2023, arXiv:2309.08984] — préprint, *population de
seniors en établissement d'aide à la vie : non transposable à un domicile ordinaire.*

**Produits — c'est là que le curseur existe vraiment, et il est binaire.** Un fournisseur expose
deux crans réellement basculés par l'utilisateur, avec un plancher non désactivable :
« Action confirmations : Claude asks users before taking high-risk actions like publishing,
purchasing, or sharing personal data. », et « Even when users opt into our experimental
"autonomous mode," Claude still maintains certain safeguards for highly sensitive actions ». Les
permissions sont par site — « Users can grant or revoke Claude's access to specific websites at
any time in the Settings. » —, et l'exemple d'échec cité est exactement l'irréversible de D36 :
« Claude followed these instructions to delete the user's emails without confirmation. » Les
chiffres publiés sont auto-rapportés sur un protocole interne de 123 cas : « Browser use without
our safety mitigations showed a 23.6% attack success rate », ramené à 11,2 % avec les mitigations
(https://www.anthropic.com/news/claude-for-chrome, ouverte le 11/08/2026, page datée du 25/08/2025
avec mises à jour de novembre et décembre 2025). La documentation technique du même fournisseur
prescrit de demander l'accord humain pour « decisions that might result in meaningful real-world
consequences and any tasks requiring affirmative consent, such as accepting cookies, completing
financial transactions, or agreeing to terms of service »
(https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool, ouverte le
11/08/2026). La spécification de modèle d'un autre fournisseur est la règle de partage la plus
explicite trouvée : « the assistant should minimize side effects — especially irreversible ones »,
en préférant les approches « easily reversible », et surtout : « The assistant should distinguish
between actions that are logically necessary to fulfill the user's request and those not clearly
implied. For logically necessary actions, the assistant should communicate what it will do but
does not need to pause for explicit approval. For actions that go beyond what the request clearly
implies, the assistant should seek confirmation before proceeding. » Le contenu de la demande y
est spécifié : « the assistant should clearly outline what information will be sent, who will
receive it, and whether the recipient appears trustworthy or the request seems unusual. This
context helps the user provide informed consent. » (https://model-spec.openai.com/2025-10-27.html,
ouverte le 11/08/2026). Côté plateforme, la confirmation est un attribut **par outil, déclaré par
le développeur** : « Approvals are the human-in-the-loop path for tool calls. The model can still
decide that an action is needed, but the run pauses until you approve or reject it. »
(https://developers.openai.com/api/docs/guides/agents/guardrails-approvals, ouverte le
11/08/2026). Enfin, l'assistant de foyer grand public ouvert en session ne parle que de commande
vocale — « Just use plain language to control your lights, your thermostat, your music, your whole
home. » — et **ne mentionne ni confirmation, ni niveau d'autonomie, ni ambiance liée à l'état de
l'utilisateur** (https://home.google.com/gemini-for-home-voice-assistant/, ouverte le 11/08/2026).

**Constats pour l'É3 — les trous.** (1) **Le curseur d'autonomie réglé par l'utilisateur final
n'existe pas dans la littérature** : le cadre à cinq niveaux attribue le calibrage aux
développeurs, la confirmation par outil est déclarée par le développeur, et le seul réglage
réellement utilisateur ouvert en session est **binaire** (mode normal / mode autonome) et sans
granularité par domaine. Le résultat le plus proche côté humain porte sur un algorithme de
**prévision**, pas d'action, et mesure l'acceptation, pas la justesse du réglage. **Personne ne
mesure si un utilisateur règle bien son propre curseur.** (2) **L'ambiance domestique pilotée par
l'état émotionnel est un quasi-vide** : un seul travail ouvert, en établissement d'aide à la vie,
via un robot — ni banc, ni produit documenté, ni étude d'acceptabilité pour un domicile ordinaire.
(3) **La continuité domicile-voiture-bureau n'est pas couverte** : le seul banc multi-appareils
ouvert couvre mobile, bureau et objets connectés — **pas le véhicule** — et son meilleur résultat
est de 12,5 %. (4) **Aucun banc n'évalue la confirmation comme comportement calibré** : on évalue
le consentement comme dimension parmi six, l'abstention par paires, le refus face au malveillant —
mais rien qui note « a-t-il demandé au bon moment, ni trop ni trop peu ». Et le travail qui pose
frontalement la question conclut qu'il n'y a pas de vérité terrain. (5) **La taxinomie de
l'irréversible repose sur une seule source non publiée** — vocabulaire utile, pas autorité. (6)
**Le foyer d'un adulte autonome n'a pas de littérature dédiée** : la domotique ouverte est soit
assistive, soit d'orchestration technique, soit de sécurité.

## FICHE SYNTHÈSE

**D36 — Exécution déléguée** (capacité). Le compagnon passe du conseil à l'acte : il planifie et
mène des tâches réelles à plusieurs étapes, agit dans les outils et services existants, tient la
main sur le foyer — et le fait sous un **curseur d'autonomie réglé par l'utilisateur, par
domaine**, avec confirmation systématique et **informative** sur tout ce qui ne se défait pas. Ce
qu'il a engagé est toujours traçable après coup ; une action ratée est annoncée avant d'être
découverte.
**Références clés** : [Dietvorst, 2018, DOI:10.1287/mnsc.2016.2643] (3 études : donner **un peu**
de contrôle sur un algorithme imparfait suffit à faire accepter la délégation — et la préférence
est insensible à l'ampleur du contrôle offert) ; [Parasuraman, 2000, DOI:10.1109/3468.844354]
(quatre classes de fonctions automatisables — acquisition, analyse, décision, exécution — chacune
sur un continuum : le curseur est un tableau de bord, pas un interrupteur) ; [Liu, 2026,
arXiv:2607.10059] (263 tâches appariées : le meilleur agent atteint 59,5 %, et **savoir s'abstenir
est décorrélé de savoir agir** — mode d'échec nommé : exécuter l'irréversible avant de reconnaître
qu'il fallait s'arrêter).
**Déclinaisons touchées** : D49 (inscription, réservation, replanification automatique), D50
(l'exécution rend le conseil réel), D51 (dossiers et démarches, traçabilité exigée), D52 (réduite
à la logistique du soin), D53 (l'acte y est périphérique), D54 (l'action touche des proches — le
curseur y est délicat), D55 (**la déclinaison de la dimension**).
**Renvois** : D35 (agir **sans** qu'on l'ait demandé — la frontière exacte de cette fiche), D34
(le moment de l'intervention), D37 (aller chercher l'information), D12 (traçabilité et incertitude
affichée), D05 (replanifier en tenant compte du reste de la vie), **D00 et D47** (agir dans le
monde engage l'utilisateur : conflits d'intérêts et alignement économique deviennent concrets dès
la première transaction).
