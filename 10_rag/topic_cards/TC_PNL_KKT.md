# Topic Card: Condizioni di Karush-Kuhn-Tucker (KKT)

- **Problema in forma standard**:
  $$\min/\max \quad f(x) \quad \text{s.t.} \quad g_i(x) = 0 \quad (\forall i), \quad h_j(x) \le 0 \quad (\forall j)$$
- **Lagrangiana Generalizzata**:
  $$L(x, \lambda, \mu) = f(x) + \sum_{i=1}^m \lambda_i g_i(x) + \sum_{j=1}^p \mu_j h_j(x)$$
- **Condizioni necessarie KKT**:
  1. **Stazionarietà**: $\nabla_x L(x^*, \lambda^*, \mu^*) = 0$.
  2. **Ammissibilità Primale**: $g_i(x^*) = 0$ e $h_j(x^*) \le 0$.
  3. **Complementarità degli scarti**: $\mu_j^* \cdot h_j(x^*) = 0$.
  4. **Ammissibilità Duale (Segno di $\mu_j^*$)**:
     - Per problemi di **minimo**: $\mu_j^* \ge 0$.
     - Per problemi di **massimo**: $\mu_j^* \le 0$.
- **Vincoli Attivi vs Inattivi**:
  - **Inattivo**: $h_j(x^*) < 0 \implies \mu_j^* = 0$ (per complementarità).
  - **Attivo**: $h_j(x^*) = 0 \implies \mu_j^*$ è libero di assumere il segno prescritto dall'ammissibilità duale.
- **Fonti**: [[pnl_condizioni_kkt|Condizioni KKT]], [[pnl_vincoli_attivi_e_complementarita|Vincoli Attivi e complementarità]]
