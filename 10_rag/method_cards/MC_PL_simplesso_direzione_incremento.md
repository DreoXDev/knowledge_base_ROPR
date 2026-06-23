---
type: method-card
topic: programmazione_lineare
status: consolidated
sources:
  - raw_assets/Domande aperte RO.pdf
reliability: non-ufficiale
---

# Method Card: Direzione e Incremento nel Simplesso

## Quando Usarla

Quando la domanda chiede di descrivere come il simplesso sceglie la **variabile entrante** (direzione) e la **variabile uscente** (incremento), oppure di interpretare geometricamente un'iterazione.

---

## Passo 1 — Direzione (Variabile Entrante)

Si sceglie la variabile non di base $x_j$ con costo ridotto favorevole:
$$\bar{c}_j = c_j - c_B^T B^{-1} A_j$$

- **Massimizzazione**: si sceglie $x_j$ con $\bar{c}_j > 0$ (criterio di ottimalità: tutti $\bar{c}_j \le 0$).
- **Minimizzazione**: si sceglie $x_j$ con $\bar{c}_j < 0$ (criterio: tutti $\bar{c}_j \ge 0$).

La **direzione di spostamento** nel poliedro è data dalla colonna aggiornata:
$$d = B^{-1}A_j$$

---

## Passo 2 — Incremento (Variabile Uscente)

Si aumenta $x_j$ da zero finché una variabile di base scende a zero. Si usa il **test del minimo rapporto**:
$$\theta^* = \min_{i:\, d_i > 0} \frac{\bar{x}_{B_i}}{d_i}$$

La variabile di base corrispondente all'indice minimo **esce dalla base**.

> Se non esiste $d_i > 0$ → il problema è **illimitato**.

---

## Passo 3 — Aggiornamento (Pivot)

Il tableau viene aggiornato tramite operazioni elementari di riga per riflettere la nuova base.

---

## Interpretazione Geometrica

Il simplesso si muove **tra vertici adiacenti** del poliedro ammissibile (adiacenti = condividono $n-1$ vincoli attivi). Ogni iterazione migliora (o mantiene) la funzione obiettivo.

---

## Output da Esame

```
Passo direzione: si sceglie la variabile non di base x_j con costo ridotto
  favorevole (c_bar_j > 0 per max). La direzione di spostamento è d = B^{-1}A_j.

Passo incremento: si aumenta x_j fino al limite dato dal test del minimo rapporto:
  theta* = min {x_{B_i}/d_i : d_i > 0}
La variabile di base con rapporto minimo esce dalla base.

Interpretazione geometrica: il simplesso si sposta da un vertice al vertice
  adiacente con valore obiettivo migliore.
```

---

## Collegamento Pattern

→ [[Domande_aperte_dualita_simplesso]]
→ [[PL_teoria_simplesso]]
