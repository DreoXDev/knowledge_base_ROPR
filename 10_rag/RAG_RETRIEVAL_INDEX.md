# RAG Retrieval Index - ROPR

Indice semi-automatico dei file utili al retrieval.

## File indicizzabili

- `04_methods/programmazione_lineare/pl_formulazione_modelli.md`
- `04_methods/programmazione_lineare/pl_metodo_due_fasi.md`
- `04_methods/programmazione_lineare/pl_simplesso_tabellare.md`
- `04_methods/programmazione_lineare/pl_variabili_libere_e_segno.md`
- `05_theory/00_index.md`
- `05_theory/programmazione_lineare/01_introduzione_programmazione_lineare.md`
- `05_theory/programmazione_lineare/02_formulazione_generale_pl.md`
- `05_theory/programmazione_lineare/03_soluzione_grafica_pl.md`
- `05_theory/programmazione_lineare/04_regione_ammissibile_e_casi.md`
- `05_theory/programmazione_lineare/05_assunzioni_programmazione_lineare.md`
- `05_theory/programmazione_lineare/06_simplesso.md`
- `05_theory/programmazione_lineare/07_metodo_due_fasi.md`
- `05_theory/programmazione_lineare/08_formulazione_modelli_pl.md`
- `05_theory/programmazione_lineare/09_cammino_minimo_dualita.md`
- `05_theory/programmazione_lineare/10_dualita.md`
- `05_theory/programmazione_lineare/11_regole_costruire_duale.md`
- `07_solved_examples/programmazione_lineare/distribution_network_min_cost_flow.md`
- `07_solved_examples/programmazione_lineare/pl_cammino_minimo_formulazione.md`
- `07_solved_examples/programmazione_lineare/pl_duale_vincoli_misti.md`
- `07_solved_examples/programmazione_lineare/pl_due_fasi_esempio_base.md`
- `07_solved_examples/programmazione_lineare/pl_due_fasi_problema_illimitato.md`
- `07_solved_examples/programmazione_lineare/pl_due_fasi_problema_non_ammissibile.md`
- `07_solved_examples/programmazione_lineare/pl_simplesso_esempio_40_50.md`
- `07_solved_examples/programmazione_lineare/pl_simplesso_max_3x_5y.md`
- `07_solved_examples/programmazione_lineare/pl_tool_spa_duale.md`
- `07_solved_examples/programmazione_lineare/pl_tool_spa_simplesso.md`
- `07_solved_examples/programmazione_lineare/pl_turni_lavoro_formulazione.md`
- `07_solved_examples/programmazione_lineare/wyndor_glass.md`
- `06_exam_patterns/common_mistakes.md`
- `06_exam_patterns/PATTERN_INDEX.md`
- `06_exam_patterns/PATTERN_MAP.md`

## Programmazione Lineare — Introduzione

Fonti:
- `raw_assets/Programmazione Lineare/Ricerca Operativa - Introduzione a PL - 23-24.pdf`
- `05_theory/programmazione_lineare/01_introduzione_programmazione_lineare.md`
- `05_theory/programmazione_lineare/02_formulazione_generale_pl.md`
- `05_theory/programmazione_lineare/03_soluzione_grafica_pl.md`
- `05_theory/programmazione_lineare/04_regione_ammissibile_e_casi.md`
- `05_theory/programmazione_lineare/05_assunzioni_programmazione_lineare.md`
- `07_solved_examples/programmazione_lineare/wyndor_glass.md`
- `07_solved_examples/programmazione_lineare/distribution_network_min_cost_flow.md`

Concetti:
- modello di Programmazione Lineare;
- variabili decisionali;
- funzione obiettivo;
- vincoli funzionali;
- vincoli di non negatività;
- regione ammissibile;
- soluzione grafica;
- poliedro convesso;
- politopo;
- soluzione ottima unica;
- infinite soluzioni ottime;
- problema illimitato;
- problema inammissibile;
- assunzioni della PL;
- flusso a costo minimo.

## Programmazione Lineare — Algoritmi e Formulazione (Lezione 3)

Fonti:
- `raw_assets/Programmazione Lineare/lezione 3 completa.pdf`
- `05_theory/programmazione_lineare/06_simplesso.md`
- `05_theory/programmazione_lineare/07_metodo_due_fasi.md`
- `05_theory/programmazione_lineare/08_formulazione_modelli_pl.md`
- `07_solved_examples/programmazione_lineare/pl_turni_lavoro_formulazione.md`
- `07_solved_examples/programmazione_lineare/pl_simplesso_esempio_40_50.md`
- `07_solved_examples/programmazione_lineare/pl_tool_spa_simplesso.md`
- `07_solved_examples/programmazione_lineare/pl_simplesso_max_3x_5y.md`
- `07_solved_examples/programmazione_lineare/pl_due_fasi_esempio_base.md`
- `07_solved_examples/programmazione_lineare/pl_due_fasi_problema_illimitato.md`
- `07_solved_examples/programmazione_lineare/pl_due_fasi_problema_non_ammissibile.md`

Concetti:
- workforce scheduling / pianificazione turni di lavoro;
- simplesso tabellare;
- riga obiettivo / riga 0;
- variabili di slack e surplus;
- variabili artificiali;
- pivot / variabile entrante / variabile uscente;
- test dei rapporti minimi;
- metodo delle due fases (Fase 1 e Fase 2);
- problema illimitato;
- problema non ammissibile;
- variabili libere e variabili non positive;
- Tool.Spa.

## Programmazione Lineare — Cammino Minimo e Dualità (Week 4)

Fonti:
- `raw_assets/Programmazione Lineare/lec_w4_completa.pdf`
- `05_theory/programmazione_lineare/09_cammino_minimo_dualita.md`
- `05_theory/programmazione_lineare/10_dualita.md`
- `05_theory/programmazione_lineare/11_regole_costruire_duale.md`
- `07_solved_examples/programmazione_lineare/pl_cammino_minimo_formulazione.md`
- `07_solved_examples/programmazione_lineare/pl_tool_spa_duale.md`
- `07_solved_examples/programmazione_lineare/pl_duale_vincoli_misti.md`

Concetti:
- cammino minimo su grafo orientato pesato;
- variabili binarie sugli archi;
- vincoli di conservazione del flusso (bilancio nei nodi);
- intuizione economica della dualità;
- problema primale e problema duale;
- teorema della dualità forte ($Z^* = Z'^*$);
- lettura delle variabili duali (prezzi ombra) dal tableau ottimo;
- regole di transizione primale-duale (MAX-MIN e MIN-MAX);
- variabili/vincoli canonici, anticanonici e liberi.

## Query d'esame -> file da consultare

| Query / richiesta | Prima fonte | Seconda fonte | Note |
|---|---|---|---|
| formulare un modello di programmazione lineare | `04_methods/programmazione_lineare/pl_formulazione_modelli.md` | `05_theory/programmazione_lineare/02_formulazione_generale_pl.md` | |
| formulare problema dei turni / workforce scheduling | `04_methods/programmazione_lineare/pl_formulazione_modelli.md` | `07_solved_examples/programmazione_lineare/pl_turni_lavoro_formulazione.md` | |
| risolvere con simplesso tabellare | `04_methods/programmazione_lineare/pl_simplesso_tabellare.md` | `07_solved_examples/programmazione_lineare/pl_simplesso_esempio_40_50.md` | |
| metodo delle due fasi | `04_methods/programmazione_lineare/pl_metodo_due_fasi.md` | `07_solved_examples/programmazione_lineare/pl_due_fasi_esempio_base.md` | |
| scrivere il duale | `10_rag/method_cards/METHOD_PL_DUALE.md` | `05_theory/programmazione_lineare/11_regole_costruire_duale.md` | |
| branch and bound | `04_methods/programmazione_lineare_intera/` | `07_solved_examples/programmazione_lineare_intera/` | Da completare dopo ingestion |
| condizioni KKT | `04_methods/programmazione_non_lineare/` | `05_theory/programmazione_non_lineare/` | Da completare dopo ingestion |
| flusso a costo minimo | `10_rag/method_cards/PL_minimum_cost_flow.md` | `07_solved_examples/programmazione_lineare/distribution_network_min_cost_flow.md` | |
| soluzione grafica di PL | `10_rag/method_cards/PL_soluzione_grafica.md` | `05_theory/programmazione_lineare/03_soluzione_grafica_pl.md` | |
| gestione variabili libere o negative | `04_methods/programmazione_lineare/pl_variabili_libere_e_segno.md` | `07_solved_examples/programmazione_lineare/pl_due_fasi_problema_illimitato.md` | |
| rilevare problema illimitato | `04_methods/programmazione_lineare/pl_simplesso_tabellare.md` | `07_solved_examples/programmazione_lineare/pl_due_fasi_problema_illimitato.md` | |
| rilevare problema non ammissibile | `04_methods/programmazione_lineare/pl_metodo_due_fasi.md` | `07_solved_examples/programmazione_lineare/pl_due_fasi_problema_non_ammissibile.md` | |
| formulare cammino minimo | `10_rag/method_cards/METHOD_PL_CAMMINO_MINIMO.md` | `05_theory/programmazione_lineare/09_cammino_minimo_dualita.md` | |
| variabili duali dal tableau | `05_theory/programmazione_lineare/10_dualita.md` | | |
| variabili canoniche/anticanoniche | `05_theory/programmazione_lineare/11_regole_costruire_duale.md` | | |
