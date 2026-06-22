# Flashcard — Teoria della Dualità

## Definizioni e Fondamenti

Q: Che cos'è il problema duale in Programmazione Lineare?
A: È il problema di PL associato al primale, ottenuto scambiando il ruolo di vincoli e variabili: nel caso di primale MAX standard, il duale è un MIN.

Q: Cosa afferma la dualità debole?
A: Per ogni soluzione primale ammissibile $\mathbf{x}$ e duale ammissibile $\mathbf{y}$, nel caso MAX-MIN vale $\mathbf{c}\mathbf{x} \le \mathbf{y}\mathbf{b}$.

Q: Cosa afferma la dualità forte?
A: Se primale e duale hanno ottimi finiti, allora i valori ottimi coincidono: $Z^* = W^*$.

## Prezzi Ombra e Complementarità

Q: Cosa sono i prezzi ombra?
A: Sono le componenti della soluzione ottima duale e rappresentano il valore marginale delle risorse del primale.

Q: Qual è l'idea delle condizioni di complementarità (complementary slackness)?
A: Una variabile positiva implica che il vincolo complementare sia saturo; uno slack positivo implica che la variabile complementare sia nulla.

## Relazioni e Casi Limite

Q: Se il primale è illimitato, cosa succede al duale?
A: Il duale è inammissibile (non ammette soluzioni).

Q: Se il primale è inammissibile, cosa succede al duale?
A: Il duale può essere inammissibile oppure illimitato.
