---
type: theory
topic: programmazione_lineare_intera
status: active
sources: [modelli_PLI.pdf]
reliability: official
---

# Rilassamento Continuo e Totale Unimodularità

## Fonte
`modelli_PLI.pdf` (Mauro Passacantando)

## Idea Essenziale
In generale, risolvere un problema di PLI è computazionalmente difficile (NP-hard). Tuttavia, se la matrice dei coefficienti dei vincoli possiede una struttura matematica particolare detta **totale unimodularità** e il vettore dei termini noti è intero, i vertici del poliedro del rilassamento continuo sono interi. Questo consente di trovare la soluzione ottima intera risolvendo semplicemente il rilassamento continuo con il metodo del simplesso.

## Matrice Totalmente Unimodulare (TUM)
Una matrice $A$ di dimensioni $m \times n$ si dice **totalmente unimodulare** (TUM) se il determinante di ogni sua sottomatrice quadrata (di qualsiasi dimensione) appartiene all'insieme $\{-1, 0, 1\}$.

Da questa definizione discendono due proprietà immediate:
1.  Tutti gli elementi di una matrice TUM devono appartenere a $\{-1, 0, 1\}$.
2.  La trasposta $A^T$ di una matrice TUM è anch'essa TUM.

## Teorema dei Vertici Interi (Hoffman-Kruskal)
Sia $A$ una matrice totalmente unimodulare e sia $b \in \mathbb{Z}^m$ un vettore intero. Allora, tutti i punti estremi (vertici) del poliedro:

$$
P = \{x \in \mathbb{R}^n : Ax \le b, x \ge 0\}
$$

sono interi (ossia appartengono a $\mathbb{Z}^n$). 

Questo implica che, se il rilassamento continuo di un problema PLI con tali vincoli ha una soluzione ottima, il simplesso (che lavora sempre sui vertici del poliedro) restituirà una soluzione intera che è ottima anche per il problema intero originale.

## Condizione Sufficiente per la Totale Unimodularità su Grafi
Una matrice di incidenza nodo-arco $M$ di un grafo orientato è totalmente unimodulare.
Per un grafo orientato $(N, A)$, la matrice di incidenza nodo-arco $M$ ha una riga per ciascun nodo e una colonna per ciascun arco. Per la colonna associata all'arco $(i, j)$:
*   L'elemento corrispondente alla riga del nodo di origine $i$ vale $-1$.
*   L'elemento corrispondente alla riga del nodo di destinazione $j$ vale $1$.
*   Tutti gli altri elementi valgono $0$.

Qualsiasi matrice con questa struttura è TUM. Pertanto, i problemi formulati come flussi su rete con termini noti (bilanci e capacità) interi ereditano questa proprietà.

## Applicazioni Principali
I seguenti problemi su grafo possono essere risolti all'ottimo tramite il rilassamento continuo se i dati (domande, offerte, bilanci) sono interi:
1.  **Assegnamento di Costo Minimo**: Formulato su grafo bipartito.
2.  **Cammino di Costo Minimo**: Formulato con bilanci dei nodi $b_s = -1$, $b_t = 1$, $b_i = 0$ per nodi intermedi.
3.  **Flusso di Costo Minimo**: Con equazioni di conservazione del flusso ai nodi.

## Warning Teorico
> [!WARNING]
> La totale unimodularità garantisce che tutti i **vertici** del poliedro siano interi. Se il rilassamento continuo presenta ottimi multipli, una combinazione convessa di tali vertici ottimi potrebbe non essere intera. Il metodo del simplesso garantisce una soluzione intera poiché restituisce sempre una soluzione di base (ossia un vertice). Altri metodi (es. metodi a punti interni) potrebbero restituire soluzioni non intere pur in presenza di matrici TUM.
