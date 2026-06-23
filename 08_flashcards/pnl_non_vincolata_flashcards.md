# Flashcard Programmazione Non Lineare Non Vincolata

#flashcards/pnl/non-vincolata

## Q: Qual è la condizione necessaria del primo ordine per un punto stazionario di una funzione non vincolata?
A: Il gradiente della funzione si annulla nel punto:
$$\nabla f(x^*) = 0$$
<!-- Estensione: Rop-PNL-Stazionarieta -->

## Q: Come si classifica un punto stazionario $x^*$ in base alla matrice Hessiana $H_f(x^*)$?
A: 
- $H_f(x^*) \succ 0$ (definita positiva) $\implies$ **Minimo locale**.
- $H_f(x^*) \prec 0$ (definita negativa) $\implies$ **Massimo locale**.
- $H_f(x^*)$ indefinita $\implies$ **Punto di sella**.
- $H_f(x^*)$ semidefinita $\implies$ Criterio del secondo ordine non sufficiente.
<!-- Estensione: Rop-PNL-ClassificazioneHessiana -->

## Q: Quali sono le relazioni veloci in 2D per studiare la segnatura di $H_f(x^*) = \begin{bmatrix} A & B \\ B & C \end{bmatrix}$?
A: Si calcolano il determinante $\det(H) = AC - B^2$ e la traccia $\text{tr}(H) = A + C$:
- $\det(H) > 0$ e $\text{tr}(H) > 0 \implies$ Minimo locale.
- $\det(H) > 0$ e $\text{tr}(H) < 0 \implies$ Massimo locale.
- $\det(H) < 0 \implies$ Punto di sella.
- $\det(H) = 0 \implies$ Caso degenere (semidefinita).
<!-- Estensione: Rop-PNL-Hessiano2D -->

## Q: Cos'è il metodo del gradiente (steepest descent) con line search esatta?
A: È un algoritmo di ottimizzazione non vincolata in cui ci si sposta lungo la direzione di massima discesa $d_k = -\nabla f(x_k)$ con un passo $\alpha_k$ che minimizza esplicitamente la funzione obiettivo lungo quella retta:
$$\alpha_k = \arg\min_{\alpha \ge 0} f(x_k - \alpha \nabla f(x_k))$$
<!-- Estensione: Rop-PNL-GradienteLS -->

## Q: Qual è la relazione geometrica tra due direzioni consecutive $d_{k-1}$ e $d_k$ nel metodo del gradiente con line search esatta?
A: Le direzioni consecutive sono sempre ortogonali:
$$d_k^T d_{k-1} = 0$$
Questo provoca l'effetto di andamento a "zig-zag" se le curve di livello sono strette ed allungate.
<!-- Estensione: Rop-PNL-OrtogonalitaGradiente -->

## Q: Qual è la direzione di spostamento $d_k$ del metodo di Newton multivariabile?
A: È la soluzione del sistema lineare:
$$H_f(x_k) d_k = -\nabla f(x_k)$$
Con passo standard $\alpha_k = 1$.
<!-- Estensione: Rop-PNL-NewtonMultivariabile -->

## Q: Per quali tipi di funzioni il metodo di Newton multivariabile converge all'ottimo esatto in una sola iterazione?
A: Per le funzioni quadratiche ad Hessiana definita positiva/negativa, in quanto lo sviluppo di Taylor al secondo ordine coincide esattamente con la funzione stessa.
<!-- Estensione: Rop-PNL-NewtonQuadratica -->
