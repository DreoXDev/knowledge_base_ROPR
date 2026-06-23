---
type: solved_example
topic: programmazione_non_lineare
status: active
reliability: official
---

# Esercizi Svolti PNL Vincolata: Condizioni KKT (Esercizi 1-3)

Questo file raccoglie le soluzioni complete e strutturate degli Esercizi 1-3 estratti da `PNL_vincolata.pdf`. Gli esercizi coprono problemi vincolati con vincoli di uguaglianza e disuguaglianza, illustrando l'applicazione sistematica delle condizioni di Karush-Kuhn-Tucker (KKT).

---

## Esercizio 1 (Vincoli di Uguaglianza)

### Testo
Data la funzione $f(x, y) = x^2 + y^2$ e la regione ammissibile $\Omega$:
$$\Omega = \{(x, y) \in \mathbb{R}^2 : (x-1)^2 + (y-2)^2 = 20\}$$
1. Trovare i punti di minimo di $f$ su $\Omega$ utilizzando le condizioni KKT.
2. Trovare i punti di massimo di $f$ su $\Omega$ utilizzando le condizioni KKT.

### Soluzione
La regione $\Omega$ è una circonferenza di raggio $R = \sqrt{20}$ centrata in $(1, 2)$. Trattandosi di un insieme chiuso e limitato (compatto), per il Teorema di Weierstrass esistono sicuramente il massimo e il minimo globale vincolato.

Costruiamo la Lagrangiana con moltiplicatore $\lambda$ (libero in segno perché associato a un vincolo di uguaglianza):
$$L(x, y, \lambda) = x^2 + y^2 + \lambda ((x-1)^2 + (y-2)^2 - 20)$$

#### 1. Sistema KKT
$$\begin{cases}
\frac{\partial L}{\partial x} = 2x + 2\lambda(x-1) = 0 \implies x(1+\lambda) = \lambda \\
\frac{\partial L}{\partial y} = 2y + 2\lambda(y-2) = 0 \implies y(1+\lambda) = 2\lambda \\
(x-1)^2 + (y-2)^2 = 20
\end{cases}$$

#### 2. Risoluzione del sistema
- Se $\lambda = -1$, la prima equazione diventa $2x - 2x + 2 = 0 \implies 2 = 0$ (impossibile). Quindi $\lambda \neq -1$.
- Esplicitando $x$ e $y$ in funzione di $\lambda$:
  $$x = \frac{\lambda}{1+\lambda}, \quad y = \frac{2\lambda}{1+\lambda} \implies y = 2x$$
- Sostituiamo $y = 2x$ nel vincolo:
  $$(x-1)^2 + (2x-2)^2 = 20 \implies (x-1)^2 + 4(x-1)^2 = 20 \implies 5(x-1)^2 = 20 \implies (x-1)^2 = 4$$
  Quindi:
  $$x - 1 = \pm 2 \implies x = 3 \quad \text{oppure} \quad x = -1$$

##### Caso A: $x = 3 \implies y = 6$
Calcoliamo $\lambda$:
$$3 = \frac{\lambda}{1+\lambda} \implies 3 + 3\lambda = \lambda \implies 2\lambda = -3 \implies \lambda = -1.5$$
Otteniamo il punto candidato **$P_1 = (3, 6)$** con moltiplicatore $\lambda = -1.5$.
Valore obiettivo: $f(3, 6) = 3^2 + 6^2 = 45$.

##### Caso B: $x = -1 \implies y = -2$
Calcoliamo $\lambda$:
$$-1 = \frac{\lambda}{1+\lambda} \implies -1 - \lambda = \lambda \implies 2\lambda = -1 \implies \lambda = -0.5$$
Otteniamo il punto candidato **$P_2 = (-1, -2)$** con moltiplicatore $\lambda = -0.5$.
Valore obiettivo: $f(-1, -2) = (-1)^2 + (-2)^2 = 5$.

#### 3. Conclusione
Confrontando i valori:
- **Minimo globale vincolato**: $P_2 = (-1, -2)$ con valore ottimo $f = 5$.
- **Massimo globale vincolato**: $P_1 = (3, 6)$ con valore ottimo $f = 45$.

---

## Esercizio 2 (Vincoli di Disuguaglianza, Regione Compatta)

### Testo
Data la funzione $f(x, y) = 4(x-1)^2 + (y-2)^2$ e la regione ammissibile $\Omega$:
$$\Omega = \{(x, y) \in \mathbb{R}^2 : x+y-2 \le 0, \quad -x-1 \le 0, \quad -y-1 \le 0\}$$
1. Trovare i punti di minimo di $f$ su $\Omega$ utilizzando le condizioni KKT.
2. Trovare i punti di massimo di $f$ su $\Omega$ utilizzando le condizioni KKT.

### Soluzione
I tre vincoli lineari definiscono un triangolo con vertici $V_1 = (-1, 3)$, $V_2 = (3, -1)$ e $V_3 = (-1, -1)$. Trattandosi di un insieme compatto, per Weierstrass esistono sia il massimo che il minimo globale.

Riscriviamo i tre vincoli in forma standard $h_j(x, y) \le 0$:
- $h_1(x, y) = x+y-2 \le 0$
- $h_2(x, y) = -x-1 \le 0$
- $h_3(x, y) = -y-1 \le 0$

Lagrangiana:
$$L(x, y, \mu_1, \mu_2, \mu_3) = 4(x-1)^2 + (y-2)^2 + \mu_1(x+y-2) + \mu_2(-x-1) + \mu_3(-y-1)$$

Equazioni di stazionarietà:
$$\begin{cases}
8(x-1) + \mu_1 - \mu_2 = 0 \\
2(y-2) + \mu_1 - \mu_3 = 0
\end{cases}$$

Complementarità:
$$\mu_1(x+y-2) = 0, \quad \mu_2(-x-1) = 0, \quad \mu_3(-y-1) = 0$$

#### 1. Ricerca dei punti di Minimo ($\mu_j \ge 0$)
- **Caso $\mu_1 = \mu_2 = \mu_3 = 0$ (Vincoli inattivi)**:
  $$8(x-1) = 0 \implies x = 1, \quad 2(y-2) = 0 \implies y = 2$$
  Punto interno: $(1, 2)$. Verifichiamo l'ammissibilità primale:
  $$h_1(1, 2) = 1 + 2 - 2 = 1 \not\le 0 \quad (\text{Non ammissibile})$$
- **Caso $\mu_2 = \mu_3 = 0$, solo $h_1$ attivo ($x+y-2=0$)**:
  $$\begin{cases}
  8(x-1) + \mu_1 = 0 \implies \mu_1 = 8(1-x) \\
  2(y-2) + \mu_1 = 0 \implies \mu_1 = 2(2-y) \\
  y = 2-x
  \end{cases}$$
  Uguagliando: $8(1-x) = 2(2 - (2-x)) = 2x \implies 8 - 8x = 2x \implies 10x = 8 \implies x = 0.8 \implies y = 1.2$.
  Moltiplicatore: $\mu_1 = 8(1 - 0.8) = 1.6 \ge 0$ (ammissibilità duale soddisfatta).
  Ammissibilità primale per gli altri vincoli:
  $$h_2(0.8, 1.2) = -1.8 \le 0, \quad h_3(0.8, 1.2) = -2.2 \le 0 \quad (\text{Ammissibile})$$
  Otteniamo il candidato **$P^* = (0.8, 1.2)$** con valore $f(P^*) = 4(-0.2)^2 + (-0.8)^2 = 0.8$.

Tutti gli altri casi attivi a bordo o ai vertici producono moltiplicatori negativi.
Di conseguenza, il **minimo globale vincolato** è **$P^* = (0.8, 1.2)$** con valore $f = 0.8$.

#### 2. Ricerca dei punti di Massimo ($\mu_j \le 0$)
Analizzando sistematicamente le combinazioni di vincoli attivi per moltiplicatori non positivi $\mu_j \le 0$:
- **Caso solo $h_3$ attivo ($y = -1, \mu_1 = \mu_2 = 0$)**:
  $$8(x-1) = 0 \implies x = 1 \implies Q_1 = (1, -1)$$
  $\mu_3 = 2(-1-2) = -6 \le 0$. Ammissibile primale. Valore: $f(1, -1) = 9$.
- **Caso solo $h_2$ attivo ($x = -1, \mu_1 = \mu_3 = 0$)**:
  $$2(y-2) = 0 \implies y = 2 \implies Q_2 = (-1, 2)$$
  $\mu_2 = 8(-1-1) = -16 \le 0$. Ammissibile primale. Valore: $f(-1, 2) = 16$.
- **Caso $h_2$ e $h_3$ attivi (vertice $x = -1, y = -1$)**:
  $$Q_3 = (-1, -1)$$
  $\mu_2 = -16 \le 0$, $\mu_3 = -6 \le 0$. Ammissibile primale. Valore: $f(-1, -1) = 25$.
- **Caso $h_1$ e $h_3$ attivi (vertice $x = 3, y = -1$)**:
  $$Q_4 = (3, -1)$$
  $\mu_1 = -16 \le 0$, $\mu_3 = -22 \le 0$. Ammissibile primale. Valore: $f(3, -1) = 25$.
- **Caso $h_1$ e $h_2$ attivi (vertice $x = -1, y = 3$)**:
  $$Q_5 = (-1, 3)$$
  $\mu_1 = -2 \le 0$, $\mu_2 = -18 \le 0$. Ammissibile primale. Valore: $f(-1, 3) = 17$.

I **massimi globali vincolati** sono i punti **$Q_3 = (-1, -1)$** e **$Q_4 = (3, -1)$** con valore massimo ottimo $f = 25$.

---

## Esercizio 3 (Vincoli Non Lineari, Regione Non Limitata)

### Testo
Data la funzione $f(x, y) = x + y$ e la regione ammissibile $\Omega$:
$$\Omega = \{(x, y) \in \mathbb{R}^2 : -x+4y-3 \le 0, \quad x-y^2 \le 0, \quad -x \le 0\}$$
1. Trovare i punti di minimo di $f$ su $\Omega$ utilizzando le condizioni KKT.
2. Trovare i punti di massimo di $f$ su $\Omega$ utilizzando le condizioni KKT.

### Soluzione
La regione $\Omega$ non è limitata superiormente né inferiormente (infatti $y \to -\infty$ e $x \to +\infty$ sono ammessi). Poiché la funzione obiettivo è $f(x, y) = x+y$, allontanandosi verso l'alto-destra il valore diverge a $+\infty$ (nessun massimo globale) e verso il basso-sinistra diverge a $-\infty$ (nessun minimo globale).
Possiamo solo cercare punti stazionari di KKT candidati ad essere **ottimi locali**.

Vincoli in forma standard $h_j(x, y) \le 0$:
- $h_1(x, y) = -x+4y-3 \le 0$
- $h_2(x, y) = x-y^2 \le 0$
- $h_3(x, y) = -x \le 0$

Lagrangiana:
$$L(x, y, \mu_1, \mu_2, \mu_3) = x + y + \mu_1(-x+4y-3) + \mu_2(x-y^2) + \mu_3(-x)$$

Equazioni di stazionarietà:
$$\begin{cases}
1 - \mu_1 + \mu_2 - \mu_3 = 0 \\
1 + 4\mu_1 - 2y\mu_2 = 0
\end{cases}$$

#### 1. Ricerca dei Minimi Locali ($\mu_j \ge 0$)
Analizzando i casi, l'unica combinazione ammissibile per $\mu_j \ge 0$ è con $h_1$ e $h_2$ attivi:
- **Caso $h_1 = h_2 = 0$ ($y^2 - 4y + 3 = 0$)**:
  $$(y-1)(y-3) = 0 \implies y = 1 \quad \text{oppure} \quad y = 3$$
  - Sotto-caso $y = 3 \implies x = y^2 = 9$. Punto candidato **$P = (9, 3)$**.
    Calcolo moltiplicatori:
    $$\begin{cases} 1 - \mu_1 + \mu_2 = 0 \implies \mu_1 = 1 + \mu_2 \\ 1 + 4\mu_1 - 6\mu_2 = 0 \implies 1 + 4(1+\mu_2) - 6\mu_2 = 0 \implies 5 = 2\mu_2 \implies \mu_2 = 2.5 \end{cases}$$
    Da cui $\mu_1 = 3.5$. Poiché $\mu_1 = 3.5 \ge 0$ e $\mu_2 = 2.5 \ge 0$, le KKT per il minimo sono soddisfatte.
  - Sotto-caso $y = 1 \implies x = 1$. Punto $(1, 1)$.
    Calcolo moltiplicatori:
    $$\begin{cases} \mu_1 = 1 + \mu_2 \\ 1 + 4(1+\mu_2) - 2\mu_2 = 0 \implies 5 + 2\mu_2 = 0 \implies \mu_2 = -2.5 < 0 \end{cases}$$
    Violazione del segno per il minimo.

Disegnando le curve di livello, si verifica che **$P = (9, 3)$** è un punto di **minimo locale** (non globale).

#### 2. Ricerca dei Massimi Locali ($\mu_j \le 0$)
Analizzando i casi per $\mu_j \le 0$:
- **Caso $h_1 = h_2 = 0$ (vertici $y = 1 \implies x = 1$ e $y = 3 \implies x = 9$)**:
  - Per $Q_1 = (1, 1)$, i moltiplicatori ricavati sono $\mu_2 = -2.5 \le 0$ e $\mu_1 = -1.5 \le 0$. Le KKT per il massimo sono soddisfatte.
  - Per $Q_2 = (9, 3)$, i moltiplicatori sono positivi, quindi violati.
- **Caso solo $h_2$ attivo ($x = y^2, \mu_1 = \mu_3 = 0$)**:
  $$\begin{cases} 1 + \mu_2 = 0 \implies \mu_2 = -1 \le 0 \\ 1 - 2y\mu_2 = 0 \implies 1 - 2y(-1) = 0 \implies y = -0.5 \implies x = 0.25 \end{cases}$$
  Otteniamo il punto candidato **$Q_3 = (0.25, -0.5)$** con $\mu_2 = -1 \le 0$.
  Ammissibilità primale: $h_1(0.25, -0.5) = -0.25 - 2 - 3 = -5.25 \le 0$ (OK).

Disegnando gli insiemi di livello si rileva che:
- **$Q_1 = (1, 1)$** è un punto di **massimo locale**.
- **$Q_3 = (0.25, -0.5)$** è un **punto di sella** (nonostante soddisfi KKT per il massimo, l'analisi locale lungo il bordo mostra che in un intorno del punto esistono sia valori maggiori che minori, dovuti all'andamento della parabola).

---

## Collegamenti Obsidian
- Condizioni KKT teoriche: [[pnl_vincolata_condizioni_KKT]]
- Metodo combinatorio: [[pnl_combinatoria_vincoli_attivi]]
