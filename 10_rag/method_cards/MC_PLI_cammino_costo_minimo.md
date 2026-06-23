# MC - Cammino di Costo Minimo come PLI

## Quando Usarla
Per determinare il percorso ottimale tra un nodo origine $s$ e un nodo destinazione $t$ su un grafo orientato, minimizzando la somma dei pesi degli archi attraversati.

## Variabili Tipiche
*   $x_{ij} \in \{0, 1\}$: Vale $1$ se l'arco orientato $(i, j)$ appartiene al cammino ottimo, $0$ altrimenti.

## Modello Template
$$
\min \quad \sum_{(i,j) \in A} c_{ij} x_{ij}
$$
$$
\text{s.t.} \quad \sum_{j : (j, i) \in A} x_{ji} - \sum_{j : (i, j) \in A} x_{ij} = b_i \quad \forall i \in N
$$
$$
x_{ij} \in \{0, 1\} \quad \forall (i, j) \in A
$$
dove:
$$
b_i = \begin{cases}
-1 & \text{se } i = s \\
1 & \text{se } i = t \\
0 & \text{altrimenti}
\end{cases}
$$

## Procedura da Esame
1.  Identificare i nodi $N$, gli archi $A$, la sorgente $s$, la destinazione $t$ e i costi $c_{ij}$.
2.  Definire le variabili binarie $x_{ij}$.
3.  Scrivere l'equazione di bilancio per ciascun nodo $i \in N$ (flusso entrante meno flusso uscente = bilancio del nodo).
4.  Dichiarare il dominio binario $x_{ij} \in \{0, 1\}$.

## Mini Esempio
Grafo con nodi $\{1, 2, 3\}$, sorgente $s=1$, destinazione $t=3$. Archi: $(1,2)$, $(2,3)$, $(1,3)$:
*   Nodo 1 (Sorgente): $x_{21} - x_{12} - x_{13} = -1 \implies x_{12} + x_{13} - x_{21} = 1$
*   Nodo 2 (Intermedio): $x_{12} - x_{23} = 0 \implies x_{12} = x_{23}$
*   Nodo 3 (Destinazione): $x_{13} + x_{23} = 1$

## Errori Comuni
*   Invertire i segni dei bilanci tra sorgente e destinazione.
*   Dimenticare i flussi entranti o uscenti per i nodi intermedi.

## Fonti
*   `modelli_PLI.pdf`, Sezione 2.2
