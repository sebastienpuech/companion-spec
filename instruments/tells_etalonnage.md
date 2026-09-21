# Étalonnage du compteur de tells

`tools/mesure_tells.py` compte les marques d'écriture de modèle : tirets cadratins, antithèses
« …, pas … », triades en fin de phrase, chutes-slogans, débuts de phrase ou de paragraphe
répétés, tournures vides, et **paragraphes sans ancre factuelle**. Un compteur ne juge pas un
texte ; il donne des repères, et c'est l'étalonnage qui les rend lisibles.

Cinq textes, mesurés le 04/09/2026 pour les trois premiers et le 06/09/2026 pour les deux
derniers. Les deux documents internes ne sont pas publiés — seuls leurs compteurs le sont, parce
que ce sont eux qui donnent l'échelle.

**Cibles retenues** : ≤ 1 tiret cadratin pour 300 mots, ≤ 1 antithèse pour 1 000 mots, 0 triade,
0 chute-slogan, 0 tournure vide, 0 paragraphe sans ancre.

## Les cinq points d'étalonnage

| Texte | Mots | Tirets / 300 mots | Antithèses / 1 000 mots | Triades | Slogans | Phrase : moy. ± écart-type | Paragraphes sans ancre |
|---|---|---|---|---|---|---|---|
| **A** — document d'arbitrage interne, rédigé par un modèle | 15 833 | **5,0** (264) | 3,47 (55) | 6 | 0 | 21,7 ± 14,3 | 1 / 67 |
| **B** — prose de cadrage d'un rapport interne, rédigée par un modèle | 3 795 | 0,24 (3) | 2,90 (11) | 1 | 1 | 15,9 ± 10,5 | 3 / 29 |
| **Dictée** — texte dicté à l'oral par l'auteur, non publié | 858 | 0,0 (0) | 1,17 (1) | 0 | 1 | 29,6 ± 18,7 | 3 / 3 |
| **La thèse** — passage validé, publié (`essai/these.md`, version du 06/09 remplacée le 21/09) | 203 | **0,0** (0) | **0,0** (0) | 2 | 0 | 25,4 ± 23,8 | **0 / 1** |
| **Les limites** — passage validé, publié (`essai/limites.md`, version du 06/09 remplacée le 21/09) | 252 | **0,0** (0) | **0,0** (0) | 0 | 0 | 42,0 ± 19,1 | **0 / 1** |

## Ce que l'étalonnage montre

1. **Le tiret cadratin sépare nettement.** Le document A en porte 5 pour 300 mots, vingt fois la
   cible ; les textes publiés n'en portent aucun. C'est le signal le plus discriminant du lot.
2. **Il ne suffit pas.** Le document B est à 0,24 tiret — sous la cible — et reste un texte de
   modèle : ses antithèses (2,90 pour 1 000 mots) et ses trois paragraphes sans ancre le disent.
   Un seul compteur ne tranche rien.
3. **L'ancre factuelle est le compteur qui compte.** La dictée orale de l'auteur affiche 3
   paragraphes sans ancre sur 3 : à l'oral, on parle d'intentions. Les passages écrits validés
   sont à 0 sur 1 — chaque paragraphe porte une date, un compte ou une source.
4. **La variabilité des phrases n'est pas un défaut.** L'écart-type des passages publiés (23,8 et
   19,1 pour des moyennes de 25 et 42 mots) est proche de celui de la dictée. Un texte de modèle
   tend vers des phrases de longueur régulière ; ce n'est pas ce qu'on voit ici.
5. **Deux triades subsistent** dans le passage de la thèse. Elles ont été vues, et gardées : le
   compteur signale, il ne décide pas.

## Le protocole complet

Le compteur n'est qu'une des cinq gardes appliquées aux textes publiés. Les quatre autres :

- **la voix de l'auteur d'abord** — les passages sont écrits dans le style de ses propres écrits,
  mesuré sur un corpus de quatre textes à lui (5 890 mots, zéro tiret cadratin, phrases de 20 à
  50 mots très inégales). Ces textes ne sont pas publiés ; seule la mesure l'est ;
- **une ancre factuelle par paragraphe**, cible zéro paragraphe sans ;
- **les aveux gardés** — un par section, jamais lissé ;
- **le test à l'aveugle qui bloque** — des lecteurs en contexte frais lisent le texte, la phrase
  de transparence retirée, et répondent à trois questions dont « qui a écrit ça ? ». Un verdict
  « machine » renvoie le texte à la page. Passé le 06/09/2026 : trois lecteurs, trois
  « personne », aucun paragraphe sauté.

## Comment le rejouer

```bash
python tools/mesure_tells.py essai/these.md --plages 7-7 --titre "thèse"
python tools/mesure_tells.py essai/limites.md --plages 7-7 --titre "limites"
```

L'option `--plages` écarte l'en-tête du fichier pour ne mesurer que le corps du passage : c'est
elle qui reproduit exactement les chiffres du tableau ci-dessus. Sorties JSON dans
`instruments/tells_these.json` et `instruments/tells_limites.json`.
