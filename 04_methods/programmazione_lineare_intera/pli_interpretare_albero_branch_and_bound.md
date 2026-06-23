---
type: method
topic: programmazione_lineare_intera
status: active
sources: [BB PLI.pdf]
reliability: official
---

# Metodo: Interpretare un Albero di Branch and Bound

Questo metodo descrive i passaggi per risolvere gli esercizi d'esame basati sulla lettura e sull'interpretazione di un albero di Branch and Bound già parzialmente o totalmente tracciato.

---

## 1. Riconoscimento del Tipo di Problema ($\max$ vs $\min$)

Se la traccia d'esame non specifica esplicitamente se l'obiettivo è di massimizzazione o minimizzazione, è possibile dedurlo analizzando l'andamento dei bound indicati nei nodi:

- **Problema di Minimo ($\min$)**:
  - I bound del rilassamento continuo calcolati nei nodi sono **Lower Bound** ($LB$).
  - I valori di $LB$ **tendono a crescere (o restare uguali)** scendendo lungo i rami dell'albero (da padre a figlio) a causa delle restrizioni aggiuntive:
    $$
    LB_{\text{padre}} \le LB_{\text{figlio}}
    $$
  - Le valutazioni delle soluzioni intere ammissibili trovate rappresentano dei limiti superiori ($UB$) per l'ottimo reale.
  
- **Problema di Massimo ($\max$)**:
  - I bound del rilassamento continuo calcolati nei nodi sono **Upper Bound** ($UB$).
  - I valori di $UB$ **tendono a diminuire (o restare uguali)** scendendo lungo i rami dell'albero (da padre a figlio) a causa delle restrizioni aggiuntive:
    $$
    UB_{\text{padre}} \ge UB_{\text{figlio}}
    $$
  - Le valutazioni delle soluzioni intere ammissibili trovate rappresentano dei limiti inferiori ($LB$) per l'ottimo reale.

---

## 2. Determinare la Migliore Soluzione Ammissibile (Incumbent)

- **Per un problema di massimo**:
  - È la soluzione intera ammissibile con valore di obiettivo **più alto** tra quelle individuate. Questa costituisce l'incumbent corrente $Z_I$ (detto anche miglior $LB$ corrente).
- **Per un problema di minimo**:
  - È la soluzione intera ammissibile con valore di obiettivo **più basso** tra quelle individuate. Questa costituisce l'incumbent corrente $Z_I$ (detto anche miglior $UB$ corrente).

---

## 3. Calcolare l'Intervallo dell'Ottimo $z^*$

L'ottimo reale $z^*$ del problema intero o misto è confinato all'interno di un intervallo noto durante l'esecuzione dell'algoritmo:

- **Caso di Massimo**:
  $$
  Z_I \le z^* \le \max_{P_j \in \text{aperti}} Z_{rel}(P_j)
  $$
  dove $Z_I$ è la migliore soluzione intera nota, e il limite superiore è il massimo tra gli Upper Bound dei nodi correntemente aperti (non potati).

- **Caso di Minimo**:
  $$
  \min_{P_j \in \text{aperti}} Z_{rel}(P_j) \le z^* \le Z_I
  $$
  dove $Z_I$ è la migliore soluzione intera nota, e il limite inferiore è il minimo tra i Lower Bound dei nodi correntemente aperti (non potati).

---

## 4. Determinazione del Prossimo Nodo da Sviluppare in Best Bound First (BBF)

Se la regola di selezione del nodo è **Best Bound First**:
- **Massimo**: Identificare tutti i nodi attualmente aperti e scegliere quello avente l'**Upper Bound ($UB$) più alto**.
- **Minimo**: Identificare tutti i nodi attualmente aperti e scegliere quello avente il **Lower Bound ($LB$) più basso**.

---

## 5. Criteri per la Chiusura di Nuovi Nodi per Dominanza

Dato un nuovo nodo $P_{new}$ con bound $Z_{rel}(P_{new})$:
- **Massimo**: Il nuovo nodo permette di chiudere per dominanza un nodo aperto esistente $P_{old}$ con bound $Z_{rel}(P_{old})$ se $Z_{rel}(P_{old}) \le Z_{rel}(P_{new})$ e la soluzione associata a $P_{new}$ è intera (diventando la nuova incumbent).
- **Minimo**: Il nuovo nodo permette di chiudere per dominanza un nodo aperto esistente $P_{old}$ con bound $Z_{rel}(P_{old})$ se $Z_{rel}(P_{old}) \ge Z_{rel}(P_{new})$ e la soluzione associata a $P_{new}$ è intera (diventando la nuova incumbent).
