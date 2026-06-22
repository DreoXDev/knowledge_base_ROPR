---
type: theory-note
topic: programmazione-lineare
status: draft
sources:
  - raw_assets/Programmazione Lineare/Ricerca Operativa - Introduzione a PL - 23-24.pdf
reliability: official
---

# Formulazione Generale di un Modello di PL

Un problema di Programmazione Lineare in forma standard si può esprimere matematicamente come:

$$
\max Z = \sum_{j=1}^{n} c_j x_j
$$

soggetta a:

$$
\sum_{j=1}^{n} a_{ij}x_j \le b_i \qquad i = 1,\dots,m
$$

$$
x_j \ge 0 \qquad j = 1,\dots,n
$$

## Definizione dei Componenti

- $x_j$: **Variabile decisionale**, rappresenta il livello dell'attività $j$ da intraprendere.
- $c_j$: **Coefficiente di costo o profitto unitario**, indica l'incremento di $Z$ dovuto ad una unità di attività $j$.
- $a_{ij}$: **Coefficiente tecnologico**, quantità della risorsa $i$ consumata da una unità dell'attività $j$.
- $b_i$: **Termine noto**, indica la quantità totale disponibile della risorsa $i$.
- $n$: Numero di attività (variabili decisionali).
- $m$: Numero di risorse limitate (vincoli funzionali).

## Come riconoscere un problema di PL

Un problema appartiene alla classe della Programmazione Lineare quando soddisfa le seguenti condizioni:

1. **Funzione obiettivo lineare**: Il valore di $Z$ varia in modo lineare con ciascuna delle variabili.
2. **Vincoli lineari**: Le relazioni di limitazione delle risorse sono esprimibili come equazioni o disequazioni lineari.
3. **Variabili continue**: Le decisioni possono assumere qualsiasi valore reale non negativo (non sono vincolate ad essere intere).
4. **Parametri noti e costanti**: I coefficienti $c_j$, $a_{ij}$ e $b_i$ sono deterministici e fissati a priori.
5. **Vincoli di non negatività**: Tutte le variabili decisionali devono essere non negative ($x_j \ge 0$).

#ropr #programmazione-lineare #teoria #formulazione
