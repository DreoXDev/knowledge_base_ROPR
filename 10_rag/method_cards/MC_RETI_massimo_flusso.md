---
type: method-card
topic: programmazione_lineare
status: consolidated
sources:
  - raw_assets/Domande aperte RO.pdf
reliability: non-ufficiale
---

# Method Card: Massimo Flusso

## Quando Usarla

Quando la domanda chiede di formulare il **problema di massimo flusso** su una rete.

---

## Formulazione

Grafo orientato $G = (V, A)$ con sorgente $s$, destinazione $t$, capacità $u_{ij}$ sugli archi.

**Variabile di flusso**: $f$ (flusso totale da $s$ a $t$).
**Variabili sugli archi**: $x_{ij} \ge 0$.

$$\max f$$

**Bilanciamento**:
$$\sum_{(v,j) \in A} x_{vj} - \sum_{(i,v) \in A} x_{iv} =
\begin{cases}
f & \text{se } v = s \\
-f & \text{se } v = t \\
0 & \text{altrimenti}
\end{cases}$$

**Capacità**:
$$0 \le x_{ij} \le u_{ij} \quad \forall (i,j) \in A$$

---

## Interpretazione

- $f$ è il flusso netto in uscita dalla sorgente $s$.
- I nodi intermedi rispettano la conservazione del flusso.
- Il massimo flusso è limitato dalla **capacità del taglio minimo** (teorema max-flow min-cut).

---

## Output da Esame

```
max f
s.t.
  sum_{(v,j)} x_{vj} - sum_{(i,v)} x_{iv} = f    se v = s (sorgente)
  sum_{(v,j)} x_{vj} - sum_{(i,v)} x_{iv} = -f   se v = t (destinazione)
  sum_{(v,j)} x_{vj} - sum_{(i,v)} x_{iv} = 0    altrimenti (transito)
  0 <= x_{ij} <= u_{ij}
```

---

## Collegamento Pattern

→ [[Domande_aperte_modellazione_reti]]
