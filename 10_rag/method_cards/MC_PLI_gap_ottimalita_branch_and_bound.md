---
type: method_card
topic: programmazione_lineare_intera
status: active
sources: [BB PLI.pdf]
reliability: official
---

# Method Card: Calcolo del Gap di Ottimalità

## Quando Usarlo
Richieste d'esame in cui si deve quantificare lo scostamento assoluto o percentuale tra la soluzione incumbent corrente e la valutazione ottimale del rilassamento continuo.

## Formule Chiave

Sia $Z_I$ l'incumbent corrente (migliore intera ammissibile) e $Z_{bound}$ il miglior bound teorico tra i nodi aperti:
* **Problema di Massimo**: $Z_{bound} = \max_{P_j \in \text{aperti}} UB(P_j)$
* **Problema di Minimo**: $Z_{bound} = \min_{P_j \in \text{aperti}} LB(P_j)$

### Gap Assoluto

$$
\text{Gap Assoluto} = |Z_{bound} - Z_I|
$$
* Massimo: $Z_{bound} - Z_I$
* Minimo: $Z_I - Z_{bound}$

### Gap Relativo
Solitamente espresso in percentuale:

$$
\text{Gap Relativo} = \frac{|Z_{bound} - Z_I|}{Z_{bound}} \quad (\text{se } Z_{bound} > 0)
$$
oppure rispetto all'incumbent:
$$
\text{Gap Relativo} = \frac{|Z_{bound} - Z_I|}{|Z_I|} \quad (\text{se } Z_I \neq 0)
$$
* Se il gap scende sotto la tolleranza impostata (es. $\alpha = 0.05$ per il $5\%$), la soluzione incumbent viene accettata come quasi-ottima e la ricerca si arresta.
