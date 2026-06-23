---
type: method-card
topic: programmazione_lineare
status: consolidated
sources:
  - raw_assets/Domande aperte RO.pdf
reliability: non-ufficiale
---

# Method Card: Flusso a Costo Minimo (Teoria)

## Quando Usarla

Quando la domanda chiede di formulare il **problema di flusso a costo minimo** in termini teorici (bilanciamento nodi, capacità, relazione con trasporto).

> Complementa [MC_PLI_flusso_costo_minimo.md](MC_PLI_flusso_costo_minimo.md) con taglio teorico da domanda aperta.

---

## Formulazione

Grafo orientato $G = (V, A)$, costi $c_{ij}$, capacità $u_{ij}$, domanda/offerta netta $b_v$.

**Variabili**: $x_{ij}$ = flusso sull'arco $(i,j)$.

$$\min \sum_{(i,j) \in A} c_{ij} x_{ij}$$

**Bilanciamento** per ogni nodo $v$:
$$\sum_{(v,j) \in A} x_{vj} - \sum_{(i,v) \in A} x_{iv} = b_v \quad \forall v \in V$$

**Capacità**:
$$0 \le x_{ij} \le u_{ij} \quad \forall (i,j) \in A$$

**Bilanciamento globale**: $\sum_{v \in V} b_v = 0$.

---

## Tipi di Nodo

| Tipo | $b_v$ |
|---|---|
| Sorgente | $b_v > 0$ |
| Destinazione | $b_v < 0$ |
| Transito | $b_v = 0$ |

---

## Relazione con Trasporto

Il problema di trasporto è un caso speciale di flusso a costo minimo:
- Grafo bipartito (sorgenti → destinazioni).
- Nessuna capacità superiore sugli archi ($u_{ij} = +\infty$).

---

## Totalità Unimodulare (TUM)

La matrice di incidenza nodo-arco di un grafo orientato è **totalmente unimodulare**: ogni sottomatrice quadrata ha determinante $\in \{-1, 0, 1\}$. Quindi il rilassamento continuo del problema intero su questa struttura fornisce già soluzioni intere (se $b_v$ interi).

---

## Collegamento Pattern

→ [[Domande_aperte_modellazione_reti]]
→ [[MC_PLI_flusso_costo_minimo]]
