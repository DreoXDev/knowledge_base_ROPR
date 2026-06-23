# Topic Card: Ottimizzazione Non Lineare Vincolata Generale

- **Definizione**: Ottimizzazione di una funzione obiettivo $f(x)$ soggetta a vincoli di uguaglianza $g_i(x) = 0$ e disuguaglianza $h_j(x) \le 0$.
- **Regione Ammissibile $\Omega$**: Sottoinsieme del dominio in cui tutti i vincoli sono contemporaneamente soddisfatti. Se $\Omega$ è compatto (chiuso e limitato), il Teorema di Weierstrass assicura l'esistenza di massimi e minimi globali.
- **Strategie risolutive**:
  1. [[pnl_riduzione_variabili_libere|Riduzione delle variabili libere]]: Per eliminare gradi di libertà esplicitando i vincoli di uguaglianza.
  2. [[pnl_metodo_moltiplicatori_lagrange|Moltiplicatori di Lagrange]]: Per problemi con soli vincoli di uguaglianza.
  3. [[pnl_condizioni_kkt|Condizioni KKT]]: Quadro unificato per vincoli di disuguaglianza e misti.
- **Teorema di Weierstrass**: Garantisce l'esistenza degli ottimi se la funzione obiettivo è continua e la regione ammissibile è compatta (chiusa e limitata).
- **LICQ (Constraint Qualification)**: Condizione per cui i gradienti di tutti i vincoli attivi (uguaglianze e disuguaglianze con $h_j(x^*)=0$) sono linearmente indipendenti nel punto stazionario. Garantisce la validità delle condizioni necessarie di primo ordine.
- **Fonti**: [[pnl_ottimizzazione_vincolata|Teoria Ottimizzazione Vincolata]]
