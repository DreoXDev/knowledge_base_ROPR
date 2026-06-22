# Flashcards — Formulazione Modelli

Q: Quali sono le domande chiave per modellare un problema di PL?
A: 1. Quali sono le decisioni da prendere? (variabili)
2. Qual è l'obiettivo? (funzione obiettivo)
3. Quali sono i limiti? (vincoli)
4. Che valori possono assumere le variabili? (dominio)

Q: Come si modella una variabile libera $x$ nel simplesso?
A: Si esprime come differenza di due variabili non negative: $x = x^+ - x^-$, con $x^+, x^- \ge 0$.

Q: Come si trasforma una variabile $x \le 0$ per renderla non negativa?
A: Si definisce una nuova variabile $x' = -x$ (con $x' \ge 0$) e si sostituisce $x$ con $-x'$ in tutto il modello.

Q: Che tipo di vincoli caratterizza un problema di workforce scheduling su turni di 5 giorni su 7?
A: Vincoli di copertura minima giornaliera ciclica, dove ogni giorno è coperto dai turni iniziati in quel giorno o nei 4 giorni precedenti.

Q: In un problema di trasporto, cosa rappresenta la variabile decisionale $x_{ij}$?
A: La quantità di prodotto trasportata dall'origine $i$ alla destinazione $j$ al costo unitario $c_{ij}$.

Q: Come si linearizza un vincolo di qualità media (es. numero di ottani) in un problema di miscelazione?
A: Si moltiplicano entrambi i membri della disequazione per il denominatore (la quantità totale di miscela prodotta), ottenendo una forma lineare del tipo $\sum (q_c - Q^{min})x_{cm} \ge 0$.

