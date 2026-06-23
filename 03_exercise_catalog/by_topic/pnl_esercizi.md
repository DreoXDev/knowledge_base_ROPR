---
type: exercise_catalog
topic: programmazione_non_lineare
status: active
sources: [20_esercizi_pnl.pdf, PNL_non_vincolata.pdf, PNL_vincolata.pdf, esercizi_riepilogo.pdf]
reliability: official
---

# Esercizi Programmazione Non Lineare (PNL)

Raccolta dei testi e delle soluzioni degli esercizi ufficiali di Programmazione Non Lineare (vincolata e non vincolata).

---

## 1. Ottimizzazione Non Vincolata (Punti Stazionari e Convessità)

### Esercizi da `PNL_non_vincolata.pdf`

#### Esercizio 1
*   **Funzione**: $f(x, y) = 2x^2 + y^2 - xy - 2x - 3y$.
*   **Quesiti**: Trovare i punti stazionari, studiare la convessità/concavità ed individuare gli ottimi locali/globali.
*   **Soluzione**:
    - Punti stazionari: $P^* = (1, 2)$.
    - Hessiana: $H_f = \begin{bmatrix} 4 & -1 \\ -1 & 2 \end{bmatrix} \implies \det(H_f) = 7 > 0$, $\text{tr}(H_f) = 6 > 0 \implies$ Definita positiva $\implies f$ convessa.
    - Ottimo: $P^* = (1, 2)$ è un minimo globale.
*   **Risoluzione Completa**: [[pnl_esercizi_non_vincolati|Esempio Non Vincolato Svolto 1]].

#### Esercizio 2
*   **Funzione**: $f(x, y) = x^3 + y^3 - 3xy$.
*   **Soluzione**:
    - Punti stazionari: $(0, 0)$ e $(1, 1)$.
    - Hessiana: $H_f = \begin{bmatrix} 6x & -3 \\ -3 & 6y \end{bmatrix}$.
    - Classificazione:
      - $H_f(0, 0) = \begin{bmatrix} 0 & -3 \\ -3 & 0 \end{bmatrix} \implies \det = -9 < 0 \implies$ Punto di sella.
      - $H_f(1, 1) = \begin{bmatrix} 6 & -3 \\ -3 & 6 \end{bmatrix} \implies \det = 27 > 0$, $\text{tr} = 12 > 0 \implies$ Minimo locale.

#### Esercizi 3-5
*   **Esercizio 3**: $f(x, y) = 2x^3 + y^3 - 3x^2 - 3y$.
    - Punti stazionari: $(0, 1)$ sella, $(0, -1)$ massimo locale, $(1, 1)$ minimo locale, $(1, -1)$ sella.
*   **Esercizio 4**: $f(x, y) = x^4 + x^2y + y^2 + 3$.
    - Punto stazionario: $(0, 0)$ minimo globale. (Nota: $H_f(0, 0)$ è semidefinita, ma lo studio globale conferma il minimo).
*   **Esercizio 5**: $f(x, y) = x^4 + y^4 - 2x^2 - 2y^2 + 4xy$.
    - Punti stazionari: $(0, 0)$ sella, $(\sqrt{2}, -\sqrt{2})$ minimo locale, $(-\sqrt{2}, \sqrt{2})$ minimo locale.

---

### Esercizi da `20_esercizi_pnl.pdf` (Locali)

#### Esercizi 1-10 (Ricerca massimi e minimi locali)
- **Esercizio 1**: $f(x, y) = 2x^3 - 2x^2y + 3x^2 - 2xy + 3y^2$.
  - Punti stazionari: $(0,0)$ minimo locale, $(4, 20/3)$ sella, $(-1, 0)$ sella.
- **Esercizio 2**: $f(x, y) = -2y^3 + xy^2 + x^2 - 2xy + 3y^2$.
  - Punti stazionari: $(0,0)$ minimo locale, $(1/2, 1)$ sella, $(-12, -4)$ sella.
- **Esercizio 3**: $f(x, y) = (3x-3y)^2 + (-y^2+3x-y)^2 + 1$.
  - Punti stazionari: $(0,0)$ minimo locale, $(2,2)$ minimo locale, $(5/6, 1)$ sella.
- **Esercizio 4**: $f(x, y) = x^3 - x^2y + 2x^2 - 3xy + y^2 - 2$.
  - Punti stazionari: $(0,0)$ sella, $(-1/2, -5/8)$ minimo locale, $(-1, -1)$ sella.
- **Esercizio 5**: $f(x, y) = 2y^3 + 2xy^2 + 3x^2 + 2xy - y^2 - 3$.
  - Punti stazionari: $(0,0)$ sella, $(-2, 2)$ sella, $(-2/3, 1)$ minimo locale.
- **Esercizio 6**: $f(x, y) = (-x-3y)^2 + (-y^2-x-y)^2 - 1$.
  - Punti stazionari: $(0,0)$ minimo locale, $(-6, 2)$ minimo locale, $(-5/2, 1)$ sella.
- **Esercizio 7**: $f(x, y) = x^3 - x^2y + 4x^2 + 4xy + 3y^2 - 2$.
  - Punti stazionari: $(0,0)$ minimo locale, $(16, 32)$ sella, $(-1, 5/6)$ sella.
- **Esercizio 8**: $f(x, y) = -4y^3 - 3xy^2 - x^2 + 2xy - 5y^2 + 2$.
  - Punti stazionari: $(0,0)$ massimo locale, $(-8, 8/3)$ sella, $(-1/2, -1/3)$ sella.
- **Esercizio 9**: $f(x, y) = (x-4y)^2 + (2x^2-3x-4y)^2 - 5$.
  - Punti stazionari: $(0,0)$ minimo locale, $(1,0)$ sella, $(2, 1/2)$ minimo locale.
- **Esercizio 10**: $f(x, y) = -x^3 + x^2y + 2x^2 - xy - y^2 - 4$.
  - Punti stazionari: $(0,0)$ sella, $(3,3)$ sella, $(3/2, 3/8)$ massimo locale.

---

## 2. Esercizi Algoritmici (Gradiente e Newton 1D e n-D)

### Esercizi da `PNL_non_vincolata.pdf`

#### Esercizio 6
*   **Problema**: $\max -x^2 - 2y^2 + 2xy + 2y$ a partire da $(0, 0)$.
*   **Gradiente**: 2 iterazioni con line search esatta $\implies x_1 = (0, 0.5)$, $x_2 = (0.5, 0.5)$.
*   **Newton**: 1 iterazione $\implies x_1 = (1, 1)$.
*   **Ottimo Globale**: $(1, 1)$ (funzione concava).
*   **Risoluzione Completa**: [[pnl_esercizi_non_vincolati|Esempio Non Vincolato Svolto 2]].

#### Esercizio 7
*   **Problema**: $\min x^2 + 2y^2 + xy - 12y$ a partire da $(-1, 2)$.
*   **Gradiente**: 1 iterazione con LS esatta $\implies \alpha_0 = 0.25$, $x_1 = (-1, 3.25)$.
*   **Newton**: 1 iterazione $\implies x_1 = (-12/7, 24/7) \approx (-1.71, 3.43)$.
*   **Ottimo Globale**: $x_1$ è il minimo globale (funzione quadratica convessa).

---

## 3. Ottimizzazione Vincolata (Condizioni KKT e Casi Combinatori)

### Esercizi da `PNL_vincolata.pdf`

#### Esercizio 1 (Vincoli di Uguaglianza)
*   **Problema**: $\min/\max x^2 + y^2$ s.t. $(x-1)^2 + (y-2)^2 = 20$.
*   **Soluzione**:
    - Punti KKT: $(-1, -2)$ con $\lambda = -1/2$, e $(3, 6)$ con $\lambda = -3/2$.
    - Ottimo: Minimo globale in $(-1, -2)$ con $f=5$. Massimo globale in $(3, 6)$ con $f=45$.
*   **Risoluzione Completa**: [[pnl_metodo_moltiplicatori_lagrange|Metodo Moltiplicatori di Lagrange]].

#### Esercizio 2 (Vincoli di Disuguaglianza)
*   **Problema**: $\min/\max f(x,y) = 4(x-1)^2 + (y-2)^2$ s.t. $x+y-2 \le 0, -x-1 \le 0, -y-1 \le 0$.
*   **Soluzione**:
    - Minimo globale: $P^* = (4/5, 6/5) = (0.8, 1.2)$ con $\mu_1 = 8/5 \ge 0$ (vincolo 1 attivo). Valore $f = 0.8$.
    - Massimo globale: $Q^* = (-1, -1)$ e $(3, -1)$ con valore $f = 25$ (moltiplicatori $\mu \le 0$).
*   **Risoluzione Completa**: [[pnl_esercizi_vincolati_kkt|Esempio Vincolato Svolto KKT]].

#### Esercizio 3 (Sella e Analisi Insiemi di Livello)
*   **Problema**: $\min/\max x+y$ s.t. $-x+4y-3 \le 0$, $x-y^2 \le 0$, $-x \le 0$.
*   **Soluzione**:
    - Punto KKT minimo ($\mu \ge 0$): $(9, 3)$ con $\mu_1 = 7/2, \mu_2 = 5/2, \mu_3 = 0$. Minimo locale confermato graficamente.
    - Punti KKT massimo ($\mu \le 0$): $(1/4, -1/2)$ con $\mu_2 = -1$, e $(1, 1)$ con $\mu_1 = -3/2, \mu_2 = -5/2$. Graficamente: $(1, 1)$ è massimo locale, $(1/4, -1/2)$ è un punto di sella.

---

### Esercizi da `20_esercizi_pnl.pdf` (Globali)

#### Esercizi 11-20 (Massimi e minimi globali con vincoli)
- **Esercizio 11**: $f(x,y) = y-x^2$ s.t. $-x^2-(y-1)^2+1 \le 0$, $-x \le 0$.
  - KKT $\mu \le 0$: $(0,0)$, $(\sqrt{3}/2, 1/2)$. KKT $\mu \ge 0$: $(0,2)$. Ottimi globali: nessuno.
- **Esercizio 12**: $f(x,y) = x^2+y^2$ s.t. $-x^2+y+4 \le 0$, $-x+y-2 \le 0$.
  - Minimi globali: $(\sqrt{14}/2, -1/2)$ e $(-\sqrt{14}/2, -1/2)$.
- **Esercizio 13**: $f(x,y) = x^2+(y-2)^2$ s.t. $x^2-1 \le 0$, $y^2-1 \le 0$.
  - Minimo globale: $(0,1)$ con $f=1$. Massimi globali: $(1, -1)$ e $(-1, -1)$ con $f=10$.
- **Esercizio 14**: $f(x,y) = (x-3)^2+(y-1)^2$ s.t. $-x \le 0, -y \le 0$.
  - Minimo globale: $(3,1)$ con $f=0$ (punto stazionario interno).
- **Esercizio 15**: $f(x,y) = (x+1)^2+y^2$ s.t. $x^2+4y^2-4 \le 0$.
  - Minimo globale: $(-1,0)$ con $f=0$ (punto stazionario interno). Massimo globale: $(2,0)$ con $f=9$.
- **Esercizio 16**: $f(x,y) = -x^2-(y-1)^2$ s.t. $x^2-y \le 0, y-4 \le 0$.
  - Minimi globali: $(2,4)$ e $(-2,4)$ con $f=-13$. Massimo globale: $(0,1)$ con $f=0$ (punto stazionario interno).
- **Esercizio 17**: $f(x,y) = x+y$ s.t. $-x^2-4y^2+4 \le 0, x^2+4y^2-16 \le 0$.
  - Minimo globale: $(-8/\sqrt{5}, -2/\sqrt{5})$. Massimo globale: $(8/\sqrt{5}, 2/\sqrt{5})$.
- **Esercizio 18**: $f(x,y) = (x-2)^2+(y-2)^2$ s.t. $-x^2-y^2+1 \le 0, x-4 \le 0$.
  - Minimo globale: $(2,2)$ con $f=0$ (punto stazionario interno).
- **Esercizio 19**: $f(x,y) = (x-1)^2+y^2$ s.t. $x^2+4y^2-8 \le 0, x^2-4 = 0$.
  - Minimo globale: $(2,0)$ con $f=1$. Massimi globali: $(-2, 1)$ e $(-2, -1)$ con $f=10$.
- **Esercizio 20**: $f(x,y) = (x-1)^2+(y-2)^2$ s.t. $x-y \le 0, -x-y \le 0$.
  - Minimo globale: $(1,2)$ con $f=0$ (punto stazionario interno).
