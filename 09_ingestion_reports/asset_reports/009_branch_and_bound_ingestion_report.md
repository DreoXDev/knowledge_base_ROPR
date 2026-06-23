# Ingestion Report — Algoritmo Branch and Bound (PLI)

## Fonti
- `raw_assets/Programmazione Lineare Intera/branch_and_bound.pdf`
- `raw_assets/Programmazione Lineare Intera/BB PLI.pdf`
- `raw_assets/Programmazione Lineare Intera/Programmazione Lineare Intera_Branch and Bound binario.pdf`
- `raw_assets/Programmazione Lineare Intera/16_esercizi_BB.pdf`

## Stato
Completato

## Argomenti estratti
- Fondamenti teorici del Branch and Bound (Branching, Bounding, Fathoming/Potatura).
- Regole di branching (ramificazione per variabili intere e binarie).
- Regole di potatura per inammissibilità, ottimalità intera e dominanza.
- Strategie di visita dell'albero: profondità (Depth-First), miglior bound (Best-Bound-First) e ampiezza (Breadth-First).
- Algoritmo Greedy per il calcolo di valutazioni inferiori (euristica intera) e superiori (rilassamento continuo) nel problema dello zaino (knapsack).
- Risoluzione passo-passo di esercizi d'esame.

## File creati/aggiornati
- `05_theory/programmazione_lineare_intera/pli_branch_and_bound.md` (Nuovo)
- `05_theory/programmazione_lineare_intera/00_index.md` (Aggiornato)
- `04_methods/programmazione_lineare_intera/pli_algoritmo_branch_and_bound.md` (Nuovo)
- `04_methods/programmazione_lineare_intera/pli_algoritmo_branch_and_bound_binario.md` (Nuovo)
- `04_methods/programmazione_lineare_intera/pli_greedy_zaino.md` (Nuovo)
- `07_solved_examples/programmazione_lineare_intera/pli_bb_esercizio_svolto_1.md` (Nuovo)
- `07_solved_examples/programmazione_lineare_intera/pli_bb_esercizio_svolto_zaino.md` (Nuovo)
- `10_rag/method_cards/MC_PLI_branch_and_bound.md` (Nuovo)
- `10_rag/method_cards/MC_PLI_zaino_greedy.md` (Nuovo)
- `10_rag/topic_cards/TC_PLI_branch_and_bound.md` (Nuovo)
- `10_rag/RAG_RETRIEVAL_INDEX.md` (Aggiornato)
- `10_rag/RAG_PATTERN_MAP.md` (Aggiornato)
- `10_rag/RAG_SOURCE_PRIORITY.md` (Aggiornato)
- `08_flashcards/programmazione_lineare_intera_bb_flashcards.md` (Nuovo)
- `AI Chat during Exam/Final Prompt.md` (Aggiornato)
- `README.md` (Aggiornato)
- `TODO.md` (Aggiornato)
- `PROJECT_STATUS.md` (Aggiornato)
- `00_meta/ASSET_TRACKING.md` (Aggiornato)

## Note
Tutte le procedure e gli algoritmi seguono rigidamente la notazione del docente Mauro Passacantando. In particolare, per il B&B su zaino si utilizza l'ordinamento greedy per il calcolo rapido dei bound del rilassamento continuo.
