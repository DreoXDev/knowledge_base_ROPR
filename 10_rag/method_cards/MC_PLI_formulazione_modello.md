# MC - Formulazione Modello PLI

## Quando Usarla
Quando la traccia d'esame richiede di scrivere il modello matematico per un problema combinatorio o decisionale in cui le grandezze non sono divisibili o ci sono scelte dicotomiche (sì/no).

## Variabili Tipiche
*   $x_j \ge 0$ (intera): Quantità discrete da produrre, acquistare o spedire.
*   $y_k \in \{0, 1\}$: Decisione binaria (es. $1$ se si attiva il processo/deposito $k$, $0$ altrimenti).

## Modello Template
$$
\max \quad \sum_{j \in J} c_j x_j - \sum_{k \in K} f_k y_k
$$
$$
\text{s.t.} \quad \sum_{j \in J} a_{ij} x_j \le b_i \quad \forall i \in I
$$
$$
x_j \le M_j y_j \quad \forall j \in J, k(j) \in K
$$
$$
x_j \in \mathbb{Z}_+ \quad \forall j \in J
$$
$$
y_k \in \{0, 1\} \quad \forall k \in K
$$

## Procedura da Esame
1.  **Definire gli insiemi e gli indici**: Esplicitare cosa indicano gli indici (es. $i$ per clienti, $j$ per depositi).
2.  **Elencare i parametri**: Riportare i dati forniti con le rispettive unità di misura.
3.  **Definire le variabili**: Dichiarare variabili continue, intere e binarie con dominio preciso.
4.  **Costruire la funzione obiettivo**: Esprimere ricavi, costi fissi e variabili in modo lineare.
5.  **Formulare i vincoli**: Scrivere i vincoli con indicazione fisica a fianco (es. capacità, bilancio, logici).

## Mini Esempio
Massimizzare il profitto di due progetti con budget $10$, dove il progetto 1 ha costo $6$ e rendimento $8$, il progetto 2 ha costo $5$ e rendimento $7$:
$$
\max \quad 8 y_1 + 7 y_2
$$
$$
\text{s.t.} \quad 6 y_1 + 5 y_2 \le 10
$$
$$
y_1, y_2 \in \{0, 1\}
$$

## Errori Comuni
*   Scrivere formule non lineari (es. moltiplicare due variabili decisionali).
*   Omettere la specifica di integrità o dominio binario ($y_i \in \{0, 1\}$).

## Fonti
*   `modelli_PLI.pdf`
