---
materia: ROPR
area: Programmazione Lineare
tipo: teoria
fonte: Ricerca Operativa - Teoria del Simplesso - 23-24.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - simplesso
  - adiacenza
  - spigoli
  - cammino-simplesso
---

# Vertici adiacenti e cammino del simplesso

Il metodo del simplesso risolve un problema di programmazione lineare muovendosi in modo sistematico lungo i bordi della regione ammissibile.

## 1. Definizione di Adiacenza e Spigolo

Geometricamente, la frontiera della regione ammissibile (poliedro) è costituita da facce e spigoli.

- Un **spigolo** è il segmento di frontiera che collega due vertici ammissibili adiacenti.
- Da ogni vertice ammissibile si dipartono spigoli che conducono ai rispettivi vertici adiacenti.

> **Definizione Formale**: Due vertici ammissibili in $\mathbb{R}^n$ sono adiacenti se condividono $n-1$ frontiere di vincoli attive (cioè soddisfano contemporaneamente le stesse $n-1$ equazioni di frontiera).

## 2. Il Cammino del Simplesso

Il **cammino del simplesso** è definito come una sequenza ordinata di vertici ammissibili adiacenti:
$$
v^{(0)} \to v^{(1)} \to v^{(2)} \to \dots \to v^{(k)}
$$
dove:
- $v^{(0)}$ è il vertice ammissibile iniziale (solitamente l'origine).
- Ciascun passaggio $v^{(i)} \to v^{(i+1)}$ avviene lungo uno spigolo ammissibile che garantisce un miglioramento (o stabilità, in caso di degenerazione) della funzione obiettivo $Z$.
- $v^{(k)}$ è il vertice ottimo finale.

## 3. Collegamento tra Geometria e Algebra

Ogni spostamento lungo uno spigolo tra due vertici adiacenti corrisponde a un cambiamento minimo nel sistema di equazioni attive:

1. **Geometria**: Ci si sposta da un vertice a un altro adiacente rilasciando una delle $n$ frontiere di vincolo attive (che diventa inattiva) ed attivandone una nuova per identificare il nuovo vertice. Le altre $n-1$ frontiere rimangono attive durante lo spostamento (costituiscono lo spigolo).
2. **Algebra (Simplesso Tabellare)**: Questa operazione equivale esattamente al **cambio di base**:
   - Rilasciare una frontiera di vincolo significa far entrare in base una variabile non di base (il suo valore cresce da zero).
   - Attivare una nuova frontiera di vincolo significa far uscire dalla base una variabile di base (il suo valore scende a zero).
   - La base del tableau varia di **un solo elemento** ad ogni singola iterazione di pivot.
