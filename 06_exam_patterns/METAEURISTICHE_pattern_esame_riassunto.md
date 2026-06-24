---
type: exam-pattern
topic: metaeuristiche
status: consolidated
---

# METAEURISTICHE — Riepilogo Pattern d'Esame

## Tabella Segnali → Metodo → File

| Segnale nella traccia | Metodo | Method Card / File |
|---|---|---|
| "algoritmi genetici", "popolazione", "fitness" | Algoritmi Genetici | `MC_METAEURISTICHE_algoritmi_genetici.md` |
| "crossover", "ricombinazione", "genitori/figli" | Crossover AG | `MC_METAEURISTICHE_algoritmi_genetici.md` |
| "mutazione", "diversità", "bit-flip" | Mutazione AG | `MC_METAEURISTICHE_algoritmi_genetici.md` |
| "simulated annealing", "temperatura", "raffreddamento" | Simulated Annealing | `MC_METAEURISTICHE_simulated_annealing.md` |
| "accettare mosse peggiorative", "probabilità", "exp(-Δf/T)" | SA accettazione | `MC_METAEURISTICHE_simulated_annealing.md` |
| "exploration", "exploitation", "diversificazione", "intensificazione" | SA temperatura | `MC_METAEURISTICHE_simulated_annealing.md` |
| "tabu search", "tabu list", "lista tabu" | Tabu Search | `MC_METAEURISTICHE_tabu_search.md` |
| "criterio di aspirazione", "ignora tabu se migliora best" | Tabu aspirazione | `MC_METAEURISTICHE_tabu_search.md` |
| "criteri di arresto", "quando fermare" | Criteri arresto (tutti) | Vedere sotto |
| "ottimo globale", "garanzia ottimo" | Disclaimer | Nessuna garanzia in generale |

---

## Struttura Risposta da Esame

### Algoritmi Genetici
```
Algoritmi Genetici: metaeuristica ispirata all'evoluzione biologica.
Funzionamento:
  1. Popolazione iniziale N individui
  2. Valutazione fitness
  3. Selezione genitori (fitness proporzionale / tournament)
  4. Crossover: combina 2 genitori → 2 figli (intensificazione)
  5. Mutazione: modifica casuale (diversificazione, prob. bassa)
  6. Nuova generazione; ripetere
Criteri di arresto: max generazioni, fitness target, no miglioramento per k gen.
Non garantisce ottimo globale.
```

### Simulated Annealing
```
SA: ispirato al raffreddamento dei metalli. Minimizzazione:
  - mossa migliorativa (Δf < 0): accetta sempre
  - mossa peggiorativa (Δf ≥ 0): accetta con p = exp(-Δf/T)
  T alta → exploration (quasi tutto accettato)
  T bassa → exploitation (solo miglioramenti)
  Raffreddamento: T ← α·T (es. α = 0.95)
Criteri di arresto: T < T_min, max iter, max iter senza miglioramento best.
[Per massimizzazione: p = exp(Δf/T) con Δf < 0]
```

### Tabu Search
```
TS: ricerca locale con memoria.
  Tabu list: vieta mosse recenti → evita cycling.
  Sceglie la miglior mossa NON TABU (anche se peggiora f).
  Criterio di aspirazione: accetta mossa tabu se migliora best x*.
  Aggiorna best x* ogni volta che la soluzione corrente è migliore.
Criteri di arresto: max iter, max iter senza miglioramento di x*.
```

---

## Errori Frequenti

- ❌ Scrivere la formula SA senza distinguere min e max.
- ❌ Dire che le metaeuristiche garantiscono l'ottimo globale.
- ❌ Confondere crossover (combina due individui) con mutazione (modifica uno).
- ❌ Non specificare il ruolo della temperatura in SA (exploration ↔ exploitation).
- ❌ Dimenticare il criterio di aspirazione in Tabu Search.
- ❌ Non elencare i criteri di arresto.

---

## Method Card di Riferimento Principale

→ [[MC_METAEURISTICHE_algoritmi_genetici]]
→ [[MC_METAEURISTICHE_simulated_annealing]]
→ [[MC_METAEURISTICHE_tabu_search]]
→ [[Metaeuristiche_domande_aperte]]
