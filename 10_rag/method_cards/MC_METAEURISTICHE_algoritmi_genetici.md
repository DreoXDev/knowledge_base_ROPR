---
type: method-card
topic: metaeuristiche
status: consolidated
sources:
  - raw_assets/Domande aperte RO.pdf
reliability: non-ufficiale
---

# Method Card: Algoritmi Genetici

## Quando Usarla

Quando la domanda chiede di descrivere il funzionamento degli **algoritmi genetici**, i criteri di arresto, oppure il ruolo di crossover e mutazione.

---

## Struttura dell'Algoritmo

1. **Inizializzazione**: creare una popolazione iniziale di $N$ individui (soluzioni) casuali o euristici.
2. **Valutazione**: calcolare il valore di fitness $f(\text{individuo})$ per ogni individuo.
3. **Selezione**: scegliere i genitori con probabilità proporzionale alla fitness (o con tournament selection).
4. **Crossover**: combinare due genitori per produrre due figli. Scopo: ereditare le migliori caratteristiche di entrambi i genitori.
5. **Mutazione**: modificare casualmente alcuni geni di un figlio con probabilità $p_m$ bassa. Scopo: mantenere diversità ed esplorare regioni nuove.
6. **Nuova generazione**: sostituire (in parte o totalmente) la vecchia popolazione con i figli.
7. **Ripetere** dal passo 2 fino al criterio di arresto.

---

## Crossover

- **One-point**: scambia la parte destra del cromosoma da un punto di taglio casuale.
- **Two-point**: due punti di taglio.
- **Uniform**: ogni gene viene ereditato da uno dei due genitori con probabilità 0.5.

Ruolo: **intensificazione** — combina caratteristiche buone di soluzioni diverse.

---

## Mutazione

- **Bit-flip** (rappresentazione binaria): inverte un bit casuale.
- **Gaussian** (rappresentazione reale): aggiunge una perturbazione gaussiana.

Ruolo: **diversificazione** — mantiene la diversità e previene la convergenza prematura.

---

## Criteri di Arresto

- Numero massimo di generazioni.
- Valore di fitness raggiunto (soglia).
- Numero massimo di generazioni senza miglioramento.
- Diversità della popolazione sotto una soglia.

---

## Output da Esame

```
Gli algoritmi genetici sono metaeuristiche basate sull'evoluzione biologica.
Non garantiscono in generale l'ottimo globale.

Funzionamento:
  1. Popolazione iniziale di N individui (soluzioni codificate).
  2. Valutazione tramite funzione di fitness.
  3. Selezione dei genitori (fitness proporzionale o tournament).
  4. Crossover: combina due genitori per produrre figli.
  5. Mutazione: modifica casuale di alcuni geni (diversificazione).
  6. Nuova generazione; ripetere.

Criteri di arresto: max generazioni, no miglioramento per k generazioni,
  fitness target raggiunto.
```

---

## Collegamento Pattern

→ [[Domande_aperte_metaeuristiche]]
→ [[Metaeuristiche_domande_aperte]]
