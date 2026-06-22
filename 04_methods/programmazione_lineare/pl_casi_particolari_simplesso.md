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
  - casi-particolari
  - method-card
---

# METHOD CARD — Casi Particolari del Simplesso

Questa card descrive come identificare e gestire i casi particolari o non standard che si presentano durante la risoluzione grafica o tabellare del metodo del simplesso.

## 1. Tableau Ottimo
- **Criterio (per massimizzazione)**: Nella riga 0 del tableau non compaiono coefficienti negativi nelle colonne delle variabili (esclusa la colonna RHS).
- **Azione**: La ricerca è terminata. Leggere la soluzione ottima.

## 2. Ottimi Multipli (Soluzioni Multiple)
- **Rilevamento**: Il tableau corrente soddisfa il criterio di ottimalità (è ottimo), ma almeno una **variabile non di base** ha coefficiente esattamente pari a **zero** nella riga 0.
- **Conseguenza**: Esistono infinite soluzioni ottime.
- **Azione d'esame**:
  1. Per trovare un'altra soluzione di base ottima (un altro vertice ottimo), far entrare in base la variabile non di base con costo ridotto nullo.
  2. Eseguire una normale iterazione di pivot (calcolando i rapporti minimi e aggiornando il tableau).
  3. Il nuovo tableau avrà lo stesso valore di $Z^*$, ma con coordinate delle variabili diverse.
  4. Scrivere che tutte le soluzioni ottime sono date dalla combinazione convessa dei vertici ottimi trovati:
     $$
     x^* = \lambda x^{(1)} + (1-\lambda) x^{(2)} \quad \text{con } \lambda \in [0, 1]
     $$

## 3. Funzione Obiettivo Illimitata (Illimitatezza)
- **Rilevamento**: Viene selezionata una variabile entrante dal criterio della riga 0, ma nella sua colonna pivot tutti i coefficienti associati ai vincoli sono non positivi ($\le 0$).
- **Conseguenza**: Non è possibile calcolare il test dei rapporti minimi (nessun vincolo blocca la crescita della variabile).
- **Azione d'esame**: Arrestare l'algoritmo e dichiarare che il problema è illimitato superiormente (per MAX) con valore ottimo $Z^* \to +\infty$.

## 4. Degenerazione
- **Rilevamento**: Nel tableau, almeno una variabile di base ha termine noto pari a zero (colonna RHS pari a $0$ nelle righe $\ge 1$).
- **Conseguenza**: L'operazione di pivot su quella riga non produrrà alcun aumento nel valore della funzione obiettivo $Z$.
- **Azione d'esame**: Continuare ad applicare normalmente l'algoritmo del simplesso.

## 5. Tie Breaking (Scelta in Caso di Parità)
- **Parità sulla Variabile Entrante**: Due o più variabili non di base hanno lo stesso valore minimo negativo nella riga 0.
  - **Risoluzione**: Selezionare una qualsiasi delle variabili candidate arbitrariamente.
- **Parità sulla Variabile Uscente**: Il test del rapporto minimo produce lo stesso valore minimo per due o più righe.
  - **Risoluzione**: Selezionare una qualsiasi delle righe candidate arbitrariamente. Nota: la variabile non scelta rimarrà in base ma assumerà valore zero (degenerazione).
