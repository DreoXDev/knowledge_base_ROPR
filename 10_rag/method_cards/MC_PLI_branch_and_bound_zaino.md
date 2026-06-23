# Method Card: Branch and Bound Zaino Binario (visita in ampiezza)

## Quando usarla
Da usare per risolvere il problema dello zaino binario (knapsack 0/1) con il metodo del Branch and Bound ed una strategia di visita in ampiezza (Breadth-First) dei nodi dell'albero di decisione.

## Input tipico dell'esercizio
- Funzione obiettivo di massimizzazione: $\max \sum v_i x_i$.
- Vincolo di capacità: $\sum p_i x_i \le C$.
- Dominio binario: $x_i \in \{0, 1\}$.

## Procedura in 5 passi
1.  **Ordinamento**: Ordinare gli elementi per efficienza decrescente:
    $$\frac{v_1}{p_1} \ge \frac{v_2}{p_2} \ge \dots \ge \frac{v_n}{p_n}$$
2.  **Rilassamento Continuo (Bounding)**: Inserire gli elementi nello zaino uno alla volta in ordine di efficienza. Se l'elemento successivo supera la capacità residua, inserirlo parzialmente (frazione $\alpha$). Il bound superiore rilassato è:
    $$Z_{rel} = \sum_{\text{interi}} v_i + \alpha v_{\text{fraz}}$$
    L'upper bound intero è $UB = \lfloor Z_{rel} \rfloor$ se i coefficienti di valore sono interi.
3.  **Branching**: Eseguire la ramificazione sulla variabile frazionaria del rilassamento, creando due rami: $x_k = 0$ e $x_k = 1$.
4.  **Visita in Ampiezza**: Valutare tutti i nodi di un livello prima di passare al successivo. Se un nodo produce una soluzione intera ammissibile, registrare il suo valore come incumbent $Z_I$ (se maggiore di quello corrente).
5.  **Regole di Potatura (Fathoming)**:
    -   **Interezza**: Il rilassamento continuo fornisce una soluzione intera.
    -   **Dominanza**: Il bound rilassato del nodo è peggiore o uguale all'incumbent corrente ($UB \le Z_I$ per massimizzazione).
    -   **Inammissibilità**: Il sotto-problema non ha soluzioni ammissibili (es. la somma dei pesi delle variabili fissate a 1 supera la capacità $C$).

## Errori frequenti
-   **Non ordinare gli elementi**: Provare a fare la risoluzione greedy o il rilassamento senza aver prima ordinato gli elementi per efficienza $v_i/p_i$.
-   **Ordinamento errato degli indici**: Dimenticare di mappare le variabili agli indici ordinati durante la scrittura dei rami o del risultato.
-   **Sbagliare la visita in ampiezza**: Confondere la visita in ampiezza (Breadth-First) con il Best-Bound-First o il Depth-First. In ampiezza, si espandono tutti i nodi aperti a livello $k$ prima di scendere a $k+1$.
