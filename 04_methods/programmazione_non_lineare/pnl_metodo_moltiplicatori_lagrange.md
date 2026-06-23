---
type: method
topic: programmazione_non_lineare
status: active
reliability: official
---

# Metodo dei Moltiplicatori di Lagrange (Vincoli di Uguaglianza)

Il metodo dei moltiplicatori di Lagrange consente di trovare i punti di minimo e massimo locale di una funzione obiettivo $f(x)$ soggetta esclusivamente a vincoli di uguaglianza $g_i(x) = 0$.

---

## Formulazione Matematica

Sia il problema:

$$
\begin{aligned}
\min/\max \quad & f(x) \\
\text{s.t. } & g_i(x) = 0 \quad i = 1, \dots, m
\end{aligned}
$$

Definiamo la **funzione Lagrangiana**:

$$L(x, \lambda) = f(x) + \sum_{i=1}^m \lambda_i g_i(x)$$

dove $\lambda_1, \dots, \lambda_m$ sono i moltiplicatori di Lagrange.

---

## Procedura Operativa Passo-Passo

### 1. Costruzione della Lagrangiana
Scrivere esplicitamente la funzione $L(x, \lambda)$ sommando alla funzione obiettivo i vincoli di uguaglianza opportunamente moltiplicati per i rispettivi coefficienti $\lambda_i$.

### 2. Calcolo dei Gradienti parziali
Calcolare le derivate parziali di $L$ rispetto a ciascuna variabile decisionale $x_j$ (con $j=1, \dots, n$) e rispetto a ciascun moltiplicatore $\lambda_i$ (con $i=1, \dots, m$).

### 3. Risoluzione del Sistema Lagrangiano
Impostare e risolvere il sistema di $n + m$ equazioni:

$$
\begin{cases}
\frac{\partial L}{\partial x_j} = 0 \quad j = 1, \dots, n \\
\frac{\partial L}{\partial \lambda_i} = 0 \quad i = 1, \dots, m
\end{cases}
$$

Le soluzioni $(x^*, \lambda^*)$ di questo sistema individuano i punti stazionari vincolati.

### 4. Classificazione dei Punti
Per verificare se i punti trovati sono di massimo o minimo locale, si può ricorrere alla matrice **Hessiana Orlata** (Bordered Hessian) valutata nei punti stazionari o a valutazioni geometriche/regione compatta (teorema di Weierstrass).

---

## Esempio Numerico Svolto

Trovare i punti di ottimo della funzione $f(x, y) = x^2 + y^2$ soggetti al vincolo $(x-1)^2 + (y-2)^2 = 20$.

### 1. Costruzione della Lagrangiana
$$L(x, y, \lambda) = x^2 + y^2 + \lambda \left( (x-1)^2 + (y-2)^2 - 20 \right)$$

### 2. Sistema delle Derivate Parziali
$$
\begin{cases}
\frac{\partial L}{\partial x} = 2x + 2\lambda(x-1) = 0 \implies 2x(1+\lambda) = 2\lambda \implies x = \frac{\lambda}{1+\lambda} \\
\frac{\partial L}{\partial y} = 2y + 2\lambda(y-2) = 0 \implies 2y(1+\lambda) = 4\lambda \implies y = \frac{2\lambda}{1+\lambda} \\
\frac{\partial L}{\partial \lambda} = (x-1)^2 + (y-2)^2 - 20 = 0
\end{cases}
$$

### 3. Risoluzione
Notiamo dalla prima e seconda equazione che:
$$y = 2x$$
Sostituiamo $y = 2x$ nel vincolo:
$$(x-1)^2 + (2x-2)^2 = 20$$
$$(x-1)^2 + 4(x-1)^2 = 20 \implies 5(x-1)^2 = 20 \implies (x-1)^2 = 4$$
Questo fornisce due soluzioni per $x$:
1. $x - 1 = 2 \implies x = 3 \implies y = 6$.
2. $x - 1 = -2 \implies x = -1 \implies y = -2$.

Calcoliamo i moltiplicatori corrispondenti da $2x + 2\lambda(x-1) = 0$:
- Per $(3, 6)$: $2(3) + 2\lambda(2) = 0 \implies 6 + 4\lambda = 0 \implies \lambda = -\frac{3}{2}$.
- Per $(-1, -2)$: $2(-1) + 2\lambda(-2) = 0 \implies -2 - 4\lambda = 0 \implies \lambda = -\frac{1}{2}$.

### 4. Valutazione e Ottimo Globale
La regione $\Omega$ è una circonferenza (insieme chiuso e limitato, ovvero compatto). Per il Teorema di Weierstrass, la funzione continua $f(x, y)$ deve ammettere massimo e minimo globale su di essa:
- Valutazione in $P_1 = (3, 6)$:
  $$f(3, 6) = 3^2 + 6^2 = 9 + 36 = 45$$
- Valutazione in $P_2 = (-1, -2)$:
  $$f(-1, -2) = (-1)^2 + (-2)^2 = 1 + 4 = 5$$

Conclusione:
- Il punto $P_1 = (3, 6)$ è il **massimo globale** vincolato su $\Omega$.
- Il punto $P_2 = (-1, -2)$ è il **minimo globale** vincolato su $\Omega$.
