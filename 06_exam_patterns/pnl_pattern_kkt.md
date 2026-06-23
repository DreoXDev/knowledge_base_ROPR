# Pattern d'Esame: Ottimizzazione Vincolata (KKT)

## Descrizione del Pattern
Esercizi in cui si richiede di calcolare i punti di massimo o minimo globale vincolato di una funzione su una regione definita da vincoli di uguaglianza o disuguaglianza, impostando e risolvendo il sistema KKT.

## Trigger RAG
- "utilizzando le condizioni KKT"
- "massimi e minimi globali vincolati"
- "regione ammissibile triangolo"
- "circonferenza vincolo KKT"
- "segno dei moltiplicatori per massimo"

## Schema di Risposta Atteso

1. **Analisi Preliminare**:
   * Descrivere geometricamente la regione ammissibile (es. triangolo, cerchio) per stabilire se sia chiusa e limitata (compatta).
   * Citare il Teorema di Weierstrass per garantire l'esistenza di massimi/minimi globali.
2. **Formulazione Matematica**:
   * Riscrivere tutti i vincoli in forma standard $h_j(x, y) \le 0$ o $g_i(x, y) = 0$.
   * Costruire la Lagrangiana $L(x, y, \mu_j, \lambda_i)$.
3. **Impostazione del Sistema KKT**:
   * Scrivere le equazioni di stazionarietà per tutte le variabili decisionali.
   * Scrivere le condizioni di ammissibilità primale.
   * Scrivere le equazioni di complementarità degli scarti: $\mu_j h_j(x, y) = 0$.
   * Specificare i vincoli di segno per i moltiplicatori di disuguaglianza: $\mu_j \ge 0$ per la ricerca di minimi, oppure $\mu_j \le 0$ per la ricerca di massimi.
4. **Risoluzione per Casi Combinatori**:
   * Esplorare sistematicamente le combinazioni di vincoli attivi e inattivi.
   * Per ciascun caso, risolvere il sistema lineare o non lineare derivante.
5. **Filtraggio dei Candidati**:
   * Verificare l'ammissibilità primale (se il punto giace nella regione $\Omega$).
   * Verificare l'ammissibilità duale (segno corretto dei moltiplicatori $\mu_j$).
6. **Conclusione**:
   * Valutare la funzione obiettivo nei punti candidati validi rimasti.
   * Dichiarare i minimi/massimi globali e i relativi moltiplicatori ottimi.
   * Nel caso di regioni non limitate (non compatte), integrare l'analisi algebrica con lo studio qualitativo degli insiemi di livello per escludere selle o divergenze.
