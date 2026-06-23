---
fonte: modelli_PLI.pdf
area: Programmazione Lineare Intera
priorita: alta
stato: completato
---

# PLI - Esempio Svolto: Facility Location Capacitated

## Fonte
`modelli_PLI.pdf`, Sezione 2.6 (Modelli combinatori/applicativi)

## Descrizione del Problema
Si deve decidere quali magazzini/depositi attivare tra $n$ possibili siti e come assegnare $m$ clienti a tali magazzini. Ogni magazzino $j$ ha un costo fisso di apertura $f_j$ e una capacità massima $U_j$. Ciascun cliente $i$ ha una domanda $d_i$ che deve essere soddisfatta. Spedire dal magazzino $j$ al cliente $i$ comporta un costo unitario $c_{ij}$. Si vuole minimizzare la somma dei costi di apertura e spedizione.

## Schema da Esame

### Indici e Insiemi
*   $I = \{1, \dots, m\}$: Insieme dei clienti.
*   $J = \{1, \dots, n\}$: Insieme dei possibili siti per i magazzini.

### Parametri
*   $f_j$: Costo fisso di apertura del magazzino $j$.
*   $U_j$: Capacità massima di stoccaggio/spedizione del magazzino $j$.
*   $d_i$: Domanda di prodotto del cliente $i$.
*   $c_{ij}$: Costo unitario di trasporto dal magazzino $j$ al cliente $i$.

### Variabili Decisionali
*   $y_j \in \{0, 1\}$: Vale $1$ se si decide di aprire il magazzino $j$, $0$ altrimenti.
*   $x_{ij} \ge 0$: Frazione (o quantità) della domanda del cliente $i$ soddisfatta dal magazzino $j$. 
    *   *Nota*: Se ciascun cliente deve essere servito da un unico magazzino, allora $x_{ij} \in \{0, 1\}$. Qui formuliamo il caso generale in cui il flusso è continuo.

### Modello Matematico

$$
\min \quad \sum_{j=1}^n f_j y_j + \sum_{i=1}^m \sum_{j=1}^n c_{ij} d_i x_{ij}
$$

Soggetto ai vincoli:

*   **Soddisfacimento della domanda**: Ciascun cliente $i$ deve ricevere il 100% della sua domanda:
    $$
    \sum_{j=1}^n x_{ij} = 1 \quad \forall i \in I
    $$

*   **Capacità dei magazzini ed attivazione**: La somma delle richieste inviate a ciascun magazzino $j$ non può superare la sua capacità se aperto, e deve essere zero se chiuso:
    $$
    \sum_{i=1}^m d_i x_{ij} \le U_j y_j \quad \forall j \in J
    $$

*   **Dominio delle variabili**:
    $$
    x_{ij} \ge 0 \quad \forall i \in I, \forall j \in J
    $$
    $$
    y_j \in \{0, 1\} \quad \forall j \in J
    $$

## Varianti Comuni
*   **Assegnamento Unico (Single-Source)**: Se il cliente deve essere servito da un solo magazzino, il dominio di $x_{ij}$ diventa binario:
    $$
    x_{ij} \in \{0, 1\} \quad \forall i \in I, \forall j \in J
    $$
*   **Vincoli di Assegnamento Forte**: Spesso si aggiungono i vincoli $x_{ij} \le y_j$ per ogni coppia $(i, j)$ per rafforzare il rilassamento continuo del poliedro.

## Errori da Evitare
*   Dimenticare di moltiplicare il costo unitario $c_{ij}$ per la quantità $d_i$ nella funzione obiettivo (se $x_{ij}$ è la frazione di domanda) o non definire correttamente le unità di misura.
*   Omettere il vincolo di attivazione $U_j y_j$, il che consentirebbe di soddisfare le domande dai depositi senza pagare il relativo costo fisso di apertura.
