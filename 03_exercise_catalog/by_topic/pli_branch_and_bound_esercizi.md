---
type: exercise_catalog
topic: programmazione_lineare_intera
status: active
sources: [16_esercizi_BB.pdf]
reliability: official
---

# Esercizi Algoritmi Branch and Bound

Raccolta dei testi e dei risultati degli esercizi risolti con l'algoritmo di Branch and Bound.

---

## Esercizi Standard (2 Variabili)

Tutti gli esercizi richiedono di risolvere problemi PLI di massimo a due variabili intere non negative, visitando l'albero in ampiezza e facendo branching sulla prima variabile frazionaria.

### Esercizio 1
*   **Modello**: $\max 5x_1 + 8x_2$ s.t. $x_1 + x_2 \le 6$, $5x_1 + 9x_2 \le 45$, $x_1, x_2 \in \mathbb{Z}_+$.
*   **Rilassamento $P_0$**: $x^{(0)} = (2.25, 3.75)$, $z = 41.25$. Branching su $x_1$: $x_1 \le 2$ ($P_1$) e $x_1 \ge 3$ ($P_2$).
*   **Ottimo**: $x^* = (0, 5)$, $z^* = 40$.
*   **Esempio Svolto Completo**: [pli_bb_esercizio_svolto_1.md](../../07_solved_examples/programmazione_lineare_intera/pli_bb_esercizio_svolto_1.md).

### Esercizio 2
*   **Modello**: $\max x_1 + 3x_2$ s.t. $x_1 + 5x_2 \le 21$, $8x_1 + 2x_2 \le 35$, $x_1, x_2 \in \mathbb{Z}_+$.
*   **Rilassamento $P_0$**: $x^{(0)} = (3.5, 3.5)$, $z = 14$. Branching su $x_1$: $x_1 \le 3$ ($P_1$) e $x_1 \ge 4$ ($P_2$).
*   **Ottimo**: $x^* = (1, 4)$, $z^* = 13$ (oppure $x^* = (4, 3)$, $z^* = 13$ - ottimi multipli).

### Esercizio 3
*   **Modello**: $\max 5x_1 + 4x_2$ s.t. $3x_1 + 2x_2 \le 16$, $2x_1 + 3x_2 \le 16$, $x_1, x_2 \in \mathbb{Z}_+$.
*   **Rilassamento $P_0$**: $x^{(0)} = (3.2, 3.2)$, $z = 28.8$.
*   **Ottimo**: $x^* = (4, 2)$, $z^* = 28$.

### Esercizio 4
*   **Modello**: $\max 7x_1 + 8x_2$ s.t. $x_1 + 2x_2 \le 10$, $3x_1 + 2x_2 \le 16$, $x_1, x_2 \in \mathbb{Z}_+$.
*   **Rilassamento $P_0$**: $x^{(0)} = (3, 3.5)$, $z = 49$.
*   **Ottimo**: $x^* = (2, 4)$, $z^* = 46$ (oppure $x^* = (4, 2)$, $z^* = 46$).

### Esercizio 5
*   **Modello**: $\max 7x_1 + 6x_2$ s.t. $2x_1 + x_2 \le 10$, $2x_1 + 3x_2 \le 16$, $x_1, x_2 \in \mathbb{Z}_+$.
*   **Rilassamento $P_0$**: $x^{(0)} = (3.5, 3)$, $z = 42.5$.
*   **Ottimo**: $x^* = (3, 3)$, $z^* = 39$ (oppure $x^* = (4, 2)$, $z^* = 40$ - incombente ottimo reale).

### Esercizio 6
*   **Modello**: $\max 5x_1 + 6x_2$ s.t. $2x_1 + 3x_2 \le 12$, $3x_1 + 2x_2 \le 12$, $x_1, x_2 \in \mathbb{Z}_+$.
*   **Rilassamento $P_0$**: $x^{(0)} = (2.4, 2.4)$, $z = 26.4$.
*   **Ottimo**: $x^* = (0, 4)$, $z^* = 24$ (o multiplo $x^* = (2, 2)$, $z^* = 22$, ottimo globale $z^*=24$ in $(0,4)$).

### Esercizio 7
*   **Modello**: $\max x_1 + 2x_2$ s.t. $-3x_1 + 5x_2 \le 10$, $7x_1 + 5x_2 \le 35$, $x_1, x_2 \in \mathbb{Z}_+$.
*   **Rilassamento $P_0$**: $x^{(0)} = (2.5, 3.5)$, $z = 9.5$.
*   **Ottimo**: $x^* = (0, 2)$, $z^* = 4$ o migliore $x^* = (2, 3)$, $z^* = 8$ (ottimo globale $z^* = 9$ in $(3,3)$ o $(1,2)$).

### Esercizio 8
*   **Modello**: $\max 20x_1 + 17x_2$ s.t. $x_1 + x_2 \le 5$, $10x_1 + 6x_2 \le 45$, $x_1, x_2 \in \mathbb{Z}_+$.
*   **Rilassamento $P_0$**: $x^{(0)} = (3.75, 1.25)$, $z = 96.25$.
*   **Ottimo**: $x^* = (3, 2)$, $z^* = 94$.

### Esercizio 9
*   **Modello**: $\max x_1 - 3x_2$ s.t. $-2x_1 + 5x_2 \le 10$, $6x_1 + 5x_2 \le 30$, $x_1, x_2 \in \mathbb{Z}_+$.
*   **Rilassamento $P_0$**: $x^{(0)} = (5, 0)$, $z = 5$.
*   **Ottimo**: $x^* = (5, 0)$, $z^* = 5$ (già intera ottima alla radice).

### Esercizio 10
*   **Modello**: $\max x_1 + 2x_2$ s.t. $-3x_1 + 5x_2 \le 12$, $7x_1 + 5x_2 \le 35$, $x_1, x_2 \in \mathbb{Z}_+$.
*   **Rilassamento $P_0$**: $x^{(0)} = (2.3, 3.78)$, $z = 9.85$.
*   **Ottimo**: $x^* = (2, 3)$, $z^* = 8$ o $(3,3)$ con $z^*=9$ (ottimo globale $z^* = 9$ in $(3,3)$).

### Esercizio 11
*   **Modello**: $\max 32x_1 + 20x_2$ s.t. $9x_1 + 5x_2 \le 45$, $x_1 + x_2 \le 6$, $x_1, x_2 \in \mathbb{Z}_+$.
*   **Rilassamento $P_0$**: $x^{(0)} = (3.75, 2.25)$, $z = 165$.
*   **Ottimo**: $x^* = (5, 0)$, $z^* = 160$.

---

## Problemi dello Zaino (Knapsack)

Risoluzione dei problemi dello zaino binario con 4 oggetti.

### Esercizio 12
*   **Dati**: Valori $v = \{15, 11, 20, 10\}$, pesi $p = \{5, 2, 3, 4\}$, capacità $C = 8$.
*   **Rendimenti**: $\frac{v}{p} = \{3, 5.5, 6.67, 2.5\} \implies$ ordinamento: $3, 2, 1, 4$.
*   **Risultati**:
    *   *Euristica Greedy (LB)*: $Z_I = 31$ (oggetti 3 e 2).
    *   *Rilassamento LP (UB)*: $34.4$ (oggetti 3, 2 e $\frac{3}{5}$ di 1).
    *   *B&B Ottimo*: $x^* = (1, 0, 1, 0)$, $z^* = 35$ (oggetti 1 e 3).
*   **Esempio Svolto Completo**: [pli_bb_esercizio_svolto_zaino.md](../../07_solved_examples/programmazione_lineare_intera/pli_bb_esercizio_svolto_zaino.md).

### Esercizio 13
*   **Dati**: Valori $v = \{16, 12, 11, 7\}$, pesi $p = \{6, 5, 3, 2\}$, capacità $C = 8$.
*   **Rendimenti**: $\frac{v}{p} = \{2.67, 2.4, 3.67, 3.5\} \implies$ ordinamento: $3, 4, 1, 2$.
*   **Risultati**:
    *   *Euristica Greedy (LB)*: $18$ (oggetti 3, 4 e non c'è spazio per 1).
    *   *Rilassamento LP (UB)*: $23.67$ (oggetti 3, 4 e $\frac{1}{2}$ di 1).
    *   *B&B Ottimo*: $x^* = (1, 0, 0, 1)$, $z^* = 23$ (oggetti 1 e 4).

### Esercizio 14
*   **Dati**: Valori $v = \{11, 23, 18, 6\}$, pesi $p = \{7, 6, 3, 2\}$, capacità $C = 8$.
*   **Rendimenti**: $\frac{v}{p} = \{1.57, 3.83, 6, 3\} \implies$ ordinamento: $3, 2, 4, 1$.
*   **Risultati**:
    *   *Euristica Greedy (LB)*: $18$ (oggetto 3, oggetto 2 non entra, entra oggetto 4, $z = 18+6=24$ - incombente reale).
    *   *Rilassamento LP (UB)*: $29.67$ (oggetti 3 e $\frac{5}{6}$ di 2).
    *   *B&B Ottimo*: $x^* = (0, 0, 1, 0)$ o simile. Ottimo reale: $x^* = (0, 1, 0, 1)$, $z^* = 29$ (oggetti 2 e 4).

### Esercizio 15
*   **Dati**: Valori $v = \{13, 5, 18, 11\}$, pesi $p = \{5, 4, 3, 2\}$, capacità $C = 8$.
*   **Rendimenti**: $\frac{v}{p} = \{2.6, 1.25, 6, 5.5\} \implies$ ordinamento: $3, 4, 1, 2$.
*   **Risultati**:
    *   *Euristica Greedy (LB)*: $29$ (oggetti 3 and 4).
    *   *Rilassamento LP (UB)*: $36.8$ (oggetti 3, 4 e $\frac{3}{5}$ di 1).
    *   *B&B Ottimo*: $x^* = (1, 0, 1, 0)$, $z^* = 31$ (oggetti 1 e 3).

### Esercizio 16
*   **Dati**: Valori $v = \{16, 17, 21, 23\}$, pesi $p = \{5, 3, 6, 2\}$, capacità $C = 8$.
*   **Rendimenti**: $\frac{v}{p} = \{3.2, 5.67, 3.5, 11.5\} \implies$ ordinamento: $4, 2, 3, 1$.
*   **Risultati**:
    *   *Euristica Greedy (LB)*: $40$ (oggetti 4 and 2).
    *   *Rilassamento LP (UB)*: $47$ (oggetti 4, 2 e $\frac{1}{2}$ di 3).
    *   *B&B Ottimo*: $x^* = (1, 1, 0, 0)$, $z^* = 33$ o $x^* = (0, 1, 0, 1)$, $z^*=40$ (oggetti 2 e 4).
