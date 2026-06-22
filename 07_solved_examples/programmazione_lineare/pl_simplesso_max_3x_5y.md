---
topic: Programmazione Lineare
type: esempio_svolto
source: lezione 3 completa.pdf
status: verificato
---

# Esempio Svolto — Simplesso con Controllo Grafico (Problema Illimitato)

## Traccia Sintetica
Risolvere il seguente problema di PL tramite il metodo del simplesso tabellare e commentare l'interpretazione geometrica:

$$
\max Z = 3x + 5y
$$

soggetto a:

$$
x - y \le 1
$$

$$
2x - y \le 4
$$

$$
-2x + y \le 1
$$

$$
x, y \ge 0
$$

## Risoluzione

### 1. Forma Aumentata
Aggiungendo le slack $u, v, s \ge 0$:

$$
x - y + u = 1
$$

$$
2x - y + v = 4
$$

$$
-2x + y + s = 1
$$

Riga obiettivo (riga 0):

$$
Z - 3x - 5y = 0
$$

### 2. Tableau Iniziale (Iterazione 0)

| Base | $Z$ | $x$ | $y$ | $u$ | $v$ | $s$ | RHS |
|---|---|---|---|---|---|---|---|
| **$Z$** | 1 | -3 | -5 | 0 | 0 | 0 | 0 |
| **$u$** | 0 | 1 | -1 | 1 | 0 | 0 | 1 |
| **$v$** | 0 | 2 | -1 | 0 | 1 | 0 | 4 |
| **$s$** | 0 | -2 | **1** | 0 | 0 | 1 | 1 |

- Soluzione di base iniziale: $u=1, v=4, s=1$, con $Z=0$.
- Variabile entrante: **$y$** (coefficiente più negativo, $-5$).
- Rapporti: solo la riga $s$ ha coefficiente positivo nella colonna di $y$ ($1 > 0$). Rapporto = $1 / 1 = 1$.
- Variabile uscente: **$s$**. Elemento pivot = 1.

### 3. Tableau Iterazione 1 (Pivot su riga $s$, colonna $y$)

Eseguendo l'azzeramento della colonna $y$:

| Base | $Z$ | $x$ | $y$ | $u$ | $v$ | $s$ | RHS |
|---|---|---|---|---|---|---|---|
| **$Z$** | 1 | **-13**| 0 | 0 | 0 | 5 | 5 |
| **$u$** | 0 | -1 | 0 | 1 | 0 | 1 | 2 |
| **$v$** | 0 | 0 | 0 | 0 | 1 | 1 | 5 |
| **$y$** | 0 | -2 | 1 | 0 | 0 | 1 | 1 |

- Soluzione di base corrente: $u=2, v=5, y=1$, con $Z=5$.
- Variabile entrante: **$x$** (coefficiente $-13$ nella riga 0).
- Rapporti: verifichiamo i coefficienti della colonna pivot per $x$:
  - riga $u$: $-1 \le 0$ (nessun rapporto)
  - riga $v$: $0 \le 0$ (nessun rapporto)
  - riga $y$: $-2 \le 0$ (nessun rapporto)
- Poiché tutti i coefficienti nella colonna pivot della variabile entrante $x$ sono non positivi ($\le 0$), **non esiste alcuna variabile uscente**.

## Risultato Finale
L'algoritmo del simplesso rileva che il problema è **illimitato** superiormente. Non esiste un ottimo finito.

## Interpretazione Geometrica
Nel piano cartesiano $(x,y)$, la regione ammissibile è delimitata dalle rette:
- $y \ge x - 1$ (vincolo 1)
- $y \ge 2x - 4$ (vincolo 2)
- $y \le 2x + 1$ (vincolo 3)

La regione ammissibile si estende all'infinito verso l'alto a destra (nella direzione in cui sia $x$ che $y$ crescono). Poiché vogliamo massimizzare $3x + 5y$, all'aumentare indefinito di $x$ e $y$ (mantenendo $y \approx 2x$), il valore di $Z$ cresce senza limiti ($Z \to +\infty$).

## Risposta da Esame
Alla prima iterazione del simplesso la variabile entrante è $y$ e quella uscente è $s$. Al tableau successivo, la variabile entrante è $x$; poiché tutti i coefficienti nella colonna di $x$ nei vincoli sono non positivi, il problema è illimitato superiormente ($Z^* \to +\infty$).
