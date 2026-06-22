---
materia: ROPR
area: Programmazione Lineare
tipo: metodo
fonte: Ricerca Operativa - Teoria della Dualità.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - dualita
  - costruzione-duale
  - standard
  - method-card
---

# METHOD CARD — Costruzione del Duale Standard

## Quando usarla

Usare questa card per ricavare in modo sistematico il problema duale a partire da un problema primale espresso in forma standard di massimizzazione (o minimizzazione).

## Procedura Operativa Passo-Passo

### 1. Verifica della Forma Standard del Primale (MAX)
Assicurarsi che il problema primale sia espresso come:
$$
\max Z = \sum_{j=1}^{n} c_j x_j
$$
soggetto a vincoli di tipo minore o uguale e non-negatività delle variabili:
$$
\sum_{j=1}^{n} a_{ij}x_j \le b_i \qquad \forall i=1,\dots,m
$$
$$
x_j \ge 0 \qquad \forall j=1,\dots,n
$$

Se il primale è in questa forma, procedere con i punti successivi.

### 2. Definizione del Problema Duale (MIN)
Il problema duale sarà di minimizzazione ($\min W$).

### 3. Definizione delle Variabili Duali
Associare una variabile duale $y_i$ a ogni vincolo funzionale del primale.
- Se ci sono $m$ vincoli funzionali primali, ci saranno $m$ variabili duali: $y_1, y_2, \dots, y_m$.
- Poiché tutti i vincoli primali sono di tipo $\le$, le variabili duali ereditano il segno non negativo:
  $$
  y_i \ge 0 \qquad \forall i=1,\dots,m
  $$

### 4. Definizione della Funzione Obiettivo Duale
I coefficienti della funzione obiettivo del duale sono pari ai termini noti (RHS) dei vincoli del primale ($b_i$):
$$
\min W = b_1y_1 + b_2y_2 + \dots + b_my_m = \sum_{i=1}^{m} b_i y_i
$$

### 5. Costruzione dei Vincoli Duali
Costruire un vincolo duale per ciascuna delle $n$ variabili primali:
- Ciascuna colonna $j$-esima della matrice dei coefficienti primali $\mathbf{A}$ corrisponde al vincolo duale $j$-esimo.
- I termini noti (RHS) dei vincoli duali sono i coefficienti della funzione obiettivo primale ($c_j$).
- Il verso del vincolo duale è $\ge$ (canonico per problemi di minimo):
  $$
  a_{1j}y_1 + a_{2j}y_2 + \dots + a_{mj}y_m \ge c_j \qquad \forall j=1,\dots,n
  $$

---

## Esempio Rapido: Wyndor Glass Co.

**Primale (MAX):**
$$
\max Z = 3x_1 + 5x_2
$$
soggetto a:
$$
\begin{aligned}
x_1 &\le 4 \\
2x_2 &\le 12 \\
3x_1 + 2x_2 &\le 18 \\
x_1, x_2 &\ge 0
\end{aligned}
$$

**Duale risultante (MIN):**
$$
\min W = 4y_1 + 12y_2 + 18y_3
$$
soggetto a:
$$
\begin{aligned}
y_1 + 3y_3 &\ge 3 \\
2y_2 + 2y_3 &\ge 5 \\
y_1, y_2, y_3 &\ge 0
\end{aligned}
$$
