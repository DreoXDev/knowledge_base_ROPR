---
materia: ROPR
area: Programmazione Lineare
tipo: teoria
fonte: Ricerca Operativa - Metodo del Simplesso - 23-24.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - simplesso
  - simplesso-tabellare
  - tableau
---

# Simplesso in forma tabellare

La forma tabellare è la rappresentazione standard per applicare l'algoritmo del simplesso in modo compatto e calcolare sistematicamente le iterazioni tramite operazioni di pivot.

## Preparazione del Tableau

1. **Aumentare il modello**: Convertire i vincoli in uguaglianze inserendo variabili di slack $s_i$.
2. **Riscrivere l'obiettivo (Riga 0)**: Portare tutte le variabili al membro sinistro dell'uguaglianza:
   $$
   Z - c_1x_1 - c_2x_2 - \dots - c_nx_n = 0
   $$
3. **Inizializzare il tableau**: Inserire i coefficienti del sistema lineare organizzati per righe, ponendo a sinistra le variabili in base (inizialmente le variabili di slack $s_i$).

## Le Regole Operative del Tableau (Problema di MAX)

### 1. Scelta della Variabile Entrante
- Si analizza la riga 0 (esclusa la colonna RHS).
- Entra in base la variabile non di base associata al **coefficiente più negativo** nella riga 0.
- **Criterio di Ottimalità**: Se tutti i coefficienti nella riga 0 sono non negativi ($\ge 0$), la soluzione corrente è **ottima** e l'algoritmo si arresta.

### 2. Scelta della Variabile Uscente (Test dei Rapporti Minimi)
- Si considera la colonna della variabile entrante (detta *colonna pivot*).
- Per ciascuna riga dei vincoli (righe $\ge 1$), calcolare il rapporto:
   $$
   \text{Rapporto} = \frac{\text{Termine noto (RHS)}}{\text{Coefficiente nella colonna pivot}}
   $$
- **Vincolo**: Il calcolo si effettua **esclusivamente** per le righe che presentano un coefficiente strettamente positivo ($> 0$) nella colonna pivot.
- La riga associata al **minimo rapporto non negativo** determina la variabile uscente (e diventa la *riga pivot*).
- Se nessun elemento nella colonna pivot è positivo ($\le 0$), il problema è **illimitato** e la procedura si arresta.

### 3. Operazione di Pivotaggio
Il coefficiente all'intersezione tra colonna pivot e riga pivot è l'**elemento pivot** $P$.
1. **Normalizzazione**: Dividere tutti gli elementi della riga pivot per $P$ in modo da renderlo pari a $1$.
2. **Eliminazione Gaussiana**: Sostituire ciascuna delle altre righe $R_i$ (inclusa la riga 0) con:
   $$
   R_i \leftarrow R_i - c \cdot R_{\text{pivot}}
   $$
   dove $c$ è il valore della colonna pivot nella riga $R_i$, così da azzerare tutti gli altri elementi della colonna pivot.
3. **Aggiornamento Base**: Sostituire nella colonna della base la variabile uscente con quella entrante.

---

## Schema per lo Scritto d'Esame

Quando si risolve un esercizio sul simplesso:
1. Dichiarare la conversione del problema in forma aumentata.
2. Disegnare il **Tableau Iniziale (Iterazione 0)**.
3. Indicare chiaramente a lato del tableau:
   - Variabile entrante (colonna pivot);
   - Calcolo dei rapporti minimi per ciascuna riga candidata;
   - Variabile uscente (riga pivot) ed elemento pivot.
4. Riportare il tableau successivo e ripetere fino al tableau ottimo.
5. **Leggere la Soluzione Ottima**:
   - Impostare a 0 le variabili non in base.
   - Leggere i valori ottimi delle variabili di base direttamente dalla colonna RHS.
   - Leggere $Z^*$ come termine noto della riga 0 nella colonna RHS.
   - Fornire la stringa finale $(x_1^*, \dots, s_m^*) = (\dots)$ con il valore ottimo $Z^* = \dots$
