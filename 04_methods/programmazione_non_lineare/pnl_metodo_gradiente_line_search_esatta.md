---
type: method
topic: programmazione_non_lineare
status: active
reliability: official
---

# Metodo del Gradiente con Line Search Esatta

Questo metodo descrive l'applicazione del metodo del gradiente (discesa o salita rapida) con determinazione analitica del passo ottimo ad ogni iterazione per funzioni multivariabili.

---

## Procedura Operativa Passo-Passo

### 1. Scelta della Direzione
Ad ogni iterazione $k$, dato il punto corrente $x_k$:
- **Per problemi di MINIMIZZAZIONE (Discesa)**:
  $$d_k = -\nabla f(x_k)$$
- **Per problemi di MASSIMIZZAZIONE (Salita)**:
  $$d_k = \nabla f(x_k)$$

### 2. Impostazione della Funzione del Passo (Line Search Esatta)
Definire la funzione monodimensionale $\phi(\alpha)$ rispetto al parametro di passo $\alpha \ge 0$:
$$\phi(\alpha) = f(x_k + \alpha d_k)$$
Per fare ciò, si scrivono le coordinate del punto mobile $x_k + \alpha d_k$ in funzione di $\alpha$, e si sostituiscono all'interno dell'espressione analitica della funzione obiettivo $f(x, y)$.

### 3. Calcolo del Passo Ottimo $\alpha_k$
Trovare il valore $\alpha_k \ge 0$ che minimizza (o massimizza) $\phi(\alpha)$ risolvendo l'equazione di stazionarietà monodimensionale:
$$\frac{d\phi(\alpha)}{d\alpha} = 0 \implies \alpha_k$$
*(Nota: Per funzioni quadratiche, $\phi(\alpha)$ è un polinomio di secondo grado, la cui derivata prima rispetto ad $\alpha$ è lineare, rendendo immediata la ricerca dello zero).*

### 4. Aggiornamento del Punto
Aggiornare il punto per l'iterazione successiva:
$$x_{k+1} = x_k + \alpha_k d_k$$

### 5. Verifica dell'Arresto
Valutare il gradiente nel nuovo punto $\nabla f(x_{k+1})$. Se la sua norma $\|\nabla f(x_{k+1})\|$ è inferiore ad una tolleranza prefissata $\epsilon$, l'algoritmo si arresta. Altrimenti, porre $k = k+1$ e ripetere dal passo 1.

---

## Proprietà Chiave d'Esame: Ortogonalità Consecutiva
Nel metodo del gradiente con line search esatta, due direzioni di spostamento consecutive $d_k$ e $d_{k+1}$ sono sempre **ortogonali**:
$$d_{k+1}^T d_k = 0 \implies \nabla f(x_{k+1})^T \nabla f(x_k) = 0$$
All'esame, questa proprietà deve essere usata come verifica dei calcoli: se il prodotto scalare tra il gradiente al passo $k$ e quello al passo $k+1$ non è zero, c'è un errore nel calcolo del passo $\alpha_k$.

---

## Esempio Numerico Svolto (dall'Esercizio 6)

Massimizzare $f(x, y) = -x^2 - 2y^2 + 2xy + 2y$ a partire da $x_0 = (0, 0)$.

1. **Gradiente generale**:
   $$\nabla f(x, y) = \begin{bmatrix} -2x + 2y \\ 2x - 4y + 2 \end{bmatrix}$$
2. **Iterazione 0**:
   - Gradiente in $x_0 = (0, 0)$: $\nabla f(0, 0) = \begin{bmatrix} 0 \\ 2 \end{bmatrix}$.
   - Direzione (massimizzazione): $d_0 = \nabla f(0, 0) = \begin{bmatrix} 0 \\ 2 \end{bmatrix}$.
   - Punto in funzione di $\alpha$: $x_0 + \alpha d_0 = \begin{bmatrix} 0 \\ 2\alpha \end{bmatrix}$.
   - Funzione del passo:
     $$\phi(\alpha) = f(0, 2\alpha) = -2(2\alpha)^2 + 2(2\alpha) = -8\alpha^2 + 4\alpha$$
   - Derivata e azzeramento:
     $$\frac{d\phi}{d\alpha} = -16\alpha + 4 = 0 \implies \alpha_0 = \frac{1}{4} = 0.25$$
   - Nuovo punto:
     $$x_1 = x_0 + \alpha_0 d_0 = \begin{bmatrix} 0 \\ 0.5 \end{bmatrix}$$

3. **Iterazione 1**:
   - Gradiente in $x_1 = (0, 0.5)$: $\nabla f(0, 0.5) = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$.
   - Verifica di ortogonalità: $d_1^T d_0 = \begin{bmatrix} 1 \\ 0 \end{bmatrix} \cdot \begin{bmatrix} 0 \\ 2 \end{bmatrix} = 0$ (OK).
   - Direzione: $d_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$.
   - Punto in funzione di $\alpha$: $x_1 + \alpha d_1 = \begin{bmatrix} \alpha \\ 0.5 \end{bmatrix}$.
   - Funzione del passo:
     $$\phi(\alpha) = f(\alpha, 0.5) = -\alpha^2 - 2(0.5)^2 + 2\alpha(0.5) + 2(0.5) = -\alpha^2 + \alpha + 0.5$$
   - Derivata e azzeramento:
     $$\frac{d\phi}{d\alpha} = -2\alpha + 1 = 0 \implies \alpha_1 = \frac{1}{2} = 0.5$$
   - Nuovo punto:
     $$x_2 = x_1 + \alpha_1 d_1 = \begin{bmatrix} 0.5 \\ 0.5 \end{bmatrix}$$

---

## Collegamenti Obsidian
- Classificazione Hessiana: [[pnl_non_vincolata_punti_stazionari_hessiana]]
- Metodo di Newton: [[pnl_metodo_newton_non_vincolata]]
- Esempi non vincolati svolti: [[pnl_non_vincolata_esercizi_base]]
