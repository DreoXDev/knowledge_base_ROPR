# Topic Card: KKT e Vincoli Attivi in PNL

- **Vincolo Attivo**: Nel punto ottimo $x^*$, vale $g_i(x^*) = 0$ (sulla frontiera del vincolo).
- **Vincolo Inattivo**: Nel punto ottimo $x^*$, vale $g_i(x^*) < 0$ (all'interno del semispazio del vincolo).
- **Condizione di Complementarità**: $\mu_i g_i(x^*) = 0 \quad \forall i$.
  - Se il vincolo è inattivo ($g_i(x^*) < 0$), il moltiplicatore deve essere nullo: $\mu_i^* = 0$.
  - Se il vincolo è attivo ($g_i(x^*) = 0$), il moltiplicatore può essere positivo: $\mu_i^* \ge 0$.
- **Enumerazione dei Casi**: Con $m$ vincoli di disuguaglianza, si analizzano fino a $2^m$ casi, ponendo $\mu_i = 0$ per i vincoli inattivi e $g_i(x) = 0$ per i vincoli attivi.
- **Regole di Scarto dei Candidati**:
  - Il punto viola l'ammissibilità primale ($g_i(x^*) > 0$ per un qualunque vincolo).
  - Il moltiplicatore di un vincolo attivo è negativo ($\mu_i < 0$ per un problema di minimo).
  - Il sistema di vincoli attivi è geometricamente incompatibile.
- **Fonti**: [[pnl_vincolata_kkt_vincoli_attivi|KKT Vincoli Attivi]], [[MC_PNL_KKT_vincoli_disuguaglianza|Method Card KKT Disuguaglianze]].
