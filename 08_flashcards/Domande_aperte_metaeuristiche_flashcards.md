---
type: flashcards
topic: metaeuristiche
status: consolidated
sources:
  - raw_assets/Domande aperte RO.pdf
reliability: non-ufficiale
---

# Flashcard — Domande Aperte Metaeuristiche

---

## Q1: Cos'è una metaeuristica?
**D:** Che cos'è una metaeuristica?

**R:** Una strategia di ricerca generale che guida euristiche subordinate. Produce soluzioni di buona qualità senza garantire in generale l'ottimo globale.

---

## Q2: Ruolo della mutazione negli AG
**D:** A cosa serve la mutazione negli algoritmi genetici?

**R:** A mantenere diversità nella popolazione ed esplorare nuove regioni dello spazio di ricerca (**diversificazione**). Previene la convergenza prematura.

---

## Q3: Probabilità di accettazione in SA (minimizzazione)
**D:** In Simulated Annealing per un problema di minimizzazione, con quale probabilità si accetta una mossa peggiorativa con $\Delta f > 0$?

**R:** $p = \exp(-\Delta f / T)$.

---

## Q4: Temperatura e exploration/exploitation in SA
**D:** Cosa succede alla probabilità di accettare mosse peggiorative in SA quando la temperatura diminuisce?

**R:** Diminuisce: temperatura alta → exploration (quasi tutto accettato); temperatura bassa → exploitation (solo miglioramenti).

---

## Q5: Cos'è il criterio di aspirazione in Tabu Search?
**D:** Cos'è il criterio di aspirazione in Tabu Search?

**R:** Una regola che consente di accettare una mossa vietata (tabu) se produce una soluzione migliore della migliore soluzione globale nota $x^*$.

---

## Q6: Differenza crossover vs mutazione
**D:** Qual è la differenza tra crossover e mutazione negli algoritmi genetici?

**R:** Crossover: combina due genitori per produrre figli (**intensificazione**). Mutazione: modifica casuale un individuo (**diversificazione**).

---

## Q7: Quando si aggiorna la migliore soluzione in Tabu Search?
**D:** Quando si aggiorna la migliore soluzione $x^*$ in Tabu Search?

**R:** Ogni volta che la soluzione corrente $x_c$ è migliore di $x^*$, indipendentemente dal tabu.

---

*Source:* `Domande aperte RO.pdf` (non ufficiale — riscritto)
