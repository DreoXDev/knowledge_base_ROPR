# Topic Card: Ottimizzazione Unidimensionale (1D)

- **Ottimizzazione 1D**: Ricerca di massimi/minimi di $f(x)$ su $\mathbb{R}$ o su un intervallo limitato.
- **Condizione del Primo Ordine**: Un punto stazionario interno soddisfa l'equazione $f'(x^*) = 0$.
- **Classificazione**:
  - $f''(x^*) < 0 \implies$ **Massimo locale**.
  - $f''(x^*) > 0 \implies$ **Minimo locale**.
  - $f''(x^*) = 0 \implies$ Test inconclusivo (richiede derivate di ordine superiore).
- **Ottimalità Globale**:
  - Se la funzione è concava globale ($f''(x) \le 0 \ \forall x$) $\implies$ il punto stazionario è un **massimo globale**.
  - Se la funzione è convessa globale ($f''(x) \ge 0 \ \forall x$) $\implies$ il punto stazionario è un **minimo globale**.
- **Analitico vs Numerico**:
  - **Analitico**: Risoluzione diretta di $f'(x) = 0$. Possibile solo per forme funzionali semplici.
  - **Numerico**: Algoritmi iterativi (Bisezione, Newton) per approssimare la radice della derivata prima quando non risolvibile analiticamente.
- **Fonti**: [[pnl_ottimizzazione_unidimensionale|Teoria 1D]], [[pnl_metodo_bisezione|Bisezione]], [[pnl_metodo_newton_1d|Newton 1D]].
