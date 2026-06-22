---
topic: Programmazione Lineare
type: esempio_svolto
source: lezione 3 completa.pdf
status: verificato
---

# Esempio Svolto — Simplesso Esempio Base ($40x + 50y$)

## Traccia Sintetica
Risolvere il seguente problema di PL tramite il metodo del simplesso tabellare:

$$
\max Z = 40x + 50y
$$

soggetto a:

$$
x + 2y \le 40
$$

$$
4x + 3y \le 120
$$

$$
x, y \ge 0
$$

## Risoluzione

### 1. Forma Aumentata
Aggiungendo le slack $s_1$ e $s_2$:

$$
x + 2y + s_1 = 40
$$

$$
4x + 3y + s_2 = 120
$$

Riga obiettivo (riga 0):

$$
Z - 40x - 50y = 0
$$

### 2. Tableau Iniziale (Iterazione 0)

| Base | $Z$ | $x$ | $y$ | $s_1$ | $s_2$ | RHS |
|---|---|---|---|---|---|---|
| **$Z$** | 1 | -40 | -50 | 0 | 0 | 0 |
| **$s_1$**| 0 | 1 | **2** | 1 | 0 | 40 |
| **$s_2$**| 0 | 4 | 3 | 0 | 1 | 120 |

- La soluzione di base è $s_1 = 40$, $s_2 = 120$, con $Z = 0$.
- La variabile entrante è **$y$** (coefficiente $-50$ in riga 0).
- Rapporti: riga $s_1 = 40/2 = 20$; riga $s_2 = 120/3 = 40$. La variabile uscente è **$s_1$** (rapporto minimo = 20).
- Elemento pivot = 2.

### 3. Tableau Iterazione 1 (Pivot su riga 1, colonna $y$)

Dividendo la riga $s_1$ per 2 e azzerando la colonna di $y$ nelle altre righe:

| Base | $Z$ | $x$ | $y$ | $s_1$ | $s_2$ | RHS |
|---|---|---|---|---|---|---|
| **$Z$** | 1 | -15 | 0 | 25 | 0 | 1000 |
| **$y$** | 0 | 0.5 | 1 | 0.5 | 0 | 20 |
| **$s_2$**| 0 | **2.5** | 0 | -1.5 | 1 | 60 |

- La soluzione di base è $y = 20$, $s_2 = 60$, con $Z = 1000$.
- La variabile entrante è **$x$** (coefficiente $-15$ in riga 0).
- Rapporti: riga $y = 20/0.5 = 40$; riga $s_2 = 60/2.5 = 24$. La variabile uscente è **$s_2$** (rapporto minimo = 24).
- Elemento pivot = 2.5.

### 4. Tableau Iterazione 2 (Pivot su riga 2, colonna $x$)

Dividendo la riga $s_2$ per 2.5 (ovvero moltiplicando per 0.4) e azzerando la colonna di $x$ nelle altre righe:

| Base | $Z$ | $x$ | $y$ | $s_1$ | $s_2$ | RHS |
|---|---|---|---|---|---|---|
| **$Z$** | 1 | 0 | 0 | 16 | 6 | 1360 |
| **$y$** | 0 | 0 | 1 | 0.8 | -0.2 | 8 |
| **$x$** | 0 | 1 | 0 | -0.6 | 0.4 | 24 |

- Tutti i coefficienti della riga 0 sono $\ge 0$. La soluzione è ottima.

## Risultato Finale
La soluzione ottima è:

$$
x^* = 24, \quad y^* = 8 \qquad \text{con } Z^* = 1360
$$

Le variabili di slack valgono $s_1^* = 0, s_2^* = 0$.
