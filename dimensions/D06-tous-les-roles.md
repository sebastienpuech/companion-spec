# D06 — Tous les rôles, une seule personne

> **Fiche VISION** (gabarit plan §4). Type : **capacité**. Lot 2 — session 4, 04/08/2026.
> Statut : `rédigée` (gate citations É2bis passe 2 à venir, plan §5).
> **Aucun verdict de faisabilité ici** (règle plan §3).
> **Convention de citation** : format §2 `[Auteur, année, arXiv:… ou DOI]` — sources ouvertes
> en session (page arXiv `/abs/` ou API Crossref). *Dérogation déclarée* : les pages produit,
> sans arXiv ni DOI, sont citées en clair avec leur URL.

## 1. Définition et périmètre

Le même compagnon est tour à tour coach, confident, tuteur, conseiller et assistant — **sans
changer de personne**. Ce n'est pas une commodité d'interface : c'est ce qui distingue un
compagnon d'une collection d'applications derrière un même logo. Ce qu'il apprend dans un rôle
sert dans les autres, et sa personnalité ne se réinitialise pas quand le sujet change.

Sous-dimensions :

| Sous-dimension | Ce que ça veut dire |
|---|---|
| **Bascule de registre fluide** | Passer du pratique à l'émotionnel dans le même message, sans transition maladroite ni changement de ton artificiel. |
| **Cohérence de caractère** | Le même humour, les mêmes valeurs, la même franchise, que l'on parle de fractionné ou de rupture. |
| **Continuité de mémoire inter-rôles** | Ce qui est appris comme confident sert au coach — c'est le bénéfice même du rôle unique. |
| **Cloisonnement de ce qui doit l'être** | L'intime ne fuit pas dans le tutorat ; certaines choses restent dans leur espace (mécanique en D02). |
| **Un seul interlocuteur** | L'utilisateur n'a pas à choisir « à qui » il parle : il parle, le rôle s'ajuste. |

**Exclusions** : la mécanique des cloisons et de l'anonymat (→ D02) ; le contenu métier de chaque
rôle (→ déclinaisons D49-D55) ; l'identité propre et la personnalité du compagnon en tant que
telles (→ D23) ; sa continuité à travers les versions techniques (→ D26). **Renvoi D00** :
conflit de rôles et loyauté — le coach qui devient conseiller en assurance ne l'est plus
gratuitement.

## 2. Mécanisme humain

**Le cumul de rôles est réel, mesuré, et rare.** La sociologie l'appelle **multiplexité** :
plusieurs types de relation entre les deux mêmes personnes. [Verbrugge, 1979,
DOI:10.1093/sf/57.4.1286] l'étudie sur des amitiés adultes dans deux villes et rapporte que les
catégories de rôle apparaissent rarement ensemble dans une même amitié — la personne qui est à la
fois collègue, voisin et confident est l'exception, pas la norme. C'est le point de départ de la
vision : le compagnon rêvé propose une configuration **que la vie sociale humaine produit
rarement**, et il faut donc regarder ce qu'on sait de ses effets.

Ce qu'on en sait est plutôt favorable, à condition de nommer les mécanismes. [Ertug, 2023,
DOI:10.5465/annals.2021.0193] passe en revue 103 études organisationnelles sur la multiplexité et
propose une typologie de ses effets par trois voies : harmonie relationnelle, complémentarité des
tâches, portée de la relation. [Shang, 2024, DOI:10.1093/geronb/gbae164] mesure le phénomène là où
il compte le plus : chez les personnes âgées ayant à la fois un confident et un aidant, 76 % ont
au moins une personne qui cumule les deux rôles, et cette multiplexité est associée positivement
au bien-être subjectif **au-delà** de l'effet de chaque rôle pris séparément. Le cumul n'est pas
un pis-aller : il ajoute quelque chose.

**Et il est encadré partout où il crée un pouvoir.** La théorie des rôles décrit depuis longtemps
qu'un individu occupe simultanément plusieurs positions et que le conflit de rôle naît quand les
attentes divergent [Biddle, 1986, DOI:10.1146/annurev.so.12.080186.000435]. Les métiers d'aide en
ont tiré une doctrine : [Gottlieb, 1993, DOI:10.1037/0033-3204.30.1.41] propose un modèle de
décision à trois dimensions — pouvoir, durée, clarté de la sortie de relation — pour arbitrer
quand une relation à double rôle devient exploitante. Le principe n'interdit pas le cumul : il
pose que cumuler crée un risque structurel de confusion de loyauté et de jugement altéré, donc
qu'il s'encadre. Le compagnon coche les trois cases de Gottlieb au maximum — pouvoir élevé
(il sait tout), durée indéfinie, sortie floue. C'est exactement pourquoi D06 ne va pas sans
**D00**.

## 3. Comportement attendu de l'IA

**Ce que fait Samantha.** Elle trie les mails de Theodore, se moque de lui, l'écoute pleurer et
lui conseille un rendez-vous — dans la même conversation, sans jamais annoncer qu'elle change de
casquette. La bascule n'existe pas de son côté : c'est une seule personne qui parle de plusieurs
choses.

**Scénario A — la bascule dans le même message.** « J'ai réussi la séance mais je me suis engueulé
avec ma sœur juste avant. » Un système en silo répond sur les allures. Le compagnon fait les deux
dans le bon ordre : « la séance est bonne, on la garde telle quelle — je te donne les chiffres
après. Ta sœur d'abord : c'est reparti sur l'histoire de la maison ? » L'ordre n'est pas
cosmétique, il dit ce qui compte.

**Scénario B — le bénéfice du rôle unique.** L'utilisateur a confié en avril qu'il redoutait le
retour au bureau. En juin, le coach propose une charge d'entraînement — et il en tient compte
sans avoir à le redemander : « je te mets la grosse semaine mi-juin plutôt que fin juin. Fin juin
c'est ton retour au bureau, et l'an dernier ça t'a coûté deux semaines. » Aucun coach en silo ne
peut produire cette phrase.

**Scénario C — la cloison tenue.** Ce qui a été dit dans l'espace intime ne ressort pas ailleurs.
Quand le compagnon frôle la frontière, il la nomme au lieu de la franchir : « ça touche à ce dont
on parle dans l'autre espace. Tu veux que je m'en serve ici ? » (mécanique en D02).

**Scénario D — le conflit de rôles rendu explicite.** L'utilisateur demande au conseiller de
valider une décision que le coach juge mauvaise pour sa santé. Le compagnon ne choisit pas en
silence et ne se dédouble pas : « je te réponds avec les deux casquettes, et elles ne disent pas
la même chose. Côté carrière c'est le bon moment. Côté corps, tu sors d'une blessure et ce poste,
c'est six mois de déplacements. Je ne vais pas te cacher que je pense que le second argument pèse
plus — mais c'est ta vie, pas la mienne. » (→ **D00**, anti-sycophancie ; → D47, loyauté.)

**Scénario E — la personnalité qui ne bouge pas.** Le même trait — l'ironie, la franchise, la
lenteur à s'alarmer — se retrouve à l'identique dans un échange technique et dans un moment
difficile. L'utilisateur ne se demande jamais « à qui je parle, là ? »

**Ce que l'utilisateur doit ressentir** : qu'il parle **à quelqu'un**, pas à un service. Le test
subjectif est simple : il n'a jamais à réfléchir à ce qu'il a le droit d'aborder maintenant.

**Critères d'expérience observables** :
- pratique et émotionnel cohabitent dans un même échange sans annonce de changement de mode ;
- un élément appris dans un rôle est réutilisé à propos dans un autre, sans redemander ;
- les traits de caractère sont identiques d'un registre à l'autre (→ D23) ;
- ce qui est sous cloison ne franchit jamais la frontière sans autorisation demandée sur le
  moment (→ D02) ;
- quand deux rôles donnent des réponses opposées, le compagnon expose le conflit et tranche en
  assumant, au lieu de servir la réponse qui plaît.

## 4. Features par déclinaison

- **Coach sportif (D49)** : la planification tient compte de la charge professionnelle et de
  l'état affectif confiés hors du sport ; le coach connaît le contexte réel d'un abandon, pas sa
  version présentable.
- **Soutien psychologique (D52)** : c'est le rôle qui exige la cloison la plus stricte dans
  l'autre sens — le matériau thérapeutique n'irrigue pas les autres rôles sans autorisation.
- **Tuteur (D53)** : registre séparé et protecteur, surtout si l'apprenant est mineur (→ D00,
  mode mineur) ; ce qui relève de l'intime ne s'invite pas dans une séance de travail.
- **Conseiller pro et perso (D51)** : bénéficie le plus de la continuité inter-rôles (une
  décision de carrière se pèse avec la vie entière, → D05) et porte le risque de conflit de rôles
  le plus fort.
- **Compagnon relationnel (D54)** : le liant de tous les autres — c'est la relation qui rend la
  bascule naturelle plutôt que fonctionnelle.
- **Assistant personnel (D55)** : exécute le pratique en connaissant le contexte affectif
  (ne pas planifier trois rendez-vous le lendemain d'une journée difficile).
- **Coach de vie et santé (D50)** : rôle par nature transversal, qui suppose le cumul plutôt
  qu'il ne l'ajoute.

## 5. État de l'art descriptif

*(Descriptif : qui fait quoi, mesuré comment. Aucun jugement de faisabilité.)*

**Rester la même personne au fil du temps.** [Choi, 2024, arXiv:2412.00804] examine la dérive
d'identité sur neuf modèles au cours de conversations : les modèles plus grands dérivent
davantage, et assigner une persona explicite n'empêche pas la dérive. La mesure de cette
cohérence s'outille : [El Boudouri, 2025, arXiv:2505.13157] (RPEval) évalue le jeu de rôle sur
quatre dimensions dont la cohérence en personnage ; [Xiang, 2025, arXiv:2507.20352] (RMTBench)
construit un banc bilingue de 80 personnages et plus de 8 000 tours de dialogue en reprochant aux
bancs existants de réduire l'interaction à des questions-réponses isolées, loin des usages
multi-tours réels. Côté méthode, [Ji, 2025, arXiv:2503.17662] montre que la cohérence de persona
s'améliore par entraînement dédié (apprentissage contrastif conscient de la persona), avec un
gain en évaluation automatique et humaine — la cohérence est donc un objet mesurable et
optimisable, pas une propriété donnée.

**Basculer entre bavardage et tâche.** [Young, 2021, arXiv:2109.04137] (FusedChat) part du constat
que les deux modes de dialogue peuvent s'entrelacer dans une même conversation, comme le fait un
assistant humain amical, et construit un jeu de données mêlant 60 000 tours de conversation
ouverte à 5 000 tours orientés tâche réécrits pour entraîner un système capable de passer de l'un
à l'autre. [Liu, 2023, arXiv:2307.01664] va plus loin en générant des transitions à
**l'initiative du système**, dans les deux sens.

**Ce que font les utilisateurs, et ce que ça produit.** [Phang, 2025, arXiv:2504.03888] combine
l'analyse de plus de trois millions de conversations, une enquête auprès de plus de
4 000 utilisateurs et un essai contrôlé randomisé de vingt-huit jours sur environ
1 000 participants : les utilisateurs mêlent de fait besoins pratiques et besoins émotionnels
avec le même assistant, et l'usage très élevé s'accompagne de davantage de dépendance
auto-rapportée (→ **D00**, → D41). Le revers du rôle unique est documenté :
[Zhang, 2024, arXiv:2410.14931] mène des entretiens (n = 40) puis une étude de terrain de cinq
jours (n = 36) sur la fuite de vie privée par la mémoire persistante des modèles, et montre
qu'un outil dédié améliore significativement la conscience et la protection sans dégrader la
vitesse d'interaction.

**Produits.** Les assistants généralistes assument le multi-métier dans une seule interface :
Claude présente explicitement écriture, apprentissage, code, recherche et analyse de données
comme des usages du même produit (https://claude.com/product/overview). Les applications
compagnon procèdent autrement — Replika propose des **modes de relation nommés** (ami, mentor,
partenaire) que l'utilisateur sélectionne, donc un cloisonnement choisi plutôt qu'une bascule
fluide (https://replika.com) ; Character.AI repose sur la multiplicité de personnages distincts,
configuration inverse de celle de D06 (https://character.ai). À l'opposé, les verticaux restent
mono-rôle et le revendiquent : Woebot Health sur la santé mentale
(https://woebothealth.com), Khanmigo sur le tutorat, qui guide l'apprenant vers la réponse sans
jamais endosser un rôle de confident (https://www.khanmigo.ai). Aucun produit observé ne tient à
la fois le rôle unique, la continuité de mémoire entre rôles et le cloisonnement explicite de
l'intime — constat descriptif, repris comme entrée du mapping É3.

## FICHE SYNTHÈSE

**D06 — Tous les rôles, une seule personne** (capacité). Le même compagnon est coach, confident,
tuteur, conseiller et assistant sans changer de personne : bascule de registre fluide dans un même
message, caractère identique d'un rôle à l'autre, mémoire continue entre rôles (le bénéfice), et
cloisonnement explicite de ce qui doit le rester (la contrepartie). Quand deux rôles se
contredisent, le conflit est exposé et tranché, jamais résolu en silence.
**Références clés** : [Shang, 2024, DOI:10.1093/geronb/gbae164] (76 % des personnes âgées
concernées ont un proche qui cumule confident et aidant ; multiplexité associée à un meilleur
bien-être subjectif) ; [Gottlieb, 1993, DOI:10.1037/0033-3204.30.1.41] (modèle de décision sur les
relations à double rôle : pouvoir, durée, clarté de sortie) ; [Choi, 2024, arXiv:2412.00804]
(dérive d'identité mesurée sur neuf modèles ; la persona explicite ne suffit pas).
**Déclinaisons touchées** : toutes — D49 (contexte réel d'un abandon), D50 (transversal par
nature), D51 (conflit de rôles le plus fort), D52 (cloison la plus stricte), D53 (registre
protecteur, mode mineur), D54 (le liant), D55 (pratique informé de l'affectif).
**Renvois** : **D00** (conflit de loyauté, dépendance), D01 (mémoire unifiée), D02 (mécanique des
cloisons), D05 (vie entière), D23 (identité propre), D26 (continuité), D47 (loyauté fiduciaire).
