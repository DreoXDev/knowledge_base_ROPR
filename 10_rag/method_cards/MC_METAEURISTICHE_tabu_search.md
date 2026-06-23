---
type: method-card
topic: metaeuristiche
status: consolidated
sources:
  - raw_assets/Domande aperte RO.pdf
reliability: non-ufficiale
---

# Method Card: Tabu Search

## Quando Usarla

Quando la domanda chiede di descrivere il **Tabu Search** (TS), la **tabu list**, il **criterio di aspirazione**, o i criteri di arresto.

---

## Struttura dell'Algoritmo

1. **Inizializzazione**: soluzione corrente $x_c$, best $x^* = x_c$, tabu list $\mathcal{T} = \emptyset$.
2. **Generazione del vicinato**: $N(x_c)$.
3. **Selezione**: scegliere la **migliore mossa non tabu** nel vicinato (anche se peggiora $f$).
   - Eccezione: una mossa tabu può essere accettata se soddisfa il **criterio di aspirazione**.
4. **Aggiornamento tabu list**: aggiungere la mossa corrente a $\mathcal{T}$ (coda FIFO di lunghezza fissa $|\mathcal{T}|$).
5. **Aggiornamento best**: se $f(x_c) > f(x^*)$ (per max), $x^* \leftarrow x_c$.
6. Ripetere fino al criterio di arresto.

---

## Tabu List

- Vieta temporaneamente le mosse recentemente effettuate.
- Scopo: evitare il **cycling** (tornare alle stesse soluzioni) e forzare la diversificazione.
- Lunghezza $|\mathcal{T}|$: corta → più intensificazione; lunga → più diversificazione.

---

## Criterio di Aspirazione

Il criterio di aspirazione **ignora il tabu** e accetta una mossa vietata se:
$$f(x_{\text{mossa tabu}}) > f(x^*) \quad \text{(per max)}$$

Ovvero: se la mossa porta a una soluzione migliore della migliore nota globale, il tabu viene revocato.

---

## Criteri di Arresto

- Numero massimo di iterazioni.
- Numero massimo di iterazioni senza miglioramento di $x^*$.
- Nessuna mossa ammissibile nel vicinato.

---

## Output da Esame

```
Tabu Search esegue ricerca locale con memoria (tabu list).
La tabu list vieta mosse recenti per evitare il cycling.

Ad ogni iterazione si sceglie la migliore mossa NON TABU nel vicinato,
anche se peggiora la soluzione corrente (escape da ottimo locale).

Criterio di aspirazione: una mossa tabu viene accettata se produce una
soluzione migliore della migliore nota globale x*.

Criteri di arresto: max iterazioni, max iter senza miglioramento di x*.
Non garantisce l'ottimo globale.
```

---

## Collegamento Pattern

→ [[Domande_aperte_metaeuristiche]]
→ [[Metaeuristiche_domande_aperte]]
