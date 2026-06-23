---
type: exam-pattern
topic: programmazione_lineare
status: consolidated
sources:
  - raw_assets/Domande aperte RO.pdf
reliability: non-ufficiale
---

# Pattern — Domanda Aperta: Dualità, Complementarità, Simplesso

## Riconoscimento

Segnali nella traccia:
- "dualità forte" / "dualità debole"
- "relazione tra primale e duale"
- "complementary slackness"
- "slack primale" / "slack duale"
- "vertici ammissibili"
- "soluzioni di base ammissibili"
- "direzione di spostamento nel simplesso"
- "variabile entrante / uscente"
- "numero massimo di soluzioni di base"

---

## Checklist per Rispondere

### Dualità
```
[ ] Specificare la coppia primale/duale (forma standard)
[ ] Enunciare dualità debole: c^Tx <= b^Ty per ogni coppia ammissibile (max primale)
[ ] Enunciare dualità forte: se ottimo finito, c^Tx* = b^Ty*
[ ] Indicare i 3 casi: ottimo/ottimo, illimitato/inammissibile, inammissibile/?
[ ] Il duale del duale è il primale
```

### Complementarità
```
[ ] Scrivere le due condizioni (slack primale × variabile duale = 0)
[ ] Spiegare: positiva primale => vincolo duale attivo
[ ] Spiegare: slack primale positivo => variabile duale nulla
[ ] Uso: verificare ottimalità senza simplesso
```

### Soluzioni di Base e Vertici
```
[ ] Definire variabili di base / non di base
[ ] x_B = B^{-1}b, x_N = 0
[ ] BFS: x_B >= 0
[ ] Numero massimo basi: C(n+m, m) in forma aumentata
[ ] Ogni BFS corrisponde a un vertice del poliedro
```

### Simplesso — Direzione e Incremento
```
[ ] Variabile entrante: costo ridotto c_bar_j favorevole
[ ] Direzione d = B^{-1} A_j
[ ] Test minimo rapporto: theta* = min {x_{B_i}/d_i : d_i > 0}
[ ] Variabile uscente: l'indice con theta* minimo
[ ] Interpretazione: movimento tra vertici adiacenti
```

---

## Template Risposta — Dualità Forte

```
Dato il primale max c^Tx s.t. Ax <= b, x >= 0
e il suo duale min b^Ty s.t. A^Ty >= c, y >= 0:

Dualità debole: per ogni x primale ammissibile e y duale ammissibile,
  c^Tx <= b^Ty.

Dualità forte: se il primale ha ottimo finito x*, anche il duale ha ottimo
  finito y* e c^Tx* = b^Ty*.

Corollario: se c^Tx = b^Ty e (x,y) sono ammissibili, entrambi sono ottimi.
```

---

## Template Risposta — Complementarità

```
Per primale max c^Tx s.t. Ax <= b, x >= 0 e duale min b^Ty:

Complementarità duale: x_j*(a_j^T y* - c_j) = 0 per ogni j
  => se x_j* > 0 allora il vincolo duale j è attivo (a_j^T y* = c_j)

Complementarità primale: y_i*(b_i - a_i^T x*) = 0 per ogni i
  => se lo slack primale i > 0 allora y_i* = 0

(x*, y*) ammissibili + entrambe le complementarità => entrambi ottimi.
```

---

## Errori da Evitare

- ❌ Invertire la direzione della dualità debole.
- ❌ Affermare che dualità debole implica ottimalità.
- ❌ Non distinguere tra BFS e soluzione di base non ammissibile.
- ❌ Scrivere complementarità senza specificare gli slack.
- ❌ Usare il test del minimo rapporto con $d_i \le 0$.

---

## Collegamento Method Cards

- [[MC_PL_vertici_soluzioni_base]]
- [[MC_PL_dualita_forte_debole]]
- [[MC_PL_simplesso_direzione_incremento]]
- [[PL_complementary_slackness]]
- [[PL_dualita_teoria]]
