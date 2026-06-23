---
fonte: modelli_PLI.pdf
area: Programmazione Lineare Intera
priorita: alta
stato: completato
---

# PLI - Esempio Svolto: Cammino di Costo Minimo

## Fonte
`modelli_PLI.pdf`, Sezione 2.2 (Problemi su grafi)

## Descrizione del Problema
Trovare il cammino a costo minimo da un nodo sorgente $s$ a un nodo destinazione $t$ in un grafo orientato $G = (N, A)$ dove ad ogni arco $(i, j) \in A$ è associato un costo $c_{ij}$.

## Schema da Esame

### Indici e Insiemi
*   $N$: Insieme dei nodi del grafo.
*   $A$: Insieme degli archi orientati, con $A \subseteq N \times N$.
*   $s \in N$: Nodo sorgente (origine).
*   $t \in N$: Nodo destinazione (arrivo).

### Parametri
*   $c_{ij}$: Costo di percorrenza dell'arco $(i, j)$.

### Variabili Decisionali
*   $x_{ij} \in \{0, 1\}$: Vale $1$ se l'arco $(i, j)$ fa parte del cammino minimo, $0$ altrimenti.

### Modello Matematico

$$
\min \quad \sum_{(i,j) \in A} c_{ij} x_{ij}
$$

Soggetto ai vincoli:

*   **Conservazione del flusso ai nodi**:
    $$
    \sum_{j : (j, i) \in A} x_{ji} - \sum_{j : (i, j) \in A} x_{ij} = b_i \quad \forall i \in N
    $$
    
    dove:
    $$
    b_i = \begin{cases}
    -1 & \text{se } i = s \text{ (sorgente)} \\
    1 & \text{se } i = t \text{ (destinazione)} \\
    0 & \text{altrimenti (nodi intermedi)}
    \end{cases}
    $$

*   **Dominio delle variabili**:
    $$
    x_{ij} \in \{0, 1\} \quad \forall (i, j) \in A
    $$

## Nota Teorica (Rilassamento Continuo)
La matrice dei vincoli è la matrice di incidenza nodo-arco del grafo, che è totalmente unimodulare (TUM). Se i costi $c_{ij}$ sono non negativi, il problema intero può essere risolto trovando un vertice ottimo del rilassamento continuo ($0 \le x_{ij} \le 1$), il quale sarà intero.

## Errori da Evitare
*   Confondere i segni del bilancio: se usi $\text{flusso entrante} - \text{flusso uscente}$, il nodo sorgente deve avere bilancio $-1$ (poiché produce flusso uscente) e il nodo destinazione $+1$. Se usi $\text{flusso uscente} - \text{flusso entrante}$, i segni si invertono.
*   Scrivere vincoli per nodi che non appartengono al grafo.
*   Dimenticare i vincoli di non negatività o integrità sulle variabili.
