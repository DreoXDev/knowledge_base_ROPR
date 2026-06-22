---
materia: ROPR
area: Programmazione Lineare
tipo: teoria
fonte: Ricerca Operativa - Teoria del Simplesso - 23-24.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - simplesso
  - forma-aumentata
  - soluzioni-base
  - vertici
---

# Forma aumentata e soluzioni di base

Per poter risolvere un problema di Programmazione Lineare (PL) tramite metodi algebrici (come il simplesso tabellare), è necessario convertire il modello in **forma aumentata** (introducendo variabili di slack) e comprendere la relazione tra la geometria dei **vertici** e l'algebra delle **soluzioni di base**.

---

## 1. Definizione di Vertice

### Definizione Geometrica
> Un **vertice ammissibile** è una soluzione ammissibile che non giace su alcun segmento che connette altre due soluzioni ammissibili distinte della regione ammissibile.

*Esempi in Wyndor Glass Co.*:
- Punti come l'origine $(0,0)$, $(4,0)$ o $(2,6)$ sono vertici ammissibili poiché si trovano sugli angoli del poligono.
- Qualsiasi punto situato lungo i lati, ad esempio $(0,3)$ o $(2,3)$, giace sul segmento che unisce i vertici di estremità, quindi **non** è un vertice.

### Definizione Algebrica (Sistemi di Frontiera)
In uno spazio multidimensionale $\mathbb{R}^n$, la definizione geometrica non è operativa. Si adotta la caratterizzazione algebrica:

> In un problema di PL con $n$ variabili decisionali, ogni vertice è l'intersezione di $n$ iperpiani associati alle equazioni di frontiera del problema. Si ottiene quindi risolvendo un sistema di $n$ equazioni di frontiera linearmente indipendenti.

*Limitazioni e casi*:
- Non tutte le scelte di $n$ equazioni di frontiera producono un vertice ammissibile.
- Se la soluzione del sistema viola uno o più dei vincoli rimanenti (non inclusi nel sistema), si ha un **vertice non ammissibile**.
- Se le equazioni scelte sono incompatibili, il sistema non ammette soluzioni.

| Oggetto / Caso | Significato algebrico |
|---|---|
| **Equazione di frontiera** | Vincolo originario reso attivo sostituendo la disuguaglianza con l'uguaglianza ($=$). |
| **Vertice ammissibile** | Soluzione di un sistema di $n$ equazioni di frontiera che soddisfa tutti gli altri vincoli. |
| **Vertice non ammissibile** | Soluzione di un sistema di $n$ equazioni di frontiera che viola almeno un altro vincolo. |
| **Sistema senza soluzione** | Incompatibilità algebrica delle $n$ equazioni di frontiera selezionate. |
| **Degenerazione** | Caso in cui più di $n$ equazioni di frontiera sono attive nello stesso punto (il vertice è sovradeterminato). |

---

## 2. Forma Aumentata e Variabili di Slack

I vincoli di disuguaglianza $\le$ vengono convertiti in uguaglianze aggiungendo una **variabile di slack** ($s_i \ge 0$) che misura la differenza tra il termine noto e il membro sinistro del vincolo:
$$
\sum_{j=1}^n a_{ij}x_j \le b_i \implies \sum_{j=1}^n a_{ij}x_j + s_i = b_i \quad \text{con } s_i \ge 0
$$

### Classificazione delle Variabili
1. **Variabili Decisionali**: Le variabili originarie del modello ($x_1, \dots, x_n$).
2. **Variabili di Slack**: Le variabili introdotte per convertire le disuguaglianze ($s_1, \dots, s_m$).
3. **Variabili di Base**: Le $m$ variabili associate alle colonne della base lineare del sistema equivalente (risolte dal sistema).
4. **Variabili Non di Base**: Le $n - m$ variabili poste pari a zero per rimuovere i gradi di libertà del sistema.

---

## 3. Gradi di Libertà e Soluzioni di Base

Dato un sistema aumentato con $N$ variabili totali ($n$ decisionali + $m$ slack) e $m$ equazioni indipendenti:
- Il sistema possiede $N - m = n$ gradi di libertà.
- Poniamo $n$ variabili (variabili non di base) pari a zero.
- Risolviamo il sistema per le restanti $m$ variabili (variabili di base).

La soluzione risultante è detta **soluzione di base**.
- Se tutti i valori ottenuti per le variabili di base sono non negativi ($\ge 0$), è una **soluzione di base ammissibile** (SBA).
- Vi è una corrispondenza biunivoca tra ciascuna SBA e un **vertice ammissibile** della regione ammissibile.

### Origine come Soluzione Iniziale
Se tutti i vincoli funzionali sono di tipo $\le$ con termini noti non negativi ($b_i \ge 0$), ponendo le variabili decisionali pari a zero ($x_j = 0$, variabili non di base), otteniamo:
- Variabili di base: $s_i = b_i \ge 0$.
- Questa è la soluzione di base ammissibile iniziale e corrisponde geometricamente all'origine degli assi.
