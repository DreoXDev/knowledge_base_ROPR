---
type: method-card
topic: programmazione_lineare
status: consolidated
sources:
  - raw_assets/Domande aperte RO.pdf
reliability: non-ufficiale
---

# Method Card: Dualità Forte e Debole

## Quando Usarla

Quando la domanda chiede di enunciare i teoremi di dualità, la relazione tra primale e duale, o di verificare l'ottimalità tramite dualità.

---

## Setup

**Primale** (P): $\max c^Tx$ s.t. $Ax \le b$, $x \ge 0$

**Duale** (D): $\min b^Ty$ s.t. $A^Ty \ge c$, $y \ge 0$

---

## Dualità Debole

Per ogni $x$ ammissibile per (P) e ogni $y$ ammissibile per (D):
$$c^Tx \le b^Ty$$

**Corollario**: se $c^Tx_0 = b^Ty_0$ per alcune soluzioni ammissibili $x_0$, $y_0$ → entrambe sono ottimali.

---

## Dualità Forte

Se (P) ha soluzione ottima finita $x^*$, allora (D) ha soluzione ottima finita $y^*$ e:
$$c^Tx^* = b^Ty^*$$

---

## Relazioni Primale-Duale

| (P) | (D) |
|---|---|
| Ottimo finito | Ottimo finito (stesso valore) |
| Illimitato | Inammissibile |
| Inammissibile | Inammissibile o illimitato |

**Il duale del duale è il primale.**

---

## Output da Esame

```
Dualità debole: per ogni x primale ammissibile e y duale ammissibile,
  c^Tx <= b^Ty  (per max primale).
Il valore duale fornisce un upper bound al valore primale.

Dualità forte: se il primale (max) ha ottimo finito x*, anche il duale (min)
  ha ottimo finito y* e c^Tx* = b^Ty*.
Equivalentemente: x* e y* sono entrambi ottimi <==> ammissibili +
  stessa funzione obiettivo.
```

---

## Collegamento Pattern

→ [[Domande_aperte_dualita_simplesso]]
→ [[PL_dualita_teoria]]
