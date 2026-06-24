---
type: index
topic: metaeuristiche
status: consolidated
---

# METAEURISTICHE — Indice Area

Algoritmi genetici, Simulated Annealing, Tabu Search.

> Contenuto integrato dall'asset `Domande aperte RO.pdf` (non ufficiale, riscritto e validato).

## Note Teoriche

- [[Metaeuristiche_domande_aperte]] — AG, SA, Tabu Search (risposte modello da esame)

## Method Cards

- [[10_rag/method_cards/MC_METAEURISTICHE_algoritmi_genetici]] — Algoritmi genetici
- [[10_rag/method_cards/MC_METAEURISTICHE_simulated_annealing]] — Simulated Annealing
- [[10_rag/method_cards/MC_METAEURISTICHE_tabu_search]] — Tabu Search
- [[10_rag/method_cards/MC_Metaeuristiche_quiz]] — Quiz sulle metaeuristiche

## Flashcards

- [[08_flashcards/Domande_aperte_metaeuristiche_flashcards]]
- [[08_flashcards/Quiz_metaeuristiche_flashcards]]
- CSV: [[flashcards/Domande_aperte_metaeuristiche.csv]]

## Pattern d'Esame

- [[06_exam_patterns/METAEURISTICHE_pattern_esame_riassunto]]
- [[06_exam_patterns/Domande_aperte_metaeuristiche]]
- [[06_exam_patterns/Quiz_metaeuristiche]]

## Topic Cards RAG

- [[10_rag/topic_cards/TC_teoria_metaeuristiche]]
- [[10_rag/topic_cards/TC_quiz_metaeuristiche]]

## Fonti

- `raw_assets/Domande aperte RO.pdf` (non ufficiale — riscritto)
- `raw_assets/AAA - La bibbia di RO.pdf` (non ufficiale — solo pattern quiz)

## Stato

Prima fase completa (via fonti non ufficiali).
Affidabilità: media — validare con slide ufficiali se disponibili.
Mancano: slide ufficiali del corso sulle metaeuristiche (se esistono).

## Errori da Ricordare

- Non confondere crossover (combina) e mutazione (modifica).
- Formula SA: $p = \exp(-\Delta f/T)$ per min, $p = \exp(\Delta f/T)$ per max.
- Il criterio di aspirazione in Tabu Search ignora il tabu se migliora il best globale.
- Nessuna metaeuristica garantisce l'ottimo globale in generale.
