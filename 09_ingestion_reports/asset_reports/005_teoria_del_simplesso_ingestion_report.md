# Ingestion Report — Teoria del Simplesso 23-24

## Metadata

- Source ID: `SRC-0078` (dal SOURCE_INVENTORY.md)
- Path: `raw_assets/Programmazione Lineare/Ricerca Operativa - Teoria del Simplesso - 23-24.pdf`
- Tipo file: PDF
- Categoria: Slide / Dispense ufficiali del corso
- Area ROPR: Programmazione Lineare
- Affidabilità: Ufficiale (official)
- Stato analisi: Completato (consolidated)

## Sintesi Contenuto
Il documento fornisce la formalizzazione matematica e geometrica che costituisce le fondamenta del metodo del simplesso. Vengono analizzati e definiti gli iperpiani e le equazioni di frontiera per vincoli funzionali e vincoli di non negatività; viene descritta la frontiera della regione ammissibile e la caratterizzazione geometrica e algebrica dei vertici; viene approfondito il fenomeno geometrico e algebrico della degenerazione; e vengono presentati i teoremi sulle proprietà dei vertici (adiacenza, cammino del simplesso, spigoli) e sull'esistenza di soluzioni ottime nei vertici.

## Argomenti Estratti
- **Iperpiani e frontiere**: Equazione di frontiera per vincolo funzionale ($\sum a_{ij}x_j = b_i$) e non negatività ($x_j = 0$).
- **Definizione di vertici**: Definizione geometrica (non giacere su segmenti interni) e definizione algebrica (soluzione simultanea di un sistema di $n$ equazioni di frontiera indipendenti), con distinzione tra vertice ammissibile e non ammissibile.
- **Degenerazione**: Presenza di più di $n$ iperpiani attivi nello stesso vertice, che si traduce algebricamente in basi multiple associate allo stesso punto e in una variabile di base a valore nullo.
- **Adiacenza e spigoli**: Condivisione di $n-1$ frontiere attive tra due vertici ammissibili. Il cammino del simplesso come sequenza di vertici adiacenti collegati da spigoli.
- **Teorema dell'ottimo nei vertici**: Se esiste un ottimo finito, almeno un vertice ammissibile è ottimo.
- **Ottimi multipli**: Combinazione convessa delle soluzioni ottime situate sui vertici di estremità.

## File Creati / Aggiornati
- `05_theory/programmazione_lineare/17_teoria_simplesso.md`
- `05_theory/programmazione_lineare/12_geometria_simplesso.md`
- `05_theory/programmazione_lineare/13_forma_aumentata_soluzioni_base.md`
- `05_theory/programmazione_lineare/18_vertici_adiacenti_cammino_simplesso.md`
- `05_theory/programmazione_lineare/19_degenerazione_simplesso.md`
- `05_theory/programmazione_lineare/20_proprieta_vertici_ammissibili.md`
- `04_methods/programmazione_lineare/pl_teoria_simplesso.md`
- `04_methods/programmazione_lineare/pl_riconoscere_vertici_e_frontiere.md`
- `04_methods/programmazione_lineare/pl_vertici_adiacenti_e_ottimalita.md`
- `08_flashcards/simplesso_teoria_flashcards.md`
- `10_rag/method_cards/PL_teoria_simplesso.md`
- `10_rag/method_cards/PL_vertici_frontiere_iperpiani.md`
- `10_rag/method_cards/PL_vertici_adiacenti_ottimalita.md`
- `10_rag/RAG_RETRIEVAL_INDEX.md`
- `10_rag/RAG_PATTERN_MAP.md`

## Warning / Refusi / Incongruenze Rilevate
- Nessuno. I concetti teorici estratti si integrano in modo coerente e complementare con la parte operativa del metodo del simplesso tabellare già integrata.
