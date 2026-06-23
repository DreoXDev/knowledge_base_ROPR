---
type: solved_example
topic: programmazione_non_lineare
status: active
reliability: official
---

# Esercizi Svolti PNL Non Vincolata: Studio di Funzione (Esercizi 1-5)

Questo file raccoglie le soluzioni complete e strutturate degli Esercizi 1-5 estratti da `PNL_non_vincolata.pdf`. Gli esercizi riguardano la determinazione dei punti stazionari, lo studio della convessità/concavità globale e la classificazione dei punti tramite analisi Hessiana (inclusi i casi semidefiniti inconclusivi).

---

## Esercizio 1

### Testo
Data la funzione $f(x, y) = 2x^2 + y^2 - xy - 2x - 3y$:
1. Trovare tutti i punti stazionari di $f$.
2. Dire se la funzione $f$ è convessa o concava nello spazio $\mathbb{R}^2$.
3. Trovare tutti i punti di minimo locale e massimo locale di $f$.

### Soluzione
1. **Punti stazionari**:
   Il gradiente si annulla in $\nabla f(x, y) = 0$:
   $$\begin{cases}
   \frac{\partial f}{\partial x} = 4x - y - 2 = 0 \implies y = 4x - 2 \\
   \frac{\partial f}{\partial y} = -x + 2y - 3 = 0
   \end{cases}$$
   Sostituendo la prima nella seconda equazione:
   $$-x + 2(4x - 2) - 3 = 0 \implies 7x = 7 \implies x = 1 \implies y = 2$$
   L'unico punto stazionario è **$P^* = (1, 2)$**.

2. **Studio della convessità**:
   Calcoliamo la matrice Hessiana:
   $$H_f(x, y) = \begin{bmatrix} 4 & -1 \\ -1 & 2 \end{bmatrix}$$
   Poiché la matrice è costante su tutto $\mathbb{R}^2$:
   - $\det(H_f) = 4(2) - (-1)^2 = 7 > 0$.
   - $\text{tr}(H_f) = 4 + 2 = 6 > 0$.
   Entrambi gli autovalori sono strettamente positivi, quindi $H_f \succ 0$ (definita positiva) per ogni $(x, y) \in \mathbb{R}^2$.
   La funzione $f$ è **strettamente convessa** in tutto lo spazio $\mathbb{R}^2$.

3. **Classificazione**:
   Essendo la funzione convessa su tutto $\mathbb{R}^2$, l'unico punto stazionario $P^* = (1, 2)$ è un **minimo globale** (e di conseguenza locale). Non esistono punti di massimo.

---

## Esercizio 2

### Testo
Data la funzione $f(x, y) = x^3 + y^3 - 3xy$:
1. Trovare tutti i punti stazionari di $f$.
2. Dire se la funzione $f$ è convessa o concava nello spazio $\mathbb{R}^2$.
3. Trovare tutti i punti di minimo locale e massimo locale di $f$.

### Soluzione
1. **Punti stazionari**:
   $$\begin{cases}
   \frac{\partial f}{\partial x} = 3x^2 - 3y = 0 \implies y = x^2 \\
   \frac{\partial f}{\partial y} = 3y^2 - 3x = 0
   \end{cases}$$
   Sostituendo la prima nella seconda equazione:
   $$3(x^2)^2 - 3x = 0 \implies 3x(x^3 - 1) = 0 \implies x = 0 \quad \text{oppure} \quad x = 1$$
   I punti stazionari sono **$P_0 = (0, 0)$** e **$P_1 = (1, 1)$**.

2. **Studio della convessità**:
   Matrice Hessiana generale:
   $$H_f(x, y) = \begin{bmatrix} 6x & -3 \\ -3 & 6y \end{bmatrix}$$
   Il determinante è $\det(H_f) = 36xy - 9$.
   Valutiamo in un punto a scelta, ad esempio in $P_0(0, 0)$: $\det(H_f(0, 0)) = -9 < 0$. Poiché in questo punto la matrice è indefinita, la funzione **non è né convessa né concava** in tutto lo spazio $\mathbb{R}^2$.

3. **Classificazione**:
   - **Punto $P_0 = (0, 0)$**:
     $\det(H_f(0, 0)) = -9 < 0$. La matrice Hessiana è indefinita, per cui $P_0$ è un **punto di sella**.
   - **Punto $P_1 = (1, 1)$**:
     $$H_f(1, 1) = \begin{bmatrix} 6 & -3 \\ -3 & 6 \end{bmatrix} \implies \det(H_f) = 27 > 0, \quad \text{tr}(H_f) = 12 > 0$$
     La matrice Hessiana in $P_1$ è definita positiva, per cui $P_1$ è un punto di **minimo locale**.

---

## Esercizio 3

### Testo
Data la funzione $f(x, y) = 2x^3 + y^3 - 3x^2 - 3y$:
1. Trovare tutti i punti stazionari di $f$.
2. Dire se la funzione $f$ è convessa o concava nello spazio $\mathbb{R}^2$.
3. Trovare tutti i punti di minimo locale e massimo locale di $f$.

### Soluzione
1. **Punti stazionari**:
   $$\begin{cases}
   \frac{\partial f}{\partial x} = 6x^2 - 6x = 6x(x-1) = 0 \implies x = 0 \quad \text{oppure} \quad x = 1 \\
   \frac{\partial f}{\partial y} = 3y^2 - 3 = 3(y^2-1) = 0 \implies y = 1 \quad \text{oppure} \quad y = -1
   \end{cases}$$
   Le combinazioni forniscono quattro punti stazionari:
   **$P_0 = (0, 1)$**, **$P_1 = (0, -1)$**, **$P_2 = (1, 1)$**, **$P_3 = (1, -1)$**.

2. **Studio della convessità**:
   Matrice Hessiana generale:
   $$H_f(x, y) = \begin{bmatrix} 12x - 6 & 0 \\ 0 & 6y \end{bmatrix}$$
   Valutando ad esempio in $P_0(0, 1)$:
   $$H_f(0, 1) = \begin{bmatrix} -6 & 0 \\ 0 & 6 \end{bmatrix} \implies \det(H_f) = -36 < 0$$
   Poiché la matrice è indefinita in un punto, la funzione **non è né convessa né concava** globalmente.

3. **Classificazione**:
   - **$P_0 = (0, 1)$**: $\det(H_f) = -36 < 0 \implies$ **Punto di sella**.
   - **$P_1 = (0, -1)$**:
     $$H_f(0, -1) = \begin{bmatrix} -6 & 0 \\ 0 & -6 \end{bmatrix} \implies \det(H_f) = 36 > 0, \quad \text{tr}(H_f) = -12 < 0 \implies \text{\textbf{Massimo locale}}.$$
   - **$P_2 = (1, 1)$**:
     $$H_f(1, 1) = \begin{bmatrix} 6 & 0 \\ 0 & 6 \end{bmatrix} \implies \det(H_f) = 36 > 0, \quad \text{tr}(H_f) = 12 > 0 \implies \text{\textbf{Minimo locale}}.$$
   - **$P_3 = (1, -1)$**:
     $$H_f(1, -1) = \begin{bmatrix} 6 & 0 \\ 0 & -6 \end{bmatrix} \implies \det(H_f) = -36 < 0 \implies$ **Punto di sella**.

---

## Esercizio 4

### Testo
Data la funzione $f(x, y) = x^4 + x^2y + y^2 + 3$:
1. Trovare tutti i punti stazionari di $f$.
2. Dire se la funzione $f$ è convessa o concava nello spazio $\mathbb{R}^2$.
3. Trovare tutti i punti di minimo locale e massimo locale di $f$.

### Soluzione
1. **Punti stazionari**:
   $$\begin{cases}
   \frac{\partial f}{\partial x} = 4x^3 + 2xy = 2x(2x^2 + y) = 0 \\
   \frac{\partial f}{\partial y} = x^2 + 2y = 0 \implies y = -\frac{1}{2}x^2
   \end{cases}$$
   Sostituendo $y$ nella prima equazione:
   $$2x\left(2x^2 - \frac{1}{2}x^2\right) = 0 \implies 3x^3 = 0 \implies x = 0 \implies y = 0$$
   L'unico punto stazionario è **$P^* = (0, 0)$**.

2. **Studio della convessità**:
   Matrice Hessiana generale:
   $$H_f(x, y) = \begin{bmatrix} 12x^2 + 2y & 2x \\ 2x & 2 \end{bmatrix}$$
   Valutiamo in un punto a piacere, ad esempio $(0, -1)$:
   $$H_f(0, -1) = \begin{bmatrix} -2 & 0 \\ 0 & 2 \end{bmatrix} \implies \det(H_f) = -4 < 0$$
   La matrice è indefinita in questo punto, quindi la funzione **non è né convessa né concava** globalmente.

3. **Classificazione**:
   Valutiamo l'Hessiana nel punto stazionario $P^*(0, 0)$:
   $$H_f(0, 0) = \begin{bmatrix} 0 & 0 \\ 0 & 2 \end{bmatrix} \implies \det(H_f) = 0$$
   Il test del secondo ordine è **inconclusivo** (matrice semidefinita positiva, autovalori $0$ e $2$).
   
   *Risoluzione analitica globale*:
   Completiamo il quadrato rispetto alle variabili dipendenti da $y$:
   $$f(x, y) = y^2 + x^2y + x^4 + 3 = \left(y + \frac{1}{2}x^2\right)^2 - \frac{1}{4}x^4 + x^4 + 3 = \left(y + \frac{1}{2}x^2\right)^2 + \frac{3}{4}x^4 + 3$$
   Poiché $\left(y + \frac{1}{2}x^2\right)^2 \ge 0$ e $\frac{3}{4}x^4 \ge 0$ per ogni $(x, y)$, si ottiene:
   $$f(x, y) \ge 3 = f(0, 0) \quad \forall (x, y) \in \mathbb{R}^2$$
   Pertanto, il punto $P^* = (0, 0)$ è un punto di **minimo globale** (ed anche locale).

---

## Esercizio 5

### Testo
Data la funzione $f(x, y) = x^4 + y^4 - 2x^2 - 2y^2 + 4xy$:
1. Trovare tutti i punti stazionari di $f$.
2. Dire se la funzione $f$ è convessa o concava nello spazio $\mathbb{R}^2$.
3. Trovare tutti i punti di minimo locale e massimo locale di $f$.

### Soluzione
1. **Punti stazionari**:
   $$\begin{cases}
   \frac{\partial f}{\partial x} = 4x^3 - 4x + 4y = 0 \implies y = x - x^3 \\
   \frac{\partial f}{\partial y} = 4y^3 - 4y + 4x = 0 \implies x = y - y^3
   \end{cases}$$
   Sottraendo le due equazioni:
   $$4(x^3 - y^3) - 8(x - y) = 0 \implies 4(x - y)(x^2 + xy + y^2 - 2) = 0$$
   - Sotto-caso 1: $x = y$. Sostituendo nella prima: $x - x^3 = x \implies x^3 = 0 \implies x = 0 \implies y = 0$. Otteniamo il punto **$P_0 = (0, 0)$**.
   - Sotto-caso 2: $x^2 + xy + y^2 = 2$. Sommando le equazioni iniziali:
     $$4(x^3 + y^3) = 0 \implies x^3 + y^3 = 0 \implies y = -x$$
     Sostituendo $y = -x$ nella prima: $-x = x - x^3 \implies x^3 - 2x = 0 \implies x(x^2 - 2) = 0 \implies x = \pm\sqrt{2} \implies y = \mp\sqrt{2}$.
     Otteniamo i punti **$P_1 = (\sqrt{2}, -\sqrt{2})$** e **$P_2 = (-\sqrt{2}, \sqrt{2})$**.

2. **Studio della convessità**:
   Matrice Hessiana generale:
   $$H_f(x, y) = \begin{bmatrix} 12x^2 - 4 & 4 \\ 4 & 12y^2 - 4 \end{bmatrix}$$
   Valutiamo in $(1/2, 1/2)$:
   $$H_f(1/2, 1/2) = \begin{bmatrix} -1 & 4 \\ 4 & -1 \end{bmatrix} \implies \det(H_f) = 1 - 16 = -15 < 0$$
   La matrice è indefinita in questo punto, quindi la funzione **non è né convessa né concava** globalmente.

3. **Classificazione**:
   - **Punto $P_0 = (0, 0)$**:
     $$H_f(0, 0) = \begin{bmatrix} -4 & 4 \\ 4 & -4 \end{bmatrix} \implies \det(H_f) = 0$$
     Il test del secondo ordine è inconclusivo (matrice semidefinita negativa, autovalori $0$ e $-8$).
     Analisi lungo la direzione $y = x$:
     $$f(x, x) = x^4 + x^4 - 2x^2 - 2x^2 + 4x^2 = 2x^4 > 0 = f(0, 0) \quad \text{per } x \neq 0$$
     Ciò mostra che lungo la diagonale la funzione cresce allontanandosi dall'origine, quindi $P_0$ non può essere un massimo locale. Poiché l'Hessiana è semidefinita negativa, non può essere un minimo locale. Pertanto, $P_0 = (0, 0)$ è un **punto di sella**.
   - **Punti $P_1 = (\sqrt{2}, -\sqrt{2})$ e $P_2 = (-\sqrt{2}, \sqrt{2})$**:
     Valutando l'Hessiana in entrambi i punti (in cui i quadrati $x^2$ e $y^2$ valgono $2$):
     $$H_f(P_1) = H_f(P_2) = \begin{bmatrix} 12(2) - 4 & 4 \\ 4 & 12(2) - 4 \end{bmatrix} = \begin{bmatrix} 20 & 4 \\ 4 & 20 \end{bmatrix}$$
     - $\det(H_f) = 20^2 - 4^2 = 384 > 0$.
     - $\text{tr}(H_f) = 20 + 20 = 40 > 0$.
     La matrice è definita positiva, per cui $P_1$ e $P_2$ sono punti di **minimo locale**.

---

## Collegamenti Obsidian
- Metodo di classificazione: [[pnl_non_vincolata_punti_stazionari_hessiana]]
- Esercizi algoritmici gradiente/Newton: [[pnl_non_vincolata_gradiente_newton]]
