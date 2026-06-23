---
type: theory
topic: programmazione_lineare_intera
status: active
sources: [BB PLI.pdf]
reliability: official
---

# Soluzioni Ottime Alternative nel Branch and Bound

La procedura standard del Branch and Bound è progettata per trovare **una singola** soluzione ottima globale. In alcuni contesti applicativi, tuttavia, è di fondamentale importanza individuare **tutte** le soluzioni ottime alternative per poter valutare criteri secondari non modellati.

## Modifiche alla Regola di Potatura (Fathoming)

Per trovare una sola soluzione ottima, un nodo $P_i$ con bound del rilassamento continuo $Z_{rel}(P_i)$ può essere potato per dominanza se:

$$
Z_{rel}(P_i) \le Z_I \quad (\text{per problemi di massimo})
$$

Se il bound di un nodo è uguale all'incumbent corrente, quel nodo non può produrre una soluzione intera strettamente migliore di quella già nota, quindi viene potato.

> [!IMPORTANT]
> Se l'obiettivo è individuare **tutte le soluzioni ottime alternative**, la regola di potatura per dominanza deve essere modificata usando **disuguaglianze strette**:
> - Massimo: Un nodo viene potato se $Z_{rel}(P_i) < Z_I$. I nodi con $Z_{rel}(P_i) = Z_I$ devono rimanere aperti ed essere esplorati, poiché potrebbero contenere altre soluzioni intere distinte di valore pari a $Z_I$.
> - Minimo: Un nodo viene potato se $Z_{rel}(P_i) > Z_I$. I nodi con $Z_{rel}(P_i) = Z_I$ rimangono aperti.

---

## Gestione dell'Incumbent e Memorizzazione

Durante l'esecuzione con ricerca di ottimi alternativi:
1. Se un nodo produce una soluzione intera ammissibile con valore $\bar{Z}$:
   - Se $\bar{Z} > Z_I$ (massimo): Si cancella la lista delle soluzioni precedenti, si imposta $Z_I = \bar{Z}$ e si memorizza la nuova soluzione come unica incombente.
   - Se $\bar{Z} = Z_I$: La nuova soluzione viene **aggiunta** alla lista delle soluzioni ottime correnti.
   - Se $\bar{Z} < Z_I$: La soluzione viene scartata.
2. Al termine dell'esplorazione (quando tutti i nodi sono potati o chiusi), la lista memorizzata conterrà tutte le soluzioni ottime globali del problema.
