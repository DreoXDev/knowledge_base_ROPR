# Topic Card: Ottimizzazione PNL Non Vincolata

- **Punti Stazionari**: Punti in cui $\nabla f(x^*) = 0$.
- **Classificazione (Hessiano $H_f(x^*)$)**:
  - $H_f \succ 0$ (definita positiva: autovalori $>0$) $\implies$ **Minimo locale**.
  - $H_f \prec 0$ (definita negativa: autovalori $<0$) $\implies$ **Massimo locale**.
  - $H_f$ indefinita (autovalori di segni opposti) $\implies$ **Punto di sella**.
- **Analisi 2D Veloce**: Per $H = \begin{bmatrix} A & B \\ B & C \end{bmatrix}$:
  - $\det(H) = AC - B^2 > 0$ e $\text{tr}(H) = A+C > 0 \implies$ Minimo.
  - $\det(H) > 0$ e $\text{tr}(H) < 0 \implies$ Massimo.
  - $\det(H) < 0 \implies$ Sella.
- **Ottimi Globali**:
  - Se $H_f(x) \succeq 0 \quad \forall x \in \mathbb{R}^n \implies f$ convessa $\implies$ il punto stazionario è un minimo globale.
  - Se $H_f(x) \preceq 0 \quad \forall x \in \mathbb{R}^n \implies f$ concava $\implies$ il punto stazionario è un massimo globale.
- **Algoritmi**: Bisezione, Newton 1D, Gradiente con LS esatta, Newton n-D.
- **Fonti**: [[pnl_ottimizzazione_unidimensionale|Teoria 1D]], [[pnl_ottimizzazione_non_vincolata_multivariabile|Teoria Multivariabile]]
