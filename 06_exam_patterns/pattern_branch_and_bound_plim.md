# Pattern d'Esame: Branch and Bound per PLIM

## Descrizione del Pattern
Esercizi algoritmici in cui si richiede di risolvere un problema con variabili sia intere che continue (PLIM) tramite il Branch and Bound.

## Trigger RAG
- "risolvere il problema PLIM tramite Branch and Bound"
- "variabili intere e continue"
- "rilassamento lineare del problema misto"
- "albero di branching per variabili continue"

## Schema di Risposta Atteso

1. **Identificazione del Dominio**:
   * Dichiarare esplicitamente quali variabili sono vincolate a essere intere ($x_j \in \mathbb{Z}$) e quali sono continue ($y_k \in \mathbb{R}$).
2. **Tabella di Enumerazione dei Nodi**:
   * Mostrare la tabella contenente: Nodo, Vincoli aggiunti, Soluzione del rilassamento continuo, Bound, Stato (aperto/chiuso) e Motivo.
3. **Regole Operative Applicate**:
   * Specificare che il branching viene effettuato solo sulle variabili intere frazionarie.
   * Evidenziare che non è stato effettuato alcun arrotondamento sui bound rilassati (trattandosi di un PLIM).
   * Segnalare che una soluzione è ammissibile intera anche se le variabili continue presentano valori frazionari.
4. **Soluzione Ottima**:
   * Dichiarare i valori ottimi di tutte le variabili $x^*$ e $y^*$ e il valore ottimo $z^*$.
