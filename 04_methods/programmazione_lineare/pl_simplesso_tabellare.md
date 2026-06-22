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
  - simplesso-tabellare
  - method-card
---

# METHOD CARD — Risoluzione con il Simplesso Tabellare

## Quando usarla

Usare questa card quando l'esercizio richiede espressamente di risolvere un problema di Programmazione Lineare tramite il metodo del simplesso o quando la traccia presenta un tableau da completare o analizzare.

## Procedura Operativa Passo-Passo

### 1. Preparazione e Forma Aumentata
- Convertire il modello in forma aumentata introducendo le variabili di slack ($s_i \ge 0$) per i vincoli di tipo $\le$.
- Riscrivere la funzione obiettivo portando tutte le variabili a sinistra dell'uguaglianza, ottenendo la **riga 0**:
  $$
  Z - c_1x_1 - c_2x_2 - \dots - c_nx_n = 0
  $$
- Disporre i coefficienti nel tableau iniziale. Le variabili in base sono inizialmente le variabili di slack.

### 2. Test di Ottimalità (per problemi di MAX)
- Esaminare la riga 0 (escludendo la colonna dei termini noti RHS).
- Se tutti i coefficienti sono non negativi ($\ge 0$), il tableau corrente è **ottimo**. Arrestare l'algoritmo.
- Se ci sono uno o più coefficienti negativi ($< 0$), procedere al punto 3.

### 3. Selezione della Variabile Entrante
- Scegliere la variabile associata al coefficiente **più negativo** nella riga 0. La colonna di questa variabile diventa la *colonna pivot*.

### 4. Selezione della Variabile Uscente (Test dei Rapporti Minimi)
- Per ciascuna riga dei vincoli (righe $\ge 1$), calcolare il rapporto:
  $$
  \text{Rapporto} = \frac{\text{Termine noto (RHS)}}{\text{Coefficiente nella colonna pivot}}
  $$
- **Importante**: Eseguire il calcolo **solo se il coefficiente nella colonna pivot è strettamente positivo ($> 0$)**. Ignorare elementi nulli o negativi.
- La riga associata al **minimo rapporto non negativo** determina la variabile uscente (e diventa la *riga pivot*).
- Se tutti i coefficienti nella colonna pivot sono $\le 0$, l'algoritmo si arresta: il problema è **illimitato** ($Z^* \to +\infty$).

### 5. Operazione di Pivot
- Individuare l'elemento pivot $P$ all'incrocio tra la colonna pivot e la riga pivot.
- Dividere l'intera riga pivot per $P$ per renderlo uguale a $1$.
- Sotttrarre opportuni multipli della riga pivot normalizzata da tutte le altre righe (inclusa la riga 0) in modo da azzerare tutti gli altri elementi della colonna pivot.
- Aggiornare la base sostituendo la variabile uscente con quella entrante.
- Ritornare al punto 2.

## Lettura della Soluzione Ottima

Una volta raggiunto il tableau ottimo:
- **Variabili in base**: Assumono il valore del termine noto (colonna RHS) nella riga in cui hanno coefficiente pari a $1$.
- **Variabili fuori base**: Assumono valore pari a $0$.
- **Valore Ottimo ($Z^*$)**: Corrisponde al valore presente nella colonna RHS della riga 0.
