---
type: solved_example
topic: programmazione_non_lineare
status: active
reliability: official
---

# Esercizi Svolti di Ottimizzazione Non Vincolata

In questa sezione vengono presentati due esercizi svolti dettagliati tratti dal materiale d'esame ufficiale.

---

## Esercizio 1: Analisi di Punti Stazionari e Convessità

### Testo
Si consideri la seguente funzione di due variabili reali:
$$f(x, y) = 2x^2 + y^2 - xy - 2x - 3y$$
a) Trovare tutti i punti stazionari di $f$.
b) Dire se la funzione $f$ è convessa o concava nello spazio $\mathbb{R}^2$.
c) Trovare tutti i punti di minimo locale e massimo locale di $f$.

---

### Soluzione Passo-Passo

#### a) Ricerca dei punti stazionari
I punti stazionari sono i punti in cui il gradiente della funzione si annulla: $\nabla f(x, y) = 0$.
Calcoliamo le derivate parziali del primo ordine:
$$\frac{\partial f}{\partial x} = 4x - y - 2$$
$$\frac{\partial f}{\partial y} = 2y - x - 3$$
Impostiamo il sistema lineare ponendo le derivate parziali a zero:
$$
\begin{cases}
4x - y = 2 \implies y = 4x - 2 \\
-x + 2y = 3
\end{cases}
$$
Sostituiamo $y = 4x - 2$ nella seconda equazione:
$$-x + 2(4x - 2) = 3 \implies -x + 8x - 4 = 3 \implies 7x = 7 \implies x = 1$$
Ricaviamo $y$:
$$y = 4(1) - 2 = 2$$
L'unico punto stazionario della funzione è il punto $P^* = (1, 2)$.

#### b) Studio di concavità/convessità
Calcoliamo le derivate parziali del secondo ordine per determinare la matrice Hessiana:
$$\frac{\partial^2 f}{\partial x^2} = 4, \quad \frac{\partial^2 f}{\partial y^2} = 2, \quad \frac{\partial^2 f}{\partial x \partial y} = -1$$
La matrice Hessiana $H_f(x, y)$ è costante per ogni $(x, y) \in \mathbb{R}^2$:
$$H_f(x, y) = \begin{bmatrix} 4 & -1 \\ -1 & 2 \end{bmatrix}$$
Per classificare la matrice Hessiana ne calcoliamo determinante e traccia:
- Determinate: $\det(H_f) = 4(2) - (-1)^2 = 8 - 1 = 7 > 0$.
- Traccia: $\text{tr}(H_f) = 4 + 2 = 6 > 0$.

Poiché il determinante è strettamente positivo e la traccia è strettamente positiva, entrambi gli autovalori sono positivi ($\lambda_1 > 0, \lambda_2 > 0$). La matrice Hessiana è **definita positiva** su tutto $\mathbb{R}^2$.
Di conseguenza, la funzione $f$ è **strettamente convessa** in tutto lo spazio $\mathbb{R}^2$.

#### c) Classificazione dei punti di minimo e massimo locale
Poiché la funzione $f$ è convessa su tutto lo spazio $\mathbb{R}^2$:
- Il punto stazionario $P^* = (1, 2)$ è un punto di **minimo locale** ed è anche un **minimo globale**.
- Non vi sono altri punti stazionari, quindi non esistono punti di massimo locale o globale.

---
---

## Esercizio 2: Metodo del Gradiente e Newton a confronto

### Testo
Si consideri il seguente problema di ottimizzazione non vincolata:
$$\max_{(x, y) \in \mathbb{R}^2} \quad -x^2 - 2y^2 + 2xy + 2y$$
a) Effettuare due iterazioni del metodo del gradiente con line search esatta a partire dal punto $x_0 = (0, 0)$.
b) Effettuare una iterazione del metodo di Newton a partire dallo stesso punto.
c) Verificare la natura dei punti trovati.

---

### Soluzione Passo-Passo

#### a) Metodo del Gradiente (2 iterazioni)
Sia $f(x, y) = -x^2 - 2y^2 + 2xy + 2y$.
Calcoliamo il gradiente generale:
$$\nabla f(x, y) = \begin{bmatrix} -2x + 2y \\ -4y + 2x + 2 \end{bmatrix}$$

##### Iterazione 0 ($k=0$):
1. Punto di partenza: $x_0 = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$.
2. Valutiamo il gradiente in $x_0$:
   $$\nabla f(0, 0) = \begin{bmatrix} 0 \\ 2 \end{bmatrix}$$
3. Direzione di spostamento (per massimizzazione ci spostiamo lungo il gradiente positivo):
   $$d_0 = \nabla f(0, 0) = \begin{bmatrix} 0 \\ 2 \end{bmatrix}$$
4. Line Search Esatta:
   $$x_0 + \alpha d_0 = \begin{bmatrix} 0 \\ 0 \end{bmatrix} + \alpha \begin{bmatrix} 0 \\ 2 \end{bmatrix} = \begin{bmatrix} 0 \\ 2\alpha \end{bmatrix}$$
   Sostituiamo $x(\alpha) = 0$ e $y(\alpha) = 2\alpha$ nella funzione obiettivo:
   $$\phi(\alpha) = f(0, 2\alpha) = -2(2\alpha)^2 + 2(2\alpha) = -8\alpha^2 + 4\alpha$$
   Deriviamo e poniamo a zero:
   $$\frac{d\phi}{d\alpha} = -16\alpha + 4 = 0 \implies \alpha_0 = \frac{4}{16} = \frac{1}{4} = 0.25$$
5. Nuovo punto:
   $$x_1 = x_0 + \alpha_0 d_0 = \begin{bmatrix} 0 \\ 0.5 \end{bmatrix}$$

##### Iterazione 1 ($k=1$):
1. Punto corrente: $x_1 = \begin{bmatrix} 0 \\ 0.5 \end{bmatrix}$.
2. Valutiamo il gradiente in $x_1$:
   $$\nabla f(0, 0.5) = \begin{bmatrix} -2(0) + 2(0.5) \\ -4(0.5) + 2(0) + 2 \end{bmatrix} = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$$
   *(Nota: $\nabla f(x_1)^T \nabla f(x_0) = \begin{bmatrix} 1 \\ 0 \end{bmatrix} \cdot \begin{bmatrix} 0 \\ 2 \end{bmatrix} = 0$, confermando l'ortogonalità consecutiva)*.
3. Direzione di spostamento:
   $$d_1 = \nabla f(0, 0.5) = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$$
4. Line Search Esatta:
   $$x_1 + \alpha d_1 = \begin{bmatrix} 0 \\ 0.5 \end{bmatrix} + \alpha \begin{bmatrix} 1 \\ 0 \end{bmatrix} = \begin{bmatrix} \alpha \\ 0.5 \end{bmatrix}$$
   Sostituiamo $x(\alpha) = \alpha$ e $y(\alpha) = 0.5$ nella funzione obiettivo:
   $$\phi(\alpha) = f(\alpha, 0.5) = -\alpha^2 - 2(0.5)^2 + 2\alpha(0.5) + 2(0.5) = -\alpha^2 - 0.5 + \alpha + 1 = -\alpha^2 + \alpha + 0.5$$
   Deriviamo e poniamo a zero:
   $$\frac{d\phi}{d\alpha} = -2\alpha + 1 = 0 \implies \alpha_1 = \frac{1}{2} = 0.5$$
5. Nuovo punto:
   $$x_2 = x_1 + \alpha_1 d_1 = \begin{bmatrix} 0.5 \\ 0.5 \end{bmatrix}$$

Il metodo del gradiente trova il punto $x_2 = (0.5, 0.5)$ in due iterazioni.

---

#### b) Metodo di Newton (1 iterazione)
Calcoliamo la matrice Hessiana:
$$H_f(x, y) = \begin{bmatrix} -2 & 2 \\ 2 & -4 \end{bmatrix} \quad \text{(costante)}$$
Il sistema di Newton $H_f(x_0) d_0 = -\nabla f(x_0)$ per la massimizzazione è:
$$\begin{bmatrix} -2 & 2 \\ 2 & -4 \end{bmatrix} \begin{bmatrix} d_x \\ d_y \end{bmatrix} = -\begin{bmatrix} 0 \\ 2 \end{bmatrix}$$
Risolviamo il sistema:
$$
\begin{cases}
-2d_x + 2d_y = 0 \implies d_x = d_y \\
2d_x - 4d_y = -2
\end{cases}
$$
Sostituendo la prima nella seconda:
$$2d_y - 4d_y = -2 \implies -2d_y = -2 \implies d_y = 1 \implies d_x = 1$$
Il vettore direzione è $d_0 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$.
Aggiorniamo il punto (con passo $\alpha = 1$):
$$x_1 = x_0 + d_0 = \begin{bmatrix} 0 \\ 0 \end{bmatrix} + \begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$$

Il metodo di Newton trova il punto $x_1 = (1, 1)$ in una sola iterazione.

---

#### c) Verifica dei punti trovati

1. **Analisi del punto $x_2 = (0.5, 0.5)$ (Gradiente)**:
   Valutiamo il gradiente in $(0.5, 0.5)$:
   $$\nabla f(0.5, 0.5) = \begin{bmatrix} -2(0.5) + 2(0.5) \\ -4(0.5) + 2(0.5) + 2 \end{bmatrix} = \begin{bmatrix} 0 \\ 1 \end{bmatrix} \ne \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$
   Poiché il gradiente non è nullo, il punto $(0.5, 0.5)$ non è stazionario. Quindi **non è un punto di ottimo**.
2. **Analisi del punto $x_1 = (1, 1)$ (Newton)**:
   Valutiamo il gradiente in $(1, 1)$:
   $$\nabla f(1, 1) = \begin{bmatrix} -2(1) + 2(1) \\ -4(1) + 2(1) + 2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$
   Il punto $(1, 1)$ è stazionario.
   Valutiamo l'Hessiana nel punto:
   $$H_f(1, 1) = \begin{bmatrix} -2 & 2 \\ 2 & -4 \end{bmatrix}$$
   Calcoliamo determinante e traccia:
   - $\det(H_f) = (-2)(-4) - 2^2 = 8 - 4 = 4 > 0$.
   - $\text{tr}(H_f) = -2 - 4 = -6 < 0$.
   Poiché $\det(H_f) > 0$ e $\text{tr}(H_f) < 0$, la matrice Hessiana è definita negativa ($H_f \prec 0$).
   Essendo l'Hessiana definita negativa su tutto $\mathbb{R}^2$, la funzione obiettivo è concava su tutto lo spazio e il punto stazionario $x_1 = (1, 1)$ è il **punto di massimo globale** del problema.
   *(Nota: Il metodo di Newton ha raggiunto l'ottimo globale esatto in una sola iterazione perché la funzione obiettivo è quadratica).*
