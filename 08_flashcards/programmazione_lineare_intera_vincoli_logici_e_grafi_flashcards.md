# Flashcard — PLI (Vincoli Logici e Grafi)

## Vincoli Logici e Tecnica Big-M

Q: Come si formula il vincolo di attivazione superiore per cui la produzione $x_i$ può essere positiva solo se la fabbrica $i$ viene aperta ($y_i = 1$)?
A: $x_i \le U_i y_i$ dove $U_i$ è la capacità produttiva massima e $y_i \in \{0, 1\}$.

Q: Come si impone una quantità minima di produzione $L_i$ nel caso in cui si decida di produrre il bene $i$?
A: $x_i \ge L_i y_i$ dove $y_i \in \{0, 1\}$ è la variabile binaria di attivazione.

Q: Cos'è e a cosa serve la tecnica Big-M?
A: Serve a linearizzare vincoli condizionali utilizzando una costante reale positiva $M$ molto grande per disattivare un vincolo quando una variabile binaria è pari a $0$.

Q: Qual è il pericolo di scegliere una costante $M$ eccessivamente grande?
A: Genera instabilità numerica nei solver e rende il rilassamento continuo debole, aumentando il gap di dualità.

## Grafi e Totale Unimodularità

Q: Come si esprime il vincolo di conservazione del flusso a un nodo intermedio $i$?
A: Flusso entrante uguale a flusso uscente: $\sum_{j : (j, i) \in A} x_{ji} - \sum_{j : (i, j) \in A} x_{ij} = 0$.

Q: Quali sono i bilanci dei nodi per formulare il cammino minimo da $s$ a $t$ come flusso su rete?
A: Bilancio sorgente $b_s = -1$, destinazione $b_t = 1$, nodi intermedi $b_i = 0$.

Q: Cos'è una matrice totalmente unimodulare (TUM)?
A: Una matrice in cui ogni sottomatrice quadrata ha determinante pari a $-1$, $0$ o $1$.

Q: Perché la totale unimodularità è importante in PLI?
A: Perché se la matrice dei vincoli è TUM e i termini noti sono interi, i vertici del rilassamento continuo sono interi, rendendolo risolvibile all'ottimo con il simplesso.
