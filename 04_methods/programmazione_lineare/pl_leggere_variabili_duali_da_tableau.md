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
  - tableau-simplesso
  - variabili-duali
  - method-card
---

# METHOD CARD — Lettura delle Variabili Duali dal Tableau Ottimo

## Quando usarla

Usare questa card per identificare la soluzione ottima del problema duale ($\mathbf{y}^*$) partendo direttamente dal tableau ottimo del simplesso del problema primale (MAX).

## Principio Teorico

Ad ogni iterazione del metodo del simplesso, la riga 0 del tableau identifica una soluzione del problema duale (non necessariamente ammissibile).
All'ottimo del primale, la soluzione duale associata diventa ammissibile ed è pari alla soluzione ottima duale $\mathbf{y}^*$.

---

## Procedura Operativa Passo-Passo

### 1. Individuare il Tableau Ottimo del Primale
Assicurarsi che il tableau sia ottimo (riga 0 con tutti i coefficienti delle variabili $\ge 0$ in caso di MAX standard).

### 2. Identificare i Coefficienti delle Variabili di Slack nella Riga 0
- Per ciascun vincolo primale $i$-esimo ($i = 1, \dots, m$), identificare la corrispondente variabile di scarto (slack) $s_i$ introdotta nella forma aumentata.
- Leggere il coefficiente della variabile $s_i$ nella **riga 0** (riga della funzione obiettivo $Z$).

### 3. Assegnare i Valori alle Variabili Duali ($y_i^*$)
Il valore ottimo della variabile duale $y_i^*$ è esattamente pari al coefficiente di $s_i$ nella riga 0 del tableau ottimo:
$$
y_i^* = \text{Coefficiente di } s_i \text{ nella riga 0 del tableau ottimo}
$$

> [!IMPORTANT]
> Questa regola si applica direttamente quando il primale è in forma standard di massimo (quindi con vincoli $\le$ e slack $s_i$ aggiunte con segno positivo $+s_i$).

---

## Esempio Numerico (Wyndor Glass Co.)

Si consideri il tableau ottimo del simplesso del problema primale di Wyndor Glass:

| Base | $Z$ | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $s_3$ | RHS |
|---|---|---|---|---|---|---|---|
| **$Z$** | 1 | 0 | 0 | 0 | $\frac{3}{2}$ | 1 | 36 |
| **$x_1$** | 0 | 1 | 0 | 0 | $-\frac{1}{3}$ | $\frac{1}{3}$ | 2 |
| **$s_1$** | 0 | 0 | 0 | 1 | $\frac{1}{3}$ | $-\frac{1}{3}$ | 2 |
| **$x_2$** | 0 | 0 | 1 | 0 | $\frac{1}{2}$ | 0 | 6 |

### Lettura dei coefficienti:
1. Sotto la variabile di slack $s_1$ (associata al vincolo 1): il coefficiente in riga 0 è $0$.
   $$\implies y_1^* = 0$$
2. Sotto la variabile di slack $s_2$ (associata al vincolo 2): il coefficiente in riga 0 è $\frac{3}{2}$.
   $$\implies y_2^* = \frac{3}{2}$$
3. Sotto la variabile di slack $s_3$ (associata al vincolo 3): il coefficiente in riga 0 è $1$.
   $$\implies y_3^* = 1$$

### Soluzione Ottima Duale:
$$
\mathbf{y}^* = \left(0, \frac{3}{2}, 1\right)
$$

### Verifica del Valore Obiettivo:
$$
W^* = 4y_1^* + 12y_2^* + 18y_3^* = 4(0) + 12\left(\frac{3}{2}\right) + 18(1) = 0 + 18 + 18 = 36
$$
Poiché $Z^* = 36$, per il teorema della dualità forte l'ottimo è corretto.
