---
type: theory-note
topic: riepilogo_generale
status: consolidated
sources:
  - raw_assets/Domande aperte RO.pdf
reliability: non-ufficiale
---

# Domande Aperte — Risposte Modello Sintetiche

Risposte concise e pronte per l'esame alle domande più probabili.

> Fonte: rielaborazione professionale di `Domande aperte RO.pdf` validata con slide ufficiali.

---

## PL — Vertici e Soluzioni di Base

**Q: Proprietà dei vertici ammissibili di un PL?**

I vertici del poliedro ammissibile godono delle seguenti proprietà:
1. Se esiste un ottimo, esiste un ottimo in un vertice.
2. Il numero di vertici è finito.
3. Due vertici adiacenti condividono $n-1$ vincoli attivi.
4. Ottimalità locale = ottimalità globale (per la linearità).
5. Infiniti ottimi se la funzione obiettivo è parallela a una faccia ottima.

---

**Q: Proprietà di una soluzione di base ammissibile (BFS)?**

Dato il problema in forma standard ($m$ vincoli, $n$ variabili):
- Scegliere $m$ variabili di base (matrice $B$ invertibile).
- $x_N = 0$, $x_B = B^{-1}b$.
- **BFS**: $x_B \ge 0$ → corrisponde a un vertice del poliedro.

---

**Q: Numero massimo di soluzioni di base?**

In forma aumentata ($n+m$ variabili, $m$ vincoli di uguaglianza):
$$\binom{n+m}{m}$$

---

## PL — Dualità

**Q: Dualità debole?**

Per ogni $x$ primale ammissibile e $y$ duale ammissibile (max primale, min duale):
$$c^Tx \le b^Ty$$
Il duale è un upper bound al primale.

---

**Q: Dualità forte?**

Se il primale (max) ha ottimo finito $x^*$, anche il duale (min) ha ottimo finito $y^*$ e:
$$c^Tx^* = b^Ty^*$$

---

**Q: Relazioni primale-duale?**

| Primale | Duale |
|---|---|
| Ottimo finito | Ottimo finito (stesso valore) |
| Illimitato | Inammissibile |
| Inammissibile | Inammissibile o illimitato |

---

## PL — Complementarità

**Q: Condizioni di complementarità (complementary slackness)?**

Per primale $\max c^Tx$ s.t. $Ax \le b$, $x \ge 0$ e duale:

$$y_i^*(b_i - a_i^Tx^*) = 0 \quad \forall i \quad \text{(slack primale)}$$
$$x_j^*(a_j^Ty^* - c_j) = 0 \quad \forall j \quad \text{(slack duale)}$$

Slack primale positivo → $y_i^* = 0$. Variabile primale positiva → vincolo duale attivo.

---

## PL — Simplesso

**Q: Direzione di spostamento e incremento nel simplesso?**

**Direzione** (variabile entrante): $x_j$ con costo ridotto $\bar{c}_j = c_j - c_B^TB^{-1}A_j$ favorevole.

**Incremento** (variabile uscente): test del minimo rapporto:
$$\theta^* = \min_{i:\,d_i>0}\frac{\bar{x}_{B_i}}{d_i}$$

La variabile con rapporto minimo esce. Il simplesso si muove tra vertici adiacenti del poliedro.

---

## PNL — KKT

**Q: Condizioni KKT e a cosa servono?**

Dato $\min f(x)$ s.t. $g_i(x)=0$, $h_j(x)\le 0$, la Lagrangiana è:
$$L = f(x) + \sum_i\lambda_i g_i(x) + \sum_j\mu_j h_j(x)$$

Condizioni KKT:
1. **Stazionarietà**: $\nabla_x L = 0$
2. **Ammissibilità primale**: $g_i=0$, $h_j\le 0$
3. **Ammissibilità duale**: $\mu_j \ge 0$
4. **Complementarità**: $\mu_j h_j(x^*)=0$

Sono condizioni **necessarie** (sotto LICQ). Sufficienti se $f$ convessa e $h_j$ convessi.

---

## Reti — Modelli

**Q: Formulazione problema di trasporto (bilanciato)?**

$$\min \sum_{i,j}c_{ij}x_{ij} \quad \text{s.t.} \quad \sum_j x_{ij}=s_i, \quad \sum_i x_{ij}=d_j, \quad x_{ij}\ge 0$$

Offerta > domanda: aggiungere destinazione fittizia con $d_{j^*}=\sum s_i - \sum d_j$, costo 0.

---

**Q: Flusso a costo minimo?**

$$\min \sum_{(i,j)\in A}c_{ij}x_{ij} \quad \text{s.t.} \quad \sum_{(v,j)}x_{vj}-\sum_{(i,v)}x_{iv}=b_v \quad \forall v, \quad 0\le x_{ij}\le u_{ij}$$

---

## Metaeuristiche

**Q: Differenza crossover e mutazione?**

- **Crossover**: combina due genitori per produrre figli (intensificazione).
- **Mutazione**: modifica casuale di un individuo con probabilità bassa (diversificazione).

---

**Q: Temperatura e exploration/exploitation in SA?**

- $T$ alta → $p\approx 1$ → quasi tutto accettato → **exploration**.
- $T$ bassa → $p\approx 0$ → solo miglioramenti → **exploitation**.

Probabilità accettazione mossa peggiorativa (min): $p = \exp(-\Delta f/T)$.

---

**Q: Criterio di aspirazione in Tabu Search?**

Regola che consente di accettare una mossa vietata (tabu) se produce una soluzione **migliore del best globale** $x^*$.
