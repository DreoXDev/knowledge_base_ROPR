# Ingestion Report — Teoria della Dualità

## Metadata

- Source ID: `SRC-0079`
- Path: `raw_assets/Programmazione Lineare/Ricerca Operativa - Teoria della Dualità.pdf`
- Tipo file: PDF
- Categoria: Slide / Dispense ufficiali del corso
- Area ROPR: Programmazione Lineare
- Affidabilità: Ufficiale (official)
- Stato analisi: Completato (consolidated)

## Sintesi Contenuto
Il documento fornisce la trattazione formale completa della teoria della dualità per la Programmazione Lineare. Vengono presentate:
1. La costruzione sistematica del problema duale in forma algebrica e matriciale.
2. Le relazioni tra il tableau del simplesso del primale e la soluzione del duale (variabili duali nella riga 0, riga obiettivo).
3. I teoremi fondamentali della dualità: dualità debole ($cx \le yb$), ottimalità per $cx = yb$, dualità forte ($Z^* = W^*$).
4. Le condizioni di complementary slackness (scarti complementari) per la verifica dell'ottimalità.
5. I prezzi ombra e l'interpretazione economica delle variabili duali.
6. Le relazioni primale-duale nei casi limite (ottimo, illimitato, inammissibile).
7. Il metodo "sensible / odd / bizarre" per la formulazione del duale di problemi non in forma standard.

## Argomenti Estratti
- **Forma Matriciale del Duale**: Formulazione compatta $\min W = yb$ s.t. $yA \ge c$, $y \ge 0$.
- **Wyndor Glass Co.**: Esempio pratico completo di coppia primale-duale.
- **Teorema di Dualità Debole**: $\mathbf{c}\mathbf{x} \le \mathbf{y}\mathbf{b}$ per ogni coppia ammissibile.
- **Teorema di Dualità Forte**: Uguaglianza all'ottimo finito $Z^* = W^*$.
- **Complementary Slackness**: $y_i s_i = 0$ e $x_j v_j = 0$ per l'ottimalità.
- **Prezzi Ombra**: Tasso di variazione della F.O. al variare della risorsa ($y_i^* = \frac{\partial Z^*}{\partial b_i}$).
- **Tabella dei Casi Limite**: Relazioni di ammissibilità e illimitatezza.
- **Metodo SOB**: Regole mnemoniche per vincoli $=$ o $\ge$ e variabili libere o negative.

## File Creati / Aggiornati

### Note Teoriche (05_theory/)
- `05_theory/programmazione_lineare/10_dualita.md` (Aggiornato)
- `05_theory/programmazione_lineare/11_regole_costruire_duale.md` (Aggiornato)
- `05_theory/programmazione_lineare/21_costruzione_duale.md` (Creato)
- `05_theory/programmazione_lineare/22_dualita_debole_forte.md` (Creato)
- `05_theory/programmazione_lineare/23_prezzi_ombra_interpretazione.md` (Creato)
- `05_theory/programmazione_lineare/24_complementary_slackness.md` (Creato)
- `05_theory/programmazione_lineare/25_relazioni_primale_duale_limite.md` (Creato)

### Method Cards (04_methods/ & 10_rag/)
- `04_methods/programmazione_lineare/pl_costruire_duale_standard.md` (Creato)
- `04_methods/programmazione_lineare/pl_costruire_duale_sensible_odd_bizarre.md` (Creato)
- `04_methods/programmazione_lineare/pl_leggere_variabili_duali_da_tableau.md` (Creato)
- `04_methods/programmazione_lineare/pl_usare_complementary_slackness.md` (Creato)
- `10_rag/method_cards/PL_dualita_teoria.md` (Creato)
- `10_rag/method_cards/PL_costruzione_duale.md` (Creato)
- `10_rag/method_cards/PL_prezzi_ombra.md` (Creato)
- `10_rag/method_cards/PL_complementary_slackness.md` (Creato)
- `10_rag/method_cards/PL_sensible_odd_bizarre.md` (Creato)

### Flashcard (08_flashcards/)
- `08_flashcards/dualita_teoria_flashcards.md` (Creato)

### RAG & Metadata
- `10_rag/RAG_RETRIEVAL_INDEX.md` (Aggiornato)
- `10_rag/RAG_PATTERN_MAP.md` (Aggiornato)
- `00_meta/ASSET_TRACKING.md` (Aggiornato)
- `AI Plans/checklist_asset_ropr_obsidian.md` (Aggiornato)

## Warning / Refusi / Incongruenze Rilevate
- Nessuno. Tutti i teoremi e i metodi corrispondono alla notazione ufficiale usata nelle slide del corso.
