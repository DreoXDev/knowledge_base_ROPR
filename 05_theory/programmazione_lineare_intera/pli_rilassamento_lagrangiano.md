---
type: theory
topic: programmazione_lineare_intera
status: active
sources: [BB PLI.pdf]
reliability: official
---

# Rilassamento Lagrangiano

Il **Rilassamento Lagrangiano** è una tecnica alternativa al rilassamento continuo (LP) per calcolare bound (valutazioni ottimistiche) per problemi di programmazione lineare intera difficile.

## Definizione Matematica

Si consideri un problema di massimo a variabili intere (detto problema primale):

$$
\begin{aligned}
Z^* = \max \quad & c^T x \\
\text{s.t.} \quad & A x \le b \\
& D x \le e \\
& x \in \mathbb{Z}^n
\end{aligned}
$$

Supponiamo che i vincoli $A x \le b$ siano vincoli "difficili" (complicating constraints), la cui rimozione renderebbe il problema estremamente facile da risolvere (es. un problema dello zaino o un cammino minimo).

Il rilassamento lagrangiano consiste nel rimuovere i vincoli difficili dall'insieme dei vincoli e inserirli nella funzione obiettivo penalizzandone la violazione tramite un vettore di moltiplicatori $\lambda \ge 0$ (moltiplicatori lagrangiani).

Il problema rilassato lagrangiano, associato al vettore $\lambda$, è:

$$
Z_R(\lambda) = \max \quad c^T x - \lambda^T (A x - b)
$$
$$
\text{s.t.} \quad D x \le e
$$
$$
x \in \mathbb{Z}^n
$$

---

## Proprietà dei Bound Lagrangiani

Per ogni vettore di moltiplicatori $\lambda \ge 0$, valgono le seguenti proprietà fondamentali:

### 1. Ammissibilità e Ottimalità (Upper Bound per Massimo)
Se $x^*$ è la soluzione ottima del problema originario, essa soddisfa $A x^* \le b$ e $D x^* \le e$, con $x^* \in \mathbb{Z}^n$. Poiché $\lambda \ge 0$ e $A x^* - b \le 0$, si ha $\lambda^T (A x^* - b) \le 0$. Di conseguenza:

$$
c^T x^* \le c^T x^* - \lambda^T (A x^* - b) \le Z_R(\lambda)
$$

Quindi, per qualsiasi $\lambda \ge 0$:
- In problemi di **massimo**: $Z_R(\lambda)$ fornisce un **Upper Bound** ($UB$) per il valore ottimo $Z^*$.
- In problemi di **minimo**: $Z_R(\lambda)$ fornisce un **Lower Bound** ($LB$) per il valore ottimo $Z^*$.

### 2. Duale Lagrangiano
Per ottenere il miglior bound possibile, si cerca di minimizzare l'Upper Bound rispetto a $\lambda$:

$$
Z_{dual} = \min_{\lambda \ge 0} Z_R(\lambda)
$$

Questo problema di minimo è noto come **Duale Lagrangiano**.

---

## Relazione con il Rilassamento Continuo (LP)

Sia $Z_{LP}$ il valore ottimo del rilassamento continuo LP del problema originario. Vale la seguente relazione:

$$
Z^* \le Z_{dual} \le Z_{LP}
$$

Il bound fornito dal duale lagrangiano è **sempre non peggiore** (più stretto o uguale) di quello fornito dal rilassamento lineare continuo del problema originario. La parità $Z_{dual} = Z_{LP}$ si ha solo quando il guscio convesso dell'insieme $\{x \in \mathbb{Z}^n : D x \le e\}$ coincide con il poliedro $\{x \ge 0 : D x \le e\}$.
In molti problemi complessi (come il Traveling Salesperson Problem o il Set Partitioning), il rilassamento lagrangiano fornisce bound estremamente più forti rispetto al semplice rilassamento lineare.
