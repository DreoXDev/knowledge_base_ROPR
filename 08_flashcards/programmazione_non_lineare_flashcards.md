# Flashcard Programmazione Non Lineare (PNL)

#flashcards/pnl

## Q: Qual è la formulazione generale di un problema di programmazione non lineare?
A: 
$$
\begin{aligned}
\min/\max \quad & f(x) \\
\text{s.t. } & g_i(x) = 0 \quad i = 1, \dots, m \\
& h_j(x) \le 0 \quad j = 1, \dots, p \\
& x \in \mathbb{R}^n
\end{aligned}
$$
dove $f, g_i, h_j$ sono funzioni reali, e almeno una di esse è non lineare.
<!-- Estensione: Rop-PNL-Formulazione -->

## Q: Qual è la condizione necessaria del primo ordine per un punto stazionario di una funzione non vincolata?
A: Il gradiente della funzione si annulla nel punto:
$$\nabla f(x^*) = 0$$
<!-- Estensione: Rop-PNL-Stazionarieta -->

## Q: Come si classifica un punto stazionario $x^*$ in base alla matrice Hessiana $H_f(x^*)$?
A: 
- $H_f(x^*) \succ 0$ (definita positiva) $\implies$ **Minimo locale**.
- $H_f(x^*) \prec 0$ (definita negativa) $\implies$ **Massimo locale**.
- $H_f(x^*)$ indefinita $\implies$ **Punto di sella**.
- $H_f(x^*)$ semidefinita $\implies$ Criterio non sufficiente (caso d'indeterminazione).
<!-- Estensione: Rop-PNL-ClassificazioneHessiana -->

## Q: Quali sono le relazioni veloci in 2D per studiare la segnatura di $H_f(x^*) = \begin{bmatrix} A & B \\ B & C \end{bmatrix}$?
A: Si calcolano il determinante $\det(H) = AC - B^2$ e la traccia $\text{tr}(H) = A + C$:
- $\det(H) > 0$ e $\text{tr}(H) > 0 \implies$ Minimo locale.
- $\det(H) > 0$ e $\text{tr}(H) < 0 \implies$ Massimo locale.
- $\det(H) < 0 \implies$ Punto di sella.
- $\det(H) = 0 \implies$ Caso degenere.
<!-- Estensione: Rop-PNL-Hessiano2D -->

## Q: Cos'è il metodo di Newton 1D e qual è la sua formula di aggiornamento?
A: È un algoritmo di approssimazione locale per trovare zeri di $f'(x) = 0$:
$$x_{k+1} = x_k - \frac{f'(x_k)}{f''(x_k)}$$
<!-- Estensione: Rop-PNL-Newton1D -->

## Q: Cos'è il metodo del gradiente (steepest descent) con line search esatta?
A: È un algoritmo di ottimizzazione non vincolata in cui ad ogni iterazione ci si sposta lungo la direzione di massima discesa $d_k = -\nabla f(x_k)$ con un passo $\alpha_k$ che risolve il problema unidimensionale di minimo esatto:
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
A: Per le funzioni quadratiche ad Hessiana definita positiva, in quanto lo sviluppo di Taylor al secondo ordine coincide esattamente con la funzione stessa.
<!-- Estensione: Rop-PNL-NewtonQuadratica -->

## Q: Quali sono le condizioni KKT per un problema di minimo $\min f(x)$ s.t. $g_i(x)=0, h_j(x) \le 0$?
A: 
1. **Stazionarietà**: $\nabla f(x^*) + \sum \lambda_i^* \nabla g_i(x^*) + \sum \mu_j^* \nabla h_j(x^*) = 0$
2. **Ammissibilità Primale**: $g_i(x^*) = 0, \quad h_j(x^*) \le 0$
3. **Ammissibilità Duale**: $\mu_j^* \ge 0$
4. **Complementarità**: $\mu_j^* \cdot h_j(x^*) = 0$
<!-- Estensione: Rop-PNL-CondizioniKKT -->

## Q: Come varia il segno dei moltiplicatori $\mu_j$ nelle condizioni KKT per un problema di massimo ($\max f(x)$ s.t. $h_j(x) \le 0$)?
A: Per problemi di massimo, la stazionarietà e complementarità rimangono uguali, ma i moltiplicatori dei vincoli attivi devono essere non positivi:
$$\mu_j^* \le 0$$
<!-- Estensione: Rop-PNL-KKTMaxSegno -->

## Q: Cosa significa che un vincolo di disuguaglianza $h_j(x) \le 0$ è "attivo" o "inattivo" in un punto ammissibile $x^*$?
A: 
- **Attivo**: se $h_j(x^*) = 0$. Il punto giace sul bordo del vincolo; il moltiplicatore $\mu_j^*$ può essere non nullo.
- **Inattivo**: se $h_j(x^*) < 0$. Il punto giace all'interno del semispazio ammissibile; per complementarità si ha necessariamente $\mu_j^* = 0$.
<!-- Estensione: Rop-PNL-VincoloAttivoInattivo -->
