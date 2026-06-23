# RAG Source Priority

Questo file cataloga le priorità dei singoli asset e file sorgente per il retrieval.

## Fonti Ufficiali Alta Priorità per Esercizi di Formulazione

- `raw_assets/Programmazione Lineare/esercitazione1_complete.pdf`
  - priorità: alta
  - ruolo: esempi ufficiali di formulazione PL
  - pattern: produzione, dieta, trasporto

- `raw_assets/Programmazione Lineare/Esercitazione 2 PL.pdf`
  - priorità: alta
  - ruolo: esempi ufficiali di formulazione PL/PLI
  - pattern: miscelazione, set covering, maximum coverage, grafica PL

- `raw_assets/Programmazione Lineare Intera/modelli_PLI.pdf`
  - priorità: alta
  - ruolo: modelli ufficiali di programmazione lineare intera e su grafi
  - pattern: assegnamento, cammino minimo, flusso costo minimo, vincoli logici, produzione e stoccaggio, facility location, zaino

- `raw_assets/Programmazione Lineare Intera/branch_and_bound.pdf`
  - priorità: alta
  - ruolo: teoria e algoritmi di Branch and Bound
  - pattern: branch and bound, potatura, branching, visita albero

- `raw_assets/Programmazione Lineare Intera/BB PLI.pdf`
  - priorità: alta
  - ruolo: approfondimenti Branch and Bound e Programmazione Lineare Intera Mista (PLIM)
  - pattern: branching, bounding, fathoming, depth-first, best-bound, PLIM, interpretazione albero B&B, gap ottimalità, rilassamento lagrangiano

- `raw_assets/Programmazione Lineare Intera/Programmazione Lineare Intera_Branch and Bound binario.pdf`
  - priorità: alta
  - ruolo: Branch and Bound binario
  - pattern: variabili binarie, branching binario, branching variabile 0-1, branch and bound binario, arrotondamento bound, Lombardia Manufacturing

- `raw_assets/Programmazione Lineare Intera/16_esercizi_BB.pdf`
  - priorità: alta
  - ruolo: esercizi ufficiali svolti con Branch and Bound e zaino greedy
  - pattern: risoluzione branch and bound, calcolo bound, euristica greedy zaino

- `raw_assets/Programmazione Lineare Intera/Programmazione lineare intera completo.pdf`
  - priorità: alta
  - ruolo: teoria e formulazione di modelli a variabili binarie/intere, vincoli logici e contro-esempi di arrotondamento
  - pattern: variabili binarie, contingenza, either-or, K su N, binarizzazione, costo fisso, fallimento arrotondamento

- `raw_assets/Programmazione Non Lineare/PNL_non_vincolata.pdf`
  - priorità: alta
  - ruolo: esercizi ufficiali svolti di ottimizzazione non vincolata (gradiente, Newton, classificazione stazionarietà, selle)
  - pattern: punti stazionari, Hessiana, sella, convessità globale, gradiente, line search esatta, Newton multivariabile, funzioni quadratiche

- `raw_assets/Programmazione Non Lineare/PNL_vincolata.pdf`
  - priorità: alta
  - ruolo: esercizi ufficiali svolti di ottimizzazione vincolata KKT (uguaglianze, disuguaglianze lineari e non lineari)
  - pattern: KKT vincolo uguaglianza, Lagrangiana, KKT vincoli disuguaglianza, complementarità, combinatoria vincoli attivi, segno moltiplicatori min/max, insiemi di livello, regioni non limitate

- `raw_assets/Programmazione Non Lineare/20_esercizi_pnl.pdf`
  - priorità: alta
  - ruolo: raccolta di 20 esercizi svolti di PNL sia non vincolata (stazionarietà) sia vincolata (KKT)
  - pattern: punti stazionari locali, KKT minimo/massimo globale su ellissi, parabole, semispazi

- `raw_assets/Programmazione Non Lineare/esercizi_riepilogo.pdf`
  - priorità: alta
  - ruolo: prove pratiche e riepiloghi di esame generale (PL, PLI, PNL)
  - pattern: modello di trasporto PL, zaino Branch and Bound in ampiezza, gradiente line search, Newton multivariabile, KKT vincolata per casi


- `raw_assets/Programmazione Non Lineare/PNL Vincolata 4.pdf`
  - priorità: alta
  - ruolo: esempio ufficiale svolto di ottimizzazione vincolata KKT ed enumerazione dei vincoli attivi
  - pattern: KKT vincoli disuguaglianza, Lagrangiana con 3 disuguaglianze, complementarità degli scarti, segno dei moltiplicatori, scarto candidati per ammissibilità e moltiplicatori

- `raw_assets/Programmazione Non Lineare/Ottimizzazione non lineare vincolata.pdf`
  - priorità: alta
  - ruolo: teoria e metodi per ottimizzazione vincolata generale
  - pattern: riduzione variabili libere, moltiplicatori di Lagrange, condizioni KKT, LICQ, vincoli attivi e inattivi, complementarità scarti, curve di livello, interpretazione geometrica moltiplicatori

---

## Fonti Non Ufficiali / Visuali (bassa priorità teorica)

- `raw_assets/AAA - La bibbia di RO.pdf`
  - priorità: **alta per pattern di quiz**, media per esercizi pratici, **bassa per teoria**
  - ruolo: raccolta di screenshot di quiz a risposta multipla su PL (primale/duale, sensitività, simplesso), PLI (B&B), PNL (bisezione, gradiente, Newton, KKT), metaeuristiche
  - affidabilità: **non ufficiale** — composto quasi interamente da immagini, nessuna estrazione OCR affidabile
  - avvertenza: Le crocette/annotazioni presenti nelle immagini vanno **ignorate** — ricalcolare sempre. Non usare come fonte teorica primaria senza validazione con slide ufficiali.
  - pattern: quiz primale/duale, analisi sensitività da tableau, casi particolari simplesso, B&B lettura albero, bisezione, gradiente, Newton, KKT, metaeuristiche
  - file collegati:
    - `09_ingestion_reports/asset_reports/022_aaa_bibbia_ro_ingestion_report.md`
    - `07_solved_examples/AAA_bibbia_RO_catalogo_visuale.md`
    - `06_exam_patterns/Quiz_PL_primale_duale.md`
    - `06_exam_patterns/Quiz_PL_analisi_sensitivita.md`
    - `06_exam_patterns/Quiz_simplesso_casi_particolari.md`
    - `06_exam_patterns/Quiz_PLI_Branch_and_Bound.md`
    - `06_exam_patterns/Quiz_PNL_bisezione_gradiente_newton_KKT.md`
    - `06_exam_patterns/Quiz_metaeuristiche.md`

- `raw_assets/Domande aperte RO.pdf`
  - priorità: **alta per lista di domande probabili d'esame**, media per bozze di risposta, **bassa per formule/teoria** se non validate
  - ruolo: raccolta di 19 domande aperte teoriche con bozze di risposta su PL (vertici, basi, dualità, simplesso, complementarità), Reti (trasporto, transhipment, flusso, max flusso, cammino minimo), PNL (KKT), Metaeuristiche (AG, SA, Tabu Search)
  - affidabilità: **non ufficiale** — bozze informali, alcune formule da verificare
  - avvertenza: Le risposte sono state riscritte e validate. Non copiare dal PDF originale senza riscrittura professionale.
  - regola: Usare le note teoriche e method card create come fonte definitiva; il PDF solo come lista di domande.
  - pattern: domanda aperta teoria, formulazione trasporto/flussi/reti, dualità forte/debole, complementarità, simplesso direzione/incremento, KKT necessità/sufficienza, AG crossover/mutazione, SA temperatura/exploration, TS tabu list/aspirazione
  - file collegati:
    - `09_ingestion_reports/asset_reports/023_domande_aperte_ro_ingestion_report.md`
    - `05_theory/Domande_aperte_RO_catalogo.md`
    - `05_theory/PL_domande_aperte_vertici_basi_dualita.md`
    - `05_theory/Reti_domande_aperte_trasporto_flussi.md`
    - `05_theory/PNL_domande_aperte_KKT.md`
    - `05_theory/Metaeuristiche_domande_aperte.md`
    - `10_rag/method_cards/MC_TEORIA_risposta_aperta.md`









