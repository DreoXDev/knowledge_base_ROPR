# Ingestion Report — Lezione Week 4 Completa

## Metadata

- Source ID: `SRC-0074` (dal SOURCE_INVENTORY.md)
- Path: `raw_assets/Programmazione Lineare/lec_w4_completa.pdf`
- Tipo file: PDF
- Categoria: Slide / Esercitazione ufficiale docente
- Area ROPR: Programmazione Lineare
- Affidabilità: Ufficiale (official)
- Stato analisi: Completato (consolidated)

## Sintesi Contenuto
Le slide introducono la formulazione del problema di cammino minimo come modello di programmazione lineare su grafo orientato pesato con vincoli di conservazione del flusso. Inoltre, introducono formalmente il concetto di dualità nella programmazione lineare (con interpretazione economica basata su prezzi unitari/ombra), la costruzione sistematica del problema duale a partire dal primale (con regole di transizione per MAX-MIN e MIN-MAX, vincoli/variabili canonici, anticanonici e liberi), e la lettura delle variabili duali ottime dalla riga della funzione obiettivo (in corrispondenza delle variabili di slack) nel tableau ottimo del simplesso.

## Argomenti Estratti
- **Cammino Minimo su Grafo**: Formulazione matematica come modello di PL con variabili decisionali binarie, funzione obiettivo di minimizzazione dei costi totali, vincoli di conservazione del flusso per nodi intermedi, origine ($+1$) e destinazione ($-1$).
- **Dualità Intuizione Economica**: Problema di massimizzazione del profitto vs minimizzazione del costo delle risorse (prezzi ombra).
- **Costruzione del Duale**: Regole di corrispondenza primale-duale (MAX/MIN, variabili/vincoli, RHS/coefficienti f.o., matrice trasposta).
- **Casi Generali/Misti**: Gestione di vincoli misti ($\le, \ge, =$) e variabili canoniche/anticanoniche/libere.
- **Variabili Duali dal Tableau**: Lettura dei valori ottimi delle variabili duali dal tableau ottimo (coefficienti delle slack).

## File Creati / Aggiornati
- `05_theory/programmazione_lineare/09_cammino_minimo_dualita.md`
- `05_theory/programmazione_lineare/10_dualita.md`
- `05_theory/programmazione_lineare/11_regole_costruire_duale.md`
- `07_solved_examples/programmazione_lineare/pl_cammino_minimo_formulazione.md`
- `07_solved_examples/programmazione_lineare/pl_tool_spa_duale.md`
- `07_solved_examples/programmazione_lineare/pl_duale_vincoli_misti.md`
- `08_flashcards/programmazione_lineare_cammino_minimo_dualita.md`
- `10_rag/method_cards/METHOD_PL_CAMMINO_MINIMO.md`
- `10_rag/method_cards/METHOD_PL_DUALE.md`
- `10_rag/RAG_RETRIEVAL_INDEX.md`
- `10_rag/RAG_PATTERN_MAP.md`
- `AI Chat during Exam/Final Prompt.md`

## Warning / Refusi / Incongruenze Rilevate
- Nessun refuso critico rilevato nelle slide originali. Le convenzioni di segno per le variabili duali e la trasposizione della matrice dei coefficienti sono state mappate e formalizzate in modo rigoroso per l'utilizzo all'esame.
