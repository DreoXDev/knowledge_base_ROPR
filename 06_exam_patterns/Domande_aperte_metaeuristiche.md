---
type: exam-pattern
topic: metaeuristiche
status: consolidated
sources:
  - raw_assets/Domande aperte RO.pdf
reliability: non-ufficiale
---

# Pattern — Domanda Aperta: Metaeuristiche

## Riconoscimento

Segnali nella traccia:
- "algoritmi genetici" / "crossover" / "mutazione" / "fitness"
- "simulated annealing" / "temperatura" / "raffreddamento"
- "tabu search" / "tabu list" / "criterio di aspirazione"
- "exploration" / "exploitation" / "diversificazione" / "intensificazione"
- "criteri di arresto"
- "ricerca locale"
- "ottimo locale" / "escape"

---

## Procedura Rapida

1. **Identificare** quale metaeuristica è richiesta (AG / SA / TS).
2. **Definire** brevemente il metodo (2 righe).
3. **Descrivere il meccanismo principale** (passi, parametri, operatori).
4. **Indicare i parametri chiave** e il loro ruolo.
5. **Elencare i criteri di arresto**.
6. **Specificare** che non garantisce in generale l'ottimo globale.

---

## Checklist per Tipo

### Algoritmi Genetici
```
[ ] Definizione: popolazione di soluzioni evoluta iterativamente
[ ] Fitness: misura qualità degli individui
[ ] Selezione: individui migliori si riproducono
[ ] Crossover: combina genitori per creare figli
[ ] Mutazione: modifica casuale per mantenere diversità
[ ] Non garantisce ottimo globale
[ ] Criteri di arresto: max generazioni, no miglioramento, fitness target
```

### Simulated Annealing
```
[ ] Analogia con raffreddamento metalli
[ ] Accetta sempre mosse migliorative
[ ] Accetta mosse peggiorative con p = exp(-Df/T) [min] o exp(Df/T) [max]
[ ] T alta: exploration (quasi tutto accettato)
[ ] T bassa: exploitation (solo miglioramenti accettati)
[ ] Schema di raffreddamento: T <- alpha*T
[ ] Criteri di arresto: T_min, max iter, max iter senza miglioramento
```

### Tabu Search
```
[ ] Ricerca locale con memoria (tabu list)
[ ] Tabu list: vieta mosse recenti per evitare cycling
[ ] Sceglie la migliore mossa NON TABU (anche se peggiora)
[ ] Criterio di aspirazione: ignora tabu se produce best overall
[ ] Criteri di arresto: max iter, max iter senza miglioramento del best
```

---

## Template Risposta da Esame

```
[Nome metaeuristica] è [definizione: algoritmo di ricerca che...].
Non garantisce in generale il raggiungimento dell'ottimo globale.

Funzionamento:
  [Descrizione del meccanismo principale in 3-5 punti]

Parametri chiave:
  - [parametro 1: ruolo]
  - [parametro 2: ruolo]

Criteri di arresto:
  - numero massimo di iterazioni
  - nessun miglioramento per k iterazioni
  - [criterio specifico]
```

---

## Errori da Evitare

- ❌ Non distinguere min e max nella formula SA.
- ❌ Dire che garantisce l'ottimo globale.
- ❌ Confondere crossover (combina) con mutazione (modifica).
- ❌ Dire che Tabu Search non accetta mai mosse peggiorative (le accetta).
- ❌ Dimenticare il criterio di aspirazione in Tabu Search.
- ❌ Non specificare il ruolo della temperatura nel bilanciamento exploration/exploitation.

---

## Collegamento Method Cards

- [[MC_METAEURISTICHE_algoritmi_genetici]]
- [[MC_METAEURISTICHE_simulated_annealing]]
- [[MC_METAEURISTICHE_tabu_search]]
- [[Metaeuristiche_domande_aperte]]
