# Flashcards: Esercizi PNL (Non Vincolata e Vincolata KKT)

- **Q**: Quali sono i tre passi principali per trovare massimi e minimi locali di una funzione $f(x, y)$ non vincolata?
  **A**:
  1. Calcolare il gradiente $\nabla f(x, y)$ ed annullarlo.
  2. Risolvere il sistema per i punti stazionari.
  3. Calcolare la matrice Hessiana $H_f(x, y)$ e classificarne il segno in ciascun punto.

- **Q**: Qual è il test locale per classificare un punto stazionario $P^*$ tramite determinante e traccia dell'Hessiana in due variabili?
  **A**:
  - $\det(H_f(P^*)) > 0$ e $\text{tr}(H_f(P^*)) > 0 \implies$ minimo locale.
  - $\det(H_f(P^*)) > 0$ e $\text{tr}(H_f(P^*)) < 0 \implies$ massimo locale.
  - $\det(H_f(P^*)) < 0 \implies$ punto di sella.

- **Q**: Se $\det(H_f(P^*)) = 0$, cosa si può concludere?
  **A**: Il test dell'Hessiana è inconclusivo. La matrice è semidefinita. Occorre uno studio locale supplementare (es. restrizioni a curve o riscrittura algebrica).

- **Q**: Nei problemi KKT d'esame per massimi e minimi globali, come si gestisce una regione ammissibile non limitata (non compatta)?
  **A**: Weierstrass non è garantito. Bisogna analizzare il limite della funzione obiettivo lungo direzioni ammissibili per verificare se la funzione diverge ad infinito (inesistenza dell'ottimo globale).

- **Q**: In KKT con vincoli in forma standard $h_j(x, y) \le 0$, quali sono i segni dei moltiplicatori $\mu_j$ per minimo e massimo?
  **A**: Per il minimo $\mu_j \ge 0$, per il massimo $\mu_j \le 0$ (per vincoli attivi; per i vincoli inattivi è sempre $\mu_j = 0$).
