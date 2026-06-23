# Topic Card: Moltiplicatori di Lagrange (Uguaglianze)

- **Lagrangiana**: $L(x, \lambda) = f(x) + \sum_{i=1}^m \lambda_i g_i(x)$.
- **Punti candidati**: Punti stazionari vincolati che soddisfano il sistema del primo ordine $\nabla_x L = 0$ e $\nabla_\lambda L = 0$ (ovvero $g_i(x) = 0$).
- **Interpretazione Geometrica**: Nel punto ottimo stazionario $x^*$, il gradiente della funzione obiettivo $\nabla f(x^*)$ è ortogonale allo spazio tangente del vincolo e parallelo al gradiente del vincolo stesso:
  $$\nabla f(x^*) = -\lambda^* \nabla g(x^*)$$
- **Segno dei Moltiplicatori**: I moltiplicatori $\lambda_i$ associati a vincoli di uguaglianza sono **liberi** in segno (possono essere positivi, negativi o nulli).
- **Classificazione**: Poiché le condizioni sono necessarie ma non sufficienti, i candidati vanno valutati calcolando la funzione obiettivo nei punti stazionari o studiando la matrice Hessiana Orlata.
- **Fonti**: [[pnl_metodo_moltiplicatori_lagrange|Metodo dei Moltiplicatori di Lagrange]], [[pnl_lagrange_cerchio_unitario|Esempio Cerchio Unitario]]
