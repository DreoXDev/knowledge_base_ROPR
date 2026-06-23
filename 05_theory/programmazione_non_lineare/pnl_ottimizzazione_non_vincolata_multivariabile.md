---
type: theory-note
topic: programmazione-non-lineare
status: consolidated
sources:
  - raw_assets/Programmazione Non Lineare/PNL 2D.pdf
  - raw_assets/Programmazione Non Lineare/PNL 2D 1.pdf
  - raw_assets/Programmazione Non Lineare/PNL_nonvincolata.pdf
reliability: official
---

# Ottimizzazione Non Vincolata Multivariabile

L'ottimizzazione multivariabile non vincolata si occupa di trovare i minimi o massimi di una funzione $f: \mathbb{R}^n \to \mathbb{R}$ definita su tutto lo spazio $\mathbb{R}^n$.

---

## Strumenti Matematici Fondamentali

Sia $f: \mathbb{R}^n \to \mathbb{R}$ differenziabile almeno due volte con continuità ($f \in C^2$).

### 1. Gradiente
Il gradiente di $f$ in $x \in \mathbb{R}^n$, denotato con $\nabla f(x)$, è il vettore delle derivate parziali del primo ordine:

$$
\nabla f(x) = \begin{bmatrix}
\frac{\partial f(x)}{\partial x_1} \\
\frac{\partial f(x)}{\partial x_2} \\
\vdots \\
\frac{\partial f(x)}{\partial x_n}
\end{bmatrix}
$$

- **Proprietà**: $\nabla f(x)$ indica la direzione di massima crescita locale della funzione. Il vettore $-\nabla f(x)$ indica invece la direzione di massima decrescita (direzione di discesa rapida).

### 2. Matrice Hessiana
La matrice Hessiana di $f$ in $x$, denotata con $H_f(x)$ o $\nabla^2 f(x)$, è la matrice quadrata delle derivate parziali seconde:

$$
H_f(x) = \begin{bmatrix}
\frac{\partial^2 f(x)}{\partial x_1^2} & \frac{\partial^2 f(x)}{\partial x_1 \partial x_2} & \dots & \frac{\partial^2 f(x)}{\partial x_1 \partial x_n} \\
\frac{\partial^2 f(x)}{\partial x_2 \partial x_1} & \frac{\partial^2 f(x)}{\partial x_2^2} & \dots & \frac{\partial^2 f(x)}{\partial x_2 \partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial^2 f(x)}{\partial x_n \partial x_1} & \frac{\partial^2 f(x)}{\partial x_n \partial x_2} & \dots & \frac{\partial^2 f(x)}{\partial x_n^2}
\end{bmatrix}
$$

- **Teorema di Schwarz**: Se le derivate seconde sono continue, allora $\frac{\partial^2 f}{\partial x_i \partial x_j} = \frac{\partial^2 f}{\partial x_j \partial x_i}$ e la matrice Hessiana è simmetrica ($H_f(x) = H_f(x)^T$).
- **Calcolo**: Per una funzione di $n$ variabili, si devono calcolare $n$ derivate parziali pure e $\frac{n(n-1)}{2}$ derivate parziali miste.

---

## Classificazione dei Punti Stazionari

I punti candidati ad essere ottimi locali (minimo o massimo) sono i **punti stazionari**, in cui il gradiente si annulla:
$$\nabla f(x^*) = 0$$

Per determinare la natura del punto stazionario si valuta la matrice Hessiana $H_f(x^*)$:

| Autovalori di $H_f(x^*)$ | Definizione della Matrice | Natura di $x^*$ |
|---|---|---|
| Tutti strettamente positivi ($\lambda_i > 0$) | Definita Positiva ($H_f \succ 0$) | **Minimo Locale Stretto** |
| Tutti strettamente negativi ($\lambda_i < 0$) | Definita Negativa ($H_f \prec 0$) | **Massimo Locale Stretto** |
| Almeno uno positivo e uno negativo | Indefinita | **Punto di Sella** |
| Non negativi, almeno uno nullo ($\lambda_i \ge 0$) | Semidefinita Positiva ($H_f \succeq 0$) | Minimo Locale o Punto di Sella (secondo ordine non sufficiente) |
| Non positivi, almeno uno nullo ($\lambda_i \le 0$) | Semidefinita Negativa ($H_f \preceq 0$) | Massimo Locale o Punto di Sella (secondo ordine non sufficiente) |

### Classificazione Veloce in 2D (Senza calcolo esplicito di autovalori)
Per $n = 2$, data $H_f(x^*) = \begin{bmatrix} A & B \\ B & C \end{bmatrix}$:
- Calcolare il determinante: $\det(H_f) = AC - B^2$.
- Calcolare la traccia: $\text{tr}(H_f) = A + C$.
  - Se $\det(H_f) > 0$ e $\text{tr}(H_f) > 0 \implies$ Definita positiva (Minimo locale).
  - Se $\det(H_f) > 0$ e $\text{tr}(H_f) < 0 \implies$ Definita negativa (Massimo locale).
  - Se $\det(H_f) < 0 \implies$ Indefinita (Punto di sella).
  - Se $\det(H_f) = 0 \implies$ Semidefinita (Caso degenere, richiede analisi di ordine superiore o globale).

---

## Studio di Convessità Globale

La convessità globale garantisce che le proprietà dei punti stazionari siano globali:
- Una funzione $f(x)$ è **convessa** su un insieme convesso se e solo se la sua matrice Hessiana $H_f(x)$ è **semidefinita positiva** ($\lambda_i \ge 0$) per ogni $x$ dell'insieme. In tal caso, ogni punto stazionario $x^*$ è un **minimo globale**.
- Una funzione $f(x)$ è **concava** su un insieme convesso se e solo se la sua matrice Hessiana $H_f(x)$ è **semidefinita negativa** ($\lambda_i \le 0$) per ogni $x$ dell'insieme. In tal caso, ogni punto stazionario $x^*$ è un **massimo globale**.

---

## Algoritmi Risolutivi Multivariabili

Dato un punto iniziale $x_0$, la successione di punti si aggiorna come:
$$x_{k+1} = x_k + \alpha_k d_k$$
dove $d_k$ è la direzione di spostamento e $\alpha_k > 0$ è la lunghezza del passo.

### 1. Metodo del Gradiente (Steepest Descent)
- **Direzione**: Discesa più ripida: $d_k = -\nabla f(x_k)$.
- **Passo (Line Search Esatta)**: Si trova risolvendo un problema unidimensionale di minimo globale in $\alpha$:
  $$\alpha_k = \arg\min_{\alpha \ge 0} \phi(\alpha) = \arg\min_{\alpha \ge 0} f(x_k - \alpha \nabla f(x_k))$$
  Si ricava ponendo $\frac{d\phi(\alpha)}{d\alpha} = 0$.
- **Proprietà**: Le direzioni di due iterazioni consecutive sono ortogonali ($d_k^T d_{k-1} = 0$), provocando un andamento a "zig-zag" se le curve di livello sono allungate.

### 2. Metodo di Newton Multivariabile
Utilizza l'approssimazione quadratica locale di $f(x)$ (sviluppo di Taylor):
$$f(x_k + d) \approx f(x_k) + \nabla f(x_k)^T d + \frac{1}{2} d^T H_f(x_k) d$$
- **Direzione (Direzione di Newton)**: Si ricava azzerando il gradiente dell'approssimazione quadratica rispetto a $d$:
  $$H_f(x_k) d_k = -\nabla f(x_k) \implies d_k = -[H_f(x_k)]^{-1} \nabla f(x_k)$$
- **Passo**: Standard $\alpha_k = 1$.
- **Proprietà**: Velocità di convergenza quadratica se inizializzato opportunamente. Se l'Hessiano non è definito positivo, la direzione potrebbe non essere di discesa (in tal caso l'algoritmo va corretto).
