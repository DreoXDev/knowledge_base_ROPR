---
type: flashcards
topic: programmazione_lineare
status: consolidated
sources:
  - raw_assets/Domande aperte RO.pdf
reliability: non-ufficiale
---

# Flashcard — Domande Aperte PL (Vertici, Basi, Dualità, Simplesso)

---

## Q1: Dualità forte
**D:** Che cosa afferma la dualità forte?

**R:** Se il primale (max) ha soluzione ottima finita $x^*$, anche il duale (min) ha soluzione ottima finita $y^*$ e i valori coincidono: $c^Tx^* = b^Ty^*$.

---

## Q2: Dualità debole
**D:** Che cosa afferma la dualità debole?

**R:** Per ogni $x$ primale ammissibile e $y$ duale ammissibile (max primale), $c^Tx \le b^Ty$. Il valore duale è un upper bound al valore primale.

---

## Q3: Quando una soluzione di base è ammissibile?
**D:** Quando una soluzione di base è ammissibile (BFS)?

**R:** Quando le variabili di base $x_B = B^{-1}b$ soddisfano la non negatività: $x_B \ge 0$.

---

## Q4: Numero massimo di soluzioni di base
**D:** Qual è il numero massimo di soluzioni di base per un problema con $n$ variabili originali e $m$ vincoli?

**R:** In forma aumentata ($n+m$ variabili totali, $m$ vincoli), il numero massimo di basi è $\binom{n+m}{m}$.

---

## Q5: Variabile uscente nel simplesso
**D:** Come si sceglie la variabile uscente nel simplesso?

**R:** Con il **test del minimo rapporto**: $\theta^* = \min_{i:\, d_i > 0} \bar{x}_{B_i}/d_i$. La variabile di base con rapporto minimo esce.

---

## Q6: Complementarità — slack primale
**D:** Cosa implica che lo slack del vincolo primale $i$ è positivo ($b_i - a_i^Tx^* > 0$)?

**R:** Per la complementarità, la variabile duale corrispondente è nulla: $y_i^* = 0$.

---

## Q7: Ogni vertice del poliedro corrisponde a cosa?
**D:** A cosa corrisponde ogni vertice del poliedro ammissibile di un PL?

**R:** A una **soluzione di base ammissibile** (BFS). Il simplesso si muove tra BFS adiacenti.

---

*Source:* `Domande aperte RO.pdf` (non ufficiale — riscritto)
