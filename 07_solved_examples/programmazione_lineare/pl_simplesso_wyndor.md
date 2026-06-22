---
materia: ROPR
area: Programmazione Lineare
tipo: esempio-svolto
fonte: Ricerca Operativa - Metodo del Simplesso - 23-24.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - simplesso
  - simplesso-tabellare
  - esempio-svolto
  - wyndor-glass
---

# Esempio Svolto — Metodo del Simplesso su Wyndor Glass Co.

Questo esempio mostra l'applicazione passo-passo dell'algoritmo del simplesso tabellare per risolvere il modello classico di Wyndor Glass Co.

## Il Modello di Partenza

$$
\max Z = 3x_1 + 5x_2
$$

soggetto a:

$$
\begin{aligned}
(1) \quad x_1 &\le 4 \\
(2) \quad 2x_2 &\le 12 \\
(3) \quad 3x_1 + 2x_2 &\le 18
\end{aligned}
$$

con $x_1, x_2 \ge 0$.

## Passaggio 1: Forma Aumentata

Introduciamo le variabili di slack non negative $s_1, s_2, s_3$ per convertire i vincoli in equazioni:

$$
\begin{aligned}
(0) \quad Z - 3x_1 - 5x_2 &= 0 \\
(1) \quad x_1 + s_1 &= 4 \\
(2) \quad 2x_2 + s_2 &= 12 \\
(3) \quad 3x_1 + 2x_2 + s_3 &= 18
\end{aligned}
$$

con $x_1, x_2, s_1, s_2, s_3 \ge 0$.

---

## Passaggio 2: Risoluzione Tabellare

### Iterazione 0 (Tableau Iniziale)
La base iniziale è composta dalle variabili di slack $\{s_1, s_2, s_3\}$. Le variabili decisionali $\{x_1, x_2\}$ sono fuori base ($x_1=0, x_2=0$).

| Base | $Z$ | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $s_3$ | RHS | Rapporti |
|---|---|---|---|---|---|---|---|---|
| **$Z$** | 1 | -3 | -5 | 0 | 0 | 0 | 0 | |
| **$s_1$** | 0 | 1 | 0 | 1 | 0 | 0 | 4 | - |
| **$s_2$** | 0 | 0 | **2** | 0 | 1 | 0 | 12 | $12/2 = 6$ (min) |
| **$s_3$** | 0 | 3 | 2 | 0 | 0 | 1 | 18 | $18/2 = 9$ |

- **Variabile Entrante**: La variabile con il coefficiente più negativo in riga 0 è $x_2$ (coefficiente $-5$).
- **Variabile Uscente**: Calcolo dei rapporti minimi sulla colonna di $x_2$:
  - Riga $s_1$: coeff. nullo (ignorato)
  - Riga $s_2$: $12/2 = 6$
  - Riga $s_3$: $18/2 = 9$
  Il rapporto minimo è $6$. La variabile uscente è $s_2$.
- **Elemento Pivot**: $2$ (riga $s_2$, colonna $x_2$).

### Iterazione 1
Normalizziamo la riga pivot dividendo la riga $s_2$ per $2$. Successivamente azzeriamo la colonna di $x_2$ sulle altre righe:
- $R_2 \leftarrow R_2 / 2$
- $R_0 \leftarrow R_0 + 5 R_2$
- $R_3 \leftarrow R_3 - 2 R_2$

| Base | $Z$ | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $s_3$ | RHS | Rapporti |
|---|---|---|---|---|---|---|---|---|
| **$Z$** | 1 | -3 | 0 | 0 | 2.5 | 0 | 30 | |
| **$s_1$** | 0 | 1 | 0 | 1 | 0 | 0 | 4 | $4/1 = 4$ |
| **$x_2$** | 0 | 0 | 1 | 0 | 0.5 | 0 | 6 | - |
| **$s_3$** | 0 | **3** | 0 | 0 | -1 | 1 | 6 | $6/3 = 2$ (min) |

- **Variabile Entrante**: L'unica variabile con coefficiente negativo in riga 0 è $x_1$ (coefficiente $-3$).
- **Variabile Uscente**: Calcolo dei rapporti minimi sulla colonna di $x_1$:
  - Riga $s_1$: $4/1 = 4$
  - Riga $x_2$: coeff. nullo (ignorato)
  - Riga $s_3$: $6/3 = 2$
  Il rapporto minimo è $2$. La variabile uscente è $s_3$.
- **Elemento Pivot**: $3$ (riga $s_3$, colonna $x_1$).

### Iterazione 2 (Tableau Ottimo)
Normalizziamo la riga pivot dividendo la riga $s_3$ per $3$. Successivamente azzeriamo la colonna di $x_1$ sulle altre righe:
- $R_3 \leftarrow R_3 / 3$
- $R_0 \leftarrow R_0 + 3 R_3$
- $R_1 \leftarrow R_1 - R_3$

| Base | $Z$ | $x_1$ | $x_2$ | $s_1$ | $s_2$ | $s_3$ | RHS |
|---|---|---|---|---|---|---|---|
| **$Z$** | 1 | 0 | 0 | 0 | 1.5 | 1 | **36** |
| **$s_1$** | 0 | 0 | 0 | 1 | 1/3 | -1/3 | 2 |
| **$x_2$** | 0 | 0 | 1 | 0 | 0.5 | 0 | 6 |
| **$x_1$** | 0 | 1 | 0 | 0 | -1/3 | 1/3 | 2 |

- **Ottimalità**: Tutti i coefficienti in riga 0 (esclusa la colonna RHS) sono non negativi ($1.5 \ge 0$, $1 \ge 0$). Il simplesso si arresta.

---

## Soluzione Finale Leggibile

- Variabili in base: $x_1^* = 2$, $x_2^* = 6$, $s_1^* = 2$.
- Variabili fuori base (slack nulle): $s_2^* = 0$, $s_3^* = 0$.
- Valore Ottimo della funzione obiettivo:
  $$
  Z^* = 36
  $$
- **Interpretazione**: La soluzione ottima prevede di produrre $2$ lotti del prodotto 1 e $6$ lotti del prodotto 2, lasciando inutilizzate $2$ ore di capacità nel primo stabilimento (slack $s_1 = 2$).
