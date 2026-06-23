# Ingestion Report — Riepilogo PL/PLI/PNL

## Metadata

- Source IDs:
  - `SRC-0091` (`raw_assets/Programmazione Non Lineare/esercizi_riepilogo.pdf`)
- Tipo file: PDF
- Categoria: Esercizi ufficiali di riepilogo
- Area ROPR: Riepilogo d'esame generale (PL, PLI, PNL)
- Affidabilità: Ufficiale (official)
- Stato analisi: Completato (consolidated)

## Sintesi Contenuto

Questo asset contiene 4 esercizi di riepilogo generale che simulano un intero compito d'esame scritto, coprendo tutte le aree del corso:
1.  **Esercizio 1 (Formulazione PL)**: Modellizzazione di un problema di trasporto con tre stabilimenti e quattro punti vendita, incluse modifiche del modello per gestire la capacità non utilizzata ed un vincolo di bilanciamento percentuale della distanza complessivamente coperta.
2.  **Esercizio 2 (Branch and Bound PLI)**: Risoluzione di un problema dello zaino binario (knapsack) a 5 variabili tramite Branch and Bound con strategia di visita in ampiezza (Breadth-First).
3.  **Esercizio 3 (PNL non vincolata)**: Esecuzione di una iterazione del metodo del gradiente con line search esatta a partire da un punto dato, ed una iterazione del metodo di Newton multivariabile dallo stesso punto. Verifica finale della natura dei punti trovati.
4.  **Esercizio 4 (PNL vincolata KKT)**: Minimizzazione di una distanza quadratica rispetto al punto $(0, 5)$ soggetta a due vincoli di disuguaglianza (una parabola $x^2-y \le 0$ ed un piano $x+y-2 \le 0$) tramite risoluzione del sistema KKT.

## Argomenti Estratti

- **Modello di trasporto PL**: Definizione variabili a doppio indice, vincoli di capacità (sorgente) e domanda (destinazione).
- **Linearizzazione di vincoli percentuali**: Formulazione algebrica lineare per limitare le distanze relative.
- **Branch and Bound in ampiezza**: Calcolo di bound tramite rilassamento continuo e ramificazione a livelli (ampiezza) dell'albero.
- **Gradiente con line search esatta**: Calcolo direzione di discesa, formulazione monodimensionale $\phi(\alpha)$ e ottimizzazione del passo $\alpha$.
- **Newton Multivariabile**: Calcolo della direzione di Newton risolvendo il sistema lineare $H_f d = -\nabla f$ e aggiornamento con passo unitario.
- **Sistema KKT per minimizzazione**: Risoluzione combinatoria dei casi attivi/inattivi per vincoli parabolici e lineari.

## File Creati / Aggiornati

- [riepilogo_pl_pli_pnl_esercizi_misti.md](../../07_solved_examples/riepilogo_pl_pli_pnl_esercizi_misti.md)
- [riepilogo_esame_pl_pli_pnl.md](../../06_exam_patterns/riepilogo_esame_pl_pli_pnl.md)
- [MC_PL_modello_trasporto.md](../../10_rag/method_cards/MC_PL_modello_trasporto.md)
- [MC_PLI_branch_and_bound_zaino.md](../../10_rag/method_cards/MC_PLI_branch_and_bound_zaino.md)
- [MC_Riepilogo_esame_misto_PL_PLI_PNL.md](../../10_rag/method_cards/MC_Riepilogo_esame_misto_PL_PLI_PNL.md)
- [TC_esercizi_riepilogo_PL_PLI_PNL.md](../../10_rag/topic_cards/TC_esercizi_riepilogo_PL_PLI_PNL.md)
- [riepilogo_pl_pli_pnl_flashcards.md](../../08_flashcards/riepilogo_pl_pli_pnl_flashcards.md)
- [Riepilogo_PL_PLI_PNL.csv](../../flashcards/Riepilogo_PL_PLI_PNL.csv)
