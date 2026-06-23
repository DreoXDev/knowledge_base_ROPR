---
type: method
topic: programmazione_non_lineare
status: active
reliability: official
---

# PNL Non Vincolata: Punti Stazionari e Classificazione Hessiana

Questo metodo descrive la procedura sistematica per trovare i punti stazionari di una funzione di due o più variabili senza vincoli e classificarli come minimi locali/globali, massimi locali/globali o punti di sella tramite la matrice Hessiana.

---

## Procedura Operativa Passo-Passo

### 1. Calcolo del Gradiente
Data la funzione $f(x, y)$, calcolare il vettore gradiente $\nabla f(x, y)$:
$$\nabla f(x, y) = \begin{bmatrix} \frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \end{bmatrix}$$

### 2. Ricerca dei Punti Stazionari
Risolvere il sistema di equazioni che annulla il gradiente per trovare i punti stazionari $P^* = (x^*, y^*)$:
$$\nabla f(x, y) = 0 \implies \begin{cases} \frac{\partial f}{\partial x} = 0 \\ \frac{\partial f}{\partial y} = 0 \end{cases}$$

### 3. Calcolo della Matrice Hessiana
Determinare la matrice Hessiana $H_f(x, y)$ calcolando le derivate parziali del secondo ordine:
$$H_f(x, y) = \begin{bmatrix} \frac{\partial^2 f}{\partial x^2} & \frac{\partial^2 f}{\partial x \partial y} \\ \frac{\partial^2 f}{\partial y \partial x} & \frac{\partial^2 f}{\partial y^2} \end{bmatrix}$$
Se $f \in C^2$, la matrice è simmetrica: $\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}$.

### 4. Classificazione dei Punti Stazionari (Test del Secondo Ordine)
Valutare la matrice Hessiana $H_f(x^*, y^*)$ in ciascun punto stazionario $P^*$:

#### Regola Veloce in 2D
Sia $H_f(P^*) = \begin{bmatrix} A & B \\ B & C \end{bmatrix}$. Calcolare il determinante $\det(H_f) = AC - B^2$ e la traccia $\text{tr}(H_f) = A + C$:
- **$\det(H_f) > 0$ e $\text{tr}(H_f) > 0$** (oppure $A > 0$): La matrice è *definita positiva* ($H_f \succ 0$). $P^*$ è un **minimo locale stretto**.
- **$\det(H_f) > 0$ e $\text{tr}(H_f) < 0$** (oppure $A < 0$): La matrice è *definita negativa* ($H_f \prec 0$). $P^*$ è un **massimo locale stretto**.
- **$\det(H_f) < 0$**: La matrice è *indefinita* (autovalori discordi). $P^*$ è un **punto di sella**.
- **$\det(H_f) = 0$**: La matrice è *semidefinita* (almeno un autovalore nullo). Il test del secondo ordine è **inconclusivo**.

### 5. Ottimalità Globale e Convessità
- Se la matrice Hessiana $H_f(x, y)$ è **semidefinita positiva** ($H_f \succeq 0$) per *ogni* $(x, y) \in \mathbb{R}^2$, allora la funzione è **convessa** su tutto lo spazio. Ogni minimo locale $P^*$ è anche **minimo globale**.
- Se la matrice Hessiana $H_f(x, y)$ è **semidefinita negativa** ($H_f \preceq 0$) per *ogni* $(x, y) \in \mathbb{R}^2$, allora la funzione è **concava** su tutto lo spazio. Ogni massimo locale $P^*$ è anche **massimo globale**.
- Se si trova anche un solo punto in cui $H_f(x, y)$ ha determinante negativo (indefinita), la funzione non è né convessa né concava in tutto $\mathbb{R}^2$.

---

## Casi Critici e Risoluzione (Hessiana Semidefinita)

Quando $\det(H_f(P^*)) = 0$, la classificazione del secondo ordine fallisce. È necessario ricorrere a manipolazioni o analisi lungo direzioni/curve:

1. **Analisi lungo curve specifiche**: Valutare $f(x, y)$ lungo rette passanti per il punto (es. $y = x$, $y = 0$, $x = 0$) per vedere se il valore cresce o decresce a seconda della direzione.
2. **Riscrittura algebrica**: Esprimere la funzione come somma di quadrati o fattori per studiare direttamente il segno della differenza $f(x, y) - f(P^*)$.

---

## Esempi Sintetici dall'Asset

### Esempio 1: Test del secondo ordine non conclusivo risolto analiticamente
Sia $f(x, y) = x^4 + x^2y + y^2 + 3$.
1. Gradiente: $\nabla f = \begin{bmatrix} 4x^3 + 2xy \\ x^2 + 2y \end{bmatrix} = 0 \implies P^* = (0, 0)$ unico punto stazionario.
2. Hessiana: $H_f(x, y) = \begin{bmatrix} 12x^2 + 2y & 2x \\ 2x & 2 \end{bmatrix} \implies H_f(0, 0) = \begin{bmatrix} 0 & 0 \\ 0 & 2 \end{bmatrix}$.
3. Poiché $\det(H_f(0, 0)) = 0$, il test è inconclusivo.
4. Risoluzione: Riscriviamo la funzione completando il quadrato per la parte in $y$:
   $$f(x, y) = \frac{1}{2}(x^2 + y)^2 + \frac{x^4}{2} + \frac{y^2}{2} + 3$$
   Poiché i tre termini dipendenti da $x$ e $y$ sono quadrati (e quindi sempre $\ge 0$), si ha:
   $$f(x, y) \ge 3 = f(0, 0) \quad \forall (x, y) \in \mathbb{R}^2$$
   Il punto $P^* = (0, 0)$ è un **minimo globale**.

### Esempio 2: Sella con Hessiana Semidefinita
Sia $f(x, y) = x^4 + y^4 - 2x^2 - 2y^2 + 4xy$.
1. Punti stazionari: $P_0 = (0, 0)$, $P_1 = (\sqrt{2}, -\sqrt{2})$, $P_2 = (-\sqrt{2}, \sqrt{2})$.
2. Hessiana in $P_0$: $H_f(0, 0) = \begin{bmatrix} -4 & 4 \\ 4 & -4 \end{bmatrix} \implies \det(H_f) = 0$ (autovalori $0$ e $-8$). Semidefinita negativa.
3. Risoluzione: Valutiamo $f(x, y)$ lungo la retta $y = x$:
   $$f(x, x) = x^4 + x^4 - 2x^2 - 2x^2 + 4x^2 = 2x^4$$
   Per $x \neq 0$, $f(x, x) = 2x^4 > 0 = f(0, 0)$, il che significa che ci sono punti arbitrariamente vicini a $(0, 0)$ con valore maggiore di $f(0, 0)$, quindi $(0, 0)$ non può essere un massimo locale. Di conseguenza, $P_0$ è un **punto di sella**.

---

## Collegamenti Obsidian
- Metodo del Gradiente: [[pnl_metodo_gradiente_line_search_esatta]]
- Metodo di Newton: [[pnl_metodo_newton_non_vincolata]]
- Condizioni KKT: [[pnl_vincolata_condizioni_KKT]]
