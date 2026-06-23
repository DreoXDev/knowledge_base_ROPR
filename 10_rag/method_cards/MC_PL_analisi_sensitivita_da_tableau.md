---
type: method-card
topic: programmazione_lineare
status: consolidated
sources:
  - raw_assets/AAA - La bibbia di RO.pdf
reliability: non-ufficiale
---

# Method Card: Analisi di Sensitività da Tableau Finale

## Quando Usarla

Quando la traccia fornisce un tableau finale del simplesso e chiede di determinare l'intervallo di variazione ammissibile di un coefficiente ($c_i$ o $b_i$) che mantiene la base corrente **ottima** o **ammissibile**.

---

## Lettura del Tableau

Dal tableau finale si leggono:
- **Base $\mathcal{B}$**: variabili con colonna identità nella matrice.
- **$\bar{x}_B = B^{-1}b$**: colonna RHS (valori attuali delle variabili di base).
- **Costi ridotti $\bar{c}_j$**: riga obiettivo per le variabili fuori base.
- **$B^{-1}$**: visibile nelle colonne delle slack originali.

---

## Variazione di $b_i$ (Termine Noto)

Perturbazione: $b \to b + \Delta e_i$ (si varia il termine noto del vincolo $i$).

La soluzione di base diventa:
$$x_B(\Delta) = \bar{b} + \Delta \cdot d \quad \text{dove } d = B^{-1} e_i \text{ (colonna } i \text{ di } B^{-1}\text{)}$$

**Condizione di ammissibilità** (la base rimane ammissibile):
$$\bar{b}_k + \Delta \cdot d_k \ge 0 \quad \forall k$$

Per ogni riga $k$:
- Se $d_k > 0$: $\Delta \ge -\bar{b}_k / d_k$
- Se $d_k < 0$: $\Delta \le -\bar{b}_k / d_k$
- Se $d_k = 0$: nessun vincolo su $\Delta$ da questa riga

L'intervallo ammissibile è l'intersezione di tutti questi vincoli.

---

## Variazione di $c_j$ (Coefficiente Obiettivo)

### Caso: $x_j$ fuori base
Il costo ridotto diventa $\bar{c}_j(\Delta) = \bar{c}_j + \Delta$.
Per mantenere l'ottimalità (max: $\bar{c}_j \le 0$; min: $\bar{c}_j \ge 0$):
$$\bar{c}_j + \Delta \le 0 \quad \text{(max)} \implies \Delta \le -\bar{c}_j$$

### Caso: $x_j$ in base (variabile $j$ è la $r$-esima variabile di base)
La variazione $\Delta$ modifica i costi ridotti di tutte le variabili fuori base:
$$\bar{c}_k(\Delta) = \bar{c}_k - \Delta \cdot (B^{-1}A)_{r,k}$$
Si impone il segno di ottimalità per ogni $k$ fuori base.

---

## Errori Comuni

- ❌ Applicare la procedura per $b_i$ quando varia $c_i$, o viceversa.
- ❌ Dimenticare il segno di $d_k$ quando $d_k < 0$ (la disuguaglianza si inverte).
- ❌ Non considerare tutte le righe della base nel caso $b_i$.
- ❌ Non distinguere variabile di base da fuori base nel caso $c_j$.

---

## Collegamento Pattern

→ [[Quiz_PL_analisi_sensitivita]]
