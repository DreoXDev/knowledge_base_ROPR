# Ingestion Report — PNL Esercizi e Riepiloghi

## Metadata

- Source IDs:
  - `SRC-0087` (`raw_assets/Programmazione Non Lineare/20_esercizi_pnl.pdf`)
  - `SRC-0088` (`raw_assets/Programmazione Non Lineare/esercizi_riepilogo.pdf`)
  - `SRC-0095` (`raw_assets/Programmazione Non Lineare/PNL_non_vincolata.pdf`)
- Tipo file: PDF
- Categoria: Esercizi d'esame proposti con soluzioni
- Area ROPR: Programmazione Non Lineare (PNL)
- Affidabilità: Ufficiale (official)
- Stato analisi: Completato (consolidated)

## Sintesi Contenuto

Questi tre asset raccolgono le prove d'esame e le esercitazioni pratiche dedicate a problemi di programmazione non lineare (vincolata e non vincolata) ed a riepiloghi generali del corso (incluso simplesso e branch and bound). Contengono un totale di oltre 30 esercizi con risposte sintetiche o dettagliate, che rappresentano i precisi pattern d'esame richiesti dai docenti.

## Argomenti Estratti

- **Esercizi non vincolati**:
  - Calcolo di punti stazionari di funzioni polinomiali $f(x, y)$ in 2 variabili.
  - Studio della concavità/convessità globale o locale tramite matrice Hessiana e calcolo del determinante/traccia per la classificazione degli autovalori.
  - Applicazione pratica del metodo del gradiente (discesa rapida) con calcolo esatto del passo tramite line search analitica.
  - Applicazione pratica di una iterazione del metodo di Newton multivariabile a partire da un punto dato.
- **Esercizi vincolati**:
  - Ricerca di massimi/minimi globali e locali su insiemi chiusi e limitati (es. cerchio, triangolo, parabole) applicando le condizioni di Karush-Kuhn-Tucker (KKT).
  - Gestione analitica di vincoli attivi e inattivi.
  - Disegno delle curve di livello della funzione obiettivo e della regione ammissibile per risolvere graficamente o confermare i risultati algebrici (es. Esercizio 3 di `PNL_vincolata.pdf`).

## File Creati / Aggiornati

- `07_solved_examples/programmazione_non_lineare/pnl_esercizi_non_vincolati.md`
- `07_solved_examples/programmazione_non_lineare/pnl_esercizi_vincolati_kkt.md`
- `10_rag/RAG_RETRIEVAL_INDEX.md`
- `10_rag/RAG_PATTERN_MAP.md`

## Warning / Refusi / Incongruenze Rilevate

- **Esercizio 3 di `PNL_vincolata.pdf`**: Si richiede di notare che disegnando la regione ammissibile $\Omega$ e gli insiemi di livello di $f(x, y) = x + y$, la regione non è limitata superiormente né inferiormente in modo da garantire massimi/minimi globali. L'albero KKT fornisce soluzioni locali che richiedono la verifica grafica degli insiemi di livello per stabilire se siano effettivi punti di massimo/minimo locale o punti di sella. Questo comportamento è dettagliato in `pnl_esercizi_vincolati_kkt.md` ed è una traccia d'esame tipica.
- **Precisione dei Calcoli**: Negli esercizi di discesa del gradiente, i coefficienti e i passi possono produrre frazioni complesse (es. Esercizio 8 di `PNL_non_vincolata.pdf` con frazioni a 12 cifre). Nella KB consigliamo di mantenere la forma frazionaria esatta o approssimare con 4 cifre decimali se esplicitamente ammesso all'esame, per evitare errori di calcolo.
