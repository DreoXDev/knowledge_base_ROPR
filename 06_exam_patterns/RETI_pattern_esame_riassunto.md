---
type: exam-pattern
topic: programmazione_lineare
status: consolidated
---

# RETI — Riepilogo Pattern d'Esame

## Tabella Segnali → Metodo → File

| Segnale nella traccia | Metodo | Method Card / File |
|---|---|---|
| "sorgenti", "destinazioni", "offerta", "domanda", "trasporto" | Modello trasporto | `MC_RETI_trasporto_transhipment.md` |
| "offerta > domanda", "domanda > offerta", "sbilanciato" | Trasporto sbilanciato | `MC_RETI_trasporto_transhipment.md` |
| "transhipment", "nodi intermedi", "transito" | Transhipment | `MC_RETI_trasporto_transhipment.md` |
| "flusso a costo minimo", "bilanciamento nodi", "b_v" | Flusso costo minimo | `MC_RETI_flusso_costo_minimo.md` |
| "massimo flusso", "max flow", "capacità archi", "taglio" | Massimo flusso | `MC_RETI_massimo_flusso.md` |
| "cammino minimo", "grafo orientato", "nodi origine/destinazione" | Cammino minimo | `MC_RETI_cammino_minimo.md` |
| "TUM", "totale unimodulare", "rilassamento continuo intero" | TUM | `MC_PL_totale_unimodularita_rilassamento.md` |
| "distribuzione", "Bell Computers", "reti di distribuzione" | Trasporto/distribuzione | `07_solved_examples/reti_distribuzione_bell_computers.md` |

---

## Template Risposta per Tipo

### Trasporto
```
Dati: m sorgenti offerta s_i, n destinazioni domanda d_j, costi c_{ij}
Variabili: x_{ij} >= 0 (quantità spedita da i a j)

min Σ_{i,j} c_{ij} x_{ij}
s.t.
  Σ_j x_{ij} = s_i    ∀i  (offerta)
  Σ_i x_{ij} = d_j    ∀j  (domanda)
  x_{ij} >= 0

[Sbilanciato: aggiungere nodo fittizio con differenza e costo 0]
```

### Flusso a Costo Minimo
```
min Σ_{(i,j)∈A} c_{ij} x_{ij}
s.t.
  Σ_{(v,j)} x_{vj} - Σ_{(i,v)} x_{iv} = b_v   ∀v∈V
  0 <= x_{ij} <= u_{ij}

[b_v > 0: sorgente, b_v < 0: destinazione, b_v = 0: transito]
[Σ_v b_v = 0 necessario]
```

### Massimo Flusso
```
max f
s.t.
  Σ_{(s,j)} x_{sj} - Σ_{(i,s)} x_{is} = f     (sorgente s)
  Σ_{(v,j)} x_{vj} - Σ_{(i,v)} x_{iv} = 0     (transito v)
  Σ_{(t,j)} x_{tj} - Σ_{(i,t)} x_{it} = -f    (destinazione t)
  0 <= x_{ij} <= u_{ij}
```

### Cammino Minimo
```
min Σ c_{ij} x_{ij}
s.t.
  Σ_{(s,j)} x_{sj} - Σ_{(i,s)} x_{is} = 1    (sorgente)
  Σ_{(v,j)} x_{vj} - Σ_{(i,v)} x_{iv} = 0    (transito)
  Σ_{(t,j)} x_{tj} - Σ_{(i,t)} x_{it} = -1   (destinazione)
  x_{ij} ∈ {0,1}  [o >= 0 per TUM]
```

---

## Errori Frequenti

- ❌ Non definire la variabile $x_{ij}$ prima di usarla.
- ❌ Segni incoerenti nel bilanciamento nodo (flusso uscente − entrante = b_v).
- ❌ Dimenticare il vincolo di bilanciamento globale $\sum_v b_v = 0$.
- ❌ Non aggiungere nodo fittizio nel caso sbilanciato.
- ❌ Non specificare il dominio delle variabili.

---

## Method Card di Riferimento Principale

→ [[MC_RETI_trasporto_transhipment]]
→ [[MC_RETI_flusso_costo_minimo]]
→ [[MC_RETI_massimo_flusso]]
→ [[MC_RETI_cammino_minimo]]
