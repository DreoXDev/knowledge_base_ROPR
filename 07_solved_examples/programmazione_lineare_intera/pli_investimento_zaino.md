---
fonte: modelli_PLI.pdf
area: Programmazione Lineare Intera
priorita: alta
stato: completato
---

# PLI - Esempio Svolto: Investimento e Zaino Binario

## Fonte
`modelli_PLI.pdf`, Sezione 2.7 (Modelli combinatori/applicativi)

## Descrizione del Problema
Un investitore ha a disposizione un capitale totale $C$ da investire tra $n$ possibili progetti. Ciascun progetto $j$ richiede un capitale iniziale $p_j$ e garantisce un ritorno economico atteso pari a $v_j$. L'investitore desidera selezionare il portafoglio di investimenti ottimale per massimizzare il ritorno economico totale, senza superare il budget a disposizione. Ciascun progetto può essere o selezionato o escluso (decisione binaria).

## Schema da Esame

### Indici e Insiemi
*   $j \in \{1, \dots, n\}$: Insieme dei progetti disponibili per l'investimento.

### Parametri
*   $v_j$: Valore o profitto atteso generato dal progetto $j$.
*   $p_j$: Capitale richiesto (peso) per finanziare il progetto $j$.
*   $C$: Capitale totale disponibile (capacità).

### Variabili Decisionali
*   $x_j \in \{0, 1\}$: Vale $1$ se si sceglie di finanziare il progetto $j$, $0$ altrimenti.

### Modello Matematico (Zaino Binario)

$$
\max \quad \sum_{j=1}^n v_j x_j
$$

Soggetto al vincolo:

*   **Vincolo di budget (capacità dello zaino)**:
    $$
    \sum_{j=1}^n p_j x_j \le C
    $$

*   **Dominio delle variabili**:
    $$
    x_j \in \{0, 1\} \quad \forall j = 1, \dots, n
    $$

## Note Teoriche
Il problema dello zaino binario (0-1 Knapsack Problem) è uno dei problemi di ottimizzazione combinatoria più celebri. Sebbene la sua formulazione matematica sia estremamente semplice (una sola riga di vincolo e variabili binarie), la sua risoluzione all'ottimo è NP-hard. 
A differenza dei problemi su grafo con matrice TUM, il rilassamento continuo dello zaino non ha vertici interi. Risolvendo il rilassamento continuo, la soluzione ottima si ottiene ordinando gli elementi per rendimento specifico decrescente $\frac{v_j}{p_j}$ e inserendoli nello zaino fino a saturazione; l'ultimo elemento inserito sarà tipicamente frazionario.

## Errori da Evitare
*   Scrivere il vincolo di capacità come uguaglianza ($=$): il budget non deve necessariamente essere speso tutto.
*   Dimenticare il dominio binario $x_j \in \{0, 1\}$ e scrivere $x_j \ge 0$, il che trasformerebbe il problema in un PL continuo banalmente risolvibile.
