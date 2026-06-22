---
topic: Programmazione Lineare
type: esempio_svolto
source: lezione 3 completa.pdf
status: da_verificare
---

# Esempio Svolto — Metodo delle Due Fasi (Esempio Base)

## Traccia Sintetica
Risolvere il seguente problema di PL tramite il metodo delle due fasi:

$$
\min Z = 2x_1 + 4x_2 + 2x_3 - x_4
$$

soggetto a:

$$
3x_1 + x_2 \ge 2
$$

$$
x_2 + 2x_3 = 4
$$

$$
x_3 + 4x_4 \le 5
$$

$$
x_1, x_2, x_3, x_4 \ge 0
$$

## Risoluzione

### 1. Conversione in Forma Aumentata e Standardizzazione
Trasformiamo il problema in massimizzazione: $\max -Z = -2x_1 - 4x_2 - 2x_3 + x_4$.
Aggiungiamo:
- surplus $x_5$ e artificiale $a_1$ nel vincolo 1;
- artificiale $a_2$ nel vincolo 2;
- slack $x_6$ nel vincolo 3.

$$
3x_1 + x_2 - x_5 + a_1 = 2
$$

$$
x_2 + 2x_3 + a_2 = 4
$$

$$
x_3 + 4x_4 + x_6 = 5
$$

con tutte le variabili $\ge 0$.

### 2. Fase 1 (Minimizzazione delle Artificiali)
La funzione obiettivo ausiliaria di Fase 1 è:

$$
\max -W = -a_1 - a_2 \implies -W + a_1 + a_2 = 0
$$

Prima di eseguire il simplesso, azzeriamo i coefficienti di $a_1, a_2$ in riga 0 sottraendo i vincoli 1 e 2 alla riga 0:

$$
-W - 3x_1 - 2x_2 - 2x_3 + x_5 = -6
$$

Risolvendo la Fase 1 tramite i pivot del simplesso, si ottiene la soluzione ottima di Fase 1 con $-W^* = 0$, il che indica che il problema iniziale è ammissibile. Le variabili artificiali $a_1, a_2$ escono dalla base e possono essere rimosse dal tableau.

### 3. Fase 2 (Risoluzione del Problema Originale)
Rimuoviamo le colonne $a_1, a_2$ ed inseriamo la riga obiettivo originaria:

$$
-Z + 2x_1 + 4x_2 + 2x_3 - x_4 = 0
$$

Effettuando l'azzeramento dei costi per le variabili correntemente in base e completando i pivot del simplesso, si perviene alla soluzione ottima.

## Soluzione Ottima Ricostruita
La soluzione finale è:

$$
x^* = \left(\frac{2}{3}, 0, 2, \frac{3}{4}, 0, 0\right)
$$

Calcolando il valore di $Z$:

$$
Z^* = 2\left(\frac{2}{3}\right) + 4(0) + 2(2) - \frac{3}{4} = \frac{4}{3} + 4 - \frac{3}{4} = \frac{16 + 48 - 9}{12} = \frac{55}{12}
$$

Nel problema di massimizzazione, il valore finale della riga 0 è $-Z^* = -55/12$.

> [!WARNING]
> Nelle slide dell'asset `lezione 3 completa.pdf` compare una incongruenza: viene riportato il valore $Z = -53/12$ in grassetto in fondo al tableau, mentre poco distante compare la frazione correct `-55/12` (che corrisponde all'effettivo calcolo di $Z$ sui valori ottimi delle variabili). Lo stato di questo esercizio è impostato su *da verificare* per allertare lo studente su questo refuso nelle slide d'esame.
