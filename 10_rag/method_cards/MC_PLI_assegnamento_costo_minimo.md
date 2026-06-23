# MC - Assegnamento di Costo Minimo

## Quando Usarla
Per abbinare in modo univoco elementi di due insiemi di pari cardinalità (es. lavoratori ad attività, macchine a compiti) in modo da minimizzare il costo o tempo totale.

## Variabili Tipiche
*   $x_{ij} \in \{0, 1\}$: Vale $1$ se l'elemento $i$ del primo insieme viene assegnato all'elemento $j$ del secondo insieme, $0$ altrimenti.

## Modello Template
$$
\min \quad \sum_{i \in I} \sum_{j \in J} c_{ij} x_{ij}
$$
$$
\text{s.t.} \quad \sum_{j \in J} x_{ij} = 1 \quad \forall i \in I
$$
$$
\sum_{i \in I} x_{ij} = 1 \quad \forall j \in J
$$
$$
x_{ij} \in \{0, 1\} \quad \forall i \in I, \forall j \in J
$$

## Procedura da Esame
1.  Riconoscere la struttura bipartita del problema.
2.  Definire la matrice dei costi $c_{ij}$.
3.  Scrivere i vincoli di riga (ogni elemento del primo insieme ha esattamente un assegnamento).
4.  Scrivere i vincoli di colonna (ogni elemento del secondo insieme riceve esattamente un assegnamento).
5.  Notare che la matrice dei vincoli è TUM, quindi il rilassamento continuo ha vertici interi.

## Mini Esempio
Assegnare 2 lavoratori a 2 attività con costi $c_{11}=5, c_{12}=9, c_{21}=8, c_{22}=4$:
$$
\min \quad 5 x_{11} + 9 x_{12} + 8 x_{21} + 4 x_{22}
$$
$$
\text{s.t.} \quad x_{11} + x_{12} = 1
$$
$$
x_{21} + x_{22} = 1
$$
$$
x_{11} + x_{21} = 1
$$
$$
x_{12} + x_{22} = 1
$$
$$
x_{ij} \in \{0, 1\}
$$

## Errori Comuni
*   Usare vincoli $\le 1$ o $\ge 1$ al posto di vincoli di uguaglianza $= 1$, il che potrebbe portare ad assegnamenti parziali o nulli se non ci sono vincoli stringenti.

## Fonti
*   `modelli_PLI.pdf`, Sezione 2.1
