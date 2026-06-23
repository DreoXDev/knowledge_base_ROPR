# MC - Totale Unimodularità e Rilassamento Continuo

## Quando Usarla
Per dimostrare teoricamente che la soluzione ottima di un problema di programmazione lineare intera (PLI) o binaria può essere ricavata risolvendo il suo rilassamento continuo. Viene richiesto frequentemente negli esercizi su grafi e reti di flusso.

## Proprietà Teoriche
Una matrice $A$ è **totalmente unimodulare (TUM)** se ogni sottomatrice quadrata di $A$ ha determinante pari a $-1, 0$ o $1$.
*   **Teorema**: Se $A$ è TUM e il vettore dei termini noti $b$ è intero, i vertici (soluzioni di base ammissibili) del poliedro $P = \{x : Ax \le b, x \ge 0\}$ sono interi.
*   Poiché l'algoritmo del simplesso esamina esclusivamente i vertici del poliedro, esso restituirà una soluzione ottima che è garantita essere intera.

## Procedura da Esame
Quando la traccia chiede di "spiegare perché è possibile risolvere il problema tramite rilassamento continuo":
1.  Dichiarare che la matrice dei coefficienti dei vincoli è la **matrice di incidenza nodo-arco** di un grafo orientato (o la sua trasposta).
2.  Spiegare che ogni colonna contiene esattamente due elementi non nulli (un $+1$ e un $-1$), il che costituisce una condizione sufficiente affinché la matrice sia **totalmente unimodulare (TUM)**.
3.  Evidenziare che i termini noti (bilanci dei nodi $b_i$ o capacità degli archi $u_{ij}$) sono interi.
4.  Concludere che, in virtù del teorema di Hoffman-Kruskal, tutti i vertici del poliedro associato sono interi, consentendo la risoluzione esatta sul rilassamento continuo tramite il metodo del simplesso.

## Mini Esempio
Problema di assegnamento con 2 lavoratori e 2 attività. Matrice dei vincoli:
$$
A = \begin{pmatrix}
1 & 1 & 0 & 0 \\
0 & 0 & 1 & 1 \\
1 & 0 & 1 & 0 \\
0 & 1 & 0 & 1
\end{pmatrix}
$$
La sottomatrice formata da qualsiasi combinazione di righe e colonne ha determinante $\in \{-1, 0, 1\}$. Essendo la parte sinistra del sistema TUM e il lato destro pari a $(1, 1, 1, 1)^T$ (intero), la soluzione del rilassamento continuo sarà intera.

## Errori Comuni
*   Affermare che *ogni* soluzione ottima del rilassamento continuo è intera: in caso di ottimi multipli continui, solo i vertici ottimi sono sicuramente interi.
*   Confondere la matrice dei coefficienti con la funzione obiettivo.

## Fonti
*   `modelli_PLI.pdf`, Sezioni 2.1 - 2.3
