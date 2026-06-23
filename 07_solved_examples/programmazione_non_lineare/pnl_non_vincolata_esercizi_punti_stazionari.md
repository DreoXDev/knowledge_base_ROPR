---
type: solved-example
topic: programmazione_non_lineare
status: consolidated
sources:
  - raw_assets/Programmazione Non Lineare/20_esercizi_pnl.pdf
reliability: official
---

# Esercizi Svolti: Ottimizzazione Non Vincolata (Punti Stazionari ed Hessiana)

Questa nota analizza nel dettaglio lo svolgimento degli esercizi 1-10 dell'asset `20_esercizi_pnl.pdf`, incentrati sull'ottimizzazione locale e globale libera (non vincolata).

---

## Procedura Risolutiva Generale

Dato un problema del tipo $\operatorname{opt}_{x, y} f(x, y)$, la procedura d'esame prevede quattro fasi fondamentali:

### 1. Ricerca dei Punti Stazionari
Si calcolano le derivate parziali del primo ordine rispetto a $x$ e $y$ e si pongono contemporaneamente pari a zero per trovare l'insieme dei punti stazionari:
$$\nabla f(x, y) = \begin{bmatrix} \frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

### 2. Calcolo dell'Hessiana
Si calcolano le derivate parziali di secondo ordine per costruire la matrice Hessiana generica:
$$H_f(x, y) = \begin{bmatrix} \frac{\partial^2 f}{\partial x^2} & \frac{\partial^2 f}{\partial x \partial y} \\ \frac{\partial^2 f}{\partial y \partial x} & \frac{\partial^2 f}{\partial y^2} \end{bmatrix} = \begin{bmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{bmatrix}$$

### 3. Valutazione e Classificazione Locale
Per ciascun punto stazionario $P^* = (x^*, y^*)$, si calcola $H_f(P^*)$ e si determina la sua segnatura tramite il determinante $\det(H_f) = f_{xx}f_{yy} - (f_{xy})^2$ e la traccia $\text{tr}(H_f) = f_{xx} + f_{yy}$:
-   **$\det(H_f) > 0$ e $\text{tr}(H_f) > 0$ (o $f_{xx} > 0$)**: La matrice è definita positiva ($H_f \succ 0$). Il punto $P^*$ è un **minimo locale stretto**.
-   **$\det(H_f) > 0$ e $\text{tr}(H_f) < 0$ (o $f_{xx} < 0$)**: La matrice è definita negativa ($H_f \prec 0$). Il punto $P^*$ è un **massimo locale stretto**.
-   **$\det(H_f) < 0$**: La matrice è indefinita. Il punto $P^*$ è un **punto di sella**.
-   **$\det(H_f) = 0$**: Il test del secondo ordine è inconclusivo (matrice semidefinita). È richiesta uno studio locale specifico.

---

## Analisi Dettagliata di Esercizi Scelti

### Esercizio 1
Trovare massimi e minimi locali di:
$$f(x, y) = 2x^3 - 2x^2y + 3x^2 - 2xy + 3y^2$$

#### 1. Sistema del Gradiente
$$
\begin{cases}
\frac{\partial f}{\partial x} = 6x^2 - 4xy + 6x - 2y = 0 \quad (1) \\
\frac{\partial f}{\partial y} = -2x^2 - 2x + 6y = 0 \implies 6y = 2x(x + 1) \implies y = \frac{x(x + 1)}{3} \quad (2)
\end{cases}
$$

Sostituiamo $(2)$ in $(1)$:
$$6x^2 - 4x\left(\frac{x(x + 1)}{3}\right) + 6x - 2\left(\frac{x(x + 1)}{3}\right) = 0$$
Moltiplichiamo tutto per $3$:
$$18x^2 - 4x^3 - 4x^2 + 18x - 2x^2 - 2x = 0$$
$$-4x^3 + 12x^2 + 16x = 0 \implies -4x(x^2 - 3x - 4) = 0$$
Le radici per $x$ sono:
1.  $x = 0 \implies y = 0$. Punto: $P_1 = (0, 0)$.
2.  $x^2 - 3x - 4 = 0 \implies (x - 4)(x + 1) = 0$:
    -   $x = 4 \implies y = \frac{4(5)}{3} = \frac{20}{3}$. Punto: $P_2 = (4, \frac{20}{3})$.
    -   $x = -1 \implies y = 0$. Punto: $P_3 = (-1, 0)$.

#### 2. Matrice Hessiana Generica
$$H_f(x, y) = \begin{bmatrix} 12x - 4y + 6 & -4x - 2 \\ -4x - 2 & 6 \end{bmatrix}$$

#### 3. Classificazione
-   **Valutazione in $P_1(0,0)$**:
    $$H_f(0, 0) = \begin{bmatrix} 6 & -2 \\ -2 & 6 \end{bmatrix} \implies \det(H) = 36 - 4 = 32 > 0, \quad \text{tr}(H) = 12 > 0 \implies \text{Minimo Locale}.$$
-   **Valutazione in $P_2(4,\frac{20}{3})$**:
    $$H_f\left(4, \frac{20}{3}\right) = \begin{bmatrix} 48 - \frac{80}{3} + 6 & -18 \\ -18 & 6 \end{bmatrix} = \begin{bmatrix} \frac{162 - 80}{3} & -18 \\ -18 & 6 \end{bmatrix} = \begin{bmatrix} \frac{82}{3} & -18 \\ -18 & 6 \end{bmatrix}$$
    $$\det(H) = \frac{82}{3} \cdot 6 - 324 = 164 - 324 = -160 < 0 \implies \text{Punto di Sella}.$$
-   **Valutazione in $P_3(-1,0)$**:
    $$H_f(-1, 0) = \begin{bmatrix} -6 & 2 \\ 2 & 6 \end{bmatrix} \implies \det(H) = -36 - 4 = -40 < 0 \implies \text{Punto di Sella}.$$

---

### Esercizio 8
Trovare massimi e minimi locali di:
$$f(x, y) = -4y^3 - 3xy^2 - x^2 + 2xy - 5y^2 + 2$$

#### 1. Sistema del Gradiente
$$
\begin{cases}
\frac{\partial f}{\partial x} = -3y^2 - 2x + 2y = 0 \implies 2x = 2y - 3y^2 \implies x = y - 1.5y^2 \quad (1) \\
\frac{\partial f}{\partial y} = -12y^2 - 6xy + 2x - 10y = 0 \quad (2)
\end{cases}
$$

Sostituiamo $x$ in $(2)$:
$$-12y^2 - 6y(y - 1.5y^2) + (2y - 3y^2) - 10y = 0$$
$$-12y^2 - 6y^2 + 9y^3 + 2y - 3y^2 - 10y = 0$$
$$9y^3 - 21y^2 - 8y = 0 \implies y(9y^2 - 21y - 8) = 0$$
Le radici per $y$ sono:
1.  $y = 0 \implies x = 0$. Punto: $P_1 = (0, 0)$.
2.  $9y^2 - 21y - 8 = 0 \implies y = \frac{21 \pm \sqrt{441 + 288}}{18} = \frac{21 \pm \sqrt{729}}{18} = \frac{21 \pm 27}{18}$:
    -   $y = \frac{48}{18} = \frac{8}{3} \implies x = \frac{8}{3} - 1.5\left(\frac{64}{9}\right) = \frac{8}{3} - \frac{32}{3} = -8$. Punto: $P_2 = (-8, \frac{8}{3})$.
    -   $y = -\frac{6}{18} = -\frac{1}{3} \implies x = -\frac{1}{3} - 1.5\left(\frac{1}{9}\right) = -\frac{1}{3} - \frac{1}{6} = -\frac{1}{2}$. Punto: $P_3 = (-\frac{1}{2}, -\frac{1}{3})$.

#### 2. Matrice Hessiana Generica
$$H_f(x, y) = \begin{bmatrix} -2 & -6y + 2 \\ -6y + 2 & -24y - 6x - 10 \end{bmatrix}$$

#### 3. Classificazione
-   **Valutazione in $P_1(0,0)$**:
    $$H_f(0, 0) = \begin{bmatrix} -2 & 2 \\ 2 & -10 \end{bmatrix} \implies \det(H) = 20 - 4 = 16 > 0, \quad \text{tr}(H) = -12 < 0 \implies \text{Massimo Locale}.$$
-   **Valutazione in $P_2(-8,\frac{8}{3})$**:
    $$H_f\left(-8, \frac{8}{3}\right) = \begin{bmatrix} -2 & -14 \\ -14 & -64 + 48 - 10 \end{bmatrix} = \begin{bmatrix} -2 & -14 \\ -14 & -26 \end{bmatrix}$$
    $$\det(H) = 52 - 196 = -144 < 0 \implies \text{Punto di Sella}.$$
-   **Valutazione in $P_3(-\frac{1}{2},-\frac{1}{3})$**:
    $$H_f(-\frac{1}{2}, -\frac{1}{3}) = \begin{bmatrix} -2 & 4 \\ 4 & 8 + 3 - 10 \end{bmatrix} = \begin{bmatrix} -2 & 4 \\ 4 & 1 \end{bmatrix}$$
    $$\det(H) = -2 - 16 = -18 < 0 \implies \text{Punto di Sella}.$$

---

## Errori Comuni da Evitare negli Scritti
1.  **Dimenticare soluzioni nel sistema non lineare**: Nel risolvere $\nabla f = 0$, spesso si semplifica dividendo per una variabile (es. per $x$ o $y$). Questo fa perdere punti stazionari cruciali (es. l'origine $(0,0)$). Raccogliere sempre a fattor comune.
2.  **Segno del termine misto $f_{xy}$**: Ricordare che l'Hessiana è simmetrica ($f_{xy} = f_{yx}$) per funzioni continue (teorema di Schwarz). Sbagliare la derivata incrociata invalida l'intera classificazione.
3.  **Conclusione errata su $\det(H) = 0$**: Se il determinante è zero, il punto non può essere classificato direttamente come sella o ottimo. Va specificato che il test è inconclusivo.

Vedi anche:
- [[pnl_non_vincolata_classificazione_hessiana]]
- [[pnl_20_esercizi_catalogo]]
