# MC - Logica Vincoli Binari (Either-Or, K su N)

## Quando Usarla
Per modellare vincoli logici disgiuntivi in cui solo un sottoinsieme di vincoli deve essere contemporaneamente soddisfatto (es. "either-or", o almeno $K$ vincoli su $N$ totali).

## Variabili Tipiche
*   $x \in \mathbb{R}^n$: Variabili decisionali continue o intere.
*   $y_i \in \{0, 1\}$: Variabili binarie di disattivazione dei vincoli.

## Modello Template

### 1. Condizione "Either-Or" (Almeno uno tra due vincoli soddisfatto)
Dati due vincoli $f_1(x) \le d_1$ e $f_2(x) \le d_2$:
$$
f_1(x) \le d_1 + M y
$$
$$
f_2(x) \le d_2 + M(1-y)
$$
$$
y \in \{0, 1\}
$$
*   Se $y = 0$, il primo vincolo è attivo ($f_1(x) \le d_1$), il secondo è disattivato.
*   Se $y = 1$, il secondo vincolo è attivo ($f_2(x) \le d_2$), il primo è disattivato.

### 2. Condizione "$K$ su $N$" (Almeno $K$ vincoli attivi)
Dati $N$ vincoli $f_i(x) \le d_i$ per $i = 1, \dots, N$:
$$
f_i(x) \le d_i + M y_i \quad \forall i = 1, \dots, N
$$
$$
\sum_{i=1}^N y_i = N - K
$$
$$
y_i \in \{0, 1\} \quad \forall i = 1, \dots, N
$$
*   Si disattivano esattamente $N-K$ vincoli ponendo $y_i = 1$. Rimangono attivi almeno $K$ vincoli.

## Procedura da Esame
1.  Identificare i vincoli alternativi o disgiuntivi del problema.
2.  Associare a ciascun vincolo alternativo una variabile binaria $y_i$ ($1$ = disattivato, $0$ = attivo).
3.  Determinare un valore di $M$ (Big-M) valido e abbastanza grande per disattivare ciascun vincolo.
4.  Scrivere i vincoli con il termine additivo $+ M y_i$ (o $+ M(1-y_i)$) e aggiungere il vincolo di cardinalità sulla somma delle variabili $y_i$.

## Mini Esempio
Dati due vincoli di capacità alternativi $3x_1 + 2x_2 \le 18$ e $x_1 + 4x_2 \le 16$, si vuole soddisfarne almeno uno:
$$
3x_1 + 2x_2 \le 18 + M y
$$
$$
x_1 + 4x_2 \le 16 + M(1 - y)
$$
$$
y \in \{0, 1\}
$$

## Errori Comuni
*   Dimenticare di definire $y$ come binaria.
*   Utilizzare vincoli di uguaglianza con Big-M (la disattivazione con $+ M y$ funziona solo per vincoli di tipo $\le$. Se il vincolo originale è $\ge$, usare $- M y$. Se è di uguaglianza, occorre spezzarlo in due disuguaglianze e disattivarle opportunamente).

## Fonti
*   `Programmazione lineare intera completo.pdf`, Pagine 14-17
