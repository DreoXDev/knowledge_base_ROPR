---
type: flashcards
topic: programmazione_lineare
status: consolidated
sources:
  - raw_assets/AAA - La bibbia di RO.pdf
reliability: non-ufficiale
---

# Flashcard — Quiz PL: Casi Particolari del Simplesso

---

## Q1: Come riconosco un ottimo multiplo nel tableau finale?
**D:** Qual è il segnale di ottimi multipli in un tableau ottimo del simplesso?

**R:** Una variabile **fuori base** ha costo ridotto $\bar{c}_j = 0$.
Si può fare pivot su quella variabile per raggiungere un altro vertice ottimo.

---

## Q2: Come riconosco degenerazione?
**D:** Qual è il segnale di degenerazione in un tableau del simplesso?

**R:** Una variabile **di base** ha valore RHS = 0. La soluzione è di base degenere.

---

## Q3: Come riconosco illimitatezza?
**D:** Qual è il segnale di un problema illimitato in un tableau del simplesso?

**R:** Esiste una variabile candidata entrante, ma la sua colonna nel tableau ha **tutti i coefficienti $\le 0$** (per max) → nessun rapporto minimo valido → $Z^* \to +\infty$.

---

## Q4: Come riconosco non ammissibilità?
**D:** Come si rileva la non ammissibilità nel metodo a due fasi?

**R:** Alla fine della Fase 1, il valore ottimo è $W^* > 0$: almeno una variabile artificiale non è stata azzerata → regione ammissibile vuota.

---

## Q5: Ottimo multiplo vs degenerazione — differenza
**D:** Qual è la differenza tra ottimo multiplo e degenerazione?

**R:** Ottimo multiplo: una variabile **fuori base** ha $\bar{c}_j = 0$ nel tableau **ottimo** (si può migliorare la soluzione con un altro ottimo).
Degenerazione: una variabile **in base** ha valore 0 (può causare cycling).

---

*Source:* `AAA - La bibbia di RO.pdf` (non ufficiale)
