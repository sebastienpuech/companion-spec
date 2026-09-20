Mesure de production du 2026-09-04 — base `coach.db`, 69 tables, lecture seule.

| # | Mesure | Table | Valeur | Statut |
|---|---|---|---|---|
| 1 | messages échangés | `message_chat` | 924 | mesuré |
| 2 | messages émis par le coach | `message_chat` | 520 | mesuré |
| 3 | messages émis par l'utilisateur | `message_chat` | 404 | mesuré |
| 4 | jours actifs (au moins un échange) | `message_chat` | 72 | mesuré |
| 5 | date du premier message | `message_chat` | 2026-05-07 | mesuré |
| 6 | date du dernier message | `message_chat` | 2026-09-04 | mesuré |
| 7 | jours calendaires depuis le premier message (inclus, jusqu'à la date de mesure) | `message_chat` | 121 | mesuré |
| 8 | notes de mémoire | `memoire_note` | 247 | mesuré |
| 9 | notes de mémoire par statut | `memoire_note` | actif 228, archivé 3, resolu 1, sanctuarisé 15 | mesuré |
| 10 | plus ancienne note | `memoire_note` | 2026-06-28 | mesuré |
| 11 | liens entre notes | `memory_link` | 1 247 | mesuré |
| 12 | rappels journalisés | `memory_recall_log` | 479 | mesuré |
| 13 | rappels journalisés par canal | `memory_recall_log` | auto_recall 403, convictions 17, portrait 3, tool 56 | mesuré |
| 14 | séances importées (Strava) | `seance_reelle` | 71 | mesuré |
| 15 | séances planifiées | `seance_prevue` | 77 | mesuré |
| 16 | première séance importée | `seance_reelle` | 2026-05-02 | mesuré |
| 17 | principes indexés (KB) | `principe` | 4 279 | mesuré |
| 18 | audits d'omission | `omission_audit` | 51 | mesuré |
| 19 | affirmations du Dossier | `dossier_claim` | 57 | mesuré |
| 20 | observations du Dossier | `dossier_observation` | 79 | mesuré |
| 21 | prédictions scellées du Dossier | `dossier_prediction` | 17 | mesuré |
| 22 | instantanés du modèle mental | `user_mental_model` | 185 | mesuré |
| 23 | entrées de mémoire de cœur | `core_memory` | 48 | mesuré |
| 24 | intentions suivies | `intention` | 38 | mesuré |
| 25 | notes sanctuarisées | `memoire_note` | 15 | mesuré |
| 26 | retours explicites | `feedback_explicite` | 0 | mesuré |
| 27 | dérives factuelles journalisées | — | 0 | mesuré hors base (logs) (aucune table : le bot les écrit dans ses logs (`_log_grounding_divergence`) — voir --logs) |
| 28 | convictions (table dédiée) | `conviction` | 0 | mesuré |
| 29 | initiatives journalisées | `initiative_coach` | 0 | mesuré |
| 30 | hypothèses N-of-1 | `hypothese` | 0 | mesuré |
| 31 | relevés de poids | `poids_releve` | 0 | mesuré |
| 32 | chantiers | `chantier` | 3 | mesuré |
| 33 | événements de situation | `situation_event` | 0 | mesuré |
| 34 | anomalies de situation détectées | `situation_anomaly` | 3 | mesuré |
| 35 | jours où le coach parle le premier (premier message du jour émis par le coach) | `message_chat` | 44 | mesuré |
| 36 | part des jours actifs où le coach parle le premier | `message_chat` | 61,1% | mesuré |
| 37 | part des jours calendaires où le coach parle le premier | `message_chat` | 36,4% | mesuré |

Tables annoncées comme capacités et toujours vides (6) : `hypothese`, `conviction`, `feedback_explicite`, `initiative_coach`, `poids_releve`, `situation_event`.
Tables vides au total (hors index vectoriels) : 13 — `contestation_sceptique`, `contexte_quotidien`, `conviction`, `entretien_strategique`, `feedback_explicite`, `hypothese`, `initiative_coach`, `modification_plan`, `poids_releve`, `retour_sebastien`, `segment`, `situation_attente`, `situation_event`.
