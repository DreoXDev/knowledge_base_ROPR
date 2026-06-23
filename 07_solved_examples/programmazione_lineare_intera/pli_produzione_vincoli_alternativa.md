---
fonte: modelli_PLI.pdf
area: Programmazione Lineare Intera
priorita: alta
stato: completato
---

# PLI - Esempio Svolto: Produzione con Vincoli di Alternativa

## Fonte
`modelli_PLI.pdf`, Sezione 2.4 (Modelli combinatori/applicativi)

## Descrizione del Problema
Una ditta deve decidere quali prodotti realizzare tra un insieme di prodotti possibili. Se un prodotto $i$ viene realizzato, si sostiene un costo fisso di attivazione macchinari $f_i$ e si ottiene un profitto unitario di vendita $p_i$. Inoltre, se si sceglie di produrre il bene $i$, la produzione deve essere almeno pari a una quantità minima $L_i$ ed è limitata da una capacità massima $U_i$. L'obiettivo è massimizzare il profitto totale netto.

## Schema da Esame

### Indici e Insiemi
*   $I = \{1, \dots, n\}$: Insieme dei possibili prodotti.

### Parametri
*   $p_i$: Profitto unitario del prodotto $i$.
*   $f_i$: Costo fisso di attivazione per il prodotto $i$.
*   $L_i$: Produzione minima se il prodotto $i$ è attivato.
*   $U_i$: Produzione massima (capacità) del prodotto $i$.

### Variabili Decisionali
*   $x_i \ge 0$ (continua o intera): Quantità prodotta del bene $i$.
*   $y_i \in \{0, 1\}$: Vale $1$ se si decide di produrre il bene $i$, $0$ altrimenti.

### Modello Matematico

$$
\max \quad \sum_{i=1}^n (p_i x_i - f_i y_i)
$$

Soggetto ai vincoli:

*   **Vincolo di capacità massima (attivazione superiore)**:
    $$
    x_i \le U_i y_i \quad \forall i \in I
    $$

*   **Vincolo di produzione minima (attivazione inferiore)**:
    $$
    x_i \ge L_i y_i \quad \forall i \in I
    $$

*   **Dominio delle variabili**:
    $$
    x_i \ge 0 \quad \forall i \in I
    $$
    $$
    y_i \in \{0, 1\} \quad \forall i \in I
    $$

## Interpretazione dei Vincoli
*   Se $y_i = 0$, i vincoli costringono $L_i \cdot 0 \le x_i \le U_i \cdot 0 \implies 0 \le x_i \le 0 \implies x_i = 0$. Nessun costo fisso viene pagato.
*   Se $y_i = 1$, i vincoli diventano $L_i \le x_i \le U_i$. Viene pagato il costo fisso $f_i$.

## Errori da Evitare
*   Dimenticare il costo fisso $f_i y_i$ nella funzione obiettivo.
*   Scrivere $x_i \ge L_i$ senza moltiplicare per $y_i$, il che obbligherebbe a produrre sempre il bene $i$ anche qualora $y_i = 0$.
*   Scegliere un valore arbitrario e sproporzionatamente grande per $U_i$ (Big-M) se la capacità massima è ricavabile dai dati del problema (es. disponibilità di risorse).
