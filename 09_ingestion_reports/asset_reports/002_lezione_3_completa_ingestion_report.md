# Ingestion Report — Lezione 3 Completa

## Metadata

- Source ID: `SRC-0005` (dal SOURCE_INVENTORY.md)
- Path: `raw_assets/Programmazione Lineare/lezione 3 completa.pdf`
- Tipo file: PDF
- Categoria: Slide / Esercitazione ufficiale docente
- Area ROPR: Programmazione Lineare
- Affidabilità: Ufficiale (official)
- Stato analisi: Completato (consolidated)

## Sintesi Contenuto
Le slide introducono la formulazione di problemi reali tramite PL (es. scheduling turni di lavoro), e definiscono l'algoritmo del simplesso in forma tabellare (tableau), inclusi il metodo delle due fasi e la gestione di variabili libere o con segno negativo.

## Argomenti Estratti
- **Formulazione**: Esercizio turni di lavoro (workforce scheduling) su calendario ciclico di 5 giorni consecutivi lavorativi su 7.
- **Simplesso Tabellare**: Slack, riga 0, tableau, pivot, test rapporti minimi, ottimo, illimitatezza.
- **Metodo due fasi**: surplus, artificiali, Fase 1, Fase 2.
- **Variabili non standard**: variabili libere e variabili non positive.
- **Casi di arresto**: inammissibilità (Fase 1 con $W^* > 0$) e illimitatezza.

## File Creati / Aggiornati
- `05_theory/programmazione_lineare/06_simplesso.md`
- `05_theory/programmazione_lineare/07_metodo_due_fasi.md`
- `05_theory/programmazione_lineare/08_formulazione_modelli_pl.md`
- `04_methods/programmazione_lineare/pl_formulazione_modelli.md`
- `04_methods/programmazione_lineare/pl_simplesso_tabellare.md`
- `04_methods/programmazione_lineare/pl_metodo_due_fasi.md`
- `04_methods/programmazione_lineare/pl_variabili_libere_e_segno.md`
- `07_solved_examples/programmazione_lineare/pl_turni_lavoro_formulazione.md`
- `07_solved_examples/programmazione_lineare/pl_simplesso_esempio_40_50.md`
- `07_solved_examples/programmazione_lineare/pl_tool_spa_simplesso.md`
- `07_solved_examples/programmazione_lineare/pl_simplesso_max_3x_5y.md`
- `07_solved_examples/programmazione_lineare/pl_due_fasi_esempio_base.md`
- `07_solved_examples/programmazione_lineare/pl_due_fasi_problema_illimitato.md`
- `07_solved_examples/programmazione_lineare/pl_due_fasi_problema_non_ammissibile.md`
- `08_flashcards/programmazione_lineare_simplesso.md`
- `08_flashcards/programmazione_lineare_due_fasi.md`
- `08_flashcards/programmazione_lineare_formulazione.md`
- `10_rag/RAG_RETRIEVAL_INDEX.md`
- `10_rag/RAG_PATTERN_MAP.md`
- `AI Chat during Exam/Final Prompt.md`

## Warning / Refusi / Incongruenze Rilevate
- **Turni di lavoro**: L'ultimo vincolo del modello sulle slide presenta un refuso nel testo (mostra la richiesta pari a 16 riferita di nuovo a mercoledì). Nella KB abbiamo ripristinato il corretto vincolo per Giovedì.
- **Due Fasi (Esempio Base)**: Nelle slide appare in grassetto il valore $Z = -53/12$, ma il calcolo corretto sui valori ottimi delle variabili fornisce $Z = -55/12$. Abbiamo contrassegnato questo esempio come `da_verificare` per allertare lo studente.
- **Tool.Spa**: La progressione dei tableau del simplesso non è del tutto esplicita ed è stata ricostruita analiticamente per intero in `pl_tool_spa_simplesso.md`, impostando lo stato su `da_verificare`.
