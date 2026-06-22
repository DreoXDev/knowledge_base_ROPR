---
materia: ROPR
area: Programmazione Lineare Intera
tipo: metodo
fonte: Esercitazione 2 PL.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare-intera
  - set-covering
  - maximum-coverage
  - localizzazione
  - method-card
---

# METHOD CARD — Set Covering e Maximum Coverage

## Quando usarla

Usare questa card quando la traccia richiede di modellare la localizzazione di servizi (es. ripetitori, centraline, magazzini, ospedali) per coprire un insieme di zone o clienti, sotto vincoli di costo minimo o budget limitato.

---

## 1. Modello di Set Covering

### Scopo
Coprire **tutte** le zone di domanda al costo minimo (minimizzando il numero di installazioni).

### Formulazione Matematica
Sia $I$ l'insieme delle posizioni candidate all'installazione ($i \in I$) e $J$ l'insieme delle zone da coprire ($j \in J$).
Sia $a_{ji} = 1$ se un'installazione in $i$ copre la zona $j$, $0$ altrimenti.
Sia $c_i$ il costo di installazione nella posizione $i$.

**Variabili decisionali:**
$$
x_i \in \{0, 1\} \qquad \forall i \in I \quad (1 = \text{installo in } i, 0 = \text{altrimenti})
$$

**Funzione obiettivo:**
$$
\min Z = \sum_{i \in I} c_i x_i
$$

**Vincoli (Copertura garantita):**
Ciascuna zona $j$ deve essere coperta da almeno un servizio installato:
$$
\sum_{i \in I} a_{ji} x_i \ge 1 \qquad \forall j \in J
$$

---

## 2. Modello di Maximum Coverage

### Scopo
Massimizzare la popolazione o l'utilità coperta avendo a disposizione un **budget fisso** (es. si possono installare al massimo $k$ servizi).

### Formulazione Matematica
Siano $I, J, a_{ji}$ definiti come sopra. Sia $u_j$ la popolazione o utilità associata alla zona $j$. Sia $k$ il numero massimo di servizi installabili.

**Variabili decisionali:**
- $x_i \in \{0, 1\}$ ($\forall i \in I$): variabile binaria di installazione.
- $y_j \in \{0, 1\}$ ($\forall j \in J$): variabile binaria di copertura ($1$ se la zona $j$ è coperta, $0$ altrimenti).

**Funzione obiettivo:**
$$
\max W = \sum_{j \in J} u_j y_j
$$

**Vincoli:**
- **Vincolo di cardinalità (budget)**:
  $$
  \sum_{i \in I} x_i \le k \qquad (\text{oppure } = k)
  $$
- **Vincolo di attivazione della copertura**: La zona $j$ è considerata coperta ($y_j = 1$) solo se è installato almeno un servizio in grado di coprirla:
  $$
  y_j \le \sum_{i \in I} a_{ji} x_i \qquad \forall j \in J
  $$

---

## Warning Importante: Evitare il Doppio Conteggio

> [!CAUTION]
> Nel Maximum Coverage, **non** scrivere mai la funzione obiettivo come $\max \sum_{j} u_j \left(\sum_i a_{ji} x_i\right)$.
> 
> Questo errore sommererebbe più volte la popolazione di una zona se questa venisse coperta da più servizi contemporaneamente. 
> L'introduzione della variabile binaria $y_j$ e del vincolo $y_j \le \sum a_{ji} x_i$ garantisce che l'utilità $u_j$ venga contata **una sola volta** non appena la zona risulta coperta da almeno un servizio.
