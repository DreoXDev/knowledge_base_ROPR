---
fonte: 16_esercizi_BB.pdf
area: Programmazione Lineare Intera
priorita: alta
stato: completato
---

# PLI - Esempio Svolto 2: B&B su Zaino Binario

## Fonte
`16_esercizi_BB.pdf`, Esercizio 12

## Descrizione del Problema
Risolvere il seguente problema dello zaino binario con il metodo Branch and Bound, visitando l'albero in ampiezza ed istanziando le variabili frazionarie del rilassamento continuo. I bound sono calcolati tramite l'algoritmo greedy.

*   **Oggetti**: $N = \{1, 2, 3, 4\}$
*   **Valori**: $v = (15, 11, 20, 10)$
*   **Pesi**: $p = (5, 2, 3, 4)$
*   **Capacità**: $C = 8$

## Risoluzione Passo-Passo

### 1. Calcolo dei Rendimenti e Ordinamento Greedy
Calcolo del rendimento specifico $e_j = v_j / p_j$ per ciascun oggetto:
*   Oggetto 1: $e_1 = 15 / 5 = 3.0$
*   Oggetto 2: $e_2 = 11 / 2 = 5.5$
*   Oggetto 3: $e_3 = 20 / 3 = 6.67$
*   Oggetto 4: $e_4 = 10 / 4 = 2.5$

Ordinamento decrescente di efficienza: **Oggetto 3, Oggetto 2, Oggetto 1, Oggetto 4**.

---

### 2. Nodo Radice ($P$)
*   **Valutazione Inferiore (Greedy Intero - $Z_I$)**:
    *   Inseriamo Obj 3 (peso 3, cap residua 5, $Z = 20$)
    *   Inseriamo Obj 2 (peso 2, cap residua 3, $Z = 31$)
    *   Obj 1 (peso 5 > 3) non entra; Obj 4 (peso 4 > 3) non entra.
    *   Soluzione intera incombente: $x_I = (0, 1, 1, 0)$ con $Z_I = 31$.
*   **Valutazione Superiore (Rilassamento Continuo Greedy - $Z_S$)**:
    *   Inseriamo Obj 3 (peso 3, cap residua 5)
    *   Inseriamo Obj 2 (peso 2, cap residua 3)
    *   Inseriamo Obj 1 frazionario: $x_1 = 3 / 5 = 0.6$
    *   $Z_S(P) = 20 + 11 + 15(0.6) = 40$.
    *   Soluzione rilassamento: $x^* = (0.6, 1, 1, 0)$ con $Z_S(P) = 40$.
*   Poiché la soluzione è frazionaria e $Z_S(P) = 40 > 31$, il nodo rimane aperto.
*   **Branching su $x_1$**:
    *   $P_1$: $x_1 = 0$
    *   $P_2$: $x_1 = 1$

---

### 3. Livello 1 dell'Albero ($P_1, P_2$)
*   **Nodo $P_1$ ($x_1 = 0$)**:
    *   Oggetti disponibili: 3, 2, 4. Capacità residua: 8.
    *   Rilassamento continuo:
        *   Inseriamo Obj 3 (peso 3, cap 5)
        *   Inseriamo Obj 2 (peso 2, cap 3)
        *   Inseriamo Obj 4 frazionario: $x_4 = 3 / 4 = 0.75$
        *   $x^* = (0, 1, 1, 0.75)$, $Z_S(P_1) = 20 + 11 + 10(0.75) = 38.5$.
    *   Stato: Poiché $Z_S(P_1) = 38.5 > 31$ e non è intero, il nodo rimane aperto.
*   **Nodo $P_2$ ($x_1 = 1$)**:
    *   Oggetti disponibili: 3, 2, 4. Capacità residua: $8 - 5 = 3$.
    *   Rilassamento continuo:
        *   Inseriamo Obj 3 (peso 3, cap 0, $Z = 15 + 20 = 35$)
        *   Obj 2 e Obj 4 non entrano ($x_2=0, x_4=0$).
        *   $x^* = (1, 0, 1, 0)$, $Z_S(P_2) = 35$.
    *   Stato: La soluzione è intera.
    *   Aggiornamento incumbent: $Z_I = \max(31, 35) = 35$. Soluzione incombente: $x_I = (1, 0, 1, 0)$.
    *   Il nodo viene **potato per ottimalità intera** (chiuso).
*   **Branching da $P_1$**: Ramificazione su $x_4$ ($x_4^* = 0.75$):
    *   $P_3$: $x_1 = 0, \ x_4 = 0$
    *   $P_4$: $x_1 = 0, \ x_4 = 1$

---

### 4. Livello 2 dell'Albero ($P_3, P_4$)
*   **Nodo $P_3$ ($x_1 = 0, x_4 = 0$)**:
    *   Oggetti disponibili: 3, 2. Capacità residua: 8.
    *   Rilassamento continuo: Inseriamo Obj 3 e Obj 2 interamente $\implies x^* = (0, 1, 1, 0)$, $Z_S(P_3) = 31$.
    *   Stato: Poiché $Z_S(P_3) = 31 \le 35$ (incumbent), il nodo viene **potato per dominanza** (chiuso).
*   **Nodo $P_4$ ($x_1 = 0, x_4 = 1$)**:
    *   Oggetti disponibili: 3, 2. Capacità residua: $8 - 4 = 4$.
    *   Rilassamento continuo:
        *   Inseriamo Obj 3 (peso 3, cap residua 1)
        *   Inseriamo Obj 2 frazionario: $x_2 = 1 / 2 = 0.5$
        *   $x^* = (0, 0.5, 1, 1)$, $Z_S(P_4) = 10 + 20 + 11(0.5) = 35.5$.
    *   Stato: Poiché $Z_S(P_4) = 35.5 > 35$ e non è intero, il nodo rimane aperto.
*   **Branching da $P_4$**: Ramificazione su $x_2$ ($x_2^* = 0.5$):
    *   $P_5$: $x_1 = 0, \ x_4 = 1, \ x_2 = 0$
    *   $P_6$: $x_1 = 0, \ x_4 = 1, \ x_2 = 1$

---

### 5. Livello 3 dell'Albero ($P_5, P_6$)
*   **Nodo $P_5$ ($x_1 = 0, x_4 = 1, x_2 = 0$)**:
    *   Oggetti disponibili: 3. Capacità residua: 4.
    *   Rilassamento continuo: Inseriamo Obj 3 $\implies x^* = (0, 0, 1, 1)$, $Z_S(P_5) = 20 + 10 = 30$.
    *   Stato: Poiché $Z_S(P_5) = 30 \le 35$ (incumbent), il nodo viene **potato per dominanza** (chiuso).
*   **Nodo $P_6$ ($x_1 = 0, x_4 = 1, x_2 = 1$)**:
    *   Oggetti disponibili: 3. Capacità residua: $8 - 4 - 2 = 2$.
    *   Rilassamento continuo: Inseriamo Obj 3 frazionario: $x_3 = 2 / 3 = 0.67$.
    *   $x^* = (0, 1, 0.67, 1)$, $Z_S(P_6) = 10 + 11 + 20(2/3) = 34.33$.
    *   Stato: Poiché $Z_S(P_6) = 34.33 \le 35$ (incumbent), il nodo viene **potato per dominanza** (chiuso).

---

### 6. Conclusione
Tutti i nodi dell'albero sono stati chiusi.
*   **Soluzione ottima intera**: $x^* = (1, 0, 1, 0)$ (ossia inserire gli oggetti 1 e 3)
*   **Valore ottimo**: $Z^* = 35$
*   **Peso totale**: $p_1 + p_3 = 5 + 3 = 8$ (capienza sfruttata al 100%).
