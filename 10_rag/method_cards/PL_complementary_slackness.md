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
  - complementary-slackness
  - scarti-complementari
  - method-card
---

# METHOD CARD — Complementary Slackness (Scarti Complementari)

## Quando usarla
Usare questa card per verificare l'ottimalità di una soluzione o per risolvere il sistema lineare che calcola le variabili duali associate a una soluzione primale nota.

## Equazioni Chiave

Per primale MAX standard e duale MIN standard:
1. **Complementarità Primal-Duale**:
   $$
   y_i \cdot (b_i - A_i x) = 0 \iff y_i \cdot s_i = 0 \qquad \forall i=1,\dots,m
   $$
   Se il vincolo primale $i$ è inattivo ($s_i > 0$), allora la variabile duale $y_i = 0$.
2. **Complementarità Dual-Primal**:
   $$
   x_j \cdot (A_j^T y - c_j) = 0 \iff x_j \cdot v_j = 0 \qquad \forall j=1,\dots,n
   $$
   Se la variabile primale $x_j > 0$, allora il vincolo duale $j$ deve essere attivo ($A_j^T y = c_j$).

## Procedura Operativa Sintetica

1. Calcola gli scarti primali $s_i$ sostituendo la soluzione primale $\mathbf{x}$.
2. Per ogni $s_i > 0$, poni $y_i = 0$.
3. Per ogni $x_j > 0$, imposta il vincolo duale all'uguaglianza: $\sum a_{ij}y_i = c_j$.
4. Risolvi il sistema di equazioni lineari per $\mathbf{y}$.
5. Controlla che $\mathbf{y}$ sia ammissibile (es. $y_i \ge 0$ e tutti i vincoli duali soddisfatti).
6. Se è ammissibile, $\mathbf{x}$ e $\mathbf{y}$ sono soluzioni ottime.
