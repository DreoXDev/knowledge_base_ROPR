---
type: method-card
topic: programmazione_lineare
status: consolidated
sources:
  - raw_assets/Domande aperte RO.pdf
reliability: non-ufficiale
---

# Method Card: Trasporto e Transhipment

## Quando Usarla

Quando la domanda chiede di formulare il **problema di trasporto** (bilanciato o sbilanciato) o il **problema di transhipment**.

---

## Problema di Trasporto

**Dati**: $m$ sorgenti con offerta $s_i$, $n$ destinazioni con domanda $d_j$, costi $c_{ij}$.

**Variabili**: $x_{ij} \ge 0$ (quantità spedita da $i$ a $j$).

**Formulazione**:
$$\min \sum_{i=1}^m \sum_{j=1}^n c_{ij} x_{ij}$$

$$\sum_{j=1}^n x_{ij} = s_i \quad \forall i \quad \text{(offerta)}$$

$$\sum_{i=1}^m x_{ij} = d_j \quad \forall j \quad \text{(domanda)}$$

$$x_{ij} \ge 0$$

**Bilanciamento**: $\sum_i s_i = \sum_j d_j$ (altrimenti aggiungere nodo fittizio).

---

## Gestione Sbilanciamento

| Caso | Azione |
|---|---|
| Offerta > domanda | Aggiungere **destinazione fittizia** $j^*$ con $d_{j^*} = \sum s_i - \sum d_j$ e $c_{ij^*} = 0$ |
| Domanda > offerta | Aggiungere **sorgente fittizia** $i^*$ con $s_{i^*} = \sum d_j - \sum s_i$ e $c_{i^*j} = 0$ (o penalizzato) |

---

## Problema di Transhipment

Il transhipment generalizza il trasporto con **nodi intermedi** (transito):
- Sorgenti: $b_v > 0$.
- Destinazioni: $b_v < 0$.
- Transito: $b_v = 0$.

$$\min \sum_{(i,j) \in A} c_{ij} x_{ij}$$

$$\sum_{(v,j) \in A} x_{vj} - \sum_{(i,v) \in A} x_{iv} = b_v \quad \forall v \in V$$

$$x_{ij} \ge 0$$

con $\sum_v b_v = 0$ (bilanciamento globale).

---

## Output da Esame

```
Problema di trasporto: m sorgenti, n destinazioni, costi c_{ij}.
min sum c_{ij} x_{ij}
s.t.
  sum_j x_{ij} = s_i  (offerta sorgente i)
  sum_i x_{ij} = d_j  (domanda destinazione j)
  x_{ij} >= 0

Se offerta > domanda: aggiungere destinazione fittizia con domanda = surplus, costo = 0.
```

---

## Collegamento Pattern

→ [[Domande_aperte_modellazione_reti]]
→ [[MC_PL_modello_trasporto]]
