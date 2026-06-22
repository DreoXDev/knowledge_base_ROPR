---
materia: ROPR
area: Programmazione Lineare
tipo: metodo
fonte: Ricerca Operativa - Teoria del Simplesso - 23-24.pdf
stato: completo
priorita: media
tags:
  - ropr
  - programmazione-lineare
  - simplesso
  - vertici
  - adiacenza
  - ottimalita
  - method-card
---

# METHOD CARD — Vertici Adiacenti e Ottimalità

## Quando usarla
Usare quando l'esercizio chiede di verificare l'adiacenza tra due vertici, descrivere il cammino del simplesso, controllare le condizioni geometriche di ottimalità o scrivere le soluzioni in caso di ottimi multipli.

## Procedura e Criteri d'Esame

### 1. Verificare l'Adiacenza tra due Vertici
Dato un problema in $n$ variabili decisionali:
- Due vertici ammissibili sono adiacenti se condividono esattamente $n-1$ equazioni di frontiera attive.
- **Verifica**:
  1. Elencare le equazioni di frontiera attive (soddisfatte con l'uguaglianza stretta) nel primo vertice $V_1$.
  2. Elencare quelle attive nel secondo vertice $V_2$.
  3. Contare quante equazioni sono presenti in entrambi gli elenchi. Se l'intersezione contiene esattamente $n-1$ equazioni, i vertici sono **adiacenti** e sono uniti da uno spigolo.

### 2. Condizione di Ottimalità Geometrica
- Un vertice ammissibile $V^*$ è ottimo globale se tutti i suoi vertici adiacenti ammissibili hanno un valore di $Z$ peggiore o uguale.
  $$
  Z(V_{\text{adiacente}}) \le Z(V^*) \quad \forall V_{\text{adiacente}} \quad (\text{per MAX})
  $$

### 3. Gestione degli Ottimi Multipli
- Se due vertici ottimi ammissibili $V_1^*$ e $V_2^*$ hanno lo stesso valore ottimo della funzione obiettivo $Z^*$:
  - Qualsiasi punto sullo spigolo che li connette (che condivide le $n-1$ frontiere attive comuni) è anch'esso una soluzione ottima.
  - Scrivere la famiglia di soluzioni ottime come **combinazione convessa**:
    $$
    x^* = \lambda V_1^* + (1-\lambda) V_2^* \qquad \forall \lambda \in [0, 1]
    $$
