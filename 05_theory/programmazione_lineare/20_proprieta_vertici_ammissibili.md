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
  - vertici
  - ottimalita
  - combinazione-convessa
---

# Proprietà dei vertici ammissibili

La Programmazione Lineare poggia su teoremi fondamentali che riducono drasticamente lo sforzo computazionale necessario per trovare la soluzione ottima.

## 1. Proprietà dell'Ottimo nei Vertici

> **Teorema Fondamentale**: Se un problema di Programmazione Lineare ammette almeno una soluzione ottima finita, allora esiste almeno un vertice ammissibile (soluzione di base ammissibile) che è ottimo.

### Conseguenza Pratica
- La regione ammissibile del problema contiene tipicamente infiniti punti.
- Grazie a questa proprietà, non è necessario esplorare l'intera regione ammissibile né tutti i suoi punti interni.
- La ricerca della soluzione ottima può essere limitata esclusivamente all'insieme **finito** dei vertici ammissibili del poliedro.
- Il metodo del simplesso sfrutta direttamente questo risultato, muovendosi in modo intelligente ed efficiente da un vertice all'altro lungo gli spigoli.

## 2. Proprietà delle Soluzioni Ottime Multiple (Ottimi Multipli)

Se il problema ammette più di una soluzione ottima:
- Esistono almeno due vertici ammissibili distinti, diciamo $x^{(1)}$ e $x^{(2)}$, che sono ottimi ed hanno lo stesso valore massimo (o minimo) della funzione obiettivo $Z^*$.
- Qualsiasi punto situato sul segmento o sulla faccia del poliedro che unisce questi vertici ottimi è anch'esso una soluzione ottima.
- Algebricamente, ogni soluzione ottima $x^*$ può essere rappresentata come **combinazione convessa** dei vertici ottimi:
  $$
  x^* = \lambda x^{(1)} + (1-\lambda) x^{(2)} \qquad \text{con } \lambda \in [0, 1]
  $$

---

## Risposte Breve da Esame

### Perché il simplesso controlla solo i vertici della regione ammissibile?
Il simplesso controlla solo i vertici perché, in base al teorema fondamentale della PL, se un problema ammette un ottimo finito, esiste sempre almeno una soluzione ottima situata in un vertice ammissibile della regione ammissibile. Questo riduce la ricerca dell'ottimo tra gli infiniti punti della regione ad un sottoinsieme finito di punti (i vertici).

### Cosa succede se ci sono infinite soluzioni ottime?
Se ci sono infinite soluzioni ottime (casi di ottimi multipli), esse giacciono su uno spigolo o su una faccia della regione ammissibile che collega tra loro i vertici ottimi. Algebricamente, tutte queste soluzioni ottime possono essere espresse come combinazioni convesse (medie pesate con pesi non negativi a somma pari a 1) dei vertici ammissibili ottimi trovati.
