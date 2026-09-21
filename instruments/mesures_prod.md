Mesure de production du 2026-09-20 — base `coach.db`, 69 tables, lecture seule.

| # | Mesure | Table | Valeur | Statut |
|---|---|---|---|---|
| 1 | messages échangés | `message_chat` | 1 001 | mesuré |
| 2 | messages émis par le coach | `message_chat` | 572 | mesuré |
| 3 | messages émis par l'utilisateur | `message_chat` | 429 | mesuré |
| 4 | jours actifs (au moins un échange) | `message_chat` | 87 | mesuré |
| 5 | date du premier message | `message_chat` | 2026-05-07 | mesuré |
| 6 | date du dernier message | `message_chat` | 2026-09-20 | mesuré |
| 7 | jours calendaires depuis le premier message (inclus, jusqu'à la date de mesure) | `message_chat` | 137 | mesuré |
| 8 | notes de mémoire | `memoire_note` | 289 | mesuré |
| 9 | notes de mémoire par statut | `memoire_note` | actif 269, archivé 4, sanctuarisé 16 | mesuré |
| 10 | plus ancienne note | `memoire_note` | 2026-06-28 | mesuré |
| 11 | liens entre notes | `memory_link` | 1 454 | mesuré |
| 12 | rappels journalisés | `memory_recall_log` | 602 | mesuré |
| 13 | rappels journalisés par canal | `memory_recall_log` | auto_recall 455, convictions 69, portrait 17, tool 61 | mesuré |
| 14 | séances importées (Strava) | `seance_reelle` | 78 | mesuré |
| 15 | séances planifiées | `seance_prevue` | 107 | mesuré |
| 16 | première séance importée | `seance_reelle` | 2026-05-02 | mesuré |
| 17 | principes indexés (KB) | `principe` | 4 279 | mesuré |
| 18 | audits d'omission | `omission_audit` | 55 | mesuré |
| 19 | affirmations du Dossier | `dossier_claim` | 64 | mesuré |
| 20 | observations du Dossier | `dossier_observation` | 108 | mesuré |
| 21 | prédictions scellées du Dossier | `dossier_prediction` | 24 | mesuré |
| 22 | instantanés du modèle mental | `user_mental_model` | 208 | mesuré |
| 23 | entrées de mémoire de cœur | `core_memory` | 62 | mesuré |
| 24 | intentions suivies | `intention` | 57 | mesuré |
| 25 | notes sanctuarisées | `memoire_note` | 16 | mesuré |
| 26 | retours explicites | `feedback_explicite` | 0 | mesuré |
| 27 | dérives factuelles journalisées | — | — | non mesurable (aucune table : le bot les écrit dans ses logs (`_log_grounding_divergence`) — voir --logs) |
| 28 | convictions (table dédiée) | `conviction` | 0 | mesuré |
| 29 | initiatives journalisées | `initiative_coach` | 0 | mesuré |
| 30 | hypothèses N-of-1 tranchées | `hypothese` | 0 | mesuré |
| 31 | relevés de poids | `poids_releve` | 0 | mesuré |
| 32 | chantiers | `chantier` | 3 | mesuré |
| 33 | événements de situation | `situation_event` | 0 | mesuré |
| 34 | anomalies de situation détectées | `situation_anomaly` | 3 | mesuré |
| 35 | jours où le coach parle le premier (premier message du jour émis par le coach) | `message_chat` | 57 | mesuré |
| 36 | part des jours actifs où le coach parle le premier | `message_chat` | 65,5% | mesuré |
| 37 | part des jours calendaires où le coach parle le premier | `message_chat` | 41,6% | mesuré |
| 38 | rappels déclenchés par une question (hors briefing systématique) | `memory_recall_log` | 515 | mesuré |
| 39 | notes servies par ces rappels | `memory_recall_log` | 2 184 | mesuré |
| 40 | âge médian d'une note servie, en jours | `memoire_note` | 9 | mesuré |
| 41 | part des notes servies créées il y a plus de 30 jours | `memoire_note` | 15,3% | mesuré |
| 42 | notes portant le tag du retour explicite (la table dédiée est vide) | `memoire_note` | 19 | mesuré |
| 43 | prédictions scellées puis résolues (la table `hypothese` est vide) | `dossier_prediction` | 22 | mesuré |

Tables annoncées comme capacités et toujours vides (6) : `hypothese`, `conviction`, `feedback_explicite`, `initiative_coach`, `poids_releve`, `situation_event`.
Tables vides au total (hors index vectoriels) : 13 — `contestation_sceptique`, `contexte_quotidien`, `conviction`, `entretien_strategique`, `feedback_explicite`, `hypothese`, `initiative_coach`, `modification_plan`, `poids_releve`, `retour_sebastien`, `segment`, `situation_attente`, `situation_event`.
