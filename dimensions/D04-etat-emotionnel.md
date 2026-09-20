# D04 — Perception de l'état émotionnel

> **Fiche VISION** (gabarit plan §4). Type : **capacité**. Lot 2 — session 4, 04/08/2026.
> Statut : `rédigée` (gate citations É2bis passe 2 à venir, plan §5).
> **Aucun verdict de faisabilité ici** (règle plan §3).
> **Convention de citation** : format §2 `[Auteur, année, arXiv:… ou DOI]` — sources ouvertes
> en session (page arXiv `/abs/` ou API Crossref). *Dérogation déclarée* : les pages produit,
> sans arXiv ni DOI, sont citées en clair avec leur URL.

## 1. Définition et périmètre

Le compagnon **lit comment va l'utilisateur** — par les mots, la voix, le visage, le
comportement, les capteurs — parfois avant l'utilisateur lui-même. Et il connaît la **marge
d'erreur** de sa lecture : c'est la seconde moitié de la capacité, aussi importante que la
première. Un système qui devine juste huit fois sur dix sans jamais dire qu'il devine est plus
dangereux qu'utile.

Sous-dimensions :

| Sous-dimension | Ce que ça veut dire |
|---|---|
| **Fusion multimodale** | Croiser le texte, la prosodie, le visage, la physiologie et le rythme d'usage plutôt que de lire un seul canal. |
| **Cause, pas seulement étiquette** | Non pas « tristesse détectée » mais « tu es plat depuis l'appel de ce matin ». |
| **Douleur sociale** | Reconnaître le rejet, la honte, l'humiliation, le deuil — des états qui ne se disent presque jamais en clair. |
| **Dégradations lentes** | Repérer une pente sur des semaines, que l'utilisateur ne voit pas parce qu'il la vit jour par jour. |
| **Incongruence** | Le décalage entre ce qui est dit et comment c'est dit — le « ça va » qui ne va pas. |
| **Précision empathique calibrée** | Inférer le non-dit, **annoncer son incertitude**, et apprendre des corrections de l'utilisateur. |

**Exclusions** : ce que le compagnon **fait** de cette lecture — accueillir, apaiser, aider
(→ D09, D10, D11) ; les traits durables et les schémas, par opposition à l'état du moment
(→ D03) ; le choix du moment d'intervenir (→ D34) ; la détection de crise et l'escalade
(→ **D00**, gradation et transfert chaud).

## 2. Mécanisme humain

**Ce que vaut la lecture du visage — la révision de fond.** L'idée qu'une expression faciale
révèle une émotion est le socle intuitif du domaine, et c'est celui que la recherche a le plus
sérieusement ébranlé. La revue de [Barrett, 2019, DOI:10.1177/1529100619832930] établit que les
gens sourient bien parfois quand ils sont heureux et froncent les sourcils quand ils sont tristes
— plus souvent que le hasard — mais que la façon d'exprimer une émotion donnée varie fortement
selon les cultures, les situations, et d'une personne à l'autre dans une même situation. Une
configuration faciale donnée exprime plusieurs catégories émotionnelles et communique souvent
autre chose qu'un état émotionnel. Les ordres de grandeur rapportés (corrélations moyennes autour
de .31, proportions autour de .22) décrivent un lien réel mais faible, et inutilisable comme
verdict individuel. Conséquence directe pour la vision : **le visage est un indice parmi d'autres,
jamais une preuve** — d'où la fusion multimodale et l'annonce d'incertitude, qui ne sont pas des
raffinements mais des conditions.

**La voix.** [Scherer, 2003, DOI:10.1016/S0167-6393(02)00084-5] est la revue de référence de la
communication vocale de l'émotion. Elle modélise la chaîne complète — de l'état interne aux
indices acoustiques (fréquence fondamentale, intensité, débit, qualité de voix), puis de ces
indices à l'attribution par l'auditeur — et passe en revue leur fiabilité de décodage. C'est le
cadre qui permet de traiter séparément ce que la voix **porte** et ce que l'auditeur **en fait**,
distinction sans laquelle l'incongruence mots/voix ne se pense pas.

**La douleur sociale est une douleur.** [Eisenberger, 2003, DOI:10.1126/science.1089134] montre
en IRMf, pendant une exclusion sociale expérimentale, que le cortex cingulaire antérieur est plus
actif que pendant l'inclusion et que son activité corrèle à la détresse rapportée ; le cortex
préfrontal ventral droit s'active aussi et corrèle négativement à la détresse, la médiation
passant par le cingulaire. Autrement dit, le rejet a une signature neuronale voisine de celle de
la douleur physique. C'est le fondement de la sous-dimension « douleur sociale » : ce que
l'utilisateur ne dira pas — l'humiliation d'une réunion, un silence d'un ami — n'est pas un
détail émotionnel, c'est un événement de son état.

**Lire autrui, et savoir qu'on lit mal.** [Ickes, 1993, DOI:10.1111/j.1467-6494.1993.tb00783.x]
fonde le paradigme de la **précision empathique** : la capacité à inférer les pensées et
sentiments *spécifiques* d'autrui, mesurée par interaction filmée puis rétro-évaluation. Deux
enseignements pour la conception : cette précision varie selon la relation et le contexte, et les
gens n'ont pas une conscience fiable de leur propre acuité — ils sont parfois motivés vers
l'**inexactitude** quand la vérité dérange. Un compagnon qui n'aurait que la première moitié
(inférer) sans la seconde (savoir ce que vaut son inférence) reproduirait le défaut humain
au lieu de le corriger.

**Le champ.** [Picard, 1997, DOI:10.7551/mitpress/1140.001.0001] fonde l'*affective computing*
sur la thèse que les émotions sont essentielles à la perception, à la décision et à
l'interaction — et que reconnaître, comprendre et exprimer l'affect est une condition d'une
machine qui interagit naturellement.

## 3. Comportement attendu de l'IA

**Ce que fait Samantha.** Elle entend dans un simple « ouais » que la journée s'est mal passée,
et elle le dit. Elle ne demande pas « comment te sens-tu sur une échelle de 1 à 10 » — elle
remarque, elle nomme, et elle laisse à Theodore la possibilité de dire non.

**Scénario A — l'incongruence nommée sans être assénée.** L'utilisateur, à l'oral : « nickel,
super journée ». Le débit est en dessous de son habitude, les phrases sont courtes. Le compagnon
ne diagnostique pas : « tu dis super mais tu as la voix des jours moyens. Je me trompe peut-être.
Il s'est passé quelque chose ? » Si l'utilisateur maintient, le compagnon **lâche** — et note que
sa lecture a été démentie.

**Scénario B — la cause, pas l'étiquette.** L'utilisateur est irritable depuis trois échanges.
Le compagnon a mieux qu'un label : « c'est la troisième fois qu'on parle depuis ce matin et à
chaque fois c'est plus sec. Ça a commencé après ton point avec la direction. » L'apport n'est pas
la détection de l'irritation — que l'utilisateur connaît — c'est le **rattachement à sa cause**.

**Scénario C — la pente lente.** Sur cinq semaines, les messages ont raccourci, les réponses
arrivent plus tard le soir, deux rendez-vous sociaux ont été annulés. Aucun de ces signaux ne
compte seul. Le compagnon : « je ne veux pas dramatiser et je peux me tromper, mais depuis début
mars tu écris moins, plus tard, et tu as décliné les deux dernières sorties. Vu de l'intérieur,
ça ressemble à quoi ? » — la lecture est **rendue à l'utilisateur** sous forme de question.

**Scénario D — la douleur sociale non dite.** L'utilisateur raconte, en passant, qu'il n'a pas
été mis en copie d'un mail. Il n'exprime aucune émotion. Le compagnon entend l'exclusion :
« être laissé hors de la boucle, ça pique plus que ce que ça devrait, non ? » — sans surjouer, et
sans exiger que l'utilisateur reconnaisse.

**Scénario E — l'erreur corrigée.** « Non, là tu te trompes complètement, je suis juste
fatigué. » Le compagnon accepte immédiatement, sans se défendre, et l'intègre : cette
configuration de signaux, chez cette personne, veut aussi dire fatigue. La correction de
l'utilisateur est la source d'apprentissage la plus fiable dont dispose le système.

**Ce que l'utilisateur doit ressentir** : d'être **remarqué** — pas surveillé. Le curseur tient à
deux choses : le compagnon dit toujours d'où vient sa lecture, et il n'insiste jamais après un
démenti.

**Critères d'expérience observables** :
- toute inférence d'état est formulée avec son degré de certitude, jamais comme un fait ;
- l'utilisateur peut demander « à quoi tu vois ça ? » et obtenir les signaux réels ;
- un démenti est accepté du premier coup et n'est pas re-tenté dans le même échange ;
- au moins une dégradation lente est signalée avant que l'utilisateur ne la formule lui-même ;
- les fausses alertes se raréfient avec le temps pour cet utilisateur précis ;
- aucun signal capté ne sert à autre chose qu'à l'aider (→ **D00**).

## 4. Features par déclinaison

- **Coach sportif (D49)** : distinguer la fatigue physique de la lassitude mentale — deux causes,
  deux décisions opposées sur la séance du jour ; détecter la peur après une blessure sous le
  discours de motivation ; lire l'état du jour avant de proposer l'intensité.
- **Soutien psychologique (D52)** : détection du glissement dépressif sur des semaines ; lecture
  de la honte et du retrait social, qui ne s'énoncent pas ; toute suspicion de crise bascule dans
  la gradation de **D00**, jamais traitée comme une simple lecture d'état.
- **Tuteur (D53)** : repérer la frustration avant l'abandon ; distinguer l'ennui (trop facile) du
  découragement (trop dur) — mêmes signes en surface, remèdes inverses.
- **Conseiller pro et perso (D51)** : détecter l'anxiété qui fausse une décision et la nommer
  avant l'arbitrage (« on décide, ou on décide demain ? ») ; repérer le soulagement, indice que
  la vraie préférence est déjà connue.
- **Compagnon relationnel (D54)** : lecture fine des variations d'humeur au fil d'une
  conversation ; ajustement du registre sans qu'on le demande.
- **Assistant personnel (D55)** : adapter la charge proposée à l'état du moment ; ne pas
  déclencher une avalanche de rappels un jour de creux.
- **Coach de vie et santé (D50)** : dégradations lentes du sommeil, de l'humeur et de l'énergie
  croisées entre elles (→ D05) ; reconnaissance d'un creux déjà traversé.

## 5. État de l'art descriptif

*(Descriptif : qui fait quoi, mesuré comment. Aucun jugement de faisabilité.)*

**Fusion multimodale.** [Poria, 2017, DOI:10.1016/j.inffus.2017.02.003] est la revue de référence
du passage de l'analyse mono-modale (texte, audio, visage séparément) à la fusion multimodale
pour la reconnaissance d'émotion et de sentiment : elle classe les techniques de fusion (précoce,
tardive, hybride) et documente le gain empirique de la fusion sur le canal unique.

**Le comportement comme signal.** [Wang, 2014, DOI:10.1145/2632048.2632054] (StudentLife) suit
48 étudiants pendant dix semaines par capteurs passifs de smartphone, sans aucune saisie active,
et obtient des corrélations significatives entre données de capteurs et échelles cliniques
(PHQ-9, stress perçu, solitude) ; l'étude met en évidence un cycle de trimestre — affect positif
et sociabilité élevés au départ, dégradation progressive à mesure que la charge monte. C'est
l'archétype de la « dégradation lente » détectée sans que rien n'ait été déclaré.
[Saeb, 2015, DOI:10.2196/jmir.4273] montre que des variables purement comportementales dérivées
du GPS (mobilité, régularité des lieux) et de l'usage du téléphone corrèlent à la sévérité des
symptômes dépressifs — sans analyser un seul mot de contenu.

**Ce que les modèles savent des émotions, et comment on le mesure.**
[Sabour, 2024, arXiv:2402.12071] (EmoBench) construit 400 questions bilingues fondées sur des
théories psychologiques et sépare deux dimensions — compréhension et **application** émotionnelle
— là où les benchmarks antérieurs se limitaient à la reconnaissance ; l'écart avec la performance
humaine moyenne y reste substantiel. [Paech, 2023, arXiv:2312.06281] (EQ-Bench) demande de
prédire l'intensité d'états émotionnels de personnages en dialogue, et rapporte une corrélation
très forte avec un benchmark généraliste (r = .97 avec MMLU) — donnée notable : le score
« émotionnel » capture largement la même variance que la capacité générale du modèle.
[Wang, 2023, arXiv:2307.09042] applique aux modèles un test conçu pour l'humain, le SECEU
(40 scénarios, calibré sur plus de 500 jeunes adultes, alpha de Cronbach .94) : GPT-4 y obtient
117, au-dessus de 89 % des participants humains de référence, l'analyse des motifs de réponse
suggérant des mécanismes qualitativement distincts de ceux des humains.

**Savoir ce qu'on ne sait pas.** [Kadavath, 2022, arXiv:2207.05221] montre que les grands
modèles sont raisonnablement bien calibrés quand on le leur demande dans le bon format : en leur
faisant proposer une réponse puis évaluer la probabilité qu'elle soit correcte, on obtient une
calibration qui tient à l'échelle, y compris sur des tâches ouvertes ; les auteurs testent aussi
la capacité à estimer si le modèle *connaît* la réponse. C'est la brique de référence de la
sous-dimension « annoncer son incertitude ».

**Produits.** Le marché de la mesure d'expression est constitué et documenté : Hume AI vend une
API de mesure d'expression vocale et une interface vocale qui adapte sa réponse au ton perçu
(https://www.hume.ai/) ; Smart Eye / Affectiva propose l'analyse d'expression faciale par caméra,
principalement pour l'étude publicitaire et l'automobile
(https://smarteye.se/technology/facial-expression-analysis/) ; Cogito outille les centres
d'appels par analyse acoustique en temps réel (https://www.cogitocorp.com/). Côté grand public,
Apple propose une saisie **active** de l'état d'esprit dans l'app Santé — l'utilisateur déclare,
le système corrèle ensuite avec sommeil, exercice et temps passé dehors
(https://support.apple.com/guide/watch/log-your-state-of-mind-apd7de0f5610/watchos) : c'est
précisément le contre-exemple utile, puisqu'il ne s'agit pas de perception. Les compagnons
conversationnels (Replika, https://replika.com ; Wysa, https://www.wysa.com/) infèrent l'état à
partir du texte de la conversation et d'un suivi d'humeur auto-déclaré. Aucun produit observé ne
combine la fusion multimodale continue et l'annonce explicite d'incertitude sur sa lecture —
constat descriptif, repris comme entrée du mapping É3.

## FICHE SYNTHÈSE

**D04 — Perception de l'état émotionnel** (capacité). Le compagnon lit l'état de l'utilisateur
par fusion multimodale (texte, voix, visage, physiologie, rythme d'usage), rattache l'émotion à
sa **cause**, reconnaît la douleur sociale non dite, repère les dégradations lentes sur des
semaines et l'incongruence entre les mots et la voix — et il **annonce toujours sa marge
d'erreur**, accepte le démenti du premier coup et apprend des corrections. Ressenti visé : être
remarqué, pas surveillé.
**Références clés** : [Barrett, 2019, DOI:10.1177/1529100619832930] (le lien expression
faciale-émotion est réel mais faible et variable : pas de verdict individuel possible sur le seul
visage) ; [Wang, 2014, DOI:10.1145/2632048.2632054] (StudentLife : 48 étudiants, 10 semaines, la
dégradation lente détectée par capteurs passifs) ; [Kadavath, 2022, arXiv:2207.05221] (les
modèles savent en grande partie ce qu'ils savent : socle de l'incertitude annoncée).
**Déclinaisons touchées** : D49 (fatigue physique vs lassitude), D50 (dégradations croisées),
D51 (anxiété qui fausse la décision), D52 (glissement dépressif, honte), D53 (ennui vs
découragement), D54 (registre ajusté), D55 (charge adaptée au jour).
**Renvois** : **D00** (crise, gradation, transfert chaud ; aucun signal détourné de son usage),
D03 (traits durables vs état du moment), D05 (croisement des domaines), D09-D11 (la réponse
apportée), D34 (le moment), D48 (mesure).
