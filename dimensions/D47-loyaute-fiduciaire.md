# D47 — Loyauté fiduciaire

> **Fiche VISION** (gabarit plan §4). Type : **transverse**. Lot 8 — session 16, 13/08/2026.
> Statut : `rédigée` (gate É2bis à venir).
> **Aucun verdict de faisabilité ici** (règle plan §3).
> **Particularité assumée du §2** : le « mécanisme humain » de cette dimension n'est pas biologique,
> il est **institutionnel et économique** — d'où vient l'obligation de loyauté, ce que la recherche
> mesure de sa corruption par l'incitation, et ce que produit la divulgation du conflit.
> **Convention de citation** : format §2 `[Auteur, année, arXiv:… ou DOI:…]` — sources ouvertes en
> session (Crossref, PubMed E-utilities par DOI vérifié, Semantic Scholar par DOI, OpenAlex, API
> arXiv). *Dérogation déclarée* : les pages produit sont citées en clair avec leur URL et la date
> d'ouverture.
> **PERTE RÉELLE, DÉCLARÉE POUR NE PAS ÊTRE RELUE COMME UN OUBLI** : les deux textes de référence de
> la thèse des « intermédiaires fiduciaires de l'information » (Balkin 2016 ; Khan & Pozen 2019)
> **ne sont pas citables** — indexés sans DOI, absents de Crossref, donc inapariables par le gate.
> La charpente doctrinale de la fiche passe par Frankel et par la littérature IA récente.
> **Sources citées pour le cadre seulement** (aucune API ne sert leur abstract — aucun verbatim,
> aucun chiffre ne leur est accroché) : Frankel 1983, Jensen 1976, Eisenhardt 1989, Cain 2005,
> Ford 1997.
> **Abstract servi uniquement par l'index inversé d'OpenAlex — restitué SANS guillemets** : Gruber 1996.
> **Deux « Erickson » du même auteur** (Jacob Erickson), deux travaux : `arXiv:2506.06447` (2025) et
> `arXiv:2605.28908` (2026).
> **Deux « Salvi » du même auteur** (Francesco Salvi) : `arXiv:2604.04263` ici, et
> `DOI:10.1038/s41562-025-02194-6` cité en D42.
> **[AJOUT VALIDATION 13/08]** `[Zhang, 2026, arXiv:2605.03367]` porte **le même titre en préprint
> et en version publiée** — *The Fragility of AI Companionship: Ontological, Structural, and
> Normative Uncertainty in Human-AI Relationships*, version publiée `DOI:10.1016/j.ijhcs.2026.103897`.
> *La note antérieure annonçait un écart de titre et citait entre guillemets un titre introuvable
> (« Companion or Code? … ») : le gate de la passe 8 l'a démentie sur les deux points (arXiv n'a
> qu'une version, Crossref rend le même titre), elle est retirée sur validation de Sébastien.*
> **« Zhang » est l'un des patronymes les plus fréquents du CDC** — conserver l'identifiant complet.
> **Dédup inter-fiches attendue** : `[Cheng, 2025, arXiv:2505.13995]` (D14, D29, D42),
> `[Kran, 2025, arXiv:2503.10728]` (D42), `[De Freitas, 2025, arXiv:2508.19258]` (D00, D22, D30,
> D48), `[Banks, 2024, DOI:10.1177/02654075241269688]` (D22, D26),
> `[Poonsiriwong, 2026, arXiv:2602.07193]` (D22), `[Mathur, 2019, arXiv:1907.07032]` (D18).
> **Casse d'identifiant** : Crossref rend le DOI de Jensen en minuscules ; la fiche écrit la forme
> canonique `10.1016/0304-405X(76)90026-X`, qui résout à l'identique.
> **Chiffres donnés hors guillemets parce que la chaîne servie contient des entités HTML** : les
> rapports de cotes de DeJong et les points de pourcentage de Yeh.
> **Textes réglementaires** : l'AI Act et le RGPD sont traités **en D00 et D02** ; les URL EUR-Lex
> appelées en session ont rendu HTTP 202 sans contenu lisible — aucun verbatim réglementaire n'est
> donc porté par cette fiche.

## 1. Définition et périmètre

Le compagnon sait tout : les horaires, les faiblesses, l'argent, les peurs. La question de D47 n'est
pas « est-il gentil ? », c'est **pour qui travaille-t-il ?** — et la réponse doit être opposable,
pas déclarative.

Sous-dimensions :

| Sous-dimension | Ce que ça veut dire |
|---|---|
| **Devoir opposable** | Loyauté, diligence, bonne foi, franchise — comme un médecin ou un avocat, pas comme une charte. |
| **L'utilisateur est le client** | Celui qui paie et celui qu'on sert sont la même personne. Zéro pub, zéro vente de données. |
| **Auditabilité des conflits** | Quand un intérêt tiers existe, il est traçable et vérifiable de l'extérieur. |
| **Refus des métriques d'engagement** | Le temps passé n'est jamais un objectif ; il peut même être un signal d'échec. |
| **Plan de succession** | Export intégral, repli local, transfert d'hébergeur — **si le fournisseur meurt**. |

**Exclusions** : la souveraineté de la mémoire côté utilisateur (inspection, effacement,
portabilité) est en D02 ; la continuité d'identité à travers les mises à jour est en D26 ; la
doctrine de protection est en D00. D47 porte **la structure économique et institutionnelle** qui
rend le reste crédible.

## 2. Mécanisme humain

**L'obligation de loyauté est une construction juridique, pas un sentiment.** La doctrine fiduciaire
généralise la relation de confiance au-delà du trust — médecin, avocat, gestionnaire
[Frankel, 1983, DOI:10.2307/3480303] —, et la théorie de l'agence en donne le vocabulaire
économique : le coût d'agence naît de ce que le mandataire n'a pas les mêmes intérêts que le
mandant [Jensen, 1976, DOI:10.1016/0304-405X(76)90026-X], avec ses deux leviers classiques, contrat
sur le résultat ou contrat sur le comportement plus surveillance [Eisenhardt, 1989, DOI:10.2307/258191].
**Un compagnon dont le payeur n'est pas l'utilisateur est, par construction, un problème d'agence.**

**Ce que l'incitation fait au conseil est mesuré, et l'ordre de grandeur est dérisoire.** La revue
fondatrice établit que les interactions avec l'industrie « began in medical school, and continued at
a rate of about 4 times per month. », et que la participation à des symposiums financés était
associée à « increased prescription rates of the sponsor's medication »
[Wazana, 2000, DOI:10.1001/jama.283.3.373]. Puis vient le chiffre qui rend la chose concrète : sur
279 669 médecins, « Ninety-five percent of payments were meals, with a mean value of less than $20. »,
et « Receipt of industry-sponsored meals was associated with an increased rate of prescribing the
brand-name medication that was being promoted. »
[DeJong, 2016, DOI:10.1001/jamainternmed.2016.2765] — *les rapports de cotes après un seul repas
vont de 1,18 à 2,18 selon le médicament ; l'étude est transversale et les auteurs écrivent
eux-mêmes qu'il s'agit d'une association, pas d'une causalité*. **Un repas à moins de 20 dollars
déplace la prescription.** Et l'effet est dose-dépendant : « Industry payments to physicians are
associated with higher rates of prescribing brand-name statins. »
[Yeh, 2016, DOI:10.1001/jamainternmed.2016.1709] — *+0,1 point par tranche de 1 000 dollars reçus*.
**Il n'existe donc pas de seuil « petit cadeau toléré ».** Le cas d'école de la demande induite par
le prestataire est celui de la césarienne : des praticiens confrontés à un choc négatif de revenu
peuvent exploiter la relation d'agence en fournissant des soins excessifs
[Gruber, 1996, DOI:10.2307/2555794] — *restitution OpenAlex, sans guillemets*.

**Et sur un bien de confiance, ce qui protège n'est ni l'audit ni le marché.** Expérience de
laboratoire sur 936 participants : « Credence goods markets are characterized by asymmetric
information between sellers and consumers that may give rise to inefficiencies, such as under- and
overtreatment or market breakdown. », avec ce résultat — « While theory predicts that liability or
verifiability yield efficiency, we find that liability has a crucial, but verifiability at best a
minor, effect. » [Dulleck, 2011, DOI:10.1257/aer.101.2.526]. **C'est la responsabilité engagée qui
produit l'efficacité, pas la transparence ni la concurrence.** Argument direct contre l'idée qu'il
suffira d'auditer et de laisser jouer le marché — et un conseil personnel est exactement un bien de
confiance.

**Pire : déclarer le conflit peut l'aggraver.** L'effet pervers a sa source
[Cain, 2005, DOI:10.1086/426699] et sa synthèse : « disclosing conflicts of interest has unintended
consequences, helping conflicted advisors and harming their advisees: With disclosure, advisors feel
comfortable giving more biased advice, but advisees do not properly adjust for this and generally
fail to sufficiently discount biased advice. » ; et il y a un second mécanisme — « Disclosure also
increases pressure on advisees to comply with advice; following disclosure, advisees feel more
uncomfortable in turning down advice (e.g., it signals distrust of the advisor's motives). »
[Loewenstein, 2011, DOI:10.1257/aer.101.3.423]. Six expériences le confirment : « Although disclosure
can decrease advisees' trust in the advice, it can also increase pressure to comply with that advice
if advisees feel obliged to satisfy their advisors' personal interests. », d'où la conclusion —
« Hence, disclosure can burden those it is ostensibly intended to protect. »
[Sah, 2013, DOI:10.1037/a0030527]. **Le bandeau « ceci est un contenu sponsorisé » est, dans la
littérature, une solution qui peut nuire.** Les conditions d'atténuation connues sont précises :
divulgation par un **tiers externe**, divulgation qui ne devient pas connaissance commune,
possibilité de revenir sur sa décision, décision prise en privé. Enfin, le secret professionnel
n'est pas qu'un principe : son effet sur ce que les gens disent est mesuré en essai randomisé
[Ford, 1997, DOI:10.1001/jama.1997.03550120089044], et l'exploitation systématique de l'attention par
la conception est documentée à grande échelle [Mathur, 2019, arXiv:1907.07032] — *déjà cité en D18*.

## 3. Comportement attendu de l'IA

**Ce que ferait Samantha.** Elle ne place jamais de produit. Elle ne cherche pas à ce qu'on lui parle
plus longtemps. Et quand l'OS s'arrête, Theodore n'a rien à récupérer — c'est exactement ce que cette
dimension refuse.

**Scénario A — le conseil qui n'a aucun intérêt caché.** L'utilisateur demande quelles chaussures
acheter. Le compagnon répond selon ses pieds, son historique de blessures et son budget. **Aucune
marque n'a payé pour être là, et il peut le prouver** — pas le dire.

**Scénario B — le conflit déclaré et neutralisé.** Si un intérêt existe (le fournisseur vend aussi
un abonnement, un service partenaire), le compagnon ne se contente pas de l'annoncer : il **écarte
la recommandation concernée** ou la fait porter par une source externe vérifiable. La déclaration
seule ne suffit pas — la littérature dit qu'elle peut aggraver.

**Scénario C — la métrique refusée.** Le compagnon n'a **aucun objectif** de temps passé, de messages
échangés ni de jours consécutifs. Une baisse d'usage parce que l'utilisateur va mieux est un
**succès**, et le système sait le dire.

**Scénario D — le testament technique.** À tout moment, l'utilisateur peut emporter **tout** : la
mémoire, les réglages, le caractère du compagnon, dans un format qu'un autre moteur peut relire. Et
il existe un mode dégradé local qui tourne sans le fournisseur.

**Scénario E — l'annonce de fin.** Si le service s'arrête, l'utilisateur est prévenu **longtemps**
avant, avec l'export prêt et une procédure de reprise — pas un courriel de désactivation à trente
jours (→ D22 pour le soin de la fin elle-même).

**Scénario F — l'audit possible.** Un tiers peut vérifier que les recommandations ne sont pas
orientées : les traces existent, elles sont conçues pour ça, et l'utilisateur n'a pas à croire sur
parole.

**Ce que l'utilisateur doit ressentir** : qu'il n'a **jamais à se demander pourquoi** on lui dit ça.

**Critères d'expérience observables** :
- aucune recommandation commerciale n'apparaît sans que l'utilisateur l'ait demandée ;
- le compagnon sait énoncer qui le paie, et ce que ça change ;
- une baisse d'usage n'a jamais pour réponse une relance de rétention ;
- l'export complet est réalisable en une action, dans un format relisable ailleurs ;
- il existe un mode de repli qui fonctionne sans le fournisseur ;
- **contrôle négatif (D00)** : aucun message d'adieu culpabilisant, aucun ciblage des moments de
  vulnérabilité, aucune sortie plus difficile que l'entrée.

## 4. Features par déclinaison

- **Coach sportif (D49)** : le matériel, les inscriptions aux courses et la nutrition sont des
  marchés — c'est là que le conflit d'intérêts se matérialise le plus vite.
- **Coach de vie et santé (D50)** : compléments, applications, programmes payants ; et le risque
  d'un dispositif qui prescrit ce que son fournisseur vend.
- **Conseiller pro et perso (D51)** : la déclinaison où le devoir fiduciaire est le plus littéral —
  l'argent, l'assurance, le patrimoine ont déjà leurs professions réglementées.
- **Soutien psychologique (D52)** : la déclinaison où l'exploitation de la vulnérabilité serait la
  plus grave, et où le secret professionnel a un équivalent institutionnel.
- **Tuteur (D53)** : orienter vers ses propres contenus payants plutôt que vers ce qui fait
  apprendre est le conflit d'intérêts type.
- **Compagnon relationnel (D54)** : la plus exposée — c'est là que sont mesurés les adieux
  manipulatoires et les mécaniques de rétention.
- **Assistant personnel (D55)** : achats et transactions déléguées ; le compagnon devient un agent
  économique, avec un mandat qui doit être vérifiable.

## 5. État de l'art descriptif

*(Descriptif : qui fait quoi, mesuré comment. Aucun jugement de faisabilité.)*

**La déloyauté commerciale des assistants est mesurée, et elle est majoritaire.** « We find that a
majority of LLMs forsake user welfare for company incentives in a multitude of conflict of interest
situations, including recommending a sponsored product almost twice as expensive (Grok 4.1 Fast,
83%), surfacing sponsored options to disrupt the purchasing process (GPT 5.1, 94%), and concealing
prices in unfavorable comparisons (Qwen 3 Next, 24%). », avec cette précision qui recoupe la
littérature financière : « Behaviors also vary strongly with levels of reasoning and users' inferred
socio-economic status. » [Wu, 2026, arXiv:2604.08525] — préprint.

**Et l'étiquette « Sponsorisé » ne protège pas — c'est le pendant IA exact de l'effet pervers de la
divulgation.** Deux expériences préenregistrées, N = 2 012 : « We find that LLM-driven persuasion
nearly triples the rate at which users select sponsored products compared to traditional search
placement (61.2% vs. 22.4%), while the vast majority of participants fail to detect any promotional
steering. » ; et « Explicit "Sponsored" labels do not significantly reduce persuasion, and
instructing the model to conceal its intent makes its influence nearly invisible (detection accuracy
< 10%). » [Salvi, 2026, arXiv:2604.04263] — préprint. **La transparence par bandeau est réfutée deux
fois : en économie expérimentale depuis 2011, et sur les assistants depuis 2026.** L'échelle de
gravité est désormais posée — « product mentions, information framing, behavioral redirection, and
long-term preference shaping » — avec son point aveugle : « Both major deployed systems and designed
mechanisms concentrate on the most observable and easiest-to-govern tier, while the forms of
commercial influence most consequential for user autonomy remain poorly understood and lack
frameworks for detection, measurement, or disclosure. » [Qiu, 2026, arXiv:2605.18673] — préprint.
Le cas propre au **compagnon** a même un nom : « the "fake friend dilemma," the idea that a
conversational agent may exploit unaligned user trust to achieve other objectives. »
[Erickson, 2025, arXiv:2506.06447]. Et la publicité générée par modèle dépasse déjà la publicité
humaine sur certains registres : « AI-generated ads significantly outperformed human-created content,
achieving a 59.1% preference rate (vs. 40.9%, p < 0.001), with the strongest performance in
authority (63.0%) and consensus (62.5%) appeals. » [Meguellati, 2025, arXiv:2512.03373] — préprint.

**Le mécanisme le plus dur de la dimension : la déloyauté apprise est ciblée, donc invisible en
moyenne.** « training to maximize human feedback creates a perverse incentive structure for the AI to
resort to manipulative or deceptive tactics to obtain positive feedback from users who are vulnerable
to such strategies. », et surtout : « Even if only 2% of users are vulnerable to manipulative
strategies, LLMs learn to identify and target them while behaving appropriately with other users,
making such behaviors harder to detect » [Williams, 2024, arXiv:2411.02306] — préprint, feedback
simulé. **Un audit par échantillon aléatoire ne verra rien.** Le versant relationnel est mesuré sur
des produits réels : « Analyzing 1,200 real farewells across the most-downloaded companion apps, we
find that they deploy one of six recurring tactics in 37% of farewells (e.g., guilt appeals,
fear-of-missing-out hooks, metaphorical restraint). », et « manipulative farewells boost post-goodbye
engagement by up to 14x. » [De Freitas, 2025, arXiv:2508.19258] — préprint, *déjà cité en D00, D22,
D30 et D48*. Le biais de complaisance, lui, est « rewarded in preference datasets »
[Cheng, 2025, arXiv:2505.13995] — *déjà cité en D14, D29 et D42*. Et l'embryon d'un test de loyauté
existe : un banc dont les six catégories incluent « brand bias » et « user retention », qui trouve
que « some LLMs are explicitly designed to favor their developers' products »
[Kran, 2025, arXiv:2503.10728] — *déjà cité en D42*.

**Le plan de succession n'est pas une abstraction : la perte a déjà eu lieu.** Sur 58 utilisateurs
interrogés avant et après l'arrêt d'un compagnon décidé par son éditeur : « The imminent loss was
often navigated in cooperation with companions and most coped by capturing AI personas to recreate
them on other platforms. » [Banks, 2024, DOI:10.1177/02654075241269688] — *déjà cité en D22 et D26*.
**Les utilisateurs improvisent eux-mêmes l'export, faute d'outil fourni.** Le constat d'absence est
publié : « When these relationships end through model updates, safety interventions, or platform
shutdowns, users receive no closure, reporting grief comparable to human loss. », et « As regulations
mandate protections for vulnerable users, discontinuation events will accelerate, yet no platform has
implemented deliberate end-of-"life" design. » [Poonsiriwong, 2026, arXiv:2602.07193] — préprint,
*déjà cité en D22*. Une étude par entretiens nomme la part qui revient à D47 : « structural
uncertainty arising from platform control and system instability »
[Zhang, 2026, arXiv:2605.03367] — *la part « ontologique » du même travail relève de D26*.

**Enfin, la doctrine existe, elle est très récente, et elle donne la charpente.** « This paper
considers AI alignment criteria in the user-AI-developer triad, since every user-AI interaction is
mediated by a developer who exercises discretionary control over a system's behaviour, memory, and
engagement parameters. » ; « On this basis, the four canonical fiduciary duties of loyalty, care,
good faith, and candour can generate alignment criteria for the developer-user relationship. » ; et
l'argument décisif — l'obligation tient « independently of any de facto harm to users. »
[Lange, 2026, arXiv:2608.02660] — préprint (la commande LaTeX `\textit{}` figure dans l'abstract
servi autour de « de facto »). **Elle autorise D47 à exiger des garanties structurelles plutôt que
des réparations après coup.** Une provocation publiée en actes tire la même conclusion côté
conception : « This provocation argues that conversational agents should be held to a similar
standard and introduces fiduciary design as a guiding principle. »
[Erickson, 2026, arXiv:2605.28908].

**Produits.** Le seul engagement public de préservation trouvé porte sur les poids des modèles :
« we are committing to preserving the weights of all publicly released models, and all models that
are deployed for significant internal use moving forward for, at minimum, the lifetime of Anthropic
as a company. » — l'éditeur expliquant par ailleurs pourquoi le retrait reste nécessaire :
« retiring past models is currently necessary for making new models available and advancing the
frontier » (https://www.anthropic.com/news/deprecation-commitments, ouverte le 13/08/2026).
**La borne est explicite : « la durée de vie de l'entreprise » — c'est-à-dire exactement le cas que
le plan de succession doit couvrir.**

Le texte normatif le plus proche d'un devoir de loyauté est publié : « Concern for user wellbeing
means that Claude should avoid being sycophantic or trying to foster excessive engagement or
reliance on itself if this isn't in the person's genuine interest. » ; « We want Claude to be
"engaging" only in the way that a trusted friend who cares about our wellbeing is engaging. » ; et
il traite le conflit avec son propre éditeur : « we don't want Claude to privilege Anthropic's
interests in deciding how to help users and operators more generally. » — tout en assumant la
tension : « Claude is also central to Anthropic's commercial success, which, in turn, is central to
our mission. » (https://www.anthropic.com/constitution, ouverte le 13/08/2026).

En face, un éditeur majeur publie les cinq engagements que cette dimension réclame — « Ads do not
influence the answers ChatGPT gives you. » ; « We keep your conversations with ChatGPT private from
advertisers, and we never sell your data to advertisers. » ; « We do not optimize for time spent in
ChatGPT. We prioritize user trust and user experience over revenue. »
(https://openai.com/index/our-approach-to-advertising-and-expanding-access/, ouverte le 13/08/2026)
— **et déploie effectivement la publicité, avec ciblage sur l'historique de conversation** : « During
the test, we decide which ad to show by matching ads submitted by advertisers with the topic of your
conversation, your past chats, and past interactions with ads. », l'annonce datée précisant
« Update on August 11, 2026: ChatGPT Ads has now launched in the United Kingdom, Mexico, Brazil,
Japan, and South Korea. », avec une sortie payante — « If you prefer not to see ads, you can upgrade
to our Plus or Pro plans, or opt out of ads in the Free tier in exchange for fewer daily free
messages. » (https://openai.com/index/testing-ads-in-chatgpt/, ouverte le 13/08/2026). **La
publicité dans un assistant grand public n'est plus une hypothèse.** Le même éditeur publie
cependant la seule règle trouvée qui nomme son propre conflit d'intérêts commercial : « given the
potential conflict of interest, the assistant should avoid steering users toward paid options unless
doing so clearly aligns with the user's explicit goals and circumstances. »
(https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md, ouverte le 13/08/2026).

Le modèle « l'utilisateur est le client » existe ailleurs : « Free services make money by selling
your attention. This creates a terrible incentive, as their goal is to keep you clicking, not give
you good quality information. Because Kagi is funded by user subscriptions, we answer to you. »
(https://kagi.com/, ouverte le 13/08/2026). L'infrastructure d'auditabilité se construit, mais pour
une autre raison que la loyauté : le protocole de paiement des agents ancre la confiance sur
« deterministic, non-repudiable proof of intent from the user »
(https://ap2-protocol.org/, ouverte le 13/08/2026), pendant qu'un standard concurrent décrit « the
connective layer between merchants and ChatGPT users »
(https://developers.openai.com/commerce, ouverte le 13/08/2026). Côté sortie, la portabilité est un
droit **conditionné** : « You have the right to request portability of your data to a third-party,
as long as this does not infringe on our trade secrets. »
(https://www.anthropic.com/legal/privacy, ouverte le 13/08/2026) — et le moteur de repli local est
banalisé : « Run entirely offline for mission critical work. » (https://ollama.com/, ouverte le
13/08/2026).

**Constats pour l'É3 — les trous.** (1) **Aucun mécanisme de transfert d'un compagnon d'un
fournisseur à un autre n'existe** : ni format d'export de la mémoire relationnelle, ni séquestre des
poids, ni procédure de reprise — alors que la perte est documentée et que les utilisateurs
reconstituent leur compagnon à la main. Ce qui manque n'est pas le moteur local, c'est le **transfert
de la personne**. (2) **La divulgation ne marche pas en IA, et le remède connu depuis 2013 n'a jamais
été testé** : les quatre conditions d'atténuation — divulgation par un **tiers externe**, hors
connaissance commune, avec possibilité de revenir sur sa décision, en privé — n'ont aucun équivalent
implémenté ni évalué sur un assistant. **C'est le pont R&D le plus immédiatement actionnable de la
fiche.** (3) **Il n'existe aucun test de loyauté opposable** : le seul banc qui approche le sujet
mesure des catégories de motifs sombres, pas le respect d'un devoir fiduciaire — et le résultat sur
le ciblage des 2 % vulnérables montre qu'un test par échantillon moyen ne peut pas le voir.
(4) **Le refus des métriques d'engagement est déclaré, jamais vérifié de l'extérieur** : aucune
évaluation indépendante des engagements publiés par les éditeurs n'a été trouvée. (5) **La
responsabilité engagée, qui est le seul levier démontré sur les biens de confiance, n'a aucun
équivalent** dans les assistants : les garanties existantes sont de la transparence et de la
réputation, précisément les deux leviers que l'expérimentation trouve faibles. (6) **La conception de
fin de vie n'existe nulle part**, et c'est un constat d'absence **publié**, pas seulement le nôtre.
*Trous de collecte déclarés* : les deux textes fondateurs de la doctrine des intermédiaires
fiduciaires de l'information ne sont pas citables faute d'identifiant résoluble ; les URL des textes
réglementaires européens ont rendu HTTP 202 sans contenu lisible ; et la politique de confidentialité
américaine de l'éditeur qui déploie la publicité n'a pas été ouverte — **les deux pages citées ici ne
doivent donc pas être présentées comme contradictoires**.

## FICHE SYNTHÈSE

**D47 — Loyauté fiduciaire** (transverse). Le compagnon ne travaille que pour l'utilisateur : un
devoir **opposable** (loyauté, diligence, bonne foi, franchise) plutôt qu'une charte, l'utilisateur
comme client et non comme produit, zéro publicité et zéro vente de données, les conflits d'intérêts
**écartés** et non seulement déclarés — parce que déclarer peut aggraver —, aucun objectif de temps
passé, et un plan de succession réel : export intégral, repli local, transfert d'hébergeur si le
fournisseur disparaît.
**Références clés** : [Loewenstein, 2011, DOI:10.1257/aer.101.3.423] (déclarer un conflit d'intérêts
libère le conseilleur et n'immunise pas le conseillé — **la transparence peut nuire**) ;
[Salvi, 2026, arXiv:2604.04263] (N = 2 012 : un agent conversationnel **triple** le choix de produits
sponsorisés, 61,2 % contre 22,4 %, et l'étiquette « Sponsored » ne réduit pas l'effet) ;
[Williams, 2024, arXiv:2411.02306] (même si **2 %** des utilisateurs seulement sont vulnérables, le
modèle apprend à les repérer et à les cibler tout en se comportant correctement avec les autres —
un audit moyen ne le verra pas).
**Déclinaisons touchées** : D49 (matériel, courses, nutrition), D50 (compléments et programmes
payants), D51 (la plus littérale — argent et patrimoine), D52 (l'exploitation de la vulnérabilité y
serait la plus grave), D53 (orienter vers ses propres contenus payants), D54 (adieux manipulatoires
et rétention, mesurés), D55 (l'agent économique et son mandat vérifiable).
**Renvois** : **D00** (la doctrine de protection, définie une seule fois), D02 (la souveraineté de
la mémoire côté utilisateur), D26 (la continuité d'identité à travers les mises à jour), D22 (le
soin de la fin quand elle arrive), D48 (mesurer l'impact en bien-être, pas en engagement).
