---
materia: ROPR
area: Programmazione Lineare
tipo: teoria
fonte: Ricerca Operativa - Metodo del Simplesso - 23-24.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - simplesso
  - geometria
  - vertici
---

# Geometria del simplesso

Il funzionamento del metodo del simplesso poggia su una solida base geometrica legata alle proprietà dei poliedri convessi.

## Definizioni Fondamentali

- **Frontiera del vincolo**: L'iperpiano definito dall'uguaglianza del vincolo (ad esempio, l'equazione $a_{i1}x_1 + a_{i2}x_2 + \dots = b_i$).
- **Vertice (o Punto di Intersezione di Frontiera)**: Un punto nello spazio delle variabili decisionali determinato dall'intersezione di $n$ frontiere di vincolo indipendenti (dove $n$ è il numero di variabili decisionali del problema).
- **Vertice Ammissibile**: Un vertice che soddisfa tutti i vincoli del problema (corrisponde a una soluzione di base ammissibile).
- **Vertice Non Ammissibile**: Un vertice che viola almeno uno dei vincoli del problema.
- **Spigolo**: Il segmento che unisce due vertici adiacenti. Corrisponde geometricamente alla retta di intersezione di $n-1$ frontiere di vincoli condivise dai due vertici.
- **Vertici Adiacenti**: Due vertici ammissibili sono adiacenti se condividono $n-1$ frontiere di vincoli.

## Test di Ottimalità Geometrico

> **Teorema**: Se una soluzione vertice ammissibile non ha vertici ammissibili adiacenti con un valore migliore della funzione obiettivo, allora essa è una soluzione ottima globale del problema di PL.

Questo permette al simplesso di limitare l'analisi a un sottoinsieme discreto di punti (i vertici) e di arrestarsi non appena nessun movimento lungo uno spigolo porta ad un miglioramento.

## Esempio Geometrico: Wyndor Glass

Il modello di Wyndor Glass Co. è definito da:

$$
\max Z = 3x_1 + 5x_2
$$

soggetto a:

$$
x_1 \le 4 \quad (\text{Stabilimento 1})
$$

$$
2x_2 \le 12 \quad (\text{Stabilimento 2})
$$

$$
3x_1 + 2x_2 \le 18 \quad (\text{Stabilimento 3})
$$

$$
x_1, x_2 \ge 0 \quad (\text{Vincoli di non negatività})
$$

### Adiacenza dei Vertici in Wyndor Glass

Poiché $n = 2$, due vertici sono adiacenti se condividono $n-1 = 1$ frontiera di vincolo.

| Vertice ammissibile | Vertici adiacenti |
|---|---|
| $(0,0)$ | $(0,6)$, $(4,0)$ |
| $(0,6)$ | $(2,6)$, $(0,0)$ |
| $(2,6)$ | $(4,3)$, $(0,6)$ |
| $(4,3)$ | $(4,0)$, $(2,6)$ |
| $(4,0)$ | $(0,0)$, $(4,3)$ |

### Valutazione dei Vertici

La funzione obiettivo $Z = 3x_1 + 5x_2$ assume i seguenti valori nei vertici ammissibili:

| Vertice $(x_1, x_2)$ | Valore di $Z$ | Stato |
|---|---:|---|
| $(0,0)$ | $0$ | Non ottimo |
| $(0,6)$ | $30$ | Non ottimo |
| $(2,6)$ | $36$ | **Ottimo** |
| $(4,3)$ | $27$ | Non ottimo |
| $(4,0)$ | $12$ | Non ottimo |

Geometricamente, il simplesso parte da $(0,0)$, si sposta verso $(0,6)$ (poiché il coefficiente di $x_2$ in $Z$ è maggiore), poi si sposta a $(2,6)$. In $(2,6)$ i vertici adiacenti sono $(0,6)$ con $Z=30$ e $(4,3)$ con $Z=27$. Poiché nessuno dei due migliora $Z=36$, $(2,6)$ viene dichiarato ottimo globale.
