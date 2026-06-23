# MC - Vincoli Logici e Big-M

## Quando Usarla
Per attivare o disattivare vincoli sulle variabili continue/intere $x_i$ in base al valore di variabili binarie $y_i \in \{0, 1\}$.

## Variabili Tipiche
*   $x_i \ge 0$: Variabile continua o intera di livello/quantità.
*   $y_i \in \{0, 1\}$: Variabile binaria di attivazione.

## Modello Template
Attivazione con limite superiore $U_i$ (capacità massima):
$$
x_i \le U_i y_i
$$
Attivazione con limite inferiore $L_i$ (produzione minima):
$$
x_i \ge L_i y_i
$$
Linearizzazione Big-M generica se $U_i$ non è noto:
$$
x_i \le M y_i
$$
dove $M$ è una costante reale positiva sufficientemente grande.

## Procedura da Esame
1.  Verificare se la produzione/attività $x_i$ ha costi fissi o soglie minime di attivazione.
2.  Associare a tale attività una variabile binaria $y_i$.
3.  Formulare il limite superiore linearizzato usando la capacità massima o, se assente, un valore Big-M calcolato (es. capacità totale disponibile di risorsa divisa per il coefficiente di consumo del prodotto).
4.  Formulare il limite inferiore linearizzato se presente.

## Mini Esempio
La produzione $x$ consuma materia prima e non può superare la disponibilità totale $D = 100$. Se prodotta, si paga un setup fisso.
Il vincolo è:
$$
x \le 100 y
$$
$$
y \in \{0, 1\}
$$

## Errori Comuni
*   Scegliere un valore di $M$ casuale o eccessivamente grande (es. $10^9$) che crea instabilità nei solver numerici.
*   Dimenticare di moltiplicare il bound inferiore per la variabile binaria, costringendo la variabile a essere positiva anche quando $y=0$.

## Fonti
*   `modelli_PLI.pdf`, Sezione 2.4
