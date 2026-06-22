# Flashcards — Metodo delle Due Fasi

Q: Quando si aggiunge una variabile di surplus?
A: Quando un vincolo di tipo $\ge$ viene trasformato in uguaglianza, sottraendo una variabile non negativa ($e_i \ge 0$).

Q: Perché si aggiungono le variabili artificiali?
A: Per costruire una base iniziale ammissibile (con coefficiente $+1$) quando slack o surplus non sono sufficienti (es. in vincoli $\ge$ o $=$).

Q: Qual è l'obiettivo della Fase 1 nel metodo delle due fasi?
A: Minimizzare la somma delle variabili artificiali (ovvero massimizzare $-W = -\sum x_{ai}$) per trovare una soluzione di base ammissibile.

Q: Nel metodo delle due fasi, cosa significa ottimo di Fase 1 maggiore di zero ($W^* > 0$)?
A: Significa che non è possibile annullare tutte le variabili artificiali; pertanto il problema originario non è ammissibile.

Q: Qual è l'errore tipico prima di avviare i pivot in Fase 2?
A: Dimenticare di azzerare i coefficienti (costi ridotti) delle variabili attualmente in base nella riga obiettivo originaria ripristinata.
