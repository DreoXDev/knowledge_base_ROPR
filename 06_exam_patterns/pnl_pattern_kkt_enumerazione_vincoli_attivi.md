# Pattern d'Esame: KKT ed Enumerazione dei Vincoli Attivi

## Descrizione del Pattern
Domande o esercizi pratici in cui viene richiesta la risoluzione di un problema di Programmazione Non Lineare (PNL) vincolata da disuguaglianze tramite la scrittura delle condizioni KKT e l'analisi sistematica di tutte le combinazioni di vincoli attivi e inattivi.

## Trigger RAG
- "risolvere il sistema KKT associato"
- "vincoli attivi e non attivi"
- "condizioni KKT per vincoli di disuguaglianza"
- "Lagrangiana con disuguaglianze"
- "moltiplicatori di segno corretto"
- "regola dei segni moltiplicatori KKT"

## Schema di Risposta Atteso

1. **Standardizzazione dei Vincoli**:
   * Scrivere tutti i vincoli di disuguaglianza nella forma standard $g_i(x) \le 0$ (moltiplicando per $-1$ se necessario).
2. **Scrittura della Lagrangiana**:
   * Scrivere la funzione Lagrangiana $L(x, \mu) = f(x) + \sum \mu_i g_i(x)$.
3. **Elencazione delle Condizioni KKT**:
   * Stazionarietà: $\nabla_x L = 0$
   * Ammissibilità primale: $g_i(x) \le 0 \quad \forall i$
   * Ammissibilità duale: $\mu_i \ge 0 \quad \forall i$ (per minimizzazione)
   * Complementarità: $\mu_i g_i(x) = 0 \quad \forall i$
4. **Analisi Combinatoria Sistematico per Casi**:
   * Con $m$ vincoli, dichiarare che esistono $2^m$ combinazioni.
   * Analizzare i casi rilevanti (partendo dal caso non vincolato $\mu_i = 0$, poi singoli vincoli attivi, poi coppie di vincoli attivi, ecc.).
5. **Verifica dei Candidati (Scarto)**:
   * Per ciascun punto trovato, controllare l'ammissibilità primale (se viola i vincoli inattivi) e l'ammissibilità duale (se i moltiplicatori dei vincoli attivi sono negativi $\mu_i < 0$).
   * Mostrare i calcoli che giustificano lo scarto di ciascun candidato invalido.
6. **Tabella Riassuntiva dei Casi**:
   * Compilare una tabella che elenchi per ogni caso analizzato: Caso, Vincoli Attivi, Punto Candidato, Valore dell'obiettivo $f$, Moltiplicatori, ed Esito (Validato/Scartato con motivazione).
7. **Conclusione**:
   * Dichiarare il punto di ottimo globale definitivo $x^*$, i moltiplicatori associati $\mu^*$ e il valore della funzione all'ottimo $f(x^*)$.

## Errori Frequenti da Evitare
- **Inversione del segno dei vincoli**: Scrivere la Lagrangiana senza aver prima trasformato $x \ge -1$ in $-x-1 \le 0$.
- **Uso errato del segno del moltiplicatore**: Dimenticare che per un problema di minimo con Lagrangiana standard $f(x) + \sum \mu_i g_i(x)$, i moltiplicatori $\mu_i$ devono essere non negativi ($\ge 0$).
- **Dimenticare di verificare i vincoli inattivi**: Considerare valido un candidato analizzato per un vincolo attivo senza controllare se rispetta anche gli altri vincoli originari.
