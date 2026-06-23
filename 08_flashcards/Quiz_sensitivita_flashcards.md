---
type: flashcards
topic: programmazione_lineare
status: consolidated
sources:
  - raw_assets/AAA - La bibbia di RO.pdf
reliability: non-ufficiale
---

# Flashcard — Quiz PL: Analisi di Sensitività

---

## Q1: Variazione di $b_i$ — cosa mantenere?
**D:** Per variazioni del termine noto $b_i$, quale condizione deve rimanere soddisfatta?

**R:** L'**ammissibilità** della base corrente: $x_B(\Delta) = \bar{b} + \Delta \cdot d \ge 0$ per ogni riga.

---

## Q2: Variazione di $c_j$ — cosa mantenere?
**D:** Per variazioni del coefficiente obiettivo $c_j$, quale condizione deve rimanere soddisfatta?

**R:** L'**ottimalità**: il segno dei costi ridotti deve rimanere coerente con il criterio di ottimalità (massimo: $\bar{c}_j \le 0$; minimo: $\bar{c}_j \ge 0$).

---

## Q3: Da dove si ricava l'intervallo ammissibile di $\Delta$?
**D:** Come si determina l'intervallo ammissibile per $\Delta$?

**R:** Dalle **disequazioni** che mantengono ammissibile o ottima la base corrente. Si risolve il sistema e si prende l'intersezione degli intervalli.

---

## Q4: Variazione di $b_i$ — formula
**D:** Scrivi la formula per la soluzione di base dopo una perturbazione $\Delta$ su $b_i$.

**R:** $x_B(\Delta) = \bar{b} + \Delta \cdot d$ dove $d = B^{-1}e_i$ è la colonna $i$ di $B^{-1}$.

---

## Q5: Cosa si legge nella riga obiettivo del tableau finale?
**D:** Cosa rappresentano i valori nella riga obiettivo del tableau finale?

**R:** I **costi ridotti** $\bar{c}_j$ delle variabili. Sono zero per le variabili di base, e hanno segno coerente con l'ottimalità per le variabili fuori base.

---

*Source:* `AAA - La bibbia di RO.pdf` (non ufficiale)
