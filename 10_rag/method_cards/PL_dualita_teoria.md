---
materia: ROPR
area: Programmazione Lineare
tipo: metodo
fonte: Ricerca Operativa - Teoria della Dualità.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - dualita
  - teoria
  - method-card
---

# METHOD CARD — Teoria della Dualità

## Quando usarla
Usare questa card per rispondere a domande d'esame teoriche riguardanti la relazione primale-duale, la dualità debole, la dualità forte e i casi limite.

## Idee e Definizioni Chiave

1. **Problema Primale e Duale**: Ad ogni problema di PL (primale) è associato un secondo problema di PL (duale) che condivide gli stessi dati ma con una struttura simmetrica speculare.
2. **Dualità Debole**: Per ogni soluzione ammissibile $\mathbf{x}$ del primale e $\mathbf{y}$ del duale (in caso MAX-MIN):
   $$
   \mathbf{c}\mathbf{x} \le \mathbf{y}\mathbf{b}
   $$
   Il valore di una soluzione ammissibile primale fornisce sempre un limite inferiore all'ottimo duale, e viceversa.
3. **Dualità Forte**: Se primale e duale hanno soluzioni ottime finite $\mathbf{x}^*$ e $\mathbf{y}^*$, allora i valori ottimi coincidono:
   $$
   Z^* = W^* \iff \mathbf{c}\mathbf{x}^* = \mathbf{y}^*\mathbf{b}
   $$
4. **Casi Limite**:
   - Se il primale è **illimitato** ($Z^* \to +\infty$), il duale è **inammissibile** (nessuna soluzione).
   - Se il primale è **inammissibile**, il duale è **inammissibile** oppure **illimitato**.

## Risposta da Esame Standard

La teoria della dualità lega in modo indissolubile due problemi di PL. Il teorema di **dualità debole** dimostra che ogni soluzione ammissibile del primale ($\max$) ha valore inferiore o uguale ad ogni soluzione ammissibile del duale ($\min$), garantendo che $\mathbf{c}\mathbf{x} \le \mathbf{y}\mathbf{b}$. Il teorema di **dualità forte** stabilisce che, all'ottimo finito, non vi è divario di dualità (duality gap), cioè $Z^* = W^*$. Di conseguenza, l'uguaglianza $\mathbf{c}\mathbf{x} = \mathbf{y}\mathbf{b}$ costituisce una condizione necessaria e sufficiente di ottimalità per una coppia di soluzioni ammissibili.
