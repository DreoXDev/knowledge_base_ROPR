---
topic: Programmazione Lineare
type: esempio_svolto
source: lezione 3 completa.pdf
status: verificato
---

# Esempio Svolto — Due Fasi e Problema Non Ammissibile

## Traccia Sintetica
Risolvere il seguente problema di PL:

$$
\max Z = 2x_1 + 2x_2 + 2x_3
$$

soggetto a:

$$
-x_1 + x_2 + x_3 \ge 2
$$

$$
x_1 - 2x_2 + x_3 \ge 1
$$

$$
x_1 \ge 0, \quad x_2 \ge 0, \quad x_3 \le 0
$$

## Risoluzione

### 1. Gestione del Vincolo di Segno di $x_3$
Poiché $x_3 \le 0$, poniamo $x_3 = -x_3'$ (con $x_3' \ge 0$).
Il modello modificato diventa:

$$
\max Z = 2x_1 + 2x_2 - 2x_3'
$$

soggetto a:

$$
-x_1 + x_2 - x_3' \ge 2
$$

$$
x_1 - 2x_2 - x_3' \ge 1
$$

$$
x_1, x_2, x_3' \ge 0
$$

### 2. Standardizzazione e Variabili Artificiali
Aggiungiamo surplus ($s_1, s_2 \ge 0$) e artificiali ($a_1, a_2 \ge 0$):

$$
-x_1 + x_2 - x_3' - s_1 + a_1 = 2
$$

$$
x_1 - 2x_2 - x_3' - s_2 + a_2 = 1
$$

con tutte le variabili $\ge 0$.

### 3. Fase 1 (Minimizzazione delle Artificiali)
Formuliamo la funzione obiettivo ausiliaria:

$$
\max -W = -a_1 - a_2 \implies -W + a_1 + a_2 = 0
$$

Azzeriamo i costi delle variabili artificiali $a_1, a_2$ (che sono in base iniziale con valori $a_1 = 2$ e $a_2 = 1$).
Esprimiamo $a_1$ e $a_2$ dai vincoli:
- $a_1 = 2 + x_1 - x_2 + x_3' + s_1$
- $a_2 = 1 - x_1 + 2x_2 + x_3' + s_2$

Sommando $a_1 + a_2$ otteniamo la riga 0:

$$
-W + x_2 + 2x_3' + s_1 + s_2 = -3
$$

### 4. Verifica di Ottimalità della Fase 1
Esaminiamo i coefficienti delle variabili nella riga 0:
- $x_1$: 0
- $x_2$: +1
- $x_3'$: +2
- $s_1$: +1
- $s_2$: +1

Poiché tutti i coefficienti nella riga 0 per un problema di massimizzazione sono **non negativi** ($\ge 0$), il tableau iniziale della Fase 1 è **già ottimo**.

Non è possibile fare alcuna operazione di pivot per diminuire la somma delle artificiali.
Il valore ottimo di Fase 1 è:

$$
-W^* = -3 \implies W^* = 3
$$

## Risultato Finale
Poiché il valore ottimo di Fase 1 è $W^* = 3 > 0$, le variabili artificiali non possono essere eliminate dalla base (rimangono attive con valori non nulli). Il problema originario è **inammissibile** (non possiede soluzioni ammissibili).

## Risposta da Esame
Sostituendo $x_3 = -x_3'$, si introducono surplus e artificiali. L'azzeramento dei costi della riga obiettivo ausiliaria di Fase 1 produce una riga 0 con tutti i coefficienti non negativi ($\ge 0$). Il tableau di Fase 1 è quindi già ottimo con somma delle artificiali $W^* = 3 > 0$. Il problema è inammissibile.
