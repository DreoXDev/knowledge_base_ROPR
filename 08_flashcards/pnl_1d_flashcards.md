# Flashcards: Programmazione Non Lineare 1D

- **Q**: Qual è la condizione necessaria per un ottimo interno in una variabile?
  **A**: $f'(x^*) = 0$ (punto stazionario).

- **Q**: In un punto stazionario $x^*$, quali sono le condizioni sufficienti del secondo ordine per un massimo o minimo locale?
  **A**: Se $f''(x^*) < 0$, è un massimo locale. Se $f''(x^*) > 0$, è un minimo locale.

- **Q**: Quando un punto stazionario di massimo locale $x^*$ è anche massimo globale?
  **A**: Quando la funzione $f(x)$ è concava su tutto il suo dominio ($f''(x) \le 0 \ \forall x$).

- **Q**: Quali sono le ipotesi del metodo di bisezione 1D?
  **A**: La funzione $f(x)$ deve essere continua sull'intervallo chiuso $[\underline{x}, \bar{x}]$, derivabile sull'aperto $(\underline{x}, \bar{x})$, concava (per massimo) o convessa (per minimo), e le derivate prima agli estremi devono avere segno opposto ($f'(\underline{x}) \cdot f'(\bar{x}) < 0$).

- **Q**: Qual è la formula del metodo di Newton in una variabile (1D)?
  **A**:
  $$x_{k+1} = x_k - \frac{f'(x_k)}{f''(x_k)}$$

- **Q**: Qual è il criterio di arresto tipico della bisezione 1D?
  **A**: L'ampiezza dell'intervallo di incertezza è minore o uguale a due volte la tolleranza: $\bar{x} - \underline{x} \le 2\epsilon$.

- **Q**: Qual è la velocità di convergenza del metodo di bisezione 1D?
  **A**: Convergenza lineare con fattore di riduzione costante pari a $0.5$ (lento ma robusto).

- **Q**: Qual è la velocità di convergenza del metodo di Newton 1D?
  **A**: Convergenza quadratica locale (molto rapido, raddoppia le cifre decimali corrette ad ogni iterazione se vicino alla soluzione).

- **Q**: Qual è lo svantaggio o rischio principale del metodo di Newton 1D rispetto alla bisezione?
  **A**: Può divergere o oscillare se il punto di partenza $x_0$ è lontano dall'ottimo, e richiede il calcolo della derivata seconda (fallisce se $f''(x_k) = 0$).
