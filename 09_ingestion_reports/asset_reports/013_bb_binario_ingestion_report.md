# Ingestion Report — Branch and Bound Binario

## Fonte
`raw_assets/Programmazione Lineare Intera/Programmazione Lineare Intera_Branch and Bound binario.pdf`

## Stato
Completato

## Argomenti estratti
- **Tecnica di branching per problemi binari (PB)**: divisione dello spazio ammissibile fissando una variabile decisionale $x_k = 0$ per un sotto-problema e $x_k = 1$ per l'altro. Genera alberi binari simmetrici.
- **Euristica di ordinamento delle variabili**: uso dell'ordinamento naturale delle variabili ($x_1, x_2, \dots$) come politica predefinita per la selezione della variabile di branching ad ogni nodo.
- **Bounding e limitazioni continue**: risoluzione della versione rilassata inserendo i vincoli $0 \le x_j \le 1$ per ogni variabile non ancora fissata.
- **Arrotondamento all'intero dei bound (Integer Bounding)**: se i coefficienti della funzione obiettivo sono interi e le variabili decisionali devono essere intere, il valore dell'ottimo intero deve essere intero.
  - Per problemi di massimo: il bound reale $Z$ del rilassamento continuo può essere arrotondato per difetto ($\lfloor Z \rfloor$). Ad esempio, $Z_{\text{rilassato}} = 16.5 \implies Z_{\text{bound}} = 16$.
- **Fathoming (Criteri di chiusura dei nodi)**:
  - *Ottimalità intera*: la soluzione ottima del rilassamento soddisfa l'integrità. Fornisce un candidato incumbent ($Z_I$).
  - *Dominanza*: il bound del nodo è inferiore o uguale all'incumbent corrente ($Z_S \le Z_I$ per massimo).
  - *Inammissibilità*: il rilassamento del sotto-problema non ammette soluzioni ammissibili ($\emptyset$).
- **Esempio svolto passo-passo Lombardia Manufacturing Co.**:
  - $P_0$ (Rilassamento completo): $x = (5/6, 1, 0, 1)$, $z = 16.5 \implies Z_{\text{bound}} = 16$. Branching su $x_1$.
  - $P_1$ ($x_1 = 0$): $x = (0, 1, 0, 1)$, $z = 9$. Soluzione intera! Primo incumbent $Z_I = 9$. Chiuso per interezza.
  - $P_2$ ($x_1 = 1$): $x = (1, 4/5, 0, 4/5)$, $z = 16.2 \implies Z_{\text{bound}} = 16$. Branching su $x_2$.
  - $P_3$ ($x_1 = 1, x_2 = 0$): $x = (1, 0, 4/5, 0)$, $z = 13.8 \implies Z_{\text{bound}} = 13$. Aperto.
  - $P_4$ ($x_1 = 1, x_2 = 1$): $x = (1, 1, 0, 1/2)$, $z = 16$. Branching su $x_3$.
  - $P_5$ ($x_1 = 1, x_2 = 1, x_3 = 0$): $x = (1, 1, 0, 1/2)$, $z = 16$. Branching su $x_4$.
  - $P_6$ ($x_1 = 1, x_2 = 1, x_3 = 1$): Inammissibile. Chiuso.
  - $P_7$ ($x_1 = 1, x_2 = 1, x_3 = 0, x_4 = 0$): $x = (1, 1, 0, 0)$, $z = 14$. Nuova soluzione intera! Aggiornato incumbent $Z_I = 14$. Chiuso per interezza.
  - $P_8$ ($x_1 = 1, x_2 = 1, x_3 = 0, x_4 = 1$): Inammissibile. Chiuso.
  - Chiusura finale per dominanza di $P_3$ ($Z_{\text{bound}} = 13 \le Z_I = 14$). Ottimo a $(1, 1, 0, 0)$ con $z^* = 14$.

## File creati/aggiornati
- `05_theory/programmazione_lineare_intera/00_index.md` (Aggiornato)
- `05_theory/programmazione_lineare_intera/pli_branch_and_bound_binario.md` (Nuovo)
- `07_solved_examples/programmazione_lineare_intera/pli_bb_binario_lombardia_manufacturing.md` (Nuovo)
- `10_rag/method_cards/MC_PLI_branch_and_bound_binario.md` (Nuovo)
- `08_flashcards/programmazione_lineare_intera_bb_binario_flashcards.md` (Nuovo)
- `10_rag/RAG_RETRIEVAL_INDEX.md` (Aggiornato)
- `10_rag/RAG_PATTERN_MAP.md` (Aggiornato)
- `10_rag/RAG_SOURCE_PRIORITY.md` (Aggiornato)
- `README.md` (Aggiornato)
- `00_meta/ASSET_TRACKING.md` (Aggiornato)

## Note
L'asset dettaglia in modo chiaro la procedura algoritmica applicata a problemi a variabili binarie, evidenziando il ruolo determinante dell'arrotondamento del bound all'intero, tecnica fondamentale per velocizzare la potatura all'esame scritto.
