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
  - forma-aumentata
  - soluzioni-base
---

# Forma aumentata e soluzioni di base

Per poter applicare i metodi algebrici di risoluzione (come il simplesso), il problema di PL deve essere formulato in **forma aumentata**, in modo da operare su sistemi di equazioni lineari anziché su disequazioni.

## Forma Aumentata e Variabili di Slack

I vincoli di disuguaglianza $\le$ vengono trasformati in equazioni aggiungendo una **variabile di slack** non negativa, che rappresenta la quantità di risorsa non utilizzata dal vincolo corrispondente.

Esempio:
$$
a_{i1}x_1 + a_{i2}x_2 \le b_i \implies a_{i1}x_1 + a_{i2}x_2 + s_i = b_i \quad \text{con } s_i \ge 0
$$

## Classificazione delle Variabili

1. **Variabili Decisionali**: Le variabili originarie del modello ($x_1, x_2, \dots, x_n$).
2. **Variabili di Slack**: Le variabili introdotte per convertire le disuguaglianze in uguaglianze ($s_1, s_2, \dots, s_m$).
3. **Variabili di Base**: Le $m$ variabili associate alle colonne che compongono una base lineare per il sistema (corrispondono a valori tipicamente non nulli risolti dal sistema).
4. **Variabili Non di Base**: Le $n - m$ variabili libere che vengono poste pari a zero per poter risolvere il sistema di equazioni.

## Gradi di Libertà e Soluzione di Base

Dato un sistema di $m$ equazioni lineari indipendenti con $N$ variabili ($N > m$):
- Il sistema ha $N - m$ gradi di libertà.
- Poniamo $N - m$ variabili pari a zero (**variabili non di base**).
- Risolviamo il sistema lineare quadrato risultante per le restanti $m$ variabili (**variabili di base**).

La soluzione così ottenuta è detta **soluzione di base**.

> [!NOTE]
> - **Soluzione di base ammissibile**: Se tutte le $m$ variabili di base risultanti sono non negative ($\ge 0$). Ciascuna soluzione di base ammissibile corrisponde esattamente a un **vertice ammissibile** del poliedro.
> - **Soluzione di base non ammissibile**: Se almeno una delle variabili risolte assume un valore negativo ($< 0$). Corrisponde a un vertice geometrico che giace al di fuori della regione ammissibile.

## Origine come Soluzione Iniziale

Se il problema originale ha solo vincoli del tipo $\le$ con termini noti non negativi ($b_i \ge 0$):
- Ponendo le variabili decisionali originarie pari a zero ($x_j = 0$, variabili non di base), le variabili di slack diventano le variabili di base iniziale.
- Il loro valore è pari a $s_i = b_i \ge 0$.
- Questa è una soluzione di base ammissibile iniziale immediata e coincide con l'origine degli assi geometrici.

## Esempio: Wyndor Glass in Forma Aumentata

Problema originale:

$$
\max Z = 3x_1 + 5x_2
$$

soggetto a:

$$
x_1 \le 4
$$

$$
2x_2 \le 12
$$

$$
3x_1 + 2x_2 \le 18
$$

$$
x_1, x_2 \ge 0
$$

Forma aumentata:

$$
\begin{aligned}
(0) \quad Z - 3x_1 - 5x_2 &= 0 \\
(1) \quad x_1 + s_1 &= 4 \\
(2) \quad 2x_2 + s_2 &= 12 \\
(3) \quad 3x_1 + 2x_2 + s_3 &= 18
\end{aligned}
$$

con $x_1, x_2, s_1, s_2, s_3 \ge 0$.

Ponendo le $N-m = 5-3 = 2$ variabili non di base $x_1 = 0, x_2 = 0$, otteniamo la soluzione di base iniziale:
- Variabili di base: $s_1 = 4$, $s_2 = 12$, $s_3 = 18$ (ammissibile).
- Valore di $Z = 0$.
