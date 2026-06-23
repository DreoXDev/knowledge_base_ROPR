---
type: method-card
topic: programmazione_lineare
status: consolidated
sources:
  - raw_assets/Domande aperte RO.pdf
reliability: non-ufficiale
---

# Method Card: Vertici Ammissibili e Soluzioni di Base

## Quando Usarla

Quando la domanda chiede di enunciare le proprietà dei **vertici ammissibili** di un problema PL, le proprietà di una **soluzione di base** (BFS), oppure il **numero massimo di soluzioni di base**.

---

## Proprietà dei Vertici Ammissibili

1. Se esiste un ottimo, esiste un ottimo in un vertice (grazie alla linearità di $f$).
2. Il poliedro ammissibile ha un numero finito di vertici.
3. Due vertici sono adiacenti se condividono $n-1$ vincoli attivi.
4. Il simplesso si muove tra vertici adiacenti migliorando $f$.
5. Ottimalità locale = ottimalità globale (per la linearità).

---

## Proprietà di una Soluzione di Base

Dato un problema in forma standard con $m$ vincoli e $n$ variabili totali:

1. Scegliere $m$ variabili linearmente indipendenti → matrice di base $B$ invertibile.
2. Variabili non di base: $x_N = 0$.
3. Variabili di base: $x_B = B^{-1}b$.
4. **BFS** (ammissibile): $x_B \ge 0$.
5. **Soluzione degenere**: $x_B \ge 0$ ma almeno un componente = 0.
6. Ogni BFS corrisponde a un vertice del poliedro.

---

## Numero Massimo di Soluzioni di Base

Problema originale: $n$ variabili, $m$ vincoli di disuguaglianza.
Forma aumentata: $n + m$ variabili, $m$ vincoli di uguaglianza.

Numero massimo di basi (non necessariamente ammissibili):
$$\binom{n+m}{m}$$

---

## Output da Esame

```
Una soluzione di base di un PL in forma standard (m vincoli, n variabili) è
definita da una scelta di m variabili di base (matrice B invertibile).
Le variabili non di base sono poste a zero; le variabili di base si ottengono
come x_B = B^{-1}b.

Una BFS (soluzione di base ammissibile) soddisfa x_B >= 0 e corrisponde a
un vertice del poliedro ammissibile.

Il numero massimo di basi, in forma aumentata con n+m variabili e m vincoli,
è C(n+m, m).
```

---

## Collegamento Pattern

→ [[Domande_aperte_dualita_simplesso]]
