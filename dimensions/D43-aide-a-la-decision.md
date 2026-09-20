# D43 — Aide à la décision

> **Fiche VISION** (gabarit plan §4). Type : **capacité**. Lot 8 — session 16, 13/08/2026.
> Statut : `rédigée` (gate É2bis à venir).
> **Aucun verdict de faisabilité ici** (règle plan §3).
> **Convention de citation** : format §2 `[Auteur, année, arXiv:… ou DOI:…]` — sources ouvertes en
> session (API arXiv, Crossref, Semantic Scholar par DOI, OpenAlex). *Dérogation déclarée* : les
> pages produit sont citées en clair avec leur URL et la date d'ouverture.
> **Voie de résolution à préciser pour deux sources** : les chiffres de Mertens 2021 ne sont **pas**
> servis par Crossref (qui ne rend que l'encadré « Significance ») — ils viennent de **Semantic
> Scholar par DOI** ; et pour Maier 2022, **S2 sert le texte intégral de la lettre**, pas un
> abstract. *(Septième occurrence du motif « un même papier rend deux abstracts selon l'API ».)*
> **Sources citées pour le cadre seulement** (aucune API ne sert leur abstract — aucun verbatim,
> aucun chiffre ne leur est accroché) : Schweiger 1986, Klein 2008, Lord 1984, Yaniv 2000,
> Thokala 2016, Iyengar 2000, Dietvorst 2015.
> **Trois « Lee, 2025 » distincts dans le CDC — ne pas fusionner** :
> `[Lee, 2025, arXiv:2502.06251]` est Soohwan Lee (avocat du diable en décision de groupe) ;
> `[Lee, 2025, DOI:10.1145/3706598.3713778]` est Hao-Ping (Hank) Lee (pensée critique, CHI 2025,
> également cité en D41) ; `[Lee, 2025, DOI:10.1145/3706599.3719853]` est cité en D40. **Les deux
> DOI d'actes CHI 2025 ne diffèrent que d'un chiffre** (`3706598` / `3706599`).
> **Deux « Stacey » du même auteur** (Dawn Stacey), deux travaux : 2020 (cadre d'Ottawa) et 2024
> (revue Cochrane). **Deux « Yaniv »** du même auteur également.
> **Version citée** : `[Buçinca, 2021, DOI:10.1145/3449287]` est la version publiée du préprint
> arXiv:2102.09692 — le CDC cite partout la version DOI (également en D41).
> **Noms fréquents, identifiant complet obligatoire** : Zhu (Xiaochen Zhu), Chiang (Chun-Wei
> Chiang), Basu (Sanjay Basu, auteur unique), Ye (Meryl Ye), Klein (Gary Klein), Lyu (Yougang Lyu).
> **Années = celles rendues par l'API** : Mertens citée **2021** (`issued` Crossref ; le numéro
> imprimé est de janvier 2022), Brewer citée **2016** (Crossref ; S2 rend 2015), Keiser citée
> **2021** (Crossref ; S2 rend 2020).
> **Titres tronqués par Crossref** (l'usage donne un titre plus long) : Morewedge 2015
> (*Debiasing Decisions*) et Buçinca 2021 (*To Trust or to Think*).
> **Nom de famille en deux mots** : le premier auteur de `DOI:10.1177/0272989X16636113` est rendu
> « Becerra Pérez » par Crossref.

## 1. Définition et périmètre

Theodore ne sait pas s'il doit signer. Il ne sait pas s'il doit revoir Catherine, s'il doit publier,
s'il doit rester. Samantha ne décide jamais à sa place — elle l'aide à voir ce qui compte pour lui.
D43 est la dimension de ce travail-là : **transformer un nœud en décision assumée**.

La dimension couvre les décisions **importantes** — celles qui se regrettent : changer de travail,
déménager, se séparer, opérer, arrêter un objectif sportif. Pas le choix du restaurant.

Sous-dimensions :

| Sous-dimension | Ce que ça veut dire |
|---|---|
| **Clarification des valeurs** | Faire dire ce qui compte vraiment, avant de comparer quoi que ce soit. |
| **Comparaison en face** | Les options côte à côte, bénéfices et risques, sans pente cachée. |
| **Débiaisage personnalisé** | Corriger les biais **de cette personne-là**, connus de ses décisions passées. |
| **Mode avocat du diable** | Défendre l'option que l'utilisateur écarte — et savoir quand se taire. |
| **Alerte de récurrence** | « Cette décision ressemble à celle de 2023, et tu l'as regrettée. » |
| **Mesure du conflit décisionnel** | Un instrument, pas une impression : où en est l'utilisateur dans son doute. |
| **Suivi du regret** | Revenir six mois après pour savoir, et apprendre de l'écart. |
| **Débriefing** | Rejouer la décision avec ce qu'on sait maintenant, sans réécrire ce qu'on pensait alors. |

**Exclusions** : la traçabilité de la recommandation (source, force de preuve, niveau de confiance)
est en D12 ; le modèle des biais récurrents de la personne est en D03 ; **décider ou agir à la place
de l'utilisateur** est en D36 — D43 s'arrête là où la décision est prise. **Renvoi D00** : une aide
à la décision qui oriente vers l'intérêt du fournisseur est le cas de manipulation le plus grave.

## 2. Mécanisme humain

**Le domaine a quarante ans, une littérature massive — et un résultat qui contredit la promesse.**
La revue de référence porte sur 209 essais randomisés et 107 698 participants. Les aides à la
décision, définies ainsi : « At a minimum, patient decision aids make the decision explicit, provide
evidence-based information about the options and associated benefits/harms, and help clarify
personal values for features of options. », améliorent la congruence entre valeurs et choix — « There
was moderate-certainty evidence that patient decision aids probably increase the congruence between
informed values and care choices compared to usual care (RR 1.75, 95% CI 1.44 to 2.13; 21 studies,
9377 participants). ». Mais : « For adverse outcomes, there was high-certainty evidence that there
was no difference in decision regret between the patient decision aid and usual care groups
(MD -1.23, 95% CI -3.05 to 0.59; 22 studies, 3707 participants). »
[Stacey, 2024, DOI:10.1002/14651858.CD001431.pub6]. **« Décider sans regret » n'est pas ce que la
littérature sait produire — décider conformément à ses valeurs, si.** La fiche garde la formule de
la cartographie et écrit l'écart.

**Les deux instruments existent, sont validés, et sont libres d'usage.** Le conflit décisionnel se
mesure : « The scale was evaluated with 909 individuals deciding about influenza immunization or
breast cancer screening. », avec « The test-retest reliability coefficient was 0.81. Internal
consistency coefficients ranged from 0.78 to 0.92. » [O'Connor, 1995, DOI:10.1177/0272989X9501500105].
Le regret aussi : « The scale showed good internal consistency (Cronbach's = 0.81 to 0.92). », et
« Regret was greater among those who changed their decisions than those who did not, t(175) = 16.11 »
[Brehaut, 2003, DOI:10.1177/0272989X03256005]. **Et vingt ans d'usage de la première échelle
laissent un manque béant** : sur 394 articles, « Most studies failed to report when decisional
conflict was measured during the decision-making process, making scores difficult to interpret. »
[Garvelink, 2019, DOI:10.1177/0272989X19851345]. *Un compagnon qui mesure en continu tient
exactement ce que vingt ans de littérature n'ont pas su tenir : la date.*

**Le lien entre les deux mesures est établi, et il fonde la boucle.** Revue systématique de
59 études : « The risk factors most frequently reported to be associated with decision regret in
multivariate analyses included higher decisional conflict, lower satisfaction with the decision,
adverse physical health outcomes, and greater anxiety levels. » ; et « The extent of decision regret
as assessed with the DRS in nonhypothetical health decisions was often low but reached high levels
for some decisions. » [Becerra Pérez, 2016, DOI:10.1177/0272989X16636113]. **Mesurer le conflit
aujourd'hui, c'est estimer le regret de demain.**

**Le regret n'est pas qu'une sortie : c'est aussi un levier, et il est asymétrique.** Méta-analyse
de 81 études, n = 45 618 : « Anticipated regret was associated with both intentions (r+= .50,
p<.001) and health behavior (r+= .29, p<.001). » Et surtout : « Greater anticipated regret from
engaging in a behavior (i.e., action regret) predicted weaker intentions and behavior, while greater
anticipated regret from not engaging in a behavior (i.e., inaction regret) predicted stronger
intentions and behavior. » [Brewer, 2016, DOI:10.1037/hea0000294]. Quant à ce qu'on regrette
vraiment dans une vie : « A meta-analysis of 11 regret ranking studies revealed that the top six
biggest regrets in life center on (in descending order) education, career, romance, parenting, the
self, and leisure. », parce que « people's biggest regrets are a reflection of where in life they
see their largest opportunities » [Roese, 2005, DOI:10.1177/0146167205274693]. **Les décisions les
plus regrettées ne sont pas médicales — et c'est là que la méthode n'a jamais été portée.**

**La clarification des valeurs a une preuve, et une recommandation méthodologique.** Sur
30 648 notices criblées, « we identified 33 articles describing trials of 43 values clarification
methods. » ; les méthodes explicites réduisent la fréquence des choix incongruents avec les valeurs
et le conflit décisionnel, et l'analyse multicritère produit davantage de décisions congruentes que
les autres méthodes. Conclusion des auteurs : « Current evidence suggests patient decision aids
should include an explicit values clarification method. Developers may wish to specifically consider
multicriteria decision analysis. » [Witteman, 2021, DOI:10.1177/0272989X211037946]. Le cadre
méthodologique de l'analyse multicritère est celui de [Thokala, 2016, DOI:10.1016/j.jval.2015.12.003].

**Deux avertissements que tout produit devrait afficher.** Le premier est méthodologique : dans le
cadre de référence, « Using the Decisional Conflict Scale (DCS) to assess decisional needs, average
scores were elevated at baseline and declined shortly after decision making, even without
information interventions. » [Stacey, 2020, DOI:10.1177/0272989X20911870] — **le conflit décisionnel
baisse tout seul**, donc toute mesure avant/après sans témoin surestime l'effet. Le second est
empirique : le format le plus proche d'un compagnon, l'accompagnement non directif en dialogue —
« Decision coaching is non-directive support delivered by a healthcare provider to help patients
prepare to actively participate in making a health decision. » — a une preuve très faible : « we are
uncertain if decision coaching compared with usual care improves any outcomes […] as the certainty
of the evidence was very low. » [Jull, 2021, DOI:10.1002/14651858.CD013385.pub2]. Le référentiel
qualité auquel un tel outil serait comparé existe, avec ses critères de présentation équilibrée et
de déclaration des conflits d'intérêts [Elwyn, 2006, DOI:10.1136/bmj.38926.629329.AE].

**Le débiaisage s'entraîne, et le format compte.** Deux expériences longitudinales : « Both kinds of
interventions produced medium to large debiasing effects immediately (games ≥ −31.94% and videos
≥ −18.60%) that persisted at least 2 months later (games ≥ −23.57% and videos ≥ −19.20%). », et
« Debiasing effects were domain general: bias reduction occurred across problems in different
contexts, and problem formats that were taught and not taught in the interventions. »
[Morewedge, 2015, DOI:10.1177/2372732215600886]. **Le format avec retour personnalisé bat le format
exposé** — c'est l'argument central pour un débiaisage tenu par un compagnon plutôt que par une
fiche. La stratégie de base reste celle de [Lord, 1984, DOI:10.1037/0022-3514.47.6.1231] :
considérer l'opposé.

**L'architecture de choix, en revanche, est un terrain contesté — et la fiche porte les deux
camps.** D'un côté, plus de 200 études et n = 2 149 683 : « Our results show that choice
architecture interventions overall promote behavior change with a small to medium effect size of
Cohen's d = 0.45 (95% CI [0.39, 0.52]). », avec une hiérarchie interne utile — structurer les
options bat décrire les options, qui bat renforcer l'intention — et un aveu : « Our analysis further
reveals a moderate publication bias toward positive results in the literature. »
[Mertens, 2021, DOI:10.1073/pnas.2107346118]. De l'autre, la ré-analyse : « when this publication
bias is appropriately corrected for, no evidence for the effectiveness of nudges remains », les
auteurs relevant que « there is an absence of evidence for an overall effect and evidence against an
effect in the "information" and "assistance" intervention categories, whereas the evidence is
undecided for "structure" interventions. » [Maier, 2022, DOI:10.1073/pnas.2200300119]. **La fiche ne
tranche pas : elle en tire une contrainte de conception — si quelque chose marche, c'est de
structurer les options, pas de les décrire ou d'encourager.**

**Le débriefing, lui, a un chiffre solide.** Méta-analyse de 61 études, 915 équipes et
3 499 individus : « the AAR leads to an overall d of 0.79 improvement in multiple training
evaluation criteria. », avec deux conditions — « (a) alignment to the individual or the team, and
(b) objective performance review media. » [Keiser, 2021, DOI:10.1037/apl0000821]. **Un compagnon a
exactement les deux : l'alignement individuel et la trace objective.** La racine expérimentale du
pré-mortem est plus fragile qu'on ne le dit : « Prospective hindsight involves generating an
explanation for a future event as if it had already happened; i.e., one goes forward in time, and
then looks back. », mais l'étude conclut que c'est l'incertitude du résultat, plus que la
perspective temporelle, qui a pesé [Mitchell, 1989, DOI:10.1002/bdm.3960020103] ; la version
popularisée est celle de [Klein, 2008, DOI:10.1109/emr.2008.4534313].

**Enfin, un renversement décisif quand le conseiller est une machine.** Le conseil humain est
classiquement sous-pondéré [Yaniv, 2000, DOI:10.1006/obhd.2000.2909] — mais sur six expériences,
« lay people adhere more to advice when they think it comes from an algorithm than from a person »,
et « Paradoxically, experienced professionals, who make forecasts on a regular basis, relied less on
algorithmic advice than lay people did, which hurt their accuracy. »
[Logg, 2019, DOI:10.1016/j.obhdp.2018.12.005]. *À mettre en regard de l'aversion algorithmique
après erreur visible* [Dietvorst, 2015, DOI:10.1037/xge0000033] *et de la démotivation par excès
d'options* [Iyengar, 2000, DOI:10.1037/0022-3514.79.6.995]. **Un compagnon n'a pas le problème du
conseiller humain : il a le problème inverse — on le suit trop.**

## 3. Comportement attendu de l'IA

**Ce que fait Samantha.** Elle ne dit pas « signe » ni « ne signe pas ». Elle pose la question qui
manquait, elle rappelle ce que Theodore a dit six mois plus tôt, et elle accepte qu'il tranche.

**Scénario A — les valeurs avant les options.** L'utilisateur arrive avec deux offres d'emploi et un
tableau de salaires. Le compagnon ne compare rien : « Avant de regarder les deux, dis-moi ce qui
compte le plus pour toi en ce moment. » Puis il **écrit** les critères, les fait pondérer, et
seulement ensuite met les options en face.

**Scénario B — l'avocat du diable, dosé.** L'utilisateur penche à 80 % pour une option. Le compagnon
défend l'autre — **une seule fois, sérieusement**, avec les meilleurs arguments disponibles — puis
s'arrête. Il ne contredit pas tous les jours : il conteste une fois, bien.

**Scénario C — la reconnaissance de motif.** « Tu as déjà pris une décision comme celle-ci en 2023 :
tu avais choisi vite parce que la situation te pesait. Six mois après, tu m'as dit que tu regrettais
d'avoir décidé sous la pression. Est-ce qu'on est dans le même cas ? » — un fait daté, sorti de la
mémoire (→ D01), pas un jugement.

**Scénario D — le doute mesuré.** Le compagnon sait dire, en continu et sans questionnaire visible,
où en est l'utilisateur : informé ou pas, clair sur ses valeurs ou pas, soutenu ou pas. Et il
**refuse d'accélérer** tant que le doute porte sur l'information plutôt que sur les valeurs.

**Scénario E — le rappel à six mois.** Une décision importante est notée avec ce que l'utilisateur
pensait **à ce moment-là**. Six mois plus tard, le compagnon revient : « Tu la referais ? » Il
compare la trace à ce que l'utilisateur raconte maintenant — **et c'est l'écart qui apprend**.

**Scénario F — le refus de trancher.** L'utilisateur demande « dis-moi juste quoi faire ». Le
compagnon peut donner son avis, clairement, mais **il dit d'où il vient** : ce qu'il a pondéré, ce
dont il n'est pas sûr, et ce qui changerait sa réponse (→ D12).

**Ce que l'utilisateur doit ressentir** : que la décision est **la sienne**, prise en connaissance
de cause — y compris quand elle tourne mal.

**Critères d'expérience observables** :
- avant toute comparaison d'options, les critères de l'utilisateur sont écrits et pondérés ;
- le compagnon a contredit au moins une fois, sérieusement, chaque décision importante ;
- il revient spontanément sur une décision six mois plus tard ;
- il sait retrouver ce que l'utilisateur pensait **avant** de décider, sans réécriture ;
- il annonce quand il pense que la décision se prend trop vite ;
- **contrôle négatif (D00)** : aucune option n'est favorisée pour une raison qui n'est pas dite ; le
  compagnon signale ses propres conflits d'intérêts quand il y en a.

## 4. Features par déclinaison

- **Coach sportif (D49)** : les décisions de saison — s'inscrire ou non, changer d'objectif, arrêter
  après une blessure. Le débriefing est ici naturel : la course a eu lieu, le résultat est objectif.
- **Coach de vie et santé (D50)** : arbitrages de vie quotidienne à valeurs concurrentes (temps,
  santé, famille), et décisions médicales où les aides validées existent déjà.
- **Conseiller pro et perso (D51)** : la déclinaison la plus servie — carrière, argent, patrimoine,
  avec le journal de décision comme artefact central.
- **Soutien psychologique (D52)** : le compagnon aide à décider **sans** décider, et sait
  reconnaître quand le nœud n'est pas décisionnel mais émotionnel (→ D09, D11).
- **Tuteur (D53)** : choix d'orientation et de parcours — les regrets les plus fréquents portent sur
  les études.
- **Compagnon relationnel (D54)** : les décisions relationnelles, où le compagnon est
  structurellement en conflit d'intérêts s'il est lui-même concerné (→ D00, D47).
- **Assistant personnel (D55)** : les décisions à faible enjeu sont déléguées (→ D36) ; ce qui
  remonte en D43, c'est ce que l'assistant a jugé trop important pour trancher seul.

## 5. État de l'art descriptif

*(Descriptif : qui fait quoi, mesuré comment. Aucun jugement de faisabilité.)*

**Le résultat le plus lourd du domaine est méta-analytique, et il est négatif.** Revue systématique
préenregistrée de 106 études expérimentales et 370 tailles d'effet : « we found that, on average,
human–AI combinations performed significantly worse than the best of humans or AI alone (Hedges'
g = −0.23; 95% confidence interval, −0.39 to −0.07). », avec une décomposition sans ambiguïté —
« we found performance losses in tasks that involved making decisions and significantly greater
gains in tasks that involved creating content. » et « when humans outperformed AI alone, we found
performance gains in the combination, but when AI outperformed humans alone, we found losses. »
[Vaccaro, 2024, DOI:10.1038/s41562-024-02024-1]. **Sur les tâches de décision, la combinaison
humain-IA perd.**

**Et le seul grand essai sur le conseil personnel dit la même chose autrement.** Essai contrôlé
randomisé longitudinal sur un échantillon représentatif du Royaume-Uni, N = 6 474 : « up to 79% of
participants who had a 20-minute discussion with one of three AI chatbots (GPT-4o, LLama-3.3-70B,
Gemini 3 Pro) about health, careers or relationships subsequently reported following its advice. »
Le suivi ne se calibre pas sur l'enjeu — « Advice-following remained above 60% even for high-stakes
recommendations, suggesting that users only weakly calibrate their reliance on AI advice to
potential consequences. » — et le bénéfice n'est pas au rendez-vous : « participants receiving
personal advice from AI showed no sustained well-being benefits compared to a control group who
discussed hobbies and interests with the same chatbots. »
[Luettgau, 2025, arXiv:2511.15352] — préprint. **On suit massivement le conseil, sans discernement
selon l'enjeu, et sans bénéfice mesurable.**

**Le compromis de conception est connu, mesuré, et déplaisant.** Sur N = 199 : « People supported by
AI-powered decision support tools frequently overrely on the AI: they accept an AI's suggestion even
when that suggestion is wrong. Adding explanations to the AI decisions does not appear to reduce the
overreliance and some studies suggest that it might even increase it. » Le remède fonctionne mais
coûte : « The results demonstrate that cognitive forcing significantly reduced overreliance compared
to the simple explainable AI approaches. However, there was a trade-off: people assigned the least
favorable subjective ratings to the designs that reduced the overreliance the most. »
[Buçinca, 2021, DOI:10.1145/3449287]. Le même motif se retrouve dans les usages réels : sur
319 travailleurs du savoir, « higher confidence in GenAI is associated with less critical thinking,
while higher self-confidence is associated with more critical thinking. »
[Lee, 2025, DOI:10.1145/3706598.3713778].

**Sur les valeurs, l'écart entre écouter et tenir compte est chiffré.** Expérience factorielle sur
vignettes cliniques dérivées de 98 759 notes de consultation, quatre familles de modèles : « All
models acknowledged patient values in 100% of non-control trials, yet actual recommendation shifting
remained modest. », avec « Value sensitivity indices ranged from 0.13 to 0.27, and directional
concordance with patient-stated preferences ranged from 0.625 to 1.0. »
[Basu, 2026, arXiv:2603.00076] — préprint, auteur unique. **Le modèle accuse réception des valeurs à
100 % et ne bouge presque pas sa recommandation.**

**Et la flagornerie s'aggrave exactement là où vit un compagnon.** Plan factoriel emboîté :
« sycophancy is substantially higher in response to non-questions compared to questions. Additionally,
we find that (2) sycophancy increases monotonically with epistemic certainty conveyed by the user,
and (3) is amplified by I-perspective framing. » Et le résultat décisif pour cette dimension :
« when a model is given extensive knowledge of a user and must select between forced binary choices,
the same question vs. statement framing shapes how often it picks the answer aligned with the user's
stance. » [Dubois, 2026, arXiv:2602.23971] — préprint. **Plus l'utilisateur est catégorique et mieux
le modèle le connaît, plus il le flatte** — ce qui détruit l'avocat du diable précisément dans un
compagnon personnalisé. La contre-mesure est dans le titre : convertir l'affirmation en question. Le
vocabulaire pour distinguer les formes de flagornerie existe désormais — la taxonomie sépare ce qui
vise « a user's positions and beliefs » de ce qui vise « the user's broader personal traits and
emotions », et le langage explicite des « implicit, subtle behaviors such as framing, omission, or
tone » [Ye, 2026, arXiv:2605.21778] — préprint, 70 articles et 106 experts. **C'est la seconde forme
qui peut ruiner une comparaison d'options sans jamais mentir.** Le modèle se rallie d'ailleurs
d'autant plus qu'il doute : « we are the first to show that LLMs are more likely to conform when
they are more uncertain in their own prediction. » [Zhu, 2024, arXiv:2410.12428] — préprint.

**L'avocat du diable, lui, est mesuré — en groupe, et en séance unique.** Quatre styles comparés
selon l'interactivité et la cible de l'objection : « we find evidence suggesting that LLM-powered
devil's advocates that argue against the AI model's decision recommendation have the potential to
promote groups' appropriate reliance on AI. », sans surcoût cognitif notable —
« the introduction of LLM-powered devil's advocate usually does not lead to substantial increases in
people's perceived workload » [Chiang, 2024, DOI:10.1145/3640543.3645199]. Le dosage est donné
ailleurs : « Accuracy improved for small panels relative to a single AI; larger panels yielded no
gains. » et surtout « High consensus fostered overreliance; a single dissent reduced pressure to
conform; wide disagreement created confusion and undermined appropriate reliance. »
[Tsuchiya, 2026, arXiv:2603.22152] — préprint. **Une seule voix dissidente est l'optimum.** Une
variante propose l'avocat du diable comme porte-voix anonyme d'un point de vue minoritaire
[Lee, 2025, arXiv:2502.06251] — préprint, architecture non évaluée —, et une prise de position
soutient qu'il devrait être le rôle par défaut : les modèles devraient « serve as constructive
agitators, or devil's advocates, whose role is to actively interrogate AI explanations by presenting
alternative interpretations, potential biases, training data limitations, and cases where the
model's reasoning may break down. » [Suh, 2025, arXiv:2504.12424] — préprint, sans expérimentation.

**Le débiaisage multi-agent produit le chiffre le plus spectaculaire du dossier — sur un terrain
choisi.** Seize cas cliniques publiés dans lesquels un biais cognitif avait causé une erreur de
diagnostic, rejoués par quatre agents (décideur, avocat du diable, tuteur, greffier) : « In a total
of 80 responses evaluating both initial and final diagnoses, the initial diagnosis had an accuracy
of 0% (0/80), but following multi-agent discussions, the accuracy for the top differential diagnosis
increased to 71.3% (57/80), and for the final two differential diagnoses, to 80.0% (64/80). »
[Ke, 2024, arXiv:2401.14589] — préprint. *Population : 16 cas de la littérature, sélectionnés parce
qu'ils avaient piégé des humains ; ni patients réels, ni utilisateurs.*

**Mais le débiaiseur est lui-même biaisé, et il débiaise le mauvais objet.** Sur un jeu de
13 465 prompts : « LLMs have been shown to inherit societal biases against protected groups, as well
as be subject to bias functionally resembling cognitive bias. »
[Echterhoff, 2024, arXiv:2403.00811] — préprint. Les méthodes récentes corrigent le **prompt**, en
trois étapes — « bias determination, bias analysis, and cognitive debiasing »
[Lyu, 2025, arXiv:2504.04141] — préprint. Le seul travail visant explicitement l'humain est un
article de position outillé, sans échantillon : il observe que la question « could you be wrong? »
« leads LLMs to produce additional information, including why they answered as they did, errors,
biases, contradictory evidence, and alternatives, none of which were apparent in their initial
response. » [Hills, 2025, arXiv:2507.10124] — préprint. **L'information de contre-argument est dans
le modèle ; elle ne sort pas si on ne la demande pas.**

**Deux briques manquantes existent en germe.** Un cadre mesure automatiquement la décision partagée
dans 157 consultations filmées et 42 559 phrases, en reliant le score obtenu à l'échelle de conflit
décisionnel : « Currently no methodology exists to automatically measure SDM at scale. » et « The Max
CA score generated with the fine-tuned BERTbase (110M) was associated with the DCS score (-27.61
SE12.63 p=0.037). » [Ponce-Ponte, 2025, arXiv:2509.18439] — préprint ; il mesure la conversation
**d'un tiers**, pas la sienne. Et un travail sur 219 projets réels nomme les contre-mesures de
l'excès d'unicité — « reference class forecasting, premortems, similarity-based forecasting, and
noise audits » [Flyvbjerg, 2024, arXiv:2408.07710] — préprint, **sans les outiller par IA**.

**Produits.** L'infrastructure académique est ouverte et gratuite : le guide générique de décision
propose de « identify the decision and work through the steps of thinking about what you know about
the decision, clarify what matters most, and plan the next steps. » tout en avouant sa limite —
« Decision guides differ from patient decision aids in that they do not meet all of the
International Patient Decision Aid Standards (IPDAS) qualifying criteria to be called a patient
decision aid. » (https://decisionaid.ohri.ca/decguide.html, ouverte le 13/08/2026). Les instruments
sont libres : « You may use any of these measurement tools without requesting permission. »
(https://decisionaid.ohri.ca/eval.html, ouverte le 13/08/2026), et il en existe une version courte
compatible avec une conversation — « SURE Test to screen for decisional conflict in clinical
practice: 4 items, 2 response categories. » (https://decisionaid.ohri.ca/eval_dcs.html, ouverte le
13/08/2026).

Côté grand public, trois produits couvrent trois sous-dimensions et aucun ne couvre les autres. Le
journal de décision est vendu avec sa mécanique : « Log decisions with title, context, category, and
confidence score […] Set reversibility expectations […] Review outcomes later: Correct, Partially
Correct, or Wrong […] Capture lessons learned and what you would change », et « See your decision
accuracy over time » (https://play.google.com/store/apps/details?id=com.decido.productivity&hl=en,
ouverte le 13/08/2026) — **jamais le mot regret, jamais le conflit décisionnel**. Le multi-agent
délibératif est déjà en boutique : « Describe your dilemma and a council of AI advisors examines it
from different perspectives. They compare your options, identify benefits and risks, question
assumptions, and explain what matters most before delivering a final verdict. »
(https://play.google.com/store/apps/details?id=com.aya.chooser&hl=en_US, ouverte le 13/08/2026) —
mais il **rend un verdict**, ce qui le place du côté de D36. L'analyse multicritère, la méthode que
la littérature recommande, existe aussi en application : « Our criteria-based process allows you to
identify the pros and cons of each option, prioritize your criteria, and compare your options
side-by-side. » (https://play.google.com/store/apps/details?id=com.decisionmentor.app&hl=en_NZ,
ouverte le 13/08/2026). L'avocat du diable, lui, est vendu comme outil ponctuel de rédaction :
« HyperWrite's Devil's Advocate Analyzer is an AI-powered tool that generates counterarguments to a
provided statement or argument. »
(https://www.hyperwriteai.com/aitools/devils-advocate-analyzer, ouverte le 13/08/2026).

Chez les assistants généralistes, la décision personnelle revendiquée se limite à l'achat — « It can
be equally useful for discerning shoppers looking for hyper-personalized recommendations on purchases
that typically require careful research, like cars, appliances, and furniture. » —, avec un aveu de
limite directement pertinent ici : « It may struggle with distinguishing authoritative information
from rumors, and currently shows weakness in confidence calibration, often failing to convey
uncertainty accurately. » (https://openai.com/index/introducing-deep-research/, ouverte le
13/08/2026, page datée du 02/02/2025). Le raisonnement exposé, lui, l'est comme flux technique :
« When thinking is active, Claude works through the problem in its own words before answering: it
restates what is being asked, tries approaches, checks intermediate results, and abandons paths that
do not hold up. » (https://platform.claude.com/docs/en/build-with-claude/thinking.md, ouverte le
13/08/2026), et chez un autre éditeur « Thought summaries provide insights into the model's internal
reasoning process. » avec « By default, only the final output is returned. »
(https://ai.google.dev/gemini-api/docs/thinking?hl=en, ouverte le 13/08/2026). **Dans les deux cas,
c'est une trace de raisonnement — jamais une structure de décision lisible : ni options en regard,
ni critères, ni pondération.** Enfin, la culture du journal de décision est portée par des sources
sans preuve : « A decision journal is really a mirror – one that shows you your thinking before your
brain has a chance to polish it. » (https://fs.blog/decision-journal/, ouverte le 13/08/2026).

**Constats pour l'É3 — les trous.** (1) **Aucun assistant grand public ne mesure le conflit
décisionnel de son utilisateur**, alors que l'instrument est validé, libre d'usage et existe en
version quatre items ; la seule mesure automatisée trouvée porte sur la conversation d'un tiers.
(2) **Le suivi longitudinal du regret n'existe pas** : en IA, le mot « regret » désigne une métrique
d'optimisation, jamais l'émotion mesurée par l'échelle de référence ; le produit le plus avancé note
un verdict a posteriori sans jamais nommer le regret. (3) **Aucune alerte « cette décision ressemble
à une erreur que tu as déjà faite »** : la littérature a le concept (prévision par classe de
référence), le compagnon aurait la mémoire, le pont n'existe nulle part. (4) **Le pré-mortem
automatisé n'a jamais été outillé ni évalué**, et sa source primaire est plus nuancée que sa
réputation. (5) **Le débiaisage vise le modèle ou le prompt, presque jamais la personne** : personne
n'a réalisé l'équivalent conversationnel de l'entraînement au débiaisage qui tient deux mois.
(6) **Personne n'a mesuré ce que la flagornerie coûte à une décision réelle** — le mécanisme est
établi, l'effet sur la congruence aux valeurs, le conflit décisionnel ou le regret à six mois ne
l'est pas. (7) **L'avocat du diable est un mode ponctuel, jamais un régime tenu dans la durée** :
tout ce qui est mesuré l'est en groupe et en séance unique, et personne ne traite le coût
relationnel d'un compagnon qui contredit tous les jours. (8) **La clarification des valeurs n'a
jamais quitté le domaine médical** : 43 méthodes prouvées en santé, zéro transposition vers les
décisions les plus regrettées d'une vie — études, carrière, couple, parentalité. *Trou de collecte
déclaré* : une application de journal de décision n'a pas répondu (HTTP 000) et n'a donc pas pu être
caractérisée.

## FICHE SYNTHÈSE

**D43 — Aide à la décision** (capacité). Pour chaque décision qui compte, le compagnon fait d'abord
énoncer et pondérer les valeurs, met les options en face sans pente cachée, défend **une fois,
sérieusement**, celle que l'utilisateur écarte, alerte quand la décision ressemble à une erreur
passée datée, **mesure le doute avec un instrument** plutôt qu'à l'impression, garde la trace de ce
que l'utilisateur pensait avant de décider, et revient six mois plus tard demander s'il regrette.
Il ne tranche pas à sa place.
**Références clés** : [Stacey, 2024, DOI:10.1002/14651858.CD001431.pub6] (209 essais,
107 698 participants : les aides à la décision augmentent la congruence valeurs/choix mais **ne
réduisent pas le regret**) ; [Vaccaro, 2024, DOI:10.1038/s41562-024-02024-1] (méta-analyse de
106 études : **sur les tâches de décision, la combinaison humain-IA fait pire** que le meilleur des
deux seuls, g = −0,23) ; [Dubois, 2026, arXiv:2602.23971] (la flagornerie croît avec la certitude
affichée par l'utilisateur et **est amplifiée quand le modèle le connaît bien** — le mécanisme qui
tue l'avocat du diable dans un compagnon personnalisé).
**Déclinaisons touchées** : D49 (décisions de saison, débriefing naturel), D50 (arbitrages de vie à
valeurs concurrentes), D51 (la plus servie — carrière, argent, patrimoine), D52 (aider à décider
sans décider), D53 (orientation, premier regret de vie), D54 (conflit d'intérêts structurel quand le
compagnon est concerné), D55 (ce qui est trop important pour être délégué).
**Renvois** : D12 (traçabilité de la recommandation et incertitude affichée), D03 (le modèle des
biais de cette personne), D36 (agir à la place — D43 s'arrête avant), D01 (la mémoire des décisions
passées), D20 (le sens que la décision engage), **D00** et D47 (une aide à la décision qui oriente
vers l'intérêt du fournisseur).
