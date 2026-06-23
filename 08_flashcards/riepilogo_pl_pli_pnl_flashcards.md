---
type: flashcards
topic: riepilogo_esame_pl_pli_pnl
status: consolidated
sources:
  - raw_assets/Programmazione Non Lineare/esercizi_riepilogo.pdf
reliability: official
---

# Flashcards: Riepilogo Esame PL / PLI / PNL

---

## Q1: Modello di Trasporto PL — Struttura Base
**D:** Come si formulano le variabili e i vincoli di un modello di trasporto con $m$ sorgenti e $n$ destinazioni?

**R:** Variabili $x_{ij} \ge 0$ = quantità da sorgente $i$ a destinazione $j$.
$$\min \sum_i \sum_j c_{ij} x_{ij}$$
- Capacità sorgente $i$: $\sum_j x_{ij} \le s_i$
- Domanda destinazione $j$: $\sum_i x_{ij} \ge d_j$

---

## Q2: Vincolo Percentuale Lineare
**D:** Come si linea il vincolo "la distanza coperta da $S_1$ deve essere ≤ 50% di quella degli altri stabilimenti"?

**R:** Senza prodotti tra variabili:
$$\sum_j d_{1j} x_{1j} \le 0.5 \left(\sum_j d_{2j} x_{2j} + \sum_j d_{3j} x_{3j}\right)$$
Il vincolo rimane lineare perché i $d_{ij}$ sono costanti note, non variabili.

---

## Q3: Branch and Bound Zaino — Bound Superiore
**D:** Come si calcola l'upper bound di un nodo in un problema zaino 0/1 con B&B?

**R:** Si risolve il **rilassamento continuo** del sotto-problema residuo. Le variabili vengono ordinate per rapporto valore/peso; si inserisce la variabile "frazionaria" che finisce per ultima nello zaino.
$$UB = \text{valore intero accumulato} + \frac{\text{capacità residua}}{\text{peso var. critica}} \times \text{valore var. critica}$$

---

## Q4: Potatura nel B&B
**D:** Quando si pota un nodo nel Branch and Bound (maximization)?

**R:** Un nodo viene potato in uno dei tre casi:
1. **Inammissibile**: sotto-problema infeasible.
2. **Dominanza**: $UB \le Z_I$ (bound non migliora l'incumbent).
3. **Interezza**: soluzione intera trovata; aggiorna $Z_I$ e pota.

---

## Q5: Gradiente con Line Search Esatta — Schema
**D:** Elenca i 4 passi di una iterazione del metodo del gradiente con line search esatta.

**R:**
1. $d_k = -\nabla f(x_k)$
2. $x(\alpha) = x_k + \alpha d_k$
3. $\phi(\alpha) = f(x_k + \alpha d_k)$ → risolvi $\phi'(\alpha) = 0$ → $\alpha_k$
4. $x_{k+1} = x_k + \alpha_k d_k$

---

## Q6: Metodo di Newton Multivariabile — Schema
**D:** Come si calcola la direzione di Newton $s_k$ in una iterazione?

**R:** Risolvi il sistema lineare:
$$H_f(x_k) \, s_k = -\nabla f(x_k)$$
Poi aggiorna $x_{k+1} = x_k + s_k$ (passo unitario).

---

## Q7: KKT Strategia per Vincoli di Disuguaglianza
**D:** Come si trovano i candidati KKT con $p$ vincoli di disuguaglianza?

**R:** Si analizzano tutti i $2^p$ casi di attivazione/disattivazione. Per ogni caso:
- Attivo ($h_i = 0$): sostituisce il vincolo come uguaglianza.
- Inattivo ($h_i \le 0$): impone $\mu_i = 0$.
Si scartano i casi con $\mu_i < 0$ o ammissibilità violata.

---

## Q8: Verifica Minimo Globale PNL
**D:** Come si verifica che un punto stazionario è minimo locale/globale in PNL non vincolata?

**R:**
- Calcola $H_f(x^*)$
- Se $H_f \succ 0$ (definita positiva, minori principali tutti > 0): **minimo locale**
- Se la funzione è convessa su tutto $\mathbb{R}^n$ (H definita positiva ovunque): **minimo globale**

---

*Source:* `esercizi_riepilogo.pdf` — Esercizi 1–4
