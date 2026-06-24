# Knowledge Base ROPR

Repository per preparare l'esame di Ricerca Operativa e Pianificazione delle Risorse e usarla come base RAG durante studio, simulazioni ed esame.

## Obiettivo

Questa repo contiene fonti ufficiali, appunti teorici validati, method card operative, esempi svolti, flashcard e un prompt finale per la chat AI durante l'esame.

## Struttura della Repo

```
00_meta/              ← metadati, policy affidabilità, roadmap
01_sources/           ← catalogo fonti
02_transcriptions/    ← trascrizioni
03_exercise_catalog/  ← catalogo esercizi per tipologia
04_methods/           ← procedure operative (pl/ pli/ pnl/)
05_theory/            ← note teoriche Obsidian
06_exam_patterns/     ← pattern d'esame + riassunti per area
07_solved_examples/   ← esempi svolti copiabili (pl/ pli/ pnl/)
08_flashcards/        ← flashcard per ripasso attivo
09_ingestion_reports/ ← report di ingestione e TODO
10_rag/               ← infrastruttura RAG
  method_cards/       ← 67 method card operative
  topic_cards/        ← 35 topic card
AI Chat during Exam/  ← Final Prompt per la chat d'esame
AI Plans/             ← piani di lavoro Antigravity
flashcards/           ← CSV flashcards
raw_assets/           ← PDF originali
scripts/              ← script di verifica
```

## Stato Attuale (Prima Fase Stabile)

| Area | Stato | Note |
|---|---|---|
| Programmazione Lineare | ✅ Completa | Slide ufficiali + esercitazioni |
| Programmazione Lineare Intera | ✅ Completa | Slide ufficiali + esercitazioni |
| Programmazione Non Lineare | ✅ Completa | Slide ufficiali + esercizi |
| Reti e Flussi | ✅ Integrata | Via PL/PLI + domande aperte |
| Metaeuristiche | ✅ Integrata | Via domande aperte + Bibbia RO |
| Domande Aperte teoriche | ✅ Integrata | Riscritte e validate |
| Quiz a risposta multipla | ✅ Integrata | Anti-allucinazione attivata |
| **Esami Storici** | ❌ **TODO** | Non ancora analizzati |

## Aree Coperte

### Programmazione Lineare

- Formulazione modelli PL.
- Soluzione grafica.
- Simplesso tabellare (forma aumentata, pivot, casi particolari).
- Metodo delle due fasi.
- Dualità forte/debole, complementary slackness, prezzi ombra.
- Analisi di sensitività dal tableau.
- Teoria del simplesso (vertici, soluzioni di base, geometria).
- Reti di distribuzione, cammino minimo.
- Miscelazione, trasporto, workforce scheduling.

Theory: `05_theory/programmazione_lineare/`
Methods: `04_methods/programmazione_lineare/`
Examples: `07_solved_examples/programmazione_lineare/`
Pattern: `06_exam_patterns/PL_pattern_esame_riassunto.md`

### Programmazione Lineare Intera

- Modellazione con variabili binarie.
- Vincoli logici, Big-M, binarizzazione di interi.
- Set covering, maximum coverage.
- Facility location, produzione/stoccaggio, zaino, assegnamento.
- Branch and Bound (generico, binario, zaino greedy, PLIM, interpretazione albero).
- Totale unimodularità.

Theory: `05_theory/programmazione_lineare_intera/`
Methods: `04_methods/programmazione_lineare_intera/`
Examples: `07_solved_examples/programmazione_lineare_intera/`
Pattern: `06_exam_patterns/PLI_pattern_esame_riassunto.md`

### Programmazione Non Lineare

- Non vincolata: stazionarietà, Hessiana, classificazione locale.
- Numerica: bisezione, gradiente con line search esatta, Newton 1D e nD.
- Vincolata: Lagrange (uguaglianze), riduzione variabili, KKT (disuguaglianze).
- Complementarità e combinatoria dei vincoli attivi.

Theory: `05_theory/programmazione_non_lineare/`
Methods: `04_methods/programmazione_non_lineare/`
Examples: `07_solved_examples/programmazione_non_lineare/`
Pattern: `06_exam_patterns/PNL_pattern_esame_riassunto.md`

### Reti e Flussi

- Trasporto e transhipment.
- Flusso a costo minimo.
- Massimo flusso.
- Cammino di costo minimo.

Index: `05_theory/RETI_index.md`
Pattern: `06_exam_patterns/RETI_pattern_esame_riassunto.md`

### Metaeuristiche

- Algoritmi genetici (crossover, mutazione, fitness, selezione).
- Simulated Annealing (temperatura, exploration/exploitation).
- Tabu Search (tabu list, criterio di aspirazione).
- Criteri di arresto; nessuna garanzia di ottimo globale.

Index: `05_theory/METAEURISTICHE_index.md`
Pattern: `06_exam_patterns/METAEURISTICHE_pattern_esame_riassunto.md`

### Domande Aperte

- 19 domande teoriche riscritte e validate (PL, Reti, PNL, Metaeuristiche).
- Risposte modello sintetiche.
- Pattern risposta strutturata.

Index: `05_theory/DOMANDE_APERTE_index.md`
Catalogo: `05_theory/Domande_aperte_RO_catalogo.md`
Risposte: `05_theory/Domande_aperte_risposte_modello.md`

## Fonti Analizzate

| Fonte | Tipo | Affidabilità |
|---|---|---|
| Slide ufficiali PL (7 PDF) | Ufficiale | Alta |
| Slide ufficiali PLI (6 PDF) | Ufficiale | Alta |
| Slide ufficiali PNL (9 PDF) | Ufficiale | Alta |
| Esercitazioni PL 1-2 | Ufficiale | Alta |
| 20 esercizi PNL | Ufficiale | Alta |
| Esercizi riepilogo PL/PLI/PNL | Ufficiale | Alta |
| AAA - La Bibbia di RO.pdf | Non ufficiale | Bassa (solo pattern quiz) |
| Domande aperte RO.pdf | Non ufficiale | Media (riscritto/validato) |

## Fonti NON Ancora Analizzate

- **Cartella `Esami/`**: appelli storici non integrati nel RAG.
- Stato: **TODO — prossima fase**.
- Non usare come fonti affidabili nella chat d'esame.

Vedere: `09_ingestion_reports/TODO_fase_esami.md`

## Come Studiare

1. Apri `05_theory/ROPR_mappa_generale.md`.
2. Scegli l'area → apri l'indice di area.
3. Consulta le note teoriche + method card.
4. Ripassa con le flashcard in `08_flashcards/`.
5. Pratica con gli esempi svolti in `07_solved_examples/`.

## Come Usare il RAG

1. Apri `10_rag/RAG_ENTRYPOINT.md`.
2. Riconosci il pattern con `10_rag/RAG_PATTERN_MAP.md`.
3. Scegli il file con `10_rag/RAG_RETRIEVAL_INDEX.md`.
4. Applica la method card in `10_rag/method_cards/`.

Regola: traccia → pattern → method card → esempio → risposta.

## Come Usare la Chat d'Esame

1. Apri `AI Chat during Exam/Final Prompt.md`.
2. Incollalo come system prompt nella chat AI.
3. Invia la foto/testo della traccia.
4. L'AI risponde in stile esame, usando questa repo come RAG.

## Prossima Fase: Esami

La cartella `Esami/` contiene appelli storici non ancora analizzati.
Per ora non sono stati integrati nel RAG.
La fase successiva dovrà creare:
- catalogo degli appelli;
- pattern ricorrenti da appelli reali;
- esercizi svolti da appelli;
- simulazioni d'esame complete;
- aggiornamento del prompt finale.

Vedere il piano in: `09_ingestion_reports/TODO_fase_esami.md`

## Convenzioni

- **Markdown**: file `.md`, nomi in snake_case o PascalCase.
- **LaTeX**: inline `$...$`, blocco `$$...$$`.
- **Affidabilità**: indicata nel frontmatter YAML di ogni file (`reliability: alta|media|non-ufficiale`).
- **Fonti non ufficiali**: marcate con avvertenza, non usare per teoria primaria senza validazione.

## Avvertenza

Questa repo è in prima fase stabile. Gli asset non ufficiali (Bibbia RO, Domande Aperte RO) sono usati solo per pattern, domande ricorrenti e pratica, non come fonte teorica primaria. Gli appelli storici nella cartella `Esami/` non sono ancora stati integrati nel RAG.
