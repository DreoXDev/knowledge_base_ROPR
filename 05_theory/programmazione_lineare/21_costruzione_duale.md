---
materia: ROPR
area: Programmazione Lineare
tipo: teoria
fonte: Ricerca Operativa - Teoria della Dualità.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - simplesso
  - dualita
  - costruzione-duale
  - wyndor-glass
---

# Costruzione del duale standard

La costruzione sistematica del problema duale per un problema primale in forma standard segue regole algebriche precise basate sulle corrispondenze tra vettori e matrici.

## Regole Operative per la Costruzione

Dato un problema primale di massimizzazione in forma standard:

1. **Scelta dell'obiettivo**: Il problema duale sarà di minimizzazione ($\min W$).
2. **Variabili duali**: Associare una variabile duale $y_i$ a ciascuno dei $m$ vincoli funzionali del primale. Se il vincolo primale è $\le$ (canonico per MAX), la variabile corrispondente sarà $y_i \ge 0$.
3. **Coefficienti F.O. duale**: I coefficienti della funzione obiettivo duale $W$ sono pari ai termini noti (RHS) dei vincoli primali $b_1, \dots, b_m$:
   $$
   \min W = b_1y_1 + b_2y_2 + \dots + b_my_m
   $$
4. **Vincoli duali**: Associare un vincolo duale a ciascuna delle $n$ variabili primali. Ciascun vincolo duale $j$-esimo corrisponde alla colonna $j$-esima della matrice dei coefficienti primali $\mathbf{A}$:
   $$
   a_{1j}y_1 + a_{2j}y_2 + \dots + a_{mj}y_m \ge c_j
   $$
   dove il verso $\ge$ è determinato dal fatto che la variabile primale è $x_j \ge 0$ (canonica).
5. **Termini noti duali**: I termini noti dei vincoli duali (RHS) sono i coefficienti della funzione obiettivo primale $c_1, \dots, c_n$.

---

## Esempio Applicativo: Wyndor Glass Co.

### Modello Primale (MAX)

$$
\max Z = 3x_1 + 5x_2
$$

soggetto a:

$$
\begin{aligned}
(y_1) \quad x_1 &\le 4 \\
(y_2) \quad 2x_2 &\le 12 \\
(y_3) \quad 3x_1 + 2x_2 &\le 18
\end{aligned}
$$

con $x_1, x_2 \ge 0$.

### Costruzione del Modello Duale (MIN)

1. Associare la variabile duale $y_1$ al vincolo (1), $y_2$ al vincolo (2) e $y_3$ al vincolo (3). Poiché tutti i vincoli primali sono $\le$, le variabili duali sono non negative: $y_1, y_2, y_3 \ge 0$.
2. I coefficienti della funzione obiettivo duale $W$ sono i RHS del primale $(4, 12, 18)$:
   $$
   \min W = 4y_1 + 12y_2 + 18y_3
   $$
3. I vincoli duali corrispondono alle colonne della matrice dei coefficienti primali:
   - Per $x_1$ (colonna $\begin{pmatrix} 1 \\ 0 \\ 3 \end{pmatrix}$, coeff. in F.O. = 3):
     $$
     y_1 + 3y_3 \ge 3
     $$
   - Per $x_2$ (colonna $\begin{pmatrix} 0 \\ 2 \\ 2 \end{pmatrix}$, coeff. in F.O. = 5):
     $$
     2y_2 + 2y_3 \ge 5
     $$
4. Il dominio duale è $y_1, y_2, y_3 \ge 0$.

### Modello Duale Risultante

$$
\min W = 4y_1 + 12y_2 + 18y_3
$$

soggetto a:

$$
y_1 + 3y_3 \ge 3
$$

$$
2y_2 + 2y_3 \ge 5
$$

$$
y_1, y_2, y_3 \ge 0
$$
