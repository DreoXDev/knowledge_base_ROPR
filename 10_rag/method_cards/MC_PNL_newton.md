# Method Card: Metodo di Newton Unidimensionale e Multivariabile

- **Newton 1D (per $f'(x) = 0$)**:
  - Aggiornamento: $x_{k+1} = x_k - \frac{f'(x_k)}{f''(x_k)}$.
  - Convergenza quadratica vicino all'ottimo. Richiede $f''(x_k) \ne 0$.
- **Newton Multivariabile (per $\nabla f(x) = 0$)**:
  - Aggiornamento: $x_{k+1} = x_k + d_k$.
  - Direzione $d_k$ ricavata risolvendo il sistema lineare: $H_f(x_k) d_k = -\nabla f(x_k)$.
  - Passo fisso $\alpha_k = 1$.
- **Ottimalità**: Per funzioni quadratiche convergenza in una sola iterazione da qualsiasi punto di partenza.
- **Esempio di Calcolo**: Vedi [[pnl_metodo_newton_multivariabile|Metodo Newton Multivariabile]] o [[pnl_esercizi_non_vincolati|Esempi Svolti Newton]].
