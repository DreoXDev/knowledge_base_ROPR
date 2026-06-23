# MC - Variabili Binarie

## Quando Usarla
Per modellare scelte del tipo sì/no, presenza/assenza o decisioni logiche mutuamente esclusive.

## Variabili Tipiche
*   $y_j \in \{0, 1\}$: Vale $1$ se si compie l'azione $j$, $0$ altrimenti.

## Modello Template
Per imporre che si scelga al più un'alternativa da un insieme $J$:
$$
\sum_{j \in J} y_j \le 1
$$
Per imporre che si scelga esattamente un'alternativa:
$$
\sum_{j \in J} y_j = 1
$$
Per imporre che la scelta $A$ possa essere fatta solo se è fatta la scelta $B$ ($A \implies B$):
$$
y_A \le y_B
$$

## Procedura da Esame
1.  Identificare gli elementi discreti da selezionare.
2.  Associare a ciascuno una variabile $y_j$.
3.  Scrivere i vincoli di configurazione/scelta mutuamente esclusiva sommando le variabili e limitando la somma.
4.  Dichiarare $y_j \in \{0, 1\}$.

## Mini Esempio
Si possono scegliere al massimo due progetti tra tre disponibili:
$$
y_1 + y_2 + y_3 \le 2
$$
$$
y_j \in \{0, 1\} \quad \forall j = 1, 2, 3
$$

## Errori Comuni
*   Dichiarare le variabili come reali comprese tra $0$ e $1$ ($0 \le y_j \le 1$) senza imporre l'integrità.

## Fonti
*   `modelli_PLI.pdf`, Sezione 2.4
