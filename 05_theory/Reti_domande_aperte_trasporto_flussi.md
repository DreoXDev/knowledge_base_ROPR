---
type: theory-note
topic: programmazione_lineare
status: consolidated
sources:
  - raw_assets/Domande aperte RO.pdf
reliability: non-ufficiale
---

# Reti — Domande Aperte su Trasporto e Flussi

Fonte: `raw_assets/Domande aperte RO.pdf` (rielaborato con validazione)
Area: Reti e Programmazione Lineare
Prerequisiti: PL, grafi, flussi su rete

---

## Problema di Trasporto (D1, D16)

**Domanda**: Descrivere la formulazione generale del problema di trasporto. Come si gestisce il caso offerta maggiore della domanda?

### Formulazione

- $m$ sorgenti $i = 1, \dots, m$ con offerta $s_i$.
- $n$ destinazioni $j = 1, \dots, n$ con domanda $d_j$.
- Costo unitario di trasporto $c_{ij}$ dalla sorgente $i$ alla destinazione $j$.

**Variabili**:
$$x_{ij} = \text{quantità spedita da sorgente } i \text{ a destinazione } j, \quad x_{ij} \ge 0$$

**Funzione obiettivo**:
$$\min \sum_{i=1}^{m} \sum_{j=1}^{n} c_{ij} x_{ij}$$

**Vincoli di offerta** (tutta l'offerta viene spedita):
$$\sum_{j=1}^{n} x_{ij} = s_i \quad \forall i$$

**Vincoli di domanda** (tutta la domanda viene soddisfatta):
$$\sum_{i=1}^{m} x_{ij} = d_j \quad \forall j$$

**Non negatività**: $x_{ij} \ge 0$.

> Il problema di trasporto è bilanciato se $\sum_i s_i = \sum_j d_j$.

### Gestione Offerta > Domanda (D1)

Se $\sum_i s_i > \sum_j d_j$ (offerta in eccesso):

→ Si aggiunge una **destinazione fittizia** $j^*$ con domanda:
$$d_{j^*} = \sum_i s_i - \sum_j d_j$$

e costi nulli: $c_{ij^*} = 0$ per ogni $i$.

Il problema diventa bilanciato e si risolve con la formulazione standard.

### Gestione Domanda > Offerta

Se $\sum_j d_j > \sum_i s_i$ (domanda in eccesso):

→ Si aggiunge una **sorgente fittizia** $i^*$ con offerta:
$$s_{i^*} = \sum_j d_j - \sum_i s_i$$

e costi nulli (o penalizzati, secondo il contesto).

---

## Problema di Transhipment (D15)

**Domanda**: Come si modella il problema di transhipment?

Il problema di transhipment generalizza il trasporto ammettendo **nodi intermedi** (nodi di transito o trasbordo) attraverso cui il flusso può passare.

**Tipi di nodi**:
- **Sorgenti**: producono flusso netto positivo ($b_v > 0$).
- **Destinazioni**: consumano flusso netto positivo ($b_v < 0$).
- **Nodi di transito**: $b_v = 0$ (flusso in entrata = flusso in uscita).

**Formulazione** (equivalente al flusso a costo minimo):

$$\min \sum_{(i,j) \in A} c_{ij} x_{ij}$$

**Bilanciamento del flusso** per ogni nodo $v$:
$$\sum_{(v,j) \in A} x_{vj} - \sum_{(i,v) \in A} x_{iv} = b_v \quad \forall v \in V$$

con $\sum_{v} b_v = 0$ (bilanciamento globale).

**Non negatività**: $x_{ij} \ge 0$.

---

## Problema di Flusso a Costo Minimo (D17)

**Domanda**: Formulare il problema di flusso a costo minimo.

Dato un grafo orientato $G = (V, A)$:
- $c_{ij}$: costo unitario di flusso sull'arco $(i,j)$.
- $u_{ij}$: capacità massima dell'arco.
- $b_v$: domanda/offerta netta del nodo $v$ ($b_v > 0$: sorgente, $b_v < 0$: destinazione, $b_v = 0$: transito).

**Funzione obiettivo**:
$$\min \sum_{(i,j) \in A} c_{ij} x_{ij}$$

**Bilanciamento per ogni nodo**:
$$\sum_{(v,j) \in A} x_{vj} - \sum_{(i,v) \in A} x_{iv} = b_v \quad \forall v \in V$$

**Capacità**:
$$0 \le x_{ij} \le u_{ij} \quad \forall (i,j) \in A$$

> Il problema di trasporto è un caso speciale di flusso a costo minimo (senza capacità superiori sugli archi, bipartito).

---

## Problema di Massimo Flusso (D18)

**Domanda**: Formulare il problema di massimo flusso.

Dato un grafo $G = (V, A)$ con sorgente $s$ e destinazione $t$, e capacità $u_{ij}$ sugli archi:

**Funzione obiettivo**:
$$\max f$$

**Bilanciamento** (con flusso netto $f$ in uscita da $s$ e in entrata in $t$):
$$\sum_{(v,j) \in A} x_{vj} - \sum_{(i,v) \in A} x_{iv} =
\begin{cases}
f & \text{se } v = s \\
-f & \text{se } v = t \\
0 & \text{altrimenti}
\end{cases}$$

**Capacità**:
$$0 \le x_{ij} \le u_{ij} \quad \forall (i,j) \in A$$

---

## Problema di Cammino di Costo Minimo (D19)

**Domanda**: Formulare il problema di cammino di costo minimo.

Dato un grafo $G = (V, A)$ con sorgente $s$, destinazione $t$ e costi $c_{ij}$ sugli archi:

**Variabili**:
$$x_{ij} \in \{0, 1\} \quad \forall (i,j) \in A$$

**Funzione obiettivo**:
$$\min \sum_{(i,j) \in A} c_{ij} x_{ij}$$

**Bilanciamento**:
$$\sum_{(v,j) \in A} x_{vj} - \sum_{(i,v) \in A} x_{iv} =
\begin{cases}
1 & \text{se } v = s \\
-1 & \text{se } v = t \\
0 & \text{altrimenti}
\end{cases}$$

> Per la proprietà di totale unimodularità (TUM) della matrice di bilanciamento dei grafi orientati, il rilassamento continuo ($x_{ij} \ge 0$) fornisce già una soluzione intera.

---

## Risposta Modello — Struttura per Domande di Rete

```
[Definizione del problema e dei suoi dati]

Variabili: x_{ij} = ... (definire il significato)
Funzione obiettivo: min/max sum c_{ij} x_{ij}
Vincoli di [offerta / domanda / bilanciamento]:
  sum_{j} x_{ij} [=/<=/>=] [valore] per ogni [sorgente/nodo]
Vincoli di capacità: 0 <= x_{ij} <= u_{ij}
Non negatività / integrità: x_{ij} >= 0 [o binario]

[Commento su caso speciale se richiesto]
```

---

## Errori da Evitare

- ❌ Non definire la variabile $x_{ij}$ prima di usarla.
- ❌ Non specificare il dominio delle variabili ($\ge 0$, binario, ecc.).
- ❌ Usare segni incoerenti nei vincoli di bilanciamento.
- ❌ Dimenticare il vincolo di bilanciamento globale ($\sum_v b_v = 0$) nel flusso.
- ❌ Confondere flusso a costo minimo con trasporto (il trasporto è un caso speciale bipartito).

---

## Collegamenti

- [[MC_RETI_trasporto_transhipment]]
- [[MC_RETI_flusso_costo_minimo]]
- [[MC_RETI_massimo_flusso]]
- [[MC_RETI_cammino_minimo]]
- [[MC_PLI_flusso_costo_minimo]]
- [[METHOD_PL_CAMMINO_MINIMO]]
- [[MC_PL_modello_trasporto]]
