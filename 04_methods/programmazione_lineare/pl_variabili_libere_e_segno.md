---
type: method-card
topic: programmazione-lineare
status: draft
sources:
  - raw_assets/Programmazione Lineare/lezione 3 completa.pdf
reliability: official
---

# Method Card — Gestione delle Variabili Libere e Vincoli di Segno

Nel simplesso standard, tutte le variabili decisionali devono essere non negative ($x_j \ge 0$). Se il problema reale presenta variabili con limitazioni diverse, occorre effettuare una trasformazione algebrica prima della risoluzione.

## 1. Variabile Libera (Senza Vincolo di Segno)

Se una variabile $x$ può assumere sia valori positivi, sia negativi, sia nulli ($x \in \mathbb{R}$):

### Procedura
Sostituire ogni occorrenza di $x$ nel modello con la differenza di due nuove variabili non negative:

$$
x = x^+ - x^- \qquad \text{con } x^+, x^- \ge 0
$$

- $x^+$ rappresenta la parte positiva: $x^+ = \max(0, x)$
- $x^-$ rappresenta la parte negativa: $x^- = \max(0, -x)$

### Impatto sul Modello
- Nella funzione obiettivo: $c \cdot x \implies c \cdot x^+ - c \cdot x^-$
- In ogni vincolo $i$: $a_{i} x \implies a_{i} x^+ - a_{i} x^-$
- Si aggiungono entrambe le variabili $x^+, x^- \ge 0$ al dominio.

---

## 2. Variabile Non Positiva ($x \le 0$)

Se una variabile $x$ è vincolata ad essere minore o uguale a zero:

### Procedura
Sostituire la variabile con una nuova variabile non negativa definita come l'opposto di $x$:

$$
x' = -x \implies x = -x' \qquad \text{con } x' \ge 0
$$

### Impatto sul Modello
- Nella funzione obiettivo: $c \cdot x \implies -c \cdot x'$
- In ogni vincolo $i$: $a_{i} x \implies -a_{i} x'$
- Si aggiunge la variabile $x' \ge 0$ al dominio.

---

## Esempio d'Esame: Variabile Libera e Variabile Non Positiva

Si consideri il problema:

$$
\max Z = 3x_1 + 2x_2 - 2x_3
$$

soggetto a:
- $x_1$ libera
- $x_2 \ge 0$
- $x_3 \le 0$

### Trasformazione
1. Sostituire $x_1$ con $x_1^+ - x_1^-$
2. Sostituire $x_3$ con $-x_3'$

Il modello trasformato in forma standard equivalente diventa:

$$
\max Z = 3x_1^+ - 3x_1^- + 2x_2 + 2x_3'
$$

con variabili $x_1^+, x_1^-, x_2, x_3' \ge 0$.
ogni vincolo del tipo $a_1x_1 + a_2x_2 + a_3x_3 \le b$ diventa:

$$
a_1x_1^+ - a_1x_1^- + a_2x_2 - a_3x_3' \le b
$$
