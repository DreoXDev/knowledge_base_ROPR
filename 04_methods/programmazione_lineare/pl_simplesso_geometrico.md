---
materia: ROPR
area: Programmazione Lineare
tipo: metodo
fonte: Ricerca Operativa - Metodo del Simplesso - 23-24.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - simplesso
  - geometria
  - method-card
---

# METHOD CARD — Simplesso Geometrico

## Idea Fondamentale

Il metodo del simplesso interpreta la ricerca della soluzione ottima muovendosi lungo i bordi (spigoli) della regione ammissibile del problema, spostandosi da un vertice ammissibile ad un altro adiacente che migliori il valore della funzione obiettivo.

## Procedura Operativa Passo-Passo

1. **Rappresentare la Regione Ammissibile**:
   - Tracciare nel piano cartesiano (per problemi con 2 variabili decisionali) o definire algebricamente le equazioni di frontiera associate ai vincoli.
   - Identificare la regione che soddisfa contemporaneamente tutte le disuguaglianze.

2. **Identificare i Vertici della Regione Ammissibile**:
   - Risolvere i sistemi di equazioni corrispondenti alle intersezioni delle frontiere dei vincoli.
   - Selezionare solo i vertici ammissibili (quelli che non violano alcun vincolo).

3. **Determinare l'Adiacenza dei Vertici**:
   - In uno spazio con $n$ variabili, due vertici ammissibili sono adiacenti se condividono $n-1$ frontiere di vincolo. Nel piano ($n=2$), condividono esattamente $1$ vincolo (la retta che li unisce è uno spigolo).

4. **Algoritmo Iterativo Geometrico**:
   - **Partenza**: Iniziare da un vertice iniziale ammissibile (ad esempio, l'origine $(0,0)$ se ammissibile).
   - **Analisi dell'Adiacenza**: Identificare tutti i vertici ammissibili adiacenti al vertice corrente.
   - **Verifica e Spostamento**:
     - Valutare la funzione obiettivo $Z$ su ciascun vertice adiacente.
     - Se almeno un vertice adiacente ha un valore di $Z$ migliore, scegliere quello con il miglioramento maggiore e spostarsi su di esso (nuovo vertice corrente).
     - Ripetere l'analisi dell'adiacenza dal nuovo vertice.
   - **Criterio di Ottimalità**: Se nessuno dei vertici adiacenti offre un valore di $Z$ migliore del vertice corrente, il vertice corrente è la **soluzione ottima globale** del problema.
