---
type: exam-pattern
topic: programmazione_non_lineare
status: consolidated
sources:
  - raw_assets/AAA - La bibbia di RO.pdf
reliability: non-ufficiale
---

# Quiz PNL — Bisezione, Gradiente, Newton, KKT

## Riconoscimento

Segnali nella traccia:
- "bisezione", "intervallo", "punto medio", "criterio di arresto"
- "metodo del gradiente", "line search", "una iterazione"
- "Newton", "Hessiana", "$H_f$", "sistema lineare"
- "KKT", "vincoli attivi", "moltiplicatori", "complementarità"

---

## Bisezione 1D

**Scopo**: trovare $x^*$ t.c. $f'(x^*)=0$ (ottimo di $f$ in una variabile).

**Schema**:
1. Dato $[a_0, b_0]$ con $f'(a_0) \cdot f'(b_0) < 0$.
2. $x_{k+1} = \frac{a_k + b_k}{2}$.
3. Se $f'(x_{k+1}) = 0$ → stop.
4. Se $f'(a_k) \cdot f'(x_{k+1}) < 0$ → $b_{k+1} = x_{k+1}$; altrimenti $a_{k+1} = x_{k+1}$.
5. Ripetere fino a $|b_k - a_k| \le \varepsilon$.

**Tabella riassuntiva**:
| $k$ | $a_k$ | $b_k$ | $x_{k+1}$ | $f'(x_{k+1})$ | Nuovo intervallo |
|---|---|---|---|---|---|

---

## Metodo del Gradiente (Line Search Esatta)

**Schema** (minimizzazione):
1. $d_k = -\nabla f(x_k)$
2. $x(\alpha) = x_k + \alpha d_k$
3. $\phi(\alpha) = f(x_k + \alpha d_k)$; risolvi $\phi'(\alpha) = 0 \Rightarrow \alpha_k$
4. $x_{k+1} = x_k + \alpha_k d_k$

> Per massimizzazione: $d_k = +\nabla f(x_k)$.

**Checklist**:
```
[ ] Gradiente calcolato correttamente nel punto corrente?
[ ] Direzione corretta (segno di d_k)?
[ ] phi(alpha) sostituita e semplificata correttamente?
[ ] phi'(alpha) = 0 risolto per alpha?
[ ] Nuovo punto calcolato?
```

---

## Metodo di Newton Multivariabile

**Schema**:
1. Calcola $\nabla f(x_k)$ e $H_f(x_k)$.
2. Risolvi il sistema lineare:
$$H_f(x_k) \, s_k = -\nabla f(x_k)$$
3. $x_{k+1} = x_k + s_k$ (passo unitario).

> Se $f$ è quadratica e $H_f$ costante, Newton converge all'ottimo in **una sola iterazione**.

**Checklist**:
```
[ ] Hessiana calcolata correttamente?
[ ] Sistema Hs = -grad f impostato?
[ ] Sistema risolto senza invertire simbolicamente H?
[ ] Nuovo punto aggiornato con passo 1?
```

---

## Condizioni KKT

**Schema** (minimizzazione con $h_j(x) \le 0$):

1. **Forma standard**: $h_j(x) \le 0$ (moltiplicare per $-1$ se $\ge 0$).
2. **Lagrangiana**:
$$L = f(x) + \sum_j \mu_j h_j(x)$$
3. **Sistema KKT**:
$$\nabla_x L = 0, \quad h_j(x) \le 0, \quad \mu_j h_j(x) = 0, \quad \mu_j \ge 0$$
4. **Casi**: enumerare le $2^p$ combinazioni attivo/inattivo.
5. **Filtrare**: scartare $\mu_j < 0$ o ammissibilità violata.

**Checklist**:
```
[ ] Vincoli in forma standard h_j <= 0?
[ ] Lagrangiana costruita correttamente?
[ ] Stazionarietà: grad_x L = 0?
[ ] Complementarità: mu_j * h_j = 0?
[ ] Segno moltiplicatori: mu_j >= 0 (per min)?
[ ] Ogni caso controllato per ammissibilità primale?
```

---

## Errori Frequenti

- ❌ In gradiente: usare $+\nabla f$ per minimizzazione (direzione di salita invece di discesa).
- ❌ In Newton: invertire simbolicamente $H_f$ invece di risolvere il sistema.
- ❌ In KKT: dimenticare il controllo della complementarità.
- ❌ In KKT: accettare un candidato con $\mu_j < 0$ (per minimizzazione).
- ❌ In bisezione: non verificare il cambio di segno prima di aggiornare l'intervallo.

---

## Collegamento Method Cards

- [[MC_PNL_metodo_bisezione_1d]]
- [[MC_PNL_gradiente_line_search_esatta]]
- [[MC_PNL_newton_non_vincolata]]
- [[MC_PNL_KKT_generale]]
