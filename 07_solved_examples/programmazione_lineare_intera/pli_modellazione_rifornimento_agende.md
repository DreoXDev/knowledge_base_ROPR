---
type: solved_example
topic: programmazione_lineare_intera
status: active
sources: [9_esercizi_modelli.pdf]
reliability: official
---

# Esempio Svolto: Rifornimento Agende con Lotti e Sconti Fissi

Esempio di modellazione PLI complessa per la gestione della logistica di rifornimento con vincoli di ordinazione a lotti (pacchi) e sconti condizionati sui costi fissi.

---

## Dati del Problema

- **Cartolerie**: $C_1, C_2$.
- **Fornitori**: $F_1, F_2, F_3, F_4$.
- **Costi Unitari di Spedizione $d_{ij}$**:
  *   $F_1$: $2$ (per $C_1$), $6$ (per $C_2$)
  *   $F_2$: $13$, $11$
  *   $F_3$: $9$, $5$
  *   $F_4$: $8$, $4$
- **Costi Fissi di Spedizione $f_i$**: $F_1 = 100$, $F_2 = 90$, $F_3 = 80$, $F_4 = 70$ (applicati a ciascuna cartoleria servita).
- **Capacità dei Fornitori**: $F_1 \le 120$, $F_2 \le 165$, $F_3 \le 178$, $F_4 \le 199$.
- **Domanda minima e Stoccaggio**:
  *   $C_1$: Acquisto minimo $\ge 120$, capacità magazzino $\le 150$.
  *   $C_2$: Acquisto minimo $\ge 105$, capacità magazzino $\le 160$.

### Vincoli Aggiuntivi:
1.  La cartoleria $C_1$ si rifornisce al massimo da 3 diversi fornitori.
2.  Se si sceglie il fornitore $F_4$, l'acquisto minimo complessivo (per entrambe le cartolerie) deve essere di almeno 40 agende.
3.  Il fornitore $F_1$ vende la merce solo in pacchi da 20 agende.
4.  Il fornitore $F_2$ dimezza il costo fisso di spedizione a ciascuna cartoleria se l'ordine complessivo è di almeno 60 agende.

---

## Modello Matematico (PLI)

### 1. Variabili Decisionali
*   $x_{ij} \ge 0$, intero: Quantità di agende spedite dal fornitore $i \in \{1, 2, 3, 4\}$ alla cartoleria $j \in \{1, 2\}$.
*   $y_{ij} \in \{0, 1\}$: Vale $1$ se il fornitore $i$ spedisce alla cartoleria $j$, $0$ altrimenti.
*   $u_4 \in \{0, 1\}$: Vale $1$ se viene utilizzato il fornitore $F_4$, $0$ altrimenti.
*   $w_{1j} \ge 0$, intero: Numero di pacchi da 20 agende spediti da $F_1$ alla cartoleria $j$.
*   $z \in \{0, 1\}$: Vale $1$ se l'ordine complessivo presso $F_2$ è di almeno 60 agende, $0$ altrimenti.
*   $h_j \in \{0, 1\}$: Vale $1$ se si applica lo sconto sul costo fisso di $F_2$ per la cartoleria $j$ (ossia se $y_{2j} = 1$ e $z = 1$).

### 2. Funzione Obiettivo
Minimizzare il costo di trasporto unitario + i costi fissi (al netto del dimezzamento per $F_2$):

$$
\begin{aligned}
\min \quad & \sum_{i=1}^4 \sum_{j=1}^2 d_{ij} x_{ij} + \sum_{j=1}^2 (100 y_{1j} + 80 y_{3j} + 70 y_{4j}) + \\
& \sum_{j=1}^2 (90 y_{2j} - 45 h_j)
\end{aligned}
$$

### 3. Vincoli Funzionali

*   **Soddisfacimento Domanda e Stoccaggio**:
    $$
    120 \le x_{11} + x_{21} + x_{31} + x_{41} \le 150
    $$
    $$
    105 \le x_{12} + x_{22} + x_{32} + x_{42} \le 160
    $$

*   **Capacità Massima Fornitori**:
    $$
    x_{i1} + x_{i2} \le \text{Cap}_i \quad \forall i=1, 2, 3, 4
    $$

*   **Attivazione Costi Fissi**:
    L'invio di merci attiva il costo fisso (capacità massima di stoccaggio è 160):
    $$
    x_{ij} \le 160 y_{ij} \quad \forall i, j
    $$

*   **Limite Fornitori per $C_1$ (Al massimo 3)**:
    $$
    y_{11} + y_{21} + y_{31} + y_{41} \le 3
    $$

*   **Acquisto Minimo Condizionato per $F_4$ (Almeno 40)**:
    Attivazione della variabile globale del fornitore $F_4$:
    $$
    y_{4j} \le u_4 \quad \forall j=1, 2
    $$
    Se attivo, l'ordine totale deve essere di almeno 40 agende (e non può superare la capacità 199):
    $$
    x_{41} + x_{42} \ge 40 u_4
    $$
    $$
    x_{41} + x_{42} \le 199 u_4
    $$

*   **Lotti Discreti (Pacchi da 20) per $F_1$**:
    Le variabili di flusso per $F_1$ devono essere multipli di 20:
    $$
    x_{1j} = 20 w_{1j} \quad \forall j=1, 2
    $$

*   **Dimezzamento Costo Fisso per $F_2$**:
    La condizione di sconto $z = 1$ è attivata se il flusso totale di $F_2$ è almeno 60 (con capacità $F_2 = 165$):
    $$
    x_{21} + x_{22} \ge 60 z
    $$
    $$
    x_{21} + x_{22} \le 59 + 106 z
    $$
    La variabile di sconto $h_j$ rappresenta l'operatore logico AND ($h_j = y_{2j} \land z$):
    $$
    h_j \le y_{2j} \quad \forall j=1, 2
    $$
    $$
    h_j \le z \quad \forall j=1, 2
    $$
    $$
    h_j \ge y_{2j} + z - 1 \quad \forall j=1, 2
    $$

### 4. Dominio delle Variabili
$$
x_{ij} \ge 0, \text{ intero} \quad \forall i, j
$$
$$
y_{ij} \in \{0, 1\} \quad \forall i, j
$$
$$
u_4, z, h_1, h_2 \in \{0, 1\}
$$
$$
w_{11}, w_{12} \ge 0, \text{ intero}
$$
