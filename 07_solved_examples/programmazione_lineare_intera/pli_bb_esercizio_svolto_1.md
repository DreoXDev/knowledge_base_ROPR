---
fonte: 16_esercizi_BB.pdf
area: Programmazione Lineare Intera
priorita: alta
stato: completato
---

# PLI - Esempio Svolto 1: Branch and Bound

## Fonte
`16_esercizi_BB.pdf`, Esercizio 1

## Descrizione del Problema
Risolvere il seguente problema di PLI utilizzando il metodo Branch and Bound, visitando l'albero in ampiezza e istanziando le variabili frazionarie:

$$
\max \quad Z = 5 x_1 + 8 x_2
$$
$$
\text{s.t.} \quad x_1 + x_2 \le 6
$$
$$
5x_1 + 9x_2 \le 45
$$
$$
x_1, x_2 \ge 0, \quad x_1, x_2 \in \mathbb{Z}
$$

## Risoluzione Passo-Passo

### 1. Inizializzazione (Nodo Radice $P$)
*   Risoluzione del rilassamento continuo di $P$:
    *   Soluzione ottima continua: $x^* = (2.25, 3.75)$
    *   Valore di valutazione superiore: $Z_S(P) = 41.25$
*   Euristica iniziale (arrotondamento per difetto della soluzione):
    *   Soluzione intera candidata: $x_I = (2, 3)$
    *   Valore di valutazione inferiore (soluzione incombente): $Z_I = 5(2) + 8(3) = 34$
*   Poiché la soluzione non è intera e $Z_S(P) = 41.25 > 34$, il nodo rimane aperto.
*   **Branching**: Ramificazione sulla variabile frazionaria $x_1$ ($x_1^* = 2.25$):
    *   $P_1$: $x_1 \le 2$
    *   $P_2$: $x_1 \ge 3$

### 2. Livello 1 dell'Albero ($P_1, P_2$)
*   **Nodo $P_1$ ($x_1 \le 2$)**:
    *   Rilassamento continuo: $x^* = (2, 3.88)$, $Z_S(P_1) = 41.04$
    *   Stato: Poiché $Z_S(P_1) = 41.04 > 34$ e la soluzione non è intera, il nodo rimane aperto.
*   **Nodo $P_2$ ($x_1 \ge 3$)**:
    *   Rilassamento continuo: $x^* = (3, 3)$, $Z_S(P_2) = 39$
    *   Stato: La soluzione è a componenti intere.
    *   Aggiornamento incumbent: $Z_I = \max(34, 39) = 39$. Soluzione incombente aggiornata a $x_I = (3, 3)$.
    *   Il nodo $P_2$ viene **potato per ottimalità intera** (chiuso).
*   **Branching da $P_1$**: Ramificazione su $x_2$ ($x_2^* = 3.88$):
    *   $P_3$: $x_1 \le 2, \ x_2 \le 3$
    *   $P_4$: $x_1 \le 2, \ x_2 \ge 4$

### 3. Livello 2 dell'Albero ($P_3, P_4$)
*   **Nodo $P_3$ ($x_1 \le 2, x_2 \le 3$)**:
    *   Rilassamento continuo: $x^* = (2, 3)$, $Z_S(P_3) = 34$
    *   Stato: Poiché $Z_S(P_3) = 34 \le 39$ (incumbent), il nodo viene **potato per dominanza** (chiuso).
*   **Nodo $P_4$ ($x_1 \le 2, x_2 \ge 4$)**:
    *   Rilassamento continuo: $x^* = (1.8, 4)$, $Z_S(P_4) = 41$
    *   Stato: Poiché $Z_S(P_4) = 41 > 39$ e la soluzione non è intera, il nodo rimane aperto.
*   **Branching da $P_4$**: Ramificazione su $x_1$ ($x_1^* = 1.8$):
    *   $P_5$: $x_1 \le 1, \ x_2 \ge 4$
    *   $P_6$: $x_1 \ge 2, \ x_2 \ge 4$

### 4. Livello 3 dell'Albero ($P_5, P_6$)
*   **Nodo $P_5$ ($x_1 \le 1, x_2 \ge 4$)**:
    *   Rilassamento continuo: $x^* = (1, 4.44)$, $Z_S(P_5) = 40.52$
    *   Stato: Poiché $Z_S(P_5) = 40.52 > 39$ e la soluzione non è intera, il nodo rimane aperto.
*   **Nodo $P_6$ ($x_1 \ge 2, x_2 \ge 4$)**:
    *   Rilassamento continuo: Nessuna soluzione ammissibile (la combinazione $x_1 \ge 2, x_2 \ge 4$ viola il vincolo $5x_1 + 9x_2 \le 45$, dato che $10 + 36 = 46 > 45$).
    *   Stato: Il nodo viene **potato per inammissibilità** ($\emptyset$, chiuso).
*   **Branching da $P_5$**: Ramificazione su $x_2$ ($x_2^* = 4.44$):
    *   $P_7$: $x_1 \le 1, \ 4 \le x_2 \le 4 \implies x_2 = 4$
    *   $P_8$: $x_1 \le 1, \ x_2 \ge 5$

### 5. Livello 4 dell'Albero ($P_7, P_8$)
*   **Nodo $P_7$ ($x_1 \le 1, x_2 = 4$)**:
    *   Rilassamento continuo: $x^* = (1, 4)$, $Z_S(P_7) = 37$
    *   Stato: Poiché $Z_S(P_7) = 37 \le 39$ (incumbent), il nodo viene **potato per dominanza** (chiuso).
*   **Nodo $P_8$ ($x_1 \le 1, x_2 \ge 5$)**:
    *   Rilassamento continuo: $x^* = (0, 5)$, $Z_S(P_8) = 40$
    *   Stato: La soluzione è a componenti intere.
    *   Aggiornamento incumbent: $Z_I = \max(39, 40) = 40$. Soluzione incombente aggiornata a $x_I = (0, 5)$.
    *   Il nodo viene **potato per ottimalità intera** (chiuso).

### 6. Conclusione
Non vi sono altri nodi aperti nell'albero. 
*   **Soluzione ottima intera**: $x^* = (0, 5)$
*   **Valore ottimo**: $Z^* = 40$
