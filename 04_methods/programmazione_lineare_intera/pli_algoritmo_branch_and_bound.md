---
type: method
topic: programmazione_lineare_intera
status: active
sources: [branch_and_bound.pdf, 16_esercizi_BB.pdf]
reliability: official
---

# Algoritmo Branch and Bound per PLI Generale

## Quando Usarla
Per risolvere manualmente o descrivere la risoluzione di un problema di Programmazione Lineare Intera (MIP o PLI) a variabili intere generiche, partendo dall'analisi del rilassamento continuo.

## Procedura da Esame Passo-Passo

Sia dato un problema di massimizzazione con valore ottimo intero sconosciuto $Z^*$.

### Passo 1: Inizializzazione (Nodo Radice $P_0$)
1.  **Soluzione incombente**: Impostare la migliore soluzione intera nota $x_I$ e il suo valore $v_I(P_0) = Z_I$. Se non è nota alcuna soluzione ammissibile, porre $Z_I = -\infty$. (Spesso si ricava una prima soluzione intera arrotondando la soluzione del rilassamento continuo).
2.  **Risoluzione del rilassamento continuo**: Risolvere il problema senza i vincoli di integrità. Sia $x^*$ la soluzione ottima del rilassamento continuo e $Z_C$ il suo valore obiettivo ($vS(P_0) = Z_C$).
3.  **Verifica di ottimalità**:
    *   Se il rilassamento continuo è inammissibile $\implies$ il problema intero è inammissibile. Chiudere il nodo.
    *   Se la soluzione $x^*$ è intera $\implies$ $x^*$ è ottima anche per il problema intero. Fine.
    *   Se $x^*$ ha componenti frazionarie $\implies$ il nodo rimane aperto. Procedere al branching.

### Passo 2: Selezione del Nodo e Branching
1.  **Scelta del nodo**: Selezionare un nodo aperto secondo la regola di visita stabilita (Ampiezza, Profondità o Miglior Bound).
2.  **Scelta della variabile di branching**: Selezionare una variabile $x_i$ che assume un valore frazionario $x_i^*$ nell'ottimo del rilassamento del nodo corrente. (Spesso si sceglie la variabile con indice più basso o quella più vicina a un intero).
3.  **Partizionamento**: Creare due sotto-problemi (nodi figli) aggiungendo rispettivamente i vincoli:
    $$
    x_i \le \lfloor x_i^* \rfloor \quad \text{e} \quad x_i \ge \lceil x_i^* \rceil
    $$

### Passo 3: Valutazione (Bounding) e Potatura (Fathoming)
Per ciascun nodo figlio generato:
1.  **Risolvere il rilassamento continuo** del sotto-problema (es. tramite simplesso o metodo grafico). Sia $\bar{x}$ l'ottimo ottenuto e $Z_S$ il suo valore.
2.  **Applicare le regole di potatura (Fathoming)** in ordine:
    *   *Inammissibilità*: Se il rilassamento continuo non ha soluzioni ammissibili $\implies$ chiudere il nodo.
    *   *Dominanza*: Se $Z_S \le Z_I$ (per massimo) $\implies$ chiudere il nodo (il sotto-problema non contiene soluzioni migliori della soluzione incombente corrente).
    *   *Ottimalità intera*: Se la soluzione $\bar{x}$ è intera:
        *   Se $Z_S > Z_I \implies$ aggiornare la soluzione incombente $Z_I = Z_S$ e $x_I = \bar{x}$.
        *   Chiudere il nodo.
3.  Se il nodo non viene chiuso da nessuna delle tre regole, esso rimane aperto e pronto per un successivo branching.

### Passo 4: Terminazione
L'algoritmo termina quando non vi sono più nodi aperti nell'albero delle soluzioni. La soluzione ottima del problema intero è la soluzione incombente corrente $x_I$ con valore $Z_I = Z^*$. Se $Z_I = -\infty$, il problema intero è inammissibile.
