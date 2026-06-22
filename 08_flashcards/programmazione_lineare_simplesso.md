# Flashcards — Metodo del Simplesso

## Flashcard — Simplesso

Che cos'è il metodo del simplesso?::È una procedura algebrica per risolvere problemi di PL, interpretabile geometricamente come movimento tra vertici ammissibili adiacenti della regione ammissibile.

Qual è il test di ottimalità geometrico del simplesso?::Una soluzione vertice è ottima se nessun vertice ammissibile adiacente migliora il valore della funzione obiettivo.

Che cos'è una variabile slack?::È una variabile non negativa aggiunta a un vincolo di tipo $\le$ per trasformarlo in uguaglianza.

Che cos'è una soluzione di base?::È una soluzione ottenuta ponendo a zero le variabili non di base e risolvendo il sistema per le variabili di base.

Quando una soluzione di base è ammissibile?::Quando tutte le variabili assumono valore non negativo.

Per un problema di massimo, quale variabile entra in base nel simplesso tabellare?::Una variabile non di base con coefficiente negativo in riga 0, tipicamente quella con coefficiente più negativo.

Come si sceglie la variabile uscente?::Con il test del rapporto minimo tra termine noto e coefficiente positivo nella colonna pivot.

Quando il tableau è ottimo in un problema di massimo?::Quando nella riga 0 non ci sono coefficienti negativi per variabili non di base.

Come si riconosce un problema illimitato nel tableau?::Quando scelta una variabile entrante, nella sua colonna non ci sono coefficienti positivi, quindi nessuna variabile può uscire dalla base.

Come si riconoscono ottimi multipli nel tableau?::Quando il tableau è ottimo ma una variabile non di base ha coefficiente nullo nella riga 0.
