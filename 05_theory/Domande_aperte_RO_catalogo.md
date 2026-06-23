---
type: theory-note
topic: riepilogo_generale
status: consolidated
sources:
  - raw_assets/Domande aperte RO.pdf
reliability: non-ufficiale
---

# Domande Aperte RO — Catalogo

Fonte: `raw_assets/Domande aperte RO.pdf`
Tipo: appunti non ufficiali / bozze di risposta teorica
Affidabilità: media — da validare con slide ufficiali

> ⚠️ Le risposte originali sono state riscritte in modo professionale. Non usare il PDF originale come fonte definitiva.

---

## Elenco Domande

| N | Tema | Domanda sintetica | Stato | File definitivo |
|---|---|---|---|---|
| 1 | Trasporto | Formulazione e gestione offerta > domanda | ✓ riscritto | [Reti_domande_aperte_trasporto_flussi.md](Reti_domande_aperte_trasporto_flussi.md) |
| 2 | Algoritmi genetici | Funzionamento e criteri di arresto | ✓ riscritto | [Metaeuristiche_domande_aperte.md](Metaeuristiche_domande_aperte.md) |
| 3 | Vertici PL | Proprietà dei vertici ammissibili | ✓ riscritto | [PL_domande_aperte_vertici_basi_dualita.md](PL_domande_aperte_vertici_basi_dualita.md) |
| 4 | Soluzioni di base | Proprietà di una soluzione di base | ✓ riscritto | [PL_domande_aperte_vertici_basi_dualita.md](PL_domande_aperte_vertici_basi_dualita.md) |
| 5 | Dualità | Dualità forte e dualità debole | ✓ riscritto | [PL_domande_aperte_vertici_basi_dualita.md](PL_domande_aperte_vertici_basi_dualita.md) |
| 6 | Simplesso | Direzione di spostamento e incremento | ✓ riscritto | [PL_domande_aperte_vertici_basi_dualita.md](PL_domande_aperte_vertici_basi_dualita.md) |
| 7 | Dualità | Relazione tra soluzione duale e primale | ✓ riscritto | [PL_domande_aperte_vertici_basi_dualita.md](PL_domande_aperte_vertici_basi_dualita.md) |
| 8 | Soluzioni di base | Numero massimo di soluzioni di base | ✓ riscritto | [PL_domande_aperte_vertici_basi_dualita.md](PL_domande_aperte_vertici_basi_dualita.md) |
| 9 | Complementarità | Condizioni di complementarità in PL | ✓ riscritto (frase informale eliminata) | [PL_domande_aperte_vertici_basi_dualita.md](PL_domande_aperte_vertici_basi_dualita.md) |
| 10 | KKT | Condizioni KKT e loro utilità | ✓ riscritto | [PNL_domande_aperte_KKT.md](PNL_domande_aperte_KKT.md) |
| 11 | Simulated Annealing | Funzionamento e criteri di arresto | ✓ riscritto | [Metaeuristiche_domande_aperte.md](Metaeuristiche_domande_aperte.md) |
| 12 | Algoritmi genetici | Crossover e mutazione | ✓ riscritto | [Metaeuristiche_domande_aperte.md](Metaeuristiche_domande_aperte.md) |
| 13 | Simulated Annealing | Exploration/exploitation e temperatura | ✓ riscritto | [Metaeuristiche_domande_aperte.md](Metaeuristiche_domande_aperte.md) |
| 14 | Tabu Search | Tabu list e criterio di aspirazione | ✓ riscritto | [Metaeuristiche_domande_aperte.md](Metaeuristiche_domande_aperte.md) |
| 15 | Transhipment | Modello di transhipment | ✓ riscritto | [Reti_domande_aperte_trasporto_flussi.md](Reti_domande_aperte_trasporto_flussi.md) |
| 16 | Trasporto | Formulazione generale problema di trasporto | ✓ riscritto | [Reti_domande_aperte_trasporto_flussi.md](Reti_domande_aperte_trasporto_flussi.md) |
| 17 | Flusso | Formulazione flusso a costo minimo | ✓ riscritto | [Reti_domande_aperte_trasporto_flussi.md](Reti_domande_aperte_trasporto_flussi.md) |
| 18 | Massimo flusso | Formulazione massimo flusso | ✓ riscritto | [Reti_domande_aperte_trasporto_flussi.md](Reti_domande_aperte_trasporto_flussi.md) |
| 19 | Cammino minimo | Formulazione cammino di costo minimo | ✓ riscritto | [Reti_domande_aperte_trasporto_flussi.md](Reti_domande_aperte_trasporto_flussi.md) |

---

## Priorità di Revisione

- **Alta**: domande 5, 7, 8, 9 (dualità, complementarità, basi) — correzione formule necessaria
- **Alta**: domande 10 (KKT) — controllo strettamente necessario
- **Media**: domande 11–14 (metaeuristiche) — riscrittura professionale
- **Media**: domande 1, 15–19 (reti) — formalizzazione dei modelli

---

## Errori Corretti Rispetto agli Appunti

- Eliminata frase informale nella domanda 9 (complementarità).
- Corretta convenzione segno per probabilità SA (min vs max).
- Verificata formula numero massimo basi: $\binom{n+m}{m}$ con $n$ variabili originali e $m$ vincoli (forma aumentata con $n+m$ variabili).
- Aggiunta definizione precisa di dualità debole.

---

## Collegamenti

- [[PL_domande_aperte_vertici_basi_dualita]]
- [[Reti_domande_aperte_trasporto_flussi]]
- [[PNL_domande_aperte_KKT]]
- [[Metaeuristiche_domande_aperte]]
