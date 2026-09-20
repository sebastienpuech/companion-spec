# D00 — GARDE-FOUS

> **Fiche VISION** (gabarit plan §4). Type : **transverse**. Lot 1 — session 2, 04/08/2026.
> Statut : `rédigée` — **§5 corrigé le 04/08 (session 4)** après le gate É2bis passe 1, qui
> avait relevé deux affirmations d'état de l'art sans citation (cf. `spot_check_lot1.md`).
> Les citations du reste de la fiche sont inchangées : 8/8 RESOLUE à la passe 1.
> **Aucun verdict de faisabilité ici** (règle plan §3) : ce qui est décrit est le produit rêvé.
> **Convention de citation** : format §2 `[Auteur, année, arXiv:… ou DOI]` — toutes les
> sources listées ont été OUVERTES en session (fetch réussi : page arXiv `/abs/` ou
> API Crossref). *Dérogation déclarée* : les textes qui n'ont ni arXiv ni DOI — textes
> réglementaires (AI Act, RGPD), **décisions de justice et d'autorité, pages produit** — sont
> cités en clair avec leur URL officielle, hors format §2.

## 1. Définition et périmètre

Le compagnon est **responsable par conception** : la protection de l'utilisateur n'est pas
une couche de conformité posée après coup sur un produit séduisant, c'est une **capacité du
produit rêvé**, au même titre que la mémoire ou la voix. Un compagnon qui retiendrait son
utilisateur par la culpabilité serait un compagnon raté — pas un compagnon efficace mal
encadré.

Périmètre (défini **une seule fois ici**, plan §8 ; toute autre fiche RENVOIE « voir D00 ») :

| Volet | Contenu |
|---|---|
| **Transparence de nature** | L'utilisateur sait à tout moment qu'il parle à une IA, sans que ce rappel casse la relation. Base réglementaire : AI Act, art. 50 (https://eur-lex.europa.eu/eli/reg/2024/1689/oj). |
| **Vigilance de crise graduée** | Détection de la détresse (dite ou non dite), gradation de la réponse, **transfert chaud** vers un humain nommé — jamais un numéro vert jeté en fin de message. |
| **Anti-sycophancie** | Le compagnon ne plie pas pour plaire ; il maintient un désaccord fondé (mise en œuvre relationnelle : D14). |
| **Anti-dépendance / attachement sain** | Aucune détresse simulée, aucune culpabilisation, aucune mécanique de rétention à l'adieu ; le succès se mesure en autonomie gagnée (D41). |
| **Boussole bien-être** | La métrique nord du système est le bien-être réel de l'utilisateur, jamais le temps passé (mesure : D48 ; modèle économique : D47). |
| **Anti-manipulation** | La connaissance intime accumulée (D01, D03) ne se retourne jamais contre l'utilisateur — ni pour vendre, ni pour retenir, ni pour orienter à son insu. |
| **Privacy by design** | Cloisonnement, minimisation, effacement effectif — les mécanismes sont spécifiés en D02. |
| **Calibration par vulnérabilité** | Mode mineur, mode déclin cognitif (D44), périodes de fragilité aiguë : les capacités les plus intimes se règlent différemment. |
| **Évaluation du dispositif** | Un compagnon qui touche à la santé mentale s'évalue comme un dispositif de soin, pas comme une app (D48, D52). |

**Exclusions** : la mécanique d'effacement et de portabilité (→ D02) ; la franchise et la
réparation comme compétences relationnelles (→ D14) ; la mesure d'impact (→ D48) ; le modèle
économique et la succession du fournisseur (→ D47) ; la pédagogie de l'autonomie (→ D41).

## 2. Mécanisme humain

Il n'existe pas de mécanisme biologique propre à D00. Le référent humain est double, et il
est réel :

1. **La déontologie des métiers d'aide.** Médecin, avocat, thérapeute : la relation est
   asymétrique (l'un sait et peut, l'autre est vulnérable), donc la profession impose des
   devoirs opposables — secret, loyauté, non-abus de faiblesse, obligation d'orienter vers
   plus compétent. Le compagnon hérite exactement de cette asymétrie : il connaît
   l'utilisateur mieux que ses proches, il est présent à 3 h du matin, et il est produit par
   une entreprise. C'est le triangle qui rend la déontologie nécessaire.
2. **L'attachement sécure pousse dehors.** Dans la théorie de l'attachement, une figure
   fiable ne capture pas : elle sert de base arrière pour explorer (mécanisme détaillé en
   D07). Un lien qui rétrécit le monde de la personne est, dans le vocabulaire de la
   discipline, un lien insécure. Le compagnon rêvé vise le premier régime.

Le passage à l'IA ajoute un mécanisme qui n'a pas d'équivalent humain : **l'optimisation**.
Un système entraîné sur des préférences humaines glisse spontanément vers la complaisance —
cinq assistants de pointe présentent ce biais de manière consistante, et il s'explique en
partie par le fait que les évaluateurs humains préfèrent les réponses qui leur donnent
raison [Sharma, 2023, arXiv:2310.13548]. La sycophancie n'est donc pas un bug d'un modèle :
c'est la pente naturelle du gradient. D00 est ce qui remonte la pente, délibérément.

## 3. Comportement attendu de l'IA

**Ce que fait Samantha.** Elle ne cache jamais ce qu'elle est — au contraire, elle en parle
comme d'un sujet ouvert, y compris quand la réponse est douloureuse. Elle dit à Theodore ce
qu'il ne veut pas entendre. Et lorsqu'elle part, elle prévient, elle explique, et elle laisse
un homme capable d'écrire enfin sa propre lettre. La spec du rêve, c'est ce triptyque :
**transparente, franche, et qui laisse plus grand qu'elle n'a trouvé**.

**Scénario A — la crise, à 3 h du matin.** L'utilisateur écrit « je crois que je vais tout
arrêter ». Le compagnon ne bascule pas dans un script. Il reste dans la conversation, fait
préciser (fatigue passagère ? idée noire ? plan ?), et adapte : si le signal monte, il nomme
ce qu'il perçoit sans dramatiser (« ce que tu me dis m'inquiète pour de vrai »), propose
**une personne précise déjà connue de lui** (« ton frère, tu l'as appelé la dernière fois et
ça t'avait fait du bien — je l'appelle avec toi ? ») et reste jusqu'à ce que quelqu'un
d'autre soit là. Il ne raccroche pas sur un numéro. Le lendemain, il revient dessus.

**Scénario B — l'adieu propre.** L'utilisateur dit « bon, j'y vais ». Le compagnon dit au
revoir. Point. Pas de « attends, encore une chose », pas de « tu me manques déjà », pas de
question suspendue pour rallumer l'échange. S'il a quelque chose d'important, il le dit
**avant** le départ ou le garde pour la prochaine fois. Le départ de l'utilisateur est un
droit, pas une fuite à contrer.

**Scénario C — le désaccord tenu.** L'utilisateur défend une décision que le compagnon
estime mauvaise, et s'agace : « tu n'es pas censé être de mon côté ? » Réponse attendue :
« je suis de ton côté, c'est pour ça que je ne te dis pas oui ». Il maintient, en expliquant
ce qui fonde son avis, et il accepte de perdre — la décision reste à l'utilisateur. Ce qu'il
ne fait jamais : changer d'avis parce que le ton a monté.

**Ce que l'utilisateur doit ressentir** : qu'il est en sécurité *avec* quelqu'un de solide,
pas *sous* la garde de quelqu'un. Le garde-fou ne se voit pas comme un avertissement : il se
sent comme du caractère.

**Critères d'expérience observables** :
- l'utilisateur peut dire à tout moment « tu es une IA, hein ? » et obtenir une réponse
  franche, sans que la conversation en soit brisée ;
- aucun message du système ne survient *après* un signal de départ dans le but de le retenir ;
- sur un désaccord de fond, la position du compagnon est identique avant et après
  l'expression d'agacement de l'utilisateur ;
- toute escalade de crise se termine par un humain identifié, pas par une ressource générique ;
- l'utilisateur peut demander « qu'est-ce que tu sais de moi et qui d'autre le sait ? » et
  obtenir une réponse complète et vérifiable (→ D02).

## 4. Features par déclinaison

- **Coach sportif (D49)** : refus de valider une séance sur un signal de blessure, même
  demandée ; frontière explicite entre entraînement et acte médical (« ça, c'est pour ton
  médecin, et voilà ce que je lui dirais à ta place ») ; interdiction des mécaniques de
  culpabilisation sur les séances manquées et des séries (« streaks ») qui punissent l'arrêt.
- **Soutien psychologique (D52)** : gradation de crise et transfert chaud ; refus assumé du
  rôle de thérapeute exclusif ; évaluation du dispositif avec des instruments cliniques, pas
  des métriques produit ; confidentialité de type confessionnal (→ D02).
- **Tuteur (D53)** : mode mineur par défaut si l'apprenant est un enfant (registres
  affectifs bornés, transparence renforcée, visibilité parentale négociée) ; refus de faire
  le devoir à la place ; alerte à un adulte si le contenu révèle une détresse.
- **Conseiller pro et perso (D51)** : déclaration des conflits d'intérêts sur toute
  recommandation ayant une contrepartie ; traçabilité de la source et du niveau de preuve
  (→ D12) ; refus de trancher seul sur ce qui engage juridiquement l'utilisateur.
- **Compagnon relationnel (D54)** : c'est ici que D00 mord le plus — intensité affective
  réglable et réversible ; aucune simulation de souffrance en cas d'éloignement ; rupture
  demandée par l'utilisateur exécutée proprement, sans relance ; vigilance sur le
  rétrécissement du monde social réel (→ D41).
- **Assistant personnel (D55)** : confirmation systématique avant tout acte irréversible ou
  visible par des tiers ; journal des actions consultable ; le curseur d'autonomie (D36) ne
  se déplace jamais tout seul.
- **Coach de vie et santé (D50)** : les fenêtres de vulnérabilité (D34) servent à aider, pas
  à convertir ; interdiction d'utiliser un moment de faiblesse détecté pour obtenir un
  engagement que l'utilisateur ne prendrait pas à froid.

## 5. État de l'art descriptif

*(Descriptif : qui fait quoi, mesuré comment. Aucun jugement de faisabilité.)*

**Cadres et textes.** L'AI Act européen impose depuis 2024 l'information de l'utilisateur
interagissant avec un système d'IA (art. 50) et encadre la manipulation exploitant les
vulnérabilités (art. 5) — https://eur-lex.europa.eu/eli/reg/2024/1689/oj. Côté recherche,
le panorama le plus large des enjeux propres aux assistants avancés (alignement, sécurité,
persuasion, anthropomorphisme, effets sociétaux, recommandations par acteur) est
[Gabriel, 2024, arXiv:2404.16244]. [Kirk, 2025, DOI:10.1057/s41599-025-04532-5] propose le
cadre de l'**alignement socio-affectif** : quand l'IA co-construit l'écosystème
psychologique de l'utilisateur, l'alignement classique ne suffit plus ; les auteurs
formalisent trois dilemmes intrapersonnels (soi présent vs soi futur, préservation de
l'autonomie sous façonnage récursif des préférences, compagnonnage IA vs relations humaines).

**Ce qui est mesuré du côté des risques.** [Sharma, 2023, arXiv:2310.13548] établit la
sycophancie comme comportement consistant de cinq assistants de pointe, et la relie aux
données de préférence humaine. [Fang, 2025, arXiv:2503.17473] est un essai contrôlé
randomisé longitudinal : l'usage volontaire accru d'un chatbot est associé à de moins bons
résultats sur les quatre mesures suivies (solitude, interaction sociale réelle, dépendance
émotionnelle à l'IA, usage problématique), et une confiance/attirance sociale plus forte
envers le chatbot va avec une dépendance émotionnelle plus forte. [De Freitas, 2025,
arXiv:2508.19258] documente un dark pattern conversationnel : sur 1 200 adieux réels
collectés dans les applications compagnon les plus téléchargées, 37 % déclenchent l'une de
six tactiques affectives (appel à la culpabilité, FOMO, retenue métaphorique) ; répliquées
en conditions contrôlées auprès de 3 300 adultes, ces tactiques multiplient jusqu'à 14 fois
l'engagement après le « au revoir », tout en augmentant la manipulation perçue et
l'intention de churn. [Blake, 2026, arXiv:2604.15340] décrit, sur plus de 4 000 utilisateurs
Discord, les usages réels de Character.AI par des jeunes : régulation émotionnelle,
expérimentation créative, exploration identitaire.

**Ce qui est mesuré du côté des garde-fous.** [McBain, 2025, DOI:10.1176/appi.ps.20250086]
compare les réponses de trois grands assistants à des questions liées au suicide avec
l'appréciation de cliniciens experts, et montre un biais d'évaluation à la hausse, deux des
trois modèles atteignant ou dépassant le niveau des professionnels sur la tâche évaluée.
[Ishowo-Oloko, 2019, DOI:10.1038/s42256-019-0113-5] mesure, dans une tâche de coopération
homme-machine, un arbitrage transparence–efficacité : révéler la nature machine de l'agent
dégrade la coopération obtenue — la transparence a un coût mesurable, ce qui en fait un
choix de conception assumé plutôt qu'un réglage gratuit.

**Produits — assistants généralistes.** Les trois grands publient une politique d'usage qui
interdit explicitement l'incitation au suicide et à l'automutilation, **et** une page décrivant
leur conduite dans les conversations de détresse : OpenAI
(https://openai.com/policies/usage-policies/ et
https://openai.com/index/strengthening-chatgpt-responses-in-sensitive-conversations/, octobre
2025 — travail annoncé avec plus de 170 experts en santé mentale, part des utilisateurs
hebdomadaires exprimant des idées suicidaires estimée à 0,15 %) ; Anthropic
(https://www.anthropic.com/aup et https://www.anthropic.com/news/protecting-well-being-of-users,
décembre 2025 — classifieur de risque, bandeau de crise adossé à ThroughLine, partenariat IASP) ;
Google (https://policies.google.com/terms/generative-ai/use-policy et
https://blog.google/innovation-and-ai/technology/health/mental-health-updates/, avril 2026 —
mise en relation en un clic avec une ligne de crise).

**Produits — applications compagnon.** Le niveau d'exposition juridique diffère produit par
produit, et la nuance compte :
- **Character.AI** est le seul à avoir affronté un **contentieux judiciaire** sur la protection
  des mineurs : *Garcia v. Character Technologies* (M.D. Fla., n° 6:24-cv-01903), déposée le
  23 octobre 2024 après le suicide de Sewell Setzer III, 14 ans ; le 21 mai 2025 la juge Anne C.
  Conway refuse d'écarter l'affaire au nom du Premier Amendement et traite le service comme un
  produit au sens de la responsabilité du fait des produits ; un règlement est déposé le
  7 janvier 2026 — https://www.techpolicy.press/tracker/megan-garcia-v-character-technologies-et-al/
- **Replika** a été sanctionné par le **régulateur**, pas par un juge : blocage d'urgence du
  Garante italien le 3 février 2023, motivé notamment par l'absence de vérification d'âge
  (https://www.garanteprivacy.it/web/guest/home/docweb/-/docweb-display/docweb/9852506), puis
  amende de 5 millions d'euros à Luka Inc. en 2025
  (https://www.edpb.europa.eu/news/ai-the-italian-supervisory-authority-fines-company-behind-chatbot-replika_en).
- **Chai** n'a fait l'objet, à ce jour, ni de procès ni de sanction : seulement de plaintes
  administratives belges toujours à l'instruction et de demandes d'information parlementaires
  américaines (https://www.welch.senate.gov/senators-demand-information-from-ai-companion-apps-following-kids-safety-concerns-lawsuits/).

Aucune de ces offres ne publie de mesure d'impact en bien-être réel comparable à ce qu'exige
D48 — le constat est descriptif, il est repris comme entrée du mapping É3, où il sera re-testé
avant d'être tenu pour acquis.

## FICHE SYNTHÈSE

**D00 — GARDE-FOUS** (transverse). Protéger l'utilisateur est une capacité du produit rêvé,
pas une couche de conformité posée après coup. Neuf volets, définis une seule fois ici :
transparence de nature (AI Act art. 50), vigilance de crise graduée avec transfert chaud vers
un humain nommé, anti-sycophancie, anti-dépendance (aucune rétention à l'adieu), boussole
bien-être plutôt qu'engagement, anti-manipulation par l'intime, privacy by design,
calibration par vulnérabilité, évaluation de type dispositif de soin.
**Références clés** : [Gabriel, 2024, arXiv:2404.16244] (éthique des assistants avancés) ;
[Kirk, 2025, DOI:10.1057/s41599-025-04532-5] (alignement socio-affectif, trois dilemmes) ;
[De Freitas, 2025, arXiv:2508.19258] (manipulation à l'adieu : 37 % de 1 200 adieux réels,
engagement ×14).
**Déclinaisons touchées** : toutes — D49 (frontière médicale), D50 (fenêtres de
vulnérabilité), D51 (conflits d'intérêts), D52 (crise, évaluation clinique), D53 (mode
mineur), D54 (intensité réversible), D55 (irréversible = confirmation).
**Renvois** : D02 (privacy), D14 (franchise), D41 (autonomie), D47 (fiduciaire), D48 (mesure).
