---
type: index
topic: programmazione_lineare_intera
status: active
sources: [9_esercizi_modelli.pdf, 16_esercizi_BB.pdf]
reliability: official
---

# Indice Generale degli Esercizi

Indice complessivo degli esercizi di Programmazione Lineare, Lineare Intera (PLI) e Non Lineare (PNL) estratti dai fogli ufficiali.

## Esercizi di Modellazione (`9_esercizi_modelli.pdf`)

*   [Esercizio 1: Rimpiazzo Fotocopiatrici](by_topic/pli_modellazione_esercizi.md#esercizio-1): Formulazione come problema di cammino minimo su grafo.
*   [Esercizio 2: Smistamento Automobili](by_topic/pli_modellazione_esercizi.md#esercizio-2): Assegnamento porti-centri con vincoli logici se-allora. (Vedi anche esempio svolto: [pli_modellazione_smistamento_automobili.md](../07_solved_examples/programmazione_lineare_intera/pli_modellazione_smistamento_automobili.md)).
*   [Esercizio 3: Apertura Filiali Assicurazione](by_topic/pli_modellazione_esercizi.md#esercizio-3): Localizzazione e assegnamento clienti con vincoli di personale.
*   [Esercizio 4: Asili Nido Montani](by_topic/pli_modellazione_esercizi.md#esercizio-4): Localizzazione e bus scolastici con educatori proporzionali ai bambini. (Vedi anche esempio svolto: [pli_modellazione_asili_nido_montani.md](../07_solved_examples/programmazione_lineare_intera/pli_modellazione_asili_nido_montani.md)).
*   [Esercizio 5: Posizionamento Macchine Officina](by_topic/pli_modellazione_esercizi.md#esercizio-5): Assegnamento con incompatibilità spaziali e siti condivisi.
*   [Esercizio 6: Rifornimento Agende](by_topic/pli_modellazione_esercizi.md#esercizio-6): Trasporto capacitato con costi fissi di spedizione.
*   [Esercizio 7: Varianti Rifornimento Agende](by_topic/pli_modellazione_esercizi.md#esercizio-7): Condizioni di pacchi da 20, limitazioni su numero di fornitori e sconti condizionati. (Vedi anche esempio svolto: [pli_modellazione_rifornimento_agende.md](../07_solved_examples/programmazione_lineare_intera/pli_modellazione_rifornimento_agende.md)).
*   [Esercizio 8: Stendino di Remo](by_topic/pli_modellazione_esercizi.md#esercizio-8): Assegnamento di indumenti a file con minimizzazione di righe utilizzate e bilanciamento dei pesi. (Vedi anche esempio svolto: [pli_modellazione_stendino_remo.md](../07_solved_examples/programmazione_lineare_intera/pli_modellazione_stendino_remo.md)).
*   [Esercizio 9: Varianti Stendino](by_topic/pli_modellazione_esercizi.md#esercizio-9): Vincoli logici, incompatibilità e scelte condizionate per gli indumenti.

---

## Esercizi Algoritmici di B&B (`16_esercizi_BB.pdf`)

### Programmazione Lineare Intera Standard (2 Variabili)
*   [Esercizi 1-11](by_topic/pli_branch_and_bound_esercizi.md#esercizi-standard): Risoluzione tramite B&B standard con branching binario, calcolo del rilassamento continuo LP ed esplorazione in ampiezza.
    *   *Esercizio 1*: $\max 5x_1 + 8x_2$ (Vedi anche esempio svolto: [pli_bb_esercizio_svolto_1.md](../07_solved_examples/programmazione_lineare_intera/pli_bb_esercizio_svolto_1.md)).
    *   *Esercizio 2*: $\max x_1 + 3x_2$ s.t. $x_1 + 5x_2 \le 21$, $8x_1 + 2x_2 \le 35$.
    *   *Esercizi 3-11*: Varianti con diversi coefficienti e vincoli.

### Problemi dello Zaino Binario (Knapsack)
*   [Esercizi 12-16](by_topic/pli_branch_and_bound_esercizi.md#problemi-dello-zaino): Risoluzione tramite B&B per zaino binario con 4 oggetti, calcolando bound superiori (greedy continuo) ed inferiori (greedy intero).
    *   *Esercizio 12*: Valori $\{15, 11, 20, 10\}$, pesi $\{5, 2, 3, 4\}$, capacità $C=8$. (Vedi anche esempio svolto: [pli_bb_esercizio_svolto_zaino.md](../07_solved_examples/programmazione_lineare_intera/pli_bb_esercizio_svolto_zaino.md)).
    *   *Esercizi 13-16*: Varianti con diversi insiemi di valori, pesi e capacità.

---

## Esercizi di Programmazione Non Lineare (PNL)

*   [Esercizi Non Vincolati (Locale & Algoritmi)](by_topic/pnl_esercizi.md#1-ottimizzazione-non-vincolata-punti-stazionari-e-convessita): Punti stazionari, Hessiano 2D, e iterazioni con metodo del gradiente e Newton.
    *   *Esercizio 1*: $f(x, y) = 2x^2 + y^2 - xy - 2x - 3y$. (Vedi anche esempio svolto: [pnl_esercizi_non_vincolati.md](../07_solved_examples/programmazione_non_lineare/pnl_esercizi_non_vincolati.md)).
    *   *Esercizio 6*: $\max -x^2 - 2y^2 + 2xy + 2y$ da $(0,0)$ con gradiente e Newton. (Vedi anche esempio svolto: [pnl_esercizi_non_vincolati.md](../07_solved_examples/programmazione_non_lineare/pnl_esercizi_non_vincolati.md)).
*   [Esercizi Vincolati (Lagrange & KKT)](by_topic/pnl_esercizi.md#3-ottimizzazione-vincolata-condizioni-kkt-e-casi-combinatori): Ottimizzazione vincolata su insiemi chiusi e limitati (triangolo, cerchio, parabole) risolvendo il sistema KKT con combinatoria dei vincoli attivi.
    *   *Esercizio 2 (KKT)*: $\min/\max 4(x-1)^2 + (y-2)^2$ s.t. $x+y-2 \le 0, -x-1 \le 0, -y-1 \le 0$. (Vedi anche esempio svolto: [pnl_esercizi_vincolati_kkt.md](../07_solved_examples/programmazione_non_lineare/pnl_esercizi_vincolati_kkt.md)).
