---
type: method
topic: programmazione_lineare_intera
status: active
sources: [modelli_PLI.pdf]
reliability: official
---

# Modelli su Grafi con Matrice di Incidenza

## Quando Usarla
Questa metodologia si applica per formulare problemi di ottimizzazione definiti su reti o grafi (es. assegnamento di costo minimo, cammino minimo, flusso a costo minimo). La conservazione del flusso ai nodi consente di sfruttare le proprietà della matrice di incidenza nodo-arco.

## Grafo Orientato e Convenzioni di Flusso
Sia dato un grafo orientato $G = (N, A)$ dove $N$ è l'insieme dei nodi e $A$ l'insieme degli archi orientati $(i, j)$ da $i$ a $j$.
Ad ogni arco $(i, j) \in A$ associamo una variabile decisionale $x_{ij}$ che rappresenta il flusso o il transito lungo l'arco.

Ad ogni nodo $i \in N$ è associato un valore di bilancio $b_i$:
*   $b_i < 0$: Il nodo $i$ è sorgente (o di offerta). Produce un flusso netto pari a $|b_i|$.
*   $b_i > 0$: Il nodo $i$ è destinazione (o di domanda). Assorbe un flusso netto pari a $b_i$.
*   $b_i = 0$: Il nodo $i$ è di transito (conservazione pura del flusso).

## Vincoli di Conservazione del Flusso
Per ciascun nodo $i \in N$, la quantità totale di flusso entrante meno la quantità totale di flusso uscente deve essere uguale al bilancio del nodo $b_i$:

$$
\sum_{j : (j, i) \in A} x_{ji} - \sum_{j : (i, j) \in A} x_{ij} = b_i \quad \forall i \in N
$$

In alternativa, moltiplicando per $-1$, si può esprimere come flusso uscente meno flusso entrante pari a $-b_i$:
$$
\sum_{j : (i, j) \in A} x_{ij} - \sum_{j : (j, i) \in A} x_{ji} = -b_i \quad \forall i \in N
$$

Entrambe le forme sono corrette, purché applicate coerentemente a tutti i nodi.

## Formulazione Matriciale e TUM
In forma matriciale, i vincoli di conservazione si scrivono come:
$$
M x = b
$$
dove $M$ è la matrice di incidenza nodo-arco del grafo. 
*   Poiché la matrice di incidenza $M$ di un grafo orientato è **totalmente unimodulare (TUM)**, se il vettore dei bilanci $b$ è intero, tutti i vertici del poliedro del rilassamento continuo sono interi.
*   Pertanto, se le variabili hanno come vincolo di dominio $x_{ij} \ge 0$ intero, il problema può essere risolto come un normale PL continuo su $x_{ij} \ge 0$.

## Casi Tipici

### 1. Cammino Minimo da $s$ a $t$
Rappresenta il cammino a costo minimo da un nodo sorgente $s$ a un nodo destinazione $t$.
*   $b_s = -1$ (il flusso netto esce da $s$, cioè uscite - entrate = 1, o entrate - uscite = -1)
*   $b_t = 1$ (il flusso netto entra in $t$, cioè entrate - uscite = 1)
*   $b_i = 0$ per tutti gli altri nodi $i \ne s, t$.
*   Dominio: $x_{ij} \in \{0, 1\}$.

### 2. Flusso di Costo Minimo
Trasportare quantità di merci lungo la rete per soddisfare le domande nei nodi minimizzando i costi di trasporto.
*   $b_i$ rappresenta la domanda ($>0$) o l'offerta ($<0$) del nodo $i$.
*   Il problema è ammissibile solo se la somma dei bilanci è nulla: $\sum_{i \in N} b_i = 0$.
*   Vincoli aggiuntivi di capacità sugli archi: $0 \le x_{ij} \le u_{ij}$.
*   Dominio: $x_{ij} \in \mathbb{Z}_+$ (o continuo, data la TUM).

## Errori Comuni da Evitare
*   **Invertire i segni dei bilanci**: Assicurarsi che le entrate abbiano segno positivo e le uscite segno negativo (o viceversa) in modo coerente per ogni equazione.
*   **Dimenticare il bilancio complessivo**: Nei problemi di flusso a costo minimo, se la rete non è chiusa o bilanciata, il modello potrebbe risultare inammissibile.
