# Ingestion Report — Ricerca Operativa - Metodo del Simplesso - 23-24.pdf

## Metadata

- Source ID: `SRC-0077` (dal SOURCE_INVENTORY.md)
- Path: `raw_assets/Programmazione Lineare/Ricerca Operativa - Metodo del Simplesso - 23-24.pdf`
- Tipo file: PDF
- Categoria: Slide / Dispense ufficiali del corso
- Area ROPR: Programmazione Lineare
- Affidabilità: Ufficiale (official)
- Stato analisi: Completato (consolidated)

## Sintesi Contenuto
Il documento fornisce la trattazione geometrica ed algebrica completa del metodo del simplesso per la programmazione lineare. Tratta in modo sistematico l'adiacenza dei vertici, lo spigolo e la frontiera dei vincoli; definisce la forma aumentata del modello con l'introduzione delle variabili di slack; descrive algebricamente i gradi di libertà ($n-m$), le variabili di base e non di base, e la soluzione di base; formalizza la procedura tabellare del simplesso (scelta della variabile entrante e uscente tramite test dei rapporti minimi, operazione di pivotaggio); e analizza approfonditamente tutti i casi particolari (degenerazione, illimitatezza, ottimi multipli, e tie breaking).

## Argomenti Estratti
- **Geometria del simplesso**: Concetto di frontiera, vertice ammissibile/non ammissibile, spigoli, adiacenza (condivisione di $n-1$ frontiere), test di ottimalità geometrico (nessun vertice adiacente migliore).
- **Forma aumentata e basi**: Standardizzazione del modello con slack ($s_i \ge 0$), suddivisione delle variabili in base e fuori base, gradi di libertà, corrispondenza biunivoca tra vertici e soluzioni di base ammissibili.
- **Simplesso tabellare**: Riga 0 (funzione obiettivo riorganizzata), regola dei costi ridotti per la variabile entrante (massimo miglioramento unitario), test dei rapporti minimi per la variabile uscente, operazione algebrica di pivotaggio tramite eliminazione gaussiana.
- **Casi particolari**: Tie breaking (scelta arbitraria in caso di parità), degenerazione (soluzione di base con variabili nulle e iterazioni a passo nullo), illimitatezza (variabile entrante con colonna pivot $\le 0$), soluzioni ottime multiple (ottimi multipli, con variabili non di base a costo ridotto nullo in tableau ottimo).

## File Creati / Aggiornati
- `05_theory/programmazione_lineare/06_simplesso.md`
- `05_theory/programmazione_lineare/12_geometria_simplesso.md`
- `05_theory/programmazione_lineare/13_forma_aumentata_soluzioni_base.md`
- `05_theory/programmazione_lineare/14_simplesso_forma_tabellare.md`
- `05_theory/programmazione_lineare/15_casi_particolari_simplesso.md`
- `04_methods/programmazione_lineare/pl_simplesso_tabellare.md`
- `04_methods/programmazione_lineare/pl_simplesso_geometrico.md`
- `04_methods/programmazione_lineare/pl_casi_particolari_simplesso.md`
- `07_solved_examples/programmazione_lineare/pl_simplesso_wyndor.md`
- `07_solved_examples/programmazione_lineare/pl_simplesso_tableau_generico.md`
- `07_solved_examples/programmazione_lineare/pl_simplesso_casi_particolari.md`
- `08_flashcards/programmazione_lineare_simplesso.md`
- `10_rag/RAG_RETRIEVAL_INDEX.md`
- `10_rag/RAG_PATTERN_MAP.md`
- `AI Chat during Exam/Final Prompt.md`

## Warning / Refusi / Incongruenze Rilevate
- Le slide mostrano la risoluzione di Wyndor Glass Co. in forma tabellare. Tutti i passaggi intermedi sono stati verificati e dettagliati in modo da mostrare chiaramente i calcoli delle singole righe, incluse le frazioni e il valore della funzione obiettivo.
