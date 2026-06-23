# MC - Branch and Bound Binario

## Quando Usarla
Per risolvere in modo algoritmico e passo-passo problemi di Programmazione Lineare Intera a sole variabili binarie (0-1).

## Variabili Tipiche
*   $x_j \in \{0, 1\}$: Variabile decisionale binaria.
*   $Z_I$: Valore obiettivo della soluzione incombente (migliore intera ammissibile trovata).
*   $Z_C$: Valore ottimo del rilassamento continuo in un nodo.
*   $Z_S$: Upper Bound (valutazione superiore) del nodo.

## Procedura da Esame

### 1. Inizializzazione
1.  Poni la soluzione incombente $Z_I = -\infty$ (per problemi di massimo) o $Z_I = +\infty$ (per minimo).
2.  Risolvi il rilassamento continuo del problema completo $P_0$ imponendo $0 \le x_j \le 1$.
3.  Se la soluzione del rilassamento è intera, l'algoritmo termina immediatamente. Altrimenti, calcola il bound superiore $Z_S = Z_C$.
4.  **Arrotondamento all'Intero**: Se tutti i coefficienti della funzione obiettivo sono interi, applica:
    *   **Problemi di Massimo**: $Z_S = \lfloor Z_C \rfloor$
    *   **Problemi di Minimo**: $Z_S = \lceil Z_C \rceil$

### 2. Branching (Binarizzazione)
1.  Seleziona la variabile di branching seguendo l'ordinamento naturale delle variabili ($x_1, x_2, \dots$) o un'altra euristica specificata.
2.  Crea due nodi figli:
    *   Ramo sinistro: fissa la variabile a $0$.
    *   Ramo destro: fissa la variabile a $1$.

### 3. Valutazione e Potatura (Fathoming)
Per ciascun sotto-problema, risolvi il rilassamento continuo tenendo conto delle variabili fissate e determina il bound. Chiudi il nodo se:
*   **Inammissibilità ($\emptyset$)**: Il rilassamento continuo non ha soluzioni ammissibili.
*   **Ottimalità Intera**: La soluzione del rilassamento è binaria (integrità soddisfatta). Se $Z > Z_I$ (massimo), aggiorna $Z_I = Z$ e memorizza la soluzione.
*   **Dominanza**: Il bound del nodo (arrotondato) è inferiore o uguale all'incumbent corrente ($Z_S \le Z_I$ per massimo).

### 4. Selezione del Prossimo Nodo
*   **Depth First**: Scegli il nodo creato più di recente a livello più profondo.
*   **Best Bound**: Scegli il nodo aperto con il bound più promettente (più alto per massimo, più basso per minimo).

---

## Mini Esempio
Massimizzare $z = 9x_1 + 5x_2$ con $6x_1 + 3x_2 \le 7$ e $x_i \in \{0, 1\}$.
*   **Rilassamento continuo $P_0$**: $x^* = (2/3, 1)$ con $Z_C = 9(2/3) + 5(1) = 11$.
*   Poiché i coefficienti sono interi, il bound è $Z_S = 11$.
*   Branching su $x_1$:
    *   $x_1 = 0 \implies 3x_2 \le 7 \implies x^* = (0, 1)$ con $Z = 5$. Soluzione intera! Incumbent $Z_I = 5$.
    *   $x_1 = 1 \implies 6 + 3x_2 \le 7 \implies 3x_2 \le 1 \implies x_2 \le 1/3$. Soluzione rilassata $x^* = (1, 1/3)$ con $Z_C = 9 + 5(1/3) = 10.66 \implies Z_S = \lfloor 10.66 \rfloor = 10$.
    *   Branching su $x_1=1$:
        *   $x_1 = 1, x_2 = 0 \implies x^* = (1, 0)$ con $Z = 9$. Soluzione intera! Aggiorna incumbent $Z_I = 9$.
        *   $x_1 = 1, x_2 = 1 \implies 6 + 3 = 9 > 7$ (Inammissibile).
*   Ottimo intero: $x^* = (1, 0)$ con $z^* = 9$.

---

## Errori Comuni
*   **Arrotondamento errato**: Arrotondare i bound quando i coefficienti in funzione obiettivo sono frazionari.
*   **Direzione di arrotondamento**: Arrotondare per eccesso in massimizzazione o per difetto in minimizzazione.
*   **Vincoli di contingenza**: Dimenticare che fissare a $0$ una variabile primaria (es. $x_1 = 0$) costringe a $0$ anche la secondaria condizionata ($x_3 \le x_1 \implies x_3 = 0$) riducendo la dimensione dei rilassamenti.

## Fonti
*   `Programmazione Lineare Intera_Branch and Bound binario.pdf`, Pagine 8-18
