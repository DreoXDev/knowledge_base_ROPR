# Knowledge Base ROPR

Repository per preparare l'esame di Ricerca Operativa e Pianificazione delle Risorse e usarla come base RAG durante studio, simulazioni ed esame.

## Scopo

Questa repo contiene:

- fonti originali in `raw_assets/`;
- inventario delle fonti;
- appunti teorici in formato Obsidian;
- catalogo esercizi;
- method card operative;
- esempi svolti;
- flashcard;
- prompt finale per chat AI durante l'esame;
- entrypoint RAG per impedire risposte inventate.

## Come usare la repo

Per studiare:

1. partire da `00_meta/STUDY_ROADMAP.md`;
2. consultare `05_theory/00_index.md`;
3. usare `04_methods/` per gli esercizi;
4. ripassare con `08_flashcards/`.

Per usare la repo come RAG:

1. aprire `10_rag/RAG_ENTRYPOINT.md`;
2. usare `10_rag/RAG_RETRIEVAL_INDEX.md`;
3. riconoscere il pattern con `10_rag/RAG_PATTERN_MAP.md`;
4. applicare la method card più vicina;
5. seguire `AI Chat during Exam/Final Prompt.md` per lo stile di risposta.

## Regola guida

Traccia d'esame -> RAG_ENTRYPOINT -> RAG_PATTERN_MAP -> method card -> esempio svolto -> risposta compatta da esame.

## Programmazione Lineare Intera (PLI)

Sono stati integrati i modelli PLI ufficiali, la modellazione logica e gli algoritmi di Branch and Bound (da `modelli_PLI.pdf`, `branch_and_bound.pdf`, `BB PLI.pdf`, `Programmazione Lineare Intera_Branch and Bound binario.pdf`, `16_esercizi_BB.pdf` e `Programmazione lineare intera completo.pdf`) completi di:
- Teoria, metodi e note Obsidian in [05_theory/programmazione_lineare_intera/](05_theory/programmazione_lineare_intera/) (incluso concetti logici, Big-M, espansione binaria e fallimento dell'arrotondamento);
- Procedure di modellazione e risoluzione (incluso Branch and Bound generico, binario, PLIM, interpretazione alberi, zaino greedy, e binarizzazione di interi) in [04_methods/programmazione_lineare_intera/](04_methods/programmazione_lineare_intera/);
- Esempi svolti copiabili (inclusi esercizi di modellazione come Lombardia Manufacturing Co., B&B e zaino greedy) in [07_solved_examples/programmazione_lineare_intera/](07_solved_examples/programmazione_lineare_intera/);
- Catalogo degli Esercizi strutturato e indicizzato per tipologia in [03_exercise_catalog/](03_exercise_catalog/);
- Topic Cards RAG in `10_rag/topic_cards/` e Method Cards RAG in [10_rag/method_cards/](10_rag/method_cards/);
- Flashcard dedicate in [08_flashcards/](08_flashcards/).

## Programmazione Non Lineare (PNL)

Sono stati integrati tutti gli asset ufficiali di PNL (introduzione, unidimensionale 1D, multivariabile 2D/nD, vincolata, KKT ed esercizi con soluzioni) completi di:
- Teoria, metodi e note Obsidian in [05_theory/programmazione_non_lineare/](05_theory/programmazione_non_lineare/) (incluso stazionarietà, convessità, Hessiana, moltiplicatori di Lagrange e condizioni KKT);
- Procedure di risoluzione numerica e analitica (incluso Bisezione, Newton 1D e nD, Gradiente con line search esatta, e combinatoria dei vincoli attivi) in [04_methods/programmazione_non_lineare/](04_methods/programmazione_non_lineare/);
- Esempi svolti copiabili (inclusi esercizi non vincolati e vincolati con KKT ed insiemi di livello) in [07_solved_examples/programmazione_non_lineare/](07_solved_examples/programmazione_non_lineare/);
- Topic Cards RAG in `10_rag/topic_cards/` e Method Cards RAG in [10_rag/method_cards/](10_rag/method_cards/);
- Flashcard dedicate in [08_flashcards/](08_flashcards/).

