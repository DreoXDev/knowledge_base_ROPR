---
materia: ROPR
area: Programmazione Lineare
tipo: metodo
fonte: Ricerca Operativa - Teoria del Simplesso - 23-24.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - simplesso
  - teoria
  - method-card
---

# METHOD CARD — Teoria del Simplesso

## Quando usarla
Usare questa card per rispondere a domande teoriche riguardanti i fondamenti geometrici e algebrici dell'algoritmo del simplesso (ad esempio: "Perché il simplesso si muove tra i vertici?").

## Idee e Definizioni Chiave

1. **Regione ammissibile come Poliedro**: La regione ammissibile di un problema di PL è descritta geometricamente da un poliedro convesso.
2. **Vincoli e Iperpiani**: Ciascun vincolo $\le$ o $\ge$ definisce un semispazio. Le corrispondenti equazioni di frontiera (con $=$) definiscono degli iperpiani.
3. **Vertici come Intersezioni**: Un vertice ammissibile è un punto in cui si incontrano almeno $n$ iperpiani indipendenti di frontiera e che soddisfa tutti i vincoli.
4. **Proprietà dell'Ottimo**: Se esiste una soluzione ottima finita, esiste almeno un vertice ammissibile che è ottimo.
5. **Adiacenza e Spigoli**: Due vertici ammissibili sono adiacenti se condividono $n-1$ frontiere di vincolo. Lo spostamento lungo uno spigolo che li unisce equivale al cambio di una sola variabile di base (algebricamente).

## Risposta da Esame Standard

La ricerca dell'ottimo in un problema di PL può essere ristretta ai soli vertici ammissibili della regione ammissibile perché, se il problema ammette ottimo finito, esiste sempre almeno una soluzione ottima situata in uno dei vertici. Il metodo del simplesso sfrutta questa proprietà muovendosi in modo sistematico lungo gli spigoli (l'intersezione di $n-1$ frontiere attive) passando da un vertice ammissibile ad un altro adiacente che migliori $Z$. Algebricamente, questo movimento corrisponde ad un cambio di base (operazione di pivot) in cui una sola variabile entra in base e una sola esce.
