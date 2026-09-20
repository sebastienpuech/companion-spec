# Challenge a line

This repository publishes verdicts that may be wrong. The procedure below exists so that they can be attacked without writing to us, and so that a challenge can be settled by anyone other than us.

## What can be challenged, and with what

| What you challenge | What you need to produce | Where the material is |
|---|---|---|
| **A coverage score** ("covered", "partial", "none found" for a line; the French table writes them `couvert`, `partiel`, `absent`) | The **product**, its **version or the date** you observed it, and the **precise feature** that provides the coverage. Without a named product, the score stays "none found". | `couverture/tableau_couverture.md`, and the sheet in `dimensions/` |
| **A classification** (already done / exists / buildable / LIMIT) | The published work, or the product, that classifies the line differently, and how it touches the **core** of the line, not its periphery | `mapping_8_verrous.md`, and §5 of the sheet |
| **A root lock** (V1 to V8) | A measurement that contradicts the one cited, or a line attached to the wrong lock | `mapping_8_verrous.md` §5 |
| **A citation** | The identifier, and what is wrong: author, year, or above all what the sheet makes it say | `bibliographie.md`, and the sheet |
| **A novelty claim** | The neighbour we missed, with its identifier and the share of the object it covers | `note_methode.md` §4 |
| **The scope itself** (a line is missing, or two lines are really one) | The missing capability, described like the others: human mechanism, expected behaviour, what establishes it | `dimensions/` for the template |

## The template

Open an *issue* on the repository, or send this block filled in. English is fine. The first five fields are needed, the sixth is optional: without the third, the challenge cannot be settled; without the fifth, it is not dated, so it will go stale without anyone knowing when.

```
LINE           : Dnn (e.g. D22 A cared-for ending)
WHAT I         : (e.g. "the 'none found' coverage score", "the attachment of D18 to V7")
CHALLENGE
THE EVIDENCE   : product + version or date + precise feature
                 OR identifier of the work (arXiv:… / DOI:…) + what it shows
WHAT IT        : (e.g. "the line moves from 'none found' to 'partial'", "lock V7 does not
CHANGES          explain it")
OBSERVED ON    : dd/mm/yyyy. The date matters: the field moves every week
WHO I AM       : optional, but say so if you have an interest in the product cited
```

## How it is handled

1. **Every challenge carrying the five required fields enters the table**, including when it proves us wrong. That is the point of the procedure.
2. A challenge to a **coverage score** is treated as a judge's score: it does not replace the existing score, it is added to it, and the published count will be that of the majority vote of three judges (`kit_juges.md`). Today there is a single rater; the two other judges have not scored yet.
3. A challenge to a **citation** is checked by the gate (`python tools/check_citations.py`), then by hand against the source. If it is founded, the sheet is corrected, the correction is dated, and the previous version stays in the history.
4. **What is refused, and why**, is written down too. A repository that only displays the challenges it accepted proves nothing.

## What cannot be settled

- **The pilot's measurements** cannot be reproduced by a third party: they read a private database, which is not provided. The script is published and its outputs are dated, but you cannot replay them. You can only challenge what we conclude from them.
- **The completeness of the 56 lines** cannot be demonstrated. One can show that a line is missing; one cannot show that none is. The method note says where the stop was decided, and with what reservation.
