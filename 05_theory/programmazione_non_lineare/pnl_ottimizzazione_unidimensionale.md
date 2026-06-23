---
type: theory-note
topic: programmazione-non-lineare
status: consolidated
sources:
  - raw_assets/Programmazione Non Lineare/PNL 1D.pdf
reliability: official
---

# Ottimizzazione Non Lineare Unidimensionale (1D)

L'ottimizzazione unidimensionale si occupa di trovare i punti di massimo o minimo di una funzione reale di una singola variabile reale $f: \mathbb{R} \to \mathbb{R}$ su tutto l'asse reale o su un intervallo limitato.

---

## Condizioni di Ottimalità

Sia $f: \mathbb{R} \to \mathbb{R}$ due volte derivabile con continuità ($f \in C^2$).

### 1. Condizioni del Primo Ordine (Necessaria)
Se $x^*$ è un punto di ottimo locale interno (massimo o minimo) per $f(x)$, allora la derivata prima si annulla in $x^*$:
$$f'(x^*) = 0$$
I punti in cui $f'(x) = 0$ sono detti **punti stazionari** (o critici).

### 2. Condizioni del Secondo Ordine
Per determinare la natura del punto stazionario $x^*$:
- **Minimo locale**: se $f'(x^*) = 0$ e $f''(x^*) > 0$.
- **Massimo locale**: se $f'(x^*) = 0$ e $f''(x^*) < 0$.
- **Punto di flesso a tangente orizzontale**: se $f'(x^*) = 0$ e $f''(x^*) = 0$ (la natura richiede l'esame di derivate successive).

### 3. Ottimalità Globale e Convessità
Se la funzione possiede proprietà di convessità o concavità globali:
- Se $f(x)$ è **convessa** su tutto il suo dominio, ogni punto stazionario $x^*$ ($f'(x^*) = 0$) è un **minimo globale**.
- Se $f(x)$ è **concava** su tutto il suo dominio, ogni punto stazionario $x^*$ ($f'(x^*) = 0$) è un **massimo globale**.

---

## Algoritmi Risolutivi Numerici

In assenza di una soluzione analitica per l'equazione $f'(x) = 0$, si ricorre ad algoritmi iterativi che generano una successione di punti $\{x_k\}$ convergente alla soluzione ottima $x^*$.

Gli algoritmi principali si dividono in due classi:

### 1. Algoritmi Dicotomici (Metodo di Bisezione)
Operano riducendo progressivamente la dimensione di un intervallo di incertezza $[a, b]$ in cui si sa trovarsi lo zero della derivata prima $f'(x)$ (supponendo $f'(a) \cdot f'(b) < 0$).
- Si calcola il punto medio $x_m = \frac{a+b}{2}$.
- Si valuta il segno di $f'(x_m)$.
- Si restringe l'intervallo a $[a, x_m]$ o $[x_m, b]$.
- **Caratteristiche**: Convergenza garantita (lineare) per funzioni con derivata continua, ma lenta. Non richiede informazioni sulla derivata seconda.

### 2. Metodi di Approssimazione (Metodo di Newton 1D)
Utilizza l'approssimazione locale di Taylor al secondo ordine della funzione obiettivo (ovvero approssimazione lineare della derivata prima).
Ad ogni iterazione $k$, dato il punto corrente $x_k$, il punto successivo $x_{k+1}$ si ottiene azzerando l'approssimazione lineare di $f'(x)$ intorno a $x_k$:
$$f'(x) \approx f'(x_k) + f''(x_k)(x - x_k) = 0 \implies x_{k+1} = x_k - \frac{f'(x_k)}{f''(x_k)}$$
- **Caratteristiche**: Convergenza molto rapida (quadratica) se il punto iniziale $x_0$ è vicino alla soluzione e $f''(x) \ne 0$. Può non convergere o oscillare se l'inizializzazione è lontana dall'ottimo.

---

## Criteri di Arresto per Algoritmi Iterativi

A differenza dei problemi lineari (es. simplesso) che terminano in un numero finito di passi, gli algoritmi per PNL generano sequenze infinite. È necessario definire dei criteri di arresto:
1. **Norma del gradiente (derivata) prossima a zero**: $|f'(x_k)| < \epsilon$.
2. **Progresso minimo delle variabili**: $|x_{k+1} - x_k| < \epsilon_x$.
3. **Progresso minimo del valore obiettivo**: $|f(x_{k+1}) - f(x_k)| < \epsilon_f$.
4. **Numero massimo di iterazioni**: $k \ge N_{\text{max}}$.

---

## Collegamenti Correlati

- Metodo Dicotomico: [[pnl_metodo_bisezione|Metodo di Bisezione 1D]]
- Metodo di Approssimazione: [[pnl_metodo_newton_1d|Metodo di Newton 1D]]
- Analisi Comparativa: [[pnl_confronto_bisezione_newton|Confronto Bisezione vs Newton]]
- Estensione Multivariabile: [[pnl_ottimizzazione_non_vincolata_multivariabile|Ottimizzazione Non Vincolata Multivariabile]]

