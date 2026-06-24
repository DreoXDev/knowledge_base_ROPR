---
type: exam-pattern
topic: programmazione_lineare
status: consolidated
---

# PL — Riepilogo Pattern d'Esame

## Tabella Segnali → Metodo → File

| Segnale nella traccia | Metodo | Method Card / File |
|---|---|---|
| "formulare", "modellare", variabili, vincoli, obiettivo | Modellazione PL | `PL_formulazione_modello.md` |
| "problema della dieta", "produzione", "turni" | Formulazione da testo | `04_methods/pl_formulare_modello_pl_da_testo.md` |
| "trasporto", "sorgenti", "destinazioni", "offerta", "domanda" | Modello trasporto | `MC_PL_modello_trasporto.md` |
| "miscelazione", "blending", "benzina", "viscosità" | Problema miscelazione | `04_methods/pl_problemi_di_miscelazione.md` |
| "cammino minimo", "grafo", "nodi", "archi" | Cammino minimo | `METHOD_PL_CAMMINO_MINIMO.md` |
| "simplesso", "tableau", "variabile entrante/uscente", "pivot" | Simplesso tabellare | `04_methods/pl_simplesso_tabellare.md` |
| "due fasi", "variabili artificiali", "inammissibilità" | Metodo due fasi | `04_methods/pl_metodo_due_fasi.md` |
| "illimitato", "nessuna variabile uscente" | Simplesso caso illimitato | `MC_PL_simplesso_casi_particolari.md` |
| "ottimi multipli", "coefficiente zero", "infiniti ottimi" | Ottimi multipli | `MC_PL_simplesso_casi_particolari.md` |
| "degenerazione", "rapporto minimo multiplo" | Degenerazione | `05_theory/pl/19_degenerazione_simplesso.md` |
| "duale", "primale", "costruire il duale" | Costruzione duale | `METHOD_PL_DUALE.md` / `PL_costruzione_duale.md` |
| "dualità forte", "dualità debole", "relazione primale-duale" | Teoremi dualità | `MC_PL_dualita_forte_debole.md` |
| "complementary slackness", "scarti complementari" | Complementarità | `PL_complementary_slackness.md` |
| "prezzi ombra", "shadow price", "valore marginale" | Prezzi ombra | `PL_prezzi_ombra.md` |
| "analisi di sensitività", "range", "Δ", "RHS" | Analisi sensitività | `MC_PL_analisi_sensitivita_da_tableau.md` |
| "vertici ammissibili", "geometria simplesso", "faccia ottima" | Teoria vertici | `MC_PL_vertici_soluzioni_base.md` |
| "soluzione di base", "BFS", "variabili di base" | Soluzioni di base | `MC_PL_vertici_soluzioni_base.md` |
| "set covering", "maximum coverage", "copertura" | Set covering/max cov | `04_methods/pl_set_covering.md` |

---

## Struttura Risposta da Esame

### Modellazione PL
```
1. Definisci indici e parametri
2. Definisci variabili decisionali (con unità)
3. Funzione obiettivo
4. Vincoli (con spiegazione breve)
5. Dominio
```

### Simplesso Tabellare
```
1. Forma aumentata (aggiunta slack)
2. Tableau iterazione 0
3. Identifica variabile entrante (costo ridotto favorevole)
4. Test minimo rapporto → variabile uscente
5. Pivot → nuovo tableau
6. Ripeti fino a ottimalità
7. Dichiara: x*, z*
```

### Dualità (costruzione)
```
1. Porta primale in forma standard
2. Associa variabile duale y_i a ogni vincolo primale
3. Obiettivo duale: min b^Ty (se primale max)
4. Vincoli duali: A^Ty >= c
5. Segni variabili duali: y_i >= 0 se vincolo <=, libera se =
```

---

## Errori Frequenti

- ❌ Dimenticare slack/surplus nella forma aumentata.
- ❌ Test minimo rapporto su elementi ≤ 0 (escluderli).
- ❌ Non dichiarare il valore delle variabili slack nell'ottimo.
- ❌ Invertire la direzione della dualità debole.
- ❌ Usare prezzi ombra da tableau non ottimo.
- ❌ Non specificare il verso dei vincoli duali per variabili libere.

---

## Method Card di Riferimento Principale

→ [[PL_formulazione_modello]]
→ [[04_methods/pl_simplesso_tabellare]]
→ [[METHOD_PL_DUALE]]
