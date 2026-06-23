---
type: method-card
topic: programmazione_lineare
status: consolidated
sources:
  - raw_assets/Domande aperte RO.pdf
reliability: non-ufficiale
---

# Method Card: Cammino di Costo Minimo (Domanda Aperta)

## Quando Usarla

Quando la domanda chiede di formulare il **problema del cammino di costo minimo** in termini di PL o PLI, con variabili sugli archi.

> Complementa [METHOD_PL_CAMMINO_MINIMO.md](METHOD_PL_CAMMINO_MINIMO.md) con il taglio da domanda aperta teorica.

---

## Formulazione

Grafo orientato $G = (V, A)$, costi $c_{ij}$, sorgente $s$, destinazione $t$.

**Variabili**:
$$x_{ij} \in \{0, 1\} \quad \forall (i,j) \in A$$
(1 se l'arco fa parte del cammino, 0 altrimenti)

$$\min \sum_{(i,j) \in A} c_{ij} x_{ij}$$

**Bilanciamento** (conservazione del flusso unitario):
$$\sum_{(v,j) \in A} x_{vj} - \sum_{(i,v) \in A} x_{iv} =
\begin{cases}
1 & \text{se } v = s \\
-1 & \text{se } v = t \\
0 & \text{altrimenti}
\end{cases}$$

---

## Nota sulla TUM

Per la **totale unimodularità** della matrice di incidenza nodo-arco di un grafo orientato, il rilassamento continuo ($x_{ij} \ge 0$ invece di $x_{ij} \in \{0,1\}$) fornisce già una soluzione intera. Quindi si può risolvere come PL.

---

## Output da Esame

```
min sum c_{ij} x_{ij}
s.t.
  sum_{(v,j)} x_{vj} - sum_{(i,v)} x_{iv} = 1   se v = s
  sum_{(v,j)} x_{vj} - sum_{(i,v)} x_{iv} = -1  se v = t
  sum_{(v,j)} x_{vj} - sum_{(i,v)} x_{iv} = 0   altrimenti
  x_{ij} in {0,1}  [o >= 0 per rilassamento TUM]
```

---

## Collegamento Pattern

→ [[Domande_aperte_modellazione_reti]]
→ [[METHOD_PL_CAMMINO_MINIMO]]
