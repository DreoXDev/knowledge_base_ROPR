---
materia: ROPR
area: Programmazione Lineare
tipo: metodo
fonte: esercitazione1_complete.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - formulazione
  - trasporto
  - distribuzione
  - method-card
---

# METHOD CARD — Problemi di Trasporto (Reti di Distribuzione)

## Quando usarla

Usare questa card quando la traccia richiede di modellare il trasferimento ottimale di merci da un insieme di nodi di origine (fabbriche, stabilimenti, magazzini di offerta) ad un insieme di nodi di destinazione (clienti, negozi, centri di domanda) al minimo costo.

---

## Struttura Matematica del Modello

### 1. Insiemi e Indici
- $I = \{1, \dots, m\}$: insieme delle origini/stabilimenti ($i \in I$).
- $J = \{1, \dots, n\}$: insieme delle destinazioni/magazzini ($j \in J$).

### 2. Parametri (Dati)
- $s_i$: offerta massima (capacità produttiva) disponibile all'origine $i$.
- $d_j$: domanda minima richiesta dalla destinazione $j$.
- $c_{ij}$: costo unitario di trasporto per spostare una unità di merce da $i$ a $j$.

### 3. Variabili decisionali
Sia $x_{ij}$ la quantità di prodotto trasportata dall'origine $i$ alla destinazione $j$:
$$
x_{ij} \ge 0 \qquad \forall i \in I, j \in J
$$

### 4. Funzione Obiettivo
Minimizzare il costo totale di trasporto:
$$
\min Z = \sum_{i \in I} \sum_{j \in J} c_{ij} x_{ij}
$$

### 5. Vincoli

- **Vincoli di offerta** (non si può spedire da un'origine $i$ più merce della sua capacità):
  $$
  \sum_{j \in J} x_{ij} \le s_i \qquad \forall i \in I
  $$
- **Vincoli di domanda** (ogni destinazione $j$ deve ricevere almeno la quantità richiesta):
  $$
  \sum_{i \in I} x_{ij} \ge d_j \qquad \forall j \in J
  $$

---

## Il Caso Bilanciato

> [!NOTE]
> Se la somma delle capacità di offerta è esattamente pari alla somma delle domande:
> $$
> \sum_{i \in I} s_i = \sum_{j \in J} d_j
> $$
> il problema si definisce **bilanciato**. 
> 
> In questo caso, le relazioni di disuguaglianza nei vincoli possono essere scritte direttamente come **uguaglianze ($=$)**:
> $$
> \sum_{j \in J} x_{ij} = s_i \qquad \forall i \in I
> $$
> $$
> \sum_{i \in I} x_{ij} = d_j \qquad \forall j \in J
> $$
