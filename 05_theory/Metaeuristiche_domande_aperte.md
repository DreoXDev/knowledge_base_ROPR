---
type: theory-note
topic: metaeuristiche
status: consolidated
sources:
  - raw_assets/Domande aperte RO.pdf
reliability: non-ufficiale
---

# Metaeuristiche — Domande Aperte

Fonte: `raw_assets/Domande aperte RO.pdf` (rielaborato e validato)
Area: Metaeuristiche
Prerequisiti: ottimizzazione combinatoria, ricerca locale

> ⚠️ Le risposte originali sono state riscritte. In particolare, la formula per SA è stata corretta per distinguere min e max. Validare con slide ufficiali prima dell'esame.

---

## Definizione di Metaeuristica

Una **metaeuristica** è una strategia di ricerca di alto livello che guida euristiche subordinate per l'esplorazione dello spazio delle soluzioni. Non garantisce in generale l'ottimo globale, ma produce soluzioni di buona qualità in tempi computazionali ragionevoli.

**Caratteristiche**:
- Non dipende da una struttura specifica del problema (generica).
- Bilancia esplorazione (**diversificazione**) e sfruttamento locale (**intensificazione**).
- Può accettare mosse peggiorative per evitare ottimi locali.

---

## Algoritmi Genetici (D2, D12)

**Domanda D2**: Come funzionano gli algoritmi genetici? Quali sono i criteri di arresto?

**Domanda D12**: Cosa sono crossover e mutazione?

### Struttura

Un **algoritmo genetico** (AG) mantiene una **popolazione** di soluzioni (individui/cromosomi) e la evolve iterativamente tramite:

1. **Rappresentazione**: ogni soluzione è codificata come cromosoma (es. vettore binario o reale).
2. **Funzione di fitness**: misura la qualità di ogni individuo.
3. **Selezione**: si scelgono gli individui con fitness migliore per la riproduzione (es. roulette wheel, tournament selection).
4. **Crossover** (ricombinazione): due individui "genitori" combinano le loro caratteristiche per produrre individui "figli". Scopo: sfruttare le migliori caratteristiche di entrambi i genitori.
5. **Mutazione**: modifica casuale di alcuni geni di un individuo. Scopo: mantenere diversità nella popolazione ed esplorare nuove regioni dello spazio.
6. **Nuova generazione**: i figli sostituiscono (in parte o totalmente) i genitori.

### Criteri di Arresto

- Numero massimo di generazioni raggiunto.
- Valore di fitness soddisfacente (es. $f^* \ge f_{\text{target}}$).
- Numero massimo di iterazioni senza miglioramento.
- Diversità della popolazione sotto una soglia (convergenza prematura).

---

## Simulated Annealing (D11, D13)

**Domanda D11**: Come funziona il Simulated Annealing? Criteri di arresto?

**Domanda D13**: Come si relazionano temperatura, exploration ed exploitation?

### Struttura

Il **Simulated Annealing** (SA) è ispirato al raffreddamento dei metalli. Parte da una soluzione corrente $x_c$ e propone iterativamente mosse casuali nel vicinato $N(x_c)$.

**Algoritmo**:

1. Inizializzare $x_c$, temperatura $T = T_0$ alta.
2. Estrarre casualmente $x_n \in N(x_c)$.
3. Calcolare $\Delta f = f(x_n) - f(x_c)$.
4. **Accettazione**:
   - Se $\Delta f < 0$ (miglioramento per min): accetta sempre ($x_c \leftarrow x_n$).
   - Se $\Delta f \ge 0$ (mossa peggiorativa per min): accetta con probabilità:
$$p = \exp\!\left(-\frac{\Delta f}{T}\right)$$
5. Ridurre la temperatura: $T \leftarrow \alpha T$ (con $0 < \alpha < 1$, schema di raffreddamento).
6. Ripetere fino al criterio di arresto.

> Per un problema di **massimizzazione**: la mossa peggiorativa ha $\Delta f < 0$ e la probabilità è $p = \exp(\Delta f / T)$.

### Temperatura, Exploration ed Exploitation (D13)

| Temperatura alta | Temperatura bassa |
|---|---|
| $p \approx 1$: si accettano quasi tutte le mosse | $p \approx 0$: si accettano quasi solo miglioramenti |
| **Exploration** (diversificazione) | **Exploitation** (intensificazione locale) |
| Rischio: nessun miglioramento diretto | Rischio: blocco in ottimo locale |

### Criteri di Arresto

- Temperatura inferiore a $T_{\min}$.
- Numero massimo di iterazioni raggiunto.
- Numero massimo di iterazioni senza miglioramento.
- Nessuna mossa accettata in un certo numero di tentativi.

---

## Tabu Search (D14)

**Domanda**: Cosa sono la tabu list e il criterio di aspirazione?

### Struttura

Il **Tabu Search** (TS) esegue ricerca locale con memoria: mantiene una **tabu list** delle mosse recentemente effettuate per evitare di rivisitare soluzioni già visitate.

**Algoritmo**:

1. Inizializzare $x_c$, tabu list $\mathcal{T} = \emptyset$, best $x^* = x_c$.
2. Generare i vicini $N(x_c)$.
3. Scegliere la **migliore mossa non tabu** nel vicinato (anche se peggiora la soluzione corrente).
4. Aggiornare la tabu list (es. coda FIFO di lunghezza $|\mathcal{T}|$).
5. Se $f(x_c) > f(x^*)$ (per max): aggiornare $x^*$.
6. Ripetere fino al criterio di arresto.

### Tabu List

La **tabu list** vieta temporaneamente le mosse recentemente effettuate. Scopo:
- Evitare il **cycling** (tornare alla stessa soluzione).
- Forzare la **diversificazione** dell'esplorazione.

La lunghezza della tabu list è un parametro: lista corta → più intensificazione, lista lunga → più diversificazione.

### Criterio di Aspirazione

Il **criterio di aspirazione** permette di **ignorare il tabu** e accettare una mossa vietata se questa produce una soluzione migliore della migliore soluzione globale nota $x^*$.

$$\text{Accetta mossa tabu } m \text{ se } f(x_m) > f(x^*) \quad \text{(per max)}$$

### Criteri di Arresto

- Numero massimo di iterazioni.
- Numero massimo di iterazioni senza miglioramento di $x^*$.
- Numero di mosse ammissibili nel vicinato scende a zero.

---

## Risposta Modello da Esame — Template Metaeuristiche

```
[Nome metaeuristica] è [definizione sintetica in 2 righe].
Non garantisce in generale l'ottimo globale.

Meccanismo principale:
- [passo 1]
- [passo 2]
- [...]

Parametri chiave:
- [es. temperatura, lunghezza tabu list, dimensione popolazione]

Criteri di arresto:
- numero massimo di iterazioni
- numero massimo di iterazioni senza miglioramento
- [criterio specifico dell'algoritmo]
```

---

## Errori da Evitare

- ❌ Scrivere la formula SA senza distinguere min e max.
- ❌ Dire che le metaeuristiche garantiscono l'ottimo globale in generale.
- ❌ Confondere diversificazione (esplorazione nuove regioni) con intensificazione (approfondimento locale).
- ❌ Descrivere il crossover come mutazione, o viceversa.
- ❌ Non specificare il ruolo della temperatura nel bilanciamento exploration/exploitation.
- ❌ Non spiegare il criterio di aspirazione in Tabu Search.

---

## Errori Corretti Rispetto agli Appunti Originali

- Corretta la formula della probabilità SA: $p = \exp(-\Delta f / T)$ vale per minimizzazione con $\Delta f > 0$.
- Per massimizzazione: $p = \exp(\Delta f / T)$ con $\Delta f < 0$.
- Aggiunta distinzione esplicita exploration/exploitation legata alla temperatura.
- Rimossa terminologia informale presente nelle bozze originali.

---

## Connessioni

- [[MC_METAEURISTICHE_algoritmi_genetici]]
- [[MC_METAEURISTICHE_simulated_annealing]]
- [[MC_METAEURISTICHE_tabu_search]]
- [[Quiz_metaeuristiche]]
