---
type: exam-pattern
topic: programmazione_lineare
status: consolidated
sources:
  - raw_assets/Domande aperte RO.pdf
reliability: non-ufficiale
---

# Pattern — Domanda Aperta: Modellazione Reti

## Riconoscimento

Segnali nella traccia:
- "formulare il problema di trasporto"
- "sorgenti, destinazioni, offerta, domanda"
- "flusso a costo minimo"
- "massimo flusso"
- "cammino di costo minimo"
- "transhipment" / "nodi di transito"
- "bilanciamento del flusso"

---

## Procedura Rapida

1. **Identificare il tipo di problema**: trasporto / transhipment / flusso / max flusso / cammino minimo.
2. **Definire le variabili** $x_{ij}$ e il loro significato.
3. **Scrivere la funzione obiettivo**.
4. **Scrivere i vincoli** (offerta, domanda, bilanciamento, capacità).
5. **Specificare il dominio** ($x_{ij} \ge 0$, $x_{ij} \in \{0,1\}$, ecc.).
6. **Commentare** eventuali casi speciali (offerta > domanda, nodi fittizi, ecc.).

---

## Template per Ciascun Modello

### Trasporto

```
min sum_{i,j} c_{ij} x_{ij}

s.t.
  sum_j x_{ij} = s_i    per ogni sorgente i    (offerta)
  sum_i x_{ij} = d_j    per ogni destinazione j (domanda)
  x_{ij} >= 0

[Se offerta > domanda: aggiungere destinazione fittizia con
 domanda = surplus e costi = 0]
```

### Flusso a Costo Minimo

```
min sum_{(i,j) in A} c_{ij} x_{ij}

s.t.
  sum_{(v,j) in A} x_{vj} - sum_{(i,v) in A} x_{iv} = b_v   per ogni v in V
  0 <= x_{ij} <= u_{ij}   per ogni (i,j) in A

[b_v > 0: sorgente, b_v < 0: destinazione, b_v = 0: transito]
```

### Massimo Flusso

```
max f

s.t.
  sum_{(v,j)} x_{vj} - sum_{(i,v)} x_{iv} = f   se v = s (sorgente)
  sum_{(v,j)} x_{vj} - sum_{(i,v)} x_{iv} = -f  se v = t (destinazione)
  sum_{(v,j)} x_{vj} - sum_{(i,v)} x_{iv} = 0   altrimenti
  0 <= x_{ij} <= u_{ij}
```

### Cammino di Costo Minimo

```
min sum_{(i,j) in A} c_{ij} x_{ij}

s.t.
  sum_{(v,j)} x_{vj} - sum_{(i,v)} x_{iv} = 1   se v = s
  sum_{(v,j)} x_{vj} - sum_{(i,v)} x_{iv} = -1  se v = t
  sum_{(v,j)} x_{vj} - sum_{(i,v)} x_{iv} = 0   altrimenti
  x_{ij} in {0,1}  [o >= 0 per TUM]
```

---

## Errori da Evitare

- ❌ Non definire la variabile $x_{ij}$ (sempre specificare il significato).
- ❌ Segni incoerenti nel bilanciamento (flusso uscente - flusso entrante = $b_v$).
- ❌ Dimenticare la non negatività o il dominio binario.
- ❌ Non gestire il caso di bilanciamento globale ($\sum_v b_v = 0$) nel flusso.

---

## Collegamento Method Cards

- [[MC_RETI_trasporto_transhipment]]
- [[MC_RETI_flusso_costo_minimo]]
- [[MC_RETI_massimo_flusso]]
- [[MC_RETI_cammino_minimo]]
