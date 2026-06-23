# Flashcards: KKT ed Enumerazione dei Vincoli Attivi

- **Q**: In un problema di minimizzazione con vincoli $g_i(x) \le 0$, quale segno devono soddisfare i moltiplicatori KKT $\mu_i$?
  **A**: Devono essere non negativi: $\mu_i \ge 0$.

- **Q**: Cosa implica la condizione di complementarità degli scarti $\mu_i g_i(x) = 0$ se il vincolo $i$ è inattivo ($g_i(x) < 0$)?
  **A**: Implica che il moltiplicatore associato è nullo: $\mu_i = 0$.

- **Q**: Cosa significa che un vincolo di disuguaglianza $g_i(x) \le 0$ è attivo in un punto candidato $x^*$?
  **A**: Significa che il vincolo è soddisfatto all'uguaglianza: $g_i(x^*) = 0$.

- **Q**: Con $m$ vincoli di disuguaglianza, quante combinazioni di vincoli attivi/inattivi possono esistere al massimo?
  **A**: Fino a $2^m$ combinazioni possibili.

- **Q**: Per quali tre motivi un punto candidato ricavato dall'analisi KKT per casi viene scartato?
  **A**: 
  1. Violazione dell'ammissibilità primale ($g_i(x^*) > 0$ per un vincolo inattivo).
  2. Violazione dell'ammissibilità duale ($\mu_i < 0$ per un vincolo attivo in un problema di minimo).
  3. Incompatibilità algebrica delle equazioni dei vincoli attivi (sistema impossibile).

- **Q**: Nel problema $\min f(x, y) = 4(x-1)^2 + (y-2)^2$ s.t. $x+y \le 2, \ x \ge -1, \ y \ge -1$, qual è l'unico candidato KKT ammissibile e dove si trova?
  **A**: Il punto $(0.8, 1.2)$, situato sulla retta del vincolo attivo $x+y = 2$, con $\mu_1 = 1.6 > 0$ e valore ottimo $f = 0.8$.
