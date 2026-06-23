---
type: method
topic: programmazione_non_lineare
status: active
reliability: official
---

# Esplorazione Combinatoria dei Vincoli Attivi in KKT

Risolvere analiticamente un sistema KKT con $p$ vincoli di disuguaglianza richiede l'analisi di tutte le possibili combinazioni di vincoli attivi e inattivi. Per ogni vincolo di disuguaglianza $h_j(x) \le 0$, si hanno due scenari mutuamente esclusivi:
1. **Vincolo Attivo**: il punto stazionario giace sulla frontiera del vincolo $\implies h_j(x) = 0$. Il moltiplicatore $\mu_j$ è una variabile libera da ricavare (e deve rispettare il segno).
2. **Vincolo Inattivo**: il punto stazionario giace all'interno $\implies h_j(x) < 0$. Per la complementarità degli scarti, si impone $\mu_j = 0$.

Con $p$ vincoli di disuguaglianza, ci sono $2^p$ casi possibili.

---

## Tabella dei Casi per $p=2$ (4 Combinazioni)

| Caso | Stato Vincolo 1 ($h_1 \le 0$) | Stato Vincolo 2 ($h_2 \le 0$) | Condizioni Algebriche da Imporre |
|---|---|---|---|
| **Caso 1** | Inattivo ($\mu_1 = 0$) | Inattivo ($\mu_2 = 0$) | $\nabla f(x) = 0$ (ricerca ottimi interni). Verificare $h_1(x) \le 0, h_2(x) \le 0$. |
| **Caso 2** | Attivo ($h_1 = 0$) | Inattivo ($\mu_2 = 0$) | Risolvere $\nabla f(x) + \mu_1 \nabla h_1(x) = 0$ e $h_1(x) = 0$. Verificare $h_2(x) \le 0$ e segno $\mu_1$. |
| **Caso 3** | Inattivo ($\mu_1 = 0$) | Attivo ($h_2 = 0$) | Risolvere $\nabla f(x) + \mu_2 \nabla h_2(x) = 0$ e $h_2(x) = 0$. Verificare $h_1(x) \le 0$ e segno $\mu_2$. |
| **Caso 4** | Attivo ($h_1 = 0$) | Attivo ($h_2 = 0$) | Risolvere $\nabla f(x) + \mu_1 \nabla h_1(x) + \mu_2 \nabla h_2(x) = 0$ e $h_1(x) = 0, h_2(x) = 0$. Verificare segni $\mu_1, \mu_2$. |

---

## Procedura Risolutiva Sistematica per ogni Caso

Per ciascun caso impostato:

### 1. Risoluzione del sistema algebrico
- Sostituire i moltiplicatori dei vincoli inattivi a $0$ nella stazionarietà.
- Porre i vincoli attivi a zero.
- Risolvere il sistema per ricavare le variabili decisionali $x^*$ e i moltiplicatori rimanenti $\mu^*$.

### 2. Filtro Ammissibilità Primale (Feasibility check)
- Verificare che il punto ottenuto soddisfi **tutti** i vincoli del problema originale, specialmente quelli che in questo caso erano stati assunti *inattivi*:
  $$h_{\text{inattivi}}(x^*) \le 0$$
- Se il punto viola anche un solo vincolo, scartarlo immediatamente (soluzione non ammissibile).

### 3. Filtro Ammissibilità Duale (Segno moltiplicatori)
- Verificare che i moltiplicatori ricavati per i vincoli *attivi* rispettino il segno richiesto:
  - Per un problema di **minimo**: $\mu_j^* \ge 0$.
  - Per un problema di **massimo**: $\mu_j^* \le 0$.
- Se un moltiplicatore ha il segno opposto, scartare il punto (non è un ottimo per il tipo di problema cercato).

---

## Esempio di Esclusione Rapida (Incompatibilità geometrica)

Spesso alcune combinazioni possono essere escluse a priori o si rivelano prive di soluzione matematica.
Ad esempio, se i vincoli sono:
- $h_1(x, y) = -x - 1 \le 0 \implies x \ge -1$ (attivo: $x = -1$)
- $h_2(x, y) = -y - 1 \le 0 \implies y \ge -1$ (attivo: $y = -1$)
- $h_3(x, y) = x + y - 2 \le 0 \implies x + y \le 2$ (attivo: $x + y = 2$)

Se proviamo il caso in cui tutti e tre i vincoli sono attivi contemporaneamente:
$$\begin{cases}
x = -1 \\
y = -1 \\
x + y = 2 \implies -1 - 1 = -2 \neq 2
\end{cases}$$
Questo sistema non ha soluzioni reali. Il caso è geometricamente impossibile (l'intersezione di 3 rette non parallele in $\mathbb{R}^2$ è vuota in questo caso). Si conclude immediatamente che non vi sono soluzioni KKT per questa combinazione.
