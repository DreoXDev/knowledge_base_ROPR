# Flashcard — Branch and Bound (PLI)

## Algoritmo e Regole di Branch

Q: Quali sono i tre passi principali del Branch and Bound?
A: Branching (ramificazione), Bounding (valutazione tramite rilassamento continuo) e Fathoming (potatura/chiusura dei nodi).

Q: In cosa consiste il branching per una variabile intera $x_i$?
A: Se il rilassamento dà $x_i^* \notin \mathbb{Z}$, si creano due nodi aggiungendo i vincoli $x_i \le \lfloor x_i^* \rfloor$ e $x_i \ge \lceil x_i^* \rceil$.

Q: In cosa consiste il branching nel caso binario?
A: Si sceglie una variabile $x_i$ e si generano due nodi fissandola a $x_i = 0$ e $x_i = 1$.

## Regole di Potatura (Fathoming)

Q: Quali sono i tre motivi per cui un nodo viene potato (chiuso)?
A: 1) Inammissibilità del rilassamento continuo ($\emptyset$), 2) Ottimalità intera (soluzione del rilassamento intera), 3) Dominanza ($Z_S \le Z_I$ per massimo).

Q: Cos'è la soluzione incombente ($Z_I$) nel Branch and Bound?
A: È il valore della migliore soluzione ammissibile intera individuata fino ad ora nell'esplorazione dell'albero.

Q: Quando si chiude un nodo per dominanza?
A: Quando il bound superiore del nodo $Z_S$ è minore o uguale alla soluzione incombente $Z_I$ ($Z_S \le Z_I$ per massimo), rendendo inutile esplorarlo.

## Strategie di Esplorazione e Greedy

Q: Qual è la differenza tra Depth-First e Best-Bound-First?
A: Depth-First esplora il nodo più profondo per trovare rapidamente soluzioni intere ammissibili; Best-Bound-First esplora il nodo col miglior bound per ridurre i nodi totali visitati.

Q: Come si calcola la valutazione superiore ($Z_S$) dello zaino binario con l'algoritmo greedy?
A: Si ordinano gli oggetti per rendimento specifico $v_j / p_j$ decrescente e li si inserisce saturando esattamente lo zaino, inserendo eventualmente l'ultimo oggetto in frazione.
