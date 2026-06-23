---
type: flashcards
topic: programmazione_lineare
status: consolidated
sources:
  - raw_assets/Domande aperte RO.pdf
reliability: non-ufficiale
---

# Flashcard — Domande Aperte Reti (Trasporto, Flussi)

---

## Q1: Bilanciamento trasporto — offerta > domanda
**D:** Come si bilancia un problema di trasporto con offerta maggiore della domanda?

**R:** Si aggiunge una **destinazione fittizia** con domanda pari al surplus ($\sum s_i - \sum d_j$) e costi di trasporto nulli.

---

## Q2: Variabile del problema di trasporto
**D:** Qual è la variabile decisionale del problema di trasporto?

**R:** $x_{ij}$ = quantità spedita dalla sorgente $i$ alla destinazione $j$, con $x_{ij} \ge 0$.

---

## Q3: Vincolo di bilanciamento del flusso
**D:** Qual è il vincolo principale nei problemi di flusso su rete?

**R:** Il **bilanciamento del flusso** in ogni nodo:
$$\sum_{(v,j)} x_{vj} - \sum_{(i,v)} x_{iv} = b_v$$

---

## Q4: Trasporto vs flusso a costo minimo
**D:** Il problema di trasporto è un caso speciale di quale problema?

**R:** Del **problema di flusso a costo minimo** (grafo bipartito, nessuna capacità superiore).

---

## Q5: Massimo flusso — funzione obiettivo
**D:** Qual è la funzione obiettivo del problema di massimo flusso?

**R:** $\max f$, dove $f$ è il flusso netto in uscita dalla sorgente $s$.

---

## Q6: Cammino minimo — variabili
**D:** Quali sono le variabili nel problema di cammino di costo minimo?

**R:** $x_{ij} \in \{0, 1\}$: vale 1 se l'arco $(i,j)$ fa parte del cammino.

---

## Q7: Transhipment — nodo di transito
**D:** Qual è la condizione su un nodo di transito nel transhipment?

**R:** $b_v = 0$: il flusso in entrata uguale al flusso in uscita.

---

*Source:* `Domande aperte RO.pdf` (non ufficiale — riscritto)
