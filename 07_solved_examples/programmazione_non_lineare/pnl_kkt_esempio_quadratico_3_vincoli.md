---
type: solved-example
topic: programmazione_non_lineare
status: consolidated
sources:
  - raw_assets/Programmazione Non Lineare/PNL Vincolata 4.pdf
reliability: official
---

# Esercizio Svolto: Minimizzazione con Condizioni KKT ed Enumerazione dei Vincoli Attivi

Questo esercizio mostra la risoluzione completa di un problema di Programmazione Non Lineare (PNL) vincolata con vincoli di disuguaglianza tramite le condizioni KKT e l'analisi combinatoria di tutti gli 8 casi possibili.

---

## Testo del Problema

Risolvere il seguente problema di ottimizzazione:
$$\min f(x, y) = 4(x-1)^2 + (y-2)^2$$

soggetto a:
$$x+y \le 2, \quad x \ge -1, \quad y \ge -1$$

---

## 1. Ristrutturazione in Forma Standard

Riscriviamo i vincoli nella forma standard $g_i(x, y) \le 0$:
1.  $g_1(x, y) = x+y-2 \le 0$
2.  $x \ge -1 \implies -x-1 \le 0 \implies g_2(x, y) = -x-1 \le 0$
3.  $y \ge -1 \implies -y-1 \le 0 \implies g_3(x, y) = -y-1 \le 0$

La funzione Lagrangiana associata è:
$$L(x, y, \mu) = 4(x-1)^2 + (y-2)^2 + \mu_1(x+y-2) + \mu_2(-x-1) + \mu_3(-y-1)$$
Per un problema di **minimizzazione**, le condizioni KKT richiedono moltiplicatori non negativi: $\mu_1, \mu_2, \mu_3 \ge 0$.

---

## 2. Condizioni KKT

1.  **Stazionarietà**:
    $$\frac{\partial L}{\partial x} = 8(x-1) + \mu_1 - \mu_2 = 0$$
    $$\frac{\partial L}{\partial y} = 2(y-2) + \mu_1 - \mu_3 = 0$$
2.  **Ammissibilità Primale**:
    $$x+y-2 \le 0, \quad -x-1 \le 0, \quad -y-1 \le 0$$
3.  **Ammissibilità Duale**:
    $$\mu_1 \ge 0, \quad \mu_2 \ge 0, \quad \mu_3 \ge 0$$
4.  **Complementarità degli Scarti**:
    $$\mu_1(x+y-2) = 0$$
    $$\mu_2(-x-1) = 0$$
    $$\mu_3(-y-1) = 0$$

---

## 3. Analisi dei Casi dei Vincoli Attivi ($2^3 = 8$ Combinazioni)

### Caso 1: Solo $g_1$ attivo ($\mu_1 \ge 0$, $\mu_2 = \mu_3 = 0$)
-   Vincolo attivo: $x+y-2 = 0 \implies y = 2-x$.
-   Stazionarietà:
    $$8(x-1) + \mu_1 = 0 \implies \mu_1 = 8(1-x)$$
    $$2(y-2) + \mu_1 = 0 \implies 2(2-x-2) + 8(1-x) = 0 \implies -2x + 8 - 8x = 0 \implies 10x = 8 \implies x = 0.8$$
-   Coordinate del punto: $x = 0.8$, $y = 1.2$.
-   Moltiplicatore: $\mu_1 = 8(1 - 0.8) = 1.6 \ge 0$.
-   Ammissibilità primale:
    -   $g_2(0.8, 1.2) = -0.8-1 = -1.8 \le 0$ (soddisfatto)
    -   $g_3(0.8, 1.2) = -1.2-1 = -2.2 \le 0$ (soddisfatto)
-   **Esito**: Il punto $(0.8, 1.2)$ è **KKT-valido** con $f(0.8, 1.2) = 4(0.8-1)^2 + (1.2-2)^2 = 0.8$.

### Caso 2: Solo $g_2$ attivo ($\mu_2 \ge 0$, $\mu_1 = \mu_3 = 0$)
-   Vincolo attivo: $x = -1$.
-   Stazionarietà:
    $$8(x-1) - \mu_2 = 0 \implies \mu_2 = 8(x-1)$$
    $$2(y-2) = 0 \implies y = 2$$
-   Moltiplicatore: $\mu_2 = 8(-1 - 1) = -16 < 0$.
-   **Esito**: **Scartato** per violazione dell'ammissibilità duale ($\mu_2 < 0$).

### Caso 3: Solo $g_3$ attivo ($\mu_3 \ge 0$, $\mu_1 = \mu_2 = 0$)
-   Vincolo attivo: $y = -1$.
-   Stazionarietà:
    $$8(x-1) = 0 \implies x = 1$$
    $$2(y-2) - \mu_3 = 0 \implies \mu_3 = 2(y-2)$$
-   Moltiplicatore: $\mu_3 = 2(-1-2) = -6 < 0$.
-   **Esito**: **Scartato** per violazione dell'ammissibilità duale ($\mu_3 < 0$).

### Caso 4: Vincoli $g_1$ e $g_2$ attivi ($\mu_1, \mu_2 \ge 0$, $\mu_3 = 0$)
-   Vincoli attivi: $x+y-2 = 0$ e $x = -1 \implies y = 3$.
-   Stazionarietà:
    $$8(-1-1) + \mu_1 - \mu_2 = 0 \implies -16 + \mu_1 - \mu_2 = 0$$
    $$2(3-2) + \mu_1 = 0 \implies 2 + \mu_1 = 0 \implies \mu_1 = -2 < 0$$
-   **Esito**: **Scartato** per violazione dell'ammissibilità duale ($\mu_1 < 0$).

### Caso 5: Vincoli $g_1$ e $g_3$ attivi ($\mu_1, \mu_3 \ge 0$, $\mu_2 = 0$)
-   Vincoli attivi: $x+y-2 = 0$ e $y = -1 \implies x = 3$.
-   Stazionarietà:
    $$8(3-1) + \mu_1 = 0 \implies 16 + \mu_1 = 0 \implies \mu_1 = -16 < 0$$
-   **Esito**: **Scartato** per violazione dell'ammissibilità duale ($\mu_1 < 0$).

### Caso 6: Vincoli $g_2$ e $g_3$ attivi ($\mu_2, \mu_3 \ge 0$, $\mu_1 = 0$)
-   Vincoli attivi: $x = -1$ e $y = -1$.
-   Stazionarietà:
    $$8(-1-1) - \mu_2 = 0 \implies \mu_2 = -16 < 0$$
-   **Esito**: **Scartato** per violazione dell'ammissibilità duale ($\mu_2 < 0$).

### Caso 7: Tutti i vincoli attivi ($g_1, g_2, g_3$ attivi)
-   Vincoli attivi: $x+y=2$, $x=-1$, $y=-1$.
-   **Esito**: **Scartato** per inammissibilità geometrica (sistema privo di soluzioni poiche $-1 - 1 = -2 \ne 2$).

### Caso 8: Nessun vincolo attivo ($\mu_1 = \mu_2 = \mu_3 = 0$)
-   Stazionarietà:
    $$8(x-1) = 0 \implies x = 1$$
    $$2(y-2) = 0 \implies y = 2$$
-   Ammissibilità primale:
    $$g_1(1, 2) = 1+2-2 = 1 > 0 \quad (\text{violato})$$
-   **Esito**: **Scartato** per inammissibilità primale (l'ottimo non vincolato $(1,2)$ cade fuori dalla regione ammissibile).

---

## 4. Tabella Riassuntiva dei Casi

| Caso | Vincoli Attivi | Punto Candidato | Valore $f$ | Moltiplicatori | Esito |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | $g_1$ | $(0.8, 1.2)$ | **0.8** | $\mu_1=1.6$, $\mu_2=\mu_3=0$ | **Ottimo Globale** |
| 2 | $g_2$ | $(-1, 2)$ | 16 | $\mu_2=-16$ | Scartato ($\mu_2 < 0$) |
| 3 | $g_3$ | $(1, -1)$ | 9 | $\mu_3=-6$ | Scartato ($\mu_3 < 0$) |
| 4 | $g_1, g_2$ | $(-1, 3)$ | 17 | $\mu_1=-2$ | Scartato ($\mu_1 < 0$) |
| 5 | $g_1, g_3$ | $(3, -1)$ | 25 | $\mu_1=-16$ | Scartato ($\mu_1 < 0$) |
| 6 | $g_2, g_3$ | $(-1, -1)$ | 25 | $\mu_2=-16, \mu_3=-6$ | Scartato (moltiplicatori $< 0$) |
| 7 | $g_1, g_2, g_3$| $\emptyset$ | - | - | Sistema incompatibile |
| 8 | nessuno | $(1, 2)$ | 0 | $\mu_1=\mu_2=\mu_3=0$ | Scartato (punto non ammissibile) |

---

## 5. Soluzione Finale

L'unico candidato KKT ammissibile e valido è il punto ottenuto dal Caso 1.

*   **Punto di ottimo globale**: $x^* = (0.8, 1.2)$
*   **Moltiplicatori KKT**: $\mu_1^* = 1.6$, $\mu_2^* = \mu_3^* = 0$
*   **Valore della funzione all'ottimo**: $f(0.8, 1.2) = 0.8$
