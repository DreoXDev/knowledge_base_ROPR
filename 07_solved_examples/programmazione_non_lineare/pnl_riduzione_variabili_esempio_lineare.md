---
type: solved-example
topic: programmazione_non_lineare
status: consolidated
sources:
  - raw_assets/Programmazione Non Lineare/Ottimizzazione non lineare vincolata.pdf
reliability: official
---

# Esercizio Svolto: Riduzione delle Variabili Libere con Vincolo Lineare

## Testo dell'Esercizio

Si consideri il problema di ottimizzazione vincolata:

$$
\begin{aligned}
\min \quad & f(x_1, x_2) = (x_1 - 2)^2 + 2(x_2 - 1)^2 \\
\text{s.t. } & x_1 + 4x_2 = 3
\end{aligned}
$$

Risolvere il problema riducendo il numero di variabili libere tramite l'esplicitazione del vincolo di uguaglianza.

---

## Analisi Preliminare

1.  **Funzione Obiettivo**: $f(x_1, x_2)$ è una funzione quadratica strettamente convessa (la sua Hessiana è definita positiva $\nabla^2 f = \operatorname{diag}(2, 4)$).
2.  **Vincolo**: Il vincolo $x_1 + 4x_2 = 3$ è lineare (un'iperpiano/retta in $\mathbb{R}^2$).
3.  **Applicabilità**: Poiché il vincolo è lineare, è possibile esplicitare in modo univoco una delle due variabili in funzione dell'altra per eliminare un grado di libertà.

---

## Svolgimento Passo-Passo

### 1. Esplicitazione di una variabile
Isoliamo la variabile $x_1$ dall'equazione del vincolo:

$$x_1 + 4x_2 = 3 \implies x_1 = 3 - 4x_2$$

*(Avremmo potuto esplicitare anche $x_2 = \frac{3 - x_1}{4}$, ma la scelta di $x_1$ evita frazioni nei passaggi iniziali).*

### 2. Sostituzione nella Funzione Obiettivo
Sostituiamo l'espressione di $x_1$ nella funzione obiettivo per ottenere la funzione ridotta ad una sola variabile $\tilde{f}(x_2)$:

$$\tilde{f}(x_2) = \left( (3 - 4x_2) - 2 \right)^2 + 2(x_2 - 1)^2$$

Semplifichiamo l'espressione all'interno della prima parentesi:

$$\tilde{f}(x_2) = (1 - 4x_2)^2 + 2(x_2 - 1)^2$$

Sviluppiamo i quadrati:

$$\tilde{f}(x_2) = (1 - 8x_2 + 16x_2^2) + 2(x_2^2 - 2x_2 + 1)$$

$$\tilde{f}(x_2) = 1 - 8x_2 + 16x_2^2 + 2x_2^2 - 4x_2 + 2$$

Raggruppiamo i termini simili:

$$\tilde{f}(x_2) = 18x_2^2 - 12x_2 + 3$$

### 3. Ricerca del Punto Stazionario del Problema Ridotto
Calcoliamo la derivata prima della funzione ridotta $\tilde{f}(x_2)$ rispetto a $x_2$ e la poniamo pari a zero:

$$\tilde{f}'(x_2) = \frac{d}{dx_2}(18x_2^2 - 12x_2 + 3) = 36x_2 - 12$$

$$36x_2 - 12 = 0 \implies 36x_2 = 12 \implies x_2^* = \frac{12}{36} = \frac{1}{3}$$

### 4. Verifica della Condizione di Ottimalità del Secondo Ordine
Calcoliamo la derivata seconda della funzione ridotta per verificare la convessità:

$$\tilde{f}''(x_2) = 36$$

Poiché $\tilde{f}''(x_2) = 36 > 0$, la funzione ridotta $\tilde{f}(x_2)$ è strettamente convessa, il che garantisce che il punto stazionario trovato è un **punto di minimo globale**.

### 5. Ricostruzione della Variabile Eliminata
Sostituiamo il valore ottimo $x_2^* = \frac{1}{3}$ nella relazione di esplicitazione ottenuta nel primo passo per determinare $x_1^*$:

$$x_1^* = 3 - 4x_2^* = 3 - 4\left(\frac{1}{3}\right) = 3 - \frac{4}{3} = \frac{9 - 4}{3} = \frac{5}{3}$$

---

## Calcolo del Valore Ottimo della Funzione

Sostituiamo le coordinate ottime nella funzione obiettivo originale per trovare il valore minimo:

$$f\left(\frac{5}{3}, \frac{1}{3}\right) = \left(\frac{5}{3} - 2\right)^2 + 2\left(\frac{1}{3} - 1\right)^2$$

$$= \left(-\frac{1}{3}\right)^2 + 2\left(-\frac{2}{3}\right)^2 = \frac{1}{9} + 2\left(\frac{4}{9}\right) = \frac{1}{9} + \frac{8}{9} = \frac{9}{9} = 1$$

---

## Conclusione

-   **Punto di Minimo Ottimo Vincolato**: $x^* = \left(\frac{5}{3}, \frac{1}{3}\right)$
-   **Valore Ottimo Minimo**: $f(x^*) = 1$

Vedi anche:
- [[pnl_riduzione_variabili_libere]]
- [[pnl_metodo_moltiplicatori_lagrange]]
