# MC - Problema dello Zaino (Knapsack)

## Quando Usarla
Per modellare problemi di selezione ottima di elementi indivisibili sotto un vincolo di risorsa o budget limitato (es. selezione di portafoglio investimenti, carico merci su un veicolo con portata massima).

## Variabili Tipiche
*   $x_j \in \{0, 1\}$: Vale $1$ se l'oggetto/investimento $j$ viene selezionato, $0$ altrimenti.

## Modello Template
$$
\max \quad \sum_{j=1}^n v_j x_j
$$
$$
\text{s.t.} \quad \sum_{j=1}^n p_j x_j \le C
$$
$$
x_j \in \{0, 1\} \quad \forall j = 1, \dots, n
$$

## Procedura da Esame
1.  Identificare gli oggetti o progetti selezionabili, i loro valori $v_j$ e i rispettivi pesi o costi $p_j$.
2.  Definire la capacità massima o budget $C$.
3.  Scrivere l'unico vincolo di capacità.
4.  Dichiarare il dominio binario per tutte le variabili.

## Mini Esempio
Massimizzare il valore con budget $C = 15$. Oggetti:
1.  Peso 10, Valore 20
2.  Peso 7, Valore 15
3.  Peso 5, Valore 11
Il modello è:
$$
\max \quad 20 x_1 + 15 x_2 + 11 x_3
$$
$$
\text{s.t.} \quad 10 x_1 + 7 x_2 + 5 x_3 \le 15
$$
$$
x_1, x_2, x_3 \in \{0, 1\}
$$

## Errori Comuni
*   Scrivere il vincolo di capacità come uguaglianza ($=$) invece di disuguaglianza ($\le$).
*   Dimenticare di imporre il dominio binario, trasformandolo in un problema di PL continuo.

## Fonti
*   `modelli_PLI.pdf`, Sezione 2.7
