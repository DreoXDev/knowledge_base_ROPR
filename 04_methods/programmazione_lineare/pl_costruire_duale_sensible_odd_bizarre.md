---
materia: ROPR
area: Programmazione Lineare
tipo: metodo
fonte: Ricerca Operativa - Teoria della Dualità.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - dualita
  - costruzione-duale
  - sensible-odd-bizarre
  - method-card
---

# METHOD CARD — Costruzione del Duale con il Metodo Sensible / Odd / Bizarre (SOB)

## Quando usarla

Usare questa card quando l'esercizio richiede di formulare il duale di un problema di Programmazione Lineare che **non è** in forma standard (cioè presenta vincoli di uguaglianza, variabili libere, o disuguaglianze invertite).

## Regole di Corrispondenza (SOB)

Le etichette descrivono il comportamento di variabili e vincoli:
- **Sensible** (Canonico/Sensato): Rispetta la convenzione naturale del tipo di ottimizzazione.
- **Odd** (Singolare/Uguaglianza): Uguaglianze per i vincoli, o assenza di vincoli di segno per le variabili.
- **Bizarre** (Anticanonico/Inusuale): Orientamento opposto alla convenzione naturale.

---

### Per un Primale di Massimo ($\max \implies \min$)

| Elemento Primale (MAX) | Tipo / Segno | Etichetta | Elemento Duale (MIN) | Segno / Tipo |
|---|---|---|---|---|
| **Vincolo $i$-esimo** | $\le$ | Sensible | **Variabile $y_i$** | $y_i \ge 0$ |
| | $=$ | Odd | | $y_i$ libera |
| | $\ge$ | Bizarre | | $y_i \le 0$ |
| **Variabile $x_j$** | $x_j \ge 0$ | Sensible | **Vincolo $j$-esimo** | $\ge$ |
| | $x_j$ libera | Odd | | $=$ |
| | $x_j \le 0$ | Bizarre | | $\le$ |

---

### Per un Primale di Minimo ($\min \implies \max$)

| Elemento Primale (MIN) | Tipo / Segno | Etichetta | Elemento Duale (MAX) | Segno / Tipo |
|---|---|---|---|---|
| **Vincolo $i$-esimo** | $\ge$ | Sensible | **Variabile $y_i$** | $y_i \ge 0$ |
| | $=$ | Odd | | $y_i$ libera |
| | $\le$ | Bizarre | | $y_i \le 0$ |
| **Variabile $x_j$** | $x_j \ge 0$ | Sensible | **Vincolo $j$-esimo** | $\le$ |
| | $x_j$ libera | Odd | | $=$ |
| | $x_j \le 0$ | Bizarre | | $\ge$ |

---

## Procedura Operativa Passo-Passo

1. **Invertire l'obiettivo**: Se il primale è MAX, il duale sarà MIN, e viceversa.
2. **Identificare le variabili duali**: Associare una variabile duale $y_i$ a ogni vincolo primale $i$. Determinare il segno di $y_i$ confrontando il vincolo primale con la colonna *Vincolo* nelle tabelle sopra.
3. **Scrivere la F.O. del duale**: I coefficienti sono i termini noti (RHS) dei vincoli primali.
4. **Scrivere i vincoli duali**:
   - Ogni variabile primale $x_j$ genera un vincolo duale.
   - I coefficienti del vincolo $j$-esimo sono la colonna $j$-esima della matrice dei coefficienti primali.
   - Il termine noto (RHS) del vincolo è il coefficiente $c_j$ nella F.O. del primale.
   - Il verso del vincolo duale ($\le$, $\ge$, o $=$) è determinato dal segno della variabile primale $x_j$ usando la tabella corrispondente.

---

## Esempio Operativo

**Primale (MAX):**
$$
\max Z = 2x_1 + 3x_2
$$
soggetto a:
$$
\begin{aligned}
(y_1) \quad x_1 + x_2 &\ge 4 \quad \text{(Vincolo } \ge \text{ in MAX } \implies \text{Bizarre } \implies y_1 \le 0\text{)} \\
(y_2) \quad 2x_1 - x_2 &= 5 \quad \text{(Vincolo } = \text{ in MAX } \implies \text{Odd } \implies y_2 \text{ libera)}
\end{aligned}
$$
con:
- $x_1 \ge 0$ (Variabile $\ge 0$ in MAX $\implies$ Sensible $\implies$ Vincolo $\ge$ in MIN)
- $x_2$ libera (Variabile libera in MAX $\implies$ Odd $\implies$ Vincolo $=$ in MIN)

**Duale risultante (MIN):**
$$
\min W = 4y_1 + 5y_2
$$
soggetto a:
$$
\begin{aligned}
y_1 + 2y_2 &\ge 2 \quad \text{(Corrisponde a } x_1\text{)} \\
y_1 - y_2 &= 3 \quad \text{(Corrisponde a } x_2\text{)}
\end{aligned}
$$
con $y_1 \le 0$ e $y_2$ libera.
