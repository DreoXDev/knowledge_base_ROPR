# Method Card: Risoluzione di Sistemi KKT e Analisi dei Vincoli

- **Obiettivo**: Ricerca dei punti di ottimo vincolato (massimo/minimo) con vincoli di disuguaglianza.
- **Passi Risolutivi**:
  1. Convertire i vincoli in forma standard $h_j(x) \le 0$ (moltiplicando per $-1$ se necessario).
  2. Impostare la Lagrangiana generalizzata: $L(x, \mu) = f(x) + \sum \mu_j h_j(x)$.
  3. Calcolare il gradiente $\nabla_x L = 0$ (Stazionarietà).
  4. Impostare la complementarità degli scarti: $\mu_j h_j(x) = 0$ per ogni vincolo.
  5. Esplorare sistematicamente i $2^p$ casi di vincoli attivi ($h_j(x) = 0$, $\mu_j$ libero) ed inattivi ($h_j(x) < 0 \implies \mu_j = 0$).
  6. Per ogni caso, risolvere il sistema lineare o non lineare per ricavare $x^*$ e $\mu^*$.
  7. **Filtrare** i risultati controllando:
     - Ammissibilità primale ($h_j(x^*) \le 0$ per i vincoli inattivi).
     - Ammissibilità duale ($\mu_j^* \ge 0$ per problemi di **minimo**, $\mu_j^* \le 0$ per problemi di **massimo**).
  8. Confrontare i valori di $f(x^*)$ dei punti KKT ammissibili per determinare massimo/minimo globale.
- **Esempio di Calcolo**: Vedi [[pnl_condizioni_kkt|KKT Metodo]] e [[pnl_esercizi_vincolati_kkt|Esempi Vincolati KKT]].
