---
materia: ROPR
area: Programmazione Lineare
tipo: teoria
fonte: Ricerca Operativa - Teoria del Simplesso - 23-24.pdf
stato: completo
priorita: media
tags:
  - ropr
  - programmazione-lineare
  - simplesso
  - degenerazione
---

# Degenerazione nel simplesso

Durante la risoluzione algebrica o l'analisi geometrica di un problema di Programmazione Lineare, si può riscontrare il fenomeno della **degenerazione**.

## 1. Interpretazione Geometrica

In uno spazio $\mathbb{R}^n$, un vertice è definito dall'intersezione di esattamente $n$ iperpiani associati alle equazioni di frontiera dei vincoli del problema.

> **Degenerazione Geometrica**: Si verifica quando **più di $n$ iperpiani di frontiera** si intersecano nello stesso identico punto. In questo caso, il vertice è sovradeterminato da vincoli attivi ridondanti.

Un esempio tipico in due variabili ($n=2$) si ha quando tre o più rette di vincolo passano contemporaneamente per lo stesso punto di vertice ammissibile.

## 2. Interpretazione Algebrica (Basi Multiple)

Poiché un vertice degenere è all'intersezione di $k > n$ frontiere di vincoli, algebricamente:
- Possiamo scegliere $n$ equazioni tra le $k$ disponibili in diversi modi per identificare lo stesso identico punto.
- Nel simplesso tabellare, questo implica che **più basi diverse rappresentano lo stesso vertice**.
- Durante il pivot, una delle variabili di base assume valore esattamente pari a **zero**.

## 3. Conseguenze Operative
Quando l'algoritmo si trova in una soluzione degenere:
- L'operazione di pivot successivo farà entrare in base una variabile, ma il valore della variabile uscente (e quindi l'aumento di $Z$) sarà pari a **zero**.
- L'algoritmo cambia base (algebricamente) ma rimane fermo sullo stesso vertice (geometricamente).
- Si rimanda alla nota operativa [pl_casi_particolari_simplesso.md](../../04_methods/programmazione_lineare/pl_casi_particolari_simplesso.md) per la gestione del tie breaking associato alla degenerazione.

---

## Risposta Breve da Esame

Una soluzione di base ammissibile è degenere quando almeno una variabile di base vale zero. Geometricamente ciò corrisponde a un vertice in cui sono attivi più vincoli di quelli strettamente necessari per identificarlo (più di $n$ iperpiani di frontiera concorrono nello stesso punto). In questi casi basi diverse possono rappresentare lo stesso vertice, il che può causare pivotaggi a passo nullo (con $Z$ invariato).
