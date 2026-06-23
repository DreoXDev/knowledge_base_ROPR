# Topic Card: Esercizi PNL Non Vincolata (Punti Stazionari)

- **Obiettivo**: Ricerca dei punti stazionari di funzioni $f(x, y)$ non vincolate ed analisi della loro stabilità locale (massimi locali, minimi locali, punti di sella) o convessità globale.
- **Formule Chiave**:
  - Annullamento gradiente: $\nabla f(x, y) = 0$.
  - Matrice Hessiana: $H_f(x, y) = \begin{bmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{bmatrix}$.
- **Classificazione dei punti stazionari**:
  - $\det(H) > 0, \text{tr}(H) > 0 \implies$ minimo locale.
  - $\det(H) > 0, \text{tr}(H) < 0 \implies$ massimo locale.
  - $\det(H) < 0 \implies$ sella.
  - $\det(H) = 0 \implies$ caso semidefinito (test non conclusivo).
- **Convessità e Ottimo Globale**:
  - Se $H_f(x,y) \succeq 0 \quad \forall (x,y) \in \mathbb{R}^2$, la funzione è convessa $\implies$ i minimi locali sono minimi globali.
  - Se $H_f(x,y) \preceq 0 \quad \forall (x,y) \in \mathbb{R}^2$, la funzione è concava $\implies$ i massimi locali sono massimi globali.
- **Esercizi di Riferimento**: [[pnl_non_vincolata_esercizi_punti_stazionari]] (esercizi 1-10 di `20_esercizi_pnl.pdf`).
- **Fonti**: [[pnl_20_esercizi_catalogo|Catalogo 20 Esercizi]], [[pnl_non_vincolata_classificazione_hessiana|Pattern Hessiana]]
