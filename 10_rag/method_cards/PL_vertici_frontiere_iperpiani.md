---
materia: ROPR
area: Programmazione Lineare
tipo: metodo
fonte: Ricerca Operativa - Teoria del Simplesso - 23-24.pdf
stato: completo
priorita: media
tags:
  - ropr
  - programmazione-lineare
  - simplesso
  - vertici
  - frontiere
  - method-card
---

# METHOD CARD — Riconoscere Vertici, Frontiere e Iperpiani

## Quando usarla
Usare quando l'esercizio chiede di identificare le frontiere dei vincoli, definire gli iperpiani o caratterizzare algebricamente e geometricamente un vertice (ammissibile o non ammissibile).

## Procedura e Definizioni per l'Esame

### 1. Ricavare le Equazioni di Frontiera
- Per ciascun vincolo funzionale $\sum a_{ij}x_j \le b_i$, la frontiera è l'equazione lineare:
  $$
  \sum_{j=1}^n a_{ij}x_j = b_i
  $$
- Per ciascun vincolo di non negatività $x_j \ge 0$, la frontiera è:
  $$
  x_j = 0
  $$
- Ciascuna di queste equazioni definisce un **iperpiano** nello spazio $\mathbb{R}^n$.

### 2. Caratterizzare un Vertice Algebricamente
Dato un problema in $n$ variabili decisionali:
1. Selezionare un sistema composto da $n$ equazioni di frontiera linearmente indipendenti.
2. Risolvere il sistema per determinare il punto di intersezione $P$.
3. **Verificare l'Ammissibilità**:
   - Sostituire le coordinate di $P$ in tutti gli altri vincoli del problema (quelli non inclusi nel sistema).
   - Se $P$ soddisfa tutti i vincoli rimanenti, allora $P$ è un **vertice ammissibile** (corrisponde ad una soluzione di base ammissibile).
   - Se $P$ viola anche un solo vincolo, allora $P$ è un **vertice non ammissibile**.
   - Se il sistema non ha soluzioni, gli iperpiani selezionati sono paralleli o incompatibili.
   - Se $P$ soddisfa con l'uguaglianza stretta più di $n$ vincoli, il vertice è **degenere** (vincoli ridondanti attivi).
