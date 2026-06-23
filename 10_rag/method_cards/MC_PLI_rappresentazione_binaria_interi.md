# MC - Rappresentazione Binaria di Variabili Intere

## Quando Usarla
Per convertire variabili intere generali con dominio limitato $x \in [0, u]$ in un insieme equivalente di sole variabili binarie, ad esempio per consentire l'uso di algoritmi dedicati a problemi a variabili 0-1.

## Variabili Tipiche
*   $x \in \{0, 1, \dots, u\}$: Variabile intera generale limitata superiormente da $u$.
*   $y_k \in \{0, 1\}$: Variabili binarie ausiliarie di espansione pesata in base 2.

## Modello Template
Determinare la massima potenza di due $K$ tale che:
$$
2^K \le u < 2^{K+1}
$$

La variabile intera $x$ viene sostituita nel modello con la seguente combinazione lineare di $K+1$ variabili binarie:
$$
x = \sum_{k=0}^K 2^k y_k = y_0 + 2y_1 + 4y_2 + \dots + 2^K y_K
$$
$$
y_k \in \{0, 1\} \quad \forall k = 0, \dots, K
$$

Se $u$ non è una potenza esatta di $2$ meno 1 (ovvero $u \ne 2^{K+1}-1$), occorre aggiungere un vincolo per evitare che la combinazione delle $y_k$ superi la barriera $u$:
$$
\sum_{k=0}^K 2^k y_k \le u
$$

## Procedura da Esame
1.  Trovare il bound superiore $u$ per ciascuna variabile intera del problema.
2.  Calcolare $K$ in modo che $2^K \le u < 2^{K+1}$.
3.  Scrivere l'espansione binaria $x = y_0 + 2y_1 + \dots + 2^K y_K$.
4.  Aggiungere il vincolo di limitazione superiore $\sum 2^k y_k \le u$.
5.  Sostituire la variabile $x$ con la sua espansione in tutti i vincoli e nella funzione obiettivo del problema originario.

## Mini Esempio
Si consideri il vincolo $x \le 5$ con $x \in \mathbb{Z}_+$:
*   $u = 5$.
*   $2^2 \le 5 < 2^3 \implies K = 2$.
*   L'espansione è: $x = y_0 + 2y_1 + 4y_2$.
*   Si aggiunge il vincolo di validità superiore:
    $$
    y_0 + 2y_1 + 4y_2 \le 5
    $$
    *(Il valore massimo generabile dalle tre variabili binarie sarebbe altrimenti $1 + 2 + 4 = 7$)*

## Errori Comuni
*   Sbagliare l'indice dell'esponente o partire da $2^1$ anziché $2^0 = 1$.
*   Dimenticare il vincolo di limite superiore $\sum 2^k y_k \le u$ quando $u$ non coincide con un valore del tipo $2^{K+1}-1$, ammettendo così valori interi superiori a $u$ che violano i vincoli originali.

## Fonti
*   `Programmazione lineare intera completo.pdf`, Pagine 22-24
