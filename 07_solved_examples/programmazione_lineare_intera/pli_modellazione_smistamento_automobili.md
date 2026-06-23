---
type: solved_example
topic: programmazione_lineare_intera
status: active
sources: [9_esercizi_modelli.pdf]
reliability: official
---

# Esempio Svolto: Smistamento Automobili con Vincoli Logici

Esempio di modellazione PLI per la pianificazione dello smistamento auto con vincoli condizionali.

---

## Dati del Problema

- **Porti**: $P_1, P_2, P_3$.
- **Centri**: $S_1, S_2, S_3, S_4$.
- **Tasse Portuali**: $P_1 = 250$, $P_2 = 150$, $P_3 = 200$ (euro/auto).
- **Costi di Trasporto**:
  *   $P_1 \to S$: $(15, 25, 10, 20)$
  *   $P_2 \to S$: $(40, 30, 30, 50)$
  *   $P_3 \to S$: $(25, 35, 20, 30)$
- **Costi Totali Unitari ($c_{ij} = \text{tassa} + \text{trasporto}$)**:
  *   $P_1$: $c_{1} = (265, 275, 260, 270)$
  *   $P_2$: $c_{2} = (190, 180, 180, 200)$
  *   $P_3$: $c_{3} = (225, 235, 220, 230)$
- **Capacità Porti**: $P_1 \le 350$, $P_2 \le 200$, $P_3 \le 300$.
- **Richieste Centri**: $S_1 \ge 170$, $S_2 \ge 130$, $S_3 \ge 100$, $S_4 \ge 200$.

### Vincoli Speciali:
1.  Il centro $S_3$ deve essere rifornito da un solo porto.
2.  Se il porto $P_2$ serve il centro $S_2$, allora deve servire anche il centro $S_4$.

---

## Modello Matematico (PLI)

### 1. Variabili Decisionali
*   $x_{ij} \ge 0$, intero: Numero di automobili inviate dal porto $i \in \{1, 2, 3\}$ al centro $j \in \{1, 2, 3, 4\}$.
*   $y_{i3} \in \{0, 1\}$: Vale $1$ se il porto $i$ serve il centro $S_3$, $0$ altrimenti.
*   $w_{2j} \in \{0, 1\}$: Vale $1$ se il porto $P_2$ serve il centro $S_j$ (per $j \in \{2, 4\}$), $0$ altrimenti.

### 2. Funzione Obiettivo
Minimizzare i costi complessivi di trasporto e tasse portuali:

$$
\min \sum_{i=1}^3 \sum_{j=1}^4 c_{ij} x_{ij}
$$

Esplicitando i coefficienti $c_{ij}$:

$$
\begin{aligned}
\min \quad & 265 x_{11} + 275 x_{12} + 260 x_{13} + 270 x_{14} + \\
& 190 x_{21} + 180 x_{22} + 180 x_{23} + 200 x_{24} + \\
& 225 x_{31} + 235 x_{32} + 220 x_{33} + 230 x_{34}
\end{aligned}
$$

### 3. Vincoli Funzionali

*   **Soddisfacimento Domanda Centri**:
    $$
    \sum_{i=1}^3 x_{ij} \ge D_j \quad \forall j=1, 2, 3, 4
    $$
    $$
    \begin{aligned}
    x_{11} + x_{21} + x_{31} & \ge 170 \\
    x_{12} + x_{22} + x_{32} & \ge 130 \\
    x_{13} + x_{23} + x_{33} & \ge 100 \\
    x_{14} + x_{24} + x_{34} & \ge 200
    \end{aligned}
    $$

*   **Capacità Massima Porti**:
    $$
    \sum_{j=1}^4 x_{ij} \le U_i \quad \forall i=1, 2, 3
    $$
    $$
    \begin{aligned}
    x_{11} + x_{12} + x_{13} + x_{14} & \le 350 \\
    x_{21} + x_{22} + x_{23} + x_{24} & \le 200 \\
    x_{31} + x_{32} + x_{33} + x_{34} & \le 300
    \end{aligned}
    $$

*   **Servizio Unico per $S_3$**:
    La somma delle attivazioni dei porti per $S_3$ deve essere pari a 1:
    $$
    y_{13} + y_{23} + y_{33} = 1
    $$
    La quantità inviata da ciascun porto a $S_3$ è vincolata dall'attivazione (con $M = 100$, pari alla richiesta esatta di $S_3$):
    $$
    x_{i3} \le 100 y_{i3} \quad \forall i=1, 2, 3
    $$

*   **Condizione Se-Allora per $P_2$ (Se serve $S_2 \implies$ serve $S_4$)**:
    Associare le variabili di attivazione al flusso effettivo (capacità di $P_2$ è 200):
    $$
    x_{22} \le 200 w_{22}
    $$
    $$
    x_{24} \le 200 w_{24}
    $$
    Imporre la logica di implicazione ($w_{22} \le w_{24}$):
    $$
    w_{22} - w_{24} \le 0
    $$

### 4. Dominio delle Variabili
$$
x_{ij} \ge 0, \text{ intero} \quad \forall i, j
$$
$$
y_{i3} \in \{0, 1\} \quad \forall i
$$
$$
w_{22}, w_{24} \in \{0, 1\}
$$
