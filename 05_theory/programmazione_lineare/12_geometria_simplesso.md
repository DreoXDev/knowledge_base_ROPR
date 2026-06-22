---
materia: ROPR
area: Programmazione Lineare
tipo: teoria
fonte: Ricerca Operativa - Teoria del Simplesso - 23-24.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - simplesso
  - geometria
  - iperpiani
  - frontiere
---

# Geometria del simplesso: Iperpiani, Frontiere e Vertici

Il funzionamento del metodo del simplesso poggia su una solida base geometrica legata alle proprietà dei poliedri convessi definiti dai vincoli di un problema di Programmazione Lineare.

## 1. Iperpiani ed Equazioni di Frontiera

Ciascun vincolo del problema definisce una frontiera geometrica nello spazio delle variabili.

### Vincoli Funzionali
Per un generico vincolo lineare del tipo:
$$
a_{i1}x_1 + a_{i2}x_2 + \dots + a_{in}x_n \le b_i \quad (\text{oppure } \ge b_i)
$$
l'**equazione di frontiera** associata si ottiene imponendo l'uguaglianza stretta:
$$
a_{i1}x_1 + a_{i2}x_2 + \dots + a_{in}x_n = b_i
$$

### Vincoli di Non Negatività
Per ciascuna variabile decisionale con vincolo $x_j \ge 0$, l'equazione di frontiera è:
$$
x_j = 0
$$

### Definizione di Iperpiano
- Ogni equazione di frontiera definisce un **iperpiano** nello spazio $\mathbb{R}^n$ (in $2$ dimensioni è una retta, in $3$ dimensioni un piano, in dimensione $n$ un iperpiano di dimensione $n-1$).
- Un vincolo di disuguaglianza ($\le$ o $\ge$) divide lo spazio in due semispazi: uno di punti ammissibili e uno di punti non ammissibili.
- Un vincolo di uguaglianza ($=$) restringe lo spazio ammissibile esclusivamente ai punti giacenti sull'iperpiano stesso.

---

## 2. Frontiera della Regione Ammissibile

> **Definizione**: La frontiera della regione ammissibile contiene le soluzioni ammissibili che soddisfano una o più equazioni di frontiera. Geometricamente, ogni punto sulla frontiera giace su uno o più iperpiani associati ai vincoli attivi del problema.

### Collegamento con Wyndor Glass Co.
Nel problema di Wyndor Glass Co. ($n=2$ variabili):
- Ci sono $5$ vincoli in totale: $3$ funzionali e $2$ di non negatività.
- Vi sono di conseguenza $5$ equazioni di frontiera (ciascuna rappresentata da una retta nel piano):
  1. $x_1 = 4$
  2. $2x_2 = 12$
  3. $3x_1 + 2x_2 = 18$
  4. $x_1 = 0$
  5. $x_2 = 0$
- I segmenti di queste cinque rette che delimitano la regione di spazio comune e ammissibile formano il bordo (la frontiera) del poligono ammissibile.

---

## 3. Vertici, Spigoli e Adiacenza

- **Vertice (o Punto di Intersezione di Frontiera)**: Un punto dello spazio $\mathbb{R}^n$ determinato dall'intersezione di $n$ frontiere di vincolo linearmente indipendenti.
- **Vertice Ammissibile**: Un vertice che soddisfa tutti i vincoli del problema. Corrisponde a una soluzione di base ammissibile.
- **Vertice Non Ammissibile**: Un vertice ottenuto dall'intersezione di $n$ frontiere ma che viola almeno uno dei restanti vincoli.
- **Spigolo**: Il segmento che unisce due vertici adiacenti. Corrisponde all'intersezione di $n-1$ frontiere di vincolo condivise dai due vertici.
- **Vertici Adiacenti**: Due vertici ammissibili sono adiacenti se condividono $n-1$ frontiere di vincoli attive.

---

## 4. Test di Ottimalità Geometrico

> **Teorema**: Se una soluzione vertice ammissibile non ha vertici ammissibili adiacenti con un valore migliore della funzione obiettivo, allora essa è una soluzione ottima globale del problema di PL.

### Analisi dei Vertici e Adiacenza in Wyndor Glass
Poiché $n=2$, i vertici adiacenti condividono $n-1 = 1$ retta di frontiera.

| Vertice ammissibile | Vertici adiacenti |
|---|---|
| $(0,0)$ | $(0,6)$, $(4,0)$ |
| $(0,6)$ | $(2,6)$, $(0,0)$ |
| $(2,6)$ | $(4,3)$, $(0,6)$ |
| $(4,3)$ | $(4,0)$, $(2,6)$ |
| $(4,0)$ | $(0,0)$, $(4,3)$ |

Valutazione di $Z = 3x_1 + 5x_2$ sui vertici ammissibili:

| Vertice $(x_1, x_2)$ | Valore di $Z$ | Stato |
|---|---:|---|
| $(0,0)$ | $0$ | Non ottimo |
| $(0,6)$ | $30$ | Non ottimo |
| $(2,6)$ | $36$ | **Ottimo** |
| $(4,3)$ | $27$ | Non ottimo |
| $(4,0)$ | $12$ | Non ottimo |

Il simplesso geometrico, partendo da $(0,0)$, si sposta lungo lo spigolo fino a $(0,6)$ e successivamente a $(2,6)$. Dal vertice $(2,6)$, i vertici adiacenti sono $(0,6)$ con $Z=30$ e $(4,3)$ con $Z=27$. Poiché nessuno dei due migliora il valore $36$, $(2,6)$ viene identificato come ottimo globale.
