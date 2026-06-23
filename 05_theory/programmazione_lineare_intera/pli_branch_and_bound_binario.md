---
type: theory
topic: programmazione_lineare_intera
status: active
sources: [Programmazione Lineare Intera_Branch and Bound binario.pdf]
reliability: official
---

# Branch and Bound Binario (Variabili 0-1)

## Fonte
`Programmazione Lineare Intera_Branch and Bound binario.pdf` (Slide Ufficiali del Corso)

## Introduzione
La programmazione lineare binaria (PB) è una sottoclasse della PLI in cui tutte le variabili decisionali sono vincolate ad assumere valore in $\{0, 1\}$. Per questa specifica classe di problemi, l'algoritmo di **Branch and Bound** assume proprietà e comportamenti peculiari che ne semplificano l'applicazione algoritmica sia dal punto di vista del branching che del bounding.

---

## Branching per Variabili Binarie (Fissaggio)
Nei problemi binari (PB), il partizionamento della regione ammissibile di un sotto-problema avviene in modo elementare **fissando** una delle variabili decisionali libere a $0$ o a $1$:
*   **Ramo sinistro**: Fissa la variabile $x_k = 0$
*   **Ramo destro**: Fissa la variabile $x_k = 1$

Ogni operazione di branching genera esattamente due nuovi sotto-problemi e riduce di uno il numero di variabili decisionali libere (ossia non ancora fissate).

### Selezione della variabile di branching
Nello svolgimento dell'algoritmo, si può adottare come criterio predefinito l'**ordinamento naturale delle variabili**:
1.  Al primo livello di branching si sceglie $x_1$.
2.  Al secondo livello si sceglie $x_2$.
3.  Si prosegue con $x_3, x_4, \dots$ lungo i nodi dell'albero.

*Nota*: Questa euristica prescinde dalla frazionalità della variabile nella soluzione ottima del rilassamento, semplificando la struttura decisionale dell'albero d'esame.

---

## Bounding e Rilassamento Continuo Binario
Per ricavare una valutazione (bound) in ciascun nodo dell'albero, si risolve il rilassamento continuo del relativo sotto-problema.
Per le variabili binarie, il rilassamento continuo si ottiene sostituendo il vincolo $x_j \in \{0, 1\}$ con l'intervallo continuo:
$$
0 \le x_j \le 1 \quad \forall j \text{ libera}
$$
Le variabili già fissate nei nodi superiori (es. $x_1 = 1$, $x_2 = 0$) vengono trattate come costanti numeriche e inserite direttamente nei vincoli e nella funzione obiettivo del sotto-problema.

---

## Arrotondamento all'Intero dei Bound (Integer Bounding)
Si consideri un problema di massimizzazione (o minimizzazione) a variabili binarie (o intere) in cui **tutti i coefficienti della funzione obiettivo $c_j$ sono numeri interi**:
$$
z = \sum_{j=1}^n c_j x_j \quad \text{con } c_j \in \mathbb{Z}
$$
Poiché in qualsiasi soluzione ammissibile del problema intero originale le variabili $x_j$ devono essere intere, il valore della funzione obiettivo $z$ sarà necessariamente un numero intero.

Questo ci consente di rafforzare il bound ottenuto dal rilassamento continuo ($Z_{\text{rilassato}}$) applicando l'arrotondamento all'intero:
*   **Per problemi di massimizzazione (Upper Bound)**:
    Il bound reale $Z_{\text{bound}}$ può essere arrotondato per difetto:
    $$
    Z_{\text{bound}} = \lfloor Z_{\text{rilassato}} \rfloor
    $$
    *Esempio*: Se l'ottimo del rilassamento continuo ha $Z = 16.5$, qualsiasi soluzione intera ammissibile non potrà mai superare $16.5$. Essendo l'obiettivo intero, la soluzione ottimale intera soddisferà necessariamente $z^* \le \lfloor 16.5 \rfloor = 16$.
*   **Per problemi di minimizzazione (Lower Bound)**:
    Il bound reale $Z_{\text{bound}}$ può essere arrotondato per eccesso:
    $$
    Z_{\text{bound}} = \lceil Z_{\text{rilassato}} \rceil
    $$

Questo arrotondamento rafforza il bound rendendo più veloci i test di dominanza e riducendo il numero di nodi da esplorare.

---

## Criteri di Potatura (Fathoming)
Un sotto-problema viene chiuso (potato) e rimosso dalla lista dei nodi da espandere per tre possibili ragioni:

1.  **Ottimalità Intera (Fathoming by integrality)**:
    La soluzione ottima del rilassamento continuo soddisfa l'integrità (tutte le variabili libere assumono valore $0$ o $1$). Questa soluzione è ammissibile per il problema originale.
    *   Se il suo valore $Z$ è strettamente migliore della soluzione incombente corrente $Z_I$ (ossia $Z > Z_I$ per massimo), si aggiorna la soluzione incombente: $Z_I = Z$.
    *   Il nodo viene chiuso.
2.  **Inammissibilità (Fathoming by infeasibility)**:
    Il rilassamento continuo del sotto-problema non ammette soluzioni ammissibili (regione ammissibile vuota $\emptyset$). Di conseguenza, anche il problema intero originale limitato a quel nodo non ha soluzioni.
    *   Il nodo viene chiuso.
3.  **Dominanza (Fathoming by bounding)**:
    Il bound del sotto-problema $Z_{\text{bound}}$ (eventualmente arrotondato all'intero) è peggiore o uguale alla migliore soluzione intera nota (incumbent $Z_I$):
    *   Per massimo: $Z_{\text{bound}} \le Z_I$
    *   Per minimo: $Z_{\text{bound}} \ge Z_I$
    In questo caso, continuare a ramificare dal nodo non potrà mai portare a una soluzione intera migliore di quella già trovata.
    *   Il nodo viene chiuso.
