---
type: flashcards
topic: programmazione_non_lineare
status: consolidated
sources:
  - raw_assets/Domande aperte RO.pdf
reliability: non-ufficiale
---

# Flashcard — Domande Aperte KKT

---

## Q1: Le quattro condizioni KKT
**D:** Quali sono le quattro condizioni KKT?

**R:**
1. Stazionarietà: $\nabla_x L = 0$
2. Ammissibilità primale: $g_i(x^*)=0$, $h_j(x^*)\le 0$
3. Ammissibilità duale: $\mu_j \ge 0$ (per min)
4. Complementarità: $\mu_j h_j(x^*) = 0$

---

## Q2: Cosa significa vincolo attivo?
**D:** Un vincolo di disuguaglianza $h_j(x) \le 0$ è attivo in $x^*$?

**R:** È attivo se vale con **uguaglianza**: $h_j(x^*) = 0$.

---

## Q3: Le KKT sono sempre sufficienti?
**D:** Le condizioni KKT sono condizioni necessarie o sufficienti?

**R:** In generale sono **necessarie** (sotto ipotesi di regolarità come LICQ). Diventano sufficienti se $f$ è convessa (per min) e i vincoli di disuguaglianza $h_j$ sono convessi.

---

## Q4: Segno dei moltiplicatori per massimizzazione
**D:** Nella KKT per un problema di massimizzazione con $h_j(x) \le 0$, che segno hanno i moltiplicatori $\mu_j$?

**R:** $\mu_j \le 0$.

---

## Q5: Cosa implica $\mu_j > 0$ per il vincolo $h_j$?
**D:** Se il moltiplicatore KKT $\mu_j > 0$, cosa si può dire del vincolo $h_j(x^*) \le 0$?

**R:** Per la complementarità $\mu_j h_j = 0$: il vincolo è **attivo** ($h_j(x^*) = 0$).

---

*Source:* `Domande aperte RO.pdf` (non ufficiale — riscritto)
