# Flashcard — Programmazione Lineare Intera (B&B Binario)

## Algoritmo di Branch and Bound Binario

Q: Come avviene il branching per una variabile binaria $x_k$ in un problema 0-1?
A: Si divide l'insieme ammissibile in due sotto-problemi fissando la variabile a $x_k = 0$ (ramo sinistro) e $x_k = 1$ (ramo destro).

Q: Cos'è la regola dell'ordinamento naturale nel branching binario?
A: È una scelta euristica che consiste nel selezionare la variabile di branching in base al suo indice progressivo ($x_1$ al primo livello, $x_2$ al secondo, ecc.), indipendentemente dal fatto che sia frazionaria o meno nella soluzione rilassata corrente.

Q: Quando e come è possibile arrotondare all'intero il bound di un nodo nel B&B?
A: Se tutti i coefficienti della funzione obiettivo sono interi, l'ottimo intero deve essere intero. Quindi, per un problema di massimo, il bound reale $Z_C$ del rilassamento continuo può essere arrotondato per difetto: $Z_S = \lfloor Z_C \rfloor$. Per un problema di minimo, si arrotonda per eccesso: $Z_S = \lceil Z_C \rceil$.

Q: Quali sono i tre criteri di chiusura (fathoming) di un nodo nel B&B binario?
A: 
1. **Ottimalità Intera**: La soluzione rilassata rispetta l'integrità (tutte le variabili sono $0$ o $1$). Si aggiorna l'incumbent se migliora.
2. **Inammissibilità**: Il rilassamento continuo è privo di soluzioni ammissibili ($\emptyset$).
3. **Dominanza**: Il bound del nodo (arrotondato) è inferiore o uguale all'incumbent corrente ($Z_S \le Z_I$ per massimo).

Q: Perché le relazioni di contingenza logica (es. $x_3 \le x_1$) aiutano nella potatura del B&B?
A: Perché fissare la variabile indipendente a $0$ ($x_1 = 0$) costringe immediatamente anche la variabile condizionata a $0$ ($x_3 = 0$), riducendo lo spazio delle soluzioni ed evidenziando rapidamente l'inammissibilità o riducendo il bound dei nodi figli.

Q: In un problema di massimo, se ho incumbent $Z_I = 14$ e un nodo aperto ha soluzione rilassata con $Z_C = 14.8$ e coefficienti interi, il nodo va chiuso?
A: Sì. Poiché i coefficienti sono interi, il bound viene arrotondato per difetto a $\lfloor 14.8 \rfloor = 14$. Essendo il bound $14 \le Z_I = 14$, il nodo viene chiuso per dominanza.
