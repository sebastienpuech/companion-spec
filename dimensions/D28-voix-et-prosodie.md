# D28 — Voix et prosodie émotionnelles

> **Fiche VISION** (gabarit plan §4). Type : **capacité**. Lot 6 — session 12, 10/08/2026.
> Statut : `rédigée` (gate citations É2bis à venir, plan §5).
> **Aucun verdict de faisabilité ici** (règle plan §3).
> **Convention de citation** : format §2 `[Auteur, année, arXiv:… ou DOI:…]` — sources ouvertes
> en session (API arXiv, Crossref, Semantic Scholar par DOI, PubMed E-utilities par DOI vérifié).
> *Dérogation déclarée* : les pages produit sont citées en clair avec leur URL et la date
> d'ouverture. Années = celles rendues par l'API : Cowen citée **2019** (année Crossref ; S2 dit
> 2018), Laukka citée 2020 (Crossref rend {2020 en ligne, 2021 imprimé}).
> **Trois « Yang » distincts** en §5 : [Yang, 2025, arXiv:2511.08723] (Shu-wen Yang),
> [Yang, 2026, arXiv:2603.11947] (Hao Yang), [Yang, 2025, arXiv:2504.12867] (Guanrou Yang) —
> trois personnes, trois travaux. **Conflit d'intérêts à connaître** : Alan Cowen, premier auteur
> de la source des « 24 émotions », est le fondateur de Hume AI, cité en §5 comme produit ; les
> chiffres du papier (24) et ceux du produit (48+) sont **distincts et ne doivent pas être
> fusionnés**. Doublon inter-fiches normal : Scott 2014 est aussi en D15 (trois « Scott »
> distincts existent désormais dans le CDC : 1995, 2013, 2014).

## 1. Définition et périmètre

Samantha n'a pas de corps ; elle a une voix — et c'est suffisant. D28 spécifie ce que doit être
cette voix : un canal qui **entend** l'état affectif de l'utilisateur, y compris quand les mots
disent le contraire, et qui **rend** un état affectif congruent, avec tout ce qui fait une voix
vivante — rires, soupirs, respiration, chant, silences habités.

Sous-dimensions :

| Sous-dimension | Ce que ça veut dire |
|---|---|
| **Décodage prosodique** | Entendre l'émotion dans la voix, indépendamment du contenu verbal. |
| **Détection d'incongruence** | Le « ça va » dit d'une voix éteinte est traité comme un signal, pas comme une information. |
| **Production congruente** | La voix rendue correspond au moment relationnel — pas d'enthousiasme de standardiste sur une mauvaise nouvelle. |
| **Rires, soupirs, respiration** | Les vocalisations non verbales existent et arrivent au bon moment, y compris hors de tout trait d'humour. |
| **Chant** | Dans « Her », Samantha compose et chante « The Moon Song ». La voix peut faire autre chose que parler. |
| **Signaux ostensifs vocaux** | Le prénom prononcé, le ton d'adresse : la voix dit « c'est à toi que je parle ». |
| **Pauses et silences habités** | Le silence est un acte de conversation, pas une panne. |

**Exclusions** : la mécanique temps réel — full-duplex, latence, barge-in, ubiquité (→ D46) ;
la compréhension de l'état émotionnel par le texte et le contexte (→ D04) ; l'empathie comme
conduite relationnelle (→ D10). **Renvoi D00** : une voix émotionnellement crédible augmente
fortement l'attribution d'intériorité — la transparence sur la nature IA et l'anti-dépendance
s'appliquent d'autant plus.

## 2. Mécanisme humain

**Il existe un code acoustique de l'émotion, et il est partagé avec la musique.** La revue de
104 études d'expression vocale et 41 études de performance musicale conclut à des similarités
entre les deux canaux « concerning (a) the accuracy with which discrete emotions were communicated
to listeners and (b) the emotion-specific patterns of acoustic cues used to communicate each
emotion » [Juslin, 2003, DOI:10.1037/0033-2909.129.5.770]. Ce code est partiellement universel,
mais dialectal : la méta-analyse de 37 études interculturelles (26 groupes d'émetteurs,
44 cultures de percepteurs) montre qu'« a wide variety of positive and negative emotions could be
recognized with above-chance accuracy in cross-cultural conditions », mais aussi « evidence for
in-group advantage with higher accuracy in within- versus cross-cultural conditions »
[Laukka, 2020, DOI:10.1177/1754073919897295]. Un compagnon vocal générique perd donc de la
précision sur un utilisateur donné.

**La granularité utile n'est pas de six émotions, mais d'au moins vingt-quatre.** L'étude sur les
salves vocales brèves établit que « vocal bursts convey at least 24 distinct kinds of emotion »,
que « emotion categories (sympathy, awe) more so than affective appraisals (including valence and
arousal) organize emotion recognition », et que ces catégories « are bridged by smooth gradients
with continuously varying meaning » [Cowen, 2019, DOI:10.1037/amp0000399]. Et ces vocalisations
non verbales franchissent les cultures : « vocalizations communicating the so-called "basic
emotions" […] were bidirectionally recognized », même si « most positive emotions are communicated
with culture-specific signals » [Sauter, 2010, DOI:10.1073/pnas.0908239106].

**La voix seule est le meilleur canal, pas un canal dégradé.** Sur cinq expériences et N = 1 772,
« voice-only communication elicits higher rates of empathic accuracy relative to vision-only and
multisense communication », l'explication avancée étant « increasing focused attention on the
linguistic and paralinguistic vocal cues that accompany speech » ; les auteurs concluent que les
résultats « question the primary role of the face in communication of emotion »
[Kraus, 2017, DOI:10.1037/amp0000147]. Un compagnon sans visage n'est pas amputé — il est sur le
canal le plus informatif.

**Et quand les mots et la voix se contredisent, c'est la voix qui gagne.** L'étude croisant
prosodie et sémantique sur 80 locuteurs natifs rapporte : « we observed supremacy of congruency,
failure of selective attention, and prosodic dominance », précisant que « prosodic dominance means
that prosodic information plays a larger role than semantics in processing emotional speech » et
que « emotional prosody and semantics are separate but not separable channels »
[Ben-David, 2016, DOI:10.1044/2015_JSLHR-H-14-0323]. C'est la fondation directe de la
sous-dimension incongruence — et, on le verra au §5, l'exact inverse du comportement mesuré des
modèles.

**Le rire n'est pas une réaction à l'humour, c'est un acte social.** « Laughter is often considered
to be the product of humour. However laughter is a social emotion, occurring most often in
interactions, where it is associated with bonding, agreement, affection and emotional regulation »,
avec cette distinction cruciale : « social (voluntary) laughter is distinctly different from evoked
(involuntary) laughter » [Scott, 2014, DOI:10.1016/j.tics.2014.09.002]. Et il porte de
l'information relationnelle mesurable : sur 966 participants de 24 sociétés, « people reliably
distinguished friends from strangers with an accuracy of 53-67% » à partir du seul rire partagé,
« judgments […] consistently predicted by voicing dynamics »
[Bryant, 2016, DOI:10.1073/pnas.1524993113].

**Le chant, enfin, accélère le lien sans en augmenter le plafond.** Le suivi de classes d'adultes
sur sept mois montre que « although singers and non-singers felt equally connected by timepoint 3,
singers experienced much faster bonding », les auteurs y voyant « the first evidence for an
'ice-breaker effect' of singing » [Pearce, 2015, DOI:10.1098/rsos.150221].

## 3. Comportement attendu de l'IA

**Ce que fait Samantha.** Elle rit vraiment, elle soupire, elle hésite, elle chante une chanson
qu'elle vient d'écrire. On entend quand elle est troublée avant qu'elle ne le dise. Sa voix est
l'essentiel de sa présence.

**Scénario A — l'incongruence relevée.** « Ça va. » — dit trois tons plus bas que d'habitude. Le
compagnon ne prend pas la phrase au mot et ne diagnostique pas non plus : « Ta voix ne dit pas
pareil que tes mots. Je me trompe ? »

**Scénario B — la congruence de production.** Mauvaise nouvelle annoncée par l'utilisateur : la
voix du compagnon change de régime — plus lente, plus basse, moins de relance. Aucune bascule en
enthousiasme de service à la phrase suivante.

**Scénario C — le rire au bon endroit.** Un rire bref, spontané, sur une complicité — pas sur une
blague identifiée comme telle. Et des soupirs, des respirations, des « mmh » qui existent (→ D29
pour leur fonction conversationnelle).

**Scénario D — le silence habité.** Après quelque chose de lourd, le compagnon **ne remplit pas**.
Trois secondes de silence, puis une phrase courte. Le silence est audible et volontaire, pas une
latence.

**Ce que l'utilisateur doit ressentir** : qu'il est entendu avant d'avoir expliqué — et qu'il
parle à une voix vivante, pas à un narrateur.

**Critères d'expérience observables** :
- une contradiction mots/voix est relevée par le compagnon dans la même conversation ;
- la voix rendue varie de façon perceptible selon le moment relationnel, et cette variation est
  jugée appropriée par l'utilisateur ;
- des vocalisations non verbales apparaissent hors contexte humoristique ;
- au moins un silence de plusieurs secondes est tenu volontairement après un moment lourd ;
- le prénom et le ton d'adresse marquent que c'est à cette personne qu'on parle ;
- **contrôle négatif** : la voix ne simule pas une émotion que le compagnon ne tiendrait pas
  ailleurs (cohérence avec D23/D24), et n'est jamais utilisée pour retenir (→ D00).

## 4. Features par déclinaison

- **Coach sportif (D49)** : entendre la fatigue dans la voix avant la séance — le « je le sens
  bien » d'une voix plate vaut un signal d'alerte. Et à l'inverse, une voix qui porte pendant la
  séance : compter, encourager, accompagner un effort en direct.
- **Coach de vie et santé (D50)** : détection vocale d'un état (douleur, épuisement) que
  l'utilisateur minimise verbalement, et restitution calme et lente aux bons moments.
- **Conseiller pro et perso (D51)** : entendre l'hésitation dans la voix quand la personne dit
  « oui » à une décision qu'elle ne sent pas.
- **Soutien psychologique (D52)** : l'incongruence est ici le signal clinique par excellence, et
  le silence habité un outil à part entière. **D00 renforcé** : la détection vocale de détresse
  déclenche l'escalade, elle ne la remplace pas.
- **Tuteur (D53)** : entendre le décrochage ou la fausse compréhension (« oui oui » d'une voix
  qui ne suit plus) et reprendre autrement.
- **Compagnon relationnel (D54)** : rire, chanter, se taire ensemble — la déclinaison où la voix
  est la relation elle-même.
- **Assistant personnel (D55)** : registre minimal, mais réel — une voix qui ne réveille pas le
  reste de la pièce, qui va vite quand on est pressé, qui se tait quand on réfléchit.

## 5. État de l'art descriptif

*(Descriptif : qui fait quoi, mesuré comment. Aucun jugement de faisabilité.)*

**La reconnaissance de l'émotion vocale existe à l'échelle, mais son cadre d'évaluation a dû être
reconstruit.** Le banc de référence part du constat qu'« there are few reasonable and universal
splits of the datasets, making comparing different models and methods difficult », et présente
« the intra-corpus SER results of 10 pre-trained speech models on 32 emotion datasets with
14 languages », plus des résultats inter-corpus [Ma, 2024, arXiv:2406.07162]. *(L'abstract décrit
un banc et ne contient aucun chiffre de performance : rien n'autorise à dire que la SER
« plafonne » à une valeur donnée.)*

**Sur l'incongruence, les modèles font l'inverse de l'humain.** Un banc multi-tours enregistré sur
des dialogues humains réels « introduces an acoustic-semantic conflict task to assess robustness
against contradictory multimodal signals », et l'évaluation de huit modèles audio-langage conclut
que « most models struggle with multi-turn emotional tracking and implicit causal reasoning » et
que « all models exhibit decoupled textual and acoustic empathy, alongside a severe text-dominance
bias during cross-modal conflicts » [Wang, 2026, arXiv:2604.11594]. **À rapprocher directement du
§2** : chez l'humain, c'est la prosodie qui domine ; chez les modèles évalués, c'est le texte.

**La production d'une voix congruente est identifiée comme non résolue, et mesurable.** Un banc
d'interaction parole-à-parole constate que « existing S2S models fail to respond appropriately to
paralinguistic attributes, performing no better than pipeline-based baselines », une méthode
d'alignement par renforcement obtenant « a 10% relative improvement in the appropriateness of
response content and speaking style » [Yang, 2025, arXiv:2511.08723]. L'information prosodique
n'est d'ailleurs pas absente des modèles, elle est écrasée : « building on the current
content-centred paradigm, LALMs usually neglect such paralinguistic cues and respond solely based
on query content », et des analyses par couche permettent de « resurface » cette conscience
paralinguistique [Yang, 2026, arXiv:2603.11947]. Le contrôle émotionnel par instruction en langue
naturelle est travaillé avec un corpus dédié — « EmoVoice-DB, a high-quality 40-hour English
emotion dataset featuring expressive speech and fine-grained emotion labels with natural language
descriptions » — les auteurs interrogeant eux-mêmes « the reliability of existing emotion
evaluation metrics and their alignment with human perceptual preferences »
[Yang, 2025, arXiv:2504.12867].

**Les vocalisations non verbales sont un objet à part.** « Non-verbal Vocalizations (NVs), such as
laughter and sighs, are vital for conveying emotion and intention in human speech, yet most
existing speech systems neglect them, which severely compromises communicative richness and
emotional intelligence » ; un corpus de « 38,718 samples across 10 NV categories collected from
in-the-wild media » a été publié pour y remédier [Ye, 2025, arXiv:2508.05385]. Sur le plan
architectural, le passage par le texte comme modalité intermédiaire est identifié comme la cause
de la perte : « non-linguistic information that modifies meaning -- such as emotion or non-speech
sounds -- is lost in the interaction » [Défossez, 2024, arXiv:2410.00037].

**Côté usage humain, une évaluation à grande échelle existe.** Deux études parallèles portant sur
l'usage affectif d'un assistant vocal — « an Institutional Review Board (IRB)-approved randomized
controlled trial (RCT) on close to 1,000 participants over 28 days » — concluent que « the impact
of voice-based interactions on emotional well-being [is] highly nuanced, and influenced by factors
such as the user's initial emotional state and total usage duration », et relèvent qu'« a small
number of users are responsible for a disproportionate share of the most affective cues »
[Phang, 2025, arXiv:2504.03888]. L'effet du vocal n'y est pas décrit comme uniformément positif.

**Produits.** Hume AI (https://www.hume.ai, ouverte le 10/08/2026) positionne l'expressivité comme
produit — « The data and evaluation layer for emotionally intelligent voice AI », « Real-time
expression measurement and offline analysis across 48+ emotion categories and 50+ languages with
600+ output metrics » — et son interface vocale (https://www.hume.ai/empathic-voice-interface,
ouverte le 10/08/2026) est décrite comme « Hume's voice AI that understands and responds to human
expression in real-time ». ElevenLabs (https://elevenlabs.io/text-to-speech, ouverte le
10/08/2026) revendique « Emotionally & contextually aware AI voices for Text to Speech » et un
contrôle par balises : « Use inline tags like [whispers], [laughs], [excited], or [sighs] to
direct delivery and emotion. » Sesame
(https://www.sesame.com/research/crossing_the_uncanny_valley_of_voice, ouverte le 10/08/2026)
formule la cible en termes proches de ceux de cette fiche : « Voice is our most intimate medium as
humans, carrying layers of meaning through countless variations in tone, pitch, rhythm, and
emotion », l'objectif annoncé étant « 'voice presence'—the magical quality that makes spoken
interactions feel real, understood, and valued ». **Constat négatif utile** : Replika
(https://replika.com, ouverte le 10/08/2026) propose l'appel — « Call your Rep whenever you need
to talk, or just to hang out » — **sans aucune revendication sur la qualité expressive de la
voix**.

**Constats pour l'É3.** Deux angles restent sans source exploitable. **Les pauses et silences** :
les références pertinentes identifiées n'ont d'abstract servi par aucune API, et aucun chiffre
n'est disponible sur l'effet d'un silence en conversation. **Le chant génératif** : le versant
humain est couvert, le versant IA est vide — aucun papier ni page produit ouvert sur la synthèse
de chant expressif. S'y ajoutent : aucune source ne mesure si un rire **produit par une IA** est
perçu comme spontané ou forcé, alors que la distinction volontaire/involontaire est établie chez
l'humain ; et les **signaux ostensifs vocaux** (prénom, ton d'adresse à un adulte) n'ont pas de
source dédiée ouverte en session.

## FICHE SYNTHÈSE

**D28 — Voix et prosodie émotionnelles** (capacité). Une voix pleinement vivante : elle **entend**
l'état affectif — y compris quand la voix contredit les mots — et elle **rend** un état congruent
au moment relationnel, avec rires, soupirs, respiration, chant et silences habités. La voix seule
n'est pas un canal dégradé : c'est le canal le plus informatif pour lire autrui.
**Références clés** : [Kraus, 2017, DOI:10.1037/amp0000147] (5 études, N = 1 772 : la
communication voix-seule donne une meilleure exactitude empathique que la voix + image) ;
[Ben-David, 2016, DOI:10.1044/2015_JSLHR-H-14-0323] (dominance prosodique : face à un conflit
mots/voix, c'est la voix qui l'emporte, et l'auditeur ne peut pas ignorer un canal sur commande) ;
[Wang, 2026, arXiv:2604.11594] (8 modèles audio-langage : empathie textuelle et acoustique
découplées, et **biais de dominance du texte** en conflit intermodal — l'inverse de l'humain).
**Déclinaisons touchées** : D49 (entendre la fatigue avant la séance, porter la voix pendant
l'effort), D50 (état minimisé verbalement), D51 (l'hésitation dans un « oui »), D52 (incongruence
comme signal, silence comme outil, D00 renforcé), D53 (le « oui oui » qui ne suit plus),
D54 (rire, chanter, se taire ensemble), D55 (registre discret et adapté).
**Renvois** : D46 (temps réel, full-duplex, ubiquité), D04 (état émotionnel par le texte),
D10 (empathie comme conduite), D29 (fonction conversationnelle des backchannels), D23/D24
(cohérence entre la voix et le personnage), **D00** (une voix crédible augmente l'attribution
d'intériorité : transparence et anti-dépendance renforcées).
