---
type: method
topic: programmazione_non_lineare
status: active
reliability: official
---

# Condizioni di Karush-Kuhn-Tucker (KKT)

Le condizioni di Karush-Kuhn-Tucker (KKT) forniscono i criteri di ottimalità del primo ordine (condizioni necessarie) per problemi di programmazione non lineare con vincoli di disuguaglianza (e opzionalmente uguaglianza).

---

## Forma Standard del Problema

Per applicare correttamente le regole dei segni di KKT senza commettere errori, ricondurre sempre il problema alla seguente **forma standard**:

$$
\begin{aligned}
\min/\max \quad & f(x) \\
\text{s.t. } & g_i(x) = 0 \quad i = 1, \dots, m \\
& h_j(x) \le 0 \quad j = 1, \dots, p
\end{aligned}
$$

*Regola di conversione vincoli*: Se un vincolo è espresso come $A(x) \ge B$, riscriverlo moltiplicando per $-1$:
$$B - A(x) \le 0$$

---

## Costruzione della Lagrangiana Generalizzata

$$L(x, \lambda, \mu) = f(x) + \sum_{i=1}^m \lambda_i g_i(x) + \sum_{j=1}^p \mu_j h_j(x)$$

dove:
- $\lambda_i \in \mathbb{R}$ sono i moltiplicatori associati ai vincoli di uguaglianza.
- $\mu_j \in \mathbb{R}$ sono i moltiplicatori associati ai vincoli di disuguaglianza.

---

## Sistema KKT Generale

Il punto $x^*$ ed i vettori di moltiplicatori $\lambda^*, \mu^*$ devono soddisfare il seguente sistema:

### 1. Stazionarietà (Stationarity)
$$\nabla_x L(x^*, \lambda^*, \mu^*) = 0 \implies \nabla f(x^*) + \sum_{i=1}^m \lambda_i^* \nabla g_i(x^*) + \sum_{j=1}^p \mu_j^* \nabla h_j(x^*) = 0$$
Questo equivale a un sistema di $n$ equazioni parziali (una per ogni variabile decisionale $x_k$).

### 2. Ammissibilità Primale (Primal Feasibility)
$$\begin{cases}
g_i(x^*) = 0 & i = 1, \dots, m \\
h_j(x^*) \le 0 & j = 1, \dots, p
\end{cases}$$

### 3. Complementarità degli Scarti (Complementary Slackness)
$$\mu_j^* \cdot h_j(x^*) = 0 \quad j = 1, \dots, p$$
*(Se il vincolo è inattivo $h_j(x^*) < 0 \implies \mu_j^* = 0$).*

### 4. Ammissibilità Duale (Segno di $\mu$)
Il segno del moltiplicatore $\mu$ dipende esclusivamente dal senso di ottimizzazione:

- **Per problemi di MINIMO**:
  $$\mu_j^* \ge 0 \quad j = 1, \dots, p$$
- **Per problemi di MASSIMO**:
  $$\mu_j^* \le 0 \quad j = 1, \dots, p$$

*(Nota: I moltiplicatori $\lambda_i^*$ associati ad uguaglianze sono liberi in segno).*

---

## Procedura Risolutiva per Esercizi d'Esame

1. **Riscrivere i vincoli** in forma standard ($g_i(x) = 0$, $h_j(x) \le 0$).
2. **Scrivere la Lagrangiana** $L(x, \lambda, \mu)$.
3. **Calcolare il gradiente** $\nabla_x L$ e formulare le equazioni di stazionarietà.
4. **Scrivere le equazioni di complementarità**: per ciascun vincolo $j$, impostare $\mu_j h_j(x) = 0$.
5. **Risolvere il sistema** esplorando le combinazioni dei vincoli attivi (vedi [[pnl_combinatoria_vincoli_attivi]]).
6. **Filtrare le soluzioni** verificando:
   - Ammissibilità primale ($h_j(x) \le 0$).
   - Ammissibilità duale ($\mu_j \ge 0$ per min, $\mu_j \le 0$ per max).
7. **Valutare** i punti ammissibili trovati per identificare il minimo/massimo globale (o locale).
