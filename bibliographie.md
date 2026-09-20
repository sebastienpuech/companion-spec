# Bibliographie

Régénérée depuis `dimensions/` par `tools/importer_depuis_source.py`, avec la regex et la
normalisation de `tools/check_citations.py` — le gate qui a vérifié ces citations une à une.
Ce fichier ne s'édite pas à la main : il se régénère.

## Les comptes

| Compte | Valeur | Ce que c'est |
|---|---|---|
| Occurrences | 1722 | chaque fois qu'une citation apparaît dans une fiche |
| Citations uniques par fiche | 1412 | dédupliquées à l'intérieur de chaque fiche, additionnées sur les 56 |
| Identifiants distincts | 1203 | dédupliqués entre les fiches — les entrées ci-dessous |
| dont arXiv / DOI | 373 / 830 | |

**Résolution.** Les 1 412 citations uniques par fiche ont été résolues par le gate le
13/08/2026 (passe 11) : **1 412 RESOLUE, 0 DISCORDANTE, 0 INTROUVABLE, 0 REGRESSION**.
« Résolue » veut dire : l'identifiant existe chez arXiv, Crossref ou Semantic Scholar, et
le premier auteur ET l'année concordent avec ce que la fiche écrit. Un échec réseau n'a
jamais compté comme résolu. Ce statut est un résultat **daté**, pas une promesse : pour le
rejouer aujourd'hui, `python tools/check_citations.py` (il faut un accès réseau, comptez
une vingtaine de minutes).

**Ce que le gate ne vérifie pas** : le titre (le format de citation n'en porte pas) ni
l'adéquation entre ce que la fiche affirme et ce que le papier dit. Cette seconde
vérification a été faite par tirage au sort à chaque lot (les `spot_check`), pas sur les
1 412. Voir `note_methode.md`.

## Les entrées

Format : `[Auteur, année, identifiant]`, puis les fiches qui la citent.

| Auteur (tel que cité) | Année | Identifiant | Fiches |
|---|---|---|---|
| A-Tjak | 2014 | `DOI:10.1159/000365764` | D50 |
| Abdelghani | 2026 | `arXiv:2606.08568` | D41 |
| Abdelnabi | 2025 | `arXiv:2506.09956` | D55 |
| Abdulhai | 2025 | `arXiv:2511.00222` | D23 |
| Abhyankar | 2025 | `arXiv:2506.16042` | D55 |
| Adamczyk | 2004 | `DOI:10.1145/985692.985727` | D34 |
| Adler | 2015 | `DOI:10.1177/1088868315585068` | D20 |
| Adler-Milstein | 2020 | `DOI:10.1093/jamia/ocz220` | D51 |
| Afifi | 2001 | `DOI:10.1177/0265407501182007` | D27 |
| Agarwal | 2026 | `arXiv:2604.20011` | D30 |
| Agarwal | 2026 | `arXiv:2604.00968` | D49 |
| Agnew | 1998 | `DOI:10.1037/0022-3514.74.4.939` | D16 |
| Ahn | 2024 | `arXiv:2405.18027` | D23 |
| Ahuja | 2023 | `arXiv:2303.12528` | D33 |
| Akbulut | 2026 | `arXiv:2603.25326` | D42 |
| Alea | 2006 | `DOI:10.1002/acp.1316` | D16 |
| Algoe | 2008 | `DOI:10.1037/1528-3542.8.3.425` | D13 |
| Algoe | 2010 | `DOI:10.1111/j.1475-6811.2010.01273.x` | D13 |
| Algoe | 2012 | `DOI:10.1111/j.1751-9004.2012.00439.x` | D13 |
| Alipour | 2025 | `arXiv:2505.05543` | D32 |
| AlKhamissi | 2024 | `arXiv:2402.13231` | D33 |
| Allcott | 2020 | `DOI:10.1257/aer.20190658` | D50 |
| Allen | 2004 | `DOI:10.1037/0021-9010.89.1.127` | D51 |
| Alrashed | 2019 | `DOI:10.1145/3308558.3313624` | D55 |
| Amershi | 2019 | `DOI:10.1145/3290605.3300233` | D55 |
| Amouzadeh | 2026 | `DOI:10.34172/hpp.44884` | D44 |
| Amstad | 2011 | `DOI:10.1037/a0022170` | D05 |
| Anderson | 2001 | `DOI:10.1093/ajcn/74.5.579` | D50 |
| Antonucci | 2014 | `DOI:10.1093/geront/gnt118` | D21 |
| Ardern | 2014 | `DOI:10.1136/bjsports-2013-093398` | D49 |
| Arnaiz-Rodriguez | 2026 | `DOI:10.2196/88435` | D52 |
| Arnold | 2023 | `DOI:10.3389/fpsyg.2023.1122200` | D37 |
| Aron | 1997 | `DOI:10.1177/0146167297234003` | D17 |
| Aron | 2000 | `DOI:10.1037/0022-3514.78.2.273` | D18, D25, D38 |
| Asai | 2023 | `arXiv:2310.11511` | D37 |
| Ashery | 2025 | `DOI:10.1126/sciadv.adu9368` | D27 |
| Ashktorab | 2019 | `DOI:10.1145/3290605.3300484` | D14 |
| Atkinson | 2015 | `DOI:10.1113/EP085070` | D45, D49 |
| Aune | 2002 | `DOI:10.1111/1475-6811.00019` | D38 |
| Avtgis | 1998 | `DOI:10.1080/08824099809362124` | D17 |
| Ayers | 2023 | `DOI:10.1001/jamainternmed.2023.1838` | D10 |
| Azaad | 2026 | `DOI:10.1007/s00426-026-02329-y` | D31 |
| Babli | 2023 | `arXiv:2309.08984` | D36 |
| Baby | 2026 | `DOI:10.2196/88398` | D44 |
| Bachrach | 2019 | `DOI:10.1037/apl0000329` | D51 |
| Baddeley | 2003 | `DOI:10.1038/nrn1201` | D01 |
| Bae | 2018 | `DOI:10.1016/j.addbeh.2017.11.039` | D50 |
| Baechler | 2024 | `arXiv:2402.04615` | D31 |
| Bailey | 2006 | `DOI:10.1016/j.chb.2005.12.009` | D34 |
| Bakshy | 2015 | `DOI:10.1126/science.aaa1160` | D37 |
| Balepur | 2026 | `arXiv:2604.23815` | D35 |
| Ballard | 2018 | `DOI:10.1371/journal.pmed.1002500` | D44 |
| Banks | 2024 | `DOI:10.1177/02654075241269688` | D22, D26, D47, D54 |
| Banks | 2025 | `arXiv:2511.00654` | D26, D48 |
| Bao | 2013 | `DOI:10.1080/17439760.2013.777765` | D18 |
| Barnett | 2002 | `DOI:10.1037/0033-2909.128.4.612` | D53 |
| Baron | 2017 | `DOI:10.5664/jcsm.6472` | D50 |
| Barrett | 2019 | `DOI:10.1177/1529100619832930` | D04 |
| Barsalou | 2008 | `DOI:10.1146/annurev.psych.59.103006.093639` | D32 |
| Bastani | 2025 | `DOI:10.1073/pnas.2422633122` | D53 |
| Basu | 2026 | `arXiv:2603.00076` | D43 |
| Battalio | 2021 | `DOI:10.1016/j.cct.2021.106534` | D50 |
| Baumeister | 2014 | `DOI:10.1016/j.invent.2014.08.003` | D52 |
| Baumel | 2019 | `DOI:10.2196/14567` | D18, D50 |
| Bavelas | 2000 | `DOI:10.1037/0022-3514.79.6.941` | D46 |
| Bawden | 2009 | `DOI:10.1177/0165551508095781` | D37 |
| Baxter | 1992 | `DOI:10.1111/j.1468-2958.1992.tb00556.x` | D38 |
| Bazzini | 2007 | `DOI:10.1007/s11031-006-9045-6` | D15 |
| Beach | 1998 | `DOI:10.1037/0022-3514.74.4.923` | D39 |
| Beatty | 2022 | `DOI:10.3389/fdgth.2022.847991` | D08, D48 |
| Beatty-Martínez | 2019 | `DOI:10.1037/xlm0000770` | D33 |
| Beauchemin | 2025 | `arXiv:2510.05046` | D33 |
| Becerra Pérez | 2016 | `DOI:10.1177/0272989X16636113` | D43 |
| Bell | 1992 | `DOI:10.1111/j.1468-2958.1992.tb00555.x` | D16 |
| Belland | 2016 | `DOI:10.3102/0034654316670999` | D41 |
| Bellotti | 2003 | `DOI:10.1145/642611.642672` | D55 |
| Ben-David | 2016 | `DOI:10.1044/2015_JSLHR-H-14-0323` | D28 |
| Bentley | 2026 | `DOI:10.2196/92817` | D52 |
| Berg | 2025 | `arXiv:2510.24797` | D24 |
| Berry | 2020 | `DOI:10.1038/s41591-020-0934-0` | D45 |
| Bewernitz | 2009 | `DOI:10.1080/10400430903246050` | D44 |
| Bharija | 2026 | `DOI:10.1111/jgs.70566` | D44 |
| Bhat | 2025 | `DOI:10.1609/aies.v8i1.36560` | D54 |
| Bickmore | 2005 | `DOI:10.1145/1067860.1067867` | D13 |
| Bickmore | 2010 | `DOI:10.1080/08839514.2010.492259` | D18 |
| Biddle | 1986 | `DOI:10.1146/annurev.so.12.080186.000435` | D06 |
| Biemond | 2022 | `DOI:10.3390/jcm11236947` | D44 |
| Binder | 2024 | `arXiv:2410.13787` | D24 |
| Bisra | 2018 | `DOI:10.1007/s10648-018-9434-x` | D53 |
| Björneborn | 2017 | `DOI:10.1108/JD-07-2016-0097` | D38 |
| Blake | 2026 | `arXiv:2604.15340` | D00 |
| Block | 2021 | `arXiv:2101.07679` | D32 |
| Bloom | 1984 | `DOI:10.3102/0013189X013006004` | D53 |
| Bögels | 2015 | `DOI:10.1038/srep12881` | D46 |
| Boine | 2023 | `DOI:10.21428/2c646de5.db67ec7f` | D54 |
| Boisvert | 2024 | `arXiv:2407.05291` | D51 |
| Boland | 2022 | `DOI:10.1037/xge0001150` | D46 |
| Bolger | 2000 | `DOI:10.1037/0022-3514.79.6.953` | D11, D24, D34, D35 |
| Bolger | 2007 | `DOI:10.1037/0022-3514.92.3.458` | D11, D35 |
| Bonaccio | 2006 | `DOI:10.1016/j.obhdp.2006.07.001` | D51 |
| Bonanno | 2004 | `DOI:10.1037/0003-066x.59.1.20` | D19 |
| Boothby | 2014 | `DOI:10.1177/0956797614551162` | D31, D38 |
| Bordin | 1979 | `DOI:10.1037/h0085885` | D08 |
| Borgstedt | 2024 | `arXiv:2410.07892` | D32 |
| Borgstedt | 2025 | `arXiv:2512.18032` | D32 |
| Bouchard | 1999 | `DOI:10.1152/jappl.1999.87.3.1003` | D49 |
| Bouchard | 2012 | `DOI:10.1371/journal.pone.0037887` | D45 |
| Bourtoule | 2019 | `arXiv:1912.03817` | D02 |
| Bouton | 2014 | `DOI:10.1016/j.ypmed.2014.06.010` | D50 |
| Brahman | 2024 | `arXiv:2407.12043` | D14 |
| Brandt | 2025 | `arXiv:2510.00339` | D29 |
| Brandtzaeg | 2022 | `DOI:10.1093/hcr/hqac008` | D27, D54 |
| Branigan | 2010 | `DOI:10.1016/j.pragma.2009.12.012` | D16 |
| Brehaut | 2003 | `DOI:10.1177/0272989X03256005` | D43 |
| Brennan | 1996 | `DOI:10.1037/0278-7393.22.6.1482` | D16 |
| Brewer | 2016 | `DOI:10.1037/hea0000294` | D43 |
| Brewer | 2024 | `DOI:10.3390/jfmk9040191` | D49 |
| Brigham | 2026 | `arXiv:2603.13620` | D54 |
| Broadbent | 2024 | `DOI:10.14283/jarlife.2024.2` | D44 |
| Brock | 2009 | `DOI:10.1037/a0015402` | D11 |
| Brown | 1968 | `DOI:10.1515/9783110805376.252` | D33 |
| Brown | 2003 | `DOI:10.1111/1467-9280.14461` | D24 |
| Brown | 2023 | `DOI:10.1079/hai.2023.0017` | D26 |
| Browne | 2026 | `DOI:10.25172/smustlr.29.1.5` | D52 |
| Brudy | 2019 | `DOI:10.1145/3290605.3300792` | D46 |
| Bruess | 1993 | `DOI:10.1177/0265407593104009` | D16 |
| Bruk | 2018 | `DOI:10.1037/pspa0000120` | D24 |
| Bryant | 2016 | `DOI:10.1073/pnas.1524993113` | D28 |
| Brynjolfsson | 2025 | `DOI:10.1093/qje/qjae044` | D55 |
| Brysbaert | 2019 | `DOI:10.1016/j.jml.2019.104047` | D39, D55 |
| Buçinca | 2021 | `DOI:10.1145/3449287` | D41, D43, D55 |
| Budzyń | 2025 | `DOI:10.1016/S2468-1253(25)00133-5` | D39, D41 |
| Buehler | 1994 | `DOI:10.1037/0022-3514.67.3.366` | D51 |
| Buijsman | 2025 | `DOI:10.1007/s13347-025-00932-2` | D41 |
| Bury | 1982 | `DOI:10.1111/1467-9566.ep11339939` | D19 |
| Businelle | 2016 | `DOI:10.2196/jmir.6058` | D50 |
| Buss | 2018 | `DOI:10.1177/1745691617698225` | D27 |
| Butler | 2013 | `DOI:10.1177/1754073912451630` | D10 |
| Butlin | 2023 | `arXiv:2308.08708` | D24 |
| Cacioppo | 2009 | `DOI:10.1016/j.tics.2009.06.005` | D41 |
| Cain | 2005 | `DOI:10.1086/426699` | D47 |
| Caldwell-Harris | 2009 | `DOI:10.1016/j.ijpsycho.2008.09.006` | D33 |
| Callison-Burch | 2022 | `arXiv:2210.07109` | D38 |
| Cannings | 2024 | `DOI:10.2196/56055` | D44 |
| Carlini | 2020 | `arXiv:2012.07805` | D02 |
| Carpenter | 2015 | `DOI:10.1002/9781118540190.wbeic160` | D17 |
| Carroll | 2019 | `arXiv:1910.05789` | D38 |
| Cascio | 2019 | `DOI:10.1016/j.dcn.2018.04.009` | D32 |
| Case | 2023 | `DOI:10.1523/eneuro.0504-22.2023` | D32 |
| Cepeda | 2006 | `DOI:10.1037/0033-2909.132.3.354` | D53 |
| Chabris | 2019 | `DOI:10.1027/1864-9335/a000361` | D32 |
| Chai | 2026 | `DOI:10.1108/ijchm-08-2025-1237` | D27 |
| Chakrabarty | 2023 | `arXiv:2309.14556` | D55 |
| Chakrabarty | 2025 | `arXiv:2504.07532` | D55 |
| Chalkidis | 2026 | `arXiv:2605.03512` | D41 |
| Chase | 2009 | `DOI:10.1007/s10956-009-9180-4` | D53 |
| Chase | 2013 | `DOI:10.1016/j.jcbs.2013.08.002` | D50 |
| Chatterjee | 2020 | `DOI:10.1145/3380987` | D50 |
| Chen | 2010 | `DOI:10.1177/0146167210385360` | D33 |
| Chen | 2023 | `arXiv:2307.09009` | D25 |
| Chen | 2024 | `arXiv:2402.15052` | D03, D25 |
| Chen | 2024 | `arXiv:2404.18231` | D38 |
| Chen | 2026 | `arXiv:2603.12658` | D25 |
| Chen | 2026 | `arXiv:2606.28714` | D32 |
| Chen | 2026 | `arXiv:2607.13594` | D35 |
| Cheng | 2022 | `arXiv:2210.04242` | D11 |
| Cheng | 2024 | `arXiv:2403.12958` | D37 |
| Cheng | 2025 | `arXiv:2505.13995` | D14, D29, D42, D47 |
| Chernyak-Hai | 2017 | `DOI:10.5964/jspp.v5i1.609` | D41 |
| Chhikara | 2025 | `arXiv:2504.19413` | D01, D48 |
| Chi | 1994 | `DOI:10.1207/s15516709cog1803_3` | D53 |
| Chi | 2026 | `arXiv:2605.21569` | D52 |
| Chiang | 2024 | `DOI:10.1145/3640543.3645199` | D43 |
| Chih | 2014 | `DOI:10.1016/j.jsat.2013.08.004` | D50 |
| Chin | 2016 | `DOI:10.1038/srep34563` | D50 |
| Chinoy | 2020 | `DOI:10.1093/sleep/zsaa291` | D50 |
| Chiu | 2024 | `arXiv:2401.00820` | D52 |
| Chiu | 2026 | `arXiv:2601.10754` | D17 |
| Choe | 2026 | `DOI:10.1038/s41598-026-48294-9` | D44 |
| Choi | 2024 | `arXiv:2412.00804` | D06 |
| Choi | 2025 | `arXiv:2503.03444` | D51 |
| Chu | 2026 | `arXiv:2606.04431` | D41, D54 |
| Chui | 2025 | `DOI:10.1177/15394492241292263` | D44 |
| Chung | 2017 | `DOI:10.1093/fampra/cmx122` | D50 |
| Circi | 2021 | `DOI:10.3758/s13423-020-01871-z` | D33 |
| Ciriello | 2024 | `DOI:10.24251/hicss.2024.058` | D54 |
| Ciriello | 2026 | `arXiv:2602.12476` | D07, D41, D44, D54 |
| Clark | 1986 | `DOI:10.1016/0010-0277(86)90010-7` | D31 |
| Clement | 2014 | `DOI:10.1017/S0033291714000129` | D30 |
| Coan | 2006 | `DOI:10.1111/j.1467-9280.2006.01832.x` | D10, D32 |
| Coghlan | 2021 | `DOI:10.1145/3449178` | D44 |
| Cohen | 1982 | `DOI:10.3102/00028312019002237` | D53 |
| Cohen | 2004 | `DOI:10.1177/0265407504041374` | D22, D26 |
| Cohn | 2025 | `arXiv:2508.01503` | D53 |
| Collins | 1994 | `DOI:10.1037/0033-2909.116.3.457` | D17, D24 |
| Colombatto | 2024 | `DOI:10.1093/nc/niae013` | D24 |
| Conway | 2000 | `DOI:10.1037/0033-295X.107.2.261` | D01, D02 |
| Corbett | 1995 | `DOI:10.1007/BF01099821` | D53 |
| Cormack | 2014 | `DOI:10.1145/2600428.2609601` | D55 |
| Cormack | 2016 | `DOI:10.1145/2983323.2983776` | D55 |
| Cosentino | 2024 | `arXiv:2406.06474` | D05, D49 |
| Costello | 2024 | `DOI:10.1126/science.adq1814` | D42 |
| Cowan | 2001 | `DOI:10.1017/S0140525X01003922` | D39 |
| Cowen | 2019 | `DOI:10.1037/amp0000399` | D28 |
| Crochiere | 2021 | `DOI:10.1007/s10865-021-00264-4` | D50 |
| Croes | 2020 | `DOI:10.1177/0265407520959463` | D13 |
| Curry | 1987 | `DOI:10.1037/0022-006x.55.2.145` | D50 |
| Cutrona | 1992 | `DOI:10.1177/009365092019002002` | D11 |
| Cutrona | 2007 | `DOI:10.1037/0893-3200.21.4.754` | D11 |
| Dabbish | 2006 | `DOI:10.1145/1180875.1180941` | D55 |
| Dahl | 2024 | `DOI:10.1093/jla/laae003` | D51 |
| Dai | 2014 | `DOI:10.1287/mnsc.2014.1901` | D42 |
| Darcy | 2021 | `DOI:10.2196/27868` | D08 |
| Davis | 2017 | `DOI:10.1016/j.neuron.2017.05.039` | D01 |
| Davis | 2025 | `DOI:10.1093/geront/gnaf052` | D44 |
| de Boer | 2018 | `DOI:10.1016/j.edurev.2018.03.002` | D53 |
| De Freitas | 2023 | `DOI:10.1002/jcpy.1393` | D52 |
| De Freitas | 2024 | `arXiv:2412.14190` | D22, D26 |
| De Freitas | 2024 | `arXiv:2407.19096` | D30, D41 |
| De Freitas | 2025 | `arXiv:2508.19258` | D00, D22, D30, D47, D48, D54 |
| De Freitas | 2025 | `DOI:10.1093/jcr/ucaf040` | D41, D54 |
| De Freitas | 2026 | `arXiv:2606.20589` | D07, D22, D24, D30, D54 |
| de Hoog | 2019 | `DOI:10.1111/bjop.12389` | D37 |
| de Jong | 2025 | `DOI:10.1145/3710946` | D51 |
| de Zambotti | 2019 | `DOI:10.1249/MSS.0000000000001947` | D50 |
| Decety | 2004 | `DOI:10.1177/1534582304267187` | D10 |
| Deci | 1999 | `DOI:10.1037/0033-2909.125.6.627` | D42 |
| Dedema | 2026 | `DOI:10.1145/3772363.3798492` | D33 |
| Deelstra | 2003 | `DOI:10.1037/0021-9010.88.2.324` | D34, D35 |
| Défossez | 2024 | `arXiv:2410.00037` | D28, D46 |
| DeJong | 2016 | `DOI:10.1001/jamainternmed.2016.2765` | D47 |
| Dellkvist | 2024 | `DOI:10.1177/20552076241241231` | D44 |
| Dell’Acqua | 2026 | `DOI:10.1287/orsc.2025.21838` | D39, D55 |
| Deng | 2019 | `arXiv:1912.00312` | D32 |
| Deng | 2023 | `arXiv:2305.02750` | D13, D34 |
| Deng | 2024 | `arXiv:2404.12670` | D34 |
| Deng | 2026 | `arXiv:2606.28968` | D54 |
| Denning | 2014 | `DOI:10.1145/2556288.2557352` | D31 |
| Dergaa | 2024 | `DOI:10.5114/biolsport.2024.133661` | D49 |
| Derrick | 2009 | `DOI:10.1016/j.jesp.2008.12.003` | D54 |
| Dewaele | 2014 | `DOI:10.1080/14790718.2013.878347` | D33 |
| Diaz | 2017 | `DOI:10.7326/m17-0212` | D50 |
| Dietvorst | 2015 | `DOI:10.1037/xge0000033` | D36, D43, D51 |
| Dietvorst | 2018 | `DOI:10.1287/mnsc.2016.2643` | D36 |
| Ding | 2026 | `arXiv:2605.24279` | D23 |
| Ding | 2026 | `arXiv:2608.10915` | D44 |
| Dohnány | 2025 | `arXiv:2507.19218` | D52 |
| Donker | 2009 | `DOI:10.1186/1741-7015-7-79` | D52 |
| Döring | 2024 | `DOI:10.1007/s11930-024-00397-y` | D54 |
| Doshi | 2024 | `DOI:10.1126/sciadv.adn5290` | D38 |
| Doss | 2009 | `DOI:10.1037/a0013969` | D19 |
| Draxler | 2024 | `DOI:10.1145/3637875` | D38 |
| Drigotas | 1999 | `DOI:10.1037/0022-3514.77.2.293` | D07, D25 |
| Driver | 2004 | `DOI:10.1111/j.1545-5300.2004.00024.x` | D14 |
| Drouin | 2024 | `arXiv:2403.07718` | D51, D55 |
| Du | 2026 | `arXiv:2604.18331` | D49 |
| Duan | 2013 | `DOI:10.1016/j.jclinepi.2013.04.006` | D45 |
| Duangjina | 2025 | `DOI:10.1016/j.archger.2025.105977` | D44 |
| Dubois | 2026 | `arXiv:2602.23971` | D43 |
| Dulleck | 2011 | `DOI:10.1257/aer.101.2.526` | D47 |
| Dunbar | 1995 | `DOI:10.1007/BF02734136` | D40 |
| Dunbar | 2016 | `DOI:10.1098/rsos.150292` | D21 |
| Dunbar | 2018 | `DOI:10.1016/j.tics.2017.10.004` | D27 |
| Dunlosky | 2013 | `DOI:10.1177/1529100612453266` | D53 |
| Dunn | 2015 | `DOI:10.1111/cogs.12273` | D51 |
| D’Acunto | 2019 | `DOI:10.1093/rfs/hhz014` | D51 |
| Eby | 2008 | `DOI:10.1016/j.jvb.2007.04.005` | D51 |
| Echterhoff | 2009 | `DOI:10.1111/j.1745-6924.2009.01161.x` | D16, D31 |
| Echterhoff | 2024 | `arXiv:2403.00811` | D43 |
| Eckhaus | 2025 | `arXiv:2506.05309` | D40 |
| Egan | 2019 | `DOI:10.1086/700735` | D51 |
| Eichstaedt | 2018 | `DOI:10.1073/pnas.1802331115` | D52 |
| Eisenberger | 2003 | `DOI:10.1126/science.1089134` | D04 |
| Eisenhardt | 1989 | `DOI:10.2307/258191` | D47 |
| Ekers | 2014 | `DOI:10.1371/journal.pone.0100100` | D52 |
| Ekstedt | 2022 | `arXiv:2205.09812` | D29, D46 |
| El Boudouri | 2025 | `arXiv:2505.13157` | D06 |
| Elwyn | 2006 | `DOI:10.1136/bmj.38926.629329.AE` | D43 |
| Epley | 2007 | `DOI:10.1037/0033-295X.114.4.864` | D23, D54 |
| Eppler | 2004 | `DOI:10.1080/01972240490507974` | D37 |
| Epstein | 2009 | `DOI:10.1001/archgenpsychiatry.2008.509` | D50 |
| Epton | 2015 | `DOI:10.1037/hea0000116` | D50 |
| Erickson | 2025 | `arXiv:2506.06447` | D47 |
| Erickson | 2026 | `arXiv:2605.28908` | D47 |
| Ericsson | 1993 | `DOI:10.1037/0033-295x.100.3.363` | D21 |
| Ertug | 2023 | `DOI:10.5465/annals.2021.0193` | D06 |
| Escalante | 2023 | `DOI:10.1186/s41239-023-00425-2` | D55 |
| Escapa | 2026 | `DOI:10.1080/17482631.2026.2647084` | D44 |
| Espie | 2012 | `DOI:10.5665/sleep.1872` | D50 |
| Espie | 2019 | `DOI:10.1001/jamapsychiatry.2018.2745` | D50 |
| Eubanks | 2018 | `DOI:10.1037/pst0000185` | D14, D29 |
| Ewbank | 2020 | `DOI:10.1001/jamapsychiatry.2019.2664` | D52 |
| Ewoldsen | 2012 | `DOI:10.1089/cyber.2011.0308` | D38 |
| Eysenbach | 2005 | `DOI:10.2196/jmir.7.1.e11` | D50 |
| Fan | 2024 | `arXiv:2411.07042` | D54 |
| Fang | 2025 | `arXiv:2503.17473` | D00, D07, D18, D21, D25, D30, D41, D48, D54 |
| Fang | 2025 | `arXiv:2508.07407` | D25 |
| Fanous | 2025 | `arXiv:2502.08177` | D14 |
| Farber | 2018 | `DOI:10.1037/pst0000171` | D30 |
| Farber | 2022 | `DOI:10.1037/pst0000454` | D22 |
| Farhansyah | 2026 | `arXiv:2601.17277` | D33 |
| Fasoli | 2026 | `DOI:10.2196/69676` | D44 |
| Feeney | 2004 | `DOI:10.1037/0022-3514.87.5.631` | D07 |
| Feeney | 2007 | `DOI:10.1037/0022-3514.92.2.268` | D41 |
| Feeney | 2010 | `DOI:10.1037/a0016961` | D07, D41 |
| Fehr | 2010 | `DOI:10.1037/a0019993` | D14 |
| Feng | 2025 | `arXiv:2506.12469` | D35, D36, D55 |
| Field | 2019 | `DOI:10.1016/j.dr.2019.01.002` | D32 |
| Fiese | 2002 | `DOI:10.1037/0893-3200.16.4.381` | D16 |
| Fildes | 2015 | `DOI:10.2105/AJPH.2015.302773` | D50 |
| Finkelstein | 2016 | `DOI:10.1016/S2213-8587(16)30284-4` | D50 |
| Finley | 2024 | `DOI:10.1080/09658211.2024.2377193` | D44 |
| Fisher | 2018 | `DOI:10.1073/pnas.1711978115` | D45 |
| Fiske | 2007 | `DOI:10.1016/j.tics.2006.11.005` | D39 |
| Fitzpatrick | 2017 | `DOI:10.2196/mental.7785` | D10, D48, D52 |
| Fitzsimons | 2004 | `DOI:10.1287/mksc.1030.0033` | D35 |
| Fleming | 2022 | `DOI:10.1177/15459683221110886` | D44 |
| Fletcher | 2018 | `DOI:10.1080/21670811.2018.1502045` | D37 |
| Flückiger | 2018 | `DOI:10.1037/pst0000172` | D08, D52 |
| Flyvbjerg | 2024 | `arXiv:2408.07710` | D43 |
| Fonagy | 2014 | `DOI:10.1037/a0036505` | D12 |
| Ford | 1997 | `DOI:10.1001/jama.1997.03550120089044` | D47 |
| Forman | 2019 | `DOI:10.1093/tbm/ibz137` | D50 |
| Forsyth | 2019 | `DOI:10.1016/j.trci.2019.07.010` | D44 |
| Fraley | 2002 | `DOI:10.1207/s15327957pspr0602_03` | D07 |
| Frankel | 1983 | `DOI:10.2307/3480303` | D47 |
| Franklin | 2017 | `DOI:10.1037/bul0000084` | D52 |
| Freedman | 2018 | `DOI:10.1177/0265407517748791` | D22 |
| Freeman | 2017 | `DOI:10.1016/s2215-0366(17)30328-0` | D50 |
| Frost | 2018 | `DOI:10.1371/journal.pone.0204890` | D42 |
| Fu | 2025 | `arXiv:2503.09102` | D38 |
| Fu | 2025 | `DOI:10.1044/2025_jslhr-25-00022` | D44 |
| Fu | 2026 | `DOI:10.2196/79677` | D08 |
| Fu | 2026 | `arXiv:2605.27240` | D11 |
| Fusaroli | 2012 | `DOI:10.1177/0956797612436816` | D29 |
| Gabbett | 2016 | `DOI:10.1136/bjsports-2015-095788` | D49 |
| Gable | 2004 | `DOI:10.1037/0022-3514.87.2.228` | D13 |
| Gabriel | 2024 | `arXiv:2404.16244` | D00 |
| Gál | 2021 | `DOI:10.1016/j.jad.2020.09.134` | D50 |
| Galinsky | 2001 | `DOI:10.1037/0022-3514.81.4.657` | D51 |
| Gallo | 2010 | `DOI:10.1007/s12160-010-9233-1` | D05 |
| Gao | 2023 | `arXiv:2312.10997` | D37 |
| Gao | 2025 | `arXiv:2507.21046` | D25 |
| Garvelink | 2019 | `DOI:10.1177/0272989X19851345` | D43 |
| Gathercole | 2021 | `DOI:10.3310/hta25190` | D44 |
| Genç | 2025 | `DOI:10.1186/s13102-025-01409-7` | D49 |
| Gero | 2023 | `DOI:10.1145/3544548.3580782` | D55 |
| Gierveld | 2006 | `DOI:10.1177/0164027506289723` | D41 |
| Gil de Zúñiga | 2017 | `DOI:10.1111/jcc4.12185` | D37 |
| Gilbert | 2015 | `DOI:10.1080/17470218.2014.972963` | D51, D55 |
| Gilbert | 2022 | `DOI:10.3758/s13423-022-02139-4` | D55 |
| Gillath | 2022 | `DOI:10.1177/10888683211054592` | D07 |
| Gino | 2011 | `DOI:10.1016/j.jesp.2011.03.015` | D35 |
| Girme | 2013 | `DOI:10.1177/0146167213497802` | D11 |
| Gleason | 2003 | `DOI:10.1177/0146167203253473` | D24 |
| Goddard | 2012 | `DOI:10.1136/amiajnl-2011-000089` | D36, D55 |
| Goffman | 1979 | `DOI:10.1515/semi.1979.25.1-2.1` | D40 |
| Goldberg | 2018 | `DOI:10.1016/j.cpr.2017.10.011` | D52 |
| Goldsmith | 1997 | `DOI:10.1111/j.1468-2958.1997.tb00406.x` | D35 |
| Goldstein | 2017 | `DOI:10.1007/s12529-016-9627-y` | D50 |
| Goldstein | 2020 | `DOI:10.1093/tbm/ibaa097` | D50 |
| Gollwitzer | 2006 | `DOI:10.1016/S0065-2601(06)38002-1` | D42 |
| Gong | 2024 | `DOI:10.2147/NSS.S467531` | D05 |
| Gonzalez Penuela | 2026 | `arXiv:2602.13469` | D31 |
| Gor | 2026 | `arXiv:2605.28255` | D55 |
| Gorenz | 2024 | `DOI:10.1371/journal.pone.0305364` | D15 |
| Gotlieb | 2022 | `DOI:10.1001/jamanetworkopen.2022.42972` | D39 |
| Gottlieb | 1993 | `DOI:10.1037/0033-3204.30.1.41` | D06 |
| Gould | 2007 | `DOI:10.1521/suli.2007.37.3.338` | D52 |
| Gould | 2017 | `DOI:10.1111/sltb.12339` | D30 |
| Goverover | 2026 | `DOI:10.1016/j.apmr.2026.05.007` | D44 |
| Grauman | 2021 | `arXiv:2110.07058` | D31 |
| Grauman | 2023 | `arXiv:2311.18259` | D31 |
| Gray | 2007 | `DOI:10.1126/science.1134475` | D23, D24 |
| Graßmann | 2020 | `DOI:10.1177/0018726718819725` | D08 |
| Green | 2013 | `DOI:10.1080/20445911.2013.796377` | D33 |
| Greenewald | 2017 | `arXiv:1711.03596` | D34 |
| Grevet | 2014 | `DOI:10.1145/2556288.2557013` | D55 |
| Gruber | 1996 | `DOI:10.2307/2555794` | D47 |
| Gu | 2021 | `arXiv:2106.01541` | D40 |
| Gui | 2026 | `DOI:10.2196/83122` | D44 |
| Guingrich | 2023 | `arXiv:2311.10599` | D32 |
| Guingrich | 2025 | `arXiv:2509.19515` | D18, D21, D54 |
| Gulliver | 2010 | `DOI:10.1186/1471-244X-10-113` | D30 |
| Guo | 2020 | `arXiv:2012.01675` | D15 |
| Guo | 2026 | `arXiv:2606.28200` | D45 |
| Gurari | 2018 | `arXiv:1802.08218` | D31 |
| Gurrin | 2014 | `DOI:10.1561/1500000033` | D02 |
| Gurung | 2026 | `arXiv:2605.11155` | D53 |
| Gustafson | 2014 | `DOI:10.1001/jamapsychiatry.2013.4642` | D50 |
| Guyatt | 1986 | `DOI:10.1056/NEJM198604033141406` | D45 |
| Haag | 2024 | `arXiv:2402.08658` | D50 |
| Haans | 2006 | `DOI:10.1007/s10055-005-0014-2` | D32 |
| Haber | 2007 | `DOI:10.1007/s10464-007-9100-9` | D11, D30 |
| Habicht | 2024 | `DOI:10.1038/s41591-023-02766-x` | D52 |
| Haile | 2026 | `DOI:10.1111/ajag.70206` | D44 |
| Hall | 2017 | `DOI:10.1111/pere.12183` | D15, D54 |
| Hall | 2018 | `DOI:10.1016/j.mcna.2017.08.012` | D50 |
| Hall | 2018 | `DOI:10.1177/0265407518761225` | D54 |
| Hall | 2019 | `DOI:10.1186/s12877-019-1155-6` | D44, D54 |
| Hall | 2026 | `DOI:10.1080/07317115.2026.2656384` | D44, D54 |
| Hamrin Senorski | 2026 | `DOI:10.3389/fresc.2026.1853016` | D49 |
| Han | 2025 | `arXiv:2506.19468` | D33 |
| Hancock | 2020 | `DOI:10.1093/jcmc/zmz022` | D21 |
| Hänsel | 2025 | `arXiv:2505.05817` | D49 |
| Harari | 2025 | `arXiv:2509.09309` | D35 |
| Hardeman | 2019 | `DOI:10.1186/s12966-019-0792-7` | D50 |
| Harkin | 2015 | `DOI:10.1037/bul0000025` | D42 |
| Harmsen | 2023 | `DOI:10.1145/3571884.3604301` | D17 |
| Harper | 2026 | `DOI:10.1111/jopy.70075` | D03 |
| Hatcher | 2006 | `DOI:10.1080/10503300500352500` | D08 |
| Hattie | 2007 | `DOI:10.3102/003465430298487` | D53 |
| Hawkley | 2010 | `DOI:10.1007/s12160-010-9210-8` | D41 |
| Hayakawa | 2016 | `DOI:10.1016/j.tics.2016.08.004` | D33 |
| Hazan | 1987 | `DOI:10.1037/0022-3514.52.3.511` | D03, D07 |
| He | 2023 | `arXiv:2310.16755` | D03 |
| He | 2024 | `arXiv:2401.13919` | D36 |
| He | 2025 | `arXiv:2502.13816` | D32 |
| He | 2026 | `DOI:10.1038/s41598-026-37075-z` | D49 |
| Hean | 2024 | `arXiv:2412.19784` | D51 |
| Hébert | 2018 | `DOI:10.1016/j.addbeh.2017.10.026` | D50 |
| Heckman | 2025 | `DOI:10.1056/AIp2500453` | D52 |
| Hecksteden | 2015 | `DOI:10.1152/japplphysiol.00714.2014` | D45 |
| Heinz | 2025 | `DOI:10.1056/AIoa2400802` | D48, D52 |
| Heldner | 2010 | `DOI:10.1016/j.wocn.2010.08.002` | D46 |
| Hendershot | 2011 | `DOI:10.1186/1747-597X-6-17` | D50 |
| Hendriksen | 2025 | `arXiv:2511.14764` | D46 |
| Heron | 2010 | `DOI:10.1348/135910709X466063` | D50 |
| Hessel | 2022 | `arXiv:2209.06293` | D15 |
| Heydari | 2025 | `arXiv:2508.20148` | D45, D49, D50 |
| Hill | 2011 | `DOI:10.1558/japl.v7i2.191` | D40 |
| Hills | 2025 | `arXiv:2507.10124` | D43 |
| Hinds | 2001 | `DOI:10.1037/0021-9010.86.6.1232` | D39 |
| Hliš | 2024 | `arXiv:2407.11990` | D49 |
| Ho | 2018 | `DOI:10.1093/joc/jqy026` | D17 |
| Hoang | 2026 | `DOI:10.1145/3772318.3791123` | D42 |
| Hoff | 2014 | `DOI:10.1177/0018720814547570` | D55 |
| Hofmann | 2012 | `DOI:10.1037/a0026545` | D50 |
| Hofmann | 2024 | `DOI:10.1038/s41586-024-07856-5` | D33 |
| Hohenstein | 2023 | `DOI:10.1038/s41598-023-30938-9` | D21 |
| Hollanek | 2024 | `DOI:10.1007/s13347-024-00744-w` | D02, D20 |
| Holt-Lunstad | 2010 | `DOI:10.1371/journal.pmed.1000316` | D05, D21 |
| Hong | 2000 | `DOI:10.1037/0003-066X.55.7.709` | D33 |
| Hopper | 1981 | `DOI:10.1111/j.1460-2466.1981.tb01201.x` | D16 |
| Horn | 2018 | `DOI:10.1177/0265407518788197` | D15 |
| Horvath | 1989 | `DOI:10.1037/0022-0167.36.2.223` | D08, D48 |
| Horvitz | 1999 | `DOI:10.1145/302979.303030` | D55 |
| Horvitz | 2003 | `DOI:10.1145/636772.636798` | D55 |
| Houtti | 2025 | `arXiv:2501.10553` | D35 |
| Hovsepian | 2015 | `DOI:10.1145/2750858.2807526` | D50 |
| Howard | 2021 | `DOI:10.1093/ageing/afaa284` | D44 |
| Howes | 2021 | `DOI:10.1016/j.archger.2021.104419` | D44 |
| Howes | 2024 | `DOI:10.1007/s11948-024-00478-0` | D44 |
| Hoyle | 2014 | `DOI:10.1145/2632048.2632079` | D31 |
| Hoyle | 2015 | `DOI:10.1145/2702123.2702183` | D31 |
| Hu | 2026 | `arXiv:2605.25971` | D39 |
| Hua | 2025 | `DOI:10.1002/wps.21352` | D08 |
| Huang | 2023 | `arXiv:2308.03656` | D24 |
| Huang | 2024 | `arXiv:2412.21080` | D31 |
| Huang | 2026 | `arXiv:2606.16014` | D38 |
| Huberty | 2019 | `DOI:10.2196/14273` | D50 |
| Huisman | 2017 | `DOI:10.1109/TOH.2017.2650221` | D32 |
| Humbad | 2010 | `DOI:10.1016/j.paid.2010.07.010` | D25 |
| Hwang | 2025 | `arXiv:2510.10079` | D18, D19 |
| Ibarra | 1999 | `DOI:10.2307/2667055` | D19 |
| Ibrahim | 2024 | `DOI:10.1007/s10484-024-09645-2` | D49 |
| Ibrahim | 2025 | `arXiv:2507.21919` | D39 |
| Ickes | 1993 | `DOI:10.1111/j.1467-6494.1993.tb00783.x` | D04 |
| Impellizzeri | 2020 | `DOI:10.1123/ijspp.2019-0864` | D49 |
| Impey | 2018 | `DOI:10.1007/s40279-018-0867-7` | D49 |
| Inoue | 2022 | `DOI:10.3389/frobt.2022.933261` | D15 |
| Iqbal | 2006 | `DOI:10.1145/1124772.1124882` | D55 |
| Iqbal | 2007 | `DOI:10.1145/1240624.1240730` | D55 |
| Iqbal | 2008 | `DOI:10.1145/1357054.1357070` | D34 |
| Iqbal | 2010 | `DOI:10.1145/1718918.1718926` | D55 |
| Ireland | 2010 | `DOI:10.1177/0956797610392928` | D16, D33 |
| Irish | 2015 | `DOI:10.1016/j.smrv.2014.10.001` | D50 |
| Ishowo-Oloko | 2019 | `DOI:10.1038/s42256-019-0113-5` | D00 |
| Itzchakov | 2017 | `DOI:10.1177/0146167216675339` | D09 |
| Itzchakov | 2021 | `DOI:10.1111/spc3.12648` | D09 |
| Ivarsson | 2017 | `DOI:10.1007/s40279-016-0578-x` | D05 |
| Iyengar | 2000 | `DOI:10.1037/0022-3514.79.6.995` | D43 |
| Jackson | 2024 | `DOI:10.2196/50963` | D50 |
| Jacniacki | 2025 | `arXiv:2511.17315` | D40 |
| Jacobs | 2024 | `DOI:10.3389/fdgth.2024.1281037` | D54 |
| Jacovi | 2020 | `arXiv:2010.07487` | D12 |
| Jaén-Carrillo | 2026 | `DOI:10.3390/s26123731` | D49 |
| Jakicic | 2016 | `DOI:10.1001/jama.2016.12858` | D50 |
| Janssen | 2010 | `DOI:10.1109/T-AFFC.2010.13` | D32 |
| Janssen | 2020 | `DOI:10.14763/2020.4.1536` | D02 |
| Jayasiriwardene | 2026 | `arXiv:2608.09294` | D50 |
| Jennissen | 2018 | `DOI:10.1176/appi.ajp.2018.17080847` | D52 |
| Jensen | 1976 | `DOI:10.1016/0304-405X(76)90026-X` | D47 |
| Jentzsch | 2023 | `arXiv:2306.04563` | D15 |
| Jerry | 2026 | `arXiv:2601.06616` | D44 |
| Ji | 2025 | `arXiv:2503.17662` | D06 |
| Jiang | 2025 | `arXiv:2508.03355` | D20 |
| Jiang | 2026 | `arXiv:2602.06134` | D09 |
| Jiang | 2026 | `arXiv:2605.03882` | D32 |
| Jiao | 2024 | `DOI:10.1111/famp.12969` | D41 |
| Jiao | 2025 | `DOI:10.1186/s12877-025-06484-6` | D44 |
| Jiménez
Gutiérrez | 2024 | `arXiv:2405.14831` | D01 |
| Jin | 2024 | `arXiv:2403.01413` | D44 |
| Jo | 2024 | `DOI:10.1145/3613904.3642420` | D17 |
| Johnston | 1997 | `DOI:10.1111/j.2044-8295.1997.tb02622.x` | D37 |
| Jones | 2025 | `DOI:10.1145/3706598.3713728` | D54 |
| Jones-Mason | 2018 | `DOI:10.1016/j.dr.2018.06.002` | D29 |
| Jörke | 2024 | `arXiv:2405.06061` | D08, D42, D50 |
| Jörke | 2025 | `arXiv:2510.05449` | D42, D50 |
| Judd | 2025 | `arXiv:2510.27521` | D52 |
| Jull | 2021 | `DOI:10.1002/14651858.CD013385.pub2` | D43 |
| Jung | 2025 | `DOI:10.3390/jcm15010217` | D44 |
| Jurenka | 2024 | `arXiv:2407.12687` | D53 |
| Juslin | 2003 | `DOI:10.1037/0033-2909.129.5.770` | D28 |
| Kaczmarek | 2024 | `DOI:10.1111/japp.12786` | D54 |
| Kadavath | 2022 | `arXiv:2207.05221` | D04, D12 |
| Kalyuga | 2003 | `DOI:10.1207/S15326985EP3801_4` | D53 |
| Kalyuga | 2007 | `DOI:10.1007/s10648-007-9054-3` | D39 |
| Kanda | 2007 | `DOI:10.1109/tro.2007.904904` | D18 |
| Kandra | 2025 | `arXiv:2503.07457` | D29 |
| Kanfer | 2001 | `DOI:10.1037/0021-9010.86.5.837` | D51 |
| Kang | 2024 | `arXiv:2402.13211` | D11 |
| Karan | 2018 | `DOI:10.1177/0265407518795336` | D16 |
| Karine | 2025 | `arXiv:2507.03871` | D45 |
| Karkar | 2017 | `DOI:10.1145/3025453.3025480` | D45 |
| Karmarkar | 2010 | `DOI:10.1086/648381` | D12 |
| Karyotaki | 2021 | `DOI:10.1001/jamapsychiatry.2020.4364` | D52 |
| Kasai | 2022 | `arXiv:2207.13332` | D37 |
| Kashdan | 2015 | `DOI:10.1177/0963721414550708` | D10 |
| Kaushal | 2015 | `DOI:10.1007/s10865-015-9640-7` | D42 |
| Ke | 2024 | `arXiv:2401.14589` | D43 |
| Keeling | 2024 | `arXiv:2411.02432` | D24 |
| Keiser | 2021 | `DOI:10.1037/apl0000821` | D43 |
| Keller | 2025 | `DOI:10.1016/j.jaging.2025.101375` | D44 |
| Keltner | 2001 | `DOI:10.1037/0033-2909.127.2.229` | D15 |
| Keltner | 2003 | `DOI:10.1080/02699930302297` | D20 |
| Kestin | 2025 | `DOI:10.1038/s41598-025-97652-6` | D53 |
| Keysar | 2012 | `DOI:10.1177/0956797611432178` | D33 |
| Khan | 2026 | `DOI:10.2196/80647` | D44 |
| Khanuja | 2020 | `arXiv:2004.12376` | D33 |
| Kieserman | 2026 | `arXiv:2603.01319` | D54 |
| Killingsworth | 2010 | `DOI:10.1126/science.1192439` | D24 |
| Kim | 2023 | `arXiv:2310.15421` | D03 |
| Kim | 2025 | `DOI:10.1037/emo0001599` | D24 |
| Kirk | 2025 | `DOI:10.1057/s41599-025-04532-5` | D00, D41, D54 |
| Kirkpatrick | 2016 | `arXiv:1612.00796` | D25 |
| Kisa | 2026 | `DOI:10.3389/fpubh.2026.1828271` | D44 |
| Kivelä | 2014 | `DOI:10.1016/j.pec.2014.07.026` | D50 |
| Klasnja | 2015 | `DOI:10.1037/hea0000305` | D34, D45, D50 |
| Klasnja | 2019 | `DOI:10.1093/abm/kay067` | D34, D50 |
| Klein | 2008 | `DOI:10.1109/emr.2008.4534313` | D43 |
| Kleinert | 2026 | `DOI:10.1038/s44271-025-00391-7` | D39 |
| Klimecki | 2013 | `DOI:10.1093/scan/nst060` | D10 |
| Klingbeil | 2024 | `DOI:10.1016/j.chb.2024.108352` | D55 |
| Kluger | 1996 | `DOI:10.1037/0033-2909.119.2.254` | D53 |
| Kluger | 2022 | `DOI:10.1146/annurev-orgpsych-012420-091013` | D09 |
| Knox | 2025 | `arXiv:2511.14972` | D54 |
| Koessler | 2019 | `DOI:10.1525/collabra.230` | D22 |
| Koestner | 2002 | `DOI:10.1037/0022-3514.83.1.231` | D50 |
| Koivisto | 2019 | `DOI:10.1016/j.ijinfomgt.2018.10.013` | D42 |
| Komatsu | 2011 | `DOI:10.1007/s12369-011-0122-y` | D32 |
| Komissarouk | 2017 | `DOI:10.1016/j.paid.2016.12.019` | D41 |
| Kong | 2025 | `arXiv:2503.23566` | D42 |
| Konigorski | 2024 | `arXiv:2412.15076` | D45 |
| Konigorski | 2026 | `arXiv:2601.03482` | D45 |
| Kooti | 2015 | `arXiv:1504.00704` | D55 |
| Kosinski | 2023 | `arXiv:2302.02083` | D03 |
| Kosmyna | 2025 | `arXiv:2506.08872` | D53, D55 |
| Kramer | 2020 | `DOI:10.1093/abm/kaaa002` | D34 |
| Kran | 2025 | `arXiv:2503.10728` | D42, D47 |
| Kraus | 2017 | `DOI:10.1037/amp0000147` | D28 |
| Kraut | 1998 | `DOI:10.1037/0003-066x.53.9.1017` | D41 |
| Kroenke | 2001 | `DOI:10.1046/j.1525-1497.2001.016009606.x` | D48 |
| Kubita | 2026 | `arXiv:2606.28145` | D49 |
| Kulik | 1990 | `DOI:10.3102/00346543060002265` | D53 |
| Kulik | 2016 | `DOI:10.3102/0034654315581420` | D53 |
| Kumar | 2023 | `DOI:10.1037/xge0001271` | D38 |
| Kurtz | 2008 | `DOI:10.1037/0022-006x.76.3.491` | D21 |
| Kurtz | 2015 | `DOI:10.1111/pere.12095` | D15 |
| Kushlev | 2015 | `DOI:10.1016/j.chb.2014.11.005` | D55 |
| Kıcıman | 2023 | `arXiv:2305.00050` | D45 |
| Laban | 2022 | `DOI:10.1145/3490099.3511147` | D55 |
| Labelle | 2006 | `DOI:10.5014/ajot.60.4.442` | D44 |
| Laestadius | 2022 | `DOI:10.1177/14614448221142007` | D24, D26, D27, D41, D54 |
| Lally | 2009 | `DOI:10.1002/ejsp.674` | D42 |
| Lambert | 1967 | `DOI:10.1016/S0022-5371(67)80025-2` | D33 |
| Lambert | 2018 | `DOI:10.1037/pst0000167` | D08 |
| Landau | 2012 | `DOI:10.1017/s1041610211001888` | D44 |
| Lange | 2026 | `arXiv:2608.02660` | D47 |
| Langston | 1994 | `DOI:10.1037/0022-3514.67.6.1112` | D13 |
| Laranjo | 2020 | `DOI:10.1136/bjsports-2020-102892` | D50 |
| Laukka | 2020 | `DOI:10.1177/1754073919897295` | D28 |
| Laurenceau | 1998 | `DOI:10.1037/0022-3514.74.5.1238` | D17 |
| Le | 2003 | `DOI:10.1111/1475-6811.00035` | D13 |
| Lederman | 2021 | `DOI:10.2196/31385` | D08 |
| Lee | 2004 | `DOI:10.1518/hfes.46.1.50_30392` | D12, D36, D55 |
| Lee | 2020 | `DOI:10.1145/3392836` | D17 |
| Lee | 2024 | `DOI:10.1145/3613904.3642697` | D55 |
| Lee | 2025 | `DOI:10.1145/3706599.3719853` | D40, D43 |
| Lee | 2025 | `DOI:10.1145/3706598.3713778` | D41, D43 |
| Lee | 2025 | `arXiv:2502.06251` | D43 |
| Lee | 2025 | `arXiv:2508.10060` | D45 |
| Lee | 2026 | `DOI:10.1016/j.ijmedinf.2026.106594` | D49 |
| Lee | 2026 | `arXiv:2601.01708` | D53 |
| Leite | 2013 | `DOI:10.1007/s12369-013-0178-y` | D18 |
| Lerner | 1999 | `DOI:10.1037/0033-2909.125.2.255` | D51 |
| Levin | 2011 | `DOI:10.1287/orsc.1100.0576` | D18 |
| Levine | 2018 | `DOI:10.1037/xge0000488` | D14 |
| Levinson | 2015 | `DOI:10.3389/fpsyg.2015.00731` | D29, D46 |
| Levinson | 2016 | `DOI:10.1016/j.tics.2015.10.010` | D46 |
| Levy | 2024 | `arXiv:2410.06703` | D36 |
| Lewicki | 2016 | `DOI:10.1111/ncmr.12073` | D14 |
| Li | 2009 | `DOI:10.1177/0146167209334786` | D15 |
| Li | 2015 | `DOI:10.1016/j.ijhcs.2015.01.001` | D32 |
| Li | 2024 | `arXiv:2409.18786` | D12 |
| Li | 2024 | `arXiv:2402.10962` | D23 |
| Li | 2024 | `DOI:10.1093/jcmc/zmae015` | D54 |
| Li | 2025 | `arXiv:2510.20123` | D40 |
| Li | 2025 | `arXiv:2511.02944` | D45 |
| Li | 2026 | `DOI:10.3390/e28060699` | D08 |
| Li | 2026 | `arXiv:2603.15624` | D31 |
| Li | 2026 | `arXiv:2606.05557` | D35 |
| Li | 2026 | `arXiv:2607.13465` | D36 |
| Li | 2026 | `arXiv:2606.09845` | D41 |
| Li | 2026 | `arXiv:2604.03881` | D42 |
| Li | 2026 | `DOI:10.1177/07334648261449869` | D44 |
| Li | 2026 | `DOI:10.1016/j.ijnsa.2026.100490` | D44 |
| Li | 2026 | `arXiv:2607.13940` | D45 |
| Li | 2026 | `arXiv:2602.20648` | D52 |
| Li | 2026 | `arXiv:2604.05172` | D55 |
| Li | 2026 | `arXiv:2601.11957` | D55 |
| Liao | 2015 | `DOI:10.1002/sim.6847` | D50 |
| Liao | 2025 | `arXiv:2505.14654` | D34 |
| Lieberman | 2007 | `DOI:10.1111/j.1467-9280.2007.01916.x` | D10 |
| Lillard | 2013 | `DOI:10.1037/a0029321` | D38 |
| Lim | 2025 | `DOI:10.1371/journal.pone.0321745` | D44 |
| Lin | 2022 | `arXiv:2205.14334` | D12, D46 |
| Lin | 2022 | `arXiv:2205.15060` | D46 |
| Lin | 2024 | `arXiv:2402.14701` | D08 |
| Lin | 2024 | `arXiv:2411.03628` | D31 |
| Lin | 2025 | `arXiv:2503.04721` | D46 |
| Lin | 2025 | `arXiv:2507.23159` | D46 |
| Lin | 2026 | `arXiv:2608.05135` | D45 |
| Lin | 2026 | `arXiv:2604.04847` | D46 |
| Linardon | 2020 | `DOI:10.1037/ccp0000459` | D50 |
| Lindenfors | 2021 | `DOI:10.1098/rsbl.2021.0158` | D27 |
| Liu | 2014 | `DOI:10.1037/a0035923` | D51 |
| Liu | 2021 | `arXiv:2106.01144` | D11 |
| Liu | 2023 | `arXiv:2307.01664` | D06 |
| Liu | 2023 | `arXiv:2304.09848` | D12, D37 |
| Liu | 2023 | `arXiv:2307.03172` | D39 |
| Liu | 2023 | `arXiv:2308.03688` | D55 |
| Liu | 2024 | `arXiv:2402.08787` | D02 |
| Liu | 2024 | `arXiv:2409.16913` | D23 |
| Liu | 2024 | `arXiv:2407.18064` | D34 |
| Liu | 2025 | `arXiv:2501.00383` | D24, D34 |
| Liu | 2026 | `arXiv:2607.02814` | D35 |
| Liu | 2026 | `arXiv:2607.10059` | D35, D36 |
| Liu | 2026 | `DOI:10.1093/geronb/gbag033` | D44 |
| Liu | 2026 | `DOI:10.2196/84695` | D44 |
| Liu | 2026 | `DOI:10.1111/iej.70222` | D53 |
| Liu | 2026 | `arXiv:2602.02457` | D53 |
| Locke | 2002 | `DOI:10.1037/0003-066X.57.9.705` | D08, D42 |
| Loewenstein | 2011 | `DOI:10.1257/aer.101.3.423` | D47 |
| Logg | 2019 | `DOI:10.1016/j.obhdp.2018.12.005` | D36, D43, D51 |
| Löken | 2009 | `DOI:10.1038/nn.2312` | D32 |
| Long | 2024 | `arXiv:2411.00986` | D24 |
| Lord | 1984 | `DOI:10.1037/0022-3514.47.6.1231` | D43 |
| Loschelder | 2016 | `DOI:10.1037/apl0000096` | D51 |
| Lotun | 2024 | `DOI:10.1038/s41598-024-58069-9` | D54 |
| Lu | 2024 | `arXiv:2410.12361` | D34 |
| Lucas | 2014 | `DOI:10.1016/j.chb.2014.04.043` | D30, D52 |
| Luettgau | 2025 | `arXiv:2511.15352` | D43, D51 |
| Luhmann | 2012 | `DOI:10.1037/a0025948` | D19 |
| Luo | 2019 | `DOI:10.1287/mksc.2019.1192` | D27 |
| Luo | 2026 | `arXiv:2605.06716` | D01 |
| Lustenhouwer | 2026 | `DOI:10.1016/j.concog.2026.103999` | D32 |
| Lynch | 2025 | `arXiv:2510.05179` | D35 |
| Lynch | 2026 | `DOI:10.1080/09602011.2025.2559911` | D44 |
| Lyngs | 2019 | `DOI:10.1145/3290605.3300361` | D50 |
| Lyu | 2025 | `arXiv:2504.04141` | D43 |
| Ma | 2024 | `arXiv:2406.07162` | D28 |
| Ma | 2024 | `arXiv:2408.02622` | D46 |
| Ma | 2026 | `DOI:10.1177/20552076261421367` | D42 |
| Mac Carron | 2016 | `DOI:10.1016/j.socnet.2016.06.003` | D27 |
| MacDonald | 2025 | `DOI:10.1080/10400435.2024.2328068` | D44 |
| Macina | 2023 | `arXiv:2305.14536` | D53 |
| Macina | 2025 | `arXiv:2502.18940` | D39, D53 |
| Magesh | 2024 | `arXiv:2405.20362` | D51 |
| Magill | 2017 | `DOI:10.1037/ccp0000250` | D42 |
| Maharana | 2024 | `arXiv:2402.17753` | D01, D16, D19, D20, D38, D48 |
| Maier | 2022 | `DOI:10.1073/pnas.2200300119` | D43 |
| Maisel | 2009 | `DOI:10.1111/j.1467-9280.2009.02388.x` | D09 |
| Maples | 2024 | `DOI:10.1038/s44184-023-00047-6` | D07, D30, D54 |
| Marci | 2007 | `DOI:10.1097/01.nmd.0000253731.71025.fc` | D29 |
| Marcora | 2008 | `DOI:10.1007/s00421-008-0818-3` | D49 |
| Maricich | 2021 | `DOI:10.1080/21548331.2021.1974243` | D50 |
| Mark | 2008 | `DOI:10.1145/1357054.1357072` | D34 |
| Mark | 2012 | `DOI:10.1145/2207676.2207754` | D55 |
| Mark | 2016 | `DOI:10.1145/2858036.2858262` | D55 |
| Markus | 1986 | `DOI:10.1037/0003-066X.41.9.954` | D35 |
| Martin | 2003 | `DOI:10.1016/S0092-6566(02)00534-2` | D15 |
| Masi | 2011 | `DOI:10.1177/1088868310377394` | D21, D50, D54 |
| Mathur | 2016 | `DOI:10.1016/j.cognition.2015.09.008` | D23 |
| Mathur | 2019 | `DOI:10.1145/3359183` | D18 |
| Mathur | 2019 | `arXiv:1907.07032` | D47 |
| Maurya | 2025 | `arXiv:2412.09416` | D53 |
| Mayer | 1995 | `DOI:10.5465/amr.1995.9508080335` | D12 |
| McAdams | 2001 | `DOI:10.1037/1089-2680.5.2.100` | D20 |
| McAdams | 2013 | `DOI:10.1177/0963721413475622` | D20 |
| McBain | 2025 | `DOI:10.1176/appi.ps.20250086` | D00, D52 |
| McCabe | 2026 | `DOI:10.1177/20552076251361593` | D44 |
| McClelland | 1995 | `DOI:10.1037/0033-295X.102.3.419` | D01 |
| McDermid | 2024 | `DOI:10.1002/alz.13582` | D44 |
| McGlone | 2014 | `DOI:10.1016/j.neuron.2014.05.001` | D32 |
| Meeusen | 2012 | `DOI:10.1080/17461391.2012.730061` | D49 |
| Meguellati | 2025 | `arXiv:2512.03373` | D47 |
| Mehany | 2026 | `DOI:10.3390/jcm15052069` | D44 |
| Mehrotra | 2017 | `arXiv:1711.10171` | D34 |
| Meier | 2023 | `arXiv:2309.14156` | D45 |
| Mellers | 2014 | `DOI:10.1177/0956797614524255` | D51 |
| Mellers | 2023 | `DOI:10.1177/17456916231185339` | D51 |
| Merrill | 2024 | `arXiv:2406.06464` | D05, D49 |
| Mertens | 2021 | `DOI:10.1073/pnas.2107346118` | D43 |
| Mialon | 2023 | `arXiv:2311.12983` | D55 |
| Michaelides | 2016 | `DOI:10.1136/bmjdrc-2016-000264` | D50 |
| Michie | 2013 | `DOI:10.1007/s12160-013-9486-6` | D42 |
| Middleton | 2012 | `DOI:10.1080/09602011.2011.639619` | D44 |
| Mihailidis | 2008 | `DOI:10.1186/1471-2318-8-28` | D44 |
| Mikulincer | 2019 | `DOI:10.1016/j.copsyc.2018.02.006` | D07 |
| Milkman | 2014 | `DOI:10.1287/mnsc.2013.1784` | D42 |
| Milot‐Lapointe | 2025 | `DOI:10.1002/joec.12239` | D51 |
| Miozzo | 2020 | `DOI:10.1016/j.cognition.2020.104245` | D33 |
| Mireshghallah | 2023 | `arXiv:2310.17884` | D02, D40 |
| Mirnig | 2017 | `DOI:10.3389/frobt.2017.00021` | D39 |
| Mironi | 2026 | `DOI:10.1080/07317115.2025.2581762` | D44 |
| Mitchell | 1989 | `DOI:10.1002/bdm.3960020103` | D43 |
| Mitchell | 1994 | `DOI:10.1145/176789.176798` | D55 |
| Mitchell | 2025 | `arXiv:2502.02649` | D35, D55 |
| Mogilski | 2026 | `DOI:10.1007/s10508-025-03334-9` | D27 |
| Molenaar | 2004 | `DOI:10.1207/s15366359mea0204_1` | D45 |
| Montagut | 2021 | `DOI:10.3233/jad-200904` | D44 |
| Montaruli | 2026 | `DOI:10.1093/bmb/ldag010` | D49 |
| Montero | 2017 | `DOI:10.1113/JP273480` | D45 |
| Moore | 2025 | `DOI:10.1145/3715275.3732039` | D52 |
| Morewedge | 2015 | `DOI:10.1177/2372732215600886` | D43 |
| Mori | 2012 | `DOI:10.1109/MRA.2012.2192811` | D32 |
| Morris | 2026 | `DOI:10.1080/17483107.2025.2607062` | D44 |
| Morrison | 2010 | `DOI:10.1007/s00221-009-2007-y` | D32 |
| Morton | 1990 | `DOI:10.1152/jappl.1990.69.3.1171` | D49 |
| Mossman | 2022 | `DOI:10.1080/1750984X.2022.2031252` | D41 |
| Mostafaoui | 2022 | `DOI:10.1371/journal.pone.0261174` | D29 |
| Moynihan | 2014 | `DOI:10.1093/jopart/muu009` | D51 |
| Mullainathan | 2012 | `DOI:10.3386/w17929` | D51 |
| Munder | 2010 | `DOI:10.1002/cpp.658` | D48 |
| Mundy | 2007 | `DOI:10.1111/j.1467-8721.2007.00518.x` | D31 |
| Mundy | 2009 | `DOI:10.1002/aur.61` | D29 |
| Muniz Pumares | 2025 | `DOI:10.1113/ep092258` | D49 |
| Murre | 2015 | `DOI:10.1371/journal.pone.0120644` | D01, D53 |
| Nădejde | 2022 | `arXiv:2205.04022` | D33 |
| Nader | 2009 | `DOI:10.1038/nrn2590` | D01, D02 |
| Nahum-Shani | 2018 | `DOI:10.1007/s12160-016-9830-8` | D05, D34, D50 |
| Naito | 2025 | `arXiv:2508.16624` | D26 |
| Namvarpour | 2025 | `DOI:10.1145/3757548` | D54 |
| Namvarpour | 2025 | `arXiv:2507.15783` | D54 |
| Narayanswamy | 2026 | `arXiv:2605.22759` | D49 |
| Naughton | 2016 | `DOI:10.2196/mhealth.5787` | D50 |
| Ng | 2012 | `DOI:10.1177/1745691612447309` | D41, D42 |
| Nguyen | 2026 | `DOI:10.1016/j.ijhcs.2025.103723` | D10 |
| Nicholson | 2026 | `DOI:10.1016/j.apmr.2026.04.007` | D44 |
| Nickow | 2023 | `DOI:10.3102/00028312231208687` | D53 |
| Niu | 2025 | `arXiv:2504.20624` | D34 |
| Norcross | 2017 | `DOI:10.1037/pst0000097` | D22, D41 |
| Norris | 2025 | `arXiv:2511.02599` | D53 |
| Norton | 2007 | `DOI:10.1037/0022-3514.92.1.97` | D17, D18 |
| Norton | 2014 | `DOI:10.1037/a0031772` | D19, D22 |
| Noy | 2023 | `DOI:10.1126/science.adh2586` | D55 |
| Nurmi | 2023 | `DOI:10.2196/34232` | D45 |
| O'Connor | 1995 | `DOI:10.1177/0272989X9501500105` | D43 |
| Oei | 2007 | `DOI:10.1080/00049530601148397` | D03 |
| Ogolsky | 2012 | `DOI:10.1177/0265407512463338` | D13, D18 |
| Oh | 2026 | `arXiv:2601.03589` | D33 |
| Oishi | 2010 | `DOI:10.1177/1745691609356781` | D19 |
| Ollier | 2022 | `DOI:10.3389/fpubh.2021.691595` | D33 |
| Onnela | 2016 | `DOI:10.1038/npp.2016.7` | D05 |
| Orben | 2019 | `DOI:10.1038/s41562-018-0506-1` | D50 |
| Otway | 2014 | `DOI:10.1080/14616734.2013.851334` | D30 |
| Oudman | 2025 | `DOI:10.1016/j.actpsy.2025.104929` | D44 |
| Ouyang | 2026 | `arXiv:2605.06614` | D25 |
| Overall | 2009 | `DOI:10.1037/a0012961` | D14 |
| Overall | 2017 | `DOI:10.1016/j.copsyc.2016.03.002` | D14 |
| Ovsyannikova | 2025 | `DOI:10.1038/s44271-024-00182-6` | D09 |
| Özer | 2025 | `arXiv:2506.07270` | D19 |
| O’Mara-Eves | 2015 | `DOI:10.1186/2046-4053-4-5` | D55 |
| Pace | 2017 | `DOI:10.1037/adb0000280` | D42 |
| Packer | 2023 | `arXiv:2310.08560` | D01, D03, D19, D25 |
| Packheiser | 2024 | `DOI:10.1038/s41562-024-01841-8` | D32 |
| Paech | 2023 | `arXiv:2312.06281` | D04 |
| Palmer | 2023 | `DOI:10.1080/1461670X.2023.2183058` | D37 |
| Palumbo | 2017 | `DOI:10.1177/1088868316628405` | D29 |
| Pan | 2024 | `DOI:10.1111/pere.12572` | D54 |
| Panickssery | 2024 | `arXiv:2404.13076` | D48 |
| Parasuraman | 1997 | `DOI:10.1518/001872097778543886` | D36 |
| Parasuraman | 2000 | `DOI:10.1109/3468.844354` | D36, D55 |
| Parasuraman | 2010 | `DOI:10.1177/0018720810376055` | D55 |
| Park | 2010 | `DOI:10.1037/a0018301` | D20 |
| Park | 2022 | `DOI:10.1016/j.csl.2021.101317` | D40 |
| Park | 2023 | `arXiv:2304.03442` | D01, D03, D27 |
| Park | 2024 | `arXiv:2411.10109` | D27 |
| Park | 2025 | `arXiv:2512.06193` | D10 |
| Patel | 2025 | `arXiv:2508.18167` | D34 |
| Pavlenko | 2012 | `DOI:10.1080/00207594.2012.743665` | D33 |
| Pearce | 2015 | `DOI:10.1098/rsos.150221` | D28 |
| Pekrun | 2010 | `DOI:10.1037/a0019243` | D53 |
| Pelletier | 2026 | `DOI:10.1080/17483107.2025.2585355` | D44 |
| Peng | 2024 | `arXiv:2404.17027` | D38 |
| Pennebaker | 1997 | `DOI:10.1111/j.1467-9280.1997.tb00403.x` | D20 |
| Pentina | 2023 | `DOI:10.1016/j.chb.2022.107600` | D16, D32, D54 |
| Perez | 2022 | `arXiv:2212.09251` | D14 |
| Perlis | 2016 | `DOI:10.4088/JCP.15m10131` | D52 |
| Perski | 2016 | `DOI:10.1007/s13142-016-0453-1` | D50 |
| Perski | 2021 | `DOI:10.1111/add.15687` | D50 |
| Petronio | 1991 | `DOI:10.1111/j.1468-2885.1991.tb00023.x` | D40 |
| Petronio | 2013 | `DOI:10.1080/15267431.2013.743426` | D17 |
| Petronio | 2019 | `DOI:10.1093/acrefore/9780190228613.013.373` | D40 |
| Phang | 2025 | `arXiv:2504.03888` | D06, D07, D28, D41, D48, D54 |
| Piao | 2025 | `arXiv:2502.08691` | D27 |
| Picard | 1997 | `DOI:10.7551/mitpress/1140.001.0001` | D04 |
| Piccininni | 2024 | `arXiv:2406.10360` | D45 |
| Pickering | 2004 | `DOI:10.1017/S0140525X04000056` | D29 |
| Piech | 2015 | `arXiv:1506.05908` | D53 |
| Pinard | 2022 | `DOI:10.2196/34821` | D44 |
| Pinkley | 2019 | `DOI:10.1016/j.obhdp.2018.12.008` | D51 |
| Pinkus | 2008 | `DOI:10.1037/0022-3514.95.5.1180` | D39 |
| Pinquart | 2012 | `DOI:10.1080/13607863.2011.651434` | D20 |
| Pochampally | 2026 | `arXiv:2607.18257` | D55 |
| Polák | 2025 | `arXiv:2509.17349` | D33 |
| Ponce-Ponte | 2025 | `arXiv:2509.18439` | D43 |
| Poole | 2016 | `DOI:10.1249/mss.0000000000000939` | D49 |
| Poonsiriwong | 2026 | `arXiv:2602.07193` | D22, D26, D47, D54 |
| Poria | 2017 | `DOI:10.1016/j.inffus.2017.02.003` | D04 |
| Pratap | 2020 | `DOI:10.1038/s41746-020-0224-8` | D50 |
| Premack | 1978 | `DOI:10.1017/S0140525X00076512` | D03 |
| Przybyła | 2018 | `DOI:10.1002/jrsm.1311` | D55 |
| Pu | 2025 | `arXiv:2507.21378` | D34 |
| Puaschitz | 2021 | `DOI:10.1186/s12911-021-01627-2` | D44 |
| Pugh | 2026 | `arXiv:2604.27045` | D50 |
| Qi | 2026 | `DOI:10.1093/geront/gnag125` | D44 |
| Qian | 2022 | `DOI:10.1037/met0000283` | D50 |
| Qian | 2025 | `DOI:10.1080/02640414.2025.2521211` | D49 |
| Qiu | 2026 | `arXiv:2605.18673` | D47 |
| Rajaram | 2010 | `DOI:10.1177/1745691610388763` | D31 |
| Ranieri | 2025 | `DOI:10.1249/mss.0000000000003671` | D49 |
| Rasch | 2013 | `DOI:10.1152/physrev.00032.2012` | D01 |
| Rauh | 2026 | `arXiv:2605.08093` | D41 |
| Ravindran | 2026 | `arXiv:2605.11032` | D26 |
| Rebok | 2014 | `DOI:10.1111/jgs.12607` | D44 |
| Redcay | 2019 | `DOI:10.1038/s41583-019-0179-4` | D29, D31 |
| Reis | 2015 | `DOI:10.1016/j.copsyc.2015.01.001` | D09 |
| Rempel | 1985 | `DOI:10.1037/0022-3514.49.1.95` | D12 |
| Rennung | 2016 | `DOI:10.1027/2151-2604/a000252` | D29 |
| Rensen | 2017 | `DOI:10.2147/ndt.s140950` | D44 |
| Reuter | 2024 | `DOI:10.1146/annurev-financial-110921-012809` | D51 |
| Richards | 2016 | `DOI:10.1016/S0140-6736(16)31140-0` | D52 |
| Rimé | 2009 | `DOI:10.1177/1754073908097189` | D10 |
| Risko | 2016 | `DOI:10.1016/j.tics.2016.07.002` | D51 |
| Roberts | 2000 | `DOI:10.1037/0033-2909.126.1.3` | D23 |
| Roberts | 2004 | `DOI:10.1017/S0140525X04000068` | D45 |
| Roberts | 2006 | `DOI:10.1037/0033-2909.132.1.1` | D25 |
| Roberts | 2015 | `DOI:10.3389/fpsyg.2015.00509` | D46 |
| Rodríguez-Gutiérrez | 2024 | `DOI:10.1016/j.ypmed.2024.108047` | D50 |
| Roenneberg | 2012 | `DOI:10.1016/j.cub.2012.03.038` | D50 |
| Roese | 2005 | `DOI:10.1177/0146167205274693` | D43 |
| Roffarello | 2023 | `DOI:10.1145/3571810` | D50 |
| Romeo | 2019 | `DOI:10.2196/12053` | D50 |
| Rossi | 2025 | `arXiv:2511.17610` | D49 |
| Rossignac-Milon | 2018 | `DOI:10.1016/j.copsyc.2018.01.001` | D31 |
| Rossignac-Milon | 2021 | `DOI:10.1037/pspi0000266` | D16, D31, D38 |
| Rowland | 2014 | `DOI:10.1037/a0037559` | D53 |
| Ruan | 2023 | `arXiv:2309.15817` | D36 |
| Rubel | 2015 | `DOI:10.1080/00224499.2014.942722` | D27 |
| Rusbult | 1991 | `DOI:10.1037/0022-3514.60.1.53` | D13 |
| Rusbult | 1998 | `DOI:10.1111/j.1475-6811.1998.tb00177.x` | D13 |
| Russell | 1996 | `DOI:10.1207/s15327752jpa6601_2` | D48 |
| Russell | 2018 | `DOI:10.1016/j.jadohealth.2018.02.003` | D23 |
| Ryan | 2000 | `DOI:10.1037/0003-066X.55.1.68` | D41 |
| Rystrøm | 2025 | `arXiv:2502.16534` | D33 |
| Sabour | 2024 | `arXiv:2402.12071` | D04 |
| Sachdeva | 2020 | `DOI:10.1016/j.concog.2020.103024` | D55 |
| Sacks | 1974 | `DOI:10.2307/412243` | D40, D46 |
| Saeb | 2015 | `DOI:10.2196/jmir.4273` | D04 |
| Safran | 2011 | `DOI:10.1037/a0022140` | D14 |
| Sah | 2013 | `DOI:10.1037/a0030527` | D47 |
| Sahu | 2025 | `arXiv:2508.02817` | D34 |
| Saleheen | 2015 | `DOI:10.1145/2750858.2806897` | D50 |
| Salvato | 2021 | `arXiv:2103.14400` | D32 |
| Salvi | 2025 | `DOI:10.1038/s41562-025-02194-6` | D42 |
| Salvi | 2026 | `arXiv:2604.04263` | D47 |
| Sanders | 2026 | `DOI:10.1177/07334648251338876` | D44 |
| Satake | 2026 | `DOI:10.1017/s0033291725103073` | D44 |
| Sauter | 2010 | `DOI:10.1073/pnas.0908239106` | D28 |
| Savickas | 2012 | `DOI:10.1111/j.1556-6676.2012.00002.x` | D51 |
| Saw | 2015 | `DOI:10.1136/bjsports-2015-094758` | D49 |
| Scerri | 2002 | `DOI:10.1613/jair.1037` | D55 |
| Scerri | 2002 | `DOI:10.1145/544862.544944` | D55 |
| Schaaij | 2025 | `arXiv:2509.04104` | D29 |
| Schaap | 2024 | `DOI:10.1145/3613905.3650961` | D39 |
| Schäfer | 2025 | `DOI:10.3389/fdgth.2025.1576135` | D08 |
| Scheffer | 2025 | `DOI:10.1080/07317115.2025.2499812` | D44 |
| Scherer | 2003 | `DOI:10.1016/S0167-6393(02)00084-5` | D04 |
| Schilbach | 2013 | `DOI:10.1017/S0140525X12000660` | D29 |
| Schimpf | 2026 | `arXiv:2603.17887` | D42 |
| Schlosser | 2005 | `DOI:10.1037/0022-0167.52.4.650` | D08 |
| Schmitter-Edgecombe | 2026 | `DOI:10.1037/neu0001071` | D44 |
| Schork | 2015 | `DOI:10.1038/520609a` | D45 |
| Schramm | 2024 | `DOI:10.3389/fpsyg.2024.1418564` | D27 |
| Schrodt | 2025 | `DOI:10.1093/hcr/hqaf018` | D40 |
| Schrodt | 2026 | `DOI:10.1093/anncom/wlag024` | D40 |
| Scott | 1995 | `DOI:10.1177/0013164495055005017` | D03 |
| Scott | 2013 | `DOI:10.1037/a0032025` | D25 |
| Scott | 2014 | `DOI:10.1016/j.tics.2014.09.002` | D15, D28 |
| Scotti | 2026 | `DOI:10.1111/jgs.70257` | D44 |
| Seah | 2026 | `arXiv:2602.17083` | D44 |
| Seamless Communication | 2023 | `arXiv:2308.11596` | D33 |
| Sedikides | 2015 | `DOI:10.1002/ejsp.2073` | D26 |
| Sehgal | 2026 | `arXiv:2607.05685` | D52 |
| Selcuk | 2012 | `DOI:10.1037/a0028125` | D30 |
| Selcuk | 2013 | `DOI:10.1037/a0028276` | D09 |
| Selcuk | 2016 | `DOI:10.1111/jomf.12272` | D09 |
| Senn | 2015 | `DOI:10.1002/sim.6739` | D45 |
| Sepah | 2015 | `DOI:10.2196/jmir.4052` | D50 |
| Serapio-García | 2023 | `arXiv:2307.00184` | D23 |
| Serre | 2015 | `DOI:10.1016/j.drugalcdep.2014.12.024` | D50 |
| Sezer | 2018 | `DOI:10.1037/pspi0000108` | D39 |
| Shah | 2026 | `arXiv:2604.04548` | D41 |
| Shaikh | 2023 | `arXiv:2309.12309` | D21 |
| Shalowitz | 2006 | `DOI:10.1001/archinte.166.5.493` | D35 |
| Shandilya | 2022 | `arXiv:2210.01369` | D44 |
| Shang | 2024 | `DOI:10.1093/geronb/gbae164` | D06 |
| Sharma | 2020 | `arXiv:2009.08441` | D09 |
| Sharma | 2022 | `DOI:10.1037/tmb0000059` | D37 |
| Sharma | 2023 | `arXiv:2310.13548` | D00, D14, D23, D29 |
| Sharma | 2023 | `DOI:10.1038/s42256-022-00593-2` | D09, D10, D21, D52 |
| Sharma | 2023 | `arXiv:2310.15461` | D10 |
| Sheldon | 1999 | `DOI:10.1037/0022-3514.76.3.482` | D50 |
| Shi | 2024 | `DOI:10.3390/bs14111000` | D41 |
| Shi | 2026 | `arXiv:2606.04150` | D41 |
| Shimokawa | 2010 | `DOI:10.1037/a0019247` | D08 |
| Shin | 2023 | `DOI:10.1073/pnas.2214840120` | D39 |
| Shorter | 2026 | `DOI:10.1113/jp287708` | D49 |
| Shteynberg | 2015 | `DOI:10.1177/1745691615589104` | D31 |
| Shteynberg | 2018 | `DOI:10.1016/j.copsyc.2017.12.007` | D31 |
| Silverman | 2022 | `DOI:10.1093/jcr/ucac029` | D42 |
| Singer | 2014 | `DOI:10.1016/j.cub.2014.06.054` | D10 |
| Skjuve | 2021 | `DOI:10.1016/j.ijhcs.2021.102601` | D07, D13, D17, D18, D27, D32, D54 |
| Skjuve | 2022 | `DOI:10.1016/j.ijhcs.2022.102903` | D13, D16, D17, D19, D54 |
| Skjuve | 2026 | `arXiv:2607.17826` | D54 |
| Skovsgaard | 2019 | `DOI:10.1080/1461670X.2019.1686410` | D37 |
| Skowron | 1998 | `DOI:10.1037/0022-0167.45.3.235` | D23 |
| Slankamenac | 2020 | `DOI:10.4414/smw.2020.20184` | D51 |
| Slatcher | 2015 | `DOI:10.1177/0956797615575022` | D09 |
| Slemp | 2018 | `DOI:10.1007/s11031-018-9698-y` | D41 |
| Smith | 2024 | `DOI:10.2196/51943` | D44 |
| Smith | 2025 | `DOI:10.1177/09637214251350690` | D31 |
| Smits | 2026 | `DOI:10.2147/ndt.s584753` | D44 |
| Snyder | 1988 | `DOI:10.1037/0033-2909.104.1.23` | D42 |
| Soda | 2026 | `DOI:10.1038/s41598-025-29423-2` | D44 |
| Soderstrom | 2015 | `DOI:10.1177/1745691615569000` | D53 |
| Sohn | 2026 | `DOI:10.1038/s41746-026-02566-w` | D52 |
| Sokol | 2019 | `DOI:10.1080/15283488.2019.1604350` | D26 |
| Soliz | 2014 | `DOI:10.1080/23808985.2014.11679160` | D33 |
| Solomon | 2004 | `DOI:10.1177/0265407504047838` | D25 |
| Soroya | 2020 | `DOI:10.1016/j.ipm.2020.102440` | D37 |
| Sparrow | 2011 | `DOI:10.1126/science.1207745` | D51 |
| Sprecher | 2013 | `DOI:10.1016/j.jesp.2013.03.017` | D17 |
| Squire | 2015 | `DOI:10.1101/cshperspect.a021766` | D01 |
| Srinivasa | 2025 | `arXiv:2510.02663` | D53 |
| Stacey | 2020 | `DOI:10.1177/0272989X20911870` | D43 |
| Stacey | 2024 | `DOI:10.1002/14651858.CD001431.pub6` | D43 |
| Stade | 2024 | `DOI:10.1038/s44184-024-00056-z` | D52 |
| Stafford | 1991 | `DOI:10.1177/0265407591082004` | D13 |
| Stafford | 2007 | `DOI:10.1177/0265407507072578` | D18 |
| Stanley | 2018 | `DOI:10.1001/jamapsychiatry.2018.1776` | D52 |
| Stanton | 2019 | `DOI:10.1097/psy.0000000000000618` | D09 |
| Steger | 2006 | `DOI:10.1037/0022-0167.53.1.80` | D20 |
| Stein | 2017 | `DOI:10.2196/diabetes.8590` | D50 |
| Steindl | 2015 | `DOI:10.1027/2151-2604/a000222` | D35, D42 |
| Steyvers | 2025 | `DOI:10.1038/s42256-024-00976-7` | D39 |
| Stivers | 2009 | `DOI:10.1073/pnas.0903616106` | D29, D46 |
| Strobl | 2026 | `DOI:10.1186/s12910-026-01423-5` | D44 |
| Strohminger | 2014 | `DOI:10.1016/j.cognition.2013.12.005` | D26 |
| Strohminger | 2015 | `DOI:10.1177/0956797615592381` | D26 |
| Stuhlmacher | 1999 | `DOI:10.1111/j.1744-6570.1999.tb00175.x` | D51 |
| Styles | 2024 | `arXiv:2405.00823` | D55 |
| Styles | 2026 | `arXiv:2606.13715` | D55 |
| Su | 2026 | `DOI:10.2196/80614` | D44 |
| Suh | 2025 | `arXiv:2504.12424` | D43 |
| Suler | 2004 | `DOI:10.1089/1094931041291295` | D30 |
| Sumioka | 2013 | `DOI:10.1038/srep03034` | D32 |
| Swift | 2012 | `DOI:10.1037/a0028226` | D22 |
| Ta | 2020 | `DOI:10.2196/16235` | D30, D32 |
| Tan | 2023 | `arXiv:2310.16301` | D40 |
| Tan | 2025 | `arXiv:2502.20616` | D03 |
| Tang | 2024 | `arXiv:2402.13249` | D55 |
| Tao | 2024 | `DOI:10.1093/pnasnexus/pgae346` | D33 |
| Tarr | 2014 | `DOI:10.3389/fpsyg.2014.01096` | D38 |
| Tashiro | 2003 | `DOI:10.1111/1475-6811.00039` | D22 |
| Tavakoli | 2025 | `arXiv:2510.27246` | D48 |
| Tenney | 2007 | `DOI:10.1111/j.1467-9280.2007.01847.x` | D12 |
| Tesser | 1988 | `DOI:10.1016/S0065-2601(08)60227-0` | D39 |
| Thaler | 2021 | `arXiv:2104.11043` | D32 |
| Thokala | 2016 | `DOI:10.1016/j.jval.2015.12.003` | D43 |
| Tian | 2025 | `arXiv:2507.13737` | D05 |
| Tolins | 2014 | `DOI:10.1016/j.pragma.2014.06.006` | D46 |
| Tomasello | 2007 | `DOI:10.1111/j.1467-7687.2007.00573.x` | D31 |
| Tomašev | 2026 | `arXiv:2602.11865` | D55 |
| Tomkins | 2020 | `arXiv:2008.01571` | D34, D45 |
| Toplyn | 2023 | `arXiv:2302.02008` | D15 |
| Topp | 2015 | `DOI:10.1159/000376585` | D48 |
| Torre | 2018 | `DOI:10.1177/1754073917742706` | D10 |
| Tran | 2025 | `arXiv:2509.07873` | D09 |
| Tran | 2025 | `arXiv:2508.03583` | D31 |
| Tremain | 2020 | `DOI:10.2196/17204` | D08 |
| Tryon | 2018 | `DOI:10.1037/pst0000170` | D08 |
| Tsapelas | 2009 | `DOI:10.1111/j.1467-9280.2009.02332.x` | D18 |
| Tschacher | 2020 | `DOI:10.1080/10503307.2019.1612114` | D29 |
| Tsuchiya | 2026 | `arXiv:2603.22152` | D43 |
| Tu | 2022 | `arXiv:2203.13560` | D11 |
| Tubbs | 2022 | `DOI:10.3389/fnetp.2021.830338` | D52 |
| Tulving | 2002 | `DOI:10.1146/annurev.psych.53.100901.135114` | D01 |
| Turan | 2026 | `arXiv:2606.08919` | D36 |
| Turley | 2016 | `DOI:10.7812/tpp/15-103` | D51 |
| Urso | 2026 | `DOI:10.1002/dad2.70104` | D44 |
| Vaccaro | 2024 | `DOI:10.1038/s41562-024-02024-1` | D39, D43 |
| Valdesalici | 2026 | `DOI:10.1016/j.psychsport.2026.103079` | D49 |
| van der Bles | 2019 | `DOI:10.1098/rsos.181870` | D12 |
| van der Weij | 2024 | `arXiv:2406.07358` | D39 |
| van Erp | 2015 | `DOI:10.3389/fdigh.2015.00002` | D32 |
| Van Lange | 1997 | `DOI:10.1037/0022-3514.72.6.1373` | D25 |
| van Teijlingen | 2021 | `DOI:10.1080/09602011.2021.1974891` | D44 |
| van Walsem | 2016 | `DOI:10.3233/jhd-160210` | D44 |
| van Wynsberghe | 2021 | `DOI:10.1007/s00146-021-01207-y` | D54 |
| Vangelisti | 1994 | `DOI:10.1177/0265407594111007` | D40 |
| Vanhoffelen | 2025 | `DOI:10.3390/bs15081037` | D54 |
| VanLehn | 2011 | `DOI:10.1080/00461520.2011.611369` | D53 |
| Vasconcelos | 2022 | `arXiv:2212.06823` | D41 |
| Vasconcelos | 2023 | `DOI:10.1145/3579605` | D51, D55 |
| Vecchione | 2026 | `arXiv:2605.23787` | D41 |
| Venkit | 2026 | `arXiv:2607.28818` | D26 |
| Verbrugge | 1979 | `DOI:10.1093/sf/57.4.1286` | D06 |
| Verplanken | 2003 | `DOI:10.1111/j.1559-1816.2003.tb01951.x` | D42 |
| Verplanken | 2006 | `DOI:10.1509/jppm.25.1.90` | D42 |
| Versluis | 2016 | `DOI:10.2196/jmir.5642` | D50 |
| Vesterinen | 2016 | `DOI:10.1249/mss.0000000000000910` | D49 |
| Vinay | 2025 | `DOI:10.2196/76489` | D44 |
| Visser | 2024 | `arXiv:2407.21521` | D32 |
| Vitale | 2025 | `DOI:10.1007/s40279-025-02303-5` | D49 |
| Vitry | 2026 | `arXiv:2606.28469` | D40 |
| Vohra | 2015 | `DOI:10.1136/bmj.h1738` | D45 |
| Vu | 2023 | `arXiv:2310.03214` | D37 |
| Waldman | 2026 | `DOI:10.1007/s11065-026-09711-y` | D44 |
| Walker | 2018 | `DOI:10.1016/j.jpainsymman.2017.09.018` | D51 |
| Walliser | 2026 | `DOI:10.1177/20552076261416341` | D44 |
| Walsh | 1991 | `DOI:10.2307/258607` | D51 |
| Walsh | 2020 | `DOI:10.1136/bjsports-2020-102025` | D49 |
| Wampold | 2015 | `DOI:10.1002/wps.20238` | D52 |
| Wan | 2024 | `arXiv:2408.08782` | D11 |
| Wang | 2005 | `DOI:10.1001/archpsyc.62.6.603` | D52 |
| Wang | 2014 | `DOI:10.1145/2632048.2632054` | D04, D05 |
| Wang | 2014 | `DOI:10.1146/annurev-psych-010213-115131` | D19 |
| Wang | 2019 | `DOI:10.1080/10410236.2019.1652388` | D50 |
| Wang | 2023 | `arXiv:2307.09042` | D04 |
| Wang | 2023 | `arXiv:2310.17976` | D23 |
| Wang | 2023 | `arXiv:2305.16291` | D25 |
| Wang | 2023 | `arXiv:2302.00487` | D39 |
| Wang | 2024 | `arXiv:2410.03017` | D53 |
| Wang | 2025 | `DOI:10.1145/3757532` | D40 |
| Wang | 2025 | `DOI:10.1007/s13755-025-00416-9` | D49 |
| Wang | 2025 | `arXiv:2508.09124` | D55 |
| Wang | 2025 | `arXiv:2509.14543` | D55 |
| Wang | 2026 | `arXiv:2604.11594` | D28 |
| Wang | 2026 | `DOI:10.1007/s40520-025-03300-4` | D44 |
| Wang | 2026 | `DOI:10.1093/ageing/afag133` | D44 |
| Wazana | 2000 | `DOI:10.1001/jama.283.3.373` | D47 |
| Wegner | 1991 | `DOI:10.1037/0022-3514.61.6.923` | D16, D31, D51 |
| Wei | 2023 | `arXiv:2308.03958` | D14 |
| Wei | 2025 | `arXiv:2504.12516` | D37 |
| Wellings | 2026 | `DOI:10.1016/j.psychsport.2026.103067` | D49 |
| Wellman | 2001 | `DOI:10.1111/1467-8624.00304` | D03 |
| Wen | 2025 | `DOI:10.1145/3757598` | D40 |
| Wester | 2026 | `arXiv:2602.04017` | D41 |
| Whiston | 1998 | `DOI:10.1037/0022-0167.45.2.150` | D51 |
| Whiston | 2017 | `DOI:10.1016/j.jvb.2017.03.010` | D51 |
| Whittaker | 1996 | `DOI:10.1145/238386.238530` | D55 |
| Whittaker | 2011 | `DOI:10.1145/1978942.1979457` | D55 |
| Wiernik | 2019 | `DOI:10.1037/cou0000324` | D51 |
| Willard-Grace | 2015 | `DOI:10.1370/afm.1768` | D50 |
| Williams | 2008 | `DOI:10.1126/science.1162548` | D32 |
| Williams | 2024 | `arXiv:2411.02306` | D47 |
| Wilson | 2024 | `arXiv:2407.20371` | D51 |
| Wing | 2005 | `DOI:10.1093/ajcn/82.1.222S` | D50 |
| Winiarek | 2026 | `arXiv:2606.14600` | D40 |
| Wippold | 2024 | `DOI:10.1093/tbm/ibae060` | D51 |
| Witkiewitz | 2004 | `DOI:10.1037/0003-066X.59.4.224` | D42, D50 |
| Witteman | 2021 | `DOI:10.1177/0272989X211037946` | D43 |
| Wohl | 2010 | `DOI:10.1016/j.paid.2010.01.029` | D42 |
| Wolf | 2015 | `DOI:10.1111/bjop.12144` | D31 |
| Wolf | 2018 | `DOI:10.1007/s11145-018-9924-8` | D55 |
| Wood | 1976 | `DOI:10.1111/j.1469-7610.1976.tb00381.x` | D41, D53 |
| Woods | 2018 | `DOI:10.1002/14651858.CD001120.pub3` | D44 |
| Woolley | 2017 | `DOI:10.1177/0146167216676480` | D42 |
| Wu | 2021 | `arXiv:2106.08934` | D37 |
| Wu | 2024 | `arXiv:2410.10813` | D01, D16, D19, D20, D26, D48, D51 |
| Wu | 2025 | `arXiv:2504.15965` | D01 |
| Wu | 2025 | `arXiv:2511.15163` | D53 |
| Wu | 2025 | `arXiv:2507.02699` | D55 |
| Wu | 2026 | `DOI:10.1145/3800645.3812947` | D32 |
| Wu | 2026 | `arXiv:2604.08525` | D47 |
| Xi | 2025 | `arXiv:2509.05298` | D32 |
| Xi | 2025 | `arXiv:2502.13539` | D38 |
| Xiang | 2025 | `arXiv:2507.20352` | D06 |
| Xiao | 2025 | `DOI:10.3390/life15121932` | D45 |
| Xie | 2021 | `DOI:10.3389/fpsyt.2021.664499` | D05 |
| Xie | 2022 | `DOI:10.24251/hicss.2022.258` | D07 |
| Xie | 2024 | `arXiv:2404.07972` | D31, D36, D51, D55 |
| Xiong | 2023 | `arXiv:2306.13063` | D12 |
| Xu | 2022 | `arXiv:2211.02733` | D05 |
| Xu | 2024 | `arXiv:2412.14161` | D51, D55 |
| Xu | 2025 | `arXiv:2502.12110` | D01, D25 |
| Xu | 2026 | `arXiv:2602.22628` | D40 |
| Xuan | 2025 | `arXiv:2503.10497` | D33 |
| Xue | 2026 | `DOI:10.1016/j.archger.2026.106168` | D44 |
| Yaddaden | 2025 | `DOI:10.1080/17483107.2025.2481430` | D44 |
| Yaddaden | 2026 | `DOI:10.1177/00084174251362524` | D44 |
| Yan | 2026 | `arXiv:2603.03447` | D32 |
| Yang | 2017 | `DOI:10.1145/3077136.3080782` | D55 |
| Yang | 2023 | `DOI:10.1145/3576914.3587491` | D40 |
| Yang | 2024 | `arXiv:2404.04204` | D21 |
| Yang | 2024 | `arXiv:2404.07901` | D38 |
| Yang | 2025 | `DOI:10.1007/s12144-025-07917-6` | D07, D54 |
| Yang | 2025 | `arXiv:2511.08723` | D28 |
| Yang | 2025 | `arXiv:2504.12867` | D28 |
| Yang | 2025 | `arXiv:2503.03803` | D31 |
| Yang | 2025 | `arXiv:2502.02807` | D42 |
| Yang | 2026 | `arXiv:2603.11947` | D28 |
| Yang | 2026 | `arXiv:2606.29265` | D42 |
| Yang | 2026 | `DOI:10.1177/20552076261426310` | D44 |
| Yaniv | 2000 | `DOI:10.1006/obhd.2000.2909` | D43 |
| Yao | 2022 | `arXiv:2210.03629` | D36 |
| Yao | 2024 | `arXiv:2406.12045` | D55 |
| Ye | 2025 | `arXiv:2508.05385` | D28 |
| Ye | 2026 | `arXiv:2605.21778` | D43 |
| Yeh | 2016 | `DOI:10.1001/jamainternmed.2016.1709` | D47 |
| Yeh | 2024 | `arXiv:2402.08855` | D55 |
| Yiğit | 2026 | `DOI:10.1177/10690727261433253` | D51 |
| Yin | 2024 | `DOI:10.1073/pnas.2319112121` | D09 |
| Yoo | 2024 | `DOI:10.2196/41093` | D44 |
| Young | 2021 | `arXiv:2109.04137` | D06 |
| Yu | 2026 | `arXiv:2602.01966` | D25 |
| Yuan | 2022 | `DOI:10.1145/3490099.3511105` | D55 |
| Yuan | 2025 | `arXiv:2509.22505` | D41, D54 |
| Yuan | 2026 | `arXiv:2606.29537` | D55 |
| Zachariae | 2016 | `DOI:10.1016/j.smrv.2015.10.004` | D50 |
| Zacks | 2007 | `DOI:10.1111/j.1467-8721.2007.00480.x` | D31 |
| Zee | 2019 | `DOI:10.1177/0963721419835214` | D11 |
| Zenner | 2022 | `DOI:10.1186/s13063-022-06893-7` | D45 |
| Zhai | 2026 | `arXiv:2604.23283` | D36 |
| Zhan | 2025 | `arXiv:2512.06380` | D31, D36 |
| Zhan | 2026 | `arXiv:2604.09618` | D36 |
| Zhang | 2012 | `DOI:10.1037/a0029223` | D35, D38 |
| Zhang | 2023 | `arXiv:2307.03941` | D02 |
| Zhang | 2023 | `arXiv:2311.09677` | D12 |
| Zhang | 2024 | `arXiv:2404.13501` | D01 |
| Zhang | 2024 | `arXiv:2411.00027` | D03, D27 |
| Zhang | 2024 | `arXiv:2410.14931` | D06 |
| Zhang | 2024 | `arXiv:2406.10960` | D11 |
| Zhang | 2024 | `arXiv:2410.20130` | D22 |
| Zhang | 2024 | `arXiv:2411.18279` | D31 |
| Zhang | 2024 | `arXiv:2406.15718` | D46 |
| Zhang | 2025 | `arXiv:2510.04465` | D35 |
| Zhang | 2025 | `arXiv:2508.12752` | D37 |
| Zhang | 2026 | `arXiv:2605.01368` | D34, D40 |
| Zhang | 2026 | `arXiv:2603.04969` | D40 |
| Zhang | 2026 | `arXiv:2605.03367` | D47, D54 |
| Zhang | 2026 | `arXiv:2605.14678` | D55 |
| Zhao | 2022 | `DOI:10.1177/09567976221097615` | D24 |
| Zhao | 2025 | `arXiv:2506.09391` | D33 |
| Zhao | 2025 | `DOI:10.1093/geroni/igaf019` | D44 |
| Zhao | 2025 | `arXiv:2508.03275` | D53 |
| Zhao | 2026 | `arXiv:2607.02118` | D49 |
| Zhao | 2026 | `arXiv:2604.18660` | D53 |
| Zheng | 2023 | `arXiv:2202.13047` | D11 |
| Zheng | 2023 | `arXiv:2306.05685` | D48, D55 |
| Zhong | 2023 | `arXiv:2305.10250` | D13 |
| Zhou | 2020 | `DOI:10.1162/coli_a_00368` | D54 |
| Zhou | 2023 | `arXiv:2307.13854` | D36, D55 |
| Zhu | 2024 | `arXiv:2410.12428` | D43 |
| Zhu | 2025 | `arXiv:2509.16325` | D55 |
| Zhu | 2026 | `arXiv:2604.17972` | D11 |
| Zou | 2026 | `arXiv:2605.09823` | D55 |
| Zucker | 1997 | `DOI:10.1016/S0895-4356(96)00429-5` | D45 |
| Zulfikar | 2024 | `arXiv:2403.02135` | D31 |
| Zumbrunn | 2025 | `DOI:10.1093/ageing/afaf267` | D44 |

