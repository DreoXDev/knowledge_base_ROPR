---
type: method-card
topic: programmazione-lineare
status: draft
sources:
  - raw_assets/Programmazione Lineare/lezione 3 completa.pdf
reliability: official
---

# Method Card — Risoluzione con il Simplesso Tabellare

## Input Richiesto
Un modello di PL formulato in forma standard di massimizzazione (o minimizzazione).

## Procedura Passo-Passo

### 1. Trasformazione in Forma Aumentata
- Per ogni vincolo di tipo $\le$ con termine noto positivo, aggiungere una variabile di slack non negativa:
  $$
  a_{i1} x_1 + a_{i2} x_2 \le b_i \implies a_{i1} x_1 + a_{i2} x_2 + s_i = b_i \quad (s_i \ge 0)
  $$
- Riscrivere la funzione obiettivo portando tutte le variabili a sinistra dell'uguale:
  $$
  Z - c_1 x_1 - c_2 x_2 = 0
  $$

### 2. Costruzione del Tableau Iniziale
- Le variabili di slack costituiscono la base iniziale (valori RHS positivi).
- Disporre i coefficienti nel tableau organizzandoli per righe. La riga 0 è la riga obiettivo.

### 3. Criterio di Ottimalità (Massimizzazione)
- Se tutti i coefficienti nella riga 0 (esclusa la colonna dei termini noti RHS) sono **non negativi** ($\ge 0$), il tableau è ottimo.
- La soluzione ottima si legge impostando a 0 le variabili non in base (non presenti nella colonna di sinistra) e leggendo il valore di quelle in base direttamente sulla colonna RHS.

### 4. Scelta della Variabile Entrante
- Se il tableau non è ottimo, scegliere la variabile con il coefficiente **più negativo** nella riga 0. La colonna di questa variabile diventa la *colonna pivot*.

### 5. Scelta della Variabile Uscente (Test dei Rapporti Minimi)
- Per ogni riga dei vincoli (esclusa la riga 0), calcolare il rapporto tra il termine noto (RHS) e il coefficiente corrispondente nella colonna pivot, **solamente se quest'ultimo è strettamente maggiore di zero ($> 0$)**.
- La riga associata al **rapporto minimo** definisce la variabile uscente. La riga di questa variabile diventa la *riga pivot*.
- Se tutti i coefficienti nella colonna pivot sono $\le 0$, il problema è **illimitato** e la procedura si arresta.

### 6. Operazione di Pivot
- Individuare l'elemento pivot $P$ all'intersezione tra colonna pivot e riga pivot.
- Dividere la riga pivot per $P$ per rendere l'elemento pivot uguale a 1.
- Effettuare combinazioni lineari tra la riga pivot modificata e tutte le altre righe (compresa la riga 0) per azzerare i restanti elementi della colonna pivot.
- Ripetere dal punto 3.

## Formato di Risposta da Esame

Per ogni iterazione, specificare chiaramente sul foglio:
1. Variabile entrante e variabile uscente.
2. Elemento pivot e tableau risultante dall'operazione.
3. Al passo finale, dichiarare esplicitamente la soluzione ottima:
   $$
   (x_1^*, x_2^*, \dots, s_m^*) = (\dots) \quad \text{con } Z^* = \dots
   $$
   o dichiarare che il problema è illimitato/non ammissibile.
