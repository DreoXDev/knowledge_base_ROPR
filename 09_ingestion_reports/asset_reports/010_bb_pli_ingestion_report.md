# Ingestion Report — BB PLI

## Fonte
`raw_assets/Programmazione Lineare Intera/BB PLI.pdf`

## Stato
Completato

## Argomenti estratti
- **Scelte progettuali del Branch and Bound**: selezione del nodo da esplorare, selezione della variabile di branching, scelta del rilassamento e criteri di fathoming ed arresto.
- **Strategie di visita dell'albero**: Depth First (LIFO, memoria ridotta, incumbent precoce) e Best Bound First (scelta del miglior bound, minor numero di nodi, memoria elevata).
- **Branch and Bound per PLIM (Programmazione Lineare Intera Mista)**: branching limitato alle sole variabili intere frazionarie, assenza di arrotondamento automatico dei bound rilassati, ammissibilità di soluzioni con variabili continue frazionarie.
- **Rilassamento lagrangiano**: introduzione matematica, calcolo di bound e relazione con il duale lagrangiano.
- **Criteri di arresto e soluzioni quasi-ottime**: tolleranza assoluta ($K$) e relativa ($\alpha$), calcolo del gap di ottimalità assoluto/relativo.
- **Soluzioni ottime alternative**: test di fathoming con disuguaglianze strette per l'enumerazione di ottimi alternativi.
- **Interpretazione albero di B&B**: riconoscimento del tipo di problema ($\max/\min$) dall'andamento di $LB/UB$ da padre a figlio, calcolo dell'intervallo dell'ottimo, chiusura nodi e scelta del prossimo nodo in BBF.

## File creati/aggiornati
- `05_theory/programmazione_lineare_intera/00_index.md` (Aggiornato)
- `05_theory/programmazione_lineare_intera/pli_branch_and_bound.md` (Aggiornato)
- `05_theory/programmazione_lineare_intera/pli_scelte_branch_and_bound.md` (Nuovo)
- `05_theory/programmazione_lineare_intera/pli_branch_and_bound_plim.md` (Nuovo)
- `05_theory/programmazione_lineare_intera/pli_rilassamento_lagrangiano.md` (Nuovo)
- `05_theory/programmazione_lineare_intera/pli_soluzioni_quasi_ottime.md` (Nuovo)
- `05_theory/programmazione_lineare_intera/pli_soluzioni_ottime_alternative.md` (Nuovo)
- `04_methods/programmazione_lineare_intera/pli_interpretare_albero_branch_and_bound.md` (Nuovo)
- `04_methods/programmazione_lineare_intera/pli_calcolare_gap_branch_and_bound.md` (Nuovo)
- `07_solved_examples/programmazione_lineare_intera/pli_plim_bb_esercizio_svolto.md` (Nuovo)
- `10_rag/method_cards/MC_PLI_branch_and_bound_plim.md` (Nuovo)
- `10_rag/method_cards/MC_PLI_interpretare_albero_branch_and_bound.md` (Nuovo)
- `10_rag/method_cards/MC_PLI_gap_ottimalita_branch_and_bound.md` (Nuovo)
- `10_rag/method_cards/MC_PLI_soluzione_quasi_ottima_branch_and_bound.md` (Nuovo)
- `10_rag/topic_cards/TC_PLI_branch_and_bound_plim.md` (Nuovo)
- `10_rag/topic_cards/TC_PLI_interpretazione_albero.md` (Nuovo)
- `08_flashcards/programmazione_lineare_intera_bb_plim_flashcards.md` (Nuovo)
- `06_exam_patterns/pattern_interpretazione_albero_branch_and_bound.md` (Nuovo)
- `06_exam_patterns/pattern_branch_and_bound_plim.md` (Nuovo)
- `06_exam_patterns/PATTERN_INDEX.md` (Aggiornato)
- `06_exam_patterns/PATTERN_MAP.md` (Aggiornato)
- `AI Chat during Exam/Final Prompt.md` (Aggiornato)
- `README.md` (Aggiornato)
- `TODO.md` (Aggiornato)
- `PROJECT_STATUS.md` (Aggiornato)
- `00_meta/ASSET_TRACKING.md` (Aggiornato)

## Note
L'asset integra la teoria classica e le procedure operative per la risoluzione d'esame in presenza di variabili continue o quesiti concettuali sugli alberi decisionali.
