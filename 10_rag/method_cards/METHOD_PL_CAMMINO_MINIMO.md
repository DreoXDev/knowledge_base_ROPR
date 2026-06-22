---
type: method-card
topic: programmazione-lineare
status: draft
sources:
  - raw_assets/Programmazione Lineare/lec_w4_completa.pdf
reliability: official
---

# METHOD — Formulazione PL del cammino minimo

## Quando usarla
Usare questa card quando l'esercizio chiede di formulare il problema del cammino minimo su un grafo orientato pesato tra un nodo origine $s$ ed un nodo destinazione $t$.

## Descrizione del Modello

### 1. Variabili decisionali
Per ogni arco orientato $(i,j) \in A$ del grafo, si definisce la variabile binaria:

$$
x_{ij} \in \{0, 1\}
$$

dove $x_{ij} = 1$ se l'arco fa parte del cammino minimo, $0$ altrimenti.

### 2. Funzione Obiettivo
Minimizzare il costo complessivo (dove $c_{ij}$ è il costo dell'arco):

$$
\min Z = \sum_{(i,j)\in A} c_{ij}x_{ij}
$$

### 3. Vincoli (Conservazione del Flusso)
Scrivere le equazioni per ogni nodo della rete assumendo che entri 1 unità di flusso in $s$ ed esca 1 unità in $t$.

- **Nodo Origine $s$** (deve uscire il flusso unitario):
  $$
  \sum_{j:(s,j)\in A} x_{sj} - \sum_{k:(k,s)\in A} x_{ks} = 1
  $$
- **Nodo Destinazione $t$** (deve entrare il flusso unitario):
  $$
  \sum_{k:(k,t)\in A} x_{kt} - \sum_{l:(t,l)\in A} x_{tl} = 1
  $$
- **Nodi Intermedi $i \in N \setminus \{s,t\}$** (flusso entrante = flusso uscente):
  $$
  \sum_{j:(i,j)\in A} x_{ij} - \sum_{k:(k,i)\in A} x_{ki} = 0
  $$

## Formato di Risposta da Esame
1. Definire chiaramente il significato delle variabili binarie $x_{ij}$.
2. Scrivere la funzione di costo $\min Z$.
3. Elencare i vincoli di bilancio di flusso per ogni nodo del grafo (indicando chiaramente quali sono origine, destinazione e intermedi).
4. Indicare il dominio $x_{ij} \in \{0,1\}$.
