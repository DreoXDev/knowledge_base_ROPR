# Ingestion Report — PNL 1D

## Metadata

- Source IDs:
  - `SRC-0090` (`raw_assets/Programmazione Non Lineare/PNL 1D.pdf`)
- Tipo file: PDF
- Categoria: Slide ufficiali dei docenti
- Area ROPR: Programmazione Non Lineare (PNL) - Ottimizzazione Unidimensionale
- Affidabilità: Ufficiale (official)
- Stato analisi: Completato (consolidated)

## Sintesi Contenuto

Questo asset si concentra sull'ottimizzazione non lineare in una variabile reale $f(x)$ sia per via analitica ($f'(x^*) = 0$) che numerica. Presenta in dettaglio due algoritmi classici: il metodo di bisezione (algoritmo dicotomico basato sul restringimento progressivo di un intervallo di incertezza) e il metodo di Newton 1D (algoritmo di approssimazione quadratica basato sullo sviluppo di Taylor). Viene descritto in dettaglio il calcolo iterativo per massimizzare la funzione concava $f(x) = 12x - 3x^4 - 2x^6$ nell'intervallo $[0, 2]$.

## Argomenti Estratti

- **Ottimizzazione in una variabile**: Problema di massimo per funzione concava e minimo per funzione convessa; condizione necessaria del primo ordine $f'(x^*) = 0$.
- **Algoritmi numerici**: Motivazioni e confronto tra algoritmi dicotomici (ricerca dello zero della derivata prima in un intervallo dimezzato ad ogni passo) e algoritmi di approssimazione (Taylor quadratico).
- **Criteri di arresto**: Condizioni per interrompere la computazione ($|f'(x_k)| < \epsilon$, numero massimo di iterazioni $N$, progresso delle variabili $|x_{k+1} - x_k| < \epsilon$, progresso dell'obiettivo $|f(x_{k+1}) - f(x_k)| < \epsilon$, divergenza, cicli).
- **Metodo di Bisezione**:
  - Ipotesi: funzione continua, derivabile e concava/convessa su un intervallo limitato.
  - Aggiornamento degli estremi $\underline{x}$ (inferiore) e $\bar{x}$ (superiore) in base al segno di $f'(x_k)$.
  - Criterio di arresto $\bar{x} - \underline{x} \le 2\epsilon$.
  - Calcolo dettagliato delle prime 3 iterazioni su $f(x) = 12x - 3x^4 - 2x^6$.
- **Metodo di Newton 1D**:
  - Approssimazione quadratica locale con Taylor: $f(x_{k+1}) \approx f(x_k) + f'(x_k)(x_{k+1}-x_k) + \frac{1}{2}f''(x_k)(x_{k+1}-x_k)^2$.
  - Formula di ricorrenza: $x_{k+1} = x_k - \frac{f'(x_k)}{f''(x_k)}$.
  - Criteri di arresto: $|x_{k+1} - x_k| \le \epsilon$.
  - Rischi: derivata seconda nulla ($f''(x_k) = 0$), punto iniziale troppo lontano (divergenza), convergenza a punti non desiderati.
- **Confronto**: Bisezione (lento ma molto robusto, richiede solo $f'$) vs Newton (convergenza quadratica molto veloce, richiede $f''$, rischio divergenza).

## File Creati / Aggiornati

- [pnl_ottimizzazione_unidimensionale.md](../../05_theory/programmazione_non_lineare/pnl_ottimizzazione_unidimensionale.md)
- [pnl_metodo_bisezione.md](../../04_methods/programmazione_non_lineare/pnl_metodo_bisezione.md)
- [pnl_metodo_newton_1d.md](../../04_methods/programmazione_non_lineare/pnl_metodo_newton_1d.md)
- [pnl_confronto_bisezione_newton.md](../../04_methods/programmazione_non_lineare/pnl_confronto_bisezione_newton.md)
- [pnl_bisezione_funzione_concava.md](../../07_solved_examples/programmazione_non_lineare/pnl_bisezione_funzione_concava.md)
- [pnl_newton_funzione_1d.md](../../07_solved_examples/programmazione_non_lineare/pnl_newton_funzione_1d.md)
- [pnl_pattern_ottimizzazione_1d.md](../../06_exam_patterns/pnl_pattern_ottimizzazione_1d.md)
- [MC_PNL_metodo_bisezione_1d.md](../../10_rag/method_cards/MC_PNL_metodo_bisezione_1d.md)
- [MC_PNL_metodo_newton_1d.md](../../10_rag/method_cards/MC_PNL_metodo_newton_1d.md)
- [MC_PNL_ottimizzazione_1d_condizioni_ottimalita.md](../../10_rag/method_cards/MC_PNL_ottimizzazione_1d_condizioni_ottimalita.md)
- [TC_PNL_ottimizzazione_1d.md](../../10_rag/topic_cards/TC_PNL_ottimizzazione_1d.md)
- [TC_PNL_bisezione_newton.md](../../10_rag/topic_cards/TC_PNL_bisezione_newton.md)
- [pnl_1d_flashcards.md](../../08_flashcards/pnl_1d_flashcards.md)
- [PNL_1D_bisezione_newton.csv](../../flashcards/PNL_1D_bisezione_newton.csv)
