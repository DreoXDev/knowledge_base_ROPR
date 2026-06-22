# Flashcards — Cammino Minimo e Dualità

## Cammino minimo

Q: Quali variabili si usano nella formulazione PL del cammino minimo?
A: Variabili binarie $x_{ij}$, con $x_{ij}=1$ se l'arco $(i,j)$ appartiene al cammino, $0$ altrimenti.

Q: Qual è la funzione obiettivo del cammino minimo?
A: $$ \min \sum_{(i,j)\in A} c_{ij}x_{ij} $$

Q: Qual è il vincolo per un nodo intermedio nel cammino minimo?
A: $$ \sum_{j:(i,j)\in A}x_{ij} - \sum_{j:(j,i)\in A}x_{ji}=0 $$

Q: Qual è il vincolo per il nodo origine nel cammino minimo?
A: Deve uscire esattamente un arco attivo: $$ \sum_{j:(s,j)\in A}x_{sj}=1 $$

Q: Qual è il vincolo per il nodo destinazione nel cammino minimo?
A: Deve entrare esattamente un arco attivo: $$ \sum_{j:(j,t)\in A}x_{jt}=1 $$

## Dualità

Q: Se il primale è un MAX, il duale è?
A: Un MIN.

Q: In un primale MAX, un vincolo $\le$ genera che tipo di variabile duale?
A: Una variabile duale non negativa ($y_i \ge 0$).

Q: In un primale MAX, un vincolo $\ge$ genera che tipo di variabile duale?
A: Una variabile duale non positiva ($y_i \le 0$).

Q: In un primale MAX, un vincolo $=$ genera che tipo di variabile duale?
A: Una variabile duale libera (senza vincolo di segno).

Q: In un primale MAX, una variabile $x_j \ge 0$ genera che vincolo duale?
A: Un vincolo duale $\ge$.

Q: In un primale MAX, una variabile libera genera che vincolo duale?
A: Un vincolo duale di uguaglianza ($=$).

Q: Cosa rappresentano economicamente le variabili duali nel problema di produzione?
A: Prezzi unitari o prezzi ombra delle risorse.

Q: Cosa dice la dualità forte?
A: Se primale e duale hanno ottimo finito, allora i valori ottimi delle funzioni obiettivo coincidono: $Z^* = Z'^*$.
