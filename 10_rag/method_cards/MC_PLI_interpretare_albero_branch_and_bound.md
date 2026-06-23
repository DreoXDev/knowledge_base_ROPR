---
type: method_card
topic: programmazione_lineare_intera
status: active
sources: [BB PLI.pdf]
reliability: official
---

# Method Card: Interpretare un Albero di Branch and Bound

## Quando Usarlo
Esercizi in cui viene fornito un albero di Branch and Bound già parzialmente o interamente disegnato con nodi e bound, e viene chiesto di interpretarne lo stato o proseguire l'esplorazione.

## Regole d'Oro per la Risoluzione

### 1. Riconoscere Max / Min
* **Minimo**: I bound nei nodi ($LB$) **crescono** o restano uguali lungo i rami da padre a figlio.
* **Massimo**: I bound nei nodi ($UB$) **decrescono** o restano uguali lungo i rami da padre a figlio.

### 2. Miglior Soluzione Ammissibile (Incumbent $Z_I$)
* **Minimo**: Il valore della soluzione intera ammissibile **più basso**.
* **Massimo**: Il valore della soluzione intera ammissibile **più alto**.

### 3. Intervallo dell'Ottimo $z^*$
* **Minimo**: $[\min LB_{\text{aperti}}, Z_I]$
* **Massimo**: $[Z_I, \max UB_{\text{aperti}}]$

### 4. Prossimo Nodo in Best Bound First (BBF)
* **Minimo**: Selezionare il nodo aperto con **$LB$ più basso**.
* **Massimo**: Selezionare il nodo aperto con **$UB$ più alto**.

### 5. Chiudere Nodi per Dominanza
* **Minimo**: Qualsiasi nodo aperto con bound $LB \ge Z_I$ può essere potato e chiuso.
* **Massimo**: Qualsiasi nodo aperto con bound $UB \le Z_I$ può essere potato e chiuso.
