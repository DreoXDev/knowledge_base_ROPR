# Topic Card: Esempi di Risoluzione KKT Vincolata

- **Problema quadratico con 3 vincoli lineari**:
  - $\min f(x, y) = 4(x-1)^2 + (y-2)^2$ s.t. $x+y \le 2, \ x \ge -1, \ y \ge -1$.
  - Vincoli standardizzati: $g_1 = x+y-2 \le 0$, $g_2 = -x-1 \le 0$, $g_3 = -y-1 \le 0$.
- **Casi di scarto principali**:
  - Caso non vincolato ($\mu = 0$): ottimo $(1,2)$ cade fuori dalla regione ammissibile ($1+2 = 3 > 2$, viola $g_1$).
  - Caso solo $g_2$ attivo ($\mu_2 \ge 0, \mu_1=\mu_3=0$): punto candidato $(-1, 2)$ con moltiplicatore $\mu_2 = -16 < 0$ (scartato).
  - Caso solo $g_3$ attivo ($\mu_3 \ge 0, \mu_1=\mu_2=0$): punto candidato $(1, -1)$ con moltiplicatore $\mu_3 = -6 < 0$ (scartato).
- **Ottimo Globale**:
  - Trovato nel Caso 1 (solo $g_1$ attivo): $x^* = (0.8, 1.2)$, moltiplicatori $\mu_1^* = 1.6 > 0, \mu_2^* = \mu_3^* = 0$, con valore ottimo $f(x^*) = 0.8$.
- **Interpretazione Geometrica**:
  - Le curve di livello di $f(x,y)$ sono ellissi centrate nell'ottimo non vincolato $(1,2)$.
  - La regione ammissibile è un poligono in $\mathbb{R}^2$.
  - L'ottimo vincolato è il punto di tangenza tra la curva di livello più piccola e il lato del poligono $x+y=2$.
- **Fonti**: [[pnl_kkt_esempio_quadratico_3_vincoli|Esercizio Svolto KKT 3 Vincoli]], [[pnl_vincolata_kkt_vincoli_attivi|KKT Vincoli Attivi]].
