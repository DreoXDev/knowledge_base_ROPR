---
fonte: modelli_PLI.pdf
area: Programmazione Lineare Intera
priorita: alta
stato: completato
---

# PLI - Esempio Svolto: Flusso di Costo Minimo

## Fonte
`modelli_PLI.pdf`, Sezione 2.3 (Problemi su grafi)

## Descrizione del Problema
Data una rete rappresentata da un grafo orientato $G = (N, A)$, si vuole soddisfare la domanda o l'offerta di merci di ciascun nodo trasportandole lungo gli archi. Ad ogni arco $(i, j) \in A$ è associato un costo unitario di trasporto $c_{ij}$ e una capacità massima $u_{ij}$. Si vuole determinare il piano di flusso a costo totale minimo.

## Schema da Esame

### Indici e Insiemi
*   $N$: Insieme dei nodi.
*   $A$: Insieme degli archi orientati.

### Parametri
*   $c_{ij}$: Costo unitario di trasporto sull'arco $(i, j)$.
*   $u_{ij}$: Capacità massima di trasporto dell'arco $(i, j)$.
*   $b_i$: Bilancio del nodo $i$. Se $b_i < 0$, il nodo offre un quantitativo pari a $-b_i$. Se $b_i > 0$, il nodo richiede un quantitativo pari a $b_i$. Se $b_i = 0$, il nodo è di puro transito.

### Variabili Decisionali
*   $x_{ij} \ge 0$ (intera): Quantità di merce (flusso) inviata lungo l'arco $(i, j)$.

### Modello Matematico

$$
\min \quad \sum_{(i,j) \in A} c_{ij} x_{ij}
$$

Soggetto ai vincoli:

*   **Conservazione del flusso ai nodi**:
    $$
    \sum_{j : (j, i) \in A} x_{ji} - \sum_{j : (i, j) \in A} x_{ij} = b_i \quad \forall i \in N
    $$

*   **Capacità degli archi**:
    $$
    x_{ij} \le u_{ij} \quad \forall (i, j) \in A
    $$

*   **Dominio delle variabili**:
    $$
    x_{ij} \in \mathbb{Z}_+ \quad \forall (i, j) \in A
    $$

## Nota Teorica (Rilassamento Continuo)
Se la matrice di incidenza del grafo orientato è totalmente unimodulare (TUM) e sia $b_i$ che $u_{ij}$ sono interi, tutti i vertici del rilassamento continuo ($0 \le x_{ij} \le u_{ij}$) sono interi. Il problema può essere quindi risolto efficacemente tramite il metodo del simplesso.

## Errori da Evitare
*   Formulare il problema senza controllare che la rete sia bilanciata, ossia che $\sum_{i \in N} b_i = 0$. In caso contrario, il problema è intrinsecamente inammissibile.
*   Invertire la convenzione dei segni dei bilanci $b_i$.
*   Dimenticare i vincoli di capacità superiore $u_{ij}$ se esplicitati nella traccia.
