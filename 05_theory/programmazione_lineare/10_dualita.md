---
materia: ROPR
area: Programmazione Lineare
tipo: teoria
fonte: Ricerca Operativa - Teoria della Dualità.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - simplesso
  - dualita
  - teoria
---

# Teoria della dualità

A ogni problema di Programmazione Lineare, chiamato **problema primale**, è associato un secondo problema di Programmazione Lineare, strettamente connesso, denominato **problema duale**.

## 1. Utilità della Dualità

L'analisi del problema duale fornisce contributi di fondamentale importanza:
- Consente di risolvere problemi alternativi potenzialmente più semplici (es. con meno vincoli).
- Permette di interpretare economicamente i vincoli, le risorse e il consumo.
- Consente di ricavare i **prezzi ombra** delle risorse.
- Costituisce il fondamento per l'**analisi di sensitività** post-ottimo.
- Spiega il significato algebrico dei coefficienti della riga 0 nel tableau finale del simplesso.

---

## 2. Forma Standard Primale-Duale

### Problema Primale (MAX in forma standard)
Massimizzare la funzione obiettivo soggetta a vincoli di minore o uguale e non negatività:

$$
\max Z = \sum_{j=1}^{n} c_j x_j
$$

soggetto a:

$$
\sum_{j=1}^{n} a_{ij}x_j \le b_i \qquad \forall i=1,\dots,m
$$

$$
x_j \ge 0 \qquad \forall j=1,\dots,n
$$

### Problema Duale Associato (MIN in forma standard)
Minimizzare la funzione obiettivo duale soggetta a vincoli di maggiore o uguale e non negatività:

$$
\min W = \sum_{i=1}^{m} b_i y_i
$$

soggetto a:

$$
\sum_{i=1}^{m} a_{ij}y_i \ge c_j \qquad \forall j=1,\dots,n
$$

$$
y_i \ge 0 \qquad \forall i=1,\dots,m
$$

---

## 3. Formizzazione Matriciale

### Problema Primale

$$
\max Z = \mathbf{c}\mathbf{x}
$$

soggetto a:

$$
\mathbf{A}\mathbf{x} \le \mathbf{b}
$$

$$
\mathbf{x} \ge 0
$$

### Problema Duale

$$
\min W = \mathbf{y}\mathbf{b}
$$

soggetto a:

$$
\mathbf{y}\mathbf{A} \ge \mathbf{c}
$$

$$
\mathbf{y} \ge 0
$$

Dove:
- $\mathbf{x}$ è un vettore colonna $n \times 1$.
- $\mathbf{y}$ è un vettore riga $1 \times m$.
- $\mathbf{c}$ è un vettore riga $1 \times n$.
- $\mathbf{b}$ è un vettore colonna $m \times 1$.
- $\mathbf{A}$ è la matrice dei coefficienti $m \times n$.

---

## 4. Corrispondenze Primale-Duale

| Problema Primale | Problema Duale |
|---|---|
| Ottimizzazione di **Massimo (MAX)** | Ottimizzazione di **Minimo (MIN)** |
| Vincolo $i$-esimo | Variabile duale $y_i$ |
| Variabile primale $x_j$ | Vincolo duale $j$-esimo |
| Coefficienti F.O. $\mathbf{c}$ | Termini noti dei vincoli duali (RHS) |
| Termini noti vincoli $\mathbf{b}$ (RHS) | Coefficienti F.O. duale |
| Matrice dei coefficienti $\mathbf{A}$ | Matrice trasposta $\mathbf{A}^T$ |

---

## Risposta da Esame

Il problema duale è il problema di Programmazione Lineare associato al primale, ottenuto scambiando il ruolo di vincoli e variabili: i termini noti del primale diventano i coefficienti della funzione obiettivo duale, i coefficienti della funzione obiettivo primale diventano i termini noti dei vincoli duali, e la matrice dei coefficienti viene trasposta. Se il primale è un problema di massimo in forma standard ($\le$ e $\ge 0$), il duale è un problema di minimo con vincoli $\ge$ e variabili non negative.
