---
type: theory
topic: programmazione_lineare_intera
status: active
sources: [BB PLI.pdf]
reliability: official
---

# Branch and Bound per Programmazione Lineare Intera Mista (PLIM)

I problemi di **Programmazione Lineare Intera Mista (PLIM / MILP)** presentano sia variabili vincolate a assumere valori interi sia variabili continue.

## Modello Generale PLIM

Un problema PLIM generico di massimizzazione si presenta nella forma:

$$
\begin{aligned}
\max \quad & z = c^T x + d^T y \\
\text{s.t.} \quad & A x + G y \le b \\
& x \ge 0, \ y \ge 0 \\
& x \in \mathbb{Z}^n \\
& y \in \mathbb{R}^p
\end{aligned}
$$

dove:
- $x$ è il vettore delle $n$ variabili vincolate a essere **intere** (o binarie).
- $y$ è il vettore delle $p$ variabili **continue**.

---

## Regole Operative Specifiche per il PLIM

La presenza di variabili continue introduce due variazioni fondamentali nell'applicazione del Branch and Bound:

### 1. Selezione della Variabile di Branching
La ramificazione (branching) può essere effettuata **esclusivamente** sulle variabili vincolate a essere intere ($x$). 
- Se nella soluzione del rilassamento continuo $\bar{x}_j$ assume un valore frazionario per qualche $j \in \{1, \dots, n\}$, allora si esegue il branching su $x_j$.
- Le variabili continue $y$ **non** devono essere sottoposte a branching, anche se assumono valori frazionari.

### 2. Condizione di Ammissibilità Intera
Un nodo fornisce una soluzione intera ammissibile (e quindi può essere potato per ottimalità intera ed eventualmente aggiornare l'incumbent $Z_I$) se:
- Tutte le variabili vincolate ad essere intere ($x$) assumono valori interi nella soluzione ottima del rilassamento continuo del nodo.
- Le variabili continue ($y$) possono assumere qualsiasi valore reale frazionario.

### 3. Divieto di Arrotondamento del Bound
In un problema PLI puro (dove tutte le variabili e i coefficienti dei vincoli e dell'obiettivo sono interi), il bound fornito dal rilassamento continuo può essere arrotondato all'intero più vicino (per difetto in caso di massimo, per eccesso in caso di minimo).

> [!WARNING]
> Nel caso di problemi **PLIM** (o se sono presenti coefficienti non interi), **non è lecito arrotondare il bound**. La presenza di variabili continue fa sì che il valore ottimo del problema intero misto $z^*$ possa essere frazionario. Pertanto, i bound frazionari dei rilassamenti LP devono essere mantenuti esattamente come calcolati.

---

## Esempio di Branching Multiplo
Poiché le variabili continue non subiscono branching, lo spazio discreto delle variabili intere è più limitato, ma una singola variabile intera può subire branching più volte lungo percorsi diversi dell'albero man mano che i vincoli sulle altre variabili cambiano.
Confronto tra le tipologie di problemi:

| Categoria | Dominio Variabili | Ramificazione Tipica | Criterio di Interezza |
|---|---|---|---|
| **PB (Binario puro)** | $x_j \in \{0, 1\}$ | $x_j = 0$ oppure $x_j = 1$ | Tutte le variabili sono $0$ o $1$ |
| **PLI (Intero puro)** | $x_j \in \mathbb{Z}$ | $x_j \le \lfloor \bar{x}_j \rfloor$ e $x_j \ge \lceil \bar{x}_j \rceil$ | Tutte le variabili sono intere |
| **PLIM (Misto)** | $x_j \in \mathbb{Z}$, $y_k \in \mathbb{R}$ | Branching solo sulle $x_j$ | Solo le variabili $x_j$ devono essere intere |
