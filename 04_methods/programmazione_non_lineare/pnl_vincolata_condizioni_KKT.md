---
type: method
topic: programmazione_non_lineare
status: active
reliability: official
---

# Condizioni KKT per PNL Vincolata

Le condizioni di Karush-Kuhn-Tucker (KKT) sono condizioni necessarie del primo ordine affinché un punto sia ottimo locale in un problema di ottimizzazione non lineare vincolata.

---

## Formulazione Standard e Segno dei Moltiplicatori

Per evitare errori con il segno dei moltiplicatori $\mu$, scrivere sempre il problema nella forma standard:

### Problema di Minimo
$$\begin{aligned}
\min \quad & f(x) \\
\text{s.t. } & g_i(x) = 0 \quad i = 1, \dots, m \\
& h_j(x) \le 0 \quad j = 1, \dots, p
\end{aligned}$$

Lagrangiana:
$$L(x, \lambda, \mu) = f(x) + \sum_{i=1}^m \lambda_i g_i(x) + \sum_{j=1}^p \mu_j h_j(x)$$

Sistema KKT:
1. **Stazionarietà**: $\nabla_x L(x, \lambda, \mu) = 0 \implies \nabla f(x) + \sum \lambda_i \nabla g_i(x) + \sum \mu_j \nabla h_j(x) = 0$
2. **Ammissibilità Primale**: $g_i(x) = 0, \quad h_j(x) \le 0$
3. **Ammissibilità Duale (Segno)**:
   $$\mu_j \ge 0 \quad j = 1, \dots, p$$
4. **Complementarità**:
   $$\mu_j h_j(x) = 0 \quad j = 1, \dots, p$$

---

### Problema di Massimo
Nello stile degli esercizi caricati, quando si cerca un massimo mantenedo la stessa struttura di Lagrangiana e vincoli $h_j(x) \le 0$:
$$\begin{aligned}
\max \quad & f(x) \\
\text{s.t. } & g_i(x) = 0 \\
& h_j(x) \le 0
\end{aligned}$$

Lagrangiana:
$$L(x, \lambda, \mu) = f(x) + \sum_{i=1}^m \lambda_i g_i(x) + \sum_{j=1}^p \mu_j h_j(x)$$

Sistema KKT:
1. **Stazionarietà**: $\nabla_x L(x, \lambda, \mu) = 0 \implies \nabla f(x) + \sum \lambda_i \nabla g_i(x) + \sum \mu_j \nabla h_j(x) = 0$
2. **Ammissibilità Primale**: $g_i(x) = 0, \quad h_j(x) \le 0$
3. **Ammissibilità Duale (Segno)**:
   $$\mu_j \le 0 \quad j = 1, \dots, p$$
4. **Complementarità**:
   $$\mu_j h_j(x) = 0 \quad j = 1, \dots, p$$

*Nota: I moltiplicatori $\lambda_i$ associati a vincoli di uguaglianza non hanno vincoli di segno (sono liberi in $\mathbb{R}$).*

---

## Procedura Risolutiva d'Esame

1. **Ricondurre i vincoli di disuguaglianza** alla forma standard $h_j(x) \le 0$. Se il vincolo originale è $A(x) \ge B$, riscriverlo come $B - A(x) \le 0$.
2. **Costruire la Lagrangiana** $L(x, \lambda, \mu)$.
3. **Impostare le equazioni di stazionarietà** derivando rispetto ad ogni variabile decisionale.
4. **Scrivere le relazioni di complementarità**: per ciascun vincolo $j$, si ha $\mu_j = 0$ (vincolo inattivo $h_j < 0$) oppure $h_j(x) = 0$ (vincolo attivo $\mu_j$ libero in segno, da filtrare poi con l'ammissibilità duale).
5. **Risolvere per casi attivi/inattivi** (vedi la procedura combinatoria in [[pnl_combinatoria_vincoli_attivi]]).
6. **Filtrare i punti trovati**: verificare se soddisfano l'ammissibilità primale e l'ammissibilità duale.
7. **Confronto dei valori**: valutare la funzione obiettivo $f(x)$ in tutti i punti ammissibili candidati per determinare il minimo o massimo globale.

---

## Esempio con Vincolo di Uguaglianza Geometrico (dall'Esercizio 1)

Trovare i punti di minimo e massimo globale di $f(x, y) = x^2 + y^2$ soggetti al vincolo $(x-1)^2 + (y-2)^2 = 20$.

1. **Lagrangiana** (vincolo di uguaglianza, $\lambda$ libero):
   $$L(x, y, \lambda) = x^2 + y^2 + \lambda ((x-1)^2 + (y-2)^2 - 20)$$
2. **Stazionarietà**:
   $$\begin{cases}
   \frac{\partial L}{\partial x} = 2x + 2\lambda(x-1) = 0 \implies x(1+\lambda) = \lambda \implies x = \frac{\lambda}{1+\lambda} \\
   \frac{\partial L}{\partial y} = 2y + 2\lambda(y-2) = 0 \implies y(1+\lambda) = 2\lambda \implies y = \frac{2\lambda}{1+\lambda}
   \end{cases}$$
   Notiamo che $y = 2x$.
3. **Sostituzione nel vincolo**:
   $$(x-1)^2 + (2x-2)^2 = 20 \implies (x-1)^2 + 4(x-1)^2 = 20 \implies 5(x-1)^2 = 20 \implies (x-1)^2 = 4$$
   Otteniamo due soluzioni per $x$:
   - $x - 1 = 2 \implies x = 3 \implies y = 6$.
     Da $x = \frac{\lambda}{1+\lambda}$: $3 = \frac{\lambda}{1+\lambda} \implies 3 + 3\lambda = \lambda \implies 2\lambda = -3 \implies \lambda = -1.5$.
   - $x - 1 = -2 \implies x = -1 \implies y = -2$.
     Da $x = \frac{\lambda}{1+\lambda}$: $-1 = \frac{\lambda}{1+\lambda} \implies -1 - \lambda = \lambda \implies 2\lambda = -1 \implies \lambda = -0.5$.

4. **Confronto**:
   I punti candidati sono $P_1 = (3, 6)$ e $P_2 = (-1, -2)$:
   - $f(P_1) = 3^2 + 6^2 = 45$.
   - $f(P_2) = (-1)^2 + (-2)^2 = 5$.
   Poiché la regione ammissibile è chiusa e limitata (una circonferenza) e la funzione è continua, per il teorema di Weierstrass esistono massimo e minimo globale:
   - **Minimo globale vincolato**: $P_2 = (-1, -2)$ con valore $f = 5$.
   - **Massimo globale vincolato**: $P_1 = (3, 6)$ con valore $f = 45$.

---

## Collegamenti Obsidian
- Classificazione Hessiana: [[pnl_non_vincolata_punti_stazionari_hessiana]]
- Analisi Combinatoria Vincoli: [[pnl_combinatoria_vincoli_attivi]]
- Esercizi KKT svolti: [[pnl_vincolata_kkt_esempi]]
