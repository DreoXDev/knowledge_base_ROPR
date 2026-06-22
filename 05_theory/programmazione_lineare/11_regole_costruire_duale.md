---
type: theory-note
topic: programmazione-lineare
status: draft
sources:
  - raw_assets/Programmazione Lineare/lec_w4_completa.pdf
reliability: official
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

#ropr #programmazione-lineare #teoria #dualita #regole-duale
