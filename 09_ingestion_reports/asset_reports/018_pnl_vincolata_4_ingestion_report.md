# Ingestion Report — PNL Vincolata 4

## Metadata

- Source IDs:
  - `SRC-0093` (`raw_assets/Programmazione Non Lineare/PNL Vincolata 4.pdf`)
- Tipo file: PDF
- Categoria: Slide ufficiali dei docenti
- Area ROPR: Programmazione Non Lineare (PNL) - KKT con Vincoli Attivi
- Affidabilità: Ufficiale (official)
- Stato analisi: Completato (consolidated)

## Sintesi Contenuto

Questo asset presenta un esempio numerico guidato di risoluzione di un problema di Programmazione Non Lineare vincolata tramite condizioni KKT ed enumerazione dei vincoli attivi. Il problema consiste nella minimizzazione di una funzione obiettivo quadratica:
$$f(x, y) = 4(x-1)^2 + (y-2)^2$$
soggetta a tre vincoli lineari di disuguaglianza:
$$x+y \le 2, \quad x \ge -1, \quad y \ge -1$$
L'asset illustra come l'introduzione di $m$ vincoli porti ad analizzare fino a $2^m = 8$ combinazioni di vincoli attivi/inattivi, e descrive i criteri per scartare sistematicamente i candidati non ammissibili o con moltiplicatori negativi. L'ottimo globale vincolato risulta essere il punto $(0.8, 1.2)$ con valore $f(0.8, 1.2) = 0.8$.

## Argomenti Estratti

- **KKT con Vincoli di Disuguaglianza**: Formulazione standard dei vincoli $g_i(x, y) \le 0$ e stesura della Lagrangiana associata.
- **Enumerazione dei Vincoli Attivi**: Generazione combinatoria dei casi attivi ($2^3 = 8$ combinazioni possibili per tre vincoli).
- **Criteri di Scarto dei Candidati**:
  - Inammissibilità del punto primale.
  - Moltiplicatore lagrangiano $\mu_i < 0$ in un problema di minimo con vincolo standard $g_i \le 0$ (ammissibilità duale violata).
  - Sistemi di equazioni incompatibili (es. tutti i vincoli attivi).
- **Risoluzione Dettagliata per Casi**:
  - Caso 1 (solo $g_1$ attivo): ottimo stazionario ammissibile $(0.8, 1.2)$ con $\mu_1 = 1.6 > 0$ (valido, ottimo globale).
  - Caso 2 (solo $g_2$ attivo): punto candidato $(-1, 2)$ con $\mu_2 = -16 < 0$ (scartato).
  - Caso 3 (solo $g_3$ attivo): punto candidato $(1, -1)$ con $\mu_3 = -6 < 0$ (scartato).
  - Casi 4, 5, 6 (coppie di vincoli attivi): punti candidati $(-1, 3)$, $(3, -1)$ e $(-1, -1)$ (validi ma con valori obiettivo maggiori rispetto al Caso 1).
  - Caso 7 (tutti attivi): sistema privo di soluzioni.
  - Caso 8 (nessuno attivo): ottimo non vincolato $(1, 2)$ non ammissibile (viola $x+y \le 2$).

## File Creati / Aggiornati

- [pnl_vincolata_kkt_vincoli_attivi.md](../../04_methods/programmazione_non_lineare/pnl_vincolata_kkt_vincoli_attivi.md)
- [pnl_kkt_esempio_quadratico_3_vincoli.md](../../07_solved_examples/programmazione_non_lineare/pnl_kkt_esempio_quadratico_3_vincoli.md)
- [pnl_pattern_kkt_enumerazione_vincoli_attivi.md](../../06_exam_patterns/pnl_pattern_kkt_enumerazione_vincoli_attivi.md)
- [MC_PNL_kkt_vincoli_disuguaglianza.md](../../10_rag/method_cards/MC_PNL_kkt_vincoli_disuguaglianza.md)
- [TC_PNL_kkt_vincoli_attivi.md](../../10_rag/topic_cards/TC_PNL_kkt_vincoli_attivi.md)
- [TC_PNL_vincolata_esempi.md](../../10_rag/topic_cards/TC_PNL_vincolata_esempi.md)
- [pnl_kkt_vincoli_attivi_flashcards.md](../../08_flashcards/pnl_kkt_vincoli_attivi_flashcards.md)
- [PNL_KKT_vincoli_attivi.csv](../../flashcards/PNL_KKT_vincoli_attivi.csv)
