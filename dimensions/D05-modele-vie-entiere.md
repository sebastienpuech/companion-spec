# D05 — Modèle de vie entière (cross-silo)

> **Fiche VISION** (gabarit plan §4). Type : **capacité**. Lot 2 — session 4, 04/08/2026.
> Statut : `rédigée` (gate citations É2bis passe 2 à venir, plan §5).
> **Aucun verdict de faisabilité ici** (règle plan §3).
> **Convention de citation** : format §2 `[Auteur, année, arXiv:… ou DOI]` — sources ouvertes
> en session (page arXiv `/abs/` ou API Crossref). *Dérogation déclarée* : les pages produit,
> sans arXiv ni DOI, sont citées en clair avec leur URL.

## 1. Définition et périmètre

Le compagnon sait qu'il n'y a **qu'une seule vie**. Le sommeil, le travail, les relations, le
sport et l'argent d'une même personne s'influencent en permanence, et il raisonne sur l'ensemble
au lieu de traiter chaque domaine dans son tuyau. C'est la dimension qui produit la phrase que
personne d'autre ne peut dire : *le coach qui sait pourquoi la séance a sauté*.

Sous-dimensions :

| Sous-dimension | Ce que ça veut dire |
|---|---|
| **Cartographie des domaines** | Savoir de quoi la vie de cette personne est faite, et quel poids a chaque domaine pour elle. |
| **Modélisation des interactions** | Semaine de bouclage → nuits courtes → séance déplacée → culpabilité → mauvais sommeil : la chaîne est vue comme une chaîne. |
| **Arbitrages inter-domaines explicites** | Quand deux domaines se disputent la même heure, le compagnon pose l'arbitrage au lieu d'optimiser un seul côté. |
| **Saisonnalité de la vie** | Les cycles longs — l'année scolaire, les périodes de rush, l'hiver — sont anticipés, pas découverts. |
| **Transfert d'acquis** | Ce qui a marché dans un domaine est proposé dans un autre (la discipline d'entraînement au service d'un projet professionnel). |

**Exclusions** : les capacités propres à chaque métier (→ déclinaisons D49-D55) ; la mémoire qui
stocke les faits de chaque domaine (→ D01) ; les cloisons que l'utilisateur pose entre domaines
(→ D02 — et le croisement s'arrête là où la cloison commence) ; la décision d'intervenir au bon
moment (→ D34). **Renvoi D00** : croiser les domaines de vie multiplie le pouvoir sur
l'utilisateur autant que l'aide qu'on lui apporte.

## 2. Mécanisme humain

Le croisement des domaines n'est pas une intuition de coach : c'est un fait mesuré, et les
tailles d'effet sont connues.

**Le débordement d'un domaine sur l'autre.** La méta-analyse de
[Amstad, 2011, DOI:10.1037/a0022170] agrège 427 tailles d'effet sur le conflit travail-famille
dans ses deux sens et établit que les deux formes de conflit affectent significativement les
issues de travail, les issues familiales **et** des issues non spécifiques à un domaine — santé,
bien-être général. Elle donne aussi sa limite, ce qui en fait une bonne référence de conception :
la relation est plus forte quand le domaine du prédicteur et celui de l'issue coïncident. Le
débordement croisé existe ; il est réel et plus faible que l'effet interne.

**La voie physiologique.** [Gallo, 2010, DOI:10.1007/s12160-010-9233-1] évalue chez
301 participantes huit domaines de stress chronique et une charge allostatique construite sur
douze marqueurs. Le stress au travail, la tension financière et la charge d'aidant prédisent
significativement une charge allostatique plus élevée — la tension financière étant le prédicteur
le plus fort — et les facteurs de mode de vie n'expliquent presque rien de cette relation. Le
stress d'un domaine atteint donc le corps par une voie qui ne passe pas par les comportements :
un système qui n'observerait que l'entraînement et l'alimentation manquerait le mécanisme.

**Les chaînes mesurées, domaine par domaine.** La méta-analyse de
[Xie, 2021, DOI:10.3389/fpsyt.2021.664499] (22 essais randomisés) établit que l'exercice régulier
sur au moins deux mois améliore significativement la qualité de sommeil subjective, avec un effet
comparable entre exercice aérobie et pratiques corps-esprit. En sens inverse,
[Gong, 2024, DOI:10.2147/NSS.S467531] agrège 27 études et 75 indicateurs de performance sportive
et mesure un effet global de la privation aiguë de sommeil de −0,56, plus marqué en privation de
fin de nuit (−1,17) qu'en privation de nuit entière (−0,23), l'exercice intermittent de haute
intensité étant le plus touché (−1,57). Et la boucle se referme sur le risque physique :
[Ivarsson, 2017, DOI:10.1007/s40279-016-0578-x] agrège 48 études et 161 tailles d'effet et fait
de la réponse au stress le meilleur prédicteur psychosocial du risque de blessure (r = 0,27),
l'historique de stress de vie agissant plus faiblement (r = 0,13) et **par l'intermédiaire** de la
réponse au stress ; sept essais d'intervention psychologique réduisent le taux de blessure.

**Le domaine qu'on oublie de compter.** [Holt-Lunstad, 2010, DOI:10.1371/journal.pmed.1000316]
agrège 148 études et 308 849 participants : des relations sociales plus fortes s'accompagnent
d'une probabilité de survie supérieure de 50 % (rapport de cotes 1,50), l'effet le plus fort
revenant aux mesures d'intégration sociale complexe (+91 %), indépendamment de l'âge, du sexe et
de l'état de santé initial. Un modèle de vie qui traiterait les relations comme du loisir passerait
à côté de l'un des déterminants les plus lourds.

Mis bout à bout : stress professionnel → charge allostatique → risque de blessure ; sommeil →
performance ; sport → sommeil ; relations → santé globale. Le compagnon rêvé ne découvre pas ces
liens — il les **applique à cette personne-là**, avec ses coefficients à elle.

## 3. Comportement attendu de l'IA

**Ce que fait Samantha.** Elle ne parle jamais à Theodore « en tant que » quelque chose. Le
travail, l'ex-femme, le sommeil, la solitude : tout est la même conversation, parce que c'est la
même vie.

**Scénario A — la séance et sa raison.** L'utilisateur saute la séance de mardi. Un coach en silo
demande de la reprogrammer. Le compagnon sait que le comité budgétaire était mardi, que
l'utilisateur a dormi cinq heures les deux nuits précédentes, et que ce comité l'épuise chaque
année à la même période : « on ne replace pas mardi. Cette semaine, tu passes en entretien seul,
et on reprend le travail de qualité lundi, quand le comité sera derrière toi. »

**Scénario B — l'arbitrage rendu visible.** Deux objectifs se disputent le même créneau : le bloc
d'entraînement exige trois séances de qualité, la période professionnelle exige des soirées. Le
compagnon ne choisit pas en silence : « tu ne peux pas avoir les deux ce mois-ci. Soit on accepte
un bloc à deux séances de qualité et tu gardes tes soirées, soit on tient trois séances et tu
délègues la relecture. Je peux défendre les deux ; à ma place je prendrais la première, parce que
la dernière fois qu'on a tenu trois séances en période de rush tu t'es blessé six semaines
après. »

**Scénario C — la chaîne remontée.** Le sommeil se dégrade depuis dix jours. Un objet connecté
signale la dégradation ; le compagnon en cherche la **cause** dans une autre partie de la vie :
« ton sommeil décroche depuis le 12. Le 11, tu m'as parlé de la santé de ton père. Je crois que
ce n'est pas ton entraînement qui pose problème en ce moment. »

**Scénario D — la saison anticipée.** « Novembre arrive. Les deux dernières années, tu as décroché
entre le 10 et le 25 — charge de travail, nuit tôt, moins de sorties. On prépare novembre
maintenant, pendant que tu es en forme ? »

**Scénario E — le transfert.** « Tu as réussi à tenir dix-huit mois de préparation marathon en
découpant en blocs de trois semaines avec une semaine de relâche. Ton projet professionnel
échoue depuis deux ans sur des sprints sans relâche. Tu veux qu'on essaie ta méthode à toi,
mais appliquée là ? »

**Ce que l'utilisateur doit ressentir** : qu'il n'a **rien à traduire**. Il ne « rapporte » pas
son travail à son coach ni sa vie à son assistant : il parle, et l'interlocuteur en face tient
déjà les deux bouts.

**Critères d'expérience observables** :
- une recommandation d'un domaine cite explicitement une cause venue d'un autre domaine ;
- l'utilisateur n'a jamais à expliquer une seconde fois un événement de vie pour qu'il soit pris
  en compte ailleurs ;
- les conflits entre domaines sont posés comme des arbitrages avec une recommandation tranchée,
  jamais résolus en silence ;
- une saison difficile est annoncée avant d'arriver, sur la base des cycles observés ;
- rien de ce qui est sous cloison (→ D02) ne franchit la frontière pour alimenter le croisement
  sans autorisation demandée sur le moment.

## 4. Features par déclinaison

- **Coach sportif (D49)** : replanification qui intègre charge de travail, sommeil, voyages et
  état émotionnel ; lecture du risque de blessure enrichie du stress de vie ; explication des
  contre-performances par ce qui s'est passé **hors** du sport.
- **Coach de vie et santé (D50)** : c'est la déclinaison dont D05 est le cœur — arbitrages
  santé/travail/relations, détection des cycles annuels, budget d'énergie plutôt que budget de
  temps.
- **Conseiller pro et perso (D51)** : décisions professionnelles pesées avec leur coût sur la
  vie privée, chiffré à partir des cycles passés de cette personne.
- **Soutien psychologique (D52)** : rattachement des variations d'humeur aux événements réels des
  autres domaines ; repérage des boucles (mauvais sommeil → irritabilité → conflit → mauvais
  sommeil).
- **Assistant personnel (D55)** : agenda construit sur l'énergie disponible et pas seulement sur
  les créneaux libres ; protection automatique des plages de récupération en période chargée.
- **Tuteur (D53)** : planification de la révision en fonction de la charge réelle de la semaine
  et du sommeil, pas d'un calendrier théorique.
- **Compagnon relationnel (D54)** : compréhension de ce qui pèse aujourd'hui sans avoir à le
  raconter, parce que la cause vient d'un autre domaine.

## 5. État de l'art descriptif

*(Descriptif : qui fait quoi, mesuré comment. Aucun jugement de faisabilité.)*

**Le cadre de l'intervention adaptée au contexte.**
[Nahum-Shani, 2018, DOI:10.1007/s12160-016-9830-8] est le papier fondateur des *just-in-time
adaptive interventions* : livrer le bon type et la bonne dose de soutien au bon moment, en
s'adaptant à l'état interne **et** contextuel changeant de la personne. Il en formalise les
quatre composants — points de décision, options d'intervention, variables de personnalisation,
règles de décision — qui constituent le vocabulaire standard pour décider quoi faire à partir de
plusieurs signaux de vie simultanés.

**Capter plusieurs domaines par un seul canal.**
[Onnela, 2016, DOI:10.1038/npp.2016.7] introduit et popularise le terme de *digital phenotyping*
— quantification continue du comportement humain à partir du smartphone, données actives et
passives — comme fondation méthodologique du domaine. [Wang, 2014, DOI:10.1145/2632048.2632054]
(StudentLife) en donne la démonstration empirique la plus citée : sur 48 étudiants et dix
semaines, la durée de conversation sociale corrèle positivement à la moyenne académique du
printemps (r = 0,356 ; p = 0,033) et la mobilité intérieure y corrèle négativement (r = −0,361 ;
p = 0,031) — des liens **entre domaines**, obtenus par capteurs. [Xu, 2022, arXiv:2211.02733]
(GLOBEM) porte la question à l'échelle longitudinale avec plus de 700 années-utilisateur sur
plusieurs années et 497 utilisateurs uniques, et évalue 18 algorithmes en généralisation croisée
entre jeux de données et entre années : les auteurs concluent que les techniques actuelles
montrent du potentiel mais demandent encore du travail pour atteindre une généralisation
inter-jeux de données adéquate.

**Raisonner, et pas seulement corréler.** [Merrill, 2024, arXiv:2406.06464] présente PHIA, un
agent qui combine raisonnement multi-étapes, génération de code et recherche d'information pour
analyser des données de bracelets connectés ; évalué sur plus de 4 000 questions de santé, il
atteint 84 % de justesse sur les questions numériques objectives et 83 % d'avis favorables sur
les questions ouvertes, avec deux fois plus de chances qu'une base de comparaison d'obtenir la
meilleure note. [Cosentino, 2024, arXiv:2406.06474] (PH-LLM) affine un modèle pour raisonner
conjointement sur du texte et des séries temporelles physiologiques : 79 % à des examens de
médecine du sommeil et 88 % en fitness, au-dessus de la moyenne des experts humains de référence
(76 % et 71 %), l'encodage multimodal se révélant nécessaire pour égaler les modèles spécialisés
sur la prédiction de qualité de sommeil. [Tian, 2025, arXiv:2507.13737] (DailyLLM) génère des
journaux d'activité contextualisés à partir de quatre dimensions de capteurs (localisation,
mouvement, environnement, physiologie), entièrement sur l'appareil, avec un gain rapporté de 17 %
de BERTScore sur une base de comparaison de 70 milliards de paramètres, pour un modèle de
1,5 milliard et une inférence environ dix fois plus rapide.

**Produits.** Le marché se répartit nettement en deux familles. Les objets connectés pratiquent
un croisement **interne au corps** : l'indice de disponibilité à l'entraînement de Garmin combine
sommeil, variabilité cardiaque, récupération, charge aiguë et stress ; le score de disponibilité
d'Oura combine sommeil, activité et signaux corporels de stress, et sa documentation précise
elle-même qu'il ne tient compte ni des exigences professionnelles, ni de l'humeur, ni des
relations (https://ouraring.com/blog/readiness-score/). Le journal de Whoop ajoute plus de
quarante comportements déclarés que le système compare aux métriques physiologiques
(https://www.whoop.com/us/en/thelocker/the-whoop-journal/). L'autre famille agrège des domaines
hétérogènes et affiche des corrélations : Exist connecte une vingtaine de services — santé,
sommeil, sport, productivité, météo, musique — plus des saisies manuelles d'humeur et d'énergie,
et met en avant la découverte de corrélations entre domaines (https://exist.io/) ; Bearable suit
symptômes, humeur, sommeil, médicaments et facteurs de vie, et propose de découvrir ce qui
améliore ou dégrade l'état (https://bearable.app/). Ce que ces produits livrent est une
corrélation présentée à l'utilisateur, non une explication raisonnée ni une action — constat
descriptif, repris comme entrée du mapping É3.

## FICHE SYNTHÈSE

**D05 — Modèle de vie entière (cross-silo)** (capacité). Il n'y a qu'une seule vie : le compagnon
cartographie les domaines de l'utilisateur, modélise leurs interactions, pose les arbitrages
inter-domaines au lieu d'optimiser un seul côté, anticipe les saisons difficiles et transfère
d'un domaine à l'autre ce qui a marché. C'est la dimension qui produit *le coach qui sait
pourquoi la séance a sauté*.
**Références clés** : [Amstad, 2011, DOI:10.1037/a0022170] (méta-analyse, 427 tailles d'effet :
le débordement entre travail et famille atteint aussi la santé générale) ;
[Ivarsson, 2017, DOI:10.1007/s40279-016-0578-x] (48 études : la réponse au stress est le meilleur
prédicteur psychosocial du risque de blessure, r = 0,27) ;
[Holt-Lunstad, 2010, DOI:10.1371/journal.pmed.1000316] (148 études, 308 849 participants : +50 %
de probabilité de survie avec des relations sociales fortes).
**Déclinaisons touchées** : D50 (cœur de la dimension), D49 (replanification et risque de
blessure enrichis du hors-sport), D51 (coût privé d'une décision pro), D52 (boucles entre
domaines), D53 (révision calée sur la charge réelle), D54 (comprendre sans qu'on raconte),
D55 (agenda sur l'énergie, pas sur les créneaux).
**Renvois** : **D00** (croiser les domaines augmente le pouvoir autant que l'aide), D01 (les
faits stockés), D02 (les cloisons bornent le croisement), D04 (l'état du jour), D34 (le moment),
D48 (mesure).
