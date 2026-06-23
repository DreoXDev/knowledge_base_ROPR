---
type: exam-pattern
topic: programmazione_lineare
status: consolidated
sources:
  - raw_assets/AAA - La bibbia di RO.pdf
reliability: non-ufficiale
---

# Quiz PL — Analisi di Sensitività da Tableau

## Riconoscimento

Segnali nella traccia:
- "analisi di sensitività"
- "tableau finale del simplesso"
- "intervallo ammissibile di variazione"
- "$c_i$", "$b_i$", "$\Delta$"

---

## Lettura del Tableau Finale

Dal tableau finale si leggono:
- **Base corrente** $\mathcal{B}$: variabili con colonna identità.
- **Soluzione corrente** $\bar{x}_B = B^{-1}b$ (colonna RHS).
- **Costi ridotti** $\bar{c}_j = c_j - c_B^T B^{-1} A_j$ (riga obiettivo, escluse le variabili di base).
- **Matrice $B^{-1}$**: leggibile nelle colonne delle variabili di slack originali.

---

## Caso 1 — Variazione di $b_i$ (Termine Noto)

Si vuole trovare l'intervallo di $\Delta$ tale che la **base rimanga ammissibile** dopo la perturbazione $b \to b + \Delta e_i$.

La soluzione di base diventa:
$$x_B(\Delta) = B^{-1}b + \Delta \cdot B^{-1}e_i = \bar{b} + \Delta \cdot d$$

Condizione di ammissibilità:
$$x_B(\Delta) \ge 0 \quad \Longrightarrow \quad \bar{b}_k + \Delta \cdot d_k \ge 0 \quad \forall k$$

Si risolve il sistema di disequazioni in $\Delta$ e si prende l'intersezione degli intervalli.

---

## Caso 2 — Variazione di $c_j$ (Coefficiente Obiettivo)

**Se $x_j$ è fuori base**: il costo ridotto è $\bar{c}_j(\Delta) = \bar{c}_j + \Delta$. Per mantenere l'ottimalità (massimo: $\bar{c}_j \le 0$, minimo: $\bar{c}_j \ge 0$) si impone il segno corretto.

**Se $x_j$ è in base**: la variazione $\Delta$ modifica la riga obiettivo di tutte le variabili. I costi ridotti diventano $\bar{c}_k(\Delta) = \bar{c}_k - \Delta \cdot (B^{-1}A)_{j,k}$. Si impone che tutti i costi ridotti mantengano il segno di ottimalità.

---

## Procedura Rapida

1. Leggere base corrente e RHS dal tableau.
2. Capire se la variazione riguarda $c_i$ o $b_i$.
3. Scrivere la condizione di mantenimento (ammissibilità o ottimalità).
4. Risolvere le disequazioni in $\Delta$.
5. Confrontare l'intervallo ottenuto con le opzioni della domanda.

---

## Errori Frequenti

- ❌ Usare la procedura per $b_i$ quando varia $c_i$, o viceversa.
- ❌ Sbagliare il segno dei costi ridotti per la condizione di ottimalità.
- ❌ Non considerare tutte le variabili di base nella variazione di $c_j$ in base.
- ❌ Dimenticare che la variazione deve mantenere la **base corrente** ottima/ammissibile.

---

## Template Risposta da Esame

```
Base corrente: {x_i, x_j, ...}
Soluzione corrente: x_B = [...]

Variazione di [c_k / b_k] con Delta:

[Condizione di ammissibilità / ottimalità]:
  riga 1: [...] + Delta * [...] >= 0  =>  Delta [>=/<= ...]
  riga 2: [...] + Delta * [...] >= 0  =>  Delta [>=/<= ...]

Intervallo ammissibile: Delta in [a, b]
```

---

## Collegamento Method Card

→ [[MC_PL_analisi_sensitivita_da_tableau]]
