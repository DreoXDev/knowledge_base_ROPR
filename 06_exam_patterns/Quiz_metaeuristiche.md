---
type: exam-pattern
topic: metaeuristiche
status: da-validare
sources:
  - raw_assets/AAA - La bibbia di RO.pdf
reliability: non-ufficiale
---

# Quiz — Metaeuristiche

> ⚠️ **Attenzione**: Questo pattern è basato su un asset non ufficiale (screenshot). Le risposte non sono validate. Verificare ogni affermazione con le slide ufficiali del corso prima dell'esame.

## Riconoscimento

Segnali nella traccia:
- "metaeuristiche"
- "ricerca locale"
- "vicinato" / "neighborhood"
- "simulated annealing"
- "tabu search"
- "algoritmo genetico"
- "intensificazione" / "diversificazione"

---

## Concetti Chiave (da validare)

| Concetto | Definizione sintetica | Da validare |
|---|---|---|
| Euristica vs algoritmo esatto | Euristica: non garantisce ottimo globale; esatto: sì | ✓ con slide |
| Ricerca locale | Esplora il vicinato della soluzione corrente | ✓ con slide |
| Vicinato | Insieme delle soluzioni raggiungibili con una singola mossa | ✓ con slide |
| Ottimo locale | Soluzione non migliorabile nel vicinato | ✓ con slide |
| Escape da ottimo locale | Meccanismo per accettare mosse peggiorative | ✓ con slide |
| Intensificazione | Approfondire l'esplorazione di una regione promettente | ✓ con slide |
| Diversificazione | Esplorare regioni nuove dello spazio | ✓ con slide |
| Simulated annealing | Accetta mosse peggiorative con probabilità $e^{-\Delta f / T}$ | ✓ con slide |
| Tabu search | Mantiene una lista di mosse "tabù" per evitare cicli | ✓ con slide |
| Algoritmo genetico | Evoluzione di una popolazione di soluzioni (crossover, mutazione) | ✓ con slide |

---

## Domande Ricorrenti (da validare con fonti ufficiali)

| Tema | Domanda sintetica | Risposta da validare |
|---|---|---|
| Ricerca locale | Un algoritmo di ricerca locale garantisce l'ottimo globale? | No, solo locale |
| Simulated annealing | Come cambia la probabilità di accettare mosse peggiorative nel SA? | Diminuisce con la temperatura |
| Tabu search | A cosa serve la lista tabù? | Evitare cicli e ottimi locali |
| Algoritmi genetici | Cosa sono crossover e mutazione? | Operatori genetici su soluzioni codificate |
| Intensificazione | Quando si usa l'intensificazione? | Quando si è vicini a una soluzione buona |
| Diversificazione | Quando si usa la diversificazione? | Quando si è bloccati in un ottimo locale |

---

## Procedura per Rispondere

1. **Non derivare teoria da questo file** come fonte primaria.
2. Verificare ogni risposta con slide ufficiali o appunti validati.
3. Se una domanda è su definizioni, usare terminologia del corso.
4. Se una domanda è su confronti (es. SA vs tabu), rispondere in modo strutturato.

---

## Template Risposta da Esame (generico)

```
[Nome metaeuristica] è un algoritmo di ricerca [locale/globale] che ...
Il vicinato è definito come ...
L'algoritmo accetta mosse peggiorative [sì/no] perché ...
Differenza rispetto a [altro metodo]: ...
```

---

## Collegamento

→ [[MC_Metaeuristiche_quiz]]
