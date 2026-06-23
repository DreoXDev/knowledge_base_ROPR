---
type: method
topic: programmazione_non_lineare
status: active
reliability: official
---

# Metodo del Gradiente (Steepest Descent) con Line Search Esatta

Il metodo del gradiente è un algoritmo per la minimizzazione non vincolata di una funzione multivariabile $f(x)$. Ad ogni iterazione si sposta lungo la direzione di massima discesa locale, definita dal gradiente negativo.

---

## Formula di Aggiornamento

$$x_{k+1} = x_k + \alpha_k d_k$$

dove:
- $d_k = -\nabla f(x_k)$ è la direzione di discesa (gradiente negativo).
- $\alpha_k > 0$ è la lunghezza del passo, calcolata tramite **line search esatta**.

---

## Procedura Operativa Passo-Passo

### 1. Inizializzazione
- Selezionare un punto di partenza $x_0 \in \mathbb{R}^n$.
- Fissare la tolleranza $\epsilon > 0$ (generalmente riferita alla norma del gradiente: $\|\nabla f(x_k)\| < \epsilon$).
- Impostare il contatore $k = 0$.

### 2. Passo Iterativo (Iterazione $k$)
1. **Calcolo del Gradiente**:
   Calcolare il vettore gradiente $\nabla f(x_k)$.
2. **Verifica Arresto**:
   Se $\|\nabla f(x_k)\| < \epsilon$, fermarsi. Il punto corrente $x_k$ è la soluzione ottimale.
3. **Determinazione della Direzione**:
   $$d_k = -\nabla f(x_k)$$
4. **Line Search Esatta (Monodimensionale)**:
   Definire la funzione del passo $\alpha$:
   $$\phi(\alpha) = f(x_k + \alpha d_k) = f(x_k - \alpha \nabla f(x_k))$$
   Trovare il passo ottimale $\alpha_k$ che minimizza $\phi(\alpha)$ per $\alpha \ge 0$:
   $$\frac{d\phi(\alpha)}{d\alpha} = 0 \implies \alpha_k$$
   *(Nota: Analiticamente si esprime $x_k + \alpha d_k$ in termini di $\alpha$, si sostituisce nella funzione obiettivo, si deriva rispetto ad $\alpha$ e si pone uguale a zero).*
5. **Aggiornamento del Punto**:
   $$x_{k+1} = x_k + \alpha_k d_k$$
6. Incrementare $k = k + 1$ e tornare al punto 1.

---

## Esempio Numerico Svolto

Minimizzare $f(x, y) = x^2 + 2y^2 + xy - 12y$ a partire da $x_0 = \begin{bmatrix} -1 \\ 2 \end{bmatrix}$ ed eseguire una iterazione.

### 1. Calcolo del Gradiente Generale
$$
\nabla f(x, y) = \begin{bmatrix}
\frac{\partial f}{\partial x} \\
\frac{\partial f}{\partial y}
\end{bmatrix} = \begin{bmatrix}
2x + y \\
x + 4y - 12
\end{bmatrix}
$$

### 2. Iterazione 0 ($k=0$)
1. **Valutazione del Gradiente in $x_0 = [-1, 2]^T$**:
   $$\nabla f(-1, 2) = \begin{bmatrix} 2(-1) + 2 \\ -1 + 4(2) - 12 \end{bmatrix} = \begin{bmatrix} 0 \\ -5 \end{bmatrix}$$
2. **Norma del gradiente**:
   $$\|\nabla f(x_0)\| = \sqrt{0^2 + (-5)^2} = 5 \neq 0$$
3. **Direzione**:
   $$d_0 = -\nabla f(x_0) = \begin{bmatrix} 0 \\ 5 \end{bmatrix}$$
4. **Line Search Esatta**:
   Esprimiamo il nuovo punto in funzione di $\alpha$:
   $$x_0 + \alpha d_0 = \begin{bmatrix} -1 \\ 2 \end{bmatrix} + \alpha \begin{bmatrix} 0 \\ 5 \end{bmatrix} = \begin{bmatrix} -1 \\ 2 + 5\alpha \end{bmatrix}$$
   Sostituiamo le coordinate $x(\alpha) = -1$ e $y(\alpha) = 2 + 5\alpha$ nella funzione obiettivo:
   $$\phi(\alpha) = f(-1, 2 + 5\alpha) = (-1)^2 + 2(2 + 5\alpha)^2 + (-1)(2 + 5\alpha) - 12(2 + 5\alpha)$$
   $$\phi(\alpha) = 1 + 2(4 + 20\alpha + 25\alpha^2) - 2 - 5\alpha - 24 - 60\alpha$$
   $$\phi(\alpha) = 1 + 8 + 40\alpha + 50\alpha^2 - 26 - 65\alpha$$
   $$\phi(\alpha) = 50\alpha^2 - 25\alpha - 17$$
   Deriviamo rispetto ad $\alpha$ e poniamo a zero:
   $$\frac{d\phi(\alpha)}{d\alpha} = 100\alpha - 25 = 0 \implies \alpha_0 = \frac{25}{100} = \frac{1}{4} = 0.25$$
5. **Aggiornamento del Punto**:
   $$x_1 = x_0 + \alpha_0 d_0 = \begin{bmatrix} -1 \\ 2 \end{bmatrix} + \frac{1}{4} \begin{bmatrix} 0 \\ 5 \end{bmatrix} = \begin{bmatrix} -1 \\ 2 + 1.25 \end{bmatrix} = \begin{bmatrix} -1 \\ 3.25 \end{bmatrix} = \begin{bmatrix} -1 \\ \frac{13}{4} \end{bmatrix}$$

L'iterazione 1 termina con il punto $x_1 = \begin{bmatrix} -1 \\ 3.25 \end{bmatrix}$.

---

## Proprietà Fondamentale d'Esame: Ortogonalità consecutiva

In un metodo del gradiente con line search esatta, la direzione di ricerca $d_{k+1}$ a un passo successivo è sempre **ortogonale** alla direzione di ricerca corrente $d_k$:
$$d_{k+1}^T d_k = 0$$
Questo fatto deriva da:
$$\frac{d\phi(\alpha_k)}{d\alpha} = \nabla f(x_k + \alpha_k d_k)^T d_k = -\nabla f(x_{k+1})^T \nabla f(x_k) = 0$$
Questo comportamento a "zig-zag" rende il metodo lento quando le curve di livello sono molto ellittiche (Hessiano mal condizionato).
