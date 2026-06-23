# Topic Card: Ottimizzazione PNL Vincolata e KKT

- **Lagrangiana Generalizzata**:
  $$L(x, \lambda, \mu) = f(x) + \sum_{i=1}^m \lambda_i g_i(x) + \sum_{j=1}^p \mu_j h_j(x)$$
- **Condizioni KKT (per $\min f(x)$ con $h_j(x) \le 0$)**:
  1. *Stazionarietà*: $\nabla_x L = \nabla f(x^*) + \sum \lambda_i^* \nabla g_i(x^*) + \sum \mu_j^* \nabla h_j(x^*) = 0$
  2. *Ammissibilità Primale*: $g_i(x^*) = 0, \quad h_j(x^*) \le 0$
  3. *Ammissibilità Duale*: $\mu_j^* \ge 0$ (Nota: per problemi di **massimo**, $\mu_j^* \le 0$)
  4. *Complementarità*: $\mu_j^* h_j(x^*) = 0$
- **Risoluzione per Casi**: Si esplorano combinazioni di vincoli attivi ($h_j = 0$, $\mu_j$ libero) e inattivi ($h_j < 0 \implies \mu_j = 0$).
- ** LICQ (Regolarità)**: I gradienti dei vincoli attivi nel punto $x^*$ devono essere linearmente indipendenti affinché la stazionarietà KKT sia necessaria.
- **Teorema di Weierstrass**: Se la regione ammissibile è compatta (chiusa e limitata), esistono sicuramente punti di minimo e massimo globale. Si valutano tutti i punti KKT ammissibili per trovarli.
- **Fonti**: [[pnl_ottimizzazione_vincolata|Teoria Ottimizzazione Vincolata]], [[pnl_condizioni_kkt|Metodo KKT]], [[pnl_combinatoria_vincoli_attivi|Metodo Combinatorio Vincoli]]
