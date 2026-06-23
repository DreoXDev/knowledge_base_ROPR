---
type: solved-example
topic: programmazione_non_lineare
status: consolidated
sources:
  - raw_assets/Programmazione Non Lineare/esercizi_riepilogo.pdf
reliability: official
---

# Esercizi Svolti: Riepilogo Generale PL, PLI e PNL

Questa nota riporta la risoluzione passo-passo e dettagliata dei 4 esercizi dell'asset di riepilogo `esercizi_riepilogo.pdf`, che rappresenta la struttura tipica di un compito d'esame scritto.

---

## Esercizio 1: Cartiera e Rete di Distribuzione (Formulazione PL)

### Testo
Tre stabilimenti produttivi ($S_1, S_2, S_3$) producono settimanalmente al massimo 125, 180 e 170 album. Quattro punti vendita ($P_1, P_2, P_3, P_4$) richiedono almeno 100, 150, 50 e 75 album. Costi di spedizione: 0,3 Euro/km per album.
Distanze stabilimenti-punti vendita:
-   $S_1$: P1=20, P2=25, P3=15, P4=5
-   $S_2$: P1=12, P2=14, P3=18, P4=30
-   $S_3$: P1=19, P2=11, P3=40, P4=12

### a) Formulazione del Modello Base
Definiamo le **variabili decisionali**:
$x_{ij} = \text{quantità di album spediti dallo stabilimento } S_i \text{ al punto vendita } P_j \text{ alla settimana, con } i \in \{1,2,3\}, j \in \{1,2,3,4\}$.

Calcoliamo i **costi unitari di trasporto** ($c_{ij} = 0.3 \times d_{ij}$ Euro/album):
-   $c_{11} = 6.0$, $c_{12} = 7.5$, $c_{13} = 4.5$, $c_{14} = 1.5$
-   $c_{21} = 3.6$, $c_{22} = 4.2$, $c_{23} = 5.4$, $c_{24} = 9.0$
-   $c_{31} = 5.7$, $c_{32} = 3.3$, $c_{33} = 12.0$, $c_{34} = 3.6$

**Modello di Programmazione Lineare**:
$$
\begin{aligned}
\min \quad & Z = \sum_{i=1}^3 \sum_{j=1}^4 c_{ij} x_{ij} \\
\text{s.t. } & \sum_{j=1}^4 x_{1j} \le 125 \quad \text{(capacità } S_1\text{)} \\
& \sum_{j=1}^4 x_{2j} \le 180 \quad \text{(capacità } S_2\text{)} \\
& \sum_{j=1}^4 x_{3j} \le 170 \quad \text{(capacità } S_3\text{)} \\
& \sum_{i=1}^3 x_{i1} \ge 100 \quad \text{(domanda } P_1\text{)} \\
& \sum_{i=1}^3 x_{i2} \ge 150 \quad \text{(domanda } P_2\text{)} \\
& \sum_{i=1}^3 x_{i3} \ge 50 \quad \text{(domanda } P_3\text{)} \\
& \sum_{i=1}^3 x_{i4} \ge 75 \quad \text{(domanda } P_4\text{)} \\
& x_{ij} \ge 0 \quad \forall i, j
\end{aligned}
$$

### b) Modifiche Richieste
1.  **Capacità non utilizzata di $S_2$ minore o uguale a 20**:
    La capacità inutilizzata è data dalla capacità totale meno quella spedita:
    $$180 - \sum_{j=1}^4 x_{2j} \le 20 \implies \sum_{j=1}^4 x_{2j} \ge 160$$
2.  **Distanza complessiva di $S_1$ inferiore al 50% di quella degli altri due stabilimenti**:
    La distanza complessiva coperta dai veicoli da $S_1$ è $\sum_{j=1}^4 d_{1j}x_{1j}$. Riscrivendo linearmente:
    $$\sum_{j=1}^4 d_{1j} x_{1j} \le 0.5 \left( \sum_{j=1}^4 d_{2j} x_{2j} + \sum_{j=1}^4 d_{3j} x_{3j} \right)$$
    ovvero:
    $$20x_{11} + 25x_{12} + 15x_{13} + 5x_{14} \le 0.5 \left( 12x_{21} + \dots + 30x_{24} + 19x_{31} + \dots + 12x_{34} \right)$$

---

## Esercizio 2: Zaino 0/1 (Branch and Bound in Ampiezza)

### Testo
$$\max \quad Z = 9x_1 + 8x_2 + 7x_3 + 6x_4 + 3x_5$$
$$\text{s.t. } 2x_1 + 3x_2 + 5x_3 + 4x_4 + 9x_5 \le 12$$
$$x_i \in \{0, 1\} \quad \forall i$$

### Svolgimento
Ordiniamo le variabili per efficienza $v_i/p_i$:
$x_1 (4.5) > x_2 (2.67) > x_4 (1.5) > x_3 (1.4) > x_5 (0.33)$.
Le variabili sono già ordinate: $[x_1, x_2, x_4, x_3, x_5]$.

#### Albero di Enumerazione (Visita in Ampiezza)
-   **Nodo 0 (Radice)**: Rilassamento continuo:
    $x_1=1, x_2=1, x_4=1$ (peso accumulato $9$). Peso residuo $3$.
    Inseriamo la frazione di $x_3$: $x_3 = 3/5 = 0.6$.
    Soluzione: $x = (1, 1, 0.6, 1, 0) \implies Z_{rel} = 9 + 8 + 4.2 + 6 = 27.2$.
    Bound intero per massimo: $UB_0 = \lfloor 27.2 \rfloor = 27$. Incumbent corrente $Z_I = -\infty$.
    *Branching su $x_3$ (variabile frazionaria)*.

-   **Nodo 1 ($x_3 = 0$)**: Sotto-problema: peso max 12.
    $x_1=1, x_2=1, x_4=1$ (peso residuo $3$). $x_5 = 3/9 = 1/3$.
    Soluzione: $x = (1, 1, 0, 1, 1/3) \implies Z_{rel} = 24$. Bound: $UB_1 = 24$.
-   **Nodo 2 ($x_3 = 1$)**: Sotto-problema: peso max $12 - 5 = 7$.
    $x_1=1, x_2=1$ (peso residuo $2$). $x_4 = 2/4 = 0.5$.
    Soluzione: $x = (1, 1, 1, 0.5, 0) \implies Z_{rel} = 27$. Bound: $UB_2 = 27$.

-   **Nodo 3 ($x_3 = 0, x_5 = 0$)**: Sotto-problema dal Nodo 1.
    $x_1=1, x_2=1, x_4=1$ (peso totale $9 \le 12$).
    Soluzione intera! $x^* = (1, 1, 0, 1, 0) \implies Z = 23$.
    Aggiorniamo incumbent: $Z_I = 23$. Potato per interezza.
-   **Nodo 4 ($x_3 = 0, x_5 = 1$)**: Sotto-problema dal Nodo 1: peso max $12 - 9 = 3$.
    $x_1=1, x_2=1/3$.
    Soluzione: $x = (1, 1/3, 0, 0, 1) \implies Z_{rel} = 14.67 < Z_I = 23$. Potato per dominanza.
-   **Nodo 5 ($x_3 = 1, x_4 = 0$)**: Sotto-problema dal Nodo 2: peso max $7$.
    $x_1=1, x_2=1, x_5=2/9$.
    Soluzione: $x = (1, 1, 1, 0, 2/9) \implies Z_{rel} = 24.67$. Bound: $UB_5 = 24$.
-   **Nodo 6 ($x_3 = 1, x_4 = 1$)**: Sotto-problema dal Nodo 2: peso max $7 - 4 = 3$.
    $x_1=1, x_2=1/3$.
    Soluzione: $x = (1, 1/3, 1, 1, 0) \implies Z_{rel} = 24.67$. Bound: $UB_6 = 24$.

-   **Nodo 7 ($x_3 = 1, x_4 = 0, x_5 = 0$)**: Sotto-problema dal Nodo 5: peso max $7$.
    $x_1=1, x_2=1$. Soluzione intera! $x = (1, 1, 1, 0, 0) \implies Z = 24$.
    Aggiorniamo incumbent: $Z_I = 24$. Potato per interezza.
-   **Nodo 8 ($x_3 = 1, x_4 = 0, x_5 = 1$)**: Sotto-problema dal Nodo 5: peso max $7 - 9 = -2$. Inammissibile.
-   **Nodo 9 ($x_3 = 1, x_4 = 1, x_2 = 0$)**: Sotto-problema dal Nodo 6: peso max $3$.
    $x_1=1, x_5=1/9 \implies Z_{rel} = 22.33 < Z_I = 24$. Potato per dominanza.
-   **Nodo 10 ($x_3 = 1, x_4 = 1, x_2 = 1$)**: Sotto-problema dal Nodo 6: peso max $3 - 3 = 0$.
    $x_1=0, x_5=0 \implies x = (0, 1, 1, 1, 0)$ intero, $Z = 21 < Z_I = 24$. Potato per dominanza.

### Conclusione
Tutti i nodi sono chiusi. L'ottimo globale intero è $x^* = (1, 1, 1, 0, 0)$ con valore ottimo $Z^* = 24$.

---

## Esercizio 3: PNL Non Vincolata (Gradiente e Newton)

### Testo
$$\min_{x, y \in \mathbb{R}^2} \quad f(x, y) = x^2 + 2y^2 - xy - 3x - 2y$$
Punto di partenza: $A = (3, 3)$.

### a) Iterazione del Gradiente con Line Search Esatta
1.  **Gradiente**: $\nabla f(x, y) = \begin{bmatrix} 2x - y - 3 \\ 4y - x - 2 \end{bmatrix} \implies \nabla f(3, 3) = \begin{bmatrix} 0 \\ 7 \end{bmatrix}$.
2.  **Direzione**: $d_0 = -\nabla f(3, 3) = \begin{bmatrix} 0 \\ -7 \end{bmatrix}$.
3.  **Punto parametrico**: $x(\alpha) = A + \alpha d_0 = \begin{bmatrix} 3 \\ 3 - 7\alpha \end{bmatrix}$.
4.  **Sostituzione e line search**:
    $$\phi(\alpha) = 3^2 + 2(3-7\alpha)^2 - 3(3-7\alpha) - 3(3) - 2(3-7\alpha) = 98\alpha^2 - 49\alpha - 6$$
    $$\phi'(\alpha) = 196\alpha - 49 = 0 \implies \alpha_0 = 0.25$$
5.  **Nuovo punto**: $P_G = (3, 3 - 7(0.25)) = (3, 1.25) = (3, \frac{5}{4})$.

### b) Iterazione del Metodo di Newton
1.  **Matrice Hessiana**: $H_f(x, y) = \begin{bmatrix} 2 & -1 \\ -1 & 4 \end{bmatrix}$ (costante).
2.  **Sistema per la direzione**: $H_f s_0 = -\nabla f(A)$
    $$\begin{bmatrix} 2 & -1 \\ -1 & 4 \end{bmatrix} \begin{bmatrix} s_x \\ s_y \end{bmatrix} = \begin{bmatrix} 0 \\ -7 \end{bmatrix} \implies \begin{cases} s_y = 2s_x \\ 7s_x = -7 \end{cases} \implies s_0 = \begin{bmatrix} -1 \\ -2 \end{bmatrix}$$
3.  **Nuovo punto**: $P_N = A + s_0 = (3 - 1, 3 - 2) = (2, 1)$.

### c) Verifica di Minimo Locale
Poiché l'Hessiana ha $\det(H) = 7 > 0$ e $\text{tr}(H) = 6 > 0$, la matrice $H_f$ è definita positiva su tutto $\mathbb{R}^2$, quindi la funzione è strettamente convessa.
-   Nel punto di Newton $P_N(2, 1)$, il gradiente è $\nabla f(2, 1) = \begin{bmatrix} 4-1-3 \\ 4-2-2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$. Poiché è stazionario e $H \succ 0$, **$P_N$ è un punto di minimo locale (e globale)**.
-   Nel punto del gradiente $P_G(3, 1.25)$, il gradiente è $\nabla f(3, 1.25) = \begin{bmatrix} 1.75 \\ 0 \end{bmatrix} \neq \begin{bmatrix} 0 \\ 0 \end{bmatrix}$. Poiché non è stazionario, **$P_G$ non è un punto di minimo locale**.

---

## Esercizio 4: PNL Vincolata (Condizioni KKT)

### Testo
$$\min \quad f(x, y) = x^2 + (y - 5)^2$$
$$\text{s.t. } x^2 - y \le 0, \quad x + y - 2 \le 0$$

### Svolgimento
1.  **Forma standard dei vincoli**: $h_1(x, y) = x^2 - y \le 0$, $h_2(x, y) = x + y - 2 \le 0$.
2.  **Lagrangiana**: $L(x, y, \mu_1, \mu_2) = x^2 + (y - 5)^2 + \mu_1(x^2 - y) + \mu_2(x + y - 2)$.
3.  **Sistema KKT**:
    $$\begin{cases} 2x + 2\mu_1 x + \mu_2 = 0 \quad (1) \\ 2(y - 5) - \mu_1 + \mu_2 = 0 \quad (2) \\ \mu_1(x^2 - y) = 0 \quad (3) \\ \mu_2(x + y - 2) = 0 \quad (4) \\ \mu_1, \mu_2 \ge 0, \quad h_1, h_2 \le 0 \end{cases}$$

#### Analisi dei Casi
-   **Caso 1: $\mu_1 = \mu_2 = 0$ (Vincoli inattivi)**
    Da $(1),(2)$: $(0,5)$ $\implies h_2(0,5) = 3 > 0$ (non ammissibile).
-   **Caso 2: $h_1 = 0, \mu_2 = 0$ (Solo $h_1$ attivo)**
    $y = x^2 \implies \mu_1 = 2(x^2-5)$.
    Da $(1)$: $2x(1 + 2(x^2 - 5)) = 0 \implies 2x(2x^2 - 9) = 0$.
    -   $x = 0 \implies y = 0 \implies \mu_1 = -10 < 0$ (scartato).
    -   $x = \pm \frac{3}{\sqrt{2}} \implies y = 4.5 \implies x + y - 2 = \pm\frac{3}{\sqrt{2}} + 2.5 > 0$ (non ammissibile).
-   **Caso 3: $h_2 = 0, \mu_1 = 0$ (Solo $h_2$ attivo)**
    $y = 2 - x \implies \mu_2 = 10 - 2(2-x) = 6 + 2x$.
    Da $(1)$: $2x + 6 + 2x = 0 \implies 4x = -6 \implies x^* = -1.5 \implies y^* = 3.5$.
    Moltiplicatore: $\mu_2^* = 3 \ge 0$ (valido).
    Verifica $h_1$: $(-1.5)^2 - 3.5 = 2.25 - 3.5 = -1.25 \le 0$ (valido).
    Punto valido: $P^* = (-1.5, 3.5)$ con $\mu_1^*=0, \mu_2^*=3$.
-   **Caso 4: $h_1 = 0, h_2 = 0$ (Entrambi attivi)**
    $x^2 + x - 2 = 0 \implies x = 1$ o $x = -2$.
    -   $x = 1 \implies y = 1 \implies 2\mu_1 + \mu_2 = -2 \implies$ impossibile per moltiplicatori non negativi.
    -   $x = -2 \implies y = 4 \implies \mu_2 = 4 + 4\mu_1$. Da $(2)$: $2(-1) - \mu_1 + 4 + 4\mu_1 = 0 \implies 3\mu_1 = -2 < 0$ (scartato).

### Conclusione
L'unica soluzione KKT valida è $P^* = (-1.5, 3.5)$ con valore ottimo $f(P^*) = 4.5$, che rappresenta il minimo globale.

Vedi anche:
- [[pnl_vincolata_kkt_globali]]
- [[MC_PL_modello_trasporto]]
- [[MC_PLI_branch_and_bound_zaino]]
