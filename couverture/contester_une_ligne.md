# Contester une ligne

Ce dépôt publie des verdicts qui peuvent être faux. La procédure ci-dessous existe pour qu'on
puisse les attaquer sans nous écrire, et pour que la contestation soit tranchable par n'importe
qui d'autre que nous.

## Ce qui se conteste, et avec quoi

| Ce que vous contestez | Ce qu'il faut produire | Où est la matière |
|---|---|---|
| **Une note de couverture** (« couvert », « partiel », « absent » pour une ligne) | Le **produit**, sa **version ou la date** à laquelle vous l'avez observé, et la **fonction précise** qui fait la couverture. Sans produit nommé, la note reste `absent`. | `couverture/tableau_couverture.md`, et la fiche dans `dimensions/` |
| **Un classement** (déjà fait / existe / développable / LIMITE) | Le travail publié, ou le produit, qui classe la ligne autrement — et en quoi il touche le **cœur** de la ligne, pas sa périphérie | `mapping_8_verrous.md`, et le §5 de la fiche |
| **Un verrou racine** (V1 à V8) | Une mesure qui contredit celle citée, ou une ligne mal rattachée | `mapping_8_verrous.md` §5 |
| **Une citation** | L'identifiant, et ce qui cloche : auteur, année, ou surtout ce que la fiche lui fait dire | `bibliographie.md`, et la fiche |
| **Une revendication de nouveauté** | Le voisin qu'on a manqué, avec son identifiant et la part de l'objet qu'il couvre | `note_methode.md` §4 |
| **Le périmètre lui-même** (une ligne manque, ou deux n'en font qu'une) | La capacité manquante, décrite comme les autres : mécanisme humain, comportement attendu, ce qui l'établit | `dimensions/` pour le gabarit |

## Le gabarit

Ouvrez une *issue* sur le dépôt, ou envoyez ce bloc rempli. Les cinq premiers champs sont nécessaires,
le sixième est facultatif : sans le troisième, la contestation n'est pas tranchable ; sans le cinquième, elle n'est pas
datée, donc elle périmera sans qu'on sache quand.

```
LIGNE          : Dnn (ex. D22 Fin de relation)
CE QUE JE      : (ex. « la note `absent` de la couverture », « le rattachement de D18 à V7 »)
CONTESTE
LA PREUVE      : produit + version ou date + fonction précise
                 OU identifiant du travail (arXiv:… / DOI:…) + ce qu'il montre
CE QUE ÇA      : (ex. « la ligne passe de `absent` à `partiel` », « le verrou V7 ne
CHANGE           l'explique pas »)
OBSERVÉ LE     : jj/mm/aaaa — la date compte : le domaine bouge chaque semaine
QUI JE SUIS    : facultatif, mais dites si vous avez un intérêt dans le produit cité
```

## Comment c'est traité

1. **Toute contestation qui porte les cinq champs obligatoires entre au tableau**, y compris quand elle nous
   donne tort — c'est le point de la procédure.
2. Une contestation sur une **note de couverture** est traitée comme une note de juge : elle ne
   remplace pas la note existante, elle s'ajoute, et le compte publié reste celui du vote
   majoritaire des trois juges (`kit_juges.md`).
3. Une contestation sur une **citation** est vérifiée par le gate
   (`python tools/check_citations.py`) puis à la main sur la source. Si elle est fondée, la
   fiche est corrigée, la correction est datée, et la version d'avant reste dans l'historique.
4. **Ce qui est refusé, et pourquoi** est écrit aussi. Un dépôt qui n'affiche que les
   contestations qu'il a acceptées ne prouve rien.

## Ce qu'on ne peut pas trancher

- **Les mesures du pilote** ne sont pas reproductibles par un tiers : elles lisent une base
  privée, qui n'est pas fournie. Le script est publié, ses sorties sont datées, mais vous ne
  pouvez pas les rejouer — vous pouvez seulement contester ce qu'on en conclut.
- **La complétude des 56 lignes** ne se démontre pas. On peut montrer qu'une ligne manque ; on ne
  peut pas montrer qu'aucune ne manque. La note de méthode dit où l'arrêt a été décidé, et avec
  quelle réserve.
