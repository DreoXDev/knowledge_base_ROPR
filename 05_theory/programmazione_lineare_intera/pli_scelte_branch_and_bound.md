---
type: theory
topic: programmazione_lineare_intera
status: active
sources: [BB PLI.pdf]
reliability: official
---

# Scelte Progettuali nel Branch and Bound

L'algoritmo di Branch and Bound non è univocamente determinato dal formalismo matematico, ma richiede la definizione di diverse scelte progettuali ed euristiche che ne influenzano pesantemente l'efficienza computazionale.

## Scelte Progettuali Principali

Un'implementazione completa dell'algoritmo deve stabilire:
1. **Scelta del nodo da esplorare**: Quale nodo, tra quelli aperti (foglie non potate), sviluppare all'iterazione successiva.
2. **Scelta della variabile di branching**: Quale variabile non intera $x_j^*$ selezionare per generare i vincoli di ramificazione.
3. **Scelta del rilassamento**: Quale tipo di rilassamento usare per calcolare i bound (es. rilassamento continuo LP, rilassamento lagrangiano).
4. **Criteri di arresto**: Quando interrompere la procedura prima della convergenza all'ottimo globale (es. per limiti di tempo, di memoria o per gap di ottimalità tollerabile).
5. **Euristiche primali**: Algoritmi euristici per determinare rapidamente soluzioni ammissibili intere e migliorare l'incumbent $Z_I$.

---

## Regole di Selezione del Nodo

Le strategie di visita dell'albero si dividono principalmente in due categorie:

### 1. Depth First (Profondità / LIFO)
Seleziona il sotto-problema creato più recentemente (il nodo più profondo nell'albero).

- **Vantaggi**:
  - **Uso minimo di memoria**: Mantiene attivi solo i nodi lungo il cammino corrente.
  - **Incumbent precoce**: Raggiunge rapidamente le foglie dell'albero, facilitando l'individuazione di una soluzione intera ammissibile (incumbent $Z_I$) utile per la potatura degli altri rami.
- **Svantaggi**:
  - Può sprecare tempo esplorando interi sotto-alberi con soluzioni di pessima qualità se la scelta iniziale è errata.

### 2. Best Bound First (Miglior Bound)
Seleziona il nodo aperto che presenta la valutazione ottimistica migliore (il bound più promettente).

- **In problemi di massimo**: Seleziona il nodo con Upper Bound ($UB$) più alto.
- **In problemi di minimo**: Seleziona il nodo con Lower Bound ($LB$) più basso.
- **Vantaggi**:
  - **Minimalità dei nodi**: Minimizza il numero totale di nodi visitati prima di provare l'ottimalità.
  - Sviluppa sempre il ramo teoricamente più promettente.
- **Svantaggi**:
  - **Consumo di memoria**: Può richiedere di mantenere in memoria molti nodi aperti a livelli diversi.
  - Può trovare tardi le prime soluzioni ammissibili intere.

### 3. Strategie Miste
Combinano i due approcci:
- Si inizia con **Depth First** per trovare rapidamente una soluzione incombente ammissibile.
- Una volta ottenuta una buona soluzione di base per effettuare potature per dominanza, si passa a **Best Bound First** per ridurre il numero di nodi esplorati.

---

## Scelta della Variabile di Branching

Se il rilassamento continuo ha come soluzione $\bar{x}$ e vi sono variabili vincolate a interezza che assumono un valore frazionario, si seleziona una variabile frazionaria $\bar{x}_j$ e si generano due rami:
- Ramo sinistro: $x_j \le \lfloor \bar{x}_j \rfloor$
- Ramo destro: $x_j \ge \lceil \bar{x}_j \rceil$

Le euristiche comuni per la scelta di $x_j$ includono:
- **Indice più basso**: Si sceglie la prima variabile in ordine d'indice (regola deterministica semplice).
- **Variabile più frazionaria**: Si sceglie la variabile la cui parte frazionaria è più vicina a $0.5$ (quella che massimizza la distanza dall'intero, es. $\max_j | \bar{x}_j - [\bar{x}_j] |$).
- **Costi pseudodualizzati**: Valutazioni sull'impatto stimato della ramificazione sulla funzione obiettivo.
