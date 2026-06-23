# Ingestion Report — PNL 20 Esercizi

## Metadata

- Source IDs:
  - `SRC-0090` (`raw_assets/Programmazione Non Lineare/20_esercizi_pnl.pdf`)
- Tipo file: PDF
- Categoria: Esercizi ufficiali
- Area ROPR: Programmazione Non Lineare (PNL)
- Affidabilità: Ufficiale (official)
- Stato analisi: Completato (consolidated)

## Sintesi Contenuto

Questo asset contiene una raccolta di 20 esercizi sulla Programmazione Non Lineare (PNL) in due variabili, suddivisi in due gruppi principali:
1.  **Esercizi 1-10 (PNL non vincolata)**: Ricerca dei punti stazionari tramite l'annullamento del gradiente ($\nabla f(x, y) = 0$) e classificazione locale (massimi, minimi, selle) tramite l'analisi della matrice Hessiana $H_f(x, y)$ (segno degli autovalori o determinante/traccia).
2.  **Esercizi 11-20 (PNL vincolata)**: Ottimizzazione globale su insiemi chiusi e limitati (compattezza e Teorema di Weierstrass) o illimitati, impostando e risolvendo il sistema di Karush-Kuhn-Tucker (KKT). Le soluzioni contengono la differenziazione dei candidati in base al segno dei moltiplicatori duali ($\mu_j$).

## Argomenti Estratti

- **Gradiente ed Hessiana**: Formule analitiche per funzioni polinomiali a due variabili.
- **Classificazione dei punti stazionari**:
  - $\det(H) > 0, \text{tr}(H) > 0 \implies$ minimo locale.
  - $\det(H) > 0, \text{tr}(H) < 0 \implies$ massimo locale.
  - $\det(H) < 0 \implies$ sella.
- **Condizioni KKT per disuguaglianze**: Formulazione standard, stazionarietà, ammissibilità primale/duale e complementarità degli scarti.
- **Casi di inesistenza dell'ottimo globale**: Discussione sull'illimitatezza della funzione obiettivo lungo particolari direzioni per regioni ammissibili non limitate (es. Esercizio 11, 12, 14, 18, 20).

## File Creati / Aggiornati

- [pnl_20_esercizi_catalogo.md](../../07_solved_examples/programmazione_non_lineare/pnl_20_esercizi_catalogo.md)
- [pnl_non_vincolata_esercizi_punti_stazionari.md](../../07_solved_examples/programmazione_non_lineare/pnl_non_vincolata_esercizi_punti_stazionari.md)
- [pnl_vincolata_esercizi_kkt_globali.md](../../07_solved_examples/programmazione_non_lineare/pnl_vincolata_esercizi_kkt_globali.md)
- [pnl_non_vincolata_classificazione_hessiana.md](../../06_exam_patterns/pnl_non_vincolata_classificazione_hessiana.md)
- [pnl_vincolata_kkt_globali.md](../../06_exam_patterns/pnl_vincolata_kkt_globali.md)
- [MC_PNL_classificazione_hessiana.md](../../10_rag/method_cards/MC_PNL_classificazione_hessiana.md)
- [MC_PNL_KKT_generale.md](../../10_rag/method_cards/MC_PNL_KKT_generale.md)
- [TC_PNL_esercizi.md](../../10_rag/topic_cards/TC_PNL_esercizi.md)
- [TC_PNL_KKT_esercizi.md](../../10_rag/topic_cards/TC_PNL_KKT_esercizi.md)
- [pnl_esercizi_flashcards.md](../../08_flashcards/pnl_esercizi_flashcards.md)
- [PNL_esercizi.csv](../../flashcards/PNL_esercizi.csv)
