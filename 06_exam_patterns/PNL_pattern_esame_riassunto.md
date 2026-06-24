---
type: exam-pattern
topic: programmazione_non_lineare
status: consolidated
---

# PNL — Riepilogo Pattern d'Esame

## Tabella Segnali → Metodo → File

| Segnale nella traccia | Metodo | Method Card / File |
|---|---|---|
| "massimi/minimi locali", "punti stazionari", "gradiente = 0" | PNL non vincolata | `MC_PNL_classificazione_hessiana.md` |
| "Hessiana", "matrice del secondo ordine", "convessa/concava" | Classificazione Hessiana | `MC_PNL_classificazione_hessiana.md` |
| "bisezione", "metodo dicotomico", "intervallo" | Bisezione 1D | `MC_PNL_metodo_bisezione_1d.md` |
| "Newton 1D", "formula Newton", "convergenza" | Newton 1D | `MC_PNL_metodo_newton_1d.md` |
| "gradiente", "steepest descent", "line search", "direzione di discesa" | Gradiente line search | `MC_PNL_gradiente_line_search_esatta.md` |
| "metodo di Newton", "direzione di Newton", "Hessiana H d = -grad" | Newton multivariabile | `MC_PNL_newton_non_vincolata.md` |
| "vincoli di uguaglianza", "moltiplicatori di Lagrange", "λ" | Lagrange | `MC_PNL_Lagrange_vincoli_uguaglianza.md` |
| "riduci una variabile", "sostituisci nel vincolo" | Riduzione variabili | `MC_PNL_riduzione_variabili_libere.md` |
| "KKT", "condizioni KKT", "vincoli attivi e inattivi" | KKT vincolata | `MC_PNL_KKT_vincoli_disuguaglianza.md` |
| "enumerazione vincoli attivi", "casi attivo/inattivo" | Combinatoria KKT | `MC_PNL_vincoli_attivi_complementarita.md` |
| "complementarità", "μ_j h_j = 0" | Complementarità KKT | `MC_PNL_KKT_generale.md` |

---

## PNL Non Vincolata

```
1. Calcola gradiente ∇f(x,y) = 0  →  punti stazionari
2. Calcola Hessiana H_f(x,y)
3. Studio convessità/concavità globale:
   det(H) < 0 → né convessa né concava
4. Classificazione locale di ogni punto stazionario:
   det(H) > 0, tr(H) > 0 → minimo
   det(H) > 0, tr(H) < 0 → massimo
   det(H) < 0             → sella
   det(H) = 0             → test inconclusivo
```

## PNL Numerica

```
Bisezione: [a,b], f'(m) cambio segno → aggiorna estremo. Tabella k, a, b, m, f'(m).
Newton 1D: x_{k+1} = x_k - f'(x_k)/f''(x_k). Tabella k, x_k, f', f'', x_{k+1}, |Δ|.
Gradiente:  d_k = -∇f(x_k), phi(α)=f(x_k+α*d_k), phi'(α)=0 → α*,  x_{k+1}=x_k+α*d_k.
Newton nD:  H(x_k)·d_k = -∇f(x_k), risolvere il sistema, x_{k+1}=x_k+d_k.
```

## PNL Vincolata

```
Lagrange (solo uguaglianze g_i=0):
  L = f + Σλ_i g_i,  ∇_x L = 0,  g_i = 0  →  candidati

KKT (uguaglianze + disuguaglianze h_j≤0):
  L = f + Σλ_i g_i + Σμ_j h_j
  1. Stazionarietà: ∇_x L = 0
  2. Ammissibilità primale: g_i=0, h_j≤0
  3. Ammissibilità duale: μ_j≥0 (min) o μ_j≤0 (max)
  4. Complementarità: μ_j h_j = 0
  → Enumera 2^p casi (attivo/inattivo per ogni h_j)
  → Filtra candidati non ammissibili
  → Confronta f nei candidati validi
```

## KKT

```
Per ogni candidato: tabella (Caso, Vincoli attivi, Punto, f, μ, Valido?)
Ottimo globale = candidato con f migliore tra quelli validi.
```

---

## Errori Frequenti

- ❌ Confondere det(H) > 0 + tr(H) > 0 con massimo (è minimo).
- ❌ Applicare Newton senza controllare che H sia non singolare.
- ❌ Non dichiarare esplicitamente l'intervallo iniziale nella bisezione.
- ❌ Segno errato dei moltiplicatori: μ_j ≥ 0 per min, μ_j ≤ 0 per max.
- ❌ Dimenticare di verificare l'ammissibilità primale dei candidati KKT.
- ❌ Dichiarare il test dell'Hessiana conclusivo quando det(H) = 0.

---

## Method Card di Riferimento Principale

→ [[MC_PNL_classificazione_hessiana]]
→ [[MC_PNL_KKT_vincoli_disuguaglianza]]
→ [[MC_PNL_Lagrange_vincoli_uguaglianza]]
