---
type: theory-note
topic: programmazione-lineare
status: draft
sources:
  - raw_assets/Programmazione Lineare/Ricerca Operativa - Introduzione a PL - 23-24.pdf
reliability: official
---

# Regione Ammissibile e Casi della Soluzione Grafica

La **regione ammissibile** (o spazio delle soluzioni) è l'insieme di tutti i punti dello spazio delle variabili decisionali che soddisfano contemporaneamente tutti i vincoli del modello, inclusi i vincoli di non negatività.

## Caratteristiche Geometriche

Geometricamente, poiché tutti i vincoli sono lineari, la regione ammissibile possiede le seguenti proprietà:

- **Poliedro convesso**: In $\mathbb{R}^n$, l'intersezione di un numero finito di semispazi chiusi (definiti dai vincoli lineari) forma un poliedro convesso.
- **Politopo**: Se la regione ammissibile è limitata (non si estende all'infinito in nessuna direzione), il poliedro viene definito politopo convesso.
- **Regione illimitata**: La regione si estende all'infinito in una o più direzioni.
- **Regione vuota**: Non esiste alcun punto che soddisfi tutti i vincoli contemporaneamente.

## I Quattro Casi della Soluzione Grafica

La ricerca del punto ottimo su una regione ammissibile può condurre a quattro scenari distinti:

### 1. Soluzione Ottima Unica
La funzione obiettivo raggiunge il valore massimo o minimo in un singolo vertice (punto estremo) del poliedro.

### 2. Infinite Soluzioni Ottime
Questo scenario si verifica quando la linea di livello della funzione obiettivo è parallela ad un vincolo attivo all'ottimo.
- Tutte le combinazioni convesse dei due vertici ottimi adiacenti (ovvero tutti i punti del segmento/lato che li unisce) costituiscono soluzioni ottime con lo stesso valore della funzione obiettivo $Z^*$.

### 3. Problema Illimitato
La regione ammissibile è illimitata nella direzione di miglioramento della funzione obiettivo.
- In un problema di massimizzazione, è possibile incrementare indefinitamente il valore di $Z$ senza mai uscire dalla regione ammissibile ($Z \to +\infty$).
- In un problema di minimizzazione, il valore obiettivo può decrescere senza limiti ($Z \to -\infty$).

### 4. Problema Inammissibile
La regione ammissibile è vuota (non contiene alcun punto). Ciò significa che i vincoli sono incompatibili o troppo stringenti tra loro. Non esiste alcuna soluzione ammissibile per il problema.

#ropr #programmazione-lineare #teoria #geometria
