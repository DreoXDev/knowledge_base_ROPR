---
type: method
topic: programmazione_lineare_intera
status: active
sources: [Programmazione Lineare Intera_Branch and Bound binario.pdf]
reliability: official
---

# Algoritmo Branch and Bound per PLI Binaria

## Quando Usarla
Per risolvere problemi in cui tutte le variabili decisionali sono vincolate ad essere binarie, ossia $x_i \in \{0, 1\}$.

## Procedura da Esame Passo-Passo

Sia dato un problema di massimizzazione a variabili binarie.

### 1. Inizializzazione
*   Impostare il valore della migliore soluzione intera nota $Z_I$ (incombente). Se non disponibile, porre $Z_I = -\infty$.
*   Risolvere il rilassamento continuo sostituendo il dominio $x_i \in \{0, 1\}$ con il vincolo continuo:
    $$
    0 \le x_i \le 1 \quad \forall i = 1, \dots, n
    $$
*   Sia $x^*$ la soluzione ottima del rilassamento continuo e $Z_C$ il suo valore.

### 2. Scelta del Branching (Fissare a 0 o 1)
Se la soluzione ottima $x^*$ non è intera:
*   Selezionare una variabile frazionaria $x_k^*$ (solitamente si segue l'ordinamento naturale $x_1, x_2, \dots$ o si sceglie quella con parte frazionaria più vicina a $0.5$).
*   Generare due sotto-problemi (nodi figli) imponendo rispettivamente:
    *   **Nodo Figlio Sinistro**: $x_k = 0$
    *   **Nodo Figlio Destro**: $x_k = 1$
*   In questo modo, la variabile $x_k$ viene "fissata" e cessa di essere una variabile decisionale libera nei nodi figli.

### 3. Valutazione e Potatura
Nei nodi figli, il rilassamento continuo viene risolto tenendo conto delle variabili già fissate nei nodi superiori dell'albero.
Le regole di potatura (fathoming) rimangono le medesime:
*   **Inammissibilità**: Se fissare $x_k$ viola le capacità o rende i vincoli inammissibili $\implies$ chiudere il nodo.
*   **Dominanza**: Se il bound superiore $Z_S \le Z_I \implies$ chiudere il nodo.
*   **Ottimalità intera**: Se tutte le variabili libere del rilassamento assumono valore intero ($0$ o $1$):
    *   Se $Z_S > Z_I \implies$ aggiornare $Z_I = Z_S$ e registrare la nuova soluzione.
    *   Chiudere il nodo.

## Rappresentazione Grafica dell'Albero
All'esame, l'albero di enumerazione si rappresenta graficamente con cerchi o rettangoli per i nodi ($P_0, P_1, \dots$):
*   Sui rami che uniscono i nodi si scrive il vincolo inserito ($x_k = 0$ o $x_k = 1$).
*   All'interno o a fianco di ciascun nodo si scrive:
    *   La soluzione ottima del rilassamento continuo ($x$).
    *   Il valore del bound ($vS = Z_S$).
    *   Se il nodo viene chiuso, il motivo della chiusura (es. "chiuso per interezza", "chiuso per dominanza", "chiuso per inammissibilità $\emptyset$").
