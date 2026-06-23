# Pattern d'Esame: Ottimizzazione Non Lineare Vincolata Generale

## Descrizione del Pattern
Esercizi che richiedono la risoluzione di problemi di ottimizzazione non lineare vincolata utilizzando tre possibili tecniche a seconda della struttura dei vincoli:
1. **Riduzione delle variabili libere**: Consigliato per vincoli di uguaglianza semplici e lineari.
2. **Moltiplicatori di Lagrange**: Richiesto esplicitamente per vincoli di uguaglianza.
3. **Condizioni KKT generali**: Utilizzato in presenza di vincoli di disuguaglianza o misti.

---

## Trigger RAG
- "riducendo il numero di variabili libere"
- "esplicitare una variabile dal vincolo"
- "metodo dei moltiplicatori di Lagrange per vincoli di uguaglianza"
- "interpretazione geometrica dei moltiplicatori"
- "condizioni KKT per vincoli di disuguaglianza"
- "vincoli attivi e non attivi"

---

## Schemi di Risoluzione Attesi

### Schema A: Riduzione delle Variabili
1. **Identificazione**: Individuare un vincolo di uguaglianza $g(x_1, \dots, x_n) = 0$ da cui sia possibile isolare algebricamente e univocamente una variabile (es. vincoli lineari).
2. **Esplicitazione**: Esplicitare $x_k = \phi_k(x_{\neq k})$.
3. **Sostituzione**: Sostituire l'espressione nella funzione obiettivo per ottenere la funzione ridotta $\tilde{f}(x_{\neq k})$ in $n-1$ variabili.
4. **Ottimizzazione non vincolata**: Trovare i punti stazionari ponendo $\nabla \tilde{f} = 0$ e classificarli tramite la matrice Hessiana ridotta $\nabla^2 \tilde{f}$.
5. **Ricostruzione**: Ricavare il valore ottimo di $x_k^*$ usando la relazione di esplicitazione.

### Schema B: Moltiplicatori di Lagrange (Uguaglianze)
1. **Lagrangiana**: Scrivere la funzione $L(x, \lambda) = f(x) + \sum_{i=1}^m \lambda_i g_i(x)$.
2. **Sistema del primo ordine**: Risolvere il sistema di $n+m$ equazioni ponendo $\nabla_x L = 0$ e $g_i(x) = 0$.
3. **Classificazione**: Poiché le condizioni sono solo necessarie, confrontare i valori della funzione obiettivo $f(x)$ nei punti candidati stazionari trovati. Se il dominio è compatto (Weierstrass), il valore massimo corrisponde al massimo globale e il valore minimo al minimo globale.
4. **Interpretazione Geometrica**: Se richiesto, mostrare che nel punto ottimo il gradiente $\nabla f(x^*)$ è ortogonale allo spazio tangente del vincolo e parallelo al gradiente del vincolo stesso ($\nabla f(x^*) = -\lambda^* \nabla g(x^*)$).

### Schema C: Condizioni KKT (Disuguaglianze)
1. **Forma Standard**: Ricondurre i vincoli alla forma $h_j(x) \le 0$ (se $A(x) \ge B \implies B - A(x) \le 0$).
2. **Lagrangiana generalizzata**: Scrivere $L(x, \lambda, \mu) = f(x) + \sum \lambda_i g_i(x) + \sum \mu_j h_j(x)$.
3. **Condizioni KKT**: Impostare le equazioni:
   - Stazionarietà: $\nabla_x L = 0$.
   - Ammissibilità primale: $g_i(x) = 0, h_j(x) \le 0$.
   - Complementarità degli scarti: $\mu_j h_j(x) = 0$.
   - Ammissibilità duale (segno): $\mu_j \ge 0$ per problemi di minimo, $\mu_j \le 0$ per problemi di massimo.
4. **Analisi per casi**: Risolvere esplorando le combinazioni dei vincoli attivi ($h_j(x) = 0$) e inattivi ($h_j(x) < 0 \implies \mu_j = 0$).
5. **Filtraggio**: Scartare i punti che violano l'ammissibilità primale o duale. Confrontare i valori di $f(x)$ sui punti ammissibili rimasti.

---

## Errori Comuni da Evitare
- **Segno errato dei moltiplicatori**: Confondere il segno di $\mu_j$ (deve essere $\ge 0$ per min e $\le 0$ per max sotto la forma Lagrangiana $L = f + \mu h$).
- **Uso di riduzione variabili con vincoli non lineari complessi**: Cercare di applicare la riduzione delle variabili a vincoli del tipo $x_1^2 + x_2^2 = 1$ senza considerare il doppio segno dei rami della radice quadrata.
- **Trattare KKT come condizioni sufficienti**: Dimenticare di confrontare i valori della funzione obiettivo sui punti candidati trovati.

---

## Collegamenti a Esercizi Svolti
- [[pnl_lagrange_cerchio_unitario]]: Ottimizzazione di una funzione lineare su un vincolo circolare non lineare tramite moltiplicatori di Lagrange.
- [[pnl_riduzione_variabili_esempio_lineare]]: Minimizzazione di una funzione quadratica con vincolo di uguaglianza lineare tramite riduzione delle variabili libere.
