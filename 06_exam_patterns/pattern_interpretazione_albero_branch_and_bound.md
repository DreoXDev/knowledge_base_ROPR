# Pattern d'Esame: Interpretazione Albero Branch and Bound

## Descrizione del Pattern
Domande d'esame teorico-pratiche in cui viene presentato un diagramma o una tabella di un albero di Branch and Bound e si richiede di determinare il tipo di problema, identificare le migliori soluzioni, chiudere nodi per dominanza, calcolare il gap di ottimalità o selezionare il nodo successivo.

## Trigger RAG
- "si consideri l'albero di Branch and Bound"
- "stabilire se si tratta di un problema di massimo o di minimo"
- "indicare quale nodo viene selezionato con la regola best bound"
- "calcolare l'intervallo dell'ottimo"
- "quali nodi possono essere potati"

## Schema di Risposta Atteso

1. **Riconoscimento del tipo di problema ($\max/\min$)**:
   * Analizzare l'andamento dei bound nei nodi discendenti.
   * "È un problema di minimo perché i bound dei figli sono maggiori o uguali a quelli dei rispettivi padri ($LB_{\text{padre}} \le LB_{\text{figlio}}$)."
2. **Determinazione dell'Incumbent ($Z_I$)**:
   * Trovare la migliore soluzione intera ammissibile (valore più alto per $\max$, più basso per $\min$).
3. **Calcolo dell'Intervallo dell'Ottimo $z^*$**:
   * Scrivere l'intervallo $[Z_{bound}, Z_I]$ (per $\min$) o $[Z_I, Z_{bound}]$ (per $\max$), dove $Z_{bound}$ è il miglior bound tra i nodi aperti.
4. **Selezione del Prossimo Nodo in Best Bound First (BBF)**:
   * Scegliere il nodo aperto con il bound più promettente (minimo $LB$ per $\min$, massimo $UB$ per $\max$).
5. **Chiusura dei Nodi per Dominanza**:
   * Identificare i nodi aperti il cui bound è peggiore dell'incumbent ($LB \ge Z_I$ per $\min$, $UB \le Z_I$ per $\max$) e dichiararne la chiusura.
