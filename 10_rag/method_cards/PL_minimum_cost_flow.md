---
type: method-card
topic: programmazione-lineare
status: draft
sources:
  - raw_assets/Programmazione Lineare/Ricerca Operativa - Introduzione a PL - 23-24.pdf
reliability: official
---

# Method Card — Formulare un problema di flusso a costo minimo

## Quando usarla
Quando il testo descrive una rete di distribuzione composta da nodi (sorgenti/fabbriche, destinazioni/magazzini, transiti/centri di smistamento) ed archi di collegamento con costi e capacità.

## Procedura da esame
1. **Definizione delle variabili**: Definire una variabile di flusso $x_{ij}$ per ogni arco orientato $(i,j)$ che unisce il nodo $i$ al nodo $j$.
2. **Definizione della funzione obiettivo**: Minimizzare il costo totale di spedizione:
   $$
   \min Z = \sum_{(i,j) \in A} c_{ij} x_{ij}
   $$
   dove $c_{ij}$ è il costo unitario di trasporto sull'arco $(i,j)$.
3. **Vincoli di bilancio di flusso nei nodi**: Per ogni nodo della rete, scrivere l'equazione di bilancio (flusso uscente - flusso entrante):
   - **Nodo Sorgente $i$** (con offerta $S_i$):
     $$
     \sum_{j: (i,j) \in A} x_{ij} - \sum_{k: (k,i) \in A} x_{ki} = S_i
     $$
   - **Nodo Destinazione $j$** (con domanda $D_j$):
     $$
     \sum_{k: (k,j) \in A} x_{kj} - \sum_{l: (j,l) \in A} x_{jl} = D_j
     $$
   - **Nodo di Transito $t$**:
     $$
     \sum_{j: (t,j) \in A} x_{tj} - \sum_{k: (k,t) \in A} x_{kt} = 0 \implies \text{flusso entrante} = \text{flusso uscente}
     $$
4. **Vincoli di capacità**: Per ogni arco $(i,j)$ capacitato:
   $$
   x_{ij} \le u_{ij}
   $$
5. **Vincoli di non negatività**:
   $$
   x_{ij} \ge 0 \qquad \forall (i,j) \in A
   $$
