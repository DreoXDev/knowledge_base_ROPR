# MC - Flusso di Costo Minimo

## Quando Usarla
Per modellare la distribuzione e il trasporto di merci lungo una rete orientata con nodi di offerta, domanda e transito, minimizzando il costo complessivo e rispettando i limiti di capacità dei canali di trasporto.

## Variabili Tipiche
*   $x_{ij} \ge 0$ (intera): Quantità di flusso instradata sull'arco $(i, j)$.

## Modello Template
$$
\min \quad \sum_{(i,j) \in A} c_{ij} x_{ij}
$$
$$
\text{s.t.} \quad \sum_{j : (j, i) \in A} x_{ji} - \sum_{j : (i, j) \in A} x_{ij} = b_i \quad \forall i \in N
$$
$$
x_{ij} \le u_{ij} \quad \forall (i, j) \in A
$$
$$
x_{ij} \in \mathbb{Z}_+ \quad \forall (i, j) \in A
$$

## Procedura da Esame
1.  Rappresentare il problema come un grafo orientato.
2.  Calcolare e definire i bilanci $b_i$ per ciascun nodo $i$ (valori negativi per offerta, positivi per domanda, zero per transito).
3.  Verificare la condizione di bilanciamento globale: $\sum b_i = 0$.
4.  Scrivere i vincoli di conservazione del flusso nodo per nodo.
5.  Scrivere i vincoli di capacità superiore sugli archi $u_{ij}$ se presenti.

## Mini Esempio
Nodo 1 (offerta = 10, cioè $b_1 = -10$), Nodo 2 (transito, $b_2=0$), Nodo 3 (domanda = 10, cioè $b_3=10$).
Archi: $(1,2)$, $(2,3)$ con capacità $u_{12}=15, u_{23}=8$:
*   Vincolo Nodo 1: $-x_{12} = -10 \implies x_{12} = 10$
*   Vincolo Nodo 2: $x_{12} - x_{23} = 0$
*   Vincolo Nodo 3: $x_{23} = 10$
*   Capacità: $x_{12} \le 15, x_{23} \le 8$
*(Nota: questo mini esempio specifico è inammissibile poiché la capacità $u_{23}=8 < 10$)*.

## Errori Comuni
*   Dimenticare i vincoli di capacità superiore sugli archi.
*   Formulare vincoli di disuguaglianza per i bilanci dei nodi a meno che sia esplicitamente ammessa la perdita di flusso o l'insoddisfacimento della domanda.

## Fonti
*   `modelli_PLI.pdf`, Sezione 2.3
