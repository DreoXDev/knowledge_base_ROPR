---
type: theory-note
topic: programmazione-non-lineare
status: consolidated
sources:
  - raw_assets/Programmazione Non Lineare/Ottimizzazione non lineare vincolata.pdf
  - raw_assets/Programmazione Non Lineare/PNL Vincolata 4.pdf
reliability: official
---

# Ottimizzazione Non Lineare Vincolata e Condizioni KKT

L'ottimizzazione vincolata si occupa di trovare i minimi o massimi di una funzione $f(x)$ soggetta ad un insieme di vincoli che definiscono la regione ammissibile $\Omega \subseteq \mathbb{R}^n$.

---

## Struttura del Problema

Un generico problema di ottimizzazione vincolata ha la forma:

$$
\begin{aligned}
\min \quad & f(x) \\
\text{s.t. } & g_i(x) = 0 \quad i = 1, \dots, m \quad \text{(vincoli di uguaglianza)} \\
& h_j(x) \le 0 \quad j = 1, \dots, p \quad \text{(vincoli di disuguaglianza)}
\end{aligned}
$$

Qualsiasi vincolo in forma diversa può essere convertito in questa forma standard:
- $A(x) \ge B \iff B - A(x) \le 0$.
- Un problema di massimo $\max f(x)$ equivale a $\min -f(x)$.

---

## Approcci Risolutivi

### 1. Riduzione del Numero di Variabili (Riduzione Dimensionale)
Se i vincoli di uguaglianza $g_i(x) = 0$ sono lineari o facilmente invertibili, è possibile esplicitare $m$ variabili in funzione delle restanti $n-m$ variabili libere. Sostituendo queste espressioni nella funzione obiettivo, si trasforma il problema in uno non vincolato a dimensione ridotta ($n-m$).
- **Limite**: Spesso le relazioni sono complesse o non invertibili univocamente (es. $x^2 + y^2 = 1$).

### 2. Moltiplicatori di Lagrange (Soli Vincoli di Uguaglianza)
Se sono presenti solo vincoli di uguaglianza ($g_i(x) = 0$), definiamo la **funzione Lagrangiana**:
$$L(x, \lambda) = f(x) + \sum_{i=1}^m \lambda_i g_i(x)$$
dove $\lambda_i \in \mathbb{R}$ sono detti moltiplicatori di Lagrange.
Le condizioni necessarie di ottimo del primo ordine impongono l'azzeramento del gradiente della Lagrangiana rispetto a tutte le sue variabili ($x$ e $\lambda$):

$$
\nabla L(x, \lambda) = 0 \implies \begin{cases}
\nabla_x L(x, \lambda) = \nabla f(x) + \sum_{i=1}^m \lambda_i \nabla g_i(x) = 0 \\
\nabla_\lambda L(x, \lambda) = g(x) = 0
\end{cases}
$$

Questo fornisce un sistema di $n + m$ equazioni in $n + m$ incognite.

---

## Condizioni di Karush-Kuhn-Tucker (KKT)

In presenza di vincoli di disuguaglianza ($h_j(x) \le 0$), le condizioni di ottimalità del primo ordine sono estese dalle **condizioni KKT**. Esse costituiscono condizioni **necessarie** per l'ottimalità locale (sotto l'ipotesi di regolarità dei vincoli, come la linearità dei vincoli o l'indipendenza lineare dei gradienti dei vincoli attivi - LICQ).

Definiamo la Lagrangiana generalizzata:
$$L(x, \lambda, \mu) = f(x) + \sum_{i=1}^m \lambda_i g_i(x) + \sum_{j=1}^p \mu_j h_j(x)$$

Per un problema di **minimo**, le condizioni KKT per un punto $x^*$ con moltiplicatori $\lambda^*$ e $\mu^*$ sono:

### 1. Stazionarietà (Stationarity)
Il gradiente della Lagrangiana rispetto a $x$ si annulla in $x^*$:
$$\nabla_x L(x^*, \lambda^*, \mu^*) = \nabla f(x^*) + \sum_{i=1}^m \lambda_i^* \nabla g_i(x^*) + \sum_{j=1}^p \mu_j^* \nabla h_j(x^*) = 0$$

### 2. Ammissibilità Primale (Primal Feasibility)
Il punto $x^*$ deve soddisfare tutti i vincoli del problema:
$$g_i(x^*) = 0 \quad \forall i = 1, \dots, m$$
$$h_j(x^*) \le 0 \quad \forall j = 1, \dots, p$$

### 3. Complementarità degli Scarti (Complementary Slackness)
Per ogni vincolo di disuguaglianza, il prodotto tra il moltiplicatore e il vincolo deve essere nullo:
$$\mu_j^* \cdot h_j(x^*) = 0 \quad \forall j = 1, \dots, p$$

### 4. Ammissibilità Duale (Segno dei moltiplicatori $\mu$)
I moltiplicatori associati ai vincoli di disuguaglianza devono avere un segno concorde con il tipo di ottimizzazione:

- Per problemi di **minimo** (con vincoli $h_j(x) \le 0$):
  $$\mu_j^* \ge 0 \quad \forall j = 1, \dots, p$$
- Per problemi di **massimo** (con vincoli $h_j(x) \le 0$):
  $$\mu_j^* \le 0 \quad \forall j = 1, \dots, p$$

*(Nota: I moltiplicatori $\lambda_i^*$ associati ai vincoli di uguaglianza non hanno vincoli di segno).*

---

## Concetto di Vincolo Attivo e Inattivo

Dato un punto ammissibile $x^*$:
- Un vincolo di disuguaglianza $h_j(x) \le 0$ si dice **attivo** in $x^*$ se $h_j(x^*) = 0$. Il vincolo agisce come un vincolo di uguaglianza sul bordo della regione ammissibile. Il moltiplicatore associato $\mu_j$ può essere diverso da zero ($\mu_j \ge 0$ per min, $\mu_j \le 0$ per max).
- Il vincolo si dice **inattivo** in $x^*$ se $h_j(x^*) < 0$. Il punto si trova all'interno della regione ammissibile rispetto a questo vincolo. Per la complementarità degli scarti, si ha necessariamente:
  $$\mu_j^* = 0$$

Questo comportamento consente di semplificare la ricerca dei punti ottimi analizzando sistematicamente le diverse combinazioni di vincoli attivi (vedi [[pnl_combinatoria_vincoli_attivi]]).
