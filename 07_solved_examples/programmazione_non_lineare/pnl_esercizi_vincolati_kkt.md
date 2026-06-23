---
type: solved_example
topic: programmazione_non_lineare
status: active
reliability: official
---

# Esercizi Svolti di Ottimizzazione Vincolata (KKT)

In questa sezione viene presentato un esercizio svolto completo e dettagliato sull'ottimizzazione non lineare vincolata tramite le condizioni di Karush-Kuhn-Tucker (KKT).

---

## Esercizio: Ricerca di Minimi e Massimi Globali Vincolati

### Testo
Data la funzione obiettivo:
$$f(x, y) = 4(x-1)^2 + (y-2)^2$$
e la regione ammissibile $\Omega$:
$$\Omega = \{(x, y) \in \mathbb{R}^2 : x+y-2 \le 0, \quad -x-1 \le 0, \quad -y-1 \le 0\}$$
a) Trovare i punti di minimo globale di $f$ su $\Omega$ utilizzando le condizioni KKT.
b) Trovare i punti di massimo globale di $f$ su $\Omega$ utilizzando le condizioni KKT.

---

### Soluzione Passo-Passo

#### 1. Analisi preliminare
La regione ammissibile $\Omega$ è definita dall'intersezione di tre semipiani:
1. $x + y \le 2$
2. $x \ge -1 \implies -x \le 1 \implies -x - 1 \le 0$
3. $y \ge -1 \implies -y \le 1 \implies -y - 1 \le 0$

L'intersezione di queste tre disuguaglianze lineari definisce un **triangolo** con vertici:
- $V_1 = (-1, 3)$ (intersezione di $x = -1$ e $x + y = 2$)
- $V_2 = (3, -1)$ (intersezione di $y = -1$ e $x + y = 2$)
- $V_3 = (-1, -1)$ (intersezione di $x = -1$ e $y = -1$)

La regione $\Omega$ è un insieme chiuso e limitato (compatto). Poiché la funzione obiettivo $f(x, y)$ è continua, per il **Teorema di Weierstrass** esistono sicuramente almeno un punto di minimo globale ed almeno un punto di massimo globale per $f$ su $\Omega$.

Riscriviamo i tre vincoli di disuguaglianza in forma standard $h_j(x, y) \le 0$:
- $h_1(x, y) = x + y - 2 \le 0$
- $h_2(x, y) = -x - 1 \le 0$
- $h_3(x, y) = -y - 1 \le 0$

Scriviamo la Lagrangiana generalizzata:
$$L(x, y, \mu_1, \mu_2, \mu_3) = 4(x-1)^2 + (y-2)^2 + \mu_1 (x + y - 2) + \mu_2 (-x - 1) + \mu_3 (-y - 1)$$

Calcoliamo le equazioni di stazionarietà (derivando rispetto a $x$ e $y$):
$$\frac{\partial L}{\partial x} = 8(x-1) + \mu_1 - \mu_2 = 0$$
$$\frac{\partial L}{\partial y} = 2(y-2) + \mu_1 - \mu_3 = 0$$

Le condizioni di complementarità degli scarti sono:
$$\mu_1 (x + y - 2) = 0$$
$$\mu_2 (-x - 1) = 0$$
$$\mu_3 (-y - 1) = 0$$

---

#### a) Ricerca dei punti di Minimo Globale ($\mu_j \ge 0$)
Per la minimizzazione, i moltiplicatori devono essere non negativi: $\mu_1, \mu_2, \mu_3 \ge 0$.
Analizziamo sistematicamente le combinazioni di vincoli attivi:

##### Caso 1: Tutti i vincoli inattivi ($\mu_1 = \mu_2 = \mu_3 = 0$)
Le condizioni di stazionarietà diventano:
$$\begin{cases}
8(x-1) = 0 \implies x = 1 \\
2(y-2) = 0 \implies y = 2
\end{cases}$$
Il punto stazionario interno è $P_0 = (1, 2)$.
Verifichiamo l'ammissibilità primale di $P_0$:
- $h_1(1, 2) = 1 + 2 - 2 = 1 \le 0$ (Falso!)
Il punto $P_0$ giace fuori dalla regione ammissibile $\Omega$. Caso scartato.

##### Caso 2: Solo $h_1$ attivo ($h_1 = 0 \implies x+y=2$, $\mu_2 = \mu_3 = 0$)
Il sistema è:
$$\begin{cases}
8(x-1) + \mu_1 = 0 \implies \mu_1 = -8(x-1) \\
2(y-2) + \mu_1 = 0 \implies \mu_1 = -2(y-2) \\
x + y = 2 \implies y = 2 - x
\end{cases}$$
Uguagliando le espressioni per $\mu_1$:
$$-8(x-1) = -2(y-2) \implies 4(x-1) = y - 2$$
Sostituiamo $y = 2 - x$:
$$4x - 4 = (2 - x) - 2 \implies 4x - 4 = -x \implies 5x = 4 \implies x = \frac{4}{5} = 0.8$$
Ricaviamo $y$:
$$y = 2 - \frac{4}{5} = \frac{6}{5} = 1.2$$
Calcoliamo il moltiplicatore $\mu_1$:
$$\mu_1 = -8\left(\frac{4}{5} - 1\right) = -8\left(-\frac{1}{5}\right) = \frac{8}{5} = 1.6$$
Verifichiamo l'ammissibilità di $P_1 = (0.8, 1.2)$:
- **Ammissibilità primale**:
  - $h_2(0.8, 1.2) = -0.8 - 1 = -1.8 \le 0$ (Vero)
  - $h_3(0.8, 1.2) = -1.2 - 1 = -2.2 \le 0$ (Vero)
- **Ammissibilità duale**:
  - $\mu_1 = 1.6 \ge 0$ (Vero)

Il punto $P_1 = (0.8, 1.2)$ soddisfa tutte le condizioni KKT per il minimo.
La valutazione della funzione obiettivo in $P_1$ fornisce:
$$f(0.8, 1.2) = 4(0.8 - 1)^2 + (1.2 - 2)^2 = 4(-0.2)^2 + (-0.8)^2 = 4(0.04) + 0.64 = 0.16 + 0.64 = 0.8$$

Analizzando gli altri casi a bordo o ai vertici (es. solo $h_2$ o $h_3$ attivi, o coppie attive), si verifica che i moltiplicatori violano il vincolo di segno ($\mu_j < 0$).
Ad esempio, se solo $h_2$ è attivo ($x = -1, \mu_1=\mu_3=0$):
$$8(-1-1) - \mu_2 = 0 \implies \mu_2 = -16 < 0$$ (violazione del segno per il minimo).

Conclusione minimo:
Il punto di **minimo globale** è $P^* = \left(\frac{4}{5}, \frac{6}{5}\right)$ con valore ottimo $f(P^*) = 0.8$.

---

#### b) Ricerca dei punti di Massimo Globale ($\mu_j \le 0$)
Per la massimizzazione, i moltiplicatori dei vincoli attivi devono essere non positivi: $\mu_1, \mu_2, \mu_3 \le 0$.
Andando ad analizzare i casi corrispondenti:

##### Caso A: Vincolo $h_3$ attivo in $y = -1$ ($\mu_1 = \mu_2 = 0$)
Il sistema è:
$$\begin{cases}
8(x-1) = 0 \implies x = 1 \\
2(y-2) - \mu_3 = 0 \implies \mu_3 = 2(y-2) \\
y = -1
\end{cases}$$
Otteniamo il punto $Q_1 = (1, -1)$.
Calcoliamo $\mu_3$:
$$\mu_3 = 2(-1-2) = -6 \le 0 \quad \text{(Vero)}$$
Verifichiamo l'ammissibilità primale di $Q_1$:
- $h_1(1, -1) = 1 - 1 - 2 = -2 \le 0$ (Vero)
- $h_2(1, -1) = -1 - 1 = -2 \le 0$ (Vero)
Il punto $Q_1 = (1, -1)$ soddisfa le KKT per il massimo. Valore obiettivo:
$$f(1, -1) = 4(1-1)^2 + (-1-2)^2 = 9$$

##### Caso B: Vincolo $h_2$ attivo in $x = -1$ ($\mu_1 = \mu_3 = 0$)
Il sistema è:
$$\begin{cases}
8(x-1) - \mu_2 = 0 \implies \mu_2 = 8(x-1) \\
2(y-2) = 0 \implies y = 2 \\
x = -1
\end{cases}$$
Otteniamo il punto $Q_2 = (-1, 2)$.
Calcoliamo $\mu_2$:
$$\mu_2 = 8(-1-1) = -16 \le 0 \quad \text{(Vero)}$$
Verifichiamo l'ammissibilità primale di $Q_2$:
- $h_1(-1, 2) = -1 + 2 - 2 = -1 \le 0$ (Vero)
- $h_3(-1, 2) = -2 - 1 = -3 \le 0$ (Vero)
Il punto $Q_2 = (-1, 2)$ soddisfa le KKT per il massimo. Valore obiettivo:
$$f(-1, 2) = 4(-1-1)^2 + (2-2)^2 = 16$$

##### Caso C: Vincoli $h_2$ e $h_3$ attivi contemporaneamente ($x = -1, y = -1$)
Questo corrisponde al vertice $Q_3 = (-1, -1)$.
Le equazioni di stazionarietà sono:
$$8(-1-1) - \mu_2 = 0 \implies \mu_2 = -16 \le 0 \quad \text{(Vero)}$$
$$2(-1-2) - \mu_3 = 0 \implies \mu_3 = -6 \le 0 \quad \text{(Vero)}$$
Verifichiamo l'ammissibilità primale di $Q_3$:
- $h_1(-1, -1) = -1 - 1 - 2 = -4 \le 0$ (Vero)
Il punto $Q_3 = (-1, -1)$ soddisfa le KKT per il massimo. Valore obiettivo:
$$f(-1, -1) = 4(-1-1)^2 + (-1-2)^2 = 4(4) + 9 = 25$$

##### Caso D: Vincoli $h_1$ e $h_3$ attivi contemporaneamente ($x + y = 2, y = -1 \implies x = 3$)
Questo corrisponde al vertice $Q_4 = (3, -1)$.
Le equazioni di stazionarietà sono:
$$8(3-1) + \mu_1 = 0 \implies 16 + \mu_1 = 0 \implies \mu_1 = -16 \le 0 \quad \text{(Vero)}$$
$$2(-1-2) + \mu_1 - \mu_3 = 0 \implies -6 - 16 - \mu_3 = 0 \implies \mu_3 = -22 \le 0 \quad \text{(Vero)}$$
Verifichiamo l'ammissibilità primale di $Q_4$:
- $h_2(3, -1) = -3 - 1 = -4 \le 0$ (Vero)
Il punto $Q_4 = (3, -1)$ soddisfa le KKT per il massimo. Valore obiettivo:
$$f(3, -1) = 4(3-1)^2 + (-1-2)^2 = 4(4) + 9 = 25$$

##### Caso E: Vincoli $h_1$ e $h_2$ attivi contemporaneamente ($x + y = 2, x = -1 \implies y = 3$)
Questo corrisponde al vertice $Q_5 = (-1, 3)$.
Le equazioni di stazionarietà sono:
$$8(-1-1) + \mu_1 - \mu_2 = 0 \implies -16 + \mu_1 - \mu_2 = 0$$
$$2(3-2) + \mu_1 = 0 \implies 2 + \mu_1 = 0 \implies \mu_1 = -2 \le 0 \quad \text{(Vero)}$$
Ricaviamo $\mu_2$:
$$\mu_2 = \mu_1 - 16 = -2 - 16 = -18 \le 0 \quad \text{(Vero)}$$
Verifichiamo l'ammissibilità primale di $Q_5$:
- $h_3(-1, 3) = -3 - 1 = -4 \le 0$ (Vero)
Il punto $Q_5 = (-1, 3)$ soddisfa le KKT per il massimo. Valore obiettivo:
$$f(-1, 3) = 4(-1-1)^2 + (3-2)^2 = 4(4) + 1 = 17$$

---

#### Valutazione finale per i massimi
I candidati stazionari KKT per il massimo (moltiplicatori $\mu \le 0$) forniscono i seguenti valori per la funzione obiettivo:
- $Q_1 = (1, -1) \implies f = 9$
- $Q_2 = (-1, 2) \implies f = 16$
- $Q_3 = (-1, -1) \implies f = 25$
- $Q_4 = (3, -1) \implies f = 25$
- $Q_5 = (-1, 3) \implies f = 17$

Conclusione massimo:
I punti di **massimo globale** sono $Q_3 = (-1, -1)$ e $Q_4 = (3, -1)$ con valore massimo $f = 25$.
*(I punti $Q_1, Q_2, Q_5$ rappresentano massimi locali vincolati).*
