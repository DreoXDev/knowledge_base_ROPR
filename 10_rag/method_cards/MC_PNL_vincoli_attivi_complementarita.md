# Method Card: Vincoli Attivi e complementarità

## Quando usarla
Da usare per analizzare lo stato dei vincoli di disuguaglianza (attivi o inattivi) in problemi di ottimizzazione e applicare correttamente la complementarità degli scarti durante la ricerca dei punti stazionari di KKT.

## Riconoscimento dello stato del vincolo
Dato un punto candidato $x^*$ ed un vincolo di disuguaglianza $h_j(x) \le 0$:
- **Vincolo Attivo**: $h_j(x^*) = 0$. Il punto giace sulla frontiera del vincolo. Il moltiplicatore associato $\mu_j^*$ può assumere valori diversi da zero.
- **Vincolo Inattivo**: $h_j(x^*) < 0$. Il punto giace all'interno della regione ammissibile rispetto al vincolo. Il moltiplicatore associato è rigorosamente nullo:
  $$\mu_j^* = 0$$

## Condizione di complementarità degli scarti
Per ogni vincolo $j$ deve valere:
$$\mu_j^* \cdot h_j(x^*) = 0$$

## Procedura operativa per enumerare i casi (2^p casi)
Quando si hanno $p$ vincoli di disuguaglianza, impostare l'analisi combinatoria dividendo il problema in $2^p$ casi:
1.  **Tutti i vincoli inattivi**: Porre $\mu_1 = \mu_2 = \dots = \mu_p = 0$. Risolvere $\nabla f(x) = 0$ (ricerca di ottimi liberi interni). Verificare l'ammissibilità primale ($h_j(x) \le 0$ per tutti i $j$).
2.  **Un vincolo attivo alla volta**: Per ciascun vincolo $k$, porre $h_k(x) = 0$ e $\mu_j = 0$ per tutti i $j \neq k$. Risolvere il sistema. Verificare l'ammissibilità primale ($h_j(x) \le 0$) e duale (segno corretto per $\mu_k$).
3.  **Coppie di vincoli attivi**: Per ogni coppia di vincoli $(k, l)$, porre $h_k(x) = 0, h_l(x) = 0$ e $\mu_j = 0$ per gli altri. Risolvere il sistema e verificare sia l'ammissibilità primale che duale ($\mu_k$ e $\mu_l$ coerenti).
4.  **Ripetere** per combinazioni a tre o più vincoli attivi fino a coprire tutti i casi possibili.

## Errori frequenti
- **Considerare non attivi i vincoli con $h_j(x^*)=0$**: Questo è un errore terminologico grave; se il vincolo è soddisfatto con l'uguaglianza, è attivo.
- **Dimenticare l'ammissibilità primale**: Verificare solo il segno di $\mu_j$ e dimenticare di controllare se il punto soddisfa i vincoli inattivi.
- **LICQ non soddisfatto nei punti di intersezione**: Nei punti in cui si intersecano più vincoli attivi, verificare che i gradienti dei vincoli attivi siano linearmente indipendenti.

## Esempio minimo
Dati i vincoli $h_1(x, y) = x + y - 2 \le 0$ e $h_2(x, y) = -x \le 0$:
- Caso 1: $\mu_1 = 0, \mu_2 = 0$ (vincoli entrambi inattivi).
- Caso 2: $x + y - 2 = 0, \mu_2 = 0$ (solo $h_1$ attivo).
- Caso 3: $\mu_1 = 0, -x = 0 \implies x = 0$ (solo $h_2$ attivo).
- Caso 4: $x + y - 2 = 0$ e $-x = 0 \implies x = 0, y = 2$ (entrambi attivi).
