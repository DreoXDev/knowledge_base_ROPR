---
type: flashcards
topic: programmazione_non_lineare
status: consolidated
sources:
  - raw_assets/AAA - La bibbia di RO.pdf
reliability: non-ufficiale
---

# Flashcard — Quiz PNL: Bisezione, Gradiente, Newton, KKT

---

## Q1: Direzione di discesa del metodo del gradiente
**D:** Qual è la direzione di discesa nel metodo del gradiente per un problema di minimizzazione?

**R:** $d_k = -\nabla f(x_k)$.
Per massimizzazione: $d_k = +\nabla f(x_k)$.

---

## Q2: Aggiornamento di Newton multivariabile
**D:** Come si calcola il nuovo punto nel metodo di Newton per minimizzazione in più variabili?

**R:** Si risolve $H_f(x_k) s_k = -\nabla f(x_k)$, poi $x_{k+1} = x_k + s_k$ (passo unitario).

---

## Q3: Condizione di complementarità KKT
**D:** Scrivi la condizione di complementarità KKT per un vincolo di disuguaglianza $h_j(x) \le 0$.

**R:** $\mu_j \cdot h_j(x) = 0$.
Significa: o $\mu_j = 0$ (vincolo inattivo) oppure $h_j(x) = 0$ (vincolo attivo).

---

## Q4: Segno dei moltiplicatori KKT per minimizzazione
**D:** Per un problema di **minimizzazione** con vincoli $h_j(x) \le 0$, che segno devono avere i moltiplicatori $\mu_j$?

**R:** $\mu_j \ge 0$.

---

## Q5: Bisezione — aggiornamento intervallo
**D:** Nella bisezione su $f'(x) = 0$: dopo aver calcolato $x_{k+1} = (a_k + b_k)/2$, come si aggiorna l'intervallo?

**R:** Se $f'(a_k) \cdot f'(x_{k+1}) < 0$: $b_{k+1} = x_{k+1}$.
Altrimenti: $a_{k+1} = x_{k+1}$.

---

## Q6: Newton su funzione quadratica — quante iterazioni?
**D:** Per una funzione quadratica con Hessiana costante e non singolare, quante iterazioni di Newton servono per raggiungere l'ottimo esatto?

**R:** **Una sola iterazione**, poiché Newton è esatto per funzioni quadratiche.

---

*Source:* `AAA - La bibbia di RO.pdf` (non ufficiale)
