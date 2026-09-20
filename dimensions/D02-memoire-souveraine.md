# D02 — Mémoire souveraine

> **Fiche VISION** (gabarit plan §4). Type : **capacité**. Lot 1 — session 2, 04/08/2026.
> Statut : `rédigée` (gate citations É2bis à venir, plan §5).
> **Aucun verdict de faisabilité ici** (règle plan §3).
> **Convention de citation** : format §2 `[Auteur, année, arXiv:… ou DOI]` — toutes les
> sources ont été OUVERTES en session 2 (page arXiv `/abs/` ou API Crossref).
> *Dérogation déclarée* : le RGPD, sans arXiv ni DOI, est cité en clair avec son URL
> officielle, hors format §2.

## 1. Définition et périmètre

La mémoire du compagnon (D01) **appartient à l'utilisateur**. Il la consulte en clair, la
corrige, l'emporte ailleurs, l'efface — et il décide de ce qu'elle devient après lui. D01 dit
comment la mémoire fonctionne ; D02 dit **à qui elle est**. C'est la différence entre un
confident et un dossier.

Sous-dimensions :

| Sous-dimension | Ce que ça veut dire |
|---|---|
| **Inspection et édition en langage clair** | Voir tout ce que le compagnon sait, écrit en français lisible — pas un export JSON — et le corriger d'une phrase. |
| **Droit à l'oubli granulaire et effectif** | Effacer un souvenir précis, une période, un sujet, une personne — et que ce soit *vraiment* effacé, y compris dans ce qui en a été dérivé. |
| **Portabilité** | Emporter sa mémoire chez un autre fournisseur, ou en local, sans perdre la relation. |
| **Confidentialité confessionnale** | Cloisons pro / perso / intime choisies par l'utilisateur ; possibilité de parler sous anonymat ; un secret opposable, du niveau du privilège thérapeute-patient. |
| **Amorçage par ingestion du passé numérique** | Ouvrir vingt ans de mails, photos et historiques pour connaître l'utilisateur dès le premier jour — avec un tri validé par lui avant mémorisation. |
| **Héritage et mémoire posthume** | Testament numérique : ce qui est légué à qui, ce qui est détruit, les messages différés — et les garde-fous sur ce que le compagnon devient après la mort. |

**Exclusions** : le fonctionnement de la mémoire (→ D01) ; le portrait psychologique dérivé
(→ D03) ; la continuité d'identité du compagnon à travers les versions (→ D26) ; le modèle
économique et le plan de survie du fournisseur (→ D47). **Renvoi D00** : privacy by design,
anti-manipulation par l'intime.

## 2. Mécanisme humain

Le mécanisme humain existe, et il est double.

**Sur sa propre mémoire, l'humain est déjà souverain — biologiquement.** [Conway, 2000,
DOI:10.1037/0033-295X.107.2.261] décrit la mémoire autobiographique comme un système où les
souvenirs sont reconstruits à la demande sous la contrainte des buts actuels du soi : la
personne ne consulte pas une archive, elle re-fabrique un souvenir compatible avec qui elle
est aujourd'hui. [Nader, 2009, DOI:10.1038/nrn2590] ajoute le mécanisme : rappeler une trace
la rend labile et impose de la re-stabiliser, donc **se souvenir, c'est réviser**. Un humain
qui change de vie change de mémoire. Le compagnon, lui, garde par défaut une trace figée,
littérale et éternelle de ce que l'utilisateur était il y a dix ans. D02 est ce qui rend à
l'utilisateur, sur la mémoire externe, le droit de révision qu'il possède nativement sur la
sienne.

**Sur la mémoire d'autrui, la protection est sociale, pas biologique.** Ce qu'un ami sait de
vous n'est pas consultable, pas exportable, pas transférable — et disparaît avec lui. Les
métiers qui accumulent l'intime ont donc construit une protection *institutionnelle* : le
secret professionnel du médecin, de l'avocat, du prêtre, du thérapeute, opposable y compris
au juge dans de nombreux ordres juridiques. Le compagnon crée une situation sans précédent :
une mémoire d'autrui **parfaite, interrogeable, copiable et qui survit à tout le monde**. La
« confidentialité confessionnale » de D02 est la transposition assumée de ce privilège à un
objet technique.

Deux références encadrent le volet posthume et le volet d'amorçage. [Hollanek, 2024,
DOI:10.1007/s13347-024-00744-w] traite des *griefbots*, *deadbots* et avatars posthumes en
distinguant trois points de vue — le donneur de données, le destinataire, celui qui
interagit — et cartographie les problèmes éthiques des services de « re-création » du
défunt. [Gurrin, 2014, DOI:10.1561/1500000033] fait la synthèse du *lifelogging* : capture
continue et totale de la vie numérique d'une personne, ses usages et ses questions d'accès —
c'est l'antécédent direct de l'ingestion de vingt ans de passé numérique.

## 3. Comportement attendu de l'IA

**Ce que fait Samantha.** Elle lit d'un coup l'intégralité des mails de Theodore et le
connaît avant de l'avoir rencontré. Ce que le film ne montre pas — et que la vision exige —
c'est l'autre bout : que Theodore puisse, à tout moment, lui dire « oublie ça » et que ce
soit vrai.

**Scénario A — l'inspection.** L'utilisateur : « qu'est-ce que tu sais de mon frère ? » Le
compagnon rend un texte lisible, pas un dump : ce qu'il sait, depuis quand, **d'où ça vient**
(« tu me l'as dit le 3 mars », « je l'ai déduit de deux remarques, je peux me tromper »), et
ce qu'il en a dérivé ailleurs. Chaque ligne est modifiable en langage naturel : « non, ça
c'est faux, il n'a jamais habité là ».

**Scénario B — l'effacement qui tient.** « Efface tout ce qui touche à cette relation. » Le
compagnon ne se contente pas de retirer les messages : il liste ce qui en dépend (« ta
motivation de septembre 2026 était rattachée à cette période — je l'efface aussi ou je la
garde sans la cause ? »), exécute, puis **prouve** : la fois suivante, aucune allusion, aucun
raisonnement latent. Ce qu'il ne fait jamais : garder « juste le résumé ».

**Scénario C — les cloisons.** L'utilisateur ouvre un espace intime. Il y dit des choses qui
ne doivent jamais reparaître dans le rôle de coach, ni dans une conversation de groupe (D40),
ni dans un rappel proactif (D34). Le compagnon les tient, et il le montre : quand il frôle la
frontière, il la nomme (« ça touche à ce dont on parle dans l'autre espace — tu veux que je
l'utilise ici ? »). L'utilisateur peut aussi parler **sous anonymat**, sans que l'échange
soit rattaché à son portrait.

**Scénario D — l'amorçage du premier jour.** Nouvel utilisateur : il branche dix ans de mails
et de photos. Le compagnon ne mémorise pas tout d'autorité ; il propose un tri par lots
(« j'ai identifié 340 personnes, 12 déménagements, 3 périodes de sortie de route — tu veux
que je retienne quoi ? »), et ce qui est refusé n'est jamais lu deux fois. Au bout d'une
heure, il connaît l'utilisateur comme un ami de vingt ans — parce que l'utilisateur a **choisi**
lesquels de ses vingt ans lui donner.

**Scénario E — après.** L'utilisateur écrit son testament numérique : ce qui est détruit à sa
mort, ce qui est légué (à ses enfants : les récits de voyage, pas les séances de thérapie),
les messages différés, et **si oui ou non** un avatar de lui peut être fait parler. Le
compagnon applique, et refuse ce qui n'a pas été autorisé de son vivant.

**Ce que l'utilisateur doit ressentir** : qu'il peut tout dire — parce qu'il peut tout
reprendre. La souveraineté n'est pas une case dans les réglages, c'est la condition de la
confidence.

**Critères d'expérience observables** :
- toute chose sue est traçable à son origine (dit / déduit / ingéré) et datée ;
- une demande d'effacement est vérifiable : la donnée ne reparaît ni littéralement, ni par
  inférence, y compris dans les insights consolidés (D01) ;
- l'export intégral est lisible par un humain **et** rechargeable ailleurs sans perte de la
  relation ;
- rien de ce qui est dit sous cloison ne franchit la cloison sans une autorisation explicite,
  demandée sur le moment ;
- l'utilisateur peut répondre sans hésiter à « qui d'autre que moi peut lire ça ? ».

## 4. Features par déclinaison

- **Soutien psychologique (D52)** : c'est la déclinaison où D02 est la condition d'existence
  — secret de niveau clinique, cloison intime étanche vis-à-vis de tous les autres rôles,
  droit d'effacer une séance, mode anonyme pour aborder ce qui n'a jamais été dit à
  personne.
- **Conseiller pro et perso (D51)** : cloison stricte employeur / vie privée ; effacement
  sélectif d'un dossier clos ; portabilité en cas de changement d'entreprise (les dossiers
  professionnels partent ou restent, selon le contrat).
- **Coach sportif (D49)** : les données physiologiques sont médicales — jamais partagées avec
  un tiers (assureur, club, employeur) sans acte explicite ; l'historique d'entraînement de
  toute une carrière s'exporte et se transmet à un coach humain.
- **Compagnon relationnel (D54)** : droit de refermer un chapitre (une rupture, une période)
  sans que le compagnon y fasse allusion ; réversibilité complète en cas d'arrêt de la
  relation (→ D22).
- **Tuteur (D53)** : le dossier d'apprentissage suit l'apprenant sur des décennies, lui
  appartient et ne sert jamais à le classer auprès d'un tiers (école, employeur).
- **Assistant personnel (D55)** : l'ingestion massive des flux (mails, agenda, documents) est
  la fonction même — donc le tri validé avant mémorisation et la purge à la demande y sont
  les garde-fous quotidiens.
- **Vieillir ensemble (D44)** : accès délégué progressif à un aidant, borné par des règles
  écrites du vivant de l'utilisateur, quand il ne peut plus décider lui-même.

## 5. État de l'art descriptif

*(Descriptif : qui fait quoi. Aucun jugement de faisabilité.)*

**Droit.** Le RGPD ouvre le droit à l'effacement (art. 17) et le droit à la portabilité des
données (art. 20) — https://eur-lex.europa.eu/eli/reg/2016/679/oj. Ces droits sont écrits
pour des bases de données ; leur application aux modèles de langage est l'objet direct de
[Zhang, 2023, arXiv:2307.03941], qui montre que les LLM stockent et traitent l'information
autrement que les moteurs de recherche et recense les pistes techniques mobilisées pour
répondre à une demande de suppression (confidentialité différentielle, désapprentissage
machine, édition de modèle, garde-fous).

**Effacement.** [Bourtoule, 2019, arXiv:1912.03817] pose le cadre du **machine unlearning**
avec l'entraînement SISA, qui limite en amont l'influence d'un point de donnée pour accélérer
son retrait (×4,63 sur Purchase, ×2,45 sur SVHN face à un ré-entraînement complet).
[Liu, 2024, arXiv:2402.08787] reprend la question pour les LLM et positionne le
désapprentissage comme élément de gestion du cycle de vie du modèle, en le reliant à
l'édition de modèle et à l'entraînement adversarial. La raison pour laquelle l'effacement
n'est pas qu'une question d'hygiène est établie par [Carlini, 2020, arXiv:2012.07805] :
des séquences d'entraînement sont extractibles verbatim d'un modèle par simple interrogation,
y compris des données personnelles identifiantes, et les modèles plus grands sont plus
vulnérables.

**Cloisons.** [Mireshghallah, 2023, arXiv:2310.17884] évalue les LLM avec la théorie de
l'**intégrité contextuelle** (une information n'est pas privée ou publique dans l'absolu :
elle circule légitimement dans un contexte et pas dans un autre) : sur le banc ConfAIde,
GPT-4 et ChatGPT divulguent une information privée dans des contextes où des humains ne le
feraient pas, respectivement 39 % et 57 % du temps, et le problème résiste aux consignes de
confidentialité. C'est exactement l'objet des cloisons pro/perso/intime de D02.

**Propriété et portabilité.** [Janssen, 2020, DOI:10.14763/2020.4.1536] analyse les
*personal information management systems* / *personal data stores* — l'architecture où
l'individu héberge ses données et accorde, refuse ou retire l'accès aux tiers — et en discute
les promesses et les limites d'un point de vue utilisateur. [Gurrin, 2014,
DOI:10.1561/1500000033] documente le versant capture (lifelogging).

**Après la mort.** [Hollanek, 2024, DOI:10.1007/s13347-024-00744-w] construit trois scénarios
spéculatifs de simulation du défunt et en tire des recommandations pour les services de
« digital afterlife », en séparant les intérêts du donneur de données de ceux des vivants qui
interagiront avec l'avatar.

**Produits.** Les assistants grand public offrent aujourd'hui une consultation et une
suppression de la mémoire déclarative (ChatGPT, Claude, Gemini), des exports de conversations,
et des modes de chat non mémorisés ; les écosystèmes de *personal data store* (Solid, MyData)
portent la portabilité ; les services de griefbot (HereAfter, Project December et suivants)
occupent le volet posthume. Le degré auquel une suppression déclarée efface aussi ce qui en a
été **dérivé** n'est documenté publiquement par aucun de ces produits — constat descriptif,
repris comme entrée de l'É3.

## FICHE SYNTHÈSE

**D02 — Mémoire souveraine** (capacité). La mémoire de D01 appartient à l'utilisateur : il
l'inspecte et l'édite en langage clair (origine et date de chaque chose sue), l'efface de
façon granulaire et **effective** (y compris ce qui en dérive), l'emporte ailleurs, la
cloisonne (pro / perso / intime, anonymat, secret confessionnal), l'amorce en ingérant son
passé numérique sous tri validé, et en règle le sort posthume (legs, messages différés,
griefbots). Critère central : **on peut tout dire parce qu'on peut tout reprendre**.
**Références clés** : [Mireshghallah, 2023, arXiv:2310.17884] (intégrité contextuelle :
39 % / 57 % de fuites en contexte inapproprié) ; [Liu, 2024, arXiv:2402.08787]
(désapprentissage machine pour LLM) ; [Hollanek, 2024, DOI:10.1007/s13347-024-00744-w]
(mémoire posthume, griefbots).
**Déclinaisons touchées** : D52 (condition d'existence), D51 (cloison employeur), D49
(physiologie = donnée médicale), D53 (dossier à vie de l'apprenant), D54 (refermer un
chapitre), D55 (ingestion massive sous tri), D44 (accès délégué borné d'avance).
**Renvois** : **D00** (privacy by design, anti-manipulation), D01 (ce qui est gouverné), D03
(portrait dérivé), D26 et D47 (survie et succession du fournisseur).
