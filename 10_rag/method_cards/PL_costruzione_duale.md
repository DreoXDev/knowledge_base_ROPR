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
Usare questa card come riferimento rapido per scrivere le equazioni del problema duale per un modello primale espresso in forma standard.

## Procedura Sintetica

1. **Invertire l'obiettivo**: $\max Z \implies \min W$ (o viceversa).
2. **Associare variabili duali ai vincoli**: Ad ogni vincolo primale $i$ corrisponde una variabile duale $y_i \ge 0$.
3. **Impostare la F.O.**: I coefficienti di $W$ sono i termini noti (RHS) dei vincoli primali ($b_i$).
4. **Scrivere i vincoli duali**:
   - Ad ogni variabile primale $x_j \ge 0$ corrisponde un vincolo duale di tipo $\ge$.
   - La matrice dei coefficienti del duale è la trasposta $A^T$ del primale.
   - I termini noti dei vincoli duali sono i coefficienti della F.O. primale ($c_j$).

## Esempio Formale

| Primale (MAX Standard) | Duale (MIN Standard) |
|---|---|
| $\max Z = \mathbf{c}\mathbf{x}$ | $\min W = \mathbf{y}\mathbf{b}$ |
| $\mathbf{A}\mathbf{x} \le \mathbf{b}$ | $\mathbf{y}\mathbf{A} \ge \mathbf{c}$ |
| $\mathbf{x} \ge 0$ | $\mathbf{y} \ge 0$ |

## Errori da Evitare
- Non trasporre la matrice dei coefficienti $A$.
- Dimenticare che i termini noti del primale diventano i coefficienti della funzione obiettivo del duale.
