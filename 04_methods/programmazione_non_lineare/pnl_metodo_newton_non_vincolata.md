---
type: method
topic: programmazione_non_lineare
status: active
reliability: official
---

# Metodo di Newton per PNL Non Vincolata

Il metodo di Newton è un algoritmo di ottimizzazione che sfrutta le derivate seconde (matrice Hessiana) per approssimare localmente la funzione obiettivo tramite un modello quadratico e raggiungere rapidamente un punto stazionario.

---

## Procedura Operativa Passo-Passo

### 1. Calcolo del Gradiente e dell'Hessiana
Dato il punto iniziale $x_k$:
- Calcolare il vettore gradiente $\nabla f(x_k)$.
- Calcolare la matrice Hessiana $H_f(x_k)$.

### 2. Impostazione del Sistema di Newton
Invece di calcolare l'inversa della matrice Hessiana $H_f(x_k)^{-1}$ (operazione computazionalmente onerosa ed incline ad errori di arrotondamento all'esame), impostare e risolvere il sistema lineare per la direzione di Newton $d_k$:
$$H_f(x_k) d_k = -\nabla f(x_k)$$
Per una funzione di due variabili, questo equivale a risolvere il sistema $2 \times 2$:
$$\begin{bmatrix} \frac{\partial^2 f}{\partial x^2} & \frac{\partial^2 f}{\partial x \partial y} \\ \frac{\partial^2 f}{\partial y \partial x} & \frac{\partial^2 f}{\partial y^2} \end{bmatrix} \begin{bmatrix} d_x \\ d_y \end{bmatrix} = -\begin{bmatrix} \frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \end{bmatrix}$$

### 3. Aggiornamento del Punto
Aggiornare il punto con passo standard $\alpha = 1$:
$$x_{k+1} = x_k + d_k$$

### 4. Verifica di Arresto
Valutare il gradiente nel nuovo punto $\nabla f(x_{k+1})$. Se $\|\nabla f(x_{k+1})\| < \epsilon$, arrestare l'algoritmo. Altrimenti, porre $k = k+1$ e ripetere dal passo 1.

---

## Proprietà Fondamentale d'Esame: Funzioni Quadratiche
Se la funzione obiettivo $f(x)$ è una **forma quadratica** (ovvero la matrice Hessiana $H_f$ è costante in tutto lo spazio $\mathbb{R}^n$) e la matrice Hessiana è non singolare, il metodo di Newton **converge al punto stazionario esatto in una sola iterazione** a partire da *qualunque* punto iniziale $x_0$.

---

## Esempio Numerico Svolto (dall'Esercizio 7)

Minimizzare $f(x, y) = x^2 + 2y^2 + xy - 12y$ a partire da $x_0 = (-1, 2)$.

1. **Gradiente generale**:
   $$\nabla f(x, y) = \begin{bmatrix} 2x + y \\ x + 4y - 12 \end{bmatrix}$$
2. **Matrice Hessiana**:
   $$H_f(x, y) = \begin{bmatrix} 2 & 1 \\ 1 & 4 \end{bmatrix} \quad \text{(costante)}$$
3. **Iterazione 0**:
   - Valutiamo il gradiente in $x_0 = (-1, 2)$:
     $$\nabla f(-1, 2) = \begin{bmatrix} 2(-1) + 2 \\ -1 + 4(2) - 12 \end{bmatrix} = \begin{bmatrix} 0 \\ -5 \end{bmatrix}$$
   - Impostiamo il sistema lineare $H_f(x_0) d_0 = -\nabla f(x_0)$:
     $$\begin{bmatrix} 2 & 1 \\ 1 & 4 \end{bmatrix} \begin{bmatrix} d_x \\ d_y \end{bmatrix} = \begin{bmatrix} 0 \\ 5 \end{bmatrix}$$
   - Risolviamo il sistema:
     $$
     \begin{cases}
     2d_x + d_y = 0 \implies d_y = -2d_x \\
     d_x + 4d_y = 5
     \end{cases}
     $$
     Sostituendo $d_y = -2d_x$ nella seconda equazione:
     $$d_x + 4(-2d_x) = 5 \implies -7d_x = 5 \implies d_x = -\frac{5}{7}$$
     Ricaviamo $d_y$:
     $$d_y = -2\left(-\frac{5}{7}\right) = \frac{10}{7}$$
     La direzione di Newton è $d_0 = \begin{bmatrix} -5/7 \\ 10/7 \end{bmatrix}$.
   - Aggiorniamo il punto:
     $$x_1 = x_0 + d_0 = \begin{bmatrix} -1 \\ 2 \end{bmatrix} + \begin{bmatrix} -5/7 \\ 10/7 \end{bmatrix} = \begin{bmatrix} -12/7 \\ 24/7 \end{bmatrix}$$
4. **Verifica ottimalità**:
   Poiché la funzione $f(x, y)$ è quadratica e la sua Hessiana è costante e definita positiva ($\det(H_f) = 7 > 0$, $\text{tr}(H_f) = 6 > 0$), il punto $x_1 = (-12/7, 24/7)$ è il **minimo globale esatto** del problema, raggiunto in una sola iterazione. Infatti, valutando il gradiente in $x_1$:
   $$\nabla f\left(-\frac{12}{7}, \frac{24}{7}\right) = \begin{bmatrix} 2(-12/7) + 24/7 \\ -12/7 + 4(24/7) - 12 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

---

## Collegamenti Obsidian
- Classificazione Hessiana: [[pnl_non_vincolata_punti_stazionari_hessiana]]
- Metodo del Gradiente: [[pnl_metodo_gradiente_line_search_esatta]]
- Esempi non vincolati svolti: [[pnl_non_vincolata_esercizi_base]]
