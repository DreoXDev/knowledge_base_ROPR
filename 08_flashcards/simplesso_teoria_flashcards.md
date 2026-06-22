# Flashcard — Teoria del simplesso

## Frontiere e iperpiani

Q: Come si ottiene l'equazione di frontiera di un vincolo funzionale?
A: Sostituendo il simbolo di disuguaglianza con l'uguaglianza, ottenendo $a_{i1}x_1+\dots+a_{in}x_n=b_i$.

Q: Cos'è un iperpiano?
A: È l'insieme dei punti che soddisfano un'equazione lineare in dimensione $n$; è l'analogo di una retta in 2D e di un piano in 3D.

Q: Cos'è la frontiera della regione ammissibile?
A: È l'insieme delle soluzioni ammissibili che soddisfano almeno una equazione di frontiera.

## Vertici

Q: Cos'è un vertice ammissibile?
A: È una soluzione ammissibile che non giace su un segmento che connette altre due soluzioni ammissibili.

Q: Come si caratterizza algebricamente un vertice ammissibile?
A: In un PL con $n$ variabili, è una soluzione ottenuta dall'intersezione di $n$ equazioni di frontiera e che soddisfa tutti i vincoli.

Q: Ogni sistema di $n$ equazioni di frontiera produce un vertice ammissibile?
A: No. Può produrre un vertice non ammissibile, nessuna soluzione oppure situazioni degeneri.

## Simplesso

Q: Perché il simplesso cerca l'ottimo nei vertici?
A: Perché se un PL ha un ottimo finito, almeno una soluzione ottima è un vertice ammissibile.

Q: Cosa sono due vertici ammissibili adiacenti?
A: Sono vertici che condividono $n-1$ frontiere attive e sono collegati da uno spigolo della regione ammissibile.

Q: Cosa cambia in un passo del simplesso?
A: Si passa a un vertice adiacente cambiando una sola frontiera attiva, cioè algebricamente una variabile entra in base e una esce.

Q: Cos'è la degenerazione?
A: È il caso in cui più basi rappresentano lo stesso vertice; in forma algebrica una soluzione di base ammissibile è degenere se almeno una variabile di base vale zero.
