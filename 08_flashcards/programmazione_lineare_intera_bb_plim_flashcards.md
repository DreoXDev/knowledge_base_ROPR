---
type: flashcards
topic: programmazione_lineare_intera
status: active
sources: [BB PLI.pdf]
reliability: official
---

# Flashcards: B&B PLIM e Interpretazione Alberi

Q: In un problema PLIM, su quali variabili si può fare branching?
A: Esclusivamente sulle variabili vincolate ad essere intere che assumono un valore frazionario nel rilassamento continuo. Non si fa branching su quelle continue.

Q: Nel B&B per PLIM, una soluzione con variabili continue frazionarie può essere ammissibile?
A: Sì, se tutte le variabili vincolate ad essere intere assumono valori interi e tutti i vincoli del problema sono soddisfatti.

Q: Perché non è lecito arrotondare il bound frazionario del rilassamento continuo nel caso PLIM?
A: Perché la presenza di variabili continue fa sì che il valore ottimo del problema intero misto $z^*$ possa essere frazionario.

Q: In Best Bound First (BBF), come si seleziona il prossimo nodo da esplorare in un problema di minimo?
A: Si sceglie il nodo aperto che presenta il Lower Bound ($LB$) più basso.

Q: In Best Bound First (BBF), come si seleziona il prossimo nodo da esplorare in un problema di massimo?
A: Si sceglie il nodo aperto che presenta l'Upper Bound ($UB$) più alto.

Q: Come si riconosce se un albero B&B rappresenta un problema di massimo o minimo analizzando i bound?
A: Se i bound nei nodi crescono o restano uguali da padre a figlio, è un problema di minimo. Se decrescono o restano uguali, è un problema di massimo.

Q: Qual è la formula del Gap Assoluto di ottimalità per un problema di massimo?
A: $Gap_{abs} = Z_{bound} - Z_I$, dove $Z_{bound}$ è il miglior bound tra i nodi aperti e $Z_I$ è l'incumbent (migliore soluzione intera ammissibile).

Q: Quando si può potare un nodo aperto per dominanza applicando una tolleranza assoluta $K$ in un problema di massimo?
A: Quando il bound del rilassamento del nodo è inferiore o uguale a $Z_I + K$.
