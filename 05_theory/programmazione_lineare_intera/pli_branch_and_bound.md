---
type: theory
topic: programmazione_lineare_intera
status: active
sources: [branch_and_bound.pdf, BB PLI.pdf]
reliability: official
---

# Algoritmo Branch and Bound - Teoria

## Fonti
*   `branch_and_bound.pdf` (Mauro Passacantando)
*   `BB PLI.pdf`

## Idea Essenziale
Il metodo **Branch and Bound** (B&B) è una tecnica di enumerazione implicita utilizzata per risolvere problemi di ottimizzazione discreta o intera. Invece di enumerare esaustivamente tutte le possibili soluzioni (il che sarebbe impraticabile, dato che lo spazio cresce esponenzialmente), il B&B partiziona ricorsivamente la regione ammissibile in sotto-problemi (Branching) e ne calcola dei bound (Bounding) per escludere a priori porzioni di spazio che non possono contenere la soluzione ottima (Fathoming o Potatura).

## Componenti Principali del B&B

Un algoritmo di Branch and Bound è definito da tre operazioni fondamentali applicate ai nodi di un albero di enumerazione:

### 1. Branching (Ramificazione)
Consiste nel dividere il dominio delle soluzioni ammissibili di un sotto-problema in sotto-insiemi disgiunti.
*   **PLI Generale**: Se la soluzione del rilassamento continuo $\bar{x}$ ha una variabile $x_i$ con valore frazionario $x_i^* \notin \mathbb{Z}$, si generano due sotto-problemi aggiungendo rispettivamente i vincoli:
    $$
    x_i \le \lfloor x_i^* \rfloor \quad \text{e} \quad x_i \ge \lceil x_i^* \rceil
    $$
*   **PLI Binaria**: Si sceglie una variabile $x_i$ e si generano due sotto-problemi fissandola a:
    $$
    x_i = 0 \quad \text{e} \quad x_i = 1
    $$

### 2. Bounding (Valutazione)
Associa ad ogni nodo un limite (inferiore o superiore) del valore ottimo della funzione obiettivo nel sotto-albero corrispondente.
Nel caso di un problema di **massimizzazione**:
*   Si risolve il rilassamento continuo del sotto-problema.
*   Il valore ottimo del rilassamento continuo costituisce un **upper bound** (valutazione superiore $Z_S$) per quel nodo:
    $$
    Z_{\text{sotto-problema}} \le Z_S
    $$

### 3. Fathoming (Potatura / Chiusura dei nodi)
Un nodo dell'albero viene chiuso (potato) e non viene ulteriormente ramificato se si verifica una delle seguenti tre condizioni:
1.  **Inammissibilità (Fathoming by infeasibility)**: Il rilassamento continuo del sotto-problema non ammette soluzioni.
2.  **Ottimalità Intera (Fathoming by integrality)**: La soluzione ottima del rilassamento continuo rispetta i vincoli di integrità. Se il suo valore di obiettivo $Z$ è migliore della soluzione incombente corrente $Z_I$ (ossia $Z > Z_I$ per massimo), si aggiorna la soluzione incombente ($Z_I = Z$) e si chiude il nodo.
3.  **Dominanza (Fathoming by bounding)**: La valutazione superiore del nodo $Z_S$ è peggiore o uguale alla soluzione incombente corrente ($Z_S \le Z_I$ per massimo). Ciò garantisce che il sotto-problema non potrà mai produrre una soluzione intera migliore di quella già individuata.

## Strategie di Esplorazione (Visita dell'Albero)

L'ordine con cui i nodi aperti vengono selezionati per l'esplorazione determina l'efficienza dell'algoritmo:

*   **Depth-First (Visita in Profondità / "Sotto-problema creato più di recente")**:
    *   *Regola*: Si seleziona sempre il nodo a livello più profondo (creato più di recente).
    *   *Vantaggi*: Trova rapidamente soluzioni ammissibili intere (scendendo verso le foglie), il che consente di avere presto un buon valore per la soluzione incombente $Z_I$. Inoltre, richiede pochissima memoria per memorizzare i nodi aperti.
*   **Best-Bound-First (Miglior Bound / "Sotto-problema con il miglior bound")**:
    *   *Regola*: Si seleziona il nodo che presenta il bound più promettente (il valore di $Z_S$ più alto per massimo, o più basso per minimo).
    *   *Vantaggi*: Minimizza il numero totale di nodi espansi prima di raggiungere l'ottimo globale.
    *   *Svantaggi*: Tende a rimanere a livelli alti dell'albero all'inizio, ritardando l'individuazione di soluzioni intere ammissibili e richiedendo molta memoria per tenere aperti molti nodi contemporaneamente.
*   **Breadth-First (Visita in Ampiezza)**:
    *   *Regola*: Si esplorano tutti i nodi di un livello prima di passare al livello successivo.

## Approfondimenti e Scelte Avanzate

Per uno studio dettagliato delle componenti avanzate dell'algoritmo di Branch and Bound, fare riferimento alle seguenti note teoriche:
- [Scelte Progettuali nel Branch and Bound](pli_scelte_branch_and_bound.md): Analisi delle euristiche per la selezione dei nodi e delle variabili.
- [Branch and Bound per PLIM](pli_branch_and_bound_plim.md): Regole specifiche per problemi misti (interi e continui) e limitazioni sull'arrotondamento dei bound.
- [Rilassamento Lagrangiano](pli_rilassamento_lagrangiano.md): Calcolo di bound alternativi tramite penalizzazione dei vincoli difficili.
- [Soluzioni Quasi-Ottime e Criteri di Arresto](pli_soluzioni_quasi_ottime.md): Arresto precoce tramite tolleranze sul gap di ottimalità.
- [Soluzioni Ottime Alternative](pli_soluzioni_ottime_alternative.md): Adattamento delle regole di potatura per l'enumerazione di tutti gli ottimi globali.

