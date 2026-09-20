# Note de méthode

Comment les 56 lignes ont été produites, ce qui a été vérifié par script, ce qui ne l'a pas été,
et ce que ce dépôt n'établit pas. À lire avant de citer une ligne.

---

## 1. D'où viennent les 56 lignes

Trois directions de recherche, menées en parallèle par des agents en contexte frais, du 4 au
13 août 2026 :

- **(a) sciences du lien humain** — psychologie des relations, sciences cognitives,
  neurosciences ;
- **(b) recherche en intelligence artificielle** — mémoire des agents, agents compagnons ;
- **(c) déclinaisons** — ce que chaque usage (coach, tuteur, conseiller, soutien…) exige ou rend
  imaginable.

S'y ajoutent le film *Her* lui-même, parcouru en entier comme spécification d'un produit rêvé
(24 capacités relevées), et deux passes critiques de complétude sur le tableau fusionné.
**Aucun filtre de faisabilité n'a été appliqué à ce stade** : c'était la règle — on décrit
d'abord ce qu'il faudrait savoir faire, on regarde ensuite ce qui est faisable.

**≈ 180 dimensions brutes ont été fusionnées en 56 lignes**, numérotées D00 à D55, numérotation
figée le 04/08/2026. (Le document de cartographie écrit « ~180 » : le compte exact des brutes
avant fusion n'a pas été arrêté, et il ne s'écrit donc pas ici comme un chiffre rond.)

### Le critère d'arrêt, et sa réserve

L'arrêt s'est fait à **saturation** : trois sources consécutives sans nouveauté, par direction,
avec une exigence plancher de deux revues systématiques ouvertes par direction.

| Direction | Sources consultées / ouvertes | Saturation |
|---|---|---|
| (a) sciences du lien — relations ; cognition et neurosciences | 19/14 et 34/21 | atteinte (3 et 5 dernières sans nouveauté) |
| (b) recherche IA — mémoire ; compagnons | 14/12 et 18/18 | atteinte (3 et 5) |
| (c) déclinaisons — sport et vie ; psy et conseiller ; tuteur et compagnon | 31/27, 17/15, 15/14 | atteinte (3 chacune) |
| Film *Her* | 7/5 pages de vérification | sans objet — film parcouru en entier |
| Passes critiques de complétude | 10/9 | **les deux ont trouvé du nouveau : 26 manques, tous intégrés** |

**La réserve, écrite telle qu'elle a été écrite à l'époque** : le critère par direction est
atteint, mais la passe de complétude a encore produit 26 dimensions manquantes. **Une seconde
passe critique sur le tableau fusionné n'a pas été relancée.** On ne peut donc pas affirmer que
la liste est close — seulement qu'elle ne bougeait plus dans chaque direction prise séparément.

---

## 2. Le gate des citations

Chaque fiche cite au format `[Auteur, année, arXiv:… ou DOI:…]`. Un script — `tools/check_citations.py` —
extrait toutes les citations et interroge, dans l'ordre, arXiv, Crossref puis Semantic Scholar.
Chaque citation ressort dans un de trois états :

- **RESOLUE** — l'identifiant existe, et le premier auteur **et** l'année concordent avec ce que
  la fiche écrit ;
- **DISCORDANTE** — l'identifiant existe mais l'auteur ou l'année ne correspond pas ;
- **INTROUVABLE** — inconnu des trois sources, **ou** échec réseau. Un échec réseau n'a jamais
  compté comme résolu : c'est la règle qui empêche un gate de se valider tout seul un jour où
  Internet tousse.

**Onze passes** ont été jouées entre le 4 et le 13 août 2026, une par lot de fiches, avec un
garde-fou anti-triche : si le nombre de citations uniques d'une fiche **baisse** entre deux
passes, la passe marque « REGRESSION » pour cette fiche — on ne fait pas monter un taux en
retirant les citations gênantes.

**Le résultat de la dernière passe, le 13/08/2026, sur les 56 fiches :**

| | |
|---|---|
| Citations uniques par fiche, additionnées | **1 412** |
| RESOLUE | **1 412** |
| DISCORDANTE | **0** |
| INTROUVABLE | **0** |
| REGRESSION | **0** |
| Identifiants distincts après dédup entre fiches | 1 203 |
| Occurrences totales | 1 722 |

Ces trois derniers comptes se rejouent hors ligne, sur les fiches de ce dépôt :
`python tools/importer_depuis_source.py --source <la source> --verifier`.

### Ce que le gate ne vérifie pas, et ce qui a été fait à la place

Le format de citation ne porte pas de titre : le gate contrôle l'identifiant, l'auteur et
l'année, **pas** l'adéquation entre ce que la fiche affirme et ce que le papier dit. Cette
seconde vérification a été faite **par tirage au sort à chaque lot** — graine fixée à la date du
jour, écrite avant tout jugement, une dizaine de citations par lot ouvertes et jugées à la main,
plus un croisement systématique des citations entre guillemets contre le texte de leur source.

Ce contrôle a trouvé de vraies fautes, et elles sont listées ici parce qu'un contrôle qui ne
trouve rien ne prouve rien :

- une citation entre guillemets attribuée à un travail de 2004 qui n'était **dans aucune** des
  339 sources du lot — retirée, passage reformulé (D50) ;
- un titre entre guillemets **qui n'existe pas**, en note d'en-tête d'une fiche — retiré et
  démenti en clair (D47) ;
- deux élisions non signalées dans des citations (« We **also** develop models… » écrit « we
  develop models… ») — rétablies (D49, D55) ;
- une citation attribuée à un auteur alors qu'elle était textuelle d'un autre — corrigée, et
  la correction vérifiée dans les deux sens (D14) ;
- sept citations qui **échappaient à la regex du gate** depuis la première passe, dont cinq
  sources réellement portées et jamais vérifiées — le motif a été corrigé et prouvé
  non régressif (0 citation perdue, 0 modifiée, 7 gagnées).

**Ce qui n'a pas été fait** : aucun texte intégral n'a été lu en entier pour les 1 412 ; les
résumés, les pages HTML et les extraits ciblés l'ont été. Aucune source hors anglais et français
n'a été cherchée.

---

## 3. La règle des cinq états

L'état d'une ligne **dans le pilote** (le coach sportif de l'auteur) est calculé par
`tools/etats_cdc.py`, jamais écrit à la main, et chaque état est adossé à une mesure de
production. Les cinq états, avec leur condition :

| État | Condition |
|---|---|
| **en service** | le cœur de la ligne est couvert par du code en service **et** une mesure de production **non nulle** en porte la trace |
| **acquis sans code** | obtenu par construction du cadre à une seule personne (payeur = utilisateur = opérateur), sans artefact dédié ; aucune mesure ne peut le prouver ni l'infirmer — il se déclare, avec sa raison |
| **outillé sans usage** | un artefact dédié au cœur existe dans le dépôt (table, outil, protocole, nommé) **et** la mesure attachée est **nulle** |
| **amorcé** | du code touche la ligne, avec une mesure non nulle, mais ne couvre pas son cœur |
| **à construire** | aucun artefact dédié, aucun code qui touche la ligne |

Le départage entre « outillé » et « à construire » tient à un seul fait : l'existence d'un
artefact **nommé** dans le dépôt, à mesure nulle. **Une consigne de prompt seule n'est pas un
artefact** — arbitrage du 13/08/2026, et c'est lui qui fait sortir une dizaine de lignes
relationnelles de « en service ».

**Comptes au 04/09/2026** : 3 en service · 2 acquis sans code · 3 outillés sans usage ·
16 amorcés · 32 à construire. Détail ligne par ligne dans `etats/etats.json`, rapport dans
`etats/etats_rapport.md`.

---

## 4. La réfutation de nouveauté

Le mot « inédit » ne s'écrit nulle part dans ce dépôt, et « personne n'a jamais » non plus. Avant
d'écrire quoi que ce soit qui ressemble à une revendication, quatre revendications ont été
soumises à une réfutation en deux tours, le **04/09/2026** : quatre agents en contexte frais, une
revendication chacun, 15 à 32 requêtes et 11 à 18 pages ouvertes par agent, puis un contrôle
direct par une requête neuve sur chaque verdict négatif.

Deux règles gouvernent ce tableau :

- **contrôle anti-écho** — les voisins cherchés **et écartés** sont listés, sinon « rien trouvé »
  ne se distingue pas de « mal cherché » ;
- **barre du doute raisonnable** — un voisin qui couvre la moitié de l'objet retire le droit
  d'écrire « sans équivalent » ; on écrit alors « le plus proche est… ».

| Revendication | Verdict | Voisin qui décide | Part de l'objet couverte |
|---|---|---|---|
| **(a1)** le biais de complaisance vient de *mois* de portrait intime, pas d'une opinion du tour | **déjà fait** | Jain et al., arXiv:2509.12517 (CHI 2026) : le profil-mémoire condensé est le contexte qui fait le plus monter la sycophancie ; MemSyco-Bench arXiv:2607.01071 ; OP-Bench arXiv:2601.13722 ; arXiv:2607.10526 | hypothèse établie, sous-champ actif depuis janvier 2026 |
| **(a2)** juger à l'aveugle, puis livrer avec tact (deux appels) | **le plus proche est** Christian & Mazor, arXiv:2601.14553 (21/01/2026) | la baseline elle-même : architecture à deux appels, un appelé aveugle, sycophancie mesurée | ≥ 50 % |
| **(a3)** mesure longitudinale sur une personne, juge convergent, sur des questions où la réponse honnête est mal reçue | **sans équivalent trouvé** pour la combinaison | Lee et al., arXiv:2509.26593 (une personne, coach de course, 2 mois, **aucune** mesure de sycophancie) ; Keough, arXiv:2606.05183 (juge convergent, mais entre générations de modèles) | chacun ≈ la moitié d'une moitié |
| **(b)** un cahier des charges à 56 lignes spécifiées (mécanisme humain, comportement attendu, état de l'art, trous ; citations vérifiées par script) | **sans équivalent trouvé** | DeepMind, arXiv:2404.16244 (portée thématique, ~15-20 %) ; Rogge et al., DOI:10.1007/s12369-023-01031-y (structure la plus proche, ~10 %) ; **CompanionBench**, arXiv:2608.02046 (03/08/2026 ; 10 capacités ancrées sur 25 théories, ni état de l'art ni trous par capacité, ~10-15 %) | ≤ 20 % |
| **(c)** un audit de couverture ligne à ligne de systèmes déployés | **sans équivalent trouvé** dans la littérature publiée ; **des comparatifs commerciaux existent** | CDT, *Dark Patterns in AI Chatbots* (mai 2026 ; nuisances, pas capacités) ; comparatifs de blogs 2026 (5 à 13 produits, mémoire / sécurité / prix, ~20-25 %) ; Rauh et al., arXiv:2605.08093 ; CompanionBench (28 **modèles**, pas des produits déployés) | ≤ 25 % |
| **(d1)** le tri obstacle économique / obstacle technique, ligne par ligne, sur un référentiel de capacités | **sans équivalent trouvé** | Knox et al., arXiv:2511.14972 (chaîne cause économique → trait → préjudice, **en négatif**, ~20 %) ; Public Citizen (27/01/2026) ; Chu et al. arXiv:2606.04431 ; De Freitas et al. arXiv:2508.19258 | ≤ 20 % |
| **(d2)** un déploiement personnel pour une personne, instrumenté sur des mois | **le plus proche est** Lee et al., arXiv:2509.26593 (~30 %) | plus : une autoethnographie d'un système personnel sur Claude, 18 itérations, juillet 2025 → janvier 2026 (~25 %, page non ouverte, 403) ; Wu, arXiv:2606.14589 ; Hwang et al. arXiv:2510.10079 | 30 % |

**Ce qui tombe** : (a1) entièrement ; (a2) presque entièrement — il reste un point de conception
étroit, non mesuré. **Ce qui tient** : (b), (c) au sens académique, (d1), et la **conjonction**
(d1 + d2) sur un même système, qu'aucun voisin ne fait.

**L'écart d'incitation n'est pas une découverte de ce travail** : il est établi par De Freitas
2025, Knox et al. 2025, Chu et al. 2026 et Public Citizen 2026. Ce qui est ajouté ici est le tri,
ligne par ligne, contre un système qui tourne.

> **Ce tableau est daté du 04/09/2026 et il sera rejoué la semaine de la publication.** Le domaine
> publie chaque semaine — CompanionBench le 03/08/2026, MemSyco-Bench et « Agents Don't Just
> Agree, They Remember » en juillet. Un tableau de voisins vieux d'un mois est un tableau faux.
> **Limites de cette veille** : résumés et pages HTML seulement, aucun texte complet lu en entier ;
> aucune littérature hors anglais et français ; quatre agents, aucune deuxième passe indépendante
> sur le même objet.

---

## 5. Ce que ce dépôt n'établit pas

- **« Absent de tout système public » est le verdict d'un seul évaluateur**, daté du 21/08/2026.
  Il ne vaudra qu'avec l'accord de deux juges de plus (`couverture/kit_juges.md`), et il sera
  rejoué la semaine de la publication : deux des dix-sept lignes vacillent déjà.
- **« À portée de main » est un arbitrage**, rendu le 14/08/2026, pas une démonstration. La
  démonstration sera chaque brique passée en service, avec sa mesure non nulle.
- **L'incitation comme cause n'est pas une découverte de ce texte.** Elle est établie ailleurs ;
  ce travail la trie, ligne à ligne, contre un système qui tourne.
- **Le pilote n'est pas un compagnon** : c'est un coach sportif, seule déclinaison instanciée,
  trois lignes en service sur 56, et **aucune des dix-sept lignes absentes partout n'y est en
  service**. Les douze « à portée de main » restent à portée, pas obtenues.
- **La mesure de production ne peut pas être rejouée par un tiers** : elle lit la base du pilote,
  qui n'est pas fournie. Ce qui est publié, ce sont ses sorties datées et le script qui les a
  produites (`instruments/`).
