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
  - regole-duale
  - sensible-odd-bizarre
---

# Regole per Costruire il Problema Duale

Il passaggio dal problema primale al problema duale segue regole algebriche precise che dipendono dal verso dell'ottimizzazione e dal tipo di vincoli e variabili presenti.

## Corrispondenze Generali Primale-Duale

| Problema Primale | Problema Duale |
|---|---|
| Massimizzazione ($\max$) | Minimizzazione ($\min$) |
| Minimizzazione ($\min$) | Massimizzazione ($\max$) |
| $m$ Vincoli funzionali | $m$ Variabili duali |
| $n$ Variabili primali | $n$ Vincoli duali |
| Termini noti (RHS) $b_i$ | Coefficienti di costo della funzione obiettivo |
| Coefficienti obiettivo $c_j$ | Termini noti (RHS) dei vincoli duali |
| Matrice dei coefficienti $A$ | Matrice trasposta $A^T$ |

---

## Tabella di Conversione: Primale MAX $\implies$ Duale MIN

Assumendo che il primale sia un problema di massimizzazione:

| Vincolo Primale ($i$-esimo) | Variabile Duale ($y_i$) |
|---|---|
| Vincolo di tipo $\le$ (Canonico) | Variabile $y_i \ge 0$ (Canonica) |
| Vincolo di tipo $\ge$ (Anticanonico) | Variabile $y_i \le 0$ (Anticanonica) |
| Vincolo di tipo $=$ (Uguaglianza) | Variabile $y_i$ Libera |

| Variabile Primale ($x_j$) | Vincolo Duale ($j$-esimo) |
|---|---|
| Variabile $x_j \ge 0$ (Canonica) | Vincolo di tipo $\ge$ (Canonico in MIN) |
| Variabile $x_j \le 0$ (Anticanonica) | Vincolo di tipo $\le$ (Anticanonico in MIN) |
| Variabile $x_j$ Libera | Vincolo di tipo $=$ (Uguaglianza) |

---

## Tabella di Conversione: Primale MIN $\implies$ Duale MAX

Assumendo che il primale sia un problema di minimizzazione:

| Vincolo Primale ($i$-esimo) | Variabile Duale ($w_i$) |
|---|---|
| Vincolo di tipo $\ge$ (Canonico) | Variabile $w_i \ge 0$ (Canonica) |
| Vincolo di tipo $\le$ (Anticanonico) | Variabile $w_i \le 0$ (Anticanonica) |
| Vincolo di tipo $=$ (Uguaglianza) | Variabile $w_i$ Libera |

| Variabile Primale ($x_j$) | Vincolo Duale ($j$-esimo) |
|---|---|
| Variabile $x_j \ge 0$ (Canonica) | Vincolo di tipo $\le$ (Canonico in MAX) |
| Variabile $x_j \le 0$ (Anticanonica) | Vincolo di tipo $\ge$ (Anticanonico in MAX) |
| Variabile $x_j$ Libera | Vincolo di tipo $=$ (Uguaglianza) |

---

## Definizioni e Convenzioni

- **Canonico (d'accordo con la norma)**:
  - Le variabili non negative ($x \ge 0$) sono canoniche.
  - In $\max$, i vincoli canonici sono $\le$ (le risorse sono limitate superiormente).
  - In $\min$, i vincoli canonici sono $\ge$ (i requisiti minimi devono essere soddisfatti).
- **Anticanonico (discorde)**:
  - Le variabili non positive ($x \le 0$) sono anticanoniche.
  - I vincoli orientati nel verso opposto a quello canonico (es. $\ge$ in $\max$ o $\le$ in $\min$) sono anticanonici.
- **Libero (o di uguaglianza)**:
  - Una variabile libera primale genera un vincolo duale di uguaglianza ($=$).
  - Un vincolo primale di uguaglianza ($=$) genera una variabile duale libera (senza vincolo di segno).

---

## Il Metodo Sensible / Odd / Bizarre (SOB)

Il metodo **sensible / odd / bizarre (SOB)** è un sistema mnemonico per classificare vincoli e variabili nel passaggio da primale a duale. Le definizioni delle etichette sono:
- **Sensible** (Canonico/Sensato): rispetta la direzione naturale per il verso di ottimizzazione.
- **Odd** (Singolare/Uguaglianza): rappresenta situazioni di vincolo di uguaglianza o variabili senza vincolo di segno.
- **Bizarre** (Anticanonico/Inusuale): orientato in senso opposto alla direzione naturale.

### Relazioni SOB: Primale MAX $\implies$ Duale MIN

| Elemento del Primale (MAX) | Tipo / Segno | Etichetta SOB | Elemento del Duale (MIN) | Segno / Tipo |
|---|---|---|---|---|
| **Vincolo $i$-esimo** | $\le$ | Sensible | **Variabile $y_i$** | $y_i \ge 0$ |
| | $=$ | Odd | | $y_i$ libera |
| | $\ge$ | Bizarre | | $y_i \le 0$ |
| **Variabile $x_j$** | $x_j \ge 0$ | Sensible | **Vincolo $j$-esimo** | $\ge$ |
| | $x_j$ libera | Odd | | $=$ |
| | $x_j \le 0$ | Bizarre | | $\le$ |

### Relazioni SOB: Primale MIN $\implies$ Duale MAX

| Elemento del Primale (MIN) | Tipo / Segno | Etichetta SOB | Elemento del Duale (MAX) | Segno / Tipo |
|---|---|---|---|---|
| **Vincolo $i$-esimo** | $\ge$ | Sensible | **Variabile $y_i$** | $y_i \ge 0$ |
| | $=$ | Odd | | $y_i$ libera |
| | $\le$ | Bizarre | | $y_i \le 0$ |
| **Variabile $x_j$** | $x_j \ge 0$ | Sensible | **Vincolo $j$-esimo** | $\le$ |
| | $x_j$ libera | Odd | | $=$ |
| | $x_j \le 0$ | Bizarre | | $\ge$ |

### Esempio Operativo SOB
Consideriamo il problema primale (MAX):
$$
\max Z = 2x_1 + 3x_2
$$
soggetto a:
$$
\begin{aligned}
x_1 + x_2 &\ge 4 \quad \text{(Bizarre: genera } y_1 \le 0\text{)} \\
2x_1 - x_2 &= 5 \quad \text{(Odd: genera } y_2 \text{ libera)}
\end{aligned}
$$
con:
- $x_1 \ge 0$ (Sensible: genera vincolo $\ge$ in MIN)
- $x_2$ libera (Odd: genera vincolo $=$ in MIN)

Il problema duale risultante (MIN) è:
$$
\min W = 4y_1 + 5y_2
$$
soggetto a:
$$
\begin{aligned}
y_1 + 2y_2 &\ge 2 \\
y_1 - y_2 &= 3
\end{aligned}
$$
con $y_1 \le 0$ e $y_2$ libera.

