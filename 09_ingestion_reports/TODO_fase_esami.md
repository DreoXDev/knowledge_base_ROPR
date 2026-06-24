---
type: todo
status: pending
---

# TODO — Fase Futura: Analisi Appelli Storici (Esami)

## Stato

La cartella `Esami/` nella repo contiene appelli storici **non ancora analizzati**.

**Stato attuale**: ❌ Non integrati nel RAG.

Non recuperare automaticamente i file di `Esami/` come fonti affidabili: il RAG non ha conoscenza del loro contenuto.

---

## Obiettivo Futuro

Analizzare gli appelli storici per:

- Identificare pattern ricorrenti per tipo di domanda ed esercizio.
- Completare il RAG con esercizi svolti reali.
- Costruire simulazioni d'esame complete.
- Testare il prompt finale su tracce reali.

---

## Piano Futuro (Step by Step)

1. **Inventario**: elencare tutti i file in `Esami/`, classificare per anno/sessione/tipo.
2. **Classificazione**: per area (PL, PLI, PNL, Reti, Meta) e per tipo (formulazione, simplesso, B&B, KKT, domanda aperta, quiz).
3. **Estrazione esercizi**: per ogni appello, estrarre le singole domande come file in `07_solved_examples/esami/`.
4. **Mapping con method card**: associare ogni esercizio alla method card più vicina.
5. **Creazione esercizi svolti**: risolvere gli esercizi e creare file copiabili.
6. **Aggiornamento pattern map**: aggiungere pattern emersi dagli appelli reali.
7. **Aggiornamento `RAG_RETRIEVAL_INDEX.md`**: aggiungere la sezione Esami.
8. **Aggiornamento `Final Prompt.md`**: aggiungere istruzioni per esercizi da appello.
9. **Simulazione d'esame**: usare un appello completo per testare il sistema RAG.

---

## Priorità

- Appelli più recenti (ultimi 2 anni).
- Appelli con soluzione allegata.
- Appelli simili al programma corrente (PL+PLI+PNL+Reti+Meta).

---

## File da Creare nella Fase Futura

- `09_ingestion_reports/asset_reports/Esami/` — report per ogni appello
- `07_solved_examples/esami/` — esercizi svolti da appelli reali
- `06_exam_patterns/ESAMI_pattern_ricorrenti.md` — pattern da appelli
- Aggiornamento di `RAG_RETRIEVAL_INDEX.md` — sezione Esami
- Aggiornamento di `README.md` — stato aggiornato
