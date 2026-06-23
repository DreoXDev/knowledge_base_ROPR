---
type: theory-note
topic: programmazione_lineare
status: consolidated
sources:
  - raw_assets/Domande aperte RO.pdf
reliability: non-ufficiale
---

# PL — Domande Aperte su Vertici, Basi, Dualità e Simplesso

Fonte: `raw_assets/Domande aperte RO.pdf` (rielaborato con validazione sulle fonti ufficiali)
Area: Programmazione Lineare
Prerequisiti: PL, forma standard, simplesso, dualità

---

## Vertici Ammissibili (D3)

**Domanda**: Quali sono le proprietà dei vertici ammissibili di un problema di PL?

**Risposta modello**:

Un problema di PL con regione ammissibile poliedrica e funzione obiettivo lineare ha le seguenti proprietà:

1. **Esistenza di un ottimo in un vertice**: se il problema ha soluzione ottima finita, esiste almeno un vertice ottimo.
2. **Numero finito di vertici**: il poliedro ammissibile ha un numero finito di vertici, dunque il simplesso termina in un numero finito di iterazioni (escludendo il cycling).
3. **Adiacenza tra vertici**: due vertici sono adiacenti se condividono $n-1$ vincoli attivi (in $\mathbb{R}^n$). Il simplesso si muove da un vertice al suo adiacente con migliore valore obiettivo.
4. **Ottimalità locale = ottimalità globale**: se un vertice non ha vertici adiacenti con valore obiettivo migliore, è ottimo globale (grazie alla linearità).
5. **Ottimi multipli**: se la funzione obiettivo è parallela a una faccia del poliedro e quella faccia è ottima, ogni punto su quella faccia è ottimo.

---

## Soluzioni di Base (D4)

**Domanda**: Quali sono le proprietà di una soluzione di base?

**Risposta modello**:

Dato un problema in **forma standard** con $m$ vincoli di uguaglianza e $n$ variabili:

1. Una **base** è un insieme di $m$ variabili linearmente indipendenti (la matrice di base $B$ è quadrata di ordine $m$ e invertibile).
2. Le **variabili non di base** sono poste uguali a zero.
3. Le **variabili di base** si ottengono risolvendo:
$$x_B = B^{-1}b$$
4. Una soluzione di base è **ammissibile** (BFS — Basic Feasible Solution) se $x_B \ge 0$.
5. Ogni BFS corrisponde a un vertice del poliedro ammissibile.
6. Una BFS è **degenere** se almeno una variabile di base ha valore zero.

---

## Numero Massimo di Soluzioni di Base (D8)

**Domanda**: Qual è il numero massimo di soluzioni di base?

**Risposta modello**:

Dato il problema originale con $n$ variabili e $m$ vincoli di disuguaglianza, in **forma aumentata** (con l'aggiunta di $m$ variabili di slack) si hanno $n+m$ variabili totali e $m$ vincoli di uguaglianza.

Il numero massimo di basi (non necessariamente ammissibili) è:
$$\binom{n+m}{m}$$

cioè il numero di modi di scegliere $m$ variabili di base tra le $n+m$ disponibili.

> **Nota**: il numero di BFS (ammissibili) è in generale molto minore, poiché molte basi producono $x_B < 0$.

---

## Dualità Debole e Forte (D5, D7)

**Domanda D5**: Che cosa afferma la dualità debole e la dualità forte?

**Risposta modello**:

Sia dato il primale $\max\; c^Tx$ s.t. $Ax \le b$, $x \ge 0$ e il suo duale $\min\; b^Ty$ s.t. $A^Ty \ge c$, $y \ge 0$.

**Dualità debole**: per ogni $x$ primale ammissibile e $y$ duale ammissibile:
$$c^Tx \le b^Ty$$
Il valore della funzione obiettivo duale è un **upper bound** per il primale (nel caso di max). Di conseguenza, se $c^Tx = b^Ty$ per un certo $x$ ammissibile e $y$ ammissibile, allora entrambi sono ottimi.

**Dualità forte**: se il primale (max) ha soluzione ottima finita $x^*$, allora anche il duale (min) ha soluzione ottima finita $y^*$ e i valori coincidono:
$$c^Tx^* = b^Ty^*$$

**Relazioni complète primale-duale** (D7):

| Primale | Duale |
|---|---|
| Ha soluzione ottima finita | Ha soluzione ottima finita (stesso valore) |
| È illimitato | È inammissibile |
| È inammissibile | È inammissibile o illimitato |

Inoltre: **il duale del duale è il primale**.

---

## Complementarità in PL (D9)

**Domanda**: Che cosa esprimono le condizioni di complementarità?

**Risposta modello**:

Le condizioni di complementarità (o complementary slackness) stabiliscono una relazione tra le variabili del primale e gli slack del duale, e viceversa.

Per un primale $\max\; c^Tx$ s.t. $Ax \le b$, $x \ge 0$ con duale $\min\; b^Ty$ s.t. $A^Ty \ge c$, $y \ge 0$:

**Complementarità primale**: se il vincolo primale $a_i^Tx < b_i$ (slack positivo), allora la variabile duale corrispondente $y_i = 0$:
$$y_i (b_i - a_i^T x) = 0 \quad \forall i$$

**Complementarità duale**: se la variabile primale $x_j > 0$, allora il vincolo duale corrispondente è attivo ($a_j^T y = c_j$):
$$x_j (a_j^T y - c_j) = 0 \quad \forall j$$

**Utilizzo**: una coppia $(x^*, y^*)$ di soluzioni ammissibili è ottima se e solo se soddisfa entrambe le condizioni di complementarità.

> Vedi anche: [PL_complementary_slackness.md](../10_rag/method_cards/PL_complementary_slackness.md)

---

## Direzione e Incremento nel Simplesso (D6)

**Domanda**: Come si determina la direzione di spostamento e l'incremento nel metodo del simplesso?

**Risposta modello**:

**Passo 1 — Direzione (variabile entrante)**:
Si sceglie una variabile **non di base** $x_j$ con **costo ridotto favorevole**:
- Per $\max$: si sceglie $x_j$ con $\bar{c}_j = c_j - c_B^T B^{-1} A_j > 0$ (criterio di ottimalità: tutti $\bar{c}_j \le 0$).
- Per $\min$: si sceglie $x_j$ con $\bar{c}_j < 0$.

Questa variabile "entra in base". La direzione di spostamento è $d = B^{-1} A_j$ (colonna aggiornata di $A_j$).

**Passo 2 — Incremento (variabile uscente)**:
Si aumenta $x_j$ da zero finché una variabile di base scende a zero. Si usa il **test del minimo rapporto**:
$$\theta^* = \min_{i:\, d_i > 0} \frac{\bar{x}_{B_i}}{d_i}$$

La variabile di base corrispondente all'indice minimo **esce dalla base**.

**Passo 3 — Aggiornamento**:
Si esegue un'operazione di pivot: il tableau viene aggiornato per riflettere la nuova base.

**Interpretazione geometrica**: il simplesso si sposta da un vertice del poliedro ammissibile al vertice adiacente con valore obiettivo migliore.

---

## Errori da Evitare

- ❌ Confondere BFS (soluzione di base ammissibile) con soluzione di base non ammissibile.
- ❌ Dire che ogni soluzione di base è ammissibile: non è vero se $x_B < 0$.
- ❌ Affermare che dualità debole implica $c^Tx = b^Ty$ — la dualità debole dà solo un'ineguaglianza.
- ❌ Usare formule di complementarità senza specificare lo slack primale o duale.
- ❌ Nel test del minimo rapporto: considerare anche i rapporti con $d_i \le 0$ (sono esclusi).

---

## Collegamenti

- [[MC_PL_vertici_soluzioni_base]]
- [[MC_PL_dualita_forte_debole]]
- [[MC_PL_simplesso_direzione_incremento]]
- [[PL_complementary_slackness]]
- [[PL_dualita_teoria]]
