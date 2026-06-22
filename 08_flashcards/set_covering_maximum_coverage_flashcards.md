# Flashcards — Set Covering e Maximum Coverage

Q: Qual è l'obiettivo in un problema di Set Covering?
A: Coprire tutte le zone o soddisfare tutti i requisiti di domanda minimizzando il costo o il numero totale di elementi scelti.

Q: Qual è il vincolo di copertura tipico nel Set Covering?
A: $\sum_{i \in I} a_{ji} x_i \ge 1$ per ogni zona $j$ da coprire, con $x_i \in \{0, 1\}$.

Q: Qual è l'obiettivo in un problema di Maximum Coverage?
A: Massimizzare l'utilità totale o la popolazione coperta rispettando un vincolo di budget (es. selezionare al massimo $k$ servizi).

Q: Perché nel Maximum Coverage sono necessarie le variabili ausiliarie $y_j$?
A: Per rappresentare lo stato di copertura binario della zona $j$ ed evitare il doppio conteggio della popolazione qualora la zona fosse coperta da più installazioni contemporaneamente.

Q: Qual è il vincolo che lega la copertura $y_j$ e l'installazione $x_i$ nel Maximum Coverage?
A: $y_j \le \sum_{i \in I} a_{ji} x_i$ per ogni zona $j$, costringendo $y_j$ a zero se non ci sono servizi attivi per coprirla.
