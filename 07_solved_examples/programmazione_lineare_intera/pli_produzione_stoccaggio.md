---
fonte: modelli_PLI.pdf
area: Programmazione Lineare Intera
priorita: alta
stato: completato
---

# PLI - Esempio Svolto: Produzione e Stoccaggio Multi-periodo

## Fonte
`modelli_PLI.pdf`, Sezione 2.5 (Modelli combinatori/applicativi)

## Descrizione del Problema
Un'azienda deve pianificare la produzione di un bene su un orizzonte temporale suddiviso in $T$ periodi (mesi). Per ciascun mese $t$ è nota la domanda $d_t$ che deve essere interamente soddisfatta. L'azienda può produrre nel mese $t$ a un costo unitario $p_t$ ed è soggetta a capacità minima $L_t$ e massima $U_t$ di produzione. La merce non venduta può essere immagazzinata al costo unitario di stoccaggio $h_t$ per mese. La capacità massima del magazzino è $S$. Si assume che le scorte iniziali siano $I_0$ e si vuole determinare il piano a costo minimo.

## Schema da Esame

### Indici e Insiemi
*   $t \in \{1, \dots, T\}$: Periodi dell'orizzonte temporale.

### Parametri
*   $d_t$: Domanda del periodo $t$.
*   $p_t$: Costo unitario di produzione nel periodo $t$.
*   $h_t$: Costo unitario di stoccaggio nel periodo $t$.
*   $L_t$: Produzione minima consentita (se si produce).
*   $U_t$: Capacità produttiva massima del periodo $t$.
*   $S$: Capacità massima del magazzino.
*   $I_0$: Scorta iniziale a magazzino.

### Variabili Decisionali
*   $x_t \ge 0$: Quantità prodotta nel periodo $t$.
*   $s_t \ge 0$: Quantità di merce in magazzino alla fine del periodo $t$ (scorta finale del periodo $t$).
*   $y_t \in \{0, 1\}$: Vale $1$ se si decide di produrre nel periodo $t$, $0$ altrimenti.

### Modello Matematico

$$
\min \quad \sum_{t=1}^T (p_t x_t + h_t s_t)
$$

Soggetto ai vincoli:

*   **Equazione di bilancio del magazzino**:
    $$
    s_t = s_{t-1} + x_t - d_t \quad \forall t = 1, \dots, T
    $$
    dove $s_0 = I_0$ (valore dato).

*   **Vincoli di attivazione e capacità di produzione**:
    $$
    L_t y_t \le x_t \le U_t y_t \quad \forall t = 1, \dots, T
    $$

*   **Capacità massima di magazzino**:
    $$
    s_t \le S \quad \forall t = 1, \dots, T
    $$

*   **Dominio delle variabili**:
    $$
    x_t \ge 0, \quad s_t \ge 0, \quad y_t \in \{0, 1\} \quad \forall t = 1, \dots, T
    $$

## Note di Modellazione
*   La formula del bilancio esprime che il magazzino alla fine del mese $t$ è pari al magazzino iniziale (che equivale a quello del mese precedente $s_{t-1}$) più la produzione del mese corrente $x_t$ meno la domanda soddisfatta $d_t$.
*   Il costo di magazzino è calcolato qui a fine periodo ($h_t s_t$). Alcuni modelli calcolano il costo sulla scorta media del periodo $\frac{s_{t-1} + s_t}{2}$, in tal caso basta modificare la funzione obiettivo di conseguenza.

## Errori da Evitare
*   Scrivere $s_t = s_{t+1} + x_t - d_t$: il tempo scorre in avanti, quindi la scorta finale $s_t$ dipende dal passato $s_{t-1}$.
*   Dimenticare di porre $s_0 = I_0$ o di dichiarare la non negatività di $s_t$ (se $s_t$ potesse essere negativa, significherebbe accumulare ritardi sulla domanda, ossia "backlogging", che non è consentito a meno che specificato).
