---
type: flashcards
topic: metaeuristiche
status: da-validare
sources:
  - raw_assets/AAA - La bibbia di RO.pdf
reliability: non-ufficiale
---

# Flashcard — Quiz Metaeuristiche

> ⚠️ **Verificare con slide ufficiali prima dell'esame.**

---

## Q1: Ricerca locale — garanzia di ottimo globale?
**D:** Un algoritmo di ricerca locale garantisce di trovare l'ottimo globale?

**R:** **No**. Garantisce solo l'ottimo locale rispetto al vicinato scelto.

---

## Q2: Simulated Annealing — come varia la probabilità di accettare mosse peggiorative?
**D:** Nel simulated annealing, come cambia la probabilità di accettare mosse peggiorative durante l'esecuzione?

**R:** Diminuisce man mano che la **temperatura $T$ decresce** (raffreddamento). La probabilità è $p = e^{-\Delta f/T}$.

---

## Q3: Lista tabù — a cosa serve?
**D:** A cosa serve la lista tabù nel tabu search?

**R:** Evita di rivisitare soluzioni recentemente già visitate, impedendo il **cycling** e facilitando l'escape da ottimi locali.

---

## Q4: Intensificazione vs Diversificazione
**D:** Quando si usa l'intensificazione e quando la diversificazione nelle metaeuristiche?

**R:**
- **Intensificazione**: si è vicini a una buona soluzione → approfondire la regione.
- **Diversificazione**: si è bloccati in un ottimo locale → esplorare regioni nuove.

---

## Q5: Algoritmi genetici — operatori base
**D:** Quali sono i due operatori genetici principali negli algoritmi genetici?

**R:** **Crossover** (combinazione di due soluzioni genitori) e **Mutazione** (modifica casuale di una soluzione).

---

*Source:* `AAA - La bibbia di RO.pdf` (non ufficiale — da validare con slide ufficiali)*
