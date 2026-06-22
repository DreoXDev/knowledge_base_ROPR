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
  - teoria
---

# Teoria del simplesso

## Scopo della Teoria
Nelle lezioni introduttive, il metodo del simplesso è stato presentato sfruttando esempi a due sole variabili decisionali (come il problema Wyndor Glass Co.), in cui la rappresentazione geometrica nel piano cartesiano rende immediato visualizzare i vertici e gli spostamenti tra essi.

Tuttavia, i problemi reali di Programmazione Lineare (PL) coinvolgono centinaia o migliaia di variabili decisionali e vincoli. In tali contesti multidimensionali (spazi $\mathbb{R}^n$):
- L'ispezione grafica diretta è impossibile.
- È indispensabile disporre di una formalizzazione matematica rigorosa che generalizzi i concetti geometrici (frontiere, vertici, adiacenza) in termini algebrici equivalenti (sistemi di equazioni lineari, basi, soluzioni di base).

La **teoria del simplesso** stabilisce ed evidenzia questo legame e giustifica matematicamente perché l'algoritmo algebrico sia in grado di trovare la soluzione ottima globale analizzando solo un numero limitato di punti.

---

## Risposta Breve da Esame

La teoria del simplesso serve a generalizzare l'intuizione geometrica vista nei problemi a due variabili. In particolare formalizza il legame tra frontiere dei vincoli, vertici ammissibili, sistemi di equazioni e soluzioni di base. Il simplesso sfrutta la proprietà fondamentale per cui, se un problema di PL ammette un ottimo finito, almeno una soluzione ottima si trova in un vertice ammissibile della regione ammissibile. Questo riduce la ricerca dell'ottimo tra gli infiniti punti del poliedro ad un sottoinsieme discreto di punti (i vertici).
