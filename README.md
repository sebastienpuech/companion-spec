# companion-spec

Un cahier des charges du compagnon artificiel : 56 capacités spécifiées, confrontées ligne à
ligne aux systèmes déployés.

### Le propos

Depuis le film Her (2013), l'idée d'un compagnon artificiel qui nous connaîtrait mieux que personne paraissait relever d'un futur lointain ; à chaque génération de modèles, elle semble pourtant se rapprocher, au point que la question n'est plus de savoir si une telle chose est possible, mais jusqu'où il est déjà possible d'aller. Ce travail part de là, en écartant d'emblée ce qui relève d'autres capacités (la voix, la vision, le corps) pour ne garder que le cœur : un assistant qui, à force de nous côtoyer, retiendrait tout, comprendrait comment nous fonctionnons et saurait, sur n'importe quel sujet et à n'importe quelle heure, quoi dire, quoi anticiper, quoi taire ; un même socle, déclinable en coach, en conseiller, en tuteur, en directeur de cabinet, et non le seul compagnon sentimental auquel le film l'a réduit.

Ce qui rend une telle ambition pensable, c'est la mémoire. Nous parlons encore à des intelligences quasi amnésiques, dont les mémoires ajoutées (fiches, carnets, bases de notes…) ne donnent rien qui ressemble à une conversation avec quelqu'un qui se souvient ; pourtant ce sont ces couches de mémoire accumulées qui font une expérience, et c'est sans doute là, plus que dans la puissance des modèles, que se joue la prochaine étape. Il semble aussi que l'objectif doive être tenu serré : un tel assistant ne peut ni rendre dépendant, ni flatter, ni entretenir une forme d'attachement qui servirait un modèle économique plutôt que la personne (la Joi de Blade Runner 2049, qui dit tout ce que l'on veut entendre, en est le contre-modèle) ; mais il doit pouvoir, en même temps, nous comprendre mieux que personne.

### Ce qui a été fait

Plutôt que de se lancer dans un projet démesuré, ce travail a d'abord décomposé l'ambition en briques : 56 capacités, réparties en 8 blocs, chacune décrite par le mécanisme humain qu'elle imite, le comportement attendu, l'état de l'art et ce qui manque (avec, pour l'ensemble, 1 412 références vérifiées une à une par script, au 13 août 2026). Ces 56 lignes ont ensuite été confrontées aux produits existants, ligne à ligne : 8 sont couvertes, 31 partiellement, 17 absentes de tout système public (selon un premier évaluateur, le 21 août 2026 ; deux autres doivent le contester). Mais surtout, la même grille permet de noter en pour cent ce qu'un modèle, une offre ou un système couvre, c'est-à-dire de mesurer, génération après génération, à quelle vitesse ce qui exigeait hier un échafaudage sur mesure devient natif ; c'est l'objet du chapitre 9.

La thèse que ce parcours amène à défendre est somme toute modeste : sur les 17 capacités qu'aucun produit ne livre, 12 sont à portée de main, ou déjà acquises sans une ligne de code dès lors que celui qui paie, celui qui utilise et celui qui opère sont la même personne ; elles manquent au marché faute d'incitation, non de savoir-faire ; 3 relèvent encore de la recherche, 2 sont hors de portée. Et aucune des 17 n'est aujourd'hui en service, y compris chez nous.

### À qui cela s'adresse

À quiconque s'interroge sur la faisabilité d'un tel compagnon, sur le moment où il deviendra possible et sur l'endroit exact où nous en sommes ; à qui veut construire un assistant et cherche la liste de ce qu'il faut savoir faire ; à qui préfère choisir quelques blocs et les mettre en œuvre selon ses besoins, sans attendre le tout. J'ai fait tourner depuis mai 2026 un pilote, un coach sportif, dont 3 lignes sur 56 sont en service au 4 septembre 2026 ; il n'y a aucune valeur ajoutée technique à ce que je code une partie de ce projet, n'importe quel chercheur le ferait infiniment mieux, mais le retour d'une utilisation quotidienne, lui, ne s'obtient d'aucune autre manière. Ce texte a été écrit avec Claude Code et vérifié par des scripts ; les jugements et les arbitrages sont de l'auteur.

---

## Ce que contient ce dépôt

| Ce que vous cherchez | Où c'est | Ce que c'est |
|---|---|---|
| **Les 56 capacités, une par une** | `dimensions/` | 56 fiches, D00 à D55. Chacune : le mécanisme humain qu'elle imite, le comportement attendu, l'état de l'art, ce qui manque. Copiées à l'identique du dépôt de travail (sha256 comparé). |
| **Les références** | `bibliographie.md` | 1 203 identifiants distincts, 1 412 citations uniques par fiche, régénérées depuis les fiches. Chacune résolue par script : identifiant, premier auteur et année concordants. |
| **Qui couvre quoi, aujourd'hui** | `couverture/tableau_couverture.md` | Les 56 lignes notées `couvert` / `partiel` / `absent` contre les systèmes publics — **par un seul évaluateur, le 21/08/2026**. Deux juges de plus doivent le contester. |
| **Le kit pour noter à votre tour** | `couverture/kit_juges.md` | Les consignes, le tableau des 56 lignes avec leur définition, le gabarit de notes en JSON, et le script qui calcule l'accord (κ de Fleiss). |
| **Pourquoi 20 lignes ne sont pas faisables** | `mapping_8_verrous.md` | Le classement des 56 (déjà fait / existe / développable / LIMITE) et les **8 verrous racines** auxquels 19 des 20 LIMITE se ramènent, chacun avec les mesures qui l'établissent. |
| **Comment tout ça a été fait** | `note_methode.md` | Les trois directions de recherche et l'arrêt à saturation, le gate des citations et les fautes qu'il a trouvées, la règle des cinq états, la réfutation de nouveauté, et ce que ce dépôt n'établit pas. |
| **L'état d'un pilote réel** | `etats/etats.json` | Les 56 lignes vues depuis un coach sportif qui tourne depuis mai 2026 : 3 en service · 2 acquises sans code · 3 outillées sans usage · 16 amorcées · 32 à construire. |
| **Les instruments** | `instruments/`, `tools/` | Les scripts de mesure (production, tells d'écriture, provenance, accord entre juges) et leurs sorties datées. 47 tests. |
| **Les passages de l'essai déjà écrits** | `essai/` | La thèse et les limites, validées phrase par phrase. L'essai lui-même n'est pas encore publié. |

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
