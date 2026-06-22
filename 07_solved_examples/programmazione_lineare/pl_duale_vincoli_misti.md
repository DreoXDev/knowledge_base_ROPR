---
topic: Programmazione Lineare
type: esempio_svolto
source: lec_w4_completa.pdf
status: verificato
---

# Esempio Svolto — Costruzione del Duale con Vincoli Misti

## Traccia Sintetica
Scrivere il problema duale del seguente problema primale con vincoli misti ($\le, \ge, =$):

$$
\max Z = 3x + 5y
$$

soggetto a:

$$
x - y \le 1 \qquad (\text{Vincolo } 1)
$$

$$
2x - y \ge 4 \qquad (\text{Vincolo } 2)
$$

$$
-2x + y = 1 \qquad (\text{Vincolo } 3)
$$

$$
x, y \ge 0
$$

## Risoluzione Passo-Passo

1. **Associazione delle variabili duali ai vincoli**:
   - Al Vincolo 1 ($\le$ in MAX, canonico) associamo $u_1 \ge 0$.
   - Al Vincolo 2 ($\ge$ in MAX, anticanonico) associamo $u_2 \le 0$.
   - Al Vincolo 3 ($=$ in MAX) associamo $u_3$ libera (senza vincolo di segno).

2. **Funzione Obiettivo del Duale (MIN)**:
   I coefficienti sono i termini noti (RHS) del primale:

$$
\min Z' = u_1 + 4u_2 + u_3
$$

3. **Vincoli del Duale**:
   Traspugliamo la matrice del primale e confrontiamo con i coefficienti dell'obiettivo primale (3 per $x$, 5 per $y$). Poiché le variabili primali $x,y$ sono non negative ($\ge 0$, canoniche), i vincoli duali saranno di tipo $\ge$ (canonici in MIN):
   - Per la colonna di $x$ (coefficienti: $1$ nel vincolo 1, $2$ nel vincolo 2, $-2$ nel vincolo 3):
     $$
     u_1 + 2u_2 - 2u_3 \ge 3
     $$
   - Per la colonna di $y$ (coefficienti: $-1$ nel vincolo 1, $-1$ nel vincolo 2, $1$ nel vincolo 3):
     $$
     -u_1 - u_2 + u_3 \ge 5
     $$

## Modello Duale Completo

$$
\min Z' = u_1 + 4u_2 + u_3
$$

soggetto a:

$$
u_1 + 2u_2 - 2u_3 \ge 3
$$

$$
-u_1 - u_2 + u_3 \ge 5
$$

$$
u_1 \ge 0, \quad u_2 \le 0, \quad u_3 \text{ libera}
$$

## Risposta da Esame
Il problema duale è:
$\min Z' = u_1 + 4u_2 + u_3$
soggetto a:
- $u_1 + 2u_2 - 2u_3 \ge 3$
- $-u_1 - u_2 + u_3 \ge 5$
- $u_1 \ge 0$, $u_2 \le 0$, $u_3$ libera.
