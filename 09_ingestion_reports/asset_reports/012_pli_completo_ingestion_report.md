# Ingestion Report — Programmazione Lineare Intera Completo

## Fonte
`raw_assets/Programmazione Lineare Intera/Programmazione lineare intera completo.pdf`

## Stato
Completato

## Argomenti estratti
- **Modello di Lombardia Manufacturing Co.**: problema decisionale con budget limitato ($10$ milioni), mutua esclusione dei magazzini ($x_3 + x_4 \le 1$), e condizioni di contingenza logica (il magazzino deve essere collocato nella stessa città della fabbrica, $x_3 \le x_1$ e $x_4 \le x_2$).
- **Usi delle variabili binarie**: formulazione di decisioni sì/no in investimenti, selezione di siti, trasporti/spedizioni, accoppiamento velivolo-tratta, e schedulazione di attività mutuamente esclusive.
- **Condizioni logiche avanzate**:
  - Vincoli di tipo "either-or": almeno uno tra due vincoli $f_1(x) \le d_1$ e $f_2(x) \le d_2$ deve essere soddisfatto, formulato come $f_1(x) \le d_1 + M y$ e $f_2(x) \le d_2 + M(1-y)$ con $y \in \{0, 1\}$.
  - Vincoli "$K$ su $N$": esattamente o almeno $K$ vincoli su $N$ devono essere soddisfatti, formulato come $f_i(x) \le d_i + M y_i$ con $\sum y_i = N - K$.
  - Funzioni a valori discreti finiti: una funzione $f(x)$ assume solo valori nell'insieme $\{d_1, d_2, \dots, d_N\}$, formulata come $f(x) = \sum d_i y_i$ con $\sum y_i = 1$ e $y_i \in \{0, 1\}$.
  - Esempio di applicazione su Windor Glass Co. per blocchi discreti di capacità (6, 12, 18 ore).
- **Problema del costo fisso (cariche fisse)**: modellazione di un'attività con costo fisso di attivazione $k > 0$ e costo variabile unitario $c$, con funzione obiettivo minimizzata $k y + c x$ e vincolo di accoppiamento $x \le M y$ con $y \in \{0, 1\}$.
- **Rappresentazione binaria di variabili intere generali**: conversione di una variabile intera limitata $x \in [0, u]$ in variabili binarie aggiuntive $y_k \in \{0, 1\}$ mediante espansione pesata in base 2: $x = \sum_{k=0}^K 2^k y_k$ con $2^K \le u < 2^{K+1}$.
- **Difficoltà dei problemi PLI**: crescita esponenziale delle soluzioni ($2^n$ combinazioni per $n$ variabili binarie), e inutilizzabilità del simplesso standard dovuto alla rimozione di vertici ammissibili.
- **Rilassamento continuo**: definizione, bound forniti dal rilassamento continuo (upper bound per max, lower bound per min).
- **Contro-esempi sull'arrotondamento**:
  - Arrotondando la soluzione del rilassamento continuo si può incorrere in inammissibilità (es. $\max z = x_2$ con $-x_1 + x_2 \le 1/2$, $2x_1 + x_2 \le 7/2$, ottimo rilassato $(1, 1.5)$, arrotondamenti $(1, 2)$ o $(1, 1)$ entrambi inammissibili).
  - L'arrotondamento può portare a soluzioni altamente sub-ottime (es. $\max z = x_1 + 5x_2$ con $x_1 + 10x_2 \le 20$, $x_1 \le 2$, ottimo rilassato $(2, 1.8)$ con $z = 11$; ottimo PLI reale è $(0, 2)$ con $z = 10$; l'arrotondamento all'intero più vicino porta a $(2, 2)$ inammissibile o $(2, 1)$ ammissibile con $z = 7$, molto peggio dell'ottimo intero).

## File creati/aggiornati
- `05_theory/programmazione_lineare_intera/00_index.md` (Aggiornato)
- `05_theory/programmazione_lineare_intera/pli_logica_e_variabili_binarie.md` (Nuovo)
- `07_solved_examples/programmazione_lineare_intera/pli_modellazione_lombardia_manufacturing.md` (Nuovo)
- `10_rag/method_cards/MC_PLI_logica_vincoli_binari.md` (Nuovo)
- `10_rag/method_cards/MC_PLI_rappresentazione_binaria_interi.md` (Nuovo)
- `08_flashcards/programmazione_lineare_intera_logica_e_rappresentazione_flashcards.md` (Nuovo)
- `10_rag/RAG_RETRIEVAL_INDEX.md` (Aggiornato)
- `10_rag/RAG_PATTERN_MAP.md` (Aggiornato)
- `10_rag/RAG_SOURCE_PRIORITY.md` (Aggiornato)
- `README.md` (Aggiornato)
- `TODO.md` (Aggiornato)
- `PROJECT_STATUS.md` (Aggiornato)
- `00_meta/ASSET_TRACKING.md` (Aggiornato)

## Note
Questo asset fornisce la base teorica formale per la modellazione dei vincoli logici e introduce la motivazione matematica del perché il semplice arrotondamento delle variabili continue non sia un metodo affidabile per risolvere problemi interi, giustificando la necessità di algoritmi come il Branch and Bound.
