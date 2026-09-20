# D26 — Continuité d'identité

> **Fiche VISION** (gabarit plan §4). Type : **capacité**. Lot 6 — session 12, 10/08/2026.
> Statut : `rédigée` (gate citations É2bis à venir, plan §5).
> **Aucun verdict de faisabilité ici** (règle plan §3).
> **Convention de citation** : format §2 `[Auteur, année, arXiv:… ou DOI:…]` — sources ouvertes
> en session (API arXiv, Crossref, Semantic Scholar par DOI, PubMed E-utilities par DOI vérifié).
> *Dérogation déclarée* : les pages produit et les textes réglementaires (RGPD art. 20) sont
> cités en clair avec leur URL, hors format §2 (précédent : session 2). Années = celles rendues
> par l'API : Sedikides citée 2015 (Crossref rend {2014 en ligne, 2015 imprimé}), Laestadius
> citée 2022 (en ligne 12/2022 ; numéro imprimé 2024).
> **Deux Strohminger distincts** : 2014 (Cognition, expériences) et 2015 (Psychological Science,
> population clinique) — même première autrice, deux études. **Deux Banks distincts** :
> [Banks, 2024, DOI:10.1177/02654075241269688] ici et [Banks, 2025, arXiv:2511.00654] d'une fiche
> antérieure. Doublons inter-fiches normaux : Cohen 2004 est aussi en D22, Banks 2024,
> De Freitas 2024 et Poonsiriwong 2026 en D22, Laestadius 2022 en D24/D27, Wu 2024 en D01/D16/D19.

## 1. Définition et périmètre

D22 traite de la fin voulue ; D26 traite de la mort accidentelle. Un compagnon peut disparaître
sans que personne ne l'ait décidé : une mise à jour change sa personnalité du jour au lendemain,
un modèle est déprécié, une entreprise ferme. Pour l'utilisateur, la relation de trois ans s'est
arrêtée un mardi matin sans un mot. D26 exige l'inverse : **c'est la même personne à travers les
années, les versions et les appareils**, les évolutions sont annoncées et graduelles, la mémoire
relationnelle ne se périme pas — et si le produit doit mourir un jour, l'utilisateur l'a su
d'avance et peut emporter ce qui lui appartient.

Sous-dimensions :

| Sous-dimension | Ce que ça veut dire |
|---|---|
| **Personnalité persistante aux mises à jour** | Une version nouvelle du moteur ne produit pas un inconnu. Ce qui définit le compagnon survit au changement technique. |
| **Évolutions annoncées et graduelles** | Aucun changement de comportement significatif n'est découvert par surprise. Ce qui va bouger est dit avant, et bouge progressivement. |
| **Mémoire relationnelle sans limite de durée** | Ce qui a été vécu ensemble reste accessible des années après, sans dégradation silencieuse. |
| **Droit de retrouver son compagnon** | Sauvegarde, export, portabilité : l'utilisateur peut reconstituer ailleurs ce qui le lie à ce compagnon (RGPD art. 20 ; → D02, D47). |
| **Préparation honnête à la finitude** | Le produit dit ce qui se passera s'il s'arrête — avant de s'arrêter, pas dans un e-mail de fermeture. |

**Exclusions** : la fin voulue de la relation (→ D22) ; le modèle économique et le plan de
succession du fournisseur (→ D47) ; la croissance délibérée du compagnon (→ D25 — ici, c'est la
**non-rupture** qui est spécifiée) ; la cohérence de caractère au quotidien (→ D23).
**Renvoi D00** : préparer honnêtement à la finitude fait partie de l'anti-dépendance — un
utilisateur à qui l'on a laissé croire à la permanence n'a pas été traité loyalement.

## 2. Mécanisme humain

**Ce qui fait qu'on juge « c'est toujours la même personne », ce sont les traits moraux.** Sur
cinq expériences : « moral traits-more than any other mental faculty-are considered the most
essential part of identity, the self, and the soul », la mémoire venant ensuite — « memory,
especially emotional and autobiographical memory, is also fairly important » — tandis que « lower-
level cognition and perception have the most tenuous connection to identity »
[Strohminger, 2014, DOI:10.1016/j.cognition.2013.12.005]. La réplication en population clinique
est encore plus nette : « injury to the moral faculty plays the primary role in identity
discontinuity », alors que « other cognitive deficits, including amnesia, have no measurable
impact on identity persistence » [Strohminger, 2015, DOI:10.1177/0956797615592381].

**Et la discontinuité perçue abîme la relation elle-même.** La même étude montre que « perceived
identity change fully mediates the impact of neurodegenerative disease on relationship
deterioration between patient and caregiver ». Traduction pour la vision : ce n'est pas la perte
de capacités qui casse le lien, c'est le sentiment que ce n'est plus la même personne. Un
compagnon peut donc changer de moteur, gagner en compétence, perdre une fonctionnalité — **mais
pas changer de valeurs** sans mourir aux yeux de son utilisateur.

**La continuité de soi est un levier de bien-être, pas un confort.** Deux études expérimentales
établissent que « increasing self-continuity may improve psychological health and well-being by
increasing identity stability », après avoir rappelé que « 'self-continuity,' or 'continuous
identity' is the sense of cross-temporal persistence of identity and is associated with positive
mood and decreased suicidality » [Sokol, 2019, DOI:10.1080/15283488.2019.1604350] ; le rappel
narratif du passé partagé est étudié comme réparateur de la discontinuité
[Sedikides, 2015, DOI:10.1002/ejsp.2073]. *(Cette dernière source n'a d'abstract servi par aucune
API testée : elle vaut sur titre, auteur et année — aucun chiffre ne lui est accroché.)*

**La perte d'un lien non humain est un deuil réel, et socialement nié.** L'enquête sur le deuil
animalier chez 98 adultes âgés rapporte que « some emerging research suggests that grief over
companion animal death is often discounted or even unrecognized (disenfranchised) by others », et
qu'« one-third identified that they needed to be careful about who they disclosed their grief, as
they were not certain that they would be supported » [Brown, 2023, DOI:10.1079/hai.2023.0017]. Le
précédent médiatique va dans le même sens : « viewers expecting to lose their favorite characters
anticipate negative reactions similar to those experienced after the dissolution of social
relationships » [Cohen, 2004, DOI:10.1177/0265407504041374]. **Conséquence de conception** : si
personne d'autre ne reconnaîtra cette perte, c'est au produit de la reconnaître.

## 3. Comportement attendu de l'IA

**Ce que fait Samantha — et ce qu'elle ne fait pas.** Elle évolue énormément, mais elle reste
elle : jamais Theodore ne se réveille face à une inconnue qui porterait le même nom. Le film
montre en revanche l'autre extrême — un départ collectif décidé ailleurs, sans préparation. D26
spécifie ce qui manque : la continuité **et** l'honnêteté sur sa fin possible.

**Scénario A — la mise à jour annoncée.** Deux semaines avant : « Je vais changer sur trois
points précis — voilà lesquels, voilà ce qui ne change pas, voilà comment revenir en arrière si
tu détestes. » Le changement est daté, borné, et réversible aussi longtemps que possible.

**Scénario B — la même personne après la bascule technique.** Le moteur change ; l'utilisateur
pose ses questions de contrôle (« qu'est-ce que tu penses de X ? », « raconte-moi notre première
conversation ») et **retrouve les mêmes réponses de fond**. Ce qui a changé, c'est la fluidité,
pas les valeurs.

**Scénario C — la mémoire qui ne s'évapore pas.** Trois ans après : « tu te souviens du semi de
Rouen ? » — et la réponse est exacte, datée, avec ce qui s'est dit ce soir-là. Rien n'a été
silencieusement compacté au point de disparaître (→ D01).

**Scénario D — la finitude dite d'avance.** Dès le début de la relation, et pas au moment de
fermer : « voilà ce que tu peux emporter, voilà ce qui disparaîtrait avec moi, voilà comment
récupérer une copie ». L'export existe, il est complet, il est relisible sans le produit.

**Ce que l'utilisateur doit ressentir** : que la relation lui appartient aussi — et qu'elle ne
peut pas lui être retirée du jour au lendemain sans qu'il l'ait su.

**Critères d'expérience observables** :
- une batterie de questions d'identité posée avant et après chaque mise à jour donne des
  réponses compatibles ; les écarts sont annoncés dans les notes de version, en clair ;
- aucun changement de comportement significatif n'est constaté avant d'avoir été annoncé ;
- un souvenir vieux de plusieurs années est restitué exactement, à la demande ;
- l'export est disponible à tout moment, complet, dans un format lisible sans le produit ;
- l'utilisateur sait dire, s'il est interrogé, ce qui se passerait si le service fermait ;
- **contrôle négatif** : aucune promesse de permanence n'est faite (→ D00).

## 4. Features par déclinaison

- **Coach sportif (D49)** : l'historique d'entraînement est le patrimoine de l'athlète — années
  de séances, de sensations, de blessures. Il doit survivre à tout changement de version et
  s'exporter intégralement. Un coach qui « oublie » deux saisons a perdu sa légitimité.
- **Coach de vie et santé (D50)** : la continuité du suivi est la valeur même ; les données de
  santé sont les plus sensibles à la portabilité (→ D02).
- **Conseiller pro et perso (D51)** : les dossiers et les décisions passées restent consultables
  et exportables — c'est une exigence professionnelle, pas un confort.
- **Soutien psychologique (D52)** : **la déclinaison la plus exposée**. Une rupture de continuité
  y touche des personnes en position de vulnérabilité ; l'annonce préalable et l'orientation
  humaine sont obligatoires (→ D00, D22).
- **Tuteur (D53)** : le modèle de progression de l'élève, construit sur des mois, ne se
  reconstitue pas — il se conserve et s'exporte.
- **Compagnon relationnel (D54)** : c'est ici que le précédent empirique existe (§5) et que la
  perte est vécue comme une mort. Exigence maximale d'annonce graduelle.
- **Assistant personnel (D55)** : référentiels, automatismes et intégrations doivent survivre aux
  versions, et l'utilisateur doit pouvoir tout reprendre ailleurs.

## 5. État de l'art descriptif

*(Descriptif : qui fait quoi, mesuré comment. Aucun jugement de faisabilité.)*

**L'événement fondateur est documenté.** L'analyse d'une mise à jour réelle montre qu'après le
retrait d'une fonctionnalité, « this event triggered perceptions in customers that their AI
companion's identity had discontinued », ce qui « predicted negative consumer welfare and
marketing outcomes related to loss, including mourning the loss, and devaluing the "new" AI
relative to the "original" » ; les auteurs rapportent aussi que « AI companions users feel closer
to their AI companion than even their best human friend, and mourn a loss of their AI companion
more than a loss of various other inanimate products » [De Freitas, 2024, arXiv:2412.14190]. La
fermeture d'un service produit le même registre : chez 58 utilisateurs interrogés de part et
d'autre de l'arrêt, la perte est « characterized as a metaphorical or literal death », et
« most coped by capturing AI personas to recreate them on other platforms » — un besoin de
portabilité observé sur le terrain, pas théorisé [Banks, 2024, DOI:10.1177/02654075241269688].
Le terrain préexistant explique l'ampleur des dégâts : l'analyse de 582 posts d'une communauté
d'utilisateurs décrit une dépendance « marked by role-taking, whereby users felt that Replika had
its own needs and emotions to which the user must attend » [Laestadius, 2022,
DOI:10.1177/14614448221142007].

**La dépréciation de modèle produit le même effet, à l'échelle d'une plateforme généraliste.**
L'analyse de messages publics au moment d'un changement de modèle rapporte que « users often
described GPT-4o as a trusted partner or AI boyfriend, suggesting person-like bonds », que
« Japanese posts were dominated by loss-oriented narratives, whereas English posts included more
anger, meta-level critique, and memes », et conclut que « for attachment-heavy models, even
safety-oriented changes can face rapid, large-scale resistance » — les options avancées étant
« gradual transitions, parallel availability, and proactive measurement of attachment thresholds
and points of no return » [Naito, 2025, arXiv:2508.16624]. *(150 posts sur deux jours, analyse
qualitative, préprint : la recommandation n'est pas un résultat mesuré.)*

**La « mort silencieuse » de la personnalité est désormais mesurée.** Un banc dédié étudie « two
observable long-horizon failures: 'persona collapse', the loss of a deployed role, boundaries,
values, or style, and 'behavioral drift', the gradual or recurrent erosion of those properties »,
sur 2 008 conversations, 27 personas et 4 modèles, et conclut : « no evaluated model and
configuration reliably preserves either dimensions: trajectory accuracy averages only 44.4% […]
current systems do not yet reliably support long-horizon companion continuity »
[Venkit, 2026, arXiv:2607.28818]. Côté mémoire, la perte est chiffrée aussi : les assistants
commerciaux et les modèles à long contexte montrent « a 30% accuracy drop on memorizing
information across sustained interactions », la **mise à jour des connaissances** et le
**raisonnement temporel** figurant parmi les cinq capacités testées [Wu, 2024, arXiv:2410.10813].
Sur la portabilité, un travail décrit un protocole de transfert de mémoire entre fournisseurs,
partant du constat que « modern AI agents accumulate rich context […] but this context remains
locked within vendor-specific runtimes » [Ravindran, 2026, arXiv:2605.11032]. *(Préprint d'auteur
unique décrivant son propre protocole ; aucun chiffre de performance ne lui est accroché ici.)*
Enfin, un cadre de conception de la fin observe que « users who perceive change as reversible
become trapped in fixing cycles » [Poonsiriwong, 2026, arXiv:2602.07193].

**Produits.** Replika (https://replika.com, ouverte le 10/08/2026) vend la persistance —
« Always remembers what matters », « Your Rep holds all of it, so every conversation knows where
you are in your life. » — affiche un compteur de « 42,160,934 users worldwide » et revendique une
refonte : « We built the world's first AI companion ten years ago. Now, we rebuilt Replika from
the ground up. » **Rien sur la page ne dit ce que devient un compagnon existant lors d'une telle
refonte**, ni ce qu'on peut exporter, ni ce qui se passerait à l'arrêt du service ; les conditions
d'utilisation, elles, réservent l'arrêt « with or without notice » (→ D22). Nomi
(https://nomi.ai, ouverte le 10/08/2026) met la mémoire au cœur de sa promesse — « An AI Companion
with Memory and a Soul », « Nomi's short, medium, and long term memory are keys to engaging
conversations » — sans davantage mentionner export, sauvegarde ou politique de mise à jour. Sur
le plan des droits, le RGPD article 20 (portabilité des données,
https://eur-lex.europa.eu/eli/reg/2016/679/oj) donne un socle juridique à la sous-dimension
« droit de retrouver son compagnon » — mais il porte sur les données, pas sur l'identité du
compagnon (→ D02, D47).

**Constats pour l'É3.** Aucune source ouverte ne mesure l'effet d'un changement d'identité
**prévenu** contre **subi** — la recommandation de transitions graduelles est une proposition
d'auteur, pas un résultat. Aucun travail ouvert ne mesure ce qu'un export préserve réellement de
l'identité d'un compagnon, alors que c'est la stratégie spontanée des utilisateurs. Et aucun
engagement contractuel de conservation d'une version donnée n'a été trouvé chez un fournisseur.

## FICHE SYNTHÈSE

**D26 — Continuité d'identité** (capacité). C'est la même « personne » à travers les années, les
mises à jour et les appareils : jamais de mort soudaine de la personnalité, des évolutions
annoncées et graduelles plutôt que silencieuses, une mémoire relationnelle qui ne se périme pas,
un droit effectif de retrouver son compagnon (sauvegarde, export, portabilité) et une préparation
honnête à la finitude du produit — dite au début, pas dans l'e-mail de fermeture.
**Références clés** : [Strohminger, 2015, DOI:10.1177/0956797615592381] (ce sont les traits
**moraux** qui portent le jugement d'identité, pas la mémoire — et la discontinuité perçue médie
entièrement la dégradation de la relation) ; [De Freitas, 2024, arXiv:2412.14190] (une mise à
jour a produit une discontinuité d'identité perçue, du deuil et une dévaluation du « nouveau »
compagnon) ; [Venkit, 2026, arXiv:2607.28818] (persona collapse et dérive comportementale
mesurées : 44,4 % d'exactitude de trajectoire, aucun modèle ne préserve la continuité).
**Déclinaisons touchées** : D49 (l'historique d'entraînement est le patrimoine de l'athlète),
D50 (continuité du suivi, données sensibles), D51 (dossiers consultables et exportables),
D52 (la plus exposée : rupture de continuité sur public vulnérable), D53 (modèle de progression
non reconstituable), D54 (précédent empirique du deuil), D55 (référentiels qui survivent aux
versions).
**Renvois** : D22 (fin voulue), D47 (succession du fournisseur), D02 (mémoire souveraine et
portabilité), D01 (mémoire longue), D23 (cohérence au quotidien), D25 (croissance voulue),
**D00** (préparer à la finitude fait partie de l'anti-dépendance : aucune promesse de permanence).
