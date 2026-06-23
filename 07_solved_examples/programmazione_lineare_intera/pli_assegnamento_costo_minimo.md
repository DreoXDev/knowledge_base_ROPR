---
fonte: modelli_PLI.pdf
area: Programmazione Lineare Intera
priorita: alta
stato: completato
---

# PLI - Esempio Svolto: Assegnamento di Costo Minimo

## Fonte
`modelli_PLI.pdf`, Sezione 2.1 (Problemi su grafi)

## Descrizione del Problema
Si consideri il problema di assegnare $n$ impiegati a $n$ diverse attività. Ciascun impiegato $i$ può svolgere ciascuna attività $j$ con un costo $c_{ij}$. L'obiettivo è assegnare ogni impiegato a un'unica attività e ogni attività a un unico impiegato in modo da minimizzare il costo totale.

## Schema da Esame

### Indici e Insiemi
*   $I = \{1, \dots, n\}$: Insieme degli impiegati.
*   $J = \{1, \dots, n\}$: Insieme delle attività.

### Parametri
*   $c_{ij}$: Costo associato all'assegnamento dell'impiegato $i$ all'attività $j$.

### Variabili Decisionali
*   $x_{ij} \in \{0, 1\}$: Vale $1$ se l'impiegato $i$ è assegnato all'attività $j$, $0$ altrimenti.

### Modello Matematico

$$
\min \quad \sum_{i=1}^n \sum_{j=1}^n c_{ij} x_{ij}
$$

Soggetto ai vincoli:

*   **Assegnamento impiegati**: Ciascun impiegato $i$ svolge esattamente un'attività:
    $$
    \sum_{j=1}^n x_{ij} = 1 \quad \forall i \in I
    $$

*   **Assegnamento attività**: Ciascuna attività $j$ viene svolta da esattamente un impiegato:
    $$
    \sum_{i=1}^n x_{ij} = 1 \quad \forall j \in J
    $$

*   **Dominio delle variabili**:
    $$
    x_{ij} \in \{0, 1\} \quad \forall i \in I, \forall j \in J
    $$

## Nota Teorica (Rilassamento Continuo)
Poiché il modello è formulato come flusso su grafo bipartito, la matrice dei vincoli è totalmente unimodulare (TUM). Se si risolve il rilassamento continuo (sostituendo il dominio binario con $0 \le x_{ij} \le 1$), il metodo del simplesso garantisce una soluzione ottima a valori interi.

## Errori da Evitare
*   Scrivere vincoli di disuguaglianza ($\ge 1$ o $\le 1$) invece di uguaglianza ($= 1$), a meno che la traccia espliciti che alcuni lavoratori possano rimanere inattivi o alcune attività non debbano essere svolte.
*   Utilizzare indici diversi per righe e colonne se il numero di impiegati e attività è identico.
