# MC - Algoritmo Greedy per lo Zaino

## Quando Usarla
Per risolvere rapidamente il rilassamento continuo (valutazione superiore $Z_S$) o determinare una buona soluzione intera (valutazione inferiore $Z_I$) nei problemi dello zaino binario (knapsack).

## Procedura da Esame
1.  **Ordinamento**: Calcolare l'efficienza $e_j = v_j / p_j$ per ogni oggetto. Ordinare gli oggetti in senso decrescente di efficienza.
2.  **Soluzione Rilassata ($Z_S$)**: Inserire interi gli oggetti secondo l'ordinamento finché c'è capacità residua. Se l'oggetto successivo non entra interamente, inserirlo come frazione pari a:
    $$
    x_k = \frac{C_{\text{residuo}}}{p_k}
    $$
    Il valore complessivo ottenuto costituisce la valutazione superiore $Z_S$.
3.  **Soluzione Intera Greedy ($Z_I$)**: Inserire gli oggetti secondo l'ordinamento se il loro peso è inferiore o uguale alla capacità residua. Se non entrano, saltarli e passare al successivo. Il valore ottenuto è la valutazione inferiore.

## Mini Esempio
Capacità $C=8$. Oggetti ordinati: Obj 1 ($v=20, p=3$), Obj 2 ($v=11, p=2$), Obj 3 ($v=15, p=5$):
*   **Greedy Rilassato ($Z_S$)**:
    *   Inseriamo Obj 1 intero ($x_1=1$, cap residua 5, $Z=20$).
    *   Inseriamo Obj 2 intero ($x_2=1$, cap residua 3, $Z=31$).
    *   Inseriamo frazione di Obj 3 ($x_3=3/5=0.6$, cap residua 0).
    *   $Z_S = 31 + 15(0.6) = 40$.
*   **Greedy Intero ($Z_I$)**:
    *   Inseriamo Obj 1 ($x_1=1$, cap residua 5, $Z=20$).
    *   Inseriamo Obj 2 ($x_2=1$, cap residua 3, $Z=31$).
    *   Obj 3 non entra ($5 > 3 \implies x_3 = 0$).
    *   $Z_I = 31$.

## Errori Comuni
*   Sbagliare l'ordinamento degli oggetti (confondere peso e valore).
*   Nel calcolo intero, fermarsi al primo oggetto che non entra: si deve comunque controllare se gli oggetti successivi più leggeri possono essere inseriti nello spazio residuo.

## Fonti
*   `16_esercizi_BB.pdf`
