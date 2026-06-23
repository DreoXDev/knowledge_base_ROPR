---
type: solved-example
topic: programmazione_non_lineare
status: consolidated
sources:
  - raw_assets/Programmazione Non Lineare/20_esercizi_pnl.pdf
reliability: official
---

# Esercizi Svolti: Ottimizzazione Vincolata (KKT e Ottimi Globali)

Questa nota analizza nel dettaglio lo svolgimento degli esercizi 11-20 dell'asset `20_esercizi_pnl.pdf`, focalizzandosi sulle condizioni KKT per la ricerca di massimi e minimi globali vincolati.

---

## Convenzioni sui Moltiplicatori e Segni

Nei testi d'esame e nelle soluzioni degli esercizi 11-20, i candidati KKT vengono cercati risolvendo due sistemi distinti a seconda del segno prescritto per i moltiplicatori $\mu_j$ associati a vincoli in forma standard $h_j(x, y) \le 0$:
1.  **Candidati per Minimo ($\mu_j \ge 0$)**: La Lagrangiana è impostata come $L = f + \sum \mu_j h_j$. Per l'ammissibilità duale del problema di minimo, deve valere $\mu_j \ge 0$.
2.  **Candidati per Massimo ($\mu_j \le 0$)**: Mantenendo la stessa Lagrangiana, per la massimizzazione i moltiplicatori devono soddisfare $\mu_j \le 0$.

> [!IMPORTANT]
> Se la regione ammissibile $\Omega$ non è limitata (ossia non è compatta), la funzione obiettivo potrebbe decrescere o crescere all'infinito lungo direzioni ammissibili. In tal caso, massimi o minimi globali **non esistono** (inesistenza dell'ottimo globale).

---

## Analisi Dettagliata di Esercizi Scelti

### Esercizio 11
Trovare massimi e minimi globali di:
$$f(x, y) = y - x^2$$
sull'insieme:
$$\Omega = \{(x, y) \in \mathbb{R}^2 : -x^2 - (y - 1)^2 + 1 \le 0, -x \le 0\}$$

#### 1. Forma Standard dei Vincoli
-   $h_1(x, y) = -x^2 - (y-1)^2 + 1 \le 0$ (esterno di un cerchio unitario centrato in $(0,1)$).
-   $h_2(x, y) = -x \le 0$ (semipiano $x \ge 0$).

#### 2. Costruzione della Lagrangiana
$$L(x, y, \mu_1, \mu_2) = y - x^2 + \mu_1 \left( -x^2 - (y - 1)^2 + 1 \right) + \mu_2(-x)$$

#### 3. Sistema KKT
$$
\begin{cases}
\frac{\partial L}{\partial x} = -2x - 2\mu_1 x - \mu_2 = 0 \quad (1) \\
\frac{\partial L}{\partial y} = 1 - 2\mu_1(y - 1) = 0 \quad (2) \\
\mu_1 \left( -x^2 - (y - 1)^2 + 1 \right) = 0 \quad (3) \\
\mu_2 (-x) = 0 \quad (4)
\end{cases}
$$

#### 4. Risoluzione per Casi Combinatori

-   **Caso A: Entrambi i vincoli inattivi ($\mu_1 = \mu_2 = 0$)**
    Da $(2)$ otteniamo $1 = 0$, impossibile. Nessun punto interno.

-   **Caso B: Solo $h_1$ attivo ($h_1 = 0, \mu_2 = 0$)**
    Da $(4)$ e $(1)$: $-2x - 2\mu_1 x = 0 \implies -2x(1 + \mu_1) = 0$.
    -   Se $x = 0$: dal vincolo $h_1 = 0 \implies -(y-1)^2 + 1 = 0 \implies (y-1)^2 = 1 \implies y = 0$ oppure $y = 2$.
        -   Punto $(0, 0)$: da $(2)$ si ha $1 - 2\mu_1(-1) = 0 \implies \mu_1 = -1/2 \le 0$.
        -   Punto $(0, 2)$: da $(2)$ si ha $1 - 2\mu_1(1) = 0 \implies \mu_1 = 1/2 \ge 0$.
    -   Se $\mu_1 = -1$: da $(2)$ si ha $1 + 2(y-1) = 0 \implies y = 1/2$. Sostituendo in $h_1 = 0$: $-x^2 - 1/4 + 1 = 0 \implies x^2 = 3/4 \implies x = \sqrt{3}/2$ (poiché $x \ge 0$).
        -   Punto $(\sqrt{3}/2, 1/2)$ con moltiplicatore $\mu_1 = -1 \le 0$.

-   **Caso C: Solo $h_2$ attivo ($x = 0, \mu_1 = 0$)**
    Da $(2)$ otteniamo $1 = 0$, impossibile.

-   **Caso D: Entrambi i vincoli attivi ($x = 0, h_1 = 0$)**
    Punti candidati: $(0,0)$ e $(0,2)$.
    -   Per $(0,0)$: da $(2)$ si ha $\mu_1 = -1/2$. Sostituendo in $(1)$: $0 - 0 - \mu_2 = 0 \implies \mu_2 = 0$.
    -   Per $(0,2)$: da $(2)$ si ha $\mu_1 = 1/2$. Sostituendo in $(1)$: $0 - 0 - \mu_2 = 0 \implies \mu_2 = 0$.

#### 5. Sintesi Candidati
-   **Moltiplicatori $\mu \le 0$**: $(0,0)$ e $(\sqrt{3}/2, 1/2)$.
-   **Moltiplicatori $\mu \ge 0$**: $(0,2)$.

#### 6. Esistenza degli Ottimi Globali
La regione $\Omega$ è illimitata (ad esempio, per $y \ge 2$, qualsiasi punto $(0, y)$ è ammissibile).
-   Lungo la direzione $(0, y)$ con $y \to +\infty$: la funzione obiettivo $f(0, y) = y \to +\infty$. Quindi **non esiste massimo globale**.
-   Lungo la direzione $(x, 0)$ con $x \to +\infty$: il punto è ammissibile per $x \ge 1$ (infatti $-x^2 - 1 + 1 = -x^2 \le 0$). La funzione $f(x, 0) = -x^2 \to -\infty$. Quindi **non esiste minimo globale**.

---

### Esercizio 15
Trovare massimi e minimi globali di:
$$f(x, y) = (x+1)^2 + y^2$$
sull'ellisse:
$$\Omega = \{(x, y) \in \mathbb{R}^2 : x^2 + 4y^2 - 4 \le 0\}$$

#### 1. Analisi Preliminare
La regione $\Omega$ è un'ellisse chiusa e limitata in $\mathbb{R}^2$ (regione compatta). Per Weierstrass, massimo e minimo globale esistono sicuramente.

#### 2. Lagrangiana
$$L(x, y, \mu) = (x+1)^2 + y^2 + \mu(x^2 + 4y^2 - 4)$$

#### 3. Sistema KKT
$$
\begin{cases}
\frac{\partial L}{\partial x} = 2(x+1) + 2\mu x = 0 \quad (1) \\
\frac{\partial L}{\partial y} = 2y + 8\mu y = 0 \implies 2y(1 + 4\mu) = 0 \quad (2) \\
\mu(x^2 + 4y^2 - 4) = 0 \quad (3)
\end{cases}
$$

#### 4. Risoluzione per Casi
-   **Caso A: Vincolo inattivo ($\mu = 0$)**
    Da $(1)$ e $(2)$: $x = -1, y = 0$.
    Verifica ammissibilità primale: $(-1)^2 + 4(0) - 4 = -3 \le 0$ (valido).
    Punto stazionario interno: $P_1 = (-1, 0)$ con moltiplicatore $\mu = 0$ (valido sia per $\mu \le 0$ che per $\mu \ge 0$).

-   **Caso B: Vincolo attivo ($x^2 + 4y^2 - 4 = 0$)**
    Da $(2)$: $y = 0$ oppure $\mu = -1/4$.
    -   Se $y = 0$: dal vincolo $x^2 = 4 \implies x = \pm 2$.
        -   Per $P_2 = (2, 0)$: da $(1)$ si ha $6 + 4\mu = 0 \implies \mu = -3/2 \le 0$.
        -   Per $P_3 = (-2, 0)$: da $(1)$ si ha $-2 - 4\mu = 0 \implies \mu = -1/2 \le 0$.
    -   Se $\mu = -1/4$: da $(1)$ si ha $2(x+1) - x/2 = 0 \implies 1.5x = -2 \implies x = -4/3$.
        Sostituendo nel vincolo: $16/9 + 4y^2 = 4 \implies 4y^2 = 20/9 \implies y^2 = 5/9 \implies y = \pm \sqrt{5}/3$.
        Punti: $P_4, P_5 = (-4/3, \pm \sqrt{5}/3)$ con moltiplicatore $\mu = -1/4 \le 0$.

#### 5. Classificazione
Valutiamo la funzione obiettivo $f(x, y) = (x+1)^2 + y^2$ sui candidati:
-   $f(P_1) = f(-1, 0) = 0$ (Minimo globale).
-   $f(P_2) = f(2, 0) = 9$ (Massimo globale).
-   $f(P_3) = f(-2, 0) = 1$.
-   $f(P_4) = f(P_5) = f(-4/3, \sqrt{5}/3) = (-1/3)^2 + 5/9 = 6/9 = 2/3$.

Conclusione:
-   **Minimo globale**: $(-1,0)$ con valore $0$.
-   **Massimo globale**: $(2,0)$ con valore $9$.

---

Vedi anche:
- [[pnl_vincolata_kkt_globali]]
- [[pnl_20_esercizi_catalogo]]
