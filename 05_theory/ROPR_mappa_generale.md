---
type: index
topic: riepilogo_generale
status: consolidated
---

# ROPR — Mappa Generale della Knowledge Base

> Navigazione principale per studio e chat d'esame.

## ⚠️ Avvertenza

Questa repo è in **prima fase stabile**. Le fonti ufficiali su PL, PLI e PNL sono state analizzate. Gli appelli storici nella cartella `Esami` **non sono ancora stati integrati**: il RAG non deve considerarli coperti.
Gli asset non ufficiali (Bibbia RO, Domande Aperte RO) sono usati solo per pattern, domande ricorrenti e pratica.

---

## Aree Principali

| Area | Stato | Indice |
|---|---|---|
| Programmazione Lineare (PL) | ✅ Prima fase completa | [[05_theory/programmazione_lineare/]] |
| Programmazione Lineare Intera (PLI) | ✅ Prima fase completa | [[05_theory/programmazione_lineare_intera/00_index]] |
| Programmazione Non Lineare (PNL) | ✅ Prima fase completa | [[05_theory/programmazione_non_lineare/00_index]] |
| Reti e Flussi | ✅ Integrato | [[RETI_index]] |
| Metaeuristiche | ✅ Integrato | [[METAEURISTICHE_index]] |
| Domande Aperte | ✅ Integrato | [[DOMANDE_APERTE_index]] |
| Esami Storici | ❌ TODO | [[09_ingestion_reports/TODO_fase_esami]] |

---

## Come Studiare

1. Parti da questa mappa → scegli l'area.
2. Consulta l'**indice di area** per vedere le note teoriche.
3. Usa le **flashcard** in `08_flashcards/` per il ripasso attivo.
4. Usa i **pattern d'esame** in `06_exam_patterns/` per riconoscere il tipo di esercizio.
5. Consulta gli **esempi svolti** in `07_solved_examples/` per confronto.

---

## Come Usare la Repo per Esercizi (Studio)

1. Riconosci il tipo di esercizio dalla traccia.
2. Apri il **riepilogo pattern** dell'area (es. `PL_pattern_esame_riassunto.md`).
3. Segui la **method card** indicata.
4. Confronta con un **esempio svolto** simile.

---

## Come Usare la Repo per la Chat d'Esame

1. Apri `AI Chat during Exam/Final Prompt.md`.
2. Incollalo come system prompt nella chat AI.
3. La repo funge da RAG: l'AI consulterà `10_rag/RAG_RETRIEVAL_INDEX.md` e `10_rag/RAG_PATTERN_MAP.md`.
4. Invia la foto/testo della traccia e ricevi la risposta in stile esame.

---

## Struttura Cartelle

```
04_methods/       ← procedure operative
05_theory/        ← note teoriche
06_exam_patterns/ ← pattern d'esame + riassunti
07_solved_examples/ ← esempi svolti copiabili
08_flashcards/    ← ripasso attivo
10_rag/           ← infrastruttura RAG (67 MC + 35 TC)
AI Chat during Exam/ ← Final Prompt
```

---

## Stato di Completamento

```
PL:  ████████████ 100% (fonti ufficiali)
PLI: ████████████ 100% (fonti ufficiali)
PNL: ████████████ 100% (fonti ufficiali)
RETI:     ████████ 80% (integrato via PL/PLI + domande aperte)
META:     ████████ 80% (integrato via domande aperte + bibbia)
ESAMI:   ░░░░░░░░   0% (TODO - prossima fase)
```

Mancano: appelli storici nella cartella `Esami/`.
