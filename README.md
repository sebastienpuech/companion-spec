# companion-spec

> **English readers:** a summary is just below; the rest of this repository is in French.

## In English (summary)

**companion-spec** is a requirements document for an AI companion of the kind shown in the movie *Her*, taken as a foundation for a coach, a tutor, an advisor or a personal assistant rather than a romantic partner. Everything else in this repository is in French.

- **56 capabilities in 8 blocks** (memory, quality of the bond, lasting over time, presence, acting on real life…). Each sheet gives the human mechanism it imitates, the expected behaviour, the state of the art and what is missing. 1,412 citations, each checked by script (identifier, first author, year).
- **Coverage by shipping products, line by line: 8 covered, 31 partial, 17 with no coverage found** (21 August 2026). This is the verdict of a single rater, and that rater is a model. A model judge then rated the 56 lines on 20 September 2026, and again on 21 September (55 lines that time: D28 was left unrated): it agrees with itself only moderately (kappa 0.47), the "covered" count does not survive (8, then 1, then 6), and no human judge has rated yet. "Nothing found" does not mean "does not exist".
- **Only 9 lines have no coverage found under all three ratings (the first rater, then two runs of a model judge on 20 and 21 September 2026), and 7 of those 9 look buildable with today's models** (6 if D41 follows its 28 August reclassification); 1 needs research, 1 is years away. The earlier count, 12 of 17, did not survive re-running the judge. Why the market does not ship them (incentives, cost, reliability, priorities) is left open.
- **A one-person pilot**, a running coach in daily use since May 2026: 3 of 56 lines in service, each backed by a non-zero production measurement. None of those 9 lines is in service there either.
- **Status: an exploratory reference and a field report**, not a systematic review.

**Want to challenge a line?** See `couverture/challenge_a_line.md`: open an issue naming the product that covers it and why the verdict is wrong. The 56 lines, one sentence each, are in `THE_56_LINES.md`. The judges' kit (`couverture/kit_juges.md`) lets three raters re-score all 56 lines and computes their agreement.

---

## En français

Un cahier des charges du compagnon artificiel : 56 capacités spécifiées, confrontées ligne à
ligne aux systèmes déployés.

### Le propos

Depuis le film Her (2013), l'idée d'un compagnon artificiel qui nous connaîtrait mieux que personne paraissait relever d'un futur lointain ; à chaque génération de modèles, elle semble pourtant se rapprocher, au point que la question n'est plus de savoir si une telle chose est possible, mais jusqu'où il est déjà possible d'aller. Ce travail part de là, en mettant au second plan ce qui relève d'autres capacités (la voix, la vision, le corps, qui ont leurs lignes dans le cahier sans jamais en être le cœur) : un assistant qui, à force de nous côtoyer, retiendrait tout, comprendrait comment nous fonctionnons et saurait, sur n'importe quel sujet et à n'importe quelle heure, quoi dire, quoi anticiper, quoi taire ; un même socle, déclinable en coach, en conseiller, en tuteur, en directeur de cabinet, et non le seul compagnon sentimental auquel le film l'a réduit.

Ce qui rend une telle ambition pensable, c'est la mémoire. Nous parlons encore à des intelligences quasi amnésiques, dont les mémoires ajoutées (fiches, carnets, bases de notes…) ne donnent rien qui ressemble à une conversation avec quelqu'un qui se souvient ; pourtant ce sont ces couches de mémoire accumulées qui font une expérience, et c'est sans doute là, plus que dans la puissance des modèles, que se joue la prochaine étape. Il semble aussi que l'objectif doive être tenu serré : un tel assistant ne peut ni rendre dépendant, ni flatter, ni entretenir une forme d'attachement qui servirait un modèle économique plutôt que la personne (la Joi de Blade Runner 2049, qui dit tout ce que l'on veut entendre, en est le contre-modèle) ; mais il doit pouvoir, en même temps, nous comprendre mieux que personne.

### Ce qui a été fait

Plutôt que de se lancer dans un projet démesuré, ce travail a d'abord décomposé l'ambition en briques : 56 capacités, réparties en 8 blocs, chacune décrite par le mécanisme humain qu'elle imite, le comportement attendu, l'état de l'art et ce qui manque (avec, pour l'ensemble, 1 412 références dont un script a contrôlé une à une l'identifiant, le premier auteur et l'année, au 13 août 2026). Ces 56 lignes ont ensuite été confrontées aux produits existants, ligne à ligne : 8 sont couvertes, 31 partiellement, 17 sans couverture identifiée dans le relevé (un premier évaluateur, un modèle, le 21 août 2026 ; un juge modèle l'a renoté deux fois depuis, un juge humain doit encore le faire). Mais surtout, la même grille permet de noter en pour cent ce qu'un modèle, une offre ou un système couvre, c'est-à-dire de mesurer, génération après génération, à quelle vitesse ce qui exigeait hier un échafaudage sur mesure devient natif ; c'est l'objet du chapitre 9.

La thèse que ce parcours amène à défendre est somme toute modeste : sur les 9 capacités qu'aucune des trois notations du relevé ne trouve couvertes, 7 sont à portée de main, ou obtenues sans une ligne de code dès lors que celui qui paie, celui qui utilise et celui qui opère sont la même personne ; 1 relève encore de la recherche, 1 est hors de portée. Pourquoi le marché ne les livre pas reste ouvert : l'incitation, le coût d'exploitation et l'ordre des priorités se disputent l'explication. Et aucune des 9 n'est aujourd'hui en service, y compris chez nous.

### À qui cela s'adresse

À quiconque s'interroge sur la faisabilité d'un tel compagnon, sur le moment où il deviendra possible et sur l'endroit exact où nous en sommes ; à qui veut construire un assistant et cherche la liste de ce qu'il faut savoir faire ; à qui préfère choisir quelques blocs et les mettre en œuvre selon ses besoins, sans attendre le tout. J'ai fait tourner depuis mai 2026 un pilote, un coach sportif, dont 3 lignes sur 56 sont en service au 4 septembre 2026 ; il n'y a pas de valeur ajoutée technique à ce que je code moi-même une partie de ce projet, mais le retour d'une utilisation quotidienne, lui, ne s'obtient d'aucune autre manière. Ce texte a été écrit avec Claude Code, révisé avec Codex et vérifié par des scripts ; les jugements et les arbitrages sont de l'auteur.

---

## Ce que contient ce dépôt

| Ce que vous cherchez | Où c'est | Ce que c'est |
|---|---|---|
| **Les 56 capacités, une par une** | `dimensions/` | 56 fiches, D00 à D55. Chacune : le mécanisme humain qu'elle imite, le comportement attendu, l'état de l'art, ce qui manque. Copiées à l'identique du dépôt de travail (sha256 comparé). |
| **Les références** | `bibliographie.md` | 1 203 identifiants distincts, 1 412 citations uniques par fiche, régénérées depuis les fiches. Chacune résolue par script : identifiant, premier auteur et année concordants. |
| **Qui couvre quoi, aujourd'hui** | `couverture/tableau_couverture.md` | Les 56 lignes notées `couvert` / `partiel` / `absent` contre les systèmes publics — **par un seul évaluateur, le 21/08/2026**. Un juge modèle l'a renoté deux fois (20 et 21/09/2026) ; un juge humain doit encore le faire. |
| **Le kit pour noter à votre tour** | `couverture/kit_juges.md` | Les consignes, le tableau des 56 lignes avec leur définition, le gabarit de notes en JSON, et le script qui calcule l'accord (κ de Fleiss). |
| **Pourquoi 20 lignes ne sont pas faisables** | `mapping_8_verrous.md` | Le classement des 56 (déjà fait / existe / développable / LIMITE) et les **8 verrous racines** auxquels 19 des 20 LIMITE se ramènent, chacun avec les mesures qui l'établissent. |
| **Comment tout ça a été fait** | `note_methode.md` | Les trois directions de recherche et l'arrêt à saturation, le gate des citations et les fautes qu'il a trouvées, la règle des cinq états, la réfutation de nouveauté, et ce que ce dépôt n'établit pas. |
| **L'état d'un pilote réel** | `etats/etats.json` | Les 56 lignes vues depuis un coach sportif qui tourne depuis mai 2026 : 3 en service · 2 acquises sans code · 3 outillées sans usage · 16 amorcées · 32 à construire. |
| **Les instruments** | `instruments/`, `tools/` | Les scripts de mesure (production, tells d'écriture, provenance, accord entre juges) et leurs sorties datées. 106 tests au 21/09/2026. |
| **L'essai** | `essai/essai.md` | Le texte complet, avec en annexe le tableau des 56 lignes. Copié à l'identique du dépôt de travail (sha256 comparé). Trois renvois du texte (`statut_reel.md`, `scripts/annexe_56.py`, `docs/cdc/benchmark/`) pointent vers ce dépôt de travail, qui n'est pas publié. `these.md` et `limites.md` sont les deux passages validés en premier ; `these.md` garde la thèse du 06/09 (douze sur dix-sept), remplacée le 21/09 par le §5 de l'essai. |

**Ce qui n'est pas ici** : le code du pilote, sa base de données, et les documents de travail
internes. Ce dépôt publie la spécification et les verdicts, pas le système.

## Comment contester une ligne

C'est prévu, et c'est le point : `couverture/contester_une_ligne.md` donne le gabarit et dit ce
qui se conteste avec quoi. En deux mots — une note de couverture se conteste avec un **produit
nommé, sa version ou la date d'observation, et la fonction précise** ; un classement se conteste
avec le travail publié qui le contredit ; une citation se conteste avec son identifiant.

## Comment rejouer une mesure

```bash
# Les comptes du dépôt : 56 fiches identiques, 1 722 / 1 412 / 1 203 citations,
# 56 lignes de couverture, 0 donnée personnelle non arbitrée. N'écrit rien.
python tools/importer_depuis_source.py --source <chemin/vers/la/source> --verifier

# Rejouer la résolution des 1 412 citations (réseau requis, ~20 min).
python tools/check_citations.py

# Noter les 56 lignes à votre tour, puis calculer l'accord à trois juges.
python tools/notes_juges.py --gabarit          # écrit couverture/notes_juges.json
python tools/notes_juges.py --verifier couverture/notes_juges.json
python tools/notes_juges.py --vers-csv couverture/notes_juges.json --sortie out/notes.csv
python tools/accord_juges.py out/notes.csv --json couverture/accord_juges.json

# Les tests des instruments.
python -m pytest tools/tests -q
```

**Une mesure ne se rejoue pas** : celle de la production du pilote (`tools/mesure_prod_cdc.py`)
lit une base privée, qui n'est pas fournie. Le script et ses sorties datées sont publiés
(`instruments/`), pas la base.

## Transparence

Les 56 fiches ont été rédigées avec Claude Code, à partir de collectes menées par des agents en
contexte frais, et validées une par une, lot par lot. Les citations sont vérifiées par script,
et le script est ici. Les comptes de ce dépôt sortent de scripts, jamais de la main. Les
jugements, les arbitrages et les classements sont de l'auteur — et ce sont eux qui se contestent.

Ce que ce dépôt **n'établit pas** est écrit en clair : `note_methode.md` §5.

## Licence

Textes en **CC BY 4.0**, scripts en **MIT**. Répartition exacte dans `LICENSES.md`.
