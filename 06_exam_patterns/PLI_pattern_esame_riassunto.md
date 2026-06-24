---
type: exam-pattern
topic: programmazione_lineare_intera
status: consolidated
---

# PLI — Riepilogo Pattern d'Esame

## Tabella Segnali → Metodo → File

| Segnale nella traccia | Metodo | Method Card / File |
|---|---|---|
| "variabili intere", "variabili binarie", "0-1" | Modellazione PLI | `MC_PLI_formulazione_modello.md` |
| "se X allora Y", "almeno k su n", "either-or" | Vincoli logici / Big-M | `MC_PLI_vincoli_logici_big_m.md` |
| "rappresentazione binaria", "espansione binaria di intero" | Binarizzazione | `MC_PLI_rappresentazione_binaria_interi.md` |
| "set covering", "tutti i clienti coperti" | Set covering | `04_methods/pl_set_covering_e_maximum_coverage.md` |
| "maximum coverage", "budget k impianti" | Maximum coverage | `04_methods/pl_set_covering_e_maximum_coverage.md` |
| "facility location", "costi fissi apertura" | Facility location | `MC_PLI_facility_location.md` |
| "produzione e magazzino", "periodi", "scorte" | Produzione stoccaggio | `MC_PLI_produzione_stoccaggio.md` |
| "zaino", "knapsack", "investimento", "budget" | Zaino / knapsack | `MC_PLI_knapsack.md` |
| "assegnamento", "one-to-one", "matrice costi" | Assegnamento | `MC_PLI_assegnamento_costo_minimo.md` |
| "flusso", "nodi", "archi", "bilanciamento" | Flusso costo minimo PLI | `MC_PLI_flusso_costo_minimo.md` |
| "cammino minimo", "variabili 0-1 sugli archi" | Cammino minimo PLI | `MC_PLI_cammino_costo_minimo.md` |
| "Branch and Bound", "B&B", "albero", "potatura" | B&B generico | `MC_PLI_branch_and_bound.md` |
| "zaino", "rendimento decrescente", "greedy" | Zaino greedy + B&B | `MC_PLI_branch_and_bound_zaino.md` |
| "variabili 0-1 pure", "B&B binario" | B&B binario | `MC_PLI_branch_and_bound_binario.md` |
| "PLIM", "misto intero", "alcune variabili intere" | B&B PLIM | `MC_PLI_branch_and_bound_plim.md` |
| "leggi l'albero B&B", "intervallo ottimo", "best bound" | Interpretazione albero | `MC_PLI_interpretare_albero_branch_and_bound.md` |
| "gap di ottimalità", "tolleranza", "quasi-ottima" | Gap B&B | `MC_PLI_gap_ottimalita_branch_and_bound.md` |
| "TUM", "totale unimodularità", "rilassamento continuo intero" | TUM | `MC_PL_totale_unimodularita_rilassamento.md` |

---

## Struttura Risposta da Esame

### Modellazione PLI
```
1. Definisci variabili continue e binarie (distingui sempre)
2. Funzione obiettivo
3. Vincoli funzionali
4. Vincoli logici (Big-M se serve)
5. Dominio: x >= 0, y ∈ {0,1}
```

### Branch and Bound
```
1. Risolvi rilassamento LP del nodo radice
2. Se soluzione intera → aggiorna incumbent Z_I
3. Se frazionaria → branching su variabile non intera
4. Pota se: inammissibile / bound peggiore di Z_I / soluzione intera
5. Continua fino a tutti i nodi chiusi → soluzione ottima = Z_I
```

### Zaino Greedy (Bound)
```
UB (continuo): ordina per rendimento v_j/p_j decrescente, inserisci
  interi, poi frazione dell'ultimo che non entra.
LB (intero): ordina per rendimento, inserisci solo elementi che entrano,
  salta quelli troppo pesanti (nessuna frazione).
```

---

## Errori Frequenti

- ❌ Non distinguere variabili intere e continue nel PLIM.
- ❌ Arrotondare il bound frazionario del rilassamento (vietato).
- ❌ Ramificare su variabili continue in PLIM.
- ❌ Applicare greedy intero con frazione dell'elemento chiave (è greedy continuo, non intero).
- ❌ Dimenticare di aggiornare l'incumbent quando si trova soluzione intera.
- ❌ Potare per dominanza prima di aver calcolato il bound del nodo.

---

## Method Card di Riferimento Principale

→ [[MC_PLI_formulazione_modello]]
→ [[MC_PLI_branch_and_bound]]
→ [[MC_PLI_branch_and_bound_zaino]]
