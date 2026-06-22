---
topic: Programmazione Lineare
type: esempio_svolto
source: lezione 3 completa.pdf
status: da_verificare
---

# Esempio Svolto — Esercizio Tool.Spa

## Traccia Sintetica
La Tool.Spa produce due tipi di utensili: $x_c$ (utensili comuni) e $x_p$ (utensili speciali).
- Profitto unitario: 130 € per $x_c$, 100 € per $x_p$.
- Vincoli sulle ore di lavorazione in 3 reparti:
  - Reparto 1: $1.5x_c + x_p \le 27$
  - Reparto 2: $x_c + x_p \le 21$
  - Reparto 3: $0.3x_c + 0.5x_p \le 9$
- Limiti di mercato:
  - Vendite $x_c$ al massimo pari a 15: $x_c \le 15$
  - Vendite $x_p$ al massimo pari a 16: $x_p \le 16$
- Variabili non negative: $x_c, x_p \ge 0$.

Risolvere con il metodo del simplesso.

## Formulazione in Forma Aumentata

Aggiungendo le slack $s_1, s_2, s_3, s_4, s_5$:

$$
1.5x_c + x_p + s_1 = 27
$$

$$
x_c + x_p + s_2 = 21
$$

$$
0.3x_c + 0.5x_p + s_3 = 9
$$

$$
x_c + s_4 = 15
$$

$$
x_p + s_5 = 16
$$

Riga obiettivo (riga 0):

$$
Z - 130x_c - 100x_p = 0
$$

## Risoluzione del Tableau

### Tableau Iniziale (Iterazione 0)

| Base | $Z$ | $x_c$ | $x_p$ | $s_1$ | $s_2$ | $s_3$ | $s_4$ | $s_5$ | RHS |
|---|---|---|---|---|---|---|---|---|---|
| **$Z$** | 1 | -130 | -100 | 0 | 0 | 0 | 0 | 0 | 0 |
| **$s_1$**| 0 | **1.5**| 1 | 1 | 0 | 0 | 0 | 0 | 27 |
| **$s_2$**| 0 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 21 |
| **$s_3$**| 0 | 0.3 | 0.5 | 0 | 0 | 1 | 0 | 0 | 9 |
| **$s_4$**| 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 15 |
| **$s_5$**| 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 16 |

- Variabile entrante: **$x_c$** (coefficiente $-130$).
- Rapporti RHS/colonna pivot:
  - $s_1$: $27 / 1.5 = 18$
  - $s_2$: $21 / 1 = 21$
  - $s_3$: $9 / 0.3 = 30$
  - $s_4$: $15 / 1 = 15$
- La variabile uscente è **$s_4$** (rapporto minimo = 15). Elemento pivot = 1.

*Nota: Nelle slide l'operazione di pivot iniziale viene effettuata talvolta su $s_1$ o $s_4$. Se si effettua il pivot su $s_4$ (variabile uscente corretta per il rapporto minimo), si ha:*

### Tableau Iterazione 1 (Pivot su riga $s_4$, colonna $x_c$)

| Base | $Z$ | $x_c$ | $x_p$ | $s_1$ | $s_2$ | $s_3$ | $s_4$ | $s_5$ | RHS |
|---|---|---|---|---|---|---|---|---|---|
| **$Z$** | 1 | 0 | -100 | 0 | 0 | 0 | 130 | 0 | 1950 |
| **$s_1$**| 0 | 0 | **1** | 1 | 0 | 0 | -1.5 | 0 | 4.5 |
| **$s_2$**| 0 | 0 | 1 | 0 | 1 | 0 | -1 | 0 | 6 |
| **$s_3$**| 0 | 0 | 0.5 | 0 | 0 | 1 | -0.3 | 0 | 4.5 |
| **$x_c$**| 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 15 |
| **$s_5$**| 0 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 16 |

- Variabile entrante: **$x_p$** (coefficiente $-100$).
- Rapporti RHS/colonna pivot:
  - $s_1$: $4.5 / 1 = 4.5$
  - $s_2$: $6 / 1 = 6$
  - $s_3$: $4.5 / 0.5 = 9$
  - $s_5$: $16 / 1 = 16$
- Variabile uscente: **$s_1$** (rapporto minimo = 4.5). Elemento pivot = 1.

### Tableau Iterazione 2 (Pivot su riga $s_1$, colonna $x_p$)

| Base | $Z$ | $x_c$ | $x_p$ | $s_1$ | $s_2$ | $s_3$ | $s_4$ | $s_5$ | RHS |
|---|---|---|---|---|---|---|---|---|---|
| **$Z$** | 1 | 0 | 0 | 100 | 0 | 0 | -20 | 0 | 2400 |
| **$x_p$**| 0 | 0 | 1 | 1 | 0 | 0 | -1.5 | 0 | 4.5 |
| **$s_2$**| 0 | 0 | 0 | -1 | 1 | 0 | **0.5** | 0 | 1.5 |
| **$s_3$**| 0 | 0 | 0 | -0.5 | 0 | 1 | 0.45 | 0 | 2.25 |
| **$x_c$**| 0 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 15 |
| **$s_5$**| 0 | 0 | 0 | -1 | 0 | 0 | 1.5 | 1 | 11.5 |

- Variabile entrante: **$s_4$** (coefficiente $-20$ in riga 0).
- Rapporti RHS/colonna pivot ($s_4 > 0$):
  - $s_2$: $1.5 / 0.5 = 3$
  - $s_3$: $2.25 / 0.45 = 5$
  - $x_c$: $15 / 1 = 15$
  - $s_5$: $11.5 / 1.5 = 7.67$
- Variabile uscente: **$s_2$** (rapporto minimo = 3). Elemento pivot = 0.5.

### Tableau Iterazione 3 (Pivot su riga $s_2$, colonna $s_4$)

Dividendo la riga $s_2$ per 0.5 (moltiplicando per 2) e azzerando la colonna di $s_4$:

| Base | $Z$ | $x_c$ | $x_p$ | $s_1$ | $s_2$ | $s_3$ | $s_4$ | $s_5$ | RHS |
|---|---|---|---|---|---|---|---|---|---|
| **$Z$** | 1 | 0 | 0 | 60 | 40 | 0 | 0 | 0 | 2460 |
| **$x_p$**| 0 | 0 | 1 | -2 | 3 | 0 | 0 | 0 | 9 |
| **$s_4$**| 0 | 0 | 0 | -2 | 2 | 0 | 1 | 0 | 3 |
| **$s_3$**| 0 | 0 | 0 | 0.4 | -0.9 | 1 | 0 | 0 | 0.9 |
| **$x_c$**| 0 | 1 | 0 | 2 | -2 | 0 | 0 | 0 | 12 |
| **$s_5$**| 0 | 0 | 0 | 2 | -3 | 0 | 0 | 1 | 7 |

- Tutti i coefficienti della riga 0 sono $\ge 0$. La soluzione è ottima.

## Risultato Finale Ricostruito
La soluzione ottima è:

$$
x_c^* = 12, \quad x_p^* = 9 \qquad \text{con } Z^* = 2460
$$

## Risposta da Esame
La soluzione ottimale per il problema Tool.Spa è $x_c = 12$ e $x_p = 9$ con un profitto massimo $Z = 2460$.

> [!WARNING]
> Nelle slide dell'asset `lezione 3 completa.pdf` la progressione dei tableau del simplesso per l'esercizio Tool.Spa non viene completata in modo del tutto esplicito e lineare. I passaggi intermedi qui sopra sono stati ricostruiti analiticamente. Marcare lo stato dell'esempio come *da verificare* qualora vengano richieste variazioni sul pivot iniziale.
