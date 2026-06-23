# Pattern d'Esame: Riepilogo Strategico PL, PLI e PNL

## Descrizione del Pattern
Mappa strategica per identificare istantaneamente il tipo di esercizio contenuto nel compito d'esame scritto, abbinandolo alla corretta procedura e method card da consultare nella repository.

---

## Tabella di Instradamento d'Esame

| Parole Chiave nella Traccia | Area di Riferimento | Tecnica / Algoritmo da Applicare | Method Card Correlata |
|---|---|---|---|
| "stabilimenti", "punti vendita", "capacità", "domanda", "costi di spedizione" | **Programmazione Lineare (PL)** | Modello di Trasporto (formulazione) | [[MC_PL_modello_trasporto]] |
| "problema dello zaino", "Branch and Bound", "$x_i \in \{0, 1\}$", "visita in ampiezza" | **Programmazione Lineare Intera (PLI)** | Branch and Bound Zaino Binario | [[MC_PLI_branch_and_bound_zaino]] |
| "una iterazione del metodo del gradiente con line search esatta" | **Programmazione Non Lineare (PNL)** | Discesa del Gradiente | [[MC_PNL_gradiente_line_search_esatta]] |
| "una iterazione del metodo di Newton a partire dal punto" | **Programmazione Non Lineare (PNL)** | Newton Multivariabile | [[MC_PNL_newton_non_vincolata]] |
| "trovare massimi e minimi locali della funzione f(x, y)" | **Programmazione Non Lineare (PNL)** | Annullamento gradiente + Hessiana | [[MC_PNL_classificazione_hessiana]] |
| "risolvere il sistema KKT associato", "massimi e minimi globali" | **Programmazione Non Lineare (PNL)** | Condizioni KKT vincolate per casi | [[MC_PNL_KKT_generale]] |

---

## Checklist Strategica per lo Scritto

### 1. Per problemi di Modellazione PL/PLI
-   Definire sempre prima le variabili decisionali, specificando l'unità di misura (es. album/settimana, euro/km).
-   La funzione obiettivo deve indicare chiaramente il senso di ottimizzazione ($\min$ o $\max$).
-   Verificare che i vincoli percentuali o frazionari siano stati correttamente linearizzati (moltiplicando per i denominatori).

### 2. Per problemi di Branch and Bound
-   Disegnare l'albero inserendo i vincoli aggiunti su ciascun ramo.
-   Fornire una tabella riassuntiva dei nodi con: Nodo, Vincoli, Rilassamento LP continuo, Bound, Stato (aperto/chiuso) e Motivo.
-   Rispettare la regola di visita prescritta (in ampiezza o best bound).

### 3. Per problemi di Gradiente e Newton
-   **Gradiente**: Non dimenticare che la direzione di discesa per un problema di minimo è $-\nabla f(x_k)$. La line search esatta richiede di annullare la derivata della funzione ausiliaria in una variabile $\phi'(\alpha) = 0$.
-   **Newton**: Non calcolare l'inversa simbolica dell'Hessiana. Risolvere il sistema lineare $H_f d = -\nabla f$ per via algebrica diretta.

### 4. Per problemi di KKT
-   Verificare sempre la compattezza del dominio per giustificare Weierstrass.
-   Scrivere la tabella finale con tutti i casi analizzati per complementarità degli scarti, altrimenti l'esame è incompleto.

---

## Esempi di Riferimento
- [[riepilogo_pl_pli_pnl_esercizi_misti]]: risoluzione di un intero compito d'esame simulato.
