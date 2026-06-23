---
type: solved-example
topic: programmazione_non_lineare
status: consolidated
sources:
  - raw_assets/Programmazione Non Lineare/Ottimizzazione non lineare vincolata.pdf
reliability: official
---

# Esercizio Svolto: Moltiplicatori di Lagrange su Cerchio Unitario

## Testo dell'Esercizio

Si consideri il problema di ottimizzazione vincolata:

$$
\begin{aligned}
\min/\max \quad & f(x_1, x_2) = x_1 + x_2 \\
\text{s.t. } & x_1^2 + x_2^2 = 1
\end{aligned}
$$

Trovare i punti di minimo e massimo globale vincolati della funzione obiettivo sulla circonferenza unitaria.

---

## Analisi Preliminare

1. **Funzione Obiettivo**: $f(x_1, x_2) = x_1 + x_2$ è lineare, continua e differenziabile su tutto $\mathbb{R}^2$.
2. **Regione Ammissibile**: Il vincolo $g(x_1, x_2) = x_1^2 + x_2^2 - 1 = 0$ definisce una circonferenza di raggio $1$ centrata nell'origine. Poiché questo insieme è chiuso e limitato in $\mathbb{R}^2$, esso è **compatto**.
3. **Esistenza degli Ottimi**: Per il Teorema di Weierstrass, la funzione continua $f$ ammette sicuramente almeno un punto di massimo globale e uno di minimo globale su tale cerchio.
4. **Qualificazione dei Vincoli (LICQ)**: Il gradiente del vincolo è $\nabla g(x_1, x_2) = [2x_1, 2x_2]^T$. Esso si annulla solo nell'origine $(0,0)$, che non appartiene alla circonferenza. Quindi LICQ è soddisfatta in ogni punto ammissibile.

---

## Costruzione della Lagrangiana

Definiamo la funzione Lagrangiana:

$$L(x_1, x_2, \lambda) = x_1 + x_2 + \lambda(x_1^2 + x_2^2 - 1)$$

---

## Sistema delle Condizioni del Primo Ordine

Per trovare i punti candidati, imponiamo $\nabla L(x_1, x_2, \lambda) = 0$:

$$
\begin{cases}
\frac{\partial L}{\partial x_1} = 1 + 2\lambda x_1 = 0 \quad (1) \\
\frac{\partial L}{\partial x_2} = 1 + 2\lambda x_2 = 0 \quad (2) \\
\frac{\partial L}{\partial \lambda} = x_1^2 + x_2^2 - 1 = 0 \quad (3)
\end{cases}
$$

---

## Risoluzione del Sistema

Dalle equazioni $(1)$ e $(2)$, si nota che $\lambda \neq 0$ (altrimenti avremmo $1 = 0$, impossibile). Possiamo quindi esprimere $x_1$ e $x_2$ in funzione di $\lambda$:

$$x_1 = -\frac{1}{2\lambda}$$

$$x_2 = -\frac{1}{2\lambda}$$

In particolare, questo implica che nei punti stazionari vincolati deve valere:

$$x_1 = x_2$$

Sostituiamo $x_1 = x_2$ nella terza equazione (il vincolo):

$$x_1^2 + x_1^2 = 1 \implies 2x_1^2 = 1 \implies x_1^2 = \frac{1}{2}$$

Otteniamo quindi due possibili valori per $x_1$:

$$x_1 = \pm\frac{1}{\sqrt{2}}$$

Poiché $x_1 = x_2$, si individuano due punti candidati:

1.  **Punto A**:
    $$A = \left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$$
    con moltiplicatore $\lambda_A$:
    $$\frac{1}{\sqrt{2}} = -\frac{1}{2\lambda_A} \implies \lambda_A = -\frac{\sqrt{2}}{2}$$

2.  **Punto B**:
    $$B = \left(-\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right)$$
    con moltiplicatore $\lambda_B$:
    $$-\frac{1}{\sqrt{2}} = -\frac{1}{2\lambda_B} \implies \lambda_B = \frac{\sqrt{2}}{2}$$

---

## Classificazione dei Punti Ottimi

Valutiamo la funzione obiettivo $f(x_1, x_2) = x_1 + x_2$ nei due punti candidati:

-   **Valutazione nel punto A**:
    $$f(A) = f\left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right) = \frac{1}{\sqrt{2}} + \frac{1}{\sqrt{2}} = \frac{2}{\sqrt{2}} = \sqrt{2} \approx 1.414$$

-   **Valutazione nel punto B**:
    $$f(B) = f\left(-\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right) = -\frac{1}{\sqrt{2}} - \frac{1}{\sqrt{2}} = -\frac{2}{\sqrt{2}} = -\sqrt{2} \approx -1.414$$

---

## Interpretazione Geometrica dei Moltiplicatori

Nel punto ottimo:
$$\nabla f(x^*) = -\lambda^* \nabla g(x^*)$$

Verifichiamo questa relazione:
-   **Gradiente della funzione obiettivo**: $\nabla f(x) = [1, 1]^T$ (indipendente da $x$).
-   **Gradiente del vincolo nel punto A**:
    $$\nabla g(A) = \left[ 2\left(\frac{1}{\sqrt{2}}\right), 2\left(\frac{1}{\sqrt{2}}\right) \right]^T = [\sqrt{2}, \sqrt{2}]^T$$
    Si ha infatti:
    $$\nabla f(A) = \begin{bmatrix} 1 \\ 1 \end{bmatrix} = -\lambda_A \nabla g(A) = -\left(-\frac{\sqrt{2}}{2}\right) \begin{bmatrix} \sqrt{2} \\ \sqrt{2} \end{bmatrix} = \frac{\sqrt{2}}{2} \begin{bmatrix} \sqrt{2} \\ \sqrt{2} \end{bmatrix} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$$
    I gradienti sono paralleli e concordi, indicando che la direzione di massima crescita della funzione è concorde con la frontiera verso l'esterno del cerchio.

---

## Conclusione

-   **Massimo Globale Vincolato**: Si trova in $A = \left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$ con valore massimo pari a $f^*_{\max} = \sqrt{2}$.
-   **Minimo Globale Vincolato**: Si trova in $B = \left(-\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right)$ con valore minimo pari a $f^*_{\min} = -\sqrt{2}$.

Vedi anche:
- [[pnl_metodo_moltiplicatori_lagrange]]
- [[pnl_ottimizzazione_vincolata]]
