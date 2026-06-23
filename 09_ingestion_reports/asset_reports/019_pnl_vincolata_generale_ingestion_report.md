# Ingestion Report — PNL Vincolata Generale

## Metadata

- Source IDs:
  - `SRC-0089` (`raw_assets/Programmazione Non Lineare/Ottimizzazione non lineare vincolata.pdf`)
- Tipo file: PDF
- Categoria: Slide ufficiali dei docenti
- Area ROPR: Programmazione Non Lineare (PNL) - Ottimizzazione Vincolata Generale
- Affidabilità: Ufficiale (official)
- Stato analisi: Completato (consolidated)

## Sintesi Contenuto

Questo asset introduce i fondamenti teorici e gli approcci pratici per risolvere problemi di Programmazione Non Lineare (PNL) vincolata in più variabili. Definisce la formulazione standard del problema con vincoli di uguaglianza e disuguaglianza. Presenta in dettaglio tre metodologie risolutive:
1.  **Riduzione del Numero di Variabili**: Eliminazione di variabili libere esplicitando i vincoli di uguaglianza, riducendo il problema a una dimensione inferiore non vincolata.
2.  **Moltiplicatori di Lagrange**: Risoluzione del sistema lagrangiano del primo ordine per vincoli di sola uguaglianza, inclusa l'interpretazione geometrica del gradiente parallelo ai vincoli.
3.  **Condizioni KKT**: Formulazione delle condizioni necessarie per vincoli di disuguaglianza (stazionarietà, ammissibilità primale, complementarità degli scarti ed ammissibilità duale).

## Argomenti Estratti

- **Formulazione standard di PNL vincolata**: Minimizzazione di $f(x)$ s.t. $g_i(x) = 0$ e $h_j(x) \le 0$.
- **Metodo di Riduzione delle Variabili**: Applicabilità quando è possibile invertire in modo univoco i vincoli di uguaglianza. Esempio quadratico risolto con vincolo lineare $x_1+4x_2=3$.
- **Moltiplicatori di Lagrange**: Costruzione della Lagrangiana $L = f + \sum \lambda_i g_i$ e risoluzione del sistema del primo ordine. Esempio sul cerchio unitario con ottimo massimo $\sqrt{2}$ in $(1/\sqrt{2}, 1/\sqrt{2})$ e minimo $-\sqrt{2}$ in $(-1/\sqrt{2}, -1/\sqrt{2})$.
- **Condizioni KKT per disuguaglianze**: Condizioni necessarie del primo ordine per ottimalità locale. Regole di segno dei moltiplicatori ($\mu_j \ge 0$ per minimo).
- **Vincoli attivi e complementarità**: Relazione logica tra lo stato del vincolo $h_j(x^*) < 0 \implies \mu_j^* = 0$ e $h_j(x^*) = 0 \implies \mu_j^* \ge 0$.

## File Creati / Aggiornati

- [pnl_ottimizzazione_vincolata.md](../../05_theory/programmazione_non_lineare/pnl_ottimizzazione_vincolata.md)
- [pnl_riduzione_variabili_libere.md](../../04_methods/programmazione_non_lineare/pnl_riduzione_variabili_libere.md)
- [pnl_vincoli_attivi_e_complementarita.md](../../04_methods/programmazione_non_lineare/pnl_vincoli_attivi_e_complementarita.md)
- [pnl_lagrange_cerchio_unitario.md](../../07_solved_examples/programmazione_non_lineare/pnl_lagrange_cerchio_unitario.md)
- [pnl_riduzione_variabili_esempio_lineare.md](../../07_solved_examples/programmazione_non_lineare/pnl_riduzione_variabili_esempio_lineare.md)
- [pnl_pattern_vincolata_generale.md](../../06_exam_patterns/pnl_pattern_vincolata_generale.md)
- [MC_PNL_riduzione_variabili_libere.md](../../10_rag/method_cards/MC_PNL_riduzione_variabili_libere.md)
- [MC_PNL_Lagrange_vincoli_uguaglianza.md](../../10_rag/method_cards/MC_PNL_Lagrange_vincoli_uguaglianza.md)
- [MC_PNL_KKT_generale.md](../../10_rag/method_cards/MC_PNL_KKT_generale.md)
- [MC_PNL_vincoli_attivi_complementarita.md](../../10_rag/method_cards/MC_PNL_vincoli_attivi_complementarita.md)
- [TC_PNL_vincolata.md](../../10_rag/topic_cards/TC_PNL_vincolata.md)
- [TC_PNL_Lagrange.md](../../10_rag/topic_cards/TC_PNL_Lagrange.md)
- [TC_PNL_KKT.md](../../10_rag/topic_cards/TC_PNL_KKT.md)
- [pnl_vincolata_generale_flashcards.md](../../08_flashcards/pnl_vincolata_generale_flashcards.md)
- [PNL_vincolata_generale.csv](../../flashcards/PNL_vincolata_generale.csv)
