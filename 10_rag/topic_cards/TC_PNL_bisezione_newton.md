# Topic Card: Bisezione vs Newton 1D

- **Metodo di Bisezione**:
  - Algoritmo dicotomico per trovare gli zeri di $f'(x) = 0$.
  - Dimezza lo spazio ad ogni iterazione: $\bar{x}_{k+1} - \underline{x}_{k+1} = \frac{1}{2}(\bar{x}_k - \underline{x}_k)$.
  - **Vantaggi**: Estremamente robusto, converge sempre se le ipotesi sono verificate, richiede solo la derivata prima $f'(x)$.
  - **Svantaggi**: Lento (velocità di convergenza lineare, contrazione costante del 50%).
- **Metodo di Newton 1D**:
  - Algoritmo di approssimazione locale al secondo ordine (Taylor).
  - Formula di ricorrenza: $x_{k+1} = x_k - \frac{f'(x_k)}{f''(x_k)}$.
  - **Vantaggi**: Convergenza molto veloce (velocità quadratica, $e_{k+1} \approx C \cdot e_k^2$).
  - **Svantaggi**: Richiede la derivata seconda $f''(x)$ ed è instabile (può divergere o oscillare se il punto iniziale $x_0$ è lontano dall'ottimo).
- **Criteri di Arresto**:
  - Bisezione: Ampiezza intervallo $\bar{x} - \underline{x} \le 2\epsilon$.
  - Newton 1D: Avanzamento $|x_{k+1} - x_k| \le \epsilon$.
- **Errori Comuni**:
  - Calcolo del valore obiettivo $f(x_k)$ invece del segno di $f'(x_k)$ per aggiornare la bisezione.
  - Divisione per zero in Newton se $f''(x_k) = 0$.
  - Inversione delle regole di aggiornamento degli estremi tra problemi di massimo e di minimo.
- **Fonti**: [[pnl_confronto_bisezione_newton|Confronto Bisezione/Newton]], [[pnl_metodo_bisezione|Dettaglio Bisezione]], [[pnl_metodo_newton_1d|Dettaglio Newton 1D]].
