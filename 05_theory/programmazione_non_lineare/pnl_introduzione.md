---
type: theory-note
topic: programmazione-non-lineare
status: consolidated
sources:
  - raw_assets/Programmazione Non Lineare/PNL.pdf
  - raw_assets/Programmazione Non Lineare/PNL_nonvincolata.pdf
reliability: official
---

# Introduzione alla Programmazione Non Lineare

La **Programmazione Non Lineare (PNL)** si occupa di problemi di ottimizzazione matematica in cui la funzione obiettivo e/o almeno uno dei vincoli presentano carattere non lineare.

## Formulazione Generale

Un problema di programmazione non lineare può essere formulato come:

$$
\begin{aligned}
\text{opt } & f(x) \\
\text{s.t. } & g_i(x) = 0 \quad i = 1, \dots, m \\
& h_j(x) \le 0 \quad j = 1, \dots, p \\
& x \in \mathbb{R}^n
\end{aligned}
$$

dove:
- $f: \mathbb{R}^n \to \mathbb{R}$ è la funzione obiettivo.
- $g_i: \mathbb{R}^n \to \mathbb{R}$ sono i vincoli di uguaglianza.
- $h_j: \mathbb{R}^n \to \mathbb{R}$ sono i vincoli di disuguaglianza.
- $\text{opt}$ può rappresentare minimizzazione ($\min$) o massimizzazione ($\max$).

Se tutte le funzioni $f, g_i, h_j$ sono lineari, si ricade nel caso classico della Programmazione Lineare (PL). Se invece almeno una di esse non lo è, il problema è non lineare.

---

## Applicazioni Tipiche

Molte situazioni reali presentano non linearità intrinseche che rendono inadeguati i modelli lineari:

### 1. Mix di Prodotti con Elasticità del Prezzo
Nei modelli di PL classici si assume che il prezzo unitario di vendita dei prodotti sia costante. Nella realtà si riscontra l'**elasticità del prezzo**: per vendere una quantità maggiore $x_k$ di un bene, è necessario abbassarne il prezzo unitario $p_k(x_k)$. 
Ad esempio, supponiamo che il prezzo sia una funzione lineare decrescente della quantità:
$$p(x) = d - c \cdot x$$
I ricavi complessivi sono dati da:
$$R(x) = x \cdot p(x) = d \cdot x - c \cdot x^2$$
La presenza del termine quadratico $-c \cdot x^2$ introduce una non linearità nella funzione obiettivo.

### 2. Costi Marginali Variabili ed Economie di Scala
Il costo di produzione marginale può variare a seconda del volume di produzione $x$:
- **Curve di apprendimento**: l'efficienza cresce con l'esperienza, facendo diminuire il costo marginale per grandi volumi.
- **Sconti sulle quantità (trasporti)**: sconti sul volume per grandi spedizioni riducono il costo unitario non linearmente.

### 3. Problema dello Zaino Quadratico (Quadratic Knapsack)
Si differenzia dal problema dello zaino lineare per la presenza di sinergie o incompatibilità tra coppie di oggetti selezionati. Se gli oggetti $i$ e $j$ sono entrambi selezionati, si ottiene un'utilità extra $c_{ij}$:
$$
\begin{aligned}
\max \quad & \sum_{i=1}^n v_i x_i + \sum_{i=1}^{n-1} \sum_{j=i+1}^n c_{ij} x_i x_j \\
\text{s.t. } & \sum_{i=1}^n w_i x_i \le C \\
& x_i \in \{0, 1\} \quad \forall i = 1, \dots, n
\end{aligned}
$$

### 4. Ottimizzazione di Portafoglio (Modello di Markowitz)
Il problema consiste nell'allocare quote di capitale $x_i$ tra $n$ asset finanziari in modo da massimizzare il rendimento atteso minimizzando al contempo il rischio (misurato tramite la varianza del portafoglio):
$$
\begin{aligned}
\min \quad & \sum_{i=1}^n \sum_{j=1}^n \sigma_{ij} x_i x_j \\
\text{s.t. } & \sum_{i=1}^n \mu_i x_i \ge R_{\text{min}} \\
& \sum_{i=1}^n x_i = 1 \\
& x_i \ge 0 \quad \forall i = 1, \dots, n
\end{aligned}
$$
dove $\sigma_{ij}$ rappresenta la covarianza tra i rendimenti degli asset $i$ e $j$, e $\mu_i$ il rendimento atteso dell'asset $i$. La funzione obiettivo è quadratica.
