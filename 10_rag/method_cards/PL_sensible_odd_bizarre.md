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
  - sensible-odd-bizarre
  - method-card
---

# METHOD CARD — Metodo Sensible / Odd / Bizarre (SOB)

## Quando usarla
Usare questa card come riferimento rapido all'esame per costruire il duale in casi non standard (vincoli di uguaglianza, variabili negative o libere).

## Corrispondenze Rapide

### Primale MAX $\implies$ Duale MIN

- **Vincoli Primale $\implies$ Variabili Duali**:
  - Vincolo $\le$ (Sensible) $\implies$ Variabile $y_i \ge 0$
  - Vincolo $=$ (Odd) $\implies$ Variabile $y_i$ Libera
  - Vincolo $\ge$ (Bizarre) $\implies$ Variabile $y_i \le 0$
- **Variabili Primale $\implies$ Vincoli Duale**:
  - Variabile $x_j \ge 0$ (Sensible) $\implies$ Vincolo $\ge$
  - Variabile $x_j$ Libera (Odd) $\implies$ Vincolo $=$
  - Variabile $x_j \le 0$ (Bizarre) $\implies$ Vincolo $\le$

---

### Primale MIN $\implies$ Duale MAX

- **Vincoli Primale $\implies$ Variabili Duali**:
  - Vincolo $\ge$ (Sensible) $\implies$ Variabile $y_i \ge 0$
  - Vincolo $=$ (Odd) $\implies$ Variabile $y_i$ Libera
  - Vincolo $\le$ (Bizarre) $\implies$ Variabile $y_i \le 0$
- **Variabili Primale $\implies$ Vincoli Duale**:
  - Variabile $x_j \ge 0$ (Sensible) $\implies$ Vincolo $\le$
  - Variabile $x_j$ Libera (Odd) $\implies$ Vincolo $=$
  - Variabile $x_j \le 0$ (Bizarre) $\implies$ Vincolo $\ge$

## Esempio Operativo
Se in un problema di MAX hai un vincolo $x_1 + 3x_2 \ge 10$, la variabile duale corrispondente $y_1$ sarà $\le 0$ (Bizarre). Se hai una variabile primale $x_2$ libera, il secondo vincolo duale sarà un'uguaglianza ($=$).
