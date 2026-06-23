# Flashcard — Programmazione Lineare Intera (Modelli)

## Definizioni e Modelli Base

Q: Qual è la differenza principale tra un modello PL e uno PLI?
A: In un modello PLI le variabili decisionali (tutte o in parte) sono vincolate ad assumere valori interi ($\mathbb{Z}$), mentre nel PL sono continue ($\mathbb{R}$).

Q: Cos'è una variabile decisionale binaria?
A: Una variabile che può assumere solo i valori $0$ o $1$ per modellare decisioni logiche dicotomiche (sì/no).

Q: Cos'è il rilassamento continuo di un problema PLI?
A: Il problema di PL ottenuto rimuovendo i vincoli di integrità sulle variabili (sostituendo ad esempio $x_j \in \{0, 1\}$ con $0 \le x_j \le 1$).

Q: Che relazione c'è tra il valore ottimo del rilassamento continuo ($Z^*_C$) e dell'intero ($Z^*_I$) per un problema di massimo?
A: Vale sempre $Z^*_C \ge Z^*_I$ perché la regione ammissibile del rilassamento continuo contiene quella del problema intero.

## Modelli Classici

Q: Qual è la funzione obiettivo del problema dello zaino (knapsack) binario?
A: $\max \sum_{j=1}^n v_j x_j$ dove $v_j$ è il valore dell'oggetto $j$ e $x_j \in \{0, 1\}$.

Q: Qual è il vincolo di capacità nel problema dello zaino?
A: $\sum_{j=1}^n p_j x_j \le C$ dove $p_j$ è il peso dell'oggetto $j$ e $C$ è la capacità massima dello zaino.

Q: Come si formula il vincolo di assegnamento in cui ogni cliente deve essere servito da un unico magazzino?
A: $\sum_{j=1}^n x_{ij} = 1$ per ogni cliente $i$, con $x_{ij} \in \{0, 1\}$.

Q: Qual è la funzione obiettivo del problema di facility location capacitated?
A: Minimizzare la somma dei costi fissi di apertura magazzini e dei costi variabili di trasporto: $\min \sum_j f_j y_j + \sum_i \sum_j c_{ij} d_i x_{ij}$.
