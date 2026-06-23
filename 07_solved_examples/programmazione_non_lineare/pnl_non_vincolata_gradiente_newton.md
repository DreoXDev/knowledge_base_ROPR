---
type: solved_example
topic: programmazione_non_lineare
status: active
reliability: official
---

# Esercizi Svolti PNL Non Vincolata: Gradiente e Newton (Esercizi 6-9)

Questo file raccoglie le soluzioni complete e strutturate degli Esercizi 6-9 estratti da `PNL_non_vincolata.pdf`. Gli esercizi mettono a confronto l'applicazione pratica del metodo del gradiente con line search esatta e il metodo di Newton multivariabile.

---

## Esercizio 6

### Testo
Si consideri il seguente problema di ottimizzazione non vincolata:
$$\max_{(x, y) \in \mathbb{R}^2} \quad f(x, y) = -x^2 - 2y^2 + 2xy + 2y$$
1. Effettuare due iterazioni del metodo del gradiente con line search esatta a partire da $x_0 = (0, 0)$.
2. Effettuare una iterazione del metodo di Newton a partire da $x_0 = (0, 0)$.
3. Verificare se i punti trovati sono ottimi locali o globali.

### Soluzione
Gradiente generale:
$$\nabla f(x, y) = \begin{bmatrix} -2x + 2y \\ 2x - 4y + 2 \end{bmatrix}$$
Hessiana generale (costante):
$$H_f(x, y) = \begin{bmatrix} -2 & 2 \\ 2 & -4 \end{bmatrix}$$

1. **Metodo del Gradiente (2 iterazioni)**:
   - **Iterazione 0**:
     - Gradiente in $x_0 = (0, 0)^T$: $\nabla f(0, 0) = \begin{bmatrix} 0 \\ 2 \end{bmatrix}$.
     - Direzione di salita (massimizzazione): $d_0 = \nabla f(0, 0) = \begin{bmatrix} 0 \\ 2 \end{bmatrix}$.
     - Punto mobile: $x_0 + \alpha d_0 = \begin{bmatrix} 0 \\ 2\alpha \end{bmatrix}$.
     - Funzione del passo: $\phi(\alpha) = f(0, 2\alpha) = -2(2\alpha)^2 + 2(2\alpha) = -8\alpha^2 + 4\alpha$.
     - Ottimizzazione: $\phi'(\alpha) = -16\alpha + 4 = 0 \implies \alpha_0 = \frac{1}{4} = 0.25$.
     - Aggiornamento: $x_1 = \begin{bmatrix} 0 \\ 0.5 \end{bmatrix}$.
   - **Iterazione 1**:
     - Gradiente in $x_1 = (0, 0.5)^T$: $\nabla f(0, 0.5) = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$.
     - Verifica ortogonalità: $d_1^T d_0 = \begin{bmatrix} 1 \\ 0 \end{bmatrix} \cdot \begin{bmatrix} 0 \\ 2 \end{bmatrix} = 0$ (OK).
     - Direzione: $d_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$.
     - Punto mobile: $x_1 + \alpha d_1 = \begin{bmatrix} \alpha \\ 0.5 \end{bmatrix}$.
     - Funzione del passo: $\phi(\alpha) = f(\alpha, 0.5) = -\alpha^2 - 2(0.5)^2 + 2\alpha(0.5) + 2(0.5) = -\alpha^2 + \alpha + 0.5$.
     - Ottimizzazione: $\phi'(\alpha) = -2\alpha + 1 = 0 \implies \alpha_1 = \frac{1}{2} = 0.5$.
     - Aggiornamento: $x_2 = \begin{bmatrix} 0.5 \\ 0.5 \end{bmatrix}$.

2. **Metodo di Newton (1 iterazione)**:
   - Risolviamo il sistema $H_f(x_0) d_0 = -\nabla f(x_0)$:
     $$\begin{bmatrix} -2 & 2 \\ 2 & -4 \end{bmatrix} \begin{bmatrix} d_x \\ d_y \end{bmatrix} = -\begin{bmatrix} 0 \\ 2 \end{bmatrix}$$
     $$\begin{cases} -2d_x + 2d_y = 0 \implies d_x = d_y \\ 2d_x - 4d_y = -2 \implies 2d_y - 4d_y = -2 \implies d_y = 1 \implies d_x = 1 \end{cases}$$
     Direzione di Newton: $d_0 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$.
   - Aggiornamento: $x_1 = x_0 + d_0 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$.

3. **Verifica della natura dei punti**:
   - Il punto del gradiente $x_2 = (0.5, 0.5)$ ha gradiente $\nabla f(0.5, 0.5) = \begin{bmatrix} 0 \\ 1 \end{bmatrix} \neq \begin{bmatrix} 0 \\ 0 \end{bmatrix}$. Non essendo stazionario, **non è un punto di ottimo**.
   - Il punto di Newton $x_1 = (1, 1)$ ha gradiente $\nabla f(1, 1) = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$. È stazionario. L'Hessiana è definita negativa in tutto $\mathbb{R}^2$ ($\det(H_f) = 4 > 0, \text{tr}(H_f) = -6 < 0$). La funzione è concava su tutto lo spazio, per cui $x_1 = (1, 1)$ è il **massimo globale** del problema.

---

## Esercizio 7

### Testo
Si consideri il seguente problema di ottimizzazione non vincolata:
$$\min_{(x, y) \in \mathbb{R}^2} \quad f(x, y) = x^2 + 2y^2 + xy - 12y$$
1. Effettuare una iterazione del metodo del gradiente con line search esatta a partire da $x_0 = (-1, 2)$.
2. Effettuare una iterazione del metodo di Newton a partire da $x_0 = (-1, 2)$.
3. Verificare se i punti trovati sono ottimi locali o globali.

### Soluzione
Gradiente generale:
$$\nabla f(x, y) = \begin{bmatrix} 2x + y \\ x + 4y - 12 \end{bmatrix}$$
Hessiana generale (costante):
$$H_f(x, y) = \begin{bmatrix} 2 & 1 \\ 1 & 4 \end{bmatrix}$$

1. **Metodo del Gradiente (1 iterazione)**:
   - Gradiente in $x_0 = (-1, 2)^T$: $\nabla f(-1, 2) = \begin{bmatrix} 0 \\ -5 \end{bmatrix}$.
   - Direzione di discesa: $d_0 = -\nabla f(x_0) = \begin{bmatrix} 0 \\ 5 \end{bmatrix}$.
   - Punto mobile: $x_0 + \alpha d_0 = \begin{bmatrix} -1 \\ 2 + 5\alpha \end{bmatrix}$.
   - Funzione del passo:
     $$\phi(\alpha) = f(-1, 2 + 5\alpha) = (-1)^2 + 2(2 + 5\alpha)^2 + (-1)(2 + 5\alpha) - 12(2 + 5\alpha) = 50\alpha^2 - 25\alpha - 17$$
   - Ottimizzazione: $\phi'(\alpha) = 100\alpha - 25 = 0 \implies \alpha_0 = \frac{25}{100} = 0.25$.
   - Aggiornamento: $x_1 = \begin{bmatrix} -1 \\ 3.25 \end{bmatrix}$.

2. **Metodo di Newton (1 iterazione)**:
   - Risolviamo il sistema $H_f(x_0) d_0 = -\nabla f(x_0)$:
     $$\begin{bmatrix} 2 & 1 \\ 1 & 4 \end{bmatrix} \begin{bmatrix} d_x \\ d_y \end{bmatrix} = \begin{bmatrix} 0 \\ 5 \end{bmatrix} \implies \begin{cases} d_y = -2d_x \\ d_x + 4(-2d_x) = 5 \implies d_x = -5/7, \quad d_y = 10/7 \end{cases}$$
     Direzione di Newton: $d_0 = \begin{bmatrix} -5/7 \\ 10/7 \end{bmatrix}$.
   - Aggiornamento: $x_1 = x_0 + d_0 = \begin{bmatrix} -12/7 \\ 24/7 \end{bmatrix} \approx \begin{bmatrix} -1.7143 \\ 3.4286 \end{bmatrix}$.

3. **Verifica della natura dei punti**:
   - Il punto del gradiente $x_1 = (-1, 3.25)$ ha gradiente $\nabla f(-1, 3.25) = \begin{bmatrix} 1.25 \\ 0 \end{bmatrix} \neq 0$, quindi **non è un punto di ottimo**.
   - Il punto di Newton $x_1 = (-12/7, 24/7)$ ha gradiente nullo ed essendo la funzione convessa su tutto lo spazio ($\det(H_f) = 7 > 0, \text{tr}(H_f) = 6 > 0$), esso rappresenta il **minimo globale** del problema.

---

## Esercizio 8

### Testo
Si consideri il seguente problema di ottimizzazione non vincolata:
$$\min_{(x, y) \in \mathbb{R}^2} \quad f(x, y) = x^2 + \frac{y^2}{10000}$$
1. Effettuare due iterazioni del metodo del gradiente con line search esatta a partire da $x_0 = (1, 1)$.
2. Effettuare una iterazione del metodo di Newton a partire da $x_0 = (1, 1)$.
3. Verificare se i punti trovati sono ottimi locali o globali.

### Soluzione
Gradiente generale:
$$\nabla f(x, y) = \begin{bmatrix} 2x \\ \frac{y}{5000} \end{bmatrix}$$
Hessiana generale (costante):
$$H_f(x, y) = \begin{bmatrix} 2 & 0 \\ 0 & \frac{1}{5000} \end{bmatrix}$$

1. **Metodo del Gradiente (2 iterazioni)**:
   - **Iterazione 0**:
     - Gradiente in $x_0 = (1, 1)^T$: $\nabla f(1, 1) = \begin{bmatrix} 2 \\ 1/5000 \end{bmatrix} = \begin{bmatrix} 2 \\ 0.0002 \end{bmatrix}$.
     - Direzione de discesa: $d_0 = \begin{bmatrix} -2 \\ -1/5000 \end{bmatrix}$.
     - Punto mobile: $x_0 + \alpha d_0 = \begin{bmatrix} 1 - 2\alpha \\ 1 - \frac{\alpha}{5000} \end{bmatrix}$.
     - Funzione del passo:
       $$\phi(\alpha) = (1 - 2\alpha)^2 + \frac{(1 - \frac{\alpha}{5000})^2}{10000} = \left(4 + \frac{1}{2.5 \times 10^{11}}\right)\alpha^2 - \left(4 + \frac{2}{5 \times 10^7}\right)\alpha + \left(1 + \frac{1}{10000}\right)$$
       Risolvendo analiticamente $\phi'(\alpha) = 0$, si ricava il passo esatto:
       $$\alpha_0 = \frac{500000005000}{1000000000001} \approx 0.5$$
     - Aggiornamento:
       $$x_1 = \begin{bmatrix} -\frac{9999}{1000000000001} \\ \frac{999900000000}{1000000000001} \end{bmatrix} \approx \begin{bmatrix} -0.000000009999 \\ 0.9999 \end{bmatrix}$$
   - **Iterazione 1**:
     - Eseguendo l'ottimizzazione analitica del passo $\alpha_1$, si trova il secondo punto:
       $$x_2 \approx \begin{bmatrix} 0.9997 \\ 0.9997 \end{bmatrix} \times 10^{-8}$$
       *(Nota: Il condizionamento della funzione è estremo, per cui il gradiente oscilla ed avanza con passi microscopici, subendo fortemente l'effetto zig-zag).*

2. **Metodo di Newton (1 iterazione)**:
   - Risolviamo il sistema $H_f(x_0) d_0 = -\nabla f(x_0)$:
     $$\begin{bmatrix} 2 & 0 \\ 0 & 1/5000 \end{bmatrix} \begin{bmatrix} d_x \\ d_y \end{bmatrix} = \begin{bmatrix} -2 \\ -1/5000 \end{bmatrix} \implies d_x = -1, \quad d_y = -1$$
     La direzione di Newton è $d_0 = \begin{bmatrix} -1 \\ -1 \end{bmatrix}$.
   - Aggiornamento: $x_1 = x_0 + d_0 = \begin{bmatrix} 1-1 \\ 1-1 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$.

3. **Verifica della natura dei punti**:
   - Il punto del gradiente $x_2$ non ha gradiente nullo, per cui **non è ottimo**.
   - Il punto di Newton $x_1 = (0, 0)$ ha gradiente nullo. L'Hessiana è definita positiva ovunque, per cui $(0, 0)$ è il **minimo globale** della funzione. Newton converge in una sola iterazione perché la funzione è quadratica.

---

## Esercizio 9

### Testo
Si consideri il seguente problema di ottimizzazione non vincolata:
$$\min_{(x, y) \in \mathbb{R}^2} \quad f(x, y) = x^3 + y^3 - 3xy$$
1. Effettuare una iterazione del metodo del gradiente con line search esatta a partire da $x_0 = (1, 0)$.
2. Effettuare una iterazione del metodo di Newton a partire da $x_0 = (1, 0)$.
3. Verificare se i punti trovati sono ottimi locali o globali.

### Soluzione
Gradiente generale:
$$\nabla f(x, y) = \begin{bmatrix} 3x^2 - 3y \\ 3y^2 - 3x \end{bmatrix}$$
Hessiana generale:
$$H_f(x, y) = \begin{bmatrix} 6x & -3 \\ -3 & 6y \end{bmatrix}$$

1. **Metodo del Gradiente (1 iterazione)**:
   - Gradiente in $x_0 = (1, 0)^T$: $\nabla f(1, 0) = \begin{bmatrix} 3 \\ -3 \end{bmatrix}$.
   - Direzione di discesa: $d_0 = -\nabla f(1, 0) = \begin{bmatrix} -3 \\ 3 \end{bmatrix}$.
   - Punto mobile: $x_0 + \alpha d_0 = \begin{bmatrix} 1 - 3\alpha \\ 3\alpha \end{bmatrix}$.
   - Funzione del passo:
     $$\phi(\alpha) = (1 - 3\alpha)^3 + (3\alpha)^3 - 3(1-3\alpha)(3\alpha) = 1 - 9\alpha + 27\alpha^2 - 27\alpha^3 + 27\alpha^3 - 9\alpha + 27\alpha^2 = 54\alpha^2 - 18\alpha + 1$$
   - Ottimizzazione: $\phi'(\alpha) = 108\alpha - 18 = 0 \implies \alpha_0 = \frac{18}{108} = \frac{1}{6} \approx 0.1667$.
   - Aggiornamento:
     $$x_1 = \begin{bmatrix} 1 - 3(1/6) \\ 3(1/6) \end{bmatrix} = \begin{bmatrix} 0.5 \\ 0.5 \end{bmatrix}$$

2. **Metodo di Newton (1 iterazione)**:
   - Valutiamo l'Hessiana in $x_0 = (1, 0)$:
     $$H_f(1, 0) = \begin{bmatrix} 6 & -3 \\ -3 & 0 \end{bmatrix}$$
   - Risolviamo il sistema $H_f(x_0) d_0 = -\nabla f(x_0)$:
     $$\begin{bmatrix} 6 & -3 \\ -3 & 0 \end{bmatrix} \begin{bmatrix} d_x \\ d_y \end{bmatrix} = \begin{bmatrix} -3 \\ 3 \end{bmatrix} \implies \begin{cases} -3d_x = 3 \implies d_x = -1 \\ 6(-1) - 3d_y = -3 \implies -3d_y = 3 \implies d_y = -1 \end{cases}$$
     Direzione di Newton: $d_0 = \begin{bmatrix} -1 \\ -1 \end{bmatrix}$.
   - Aggiornamento: $x_1 = x_0 + d_0 = \begin{bmatrix} 1 - 1 \\ 0 - 1 \end{bmatrix} = \begin{bmatrix} 0 \\ -1 \end{bmatrix}$.

3. **Verifica della natura dei punti**:
   - Per il punto del gradiente $x_1 = (0.5, 0.5)$:
     $$\nabla f(0.5, 0.5) = \begin{bmatrix} 3(0.25) - 1.5 \\ 3(0.25) - 1.5 \end{bmatrix} = \begin{bmatrix} -0.75 \\ -0.75 \end{bmatrix} \neq \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$
     Non è stazionario, quindi **non è ottimo**.
   - Per il punto di Newton $x_1 = (0, -1)$:
     $$\nabla f(0, -1) = \begin{bmatrix} 3(0) - 3(-1) \\ 3(1) - 3(0) \end{bmatrix} = \begin{bmatrix} 3 \\ 3 \end{bmatrix} \neq \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$
     In questo caso, il punto ottenuto da Newton **non è stazionario**, per cui **non è un punto di ottimo**.
     *(Nota: Newton non ha raggiunto l'ottimo in un passo perché la funzione $f(x, y)$ non è quadratica).*

---

## Collegamenti Obsidian
- Metodo del Gradiente: [[pnl_metodo_gradiente_line_search_esatta]]
- Metodo di Newton: [[pnl_metodo_newton_non_vincolata]]
- Esercizi base studio di funzione: [[pnl_non_vincolata_esercizi_base]]
