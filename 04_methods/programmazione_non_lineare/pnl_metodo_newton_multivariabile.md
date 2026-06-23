---
type: method
topic: programmazione_non_lineare
status: active
reliability: official
---

# Metodo di Newton Multivariabile

Il metodo di Newton multivariabile è un algoritmo iterativo per la minimizzazione di una funzione non vincolata $f: \mathbb{R}^n \to \mathbb{R}$. Sfrutta l'approssimazione quadratica locale (sviluppo di Taylor) per individuare rapidamente la direzione verso il punto stazionario.

---

## Formula di Aggiornamento

$$x_{k+1} = x_k + d_k$$

dove la direzione di Newton $d_k$ è la soluzione del sistema lineare:

$$H_f(x_k) d_k = -\nabla f(x_k)$$

---

## Procedura Operativa Passo-Passo

### 1. Inizializzazione
- Definire il punto di partenza $x_0 \in \mathbb{R}^n$.
- Impostare la tolleranza $\epsilon > 0$ ed il numero massimo di iterazioni $N_{\text{max}}$.
- Impostare $k = 0$.

### 2. Passo Iterativo (Iterazione $k$)
1. **Calcolo delle Derivate nel punto corrente $x_k$**:
   - Calcolare il vettore gradiente: $\nabla f(x_k)$.
   - Calcolare la matrice Hessiana: $H_f(x_k)$.
2. **Verifica dei Criteri di Arresto**:
   - Se $\|\nabla f(x_k)\| < \epsilon$, fermarsi: $x_k$ è un punto stazionario ottimo.
3. **Calcolo della Direzione di Spostamento**:
   Invece di calcolare la matrice inversa $[H_f(x_k)]^{-1}$, impostare e risolvere il sistema lineare:
   $$H_f(x_k) d_k = -\nabla f(x_k)$$
   in cui le incognite sono i componenti del vettore direzione $d_k = [d_{k,1}, d_{k,2}, \dots, d_{k,n}]^T$.
4. **Aggiornamento del Punto**:
   $$x_{k+1} = x_k + d_k$$
5. Incrementare $k = k + 1$ e tornare al punto 1.

---

## Esempio Numerico Svolto

Risolvere il problema $\min f(x, y) = x^2 + 2y^2 + xy - 12y$ a partire da $x_0 = \begin{bmatrix} -1 \\ 2 \end{bmatrix}$ ed eseguire una iterazione del metodo di Newton.

### 1. Gradiente e Matrice Hessiana Generali
$$
\nabla f(x, y) = \begin{bmatrix}
2x + y \\
x + 4y - 12
\end{bmatrix}
$$

$$
H_f(x, y) = \begin{bmatrix}
\frac{\partial^2 f}{\partial x^2} & \frac{\partial^2 f}{\partial x \partial y} \\
\frac{\partial^2 f}{\partial y \partial x} & \frac{\partial^2 f}{\partial y^2}
\end{bmatrix} = \begin{bmatrix}
2 & 1 \\
1 & 4
\end{bmatrix}
$$

### 2. Iterazione 0 ($k=0$)
1. **Valutazione nel punto $x_0 = [-1, 2]^T$**:
   $$\nabla f(-1, 2) = \begin{bmatrix} 2(-1) + 2 \\ -1 + 4(2) - 12 \end{bmatrix} = \begin{bmatrix} 0 \\ -5 \end{bmatrix}$$
   $$H_f(-1, 2) = \begin{bmatrix} 2 & 1 \\ 1 & 4 \end{bmatrix} \quad \text{(costante)}$$
2. **Risoluzione del Sistema Lineare $H_f(x_0) d_0 = -\nabla f(x_0)$**:
   $$\begin{bmatrix} 2 & 1 \\ 1 & 4 \end{bmatrix} \begin{bmatrix} d_x \\ d_y \end{bmatrix} = -\begin{bmatrix} 0 \\ -5 \end{bmatrix} = \begin{bmatrix} 0 \\ 5 \end{bmatrix}$$
   Questo corrisponde al sistema lineare:
   $$\begin{cases}
   2 d_x + d_y = 0 \implies d_y = -2d_x \\
   d_x + 4 d_y = 5
   \end{cases}$$
   Sostituendo la prima nella seconda:
   $$d_x + 4(-2d_x) = 5 \implies d_x - 8d_x = 5 \implies -7d_x = 5 \implies d_x = -\frac{5}{7}$$
   $$d_y = -2\left(-\frac{5}{7}\right) = \frac{10}{7}$$
   Il vettore direzione è:
   $$d_0 = \begin{bmatrix} -5/7 \\ 10/7 \end{bmatrix}$$
3. **Aggiornamento del Punto**:
   $$x_1 = x_0 + d_0 = \begin{bmatrix} -1 \\ 2 \end{bmatrix} + \begin{bmatrix} -5/7 \\ 10/7 \end{bmatrix} = \begin{bmatrix} -1 - 5/7 \\ 2 + 10/7 \end{bmatrix} = \begin{bmatrix} -12/7 \\ 24/7 \end{bmatrix} \approx \begin{bmatrix} -1.7143 \\ 3.4286 \end{bmatrix}$$

---

## Nota d'Esame: Funzioni Quadratiche

Se la funzione obiettivo $f(x)$ è una funzione quadratica (come nell'esempio sopra) e la matrice Hessiana è definita positiva su tutto lo spazio, il metodo di Newton **converge alla soluzione ottima globale in una singola iterazione** a partire da qualsiasi punto iniziale $x_0$.
Infatti:
$$x^* = \begin{bmatrix} -12/7 \\ 24/7 \end{bmatrix}$$
è il punto stazionario esatto di $f(x, y)$, che è stato individuato al passo $x_1$ in una sola iterazione.
