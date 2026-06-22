---
topic: Programmazione Lineare
type: esempio_svolto
source: lec_w4_completa.pdf
status: verificato
---

# Esempio Svolto — Formulazione Cammino Minimo su Grafo

## Traccia Sintetica
Dato il grafo orientato pesato $G(N,A,c)$ con nodo origine $s \in N$ e nodo destinazione $t \in N$. Formulare il problema di cammino minimo da $s$ a $t$ come modello di programmazione lineare.

## Formulazione Matematica

### Dati della rete
- $N$: insieme dei nodi
- $A$: insieme degli archi orientati $(i,j)$
- $c_{ij}$: costo/lunghezza dell'arco $(i,j) \in A$
- $s$: nodo sorgente (origine)
- $t$: nodo destinazione

### Variabili decisionali
Per ogni arco $(i,j) \in A$, definiamo la variabile binaria:

$$
x_{ij} =
\begin{cases}
1 & \text{se l'arco } (i,j) \text{ è parte del cammino minimo} \\
0 & \text{altrimenti}
\end{cases}
$$

### Funzione Obiettivo
Minimizzare il costo totale del cammino:

$$
\min Z = \sum_{(i,j)\in A} c_{ij}x_{ij}
$$

### Vincoli di Bilancio (Conservazione del Flusso)
- **Nodo Origine $s$** (deve uscire esattamente un arco attivo):
  $$
  \sum_{j:(s,j)\in A} x_{sj} - \sum_{k:(k,s)\in A} x_{ks} = 1
  $$
- **Nodo Destinazione $t$** (deve entrare esattamente un arco attivo):
  $$
  \sum_{k:(k,t)\in A} x_{kt} - \sum_{l:(t,l)\in A} x_{tl} = 1
  $$
- **Nodi Intermedi $i \in N \setminus \{s,t\}$** (il flusso entrante deve uguagliare il flusso uscente):
  $$
  \sum_{j:(i,j)\in A} x_{ij} - \sum_{k:(k,i)\in A} x_{ki} = 0 \qquad \forall i \in N \setminus \{s,t\}
  $$

### Dominio

$$
x_{ij} \in \{0, 1\} \qquad \forall (i,j) \in A
$$

## Risposta da Esame
Il modello del cammino minimo è:
$\min \sum_{(i,j)\in A} c_{ij}x_{ij}$
soggetto a:
- $\sum_{j:(s,j)\in A} x_{sj} - \sum_{k:(k,s)\in A} x_{ks} = 1$
- $\sum_{k:(k,t)\in A} x_{kt} - \sum_{l:(t,l)\in A} x_{tl} = 1$
- $\sum_{j:(i,j)\in A} x_{ij} - \sum_{k:(k,i)\in A} x_{ki} = 0 \quad \forall i \in N \setminus \{s,t\}$
- $x_{ij} \in \{0, 1\} \quad \forall (i,j) \in A$.
