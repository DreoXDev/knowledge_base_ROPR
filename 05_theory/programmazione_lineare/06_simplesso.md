---
type: theory-note
topic: programmazione-lineare
status: draft
sources:
  - raw_assets/Programmazione Lineare/lezione 3 completa.pdf
reliability: official
---

# L'Algoritmo del Simplesso (Forma Tabellare)

L'algoritmo del simplesso è la procedura standard per risolvere problemi di Programmazione Lineare con molte variabili. Opera spostandosi da un vertice ammissibile ad un altro adiacente migliorando (o lasciando invariato) il valore della funzione obiettivo.

## Conversione in Forma Aumentata

Per applicare il simplesso, il modello deve essere convertito in **forma aumentata** (o forma standard) trasformando i vincoli di disuguaglianza in uguaglianze:

- **Variabili di Slack ($s_i$)**: Aggiunte ai vincoli di tipo $\le$ per rappresentare la risorsa non utilizzata.
  $$
  \sum_{j=1}^n a_{ij} x_j \le b_i \implies \sum_{j=1}^n a_{ij} x_j + s_i = b_i \quad \text{con } s_i \ge 0
  $$

## La Riga Obiettivo (Riga 0)

La funzione obiettivo $Z = \sum c_j x_j$ viene riscritta portando tutte le variabili a sinistra del segno di uguaglianza per formare la **riga 0** del tableau:

$$
Z - \sum_{j=1}^n c_j x_j = 0
$$

## Struttura del Tableau del Simplesso

Il tableau organizza i coefficienti del sistema in forma matriciale:

| Base | $Z$ | $x_1$ | $\dots$ | $x_n$ | $s_1$ | $\dots$ | $s_m$ | RHS ($b$) |
|---|---|---|---|---|---|---|---|---|
| **$Z$** | 1 | $-c_1$ | $\dots$ | $-c_n$ | 0 | $\dots$ | 0 | 0 |
| **$s_1$** | 0 | $a_{11}$ | $\dots$ | $a_{1n}$ | 1 | $\dots$ | 0 | $b_1$ |
| **$\dots$**| 0 | $\dots$ | $\dots$ | $\dots$ | 0 | $\dots$ | 0 | $\dots$ |
| **$s_m$** | 0 | $a_{m1}$ | $\dots$ | $a_{mn}$ | 0 | $\dots$ | 1 | $b_m$ |

## Regole di Pivotaggio

### 1. Scelta della Variabile Entrante
In un problema di massimizzazione, entra in base la variabile non di base che ha il coefficiente **più negativo** nella riga 0. Questo indica l'attività che offre il massimo miglioramento unitario di $Z$.

### 2. Scelta della Variabile Uscente (Test dei Rapporti Minimi)
Per determinare quale variabile esce dalla base per fare spazio a quella entrante, si calcola il rapporto tra il termine noto ($b_i$) e il coefficiente positivo della colonna entrante ($a_{ik} > 0$):

$$
\text{Rapporto} = \frac{b_i}{a_{ik}} \qquad \text{per } a_{ik} > 0
$$

La riga che produce il rapporto minimo definisce la variabile uscente. Questo garantisce di rimanere all'interno della regione ammissibile.

### 3. Operazione di Pivot
Si effettua l'eliminazione gaussiana per rendere pari a 1 il coefficiente all'intersezione tra colonna entrante e riga uscente (elemento pivot) e pari a 0 tutti gli altri elementi della colonna entrante.

## Condizioni Speciali

- **Ottimalità**: Il tableau è ottimo quando tutti i coefficienti nella riga 0 (esclusa la colonna RHS) sono non negativi ($\ge 0$) per problemi di massimizzazione.
- **Illimitatezza**: Se in corrispondenza di una variabile entrante tutti i coefficienti nei vincoli (nella sua colonna) sono non positivi ($\le 0$), il test dei rapporti non può essere calcolato. Il problema è **illimitato** superiormente.

## Esempio Numerico Base

Si consideri il problema:

$$
\max Z = 40x + 50y
$$

soggetto a:

$$
x + 2y \le 40
$$

$$
4x + 3y \le 120
$$

$$
x, y \ge 0
$$

La forma aumentata è:

$$
x + 2y + s_1 = 40
$$

$$
4x + 3y + s_2 = 120
$$

Eseguendo i pivot sul tableau (prima entra $y$, poi entra $x$), si ottiene la soluzione ottima:

$$
x^* = 24, \quad y^* = 8, \quad s_1^* = 0, \quad s_2^* = 0
$$

con valore ottimo $Z^* = 1360$.

## Esercizi Collegati
- [[pl_tool_spa_simplesso|Esercizio Tool.Spa]] ( tableau di grandi dimensioni, verificare soluzioni)
- [[pl_simplesso_max_3x_5y|Esempio simplesso ed ottimizzazione grafica]]

#ropr #programmazione-lineare #teoria #simplesso
