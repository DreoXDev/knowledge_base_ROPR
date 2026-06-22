# Ingestion Report — Esercitazioni PL 1 e 2

## Metadata

- Source ID: `SRC-0080`, `SRC-0081`
- Paths:
  - `raw_assets/Programmazione Lineare/esercitazione1_complete.pdf`
  - `raw_assets/Programmazione Lineare/Esercitazione 2 PL.pdf`
- Tipo file: PDF
- Categoria: Esercitazioni ufficiali
- Area ROPR: Programmazione Lineare e Programmazione Lineare Intera
- Affidabilità: Ufficiale (official)
- Stato analisi: Completato (consolidated)

## Sintesi Contenuto
Il documento descrive l'ingestione congiunta delle esercitazioni ufficiali 1 e 2. Gli argomenti modellistici principali coperti comprendono:
1. **Pianificazione della produzione**: Il modello TOOL.spa con vincoli di risorse (acciaio, ore lavorazione, ore assemblaggio) e limiti di domanda.
2. **Problema della dieta**: Minimizzazione dei costi con vincoli nutrizionali minimi ($\ge$).
3. **Problemi di trasporto (distribuzione)**: Modello Bell Computers per la spedizione ottimale di personal computer da stabilimenti a magazzini.
4. **Problemi di miscelazione (blending)**: Miscelazione di benzine con requisiti qualitativi (numero di ottani e pressione del vapore) espressi come medie pesate e linearizzati.
5. **Localizzazione ripetitori (copertura)**: Modelli CALL.spa per Set Covering (copertura totale a costo minimo) e Maximum Coverage (massima utilità con limitazione di risorse e prevenzione del doppio conteggio tramite variabili $y_j$).
6. **Risoluzione grafica**: Esercizio numerico completo a due variabili decisionali.

## Argomenti Estratti
- **Linearizzazione vincoli di qualità**: Moltiplicazione per la quantità totale prodotta per linearizzare le medie pesate.
- **Set Covering**: Modello $\min \sum x_i$ s.t. $\sum a_{ji} x_i \ge 1$, $x_i \in \{0, 1\}$.
- **Maximum Coverage**: Modello $\max \sum u_j y_j$ s.t. $\sum x_i \le k$ e $y_j \le \sum a_{ji} x_i$, $x_i, y_j \in \{0, 1\}$.
- **Doppio conteggio**: Spiegazione dell'utilità di $y_j$ binarie per contare la popolazione una sola volta.
- **Risoluzione Grafica**: Disegno delle linee di livello e scorrimento lungo il vettore gradiente $\nabla Z$.

## File Creati / Aggiornati

### Note Teoriche e Method Cards
- `05_theory/programmazione_lineare/08_formulazione_modelli_pl.md` (Aggiornato)
- `04_methods/programmazione_lineare/pl_formulare_modello_pl_da_testo.md` (Creato)
- `04_methods/programmazione_lineare/pl_soluzione_grafica.md` (Creato)
- `04_methods/programmazione_lineare_intera/pl_set_covering_e_maximum_coverage.md` (Creato)
- `04_methods/programmazione_lineare/pl_problemi_di_miscelazione.md` (Creato)
- `04_methods/programmazione_lineare/pl_problemi_di_trasporto.md` (Creato)

### Esempi Svolti
- `07_solved_examples/programmazione_lineare/produzione_tool_spa.md` (Creato)
- `07_solved_examples/programmazione_lineare/problema_dieta.md` (Creato)
- `07_solved_examples/programmazione_lineare/reti_distribuzione_bell_computers.md` (Creato)
- `07_solved_examples/programmazione_lineare/miscelazione_benzine.md` (Creato)
- `07_solved_examples/programmazione_lineare_intera/call_spa_ripetitori.md` (Creato)

### Flashcard & Prompt
- `08_flashcards/programmazione_lineare_formulazione.md` (Aggiornato)
- `08_flashcards/set_covering_maximum_coverage_flashcards.md` (Creato)
- `AI Chat during Exam/Final Prompt.md` (Aggiornato)

### RAG & Metadata
- `10_rag/RAG_SOURCE_PRIORITY.md` (Creato)
- `10_rag/RAG_RETRIEVAL_INDEX.md` (Aggiornato)
- `10_rag/RAG_PATTERN_MAP.md` (Aggiornato)
- `00_meta/ASSET_TRACKING.md` (Aggiornato)
- `AI Plans/checklist_asset_ropr_obsidian.md` (Aggiornato)

## Warning / Refusi / Incongruenze Rilevate
- **LabPython1**: L'asset `raw_assets/Programmazione Lineare/Lab-Python 1.pdf` è stato marcato come differito a causa del suo focus sull'implementazione pratica in Python, secondario rispetto ai requisiti d'esame scritto.
