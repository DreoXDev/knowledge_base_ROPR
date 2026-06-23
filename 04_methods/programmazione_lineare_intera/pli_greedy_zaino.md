---
type: method
topic: programmazione_lineare_intera
status: active
sources: [16_esercizi_BB.pdf]
reliability: official
---

# Algoritmo Greedy e Bound per il Problema dello Zaino

## Quando Usarla
Nei problemi dello zaino (knapsack) binario per calcolare rapidamente valutazioni inferiori (tramite euristica intera greedy) e valutazioni superiori (risolvendo il rilassamento continuo con metodo greedy) all'inizio o all'interno dei nodi del Branch and Bound.

## Procedura Passo-Passo

Sia dato un problema dello zaino:
$$
\max \sum_{j=1}^n v_j x_j \quad \text{s.t.} \quad \sum_{j=1}^n p_j x_j \le C, \quad x_j \in \{0, 1\}
$$

### Passo 1: Ordinamento degli Oggetti
Calcolare il rendimento specifico (efficienza) per ciascun oggetto $j$:
$$
e_j = \frac{v_j}{p_j}
$$
Ordinare gli oggetti in senso decrescente di efficienza. Per comodità di scrittura, rinominare gli oggetti in modo che:
$$
\frac{v_1}{p_1} \ge \frac{v_2}{p_2} \ge \dots \ge \frac{v_n}{p_n}
$$

### Passo 2: Valutazione Inferiore (Greedy Intero - $Z_I$)
L'euristica greedy intera inserisce gli oggetti nello zaino seguendo l'ordinamento decrescente, a patto che ci sia spazio residuo.
1.  Inizializzare lo spazio residuo $C_{\text{residuo}} = C$, il valore corrente $Z_I = 0$ e la soluzione $x = (0, \dots, 0)$.
2.  Per ciascun oggetto $j = 1, \dots, n$ (in ordine di efficienza):
    *   Se $p_j \le C_{\text{residuo}}$:
        *   Inserire l'oggetto: $x_j = 1$.
        *   Aggiornare: $C_{\text{residuo}} = C_{\text{residuo}} - p_j$.
        *   Aggiornare: $Z_I = Z_I + v_j$.
    *   Se $p_j > C_{\text{residuo}}$:
        *   Non inserire l'oggetto: $x_j = 0$ (e procedere con l'oggetto successivo per vedere se ne entra uno più leggero).
3.  La soluzione $x$ ottenuta è ammissibile per il problema intero. Il valore $Z_I$ è la valutazione inferiore del valore ottimo intero.

### Passo 3: Valutazione Superiore (Rilassamento Continuo Greedy - $Z_S$)
La soluzione ottima del rilassamento continuo dello zaino si ottiene riempiendo lo zaino con gli oggetti in ordine di efficienza. A differenza del caso intero, l'oggetto che supera la capacità viene inserito come frazione per saturare esattamente lo zaino.
1.  Inizializzare la capacità rimanente $C_{\text{rim}} = C$, il valore $Z_S = 0$ e $x = (0, \dots, 0)$.
2.  Per ciascun oggetto $j = 1, \dots, n$ (in ordine di efficienza):
    *   Se $p_j \le C_{\text{rim}}$:
        *   Inserire interamente: $x_j = 1$.
        *   Aggiornare: $C_{\text{rim}} = C_{\text{rim}} - p_j$.
        *   Aggiornare: $Z_S = Z_S + v_j$.
    *   Se $p_j > C_{\text{rim}}$ e $C_{\text{rim}} > 0$:
        *   Inserire la frazione residua:
            $$
            x_j = \frac{C_{\text{rim}}}{p_j}
            $$
        *   Aggiornare: $Z_S = Z_S + v_j \cdot x_j$.
        *   Porre $C_{\text{rim}} = 0$.
    *   Se $C_{\text{rim}} = 0$:
        *   Oggetti restanti: $x_j = 0$.
3.  La soluzione $x$ è l'ottimo del rilassamento continuo. Il valore $Z_S$ è la valutazione superiore.

## Mini Esempio
Capacità $C=8$. Oggetti:
1.  $v_1=15, p_1=5 \implies e_1 = 3.0$
2.  $v_2=11, p_2=2 \implies e_2 = 5.5$
3.  $v_3=20, p_3=3 \implies e_3 = 6.67$
4.  $v_4=10, p_4=4 \implies e_4 = 2.5$

Ordinamento: Oggetto 3 ($6.67$), Oggetto 2 ($5.5$), Oggetto 1 ($3.0$), Oggetto 4 ($2.5$).

### Calcolo Greedy Intero ($Z_I$)
1.  Inserisco 3: peso 3, cap residua 5, $Z_I=20$. Solution: $x_3=1$.
2.  Inserisco 2: peso 2, cap residua 3, $Z_I=20+11=31$. Solution: $x_2=1$.
3.  Provo 1: peso 5 > 3 (non entra). Solution: $x_1=0$.
4.  Provo 4: peso 4 > 3 (non entra). Solution: $x_4=0$.
*   Soluzione intera: $x = (0, 1, 1, 0)$ con $Z_I = 31$.

### Calcolo Rilassamento Continuo ($Z_S$)
1.  Inserisco 3: peso 3, cap residua 5, $Z_S=20$. Solution: $x_3=1$.
2.  Inserisco 2: peso 2, cap residua 3, $Z_S=20+11=31$. Solution: $x_2=1$.
3.  Inserisco frazione di 1: peso 5, cap residua 3 $\implies x_1 = 3/5 = 0.6$.
    *   $Z_S = 31 + 15 \cdot 0.6 = 31 + 9 = 40$.
*   Soluzione rilassamento: $x = (0.6, 1, 1, 0)$ con $Z_S = 40$.
