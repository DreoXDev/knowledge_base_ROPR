# MC - Algoritmo Branch and Bound (PLI)

## Quando Usarla
Per risolvere in forma algoritmica problemi di programmazione lineare intera (generica o binaria) partendo dalla risoluzione del rilassamento continuo.

## Variabili Tipiche
*   $x_i$: Variabili del problema originale.
*   $Z_S$: Valutazione superiore (upper bound per massimo) associata a ciascun nodo, calcolata risolvendo il rilassamento continuo.
*   $Z_I$: Valutazione inferiore (soluzione incombente), corrispondente alla migliore soluzione intera trovata fino a quel momento.

## Procedura da Esame
1.  **Inizializzazione**: Porre la soluzione incombente $Z_I = -\infty$ (o il valore di una soluzione intera ammissibile calcolata tramite euristica/arrotondamento). Risolvere il rilassamento continuo del nodo radice.
2.  **Branching**: Se la soluzione non è intera, ramificare su una variabile frazionaria $x_k^*$:
    *   *PLI Generale*: creare due nodi figli con vincoli $x_k \le \lfloor x_k^* \rfloor$ e $x_k \ge \lceil x_k^* \rceil$.
    *   *PLI Binaria*: creare due nodi figli ponendo $x_k = 0$ e $x_k = 1$.
3.  **Visita**: Esplorare l'albero seguendo la regola indicata (ampiezza, profondità o miglior bound).
4.  **Fathoming (Potatura)**: Chiudere ciascun nodo nei seguenti casi:
    *   *Inammissibilità*: Il rilassamento continuo non ha soluzioni ammissibili ($\emptyset$).
    *   *Ottimalità intera*: La soluzione ottima del rilassamento è intera. Se $Z > Z_I$, aggiornare la soluzione incombente $Z_I = Z$ e registrare la soluzione.
    *   *Dominanza*: Il bound del rilassamento $Z_S \le Z_I$ (per massimo).
5.  **Fine**: Terminare quando tutti i nodi sono chiusi. La soluzione incombente corrente è l'ottimo.

## Mini Esempio
Problema di massimo, incumbent $Z_I = 39$. Un nodo figlio ha come ottimo del rilassamento continuo $x^* = (2, 3.5)$ con valore $Z_S = 38.8$.
*   Poiché $Z_S = 38.8 \le 39$ (incumbent), il nodo viene chiuso immediatamente per dominanza (potatura), senza dover esplorare ulteriormente.

## Errori Comuni
*   Dimenticare di aggiornare la soluzione incombente $Z_I$ quando si incontra una soluzione intera migliore.
*   Ramificare su variabili che sono già intere nell'ottimo del rilassamento corrente.

## Vedi Anche
*   [MC_PLI_branch_and_bound_plim.md](MC_PLI_branch_and_bound_plim.md): Branch and Bound specifico per problemi interi misti (PLIM).
*   [MC_PLI_interpretare_albero_branch_and_bound.md](MC_PLI_interpretare_albero_branch_and_bound.md): Risoluzione di quesiti basati su alberi esistenti.
*   [MC_PLI_gap_ottimalita_branch_and_bound.md](MC_PLI_gap_ottimalita_branch_and_bound.md): Calcolo del gap di ottimalità assoluto/relativo.
*   [MC_PLI_soluzione_quasi_ottima_branch_and_bound.md](MC_PLI_soluzione_quasi_ottima_branch_and_bound.md): Criteri di arresto anticipato.

## Fonti
*   `branch_and_bound.pdf`, `16_esercizi_BB.pdf`, `BB PLI.pdf`
