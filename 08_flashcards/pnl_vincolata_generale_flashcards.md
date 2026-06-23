# Flashcards: Programmazione Non Lineare Vincolata Generale

- **Q**: Qual è la forma standard di un problema di ottimizzazione non lineare vincolata?
  **A**:
  $$
  \begin{aligned}
  \min/\max \quad & f(x) \\
  \text{s.t. } & g_i(x) = 0 \quad i = 1, \dots, m \\
  & h_j(x) \le 0 \quad j = 1, \dots, p
  \end{aligned}
  $$

- **Q**: In quali condizioni è applicabile il metodo di riduzione delle variabili libere?
  **A**: Quando ci sono vincoli di uguaglianza semplici (in genere lineari) che consentono di esplicitare univocamente $m$ variabili in funzione delle restanti $n-m$ variabili libere.

- **Q**: Qual è la funzione Lagrangiana per problemi con soli vincoli di uguaglianza?
  **A**:
  $$L(x, \lambda) = f(x) + \sum_{i=1}^m \lambda_i g_i(x)$$

- **Q**: Cosa affermano le condizioni necessarie del primo ordine per moltiplicatori di Lagrange?
  **A**: Che nei punti stazionari vincolati il gradiente della Lagrangiana si annulla: $\nabla_x L = 0$ e $g_i(x) = 0$.

- **Q**: Qual è l'interpretazione geometrica del moltiplicatore di Lagrange $\lambda^*$ all'ottimo?
  **A**: Nel punto ottimo il gradiente della funzione obiettivo è parallelo al gradiente del vincolo ed opposto in segno (se $\lambda^* > 0$): $\nabla f(x^*) = -\lambda^* \nabla g(x^*)$.

- **Q**: Cosa esprime la condizione di complementarità degli scarti nelle condizioni KKT?
  **A**:
  $$\mu_j^* \cdot h_j(x^*) = 0, \quad j = 1, \dots, p$$
  Esclude che sia il vincolo sia il moltiplicatore siano contemporaneamente non nulli.

- **Q**: Qual è la differenza tra vincolo attivo e vincolo inattivo in un punto $x^*$?
  **A**: Un vincolo $h_j(x) \le 0$ è **attivo** se $h_j(x^*) = 0$, ed **inattivo** se $h_j(x^*) < 0$.

- **Q**: Qual è la regola sul segno dei moltiplicatori KKT $\mu_j^*$ per problemi di disuguaglianza?
  **A**: Per problemi di **minimo** si ha $\mu_j^* \ge 0$, mentre per problemi di **massimo** si ha $\mu_j^* \le 0$ (sotto forma standard $h_j(x) \le 0$).

- **Q**: Cos'è la qualificazione dei vincoli LICQ (Linear Independence Constraint Qualification)?
  **A**: È la condizione per cui i gradienti di tutti i vincoli di uguaglianza e di tutti i vincoli di disuguaglianza attivi sono linearmente indipendenti nel punto stazionario. Garantisce la validità delle condizioni KKT.

- **Q**: Le condizioni KKT sono necessarie o sufficienti?
  **A**: In generale sono solo condizioni necessarie per l'ottimalità locale. Diventano sufficienti sotto ipotesi di convessità (funzione obiettivo convessa e regione ammissibile convessa).
