---
type: flashcards
topic: programmazione_lineare_intera
status: consolidated
sources:
  - raw_assets/AAA - La bibbia di RO.pdf
reliability: non-ufficiale
---

# Flashcard — Quiz PLI: Branch and Bound

---

## Q1: Quando si aggiorna l'incumbent $Z_I$?
**D:** In quali condizioni si aggiorna l'incumbent nel B&B?

**R:** Quando si trova una **soluzione intera ammissibile** con valore migliore dell'incumbent corrente ($Z > Z_I$ per max, $Z < Z_I$ per min).

---

## Q2: Quando si pota per dominanza (massimizzazione)?
**D:** Quando si pota un nodo per dominanza in un problema di massimizzazione?

**R:** Quando il bound superiore del nodo $UB \le Z_I$ (il nodo non può migliorare l'incumbent).

---

## Q3: Errore classico nell'aggiornamento dell'incumbent
**D:** Qual è l'errore più comune nell'aggiornamento dell'incumbent?

**R:** Aggiornare $Z_I$ con una soluzione **frazionaria** del rilassamento invece che con una soluzione **intera** ammissibile.

---

## Q4: Best Bound First — max vs min
**D:** Quale nodo aperto si sviluppa per primo con la strategia Best Bound First?

**R:** Il nodo con il **bound più promettente**: $UB$ massimo per problemi di massimizzazione, $LB$ minimo per problemi di minimizzazione.

---

## Q5: Tre regole di potatura
**D:** Elenca le tre regole di potatura di un nodo B&B.

**R:**
1. **Dominanza**: bound $\le Z_I$ (max) o $\ge Z_I$ (min).
2. **Interezza**: soluzione del rilassamento intera → aggiorna $Z_I$ se migliore.
3. **Inammissibilità**: sotto-problema infeasible.

---

*Source:* `AAA - La bibbia di RO.pdf` (non ufficiale)
