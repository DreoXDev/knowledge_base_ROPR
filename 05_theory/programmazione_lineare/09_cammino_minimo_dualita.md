---
type: theory-note
topic: programmazione-lineare
status: draft
sources:
  - raw_assets/Programmazione Lineare/lec_w4_completa.pdf
reliability: official
---

# Formulazione del Problema di Cammino Minimo

Il problema del cammino minimo consiste nel trovare il percorso di costo/lunghezza minima tra un nodo di origine $s$ ed un nodo di destinazione $t$ su un grafo orientato e pesato.

## Dati del Grafo

- Grafo orientato: $G(N, A)$, dove $N$ è l'insieme dei nodi e $A$ è l'insieme degli archi.
- $c_{ij}$: Costo, lunghezza o tempo associato ad ogni arco orientato $(i,j) \in A$.
- Nodo origine: $s \in N$.
- Nodo destinazione: $t \in N$.

## Variabili decisionali

Definiamo una variabile binaria per ciascun arco della rete:

$$
x_{ij} =
\begin{cases}
1 & \text{se l'arco } (i,j) \text{ appartiene al cammino minimo} \\
0 & \text{altrimenti}
\end{cases}
$$

## Funzione Obiettivo

Minimizzare la somma dei costi degli archi utilizzati:

$$
\min Z = \sum_{(i,j)\in A} c_{ij}x_{ij}
$$

## Vincoli di Conservazione del Flusso

Il problema si modella facendo circolare esattamente una unità di flusso dal nodo sorgente $s$ al nodo destinazione $t$. I vincoli impongono la conservazione di questa unità nei vari nodi della rete:

- **Nodo Origine $s$** (genera 1 unità di flusso uscente):
  $$
  \sum_{j:(s,j)\in A} x_{sj} - \sum_{k:(k,s)\in A} x_{ks} = 1
  $$
  *(Se non ci sono archi entranti in $s$, si riduce a: $\sum_{j:(s,j)\in A} x_{sj} = 1$)*

- **Nodo Destinazione $t$** (assorbe 1 unità di flusso):
  $$
  \sum_{k:(k,t)\in A} x_{kt} - \sum_{l:(t,l)\in A} x_{tl} = 1
  $$
  *(Se non ci sono archi uscenti da $t$, si riduce a: $\sum_{k:(k,t)\in A} x_{kt} = 1$)*

- **Nodi Intermedi $i \in N \setminus \{s,t\}$** (conservazione pura, flusso entrante = flusso uscente):
  $$
  \sum_{j:(i,j)\in A} x_{ij} - \sum_{k:(k,i)\in A} x_{ki} = 0
  $$

## Dominio

$$
x_{ij} \in \{0, 1\} \qquad \forall (i,j) \in A
$$

## Interpretazione
La formulazione matematica forza la costruzione di un percorso continuo: da $s$ deve uscire esattamente un arco attivo; in ciascun nodo intermedio toccato, l'arco in ingresso obbliga l'attivazione di esattamente un arco in uscita; il percorso si conclude necessariamente in $t$, dove deve giungere esattamente un arco attivo.

#ropr #programmazione-lineare #teoria #cammino-minimo #grafi
