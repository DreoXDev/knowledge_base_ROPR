---
type: inventory
status: consolidated
generated: 2026-06-24
---

# Inventario Finale — knowledge_base_ROPR

> Prima fase stabile completata. Questo documento cataloga lo stato attuale della repo.

---

## Struttura Cartelle

```
knowledge_base_ROPR/
├── 00_meta/           ← metadati, policy, roadmap
├── 01_sources/        ← catalogo fonti
├── 02_transcriptions/ ← trascrizioni
├── 03_exercise_catalog/ ← catalogo esercizi per tipo
├── 04_methods/        ← procedure operative (pl/pli/pnl)
├── 05_theory/         ← note teoriche Obsidian
├── 06_exam_patterns/  ← pattern d'esame
├── 07_solved_examples/ ← esempi svolti
├── 08_flashcards/     ← flashcard
├── 09_ingestion_reports/ ← report di ingestione
├── 10_rag/            ← infrastruttura RAG
│   ├── method_cards/  ← 67 method card
│   └── topic_cards/   ← 35 topic card
├── AI Chat during Exam/ ← Final Prompt
├── AI Plans/          ← piani di lavoro Antigravity
├── flashcards/        ← CSV flashcards
├── notebooklm/
├── plans/
├── raw_assets/        ← PDF originali
├── scripts/           ← script di verifica
└── templates/
```

---

## Ingestion Reports (23 totali)

| ID | Asset | Area |
|---|---|---|
| 001 | Introduzione PL | PL |
| 002 | Lezione 3 completa | PL |
| 003 | Lec W4 (cammino, dualità) | PL |
| 004 | Metodo simplesso | PL |
| 005 | Teoria simplesso | PL |
| 006 | Teoria dualità | PL |
| 007 | Esercitazioni PL 1-2 | PL |
| 008 | Modelli PLI | PLI |
| 009 | Branch and Bound | PLI |
| 010 | BB PLI | PLI |
| 011 | Esercizi modelli BB | PLI |
| 012 | PLI completo | PLI |
| 013 | BB binario | PLI |
| 014 | PNL teoria unidim. + non vincolata | PNL |
| 015 | PNL vincolata/KKT | PNL |
| 016 | PNL esercizi e riepiloghi | PNL |
| 017 | PNL 1D | PNL |
| 018 | PNL vincolata 4 | PNL |
| 019 | PNL vincolata generale | PNL |
| 020 | 20 esercizi PNL | PNL |
| 021 | Esercizi riepilogo PL/PLI/PNL | Misto |
| 022 | AAA - Bibbia di RO | Non ufficiale |
| 023 | Domande aperte RO | Non ufficiale |

---

## Method Cards (67 totali)

| Area | Count |
|---|---|
| PL | 18 (PL_*, MC_PL_*, METHOD_PL_*) |
| PLI | 24 (MC_PLI_*) |
| PNL | 16 (MC_PNL_*) |
| RETI | 4 (MC_RETI_*) |
| METAEURISTICHE | 4 (MC_METAEURISTICHE_*, MC_Metaeuristiche_quiz) |
| TEORIA | 1 (MC_TEORIA_risposta_aperta) |
| **TOTALE** | **67** |

---

## Topic Cards (35 totali)

| Area | Count |
|---|---|
| PLI | 9 (TC_PLI_*) |
| PNL | 12 (TC_PNL_*) |
| Quiz | 6 (TC_quiz_*) |
| Domande aperte | 6 (TC_teoria_*, TC_domande_aperte_*) |
| Riepilogo | 2 |
| **TOTALE** | **35** |

---

## Flashcards (37 file MD + CSV)

Coprono: PL, PLI, PNL, metaeuristiche, domande aperte, riepilogo misto.

---

## Fonti Analizzate

| Area | Fonti Ufficiali | Asset Integrativi |
|---|---|---|
| PL | 7 PDF slide+esercitazioni | — |
| PLI | 6 PDF slide+esercitazioni | — |
| PNL | 9 PDF slide+esercizi | — |
| RETI | Integrato in PL/PLI | — |
| METAEURISTICHE | — (via Domande Aperte) | Domande Aperte RO, Bibbia RO |
| QUIZ/PATTERN | — | AAA Bibbia RO |
| TEORIA | — | Domande Aperte RO |

---

## Fonti NON Ancora Analizzate

- **Cartella `Esami/`**: appelli storici — non ancora integrati nel RAG.
  - Stato: **TODO — fase futura**
  - Non recuperare come fonte RAG affidabile.

---

## File Mancanti Rispetto al Piano

| File | Stato |
|---|---|
| `05_theory/ROPR_mappa_generale.md` | **Creato oggi** |
| `05_theory/RETI_index.md` | **Creato oggi** |
| `05_theory/METAEURISTICHE_index.md` | **Creato oggi** |
| `05_theory/DOMANDE_APERTE_index.md` | **Creato oggi** |
| `06_exam_patterns/*_pattern_esame_riassunto.md` (×6) | **Creati oggi** |
| `05_theory/Domande_aperte_risposte_modello.md` | **Creato oggi** |
| `09_ingestion_reports/TODO_fase_esami.md` | **Creato oggi** |
| Sezioni Reti/Meta in `RAG_RETRIEVAL_INDEX.md` | **Aggiornato oggi** |
| Sezioni Reti/Meta in `Final Prompt.md` | **Aggiornato oggi** |
| `README.md` aggiornato | **Aggiornato oggi** |

---

## Duplicati Sospetti

- `MC_PNL_gradiente_line_search.md` (774 B, quasi vuoto) vs `MC_PNL_gradiente_line_search_esatta.md` (2361 B) — **non eliminare**, verificare contenuto.
- `MC_PNL_kkt.md` (1219 B) vs `MC_PNL_KKT_generale.md` (3123 B) — **non eliminare**, la più piccola è uno stub.
- `MC_PNL_newton.md` (720 B) vs `MC_PNL_newton_non_vincolata.md` (2263 B) — **non eliminare**, stub.
- `PL_minimum_cost_flow.md` vs `MC_RETI_flusso_costo_minimo.md` — coprono angoli diversi (PLI vs teoria aperta).

---

## Stato Complessivo

- **Prima fase**: ✅ Completata
- **PL, PLI, PNL**: ✅ Copertura completa con slide ufficiali
- **Reti**: ✅ Integrato via PL/PLI + Domande Aperte
- **Metaeuristiche**: ✅ Integrato via Domande Aperte + Bibbia RO
- **Domande Aperte**: ✅ Integrato (con riscrittura professionale)
- **Quiz**: ✅ Integrato (con anti-allucinazione attivata)
- **Esami storici**: ❌ Non ancora analizzati
