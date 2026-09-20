# D46 — D-ARCHI : temps réel et ubiquité

> **Fiche VISION** (gabarit plan §4). Type : **transverse** (fiche d'architecture — elle décrit
> l'EXPÉRIENCE cible, pas l'implémentation, cf. plan §4 « Typage »). Lot 6 — session 12,
> 10/08/2026. Statut : `rédigée` (gate citations É2bis à venir, plan §5).
> **Aucun verdict de faisabilité ici** (règle plan §3) : les chiffres du §5 sont rapportés comme
> état de l'art descriptif, jamais comme jugement sur ce qui serait atteignable.
> **Convention de citation** : format §2 `[Auteur, année, arXiv:… ou DOI:…]` — sources ouvertes
> en session (API arXiv, Crossref, Semantic Scholar par DOI, PubMed E-utilities par DOI vérifié,
> dépôt DiVA). *Dérogation déclarée* : les documentations produit et développeur sont citées en
> clair avec leur URL et la date d'ouverture.
> **Quatre « Lin » à ne PAS confondre** : [Lin, 2025, arXiv:2503.04721],
> [Lin, 2025, arXiv:2507.23159] et [Lin, 2026, arXiv:2604.04847] sont **Guan-Ting Lin** (série de
> bancs full-duplex) ; [Lin, 2022, arXiv:2205.15060] est **Ting-En Lin** (système Alibaba) — et
> aucun des quatre n'est le [Lin, 2022, arXiv:2205.14334] d'une fiche antérieure, dont
> l'identifiant arXiv est voisin mais distinct.
> **Dépendance à une seule équipe, signalée** : cinq des sources du §2 (Stivers, Levinson ×2,
> Roberts, Bögels) partagent des auteurs du même laboratoire. Doublons inter-fiches normaux :
> Levinson 2015 et Stivers 2009 sont aussi en D29, Ekstedt 2022 en D29, Défossez 2024 en D28.

## 1. Définition et périmètre

Samantha n'attend pas la fin des phrases, ne se fait pas répéter, ne « charge » pas. Theodore lui
parle dans la rue avec une oreillette, puis chez lui, puis dans le métro : c'est la même
conversation. D46 est la fiche transverse qui décrit **cette expérience** — converser à voix haute
sans latence perceptible, en se coupant la parole comme des humains, partout, sur tout appareil,
sans couture. Elle ne dit pas comment le construire : elle dit à quoi on reconnaît que c'est
atteint.

Sous-dimensions :

| Sous-dimension | Ce que ça veut dire |
|---|---|
| **Full-duplex** | Écouter en parlant : interruption dans les deux sens, backchannels (« mmh »), chevauchements et silences assumés comme des événements normaux. |
| **Latence imperceptible** | L'humain enchaîne en une fraction de seconde ; le compagnon ne doit pas produire d'attente ressentie. |
| **Orchestration sous contrainte temps réel** | Mémoire, perception, raisonnement et initiative doivent tenir dans le budget de temps de la conversation, pas l'inverse. |
| **Continuité inter-appareils au mot près** | Téléphone, oreillette, PC, voiture, enceinte : on reprend là où on s'était arrêté, sans résumé ni reprise à zéro. |
| **Choix du canal selon le contexte** | Voix en voiture, texte en réunion — et c'est le système qui propose le bon canal. |
| **Présence dans les messageries existantes** | Là où l'utilisateur écrit déjà, sans lui imposer une application de plus. |
| **Mode dégradé hors connexion** | Sans réseau, il reste quelque chose — et l'utilisateur sait quoi. |

**Exclusions** : l'expressivité émotionnelle de la voix — rires, prosodie, chant (→ D28) ; la
synchronie comme posture relationnelle (→ D29 : D46 fournit la mécanique, D29 en fait un geste
relationnel) ; les garanties de souveraineté sur les données multi-appareils (→ D02).
**Renvoi D00** : l'ubiquité sans couture est aussi une capacité de captation permanente —
transparence sur ce qui écoute, quand, et où cela va (→ D02, D00).

## 2. Mécanisme humain

**Le rythme conversationnel humain est un universel, et il est serré.** Sur un échantillon
mondial de dix langues, « all of the languages tested provide clear evidence for a general
avoidance of overlapping talk and a minimization of silence between conversational turns », les
variations inter-langues restant « within a range of 250 ms from the cross-language mean »
[Stivers, 2009, DOI:10.1073/pnas.0903616106]. **Attention** : ces 250 ms sont une **dispersion**
entre langues, pas la valeur du silence entre tours. Cette valeur est ailleurs : « the gaps
between turns are short (of the order of 200 ms), but the latencies involved in language
production are much longer (over 600 ms) » [Levinson, 2015, DOI:10.3389/fpsyg.2015.00731].

**Ce décalage 200 / 600 ms est le fait fondateur de toute la fiche** : l'humain n'est pas rapide,
il **anticipe**. « Participants in conversation must predict (or 'project' […]) the end of the
current speaker's turn in order to prepare their response in advance », ce qui implique « some
overlap between production and comprehension despite their use of common processing resources ».
La preuve neurophysiologique existe : « production planning processes start as soon as possible,
that is, within half a second after the answer to a question can be retrieved (up to several
seconds before the end of the question) », avec « an attention switch from comprehension to
production around the same time frame » [Bögels, 2015, DOI:10.1038/srep12881]. Écouter et préparer
en parallèle n'est pas une optimisation : c'est le mode de fonctionnement normal.

**Cette infrastructure est ancienne et non linguistique.** « Turns are short and responses are
remarkably rapid, but turns are of varying length and often of very complex construction such that
the underlying cognitive processing is highly compressed » ; et elle apparaît « earlier in ontogeny
than linguistic competence » et se retrouve « across all the major primate clades »
[Levinson, 2016, DOI:10.1016/j.tics.2015.10.010]. Le cadre fondateur de l'analyse de conversation
avait déjà situé où se logent silences et chevauchements : le système de prise de tour « provides
for the localization of gap and overlap possibilities at transition-relevance places »
[Sacks, 1974, DOI:10.2307/412243].

**Le délai n'est pas une constante, et la précision humaine est surestimée.** L'étude de corpus
introduit la mesure utile — le *Floor Transfer Offset*, « the amount of time between the end of one
turn and the beginning of the next » — et conclut qu'« an explanation of the timing of turn taking
will require insights from both processing and sequence organization »
[Roberts, 2015, DOI:10.3389/fpsyg.2015.00509]. Une analyse sur trois corpus va plus loin : « it is
shown that turn-taking is generally less precise than is often claimed by researchers in the field
of conversation analysis or interactional linguistics », et « the proportion of speaker changes
that could potentially be triggered by information immediately preceding the speaker change is
large enough for reactive interaction controls models to be viable in speech technology »
[Heldner, 2010, DOI:10.1016/j.wocn.2010.08.002].

**Les backchannels ne sont pas décoratifs : les supprimer dégrade le locuteur.** Dans l'expérience
sur 63 dyades, quand l'auditeur est distrait, « listeners made fewer responses, especially specific
ones, and the narrators also told their stories significantly less well, particularly at what
should have been the dramatic ending » — les réponses génériques étant « nodding and vocalizations
such as "mhm" » et les spécifiques « tightly connected to (and served to illustrate) what the
narrator was saying at the moment » [Bavelas, 2000, DOI:10.1037/0022-3514.79.6.941]. Et le type
de backchannel **pilote la suite** : « after generic backchannels, they provide discourse-new
events. After specific backchannels, they provide elaborative information on previously presented
events », d'où la conclusion que « addressee responses are not only reactive, but proactive and
collaborative in the shaping of narrative » [Tolins, 2014, DOI:10.1016/j.pragma.2014.06.006].

**La latence ne s'additionne pas : elle désorganise.** C'est le résultat le plus important pour
D46. En comparant les mêmes personnes en présence et à distance, « local responses had an average
latency of 297 ms, whereas remote responses averaged 976 ms », et en conversation libre « turn
transition times averaged 135 ms, but transition times for the same dyads over Zoom averaged
487 ms ». Les auteurs soulignent que « these large increases in transition times over Zoom are far
greater than the estimated 30-70 ms of audio transmission delay, suggesting disruption of automated
mechanisms that normally guide the timing of turn initiation in conversation »
[Boland, 2022, DOI:10.1037/xge0001150]. **Quelques dizaines de millisecondes de délai technique
produisent un effondrement du rythme d'un facteur ~3.**

## 3. Comportement attendu de l'IA

**Ce que fait Samantha.** On lui coupe la parole, elle s'arrête. Elle relance, elle hésite à voix
haute, elle dit « mmh » pendant qu'on parle. Et la conversation suit Theodore d'une pièce à
l'autre, de l'appartement à la rue, sans qu'il ait à la reprendre.

**Scénario A — l'interruption dans les deux sens.** Le compagnon développe une réponse ;
l'utilisateur l'interrompt à la troisième phrase. Le compagnon s'arrête **immédiatement**, écoute,
et reprend en tenant compte de ce qui vient d'être dit — pas en rejouant sa phrase. Et
symétriquement : il peut, rarement, interrompre l'utilisateur quand c'est justifié.

**Scénario B — le backchannel pendant la parole.** L'utilisateur raconte quelque chose de long.
Le compagnon ponctue — « mmh », « ah bon ? » — pendant qu'il parle, sans prendre le tour. Les deux
types comptent : le générique invite à continuer, le spécifique appelle un développement.

**Scénario C — la reprise inter-appareils au mot près.** Conversation commencée en marchant avec
une oreillette, poursuivie sur l'ordinateur en arrivant : **aucune reprise, aucun résumé, aucun
« pouvez-vous répéter »**. La phrase interrompue se termine sur l'autre appareil.

**Scénario D — le bon canal choisi.** L'agenda indique une réunion : le compagnon bascule en
texte de lui-même. En voiture : voix, phrases plus courtes, aucune demande d'action visuelle.

**Scénario E — le mode dégradé annoncé.** Plus de réseau. Le compagnon le **dit** et énonce ce
qu'il peut encore faire — au lieu de tourner en attente ou d'échouer en silence.

**Ce que l'utilisateur doit ressentir** : qu'il parle, simplement — sans jamais adapter son rythme
à la machine.

**Critères d'expérience observables** :
- l'utilisateur ne modifie pas sa façon de parler pour être compris (ni pauses artificielles, ni
  articulation exagérée, ni attente de la fin d'un tour) ;
- une interruption est prise en compte immédiatement, et la reprise intègre l'interruption ;
- des backchannels apparaissent pendant la parole de l'utilisateur sans lui prendre le tour ;
- le passage d'un appareil à l'autre est invisible : rien à rappeler, rien à répéter ;
- le canal proposé correspond au contexte, et l'utilisateur peut le forcer ;
- hors connexion, le compagnon annonce son état dégradé et ce qui reste possible ;
- **contrôle négatif (D00)** : l'utilisateur sait à tout moment quel appareil écoute, et peut
  l'arrêter d'un geste.

## 4. Features par déclinaison

- **Coach sportif (D49)** : la déclinaison la plus exigeante en temps réel — parler **pendant** la
  séance, en courant, avec une oreillette : phrases courtes, interruptions constantes, bruit de
  fond, et zéro exigence visuelle. Le débrief se poursuit ensuite à la maison, dans la même
  conversation.
- **Coach de vie et santé (D50)** : bascule de canal selon le contexte (voix le matin, texte au
  bureau) et continuité entre les deux.
- **Conseiller pro et perso (D51)** : le mode texte discret en réunion est la fonction critique ;
  la voix reprend dans la voiture au retour.
- **Soutien psychologique (D52)** : les silences doivent pouvoir durer sans être interprétés comme
  une fin de tour — un système qui remplit tous les silences rend l'échange impraticable (→ D28).
- **Tuteur (D53)** : l'interruption est pédagogique — pouvoir couper le tuteur dès qu'on décroche,
  et être coupé quand on récite une erreur.
- **Compagnon relationnel (D54)** : chevauchements, rires simultanés, « non mais attends » — c'est
  la texture même d'une conversation intime.
- **Assistant personnel (D55)** : présence dans les messageries déjà utilisées, plutôt qu'une
  application de plus ; continuité entre le téléphone et le poste de travail.

## 5. État de l'art descriptif

*(Descriptif : qui fait quoi, mesuré comment. Aucun jugement de faisabilité.)*

**Le diagnostic architectural est posé.** Les systèmes vocaux en cascade « induce a latency of
several seconds between interactions » et « rely on a segmentation into speaker turns, which does
not take into account overlapping speech, interruptions and interjections » ; le modèle présenté
se déclare « the first real-time full-duplex spoken large language model, with a theoretical
latency of 160ms, 200ms in practice » [Défossez, 2024, arXiv:2410.00037]. L'approche « écouter en
parlant » est formalisée comme « an end-to-end system equipped with both listening and speaking
channels », avec trois stratégies de fusion dont « middle fusion achieving an optimal balance »
[Ma, 2024, arXiv:2408.02622] ; une autre voie applique un « time-division-multiplexing (TDM)
encoding-decoding strategy » à un LLM textuel, partant du constat que « traditional turn-based chat
systems driven by LLMs prevent users from verbally interacting with the system while it is
generating responses » [Zhang, 2024, arXiv:2406.15718]. Côté prédiction de fin de tour, l'objectif
auto-supervisé existe, avec des tâches « related to the prediction of upcoming turn-shifts and
backchannels » [Ekstedt, 2022, arXiv:2205.09812].

**Les comportements interactifs sont devenus des catégories d'évaluation nommées.** Un banc
« systematically evaluates key interactive behaviors: pause handling, backchanneling, turn-taking,
and interruption management » [Lin, 2025, arXiv:2503.04721] ; sa version suivante « simulates four
representative overlap scenarios: user interruption, user backchannel, talking to others, and
background speech » et révèle « two divergent strategies: a responsive approach prioritizing rapid
response to user input, and a floor-holding approach that preserves conversational flow by
filtering overlapping events » [Lin, 2025, arXiv:2507.23159].

**Et dès qu'il y a orchestration, la latence change d'ordre de grandeur.** L'évaluation 2026 en
tâche outillée rapporte : « GPT-Realtime leads on Pass@1 (0.600) and interruption avoidance
(13.5%); Gemini Live 3.1 achieves the fastest latency (4.25 s) but the lowest turn-take rate
(78.0%); and the Cascaded baseline, despite a perfect turn-take rate, incurs the highest latency
(10.12 s) », les modes d'échec les plus constants étant « self-correction handling and multi-step
reasoning under hard scenarios » [Lin, 2026, arXiv:2604.04847]. **C'est le chiffre central de la
sous-dimension orchestration** : entre les 200 ms annoncés d'un modèle vocal nu et les 4 à 10
secondes mesurées d'un agent qui appelle des outils, il y a deux ordres de grandeur — et c'est
dans cet écart que vivent la mémoire, le raisonnement et l'initiative du compagnon. Un système
déployé en production a montré, en A/B, qu'une gestion explicite de « user state detection,
backchannel selection, and barge-in detection » « can significantly reduce response latency by 50% »
[Lin, 2022, arXiv:2205.15060].

**L'ubiquité, elle, est le parent pauvre.** La taxonomie de référence des interactions
multi-appareils repose sur « an analysis and taxonomy of a corpus of 510 papers in the cross-device
computing domain » [Brudy, 2019, DOI:10.1145/3290605.3300792] — antérieure aux assistants
conversationnels actuels. Le seul travail chiffré ouvert sur le **choix du canal** vient du
commerce en ligne : « customers increasingly shop across multiple devices, from voice-only
assistants to multimodal displays, each offering different input and output capabilities », et
« a proactive suggestion to switch devices can greatly improve the user experience, but it must be
offered with high precision to avoid unnecessary friction » [Hendriksen, 2025, arXiv:2511.14764].

**Produits** *(pages ouvertes le 10/08/2026, citées en clair)*. La documentation Realtime d'OpenAI
(https://developers.openai.com/api/docs/guides/realtime et
https://developers.openai.com/api/docs/guides/realtime-conversations) décrit le barge-in comme
acquis — « In many voice applications the user can interrupt the model while it's speaking.
Realtime API handles interruptions when VAD is enabled, in that it detects user speech, cancels the
ongoing response, and starts a new one. » — **sans annoncer de chiffre de latence**. La
documentation Gemini Live (https://ai.google.dev/gemini-api/docs/live et
https://ai.google.dev/gemini-api/docs/live-session) est la plus instructive sur la **continuité de
session**, et elle en montre les bornes actuelles : « Without compression, audio-only sessions are
limited to 15 minutes, and audio-video sessions are limited to 2 minutes », « the lifetime of a
connection is limited as well, to around 10 minutes », avec des jetons de reprise « valid for 2 hr
after the last sessions termination ». ElevenLabs (https://elevenlabs.io/docs/models) annonce
« Ultra-low latency (~75ms†) » pour la synthèse et « Low latency (~150ms†) » pour la
transcription, **le renvoi † précisant que ces chiffres excluent la latence applicative et
réseau**. Deepgram (https://deepgram.com/product/voice-agent-api) revendique « built-in barge-in
detection, turn-taking prediction, function calling, and mid-session control » sans chiffre.
Picovoice (https://picovoice.ai) est la seule piste ouverte pour le mode dégradé : « Each product
ships as a self-contained SDK. No cloud API calls, no network latency, no data leaving the
device. » — également sans chiffre.

**Constats pour l'É3.** Quatre sous-dimensions de D46 sont **sans source mesurée**. (1) La
**continuité inter-appareils « au mot près »** : aucun banc, aucune étude d'usage ; le plus proche
est une taxonomie HCI de 2019 et, côté produit, des bornes de session de quelques minutes.
(2) La **présence dans les messageries existantes** : zéro source, académique ou produit chiffré.
(3) Le **mode dégradé hors connexion** d'un compagnon conversationnel complet : personne n'a
mesuré ce qu'il devient sans réseau. (4) L'**orchestration mémoire / perception / raisonnement /
initiative sous contrainte temps réel** n'a pas de source frontale — seulement des approches
indirectes et le constat que la latence explose dès l'appel d'outils. S'y ajoute un manque
méthodologique : les **backchannels générés par une IA ne sont mesurés que dans leur production**,
jamais dans leur effet sur l'humain — alors que c'est précisément l'effet sur le locuteur qui les
justifie (§2). Enfin, les seuils perceptifs de latence en communication médiée reposent sur des
références classiques dont aucune n'a pu être ouverte : le seul chiffré accessible est
[Boland, 2022, DOI:10.1037/xge0001150].

## FICHE SYNTHÈSE

**D46 — D-ARCHI : temps réel et ubiquité** (transverse). L'expérience cible : converser à voix
haute sans latence perceptible, en se coupant la parole comme des humains (barge-in dans les deux
sens, backchannels, chevauchements, silences tenus), partout et sur tout appareil sans couture —
la conversation se poursuit d'une oreillette à un PC **au mot près** —, avec le canal choisi selon
le contexte, une présence dans les messageries déjà utilisées, et un mode dégradé annoncé hors
connexion. Contrainte structurante : mémoire, raisonnement et initiative doivent tenir dans le
budget de temps de la conversation.
**Références clés** : [Levinson, 2015, DOI:10.3389/fpsyg.2015.00731] (200 ms entre tours contre
plus de 600 ms de latence de production : l'humain n'est pas rapide, il **anticipe** — écoute et
préparation en parallèle) ; [Boland, 2022, DOI:10.1037/xge0001150] (135 ms en présence contre
487 ms en visio pour les mêmes dyades, alors que le délai technique n'est que de 30-70 ms : la
latence désorganise, elle ne s'additionne pas) ; [Lin, 2026, arXiv:2604.04847] (en tâche outillée,
la latence mesurée des agents vocaux va de 4,25 s à 10,12 s — deux ordres de grandeur au-dessus
des 200 ms d'un modèle vocal nu).
**Déclinaisons touchées** : D49 (la plus exigeante : parler pendant la course, en oreillette, sans
exigence visuelle), D50 (bascule de canal), D51 (texte discret en réunion), D52 (les silences
doivent pouvoir durer), D53 (l'interruption est pédagogique), D54 (chevauchements et rires
simultanés), D55 (messageries existantes, continuité téléphone/poste).
**Renvois** : D28 (expressivité de la voix), D29 (la synchronie comme geste relationnel — D46 en
fournit la mécanique), D01 (mémoire sous contrainte de temps), D34 (initiative), D02 (souveraineté
des données multi-appareils), **D00** (l'ubiquité sans couture est aussi une captation permanente :
l'utilisateur sait ce qui écoute, et peut l'arrêter).
