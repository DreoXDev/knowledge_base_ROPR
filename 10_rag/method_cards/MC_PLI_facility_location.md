# MC - Facility Location Problem

## Quando Usarla
Per decidere quali siti di produzione/stoccaggio attivare tra un insieme di opzioni disponibili e come distribuire il servizio ai clienti per minimizzare la somma dei costi fissi di apertura e dei costi variabili di trasporto.

## Variabili Tipiche
*   $y_j \in \{0, 1\}$: Vale $1$ se si apre l'impianto nel sito $j$, $0$ altrimenti.
*   $x_{ij} \ge 0$: Frazione della domanda del cliente $i$ soddisfatta dall'impianto $j$ (se frazionabile).

## Modello Template
$$
\min \quad \sum_{j \in J} f_j y_j + \sum_{i \in I} \sum_{j \in J} c_{ij} d_i x_{ij}
$$
$$
\text{s.t.} \quad \sum_{j \in J} x_{ij} = 1 \quad \forall i \in I
$$
$$
\sum_{i \in I} d_i x_{ij} \le U_j y_j \quad \forall j \in J
$$
$$
x_{ij} \ge 0, \quad y_j \in \{0, 1\} \quad \forall i \in I, \forall j \in J
$$

## Procedura da Esame
1.  Definire gli insiemi di clienti $I$ e siti magazzino $J$.
2.  Dichiarare le variabili binarie $y_j$ e le variabili di assegnamento/flusso $x_{ij}$.
3.  Scrivere i vincoli di assegnamento per garantire che ogni cliente sia servito.
4.  Scrivere i vincoli di capacità degli impianti legati alla variabile di attivazione $y_j$.

## Mini Esempio
2 clienti (domande $d_1=10, d_2=15$) e 2 depositi (capacità $U_1=20, U_2=30$).
*   Servire cliente 1: $x_{11} + x_{12} = 1$
*   Servire cliente 2: $x_{21} + x_{22} = 1$
*   Capacità deposito 1: $10 x_{11} + 15 x_{21} \le 20 y_1$
*   Capacità deposito 2: $10 x_{12} + 15 x_{22} \le 30 y_2$

## Errori Comuni
*   Dimenticare di inserire la domanda $d_i$ nel vincolo di capacità: scrivere $\sum x_{ij} \le U_j y_j$ è sbagliato se $x_{ij}$ rappresenta una frazione.
*   Omettere il costo fisso nella funzione obiettivo.

## Fonti
*   `modelli_PLI.pdf`, Sezione 2.6
