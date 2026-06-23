# Flashcard — Programmazione Lineare Intera (Logica e Rappresentazione)

## Condizioni Logiche e Variabili Binarie

Q: Come si modella la condizione di contingenza in cui la decisione $j_2$ (magazzino) dipende dalla decisione $j_1$ (fabbrica)?
A: Tramite il vincolo $x_{j_2} \le x_{j_1}$. Se $x_{j_1} = 0 \implies x_{j_2} = 0$. Se $x_{j_1} = 1 \implies x_{j_2} \in \{0, 1\}$.

Q: Come si modella il vincolo disgiuntivo "either-or" tra due vincoli $f_1(x) \le d_1$ e $f_2(x) \le d_2$?
A: Introducendo una variabile binaria $y \in \{0, 1\}$ e un Big-M positivo:
$f_1(x) \le d_1 + M y$
$f_2(x) \le d_2 + M(1-y)$

Q: Come si modellano $N$ vincoli $f_i(x) \le d_i$ in cui almeno $K$ devono essere soddisfatti?
A: Introducendo $N$ variabili binarie $y_i \in \{0, 1\}$ e scrivendo:
$f_i(x) \le d_i + M y_i \quad \forall i=1, \dots, N$
$\sum_{i=1}^N y_i = N - K$

Q: Come si modella una funzione $f(x)$ che può assumere solo un insieme di $N$ valori discreti $\{d_1, d_2, \dots, d_N\}$?
A: Introducendo $N$ variabili binarie $y_i \in \{0, 1\}$ tali che:
$f(x) = \sum_{i=1}^N d_i y_i$
$\sum_{i=1}^N y_i = 1$

Q: Come si modella il costo di un'attività $x \ge 0$ avente un costo fisso $k > 0$ ed un costo variabile $c$ unitario?
A: Introducendo una variabile binaria $y \in \{0, 1\}$:
$\min \quad k y + c x$
$\text{s.t.} \quad x \le M y$

---

## Rappresentazione Binaria di Variabili Intere

Q: Come si rappresenta una variabile intera limitata $x \in [0, u]$ mediante variabili binarie?
A: Calcolando $K$ tale che $2^K \le u < 2^{K+1}$, ponendo $x = \sum_{k=0}^K 2^k y_k = y_0 + 2y_1 + \dots + 2^K y_K$ con $y_k \in \{0, 1\}$ e aggiungendo il vincolo $\sum_{k=0}^K 2^k y_k \le u$ (se $u \ne 2^{K+1}-1$).

Q: Dati $x_1 \le 5$, qual è la sua espansione binaria esatta?
A: Poiché $2^2 \le 5 < 2^3$, si espande come $x_1 = y_0 + 2y_1 + 4y_2$ con il vincolo $y_0 + 2y_1 + 4y_2 \le 5$ e $y_0, y_1, y_2 \in \{0, 1\}$.

---

## Difficoltà di Risoluzione e Arrotondamento

Q: Perché non è possibile risolvere problemi PLI restringendo il simplesso a valori interi?
A: Il metodo del simplesso richiede variabili continue per scorrere lungo le frontiere della regione ammissibile e garantire vertici ammissibili. Rimuovendo i punti frazionari si perde la convessità e la continuità dello spazio delle soluzioni.

Q: Perché l'arrotondamento all'intero più vicino della soluzione di un rilassamento lineare può fallire?
A: Perché la soluzione arrotondata può essere:
1. Non ammissibile (viola uno o più vincoli).
2. Altamente sub-ottima rispetto all'ottimo intero effettivo.

Q: Fornisci un esempio in cui l'arrotondamento all'intero più vicino produce un punto non ammissibile.
A: $\max \quad z = x_2$ con $-x_1 + x_2 \le 0.5$ e $2x_1 + x_2 \le 3.5$.
L'ottimo rilassato è $(1, 1.5)$. Arrotondando per eccesso $x_2 \to 2$ si ottiene $(1, 2)$, che viola il primo vincolo: $-1 + 2 = 1 > 0.5$.
