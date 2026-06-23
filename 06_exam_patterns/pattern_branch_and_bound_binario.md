# Pattern d'Esame: Branch and Bound Binario

## Descrizione del Pattern
Esercizi algoritmici in cui si richiede di risolvere un problema a variabili binarie (0-1) tramite il Branch and Bound.

## Trigger RAG
- "risolvere tramite Branch and Bound binario"
- "branch and bound per variabili binarie"
- "Lombardia Manufacturing branch and bound"
- "arrotondamento all'intero dei bound"
- "fissaggio delle variabili a 0 o 1"

## Schema di Risposta Atteso

1. **Inizializzazione**:
   * Dichiarare l'incumbent iniziale $Z_I = -\infty$ (per massimo) o $Z_I = +\infty$ (per minimo).
   * Risolvere il rilassamento continuo completo $P_0$ (con vincoli $0 \le x_j \le 1$).
2. **Arrotondamento dei Bound**:
   * Se i coefficienti in funzione obiettivo sono interi, giustificare l'arrotondamento all'intero più vicino nel verso dell'ottimizzazione ($\lfloor Z_C \rfloor$ per massimo, $\lceil Z_C \rceil$ per minimo).
3. **Tabella o Albero di Enumerazione**:
   * Disegnare l'albero di branching o mostrare la tabella con: Nodo, Variabili Fissate, Soluzione del rilassamento, Bound (reale e arrotondato), Stato (aperto/chiuso) e Motivo.
4. **Regola di Selezione**:
   * Specificare la regola di visita (Depth First o Best Bound First) e la variabile di branching selezionata (e.g. ordinamento naturale $x_1, x_2, \dots$).
5. **Soluzione Ottima**:
   * Dichiarare i valori ottimi di tutte le variabili binarie $x^*$ e il valore ottimo $z^*$.
