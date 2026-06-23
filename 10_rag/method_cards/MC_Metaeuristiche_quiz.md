---
type: method-card
topic: metaeuristiche
status: da-validare
sources:
  - raw_assets/AAA - La bibbia di RO.pdf
reliability: non-ufficiale
---

# Method Card: Quiz Metaeuristiche

> ⚠️ **Stato**: Da validare con fonti ufficiali (slide del corso).
> Non usare questa scheda come fonte teorica primaria. Verificare ogni risposta con le slide ufficiali prima dell'esame.

## Quando Usarla

Quando la traccia contiene domande su:
- algoritmi euristici vs esatti
- ricerca locale e vicinato
- simulated annealing, tabu search, algoritmi genetici
- intensificazione e diversificazione

---

## Temi Ricorrenti (da validare)

| Tema | Definizione sintetica | Validato |
|---|---|---|
| Euristica | Algoritmo che non garantisce l'ottimo globale ma produce soluzioni buone in tempo ragionevole | ⚠️ da verificare |
| Ricerca locale | Esplora iterativamente il vicinato della soluzione corrente | ⚠️ da verificare |
| Vicinato $N(x)$ | Insieme delle soluzioni raggiungibili da $x$ con una singola operazione | ⚠️ da verificare |
| Ottimo locale | Soluzione $x^*$ t.c. $f(x^*) \le f(y)$ per ogni $y \in N(x^*)$ (minimizzazione) | ⚠️ da verificare |
| Intensificazione | Approfondire la ricerca in una regione promettente | ⚠️ da verificare |
| Diversificazione | Esplorare regioni diverse per evitare ottimi locali | ⚠️ da verificare |
| Simulated Annealing | Accetta mosse peggiorative con probabilità $e^{-\Delta f / T}$, decrementando $T$ | ⚠️ da verificare |
| Tabu Search | Mantiene lista di mosse vietate (tabù) per evitare cicli | ⚠️ da verificare |
| Algoritmo Genetico | Evoluzione di una popolazione: selezione, crossover, mutazione | ⚠️ da verificare |

---

## Domande Frequenti (da validare)

| Domanda | Risposta da validare |
|---|---|
| Un algoritmo di ricerca locale garantisce l'ottimo globale? | No, solo locale |
| In SA, come varia la probabilità di accettare mosse peggiorative? | Diminuisce con la temperatura $T$ |
| A cosa serve la lista tabù? | Evitare di rivisitare soluzioni recenti / evitare cycling |
| Crossover e mutazione: a cosa servono? | Crossover: combina; mutazione: esplora |
| Differenza intensificazione/diversificazione? | Intensificazione: sfrutta; diversificazione: esplora |

---

## Risposte Validate

*(Sezione vuota — compilare dopo verifica con slide ufficiali)*

---

## Collegamento Pattern

→ [[Quiz_metaeuristiche]]
