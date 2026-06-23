---
type: method-card
topic: programmazione_lineare_intera
status: consolidated
sources:
  - raw_assets/AAA - La bibbia di RO.pdf
reliability: non-ufficiale
---

# Method Card: Branch and Bound — Quiz e Lettura Albero

## Quando Usarla

Quando la traccia presenta un **albero B&B già tracciato** (o parzialmente tracciato) e chiede di:
- identificare l'incumbent corrente $Z_I$
- determinare quali nodi sono stati potati e perché
- stabilire il prossimo nodo da sviluppare
- rispondere a domande vero/falso su potature, bound, ottimo

---

## Lettura dell'Albero B&B

### Passo 1 — Identifica il tipo (max o min)
- **Massimo**: si vuole il bound superiore (UB) massimo. Si pota se $UB \le Z_I$.
- **Minimo**: si vuole il bound inferiore (LB) minimo. Si pota se $LB \ge Z_I$.

### Passo 2 — Trova l'incumbent $Z_I$
- Migliore soluzione intera trovata finora.
- Si aggiorna ogni volta che un nodo dà una soluzione intera migliore.

### Passo 3 — Calcola l'intervallo ottimo
- Massimo: $[Z_I, \max UB_{\text{aperti}}]$
- Minimo: $[\min LB_{\text{aperti}}, Z_I]$

### Passo 4 — Verifica potature
Ogni nodo chiuso deve rispettare **esattamente una** delle regole:
- **Dominanza**: $UB \le Z_I$ (max) o $LB \ge Z_I$ (min).
- **Interezza**: soluzione del rilassamento è già intera.
- **Inammissibilità**: sotto-problema infeasible.

### Passo 5 — Best Bound First
Il prossimo nodo da sviluppare ha il bound più promettente:
- Massimo: nodo aperto con $UB$ massimo.
- Minimo: nodo aperto con $LB$ minimo.

---

## Regole di Potatura — Tabella

| Tipo | Condizione | Azione |
|---|---|---|
| Dominanza (max) | $UB \le Z_I$ | Pota |
| Dominanza (min) | $LB \ge Z_I$ | Pota |
| Interezza | Soluzione intera ammissibile | Aggiorna $Z_I$, poi pota |
| Inammissibilità | Sotto-problema vuoto | Pota |
| Promettente (max) | $UB > Z_I$ e soluzione frazionaria | Branching |
| Promettente (min) | $LB < Z_I$ e soluzione frazionaria | Branching |

---

## Errori Frequenti

- ❌ Aggiornare $Z_I$ con una soluzione **frazionaria**.
- ❌ Potare un nodo con bound ancora promettente.
- ❌ Confondere le direzioni per max vs min.
- ❌ Dimenticare di aggiornare $Z_I$ quando si trova una soluzione intera migliore.

---

## Collegamento Pattern

→ [[Quiz_PLI_Branch_and_Bound]]
