---
type: theory
topic: programmazione_lineare_intera
status: active
sources: [Programmazione lineare intera completo.pdf]
reliability: official
---

# Programmazione Lineare Intera - Logica e Variabili Binarie

## Fonte
`Programmazione lineare intera completo.pdf` (Dispensa/Slide Ufficiali del Corso)

## Introduzione e Scelte Sì/No
Le variabili binarie $x_j \in \{0, 1\}$ sono uno strumento fondamentale in Ricerca Operativa per modellare decisioni mutuamente esclusive o logiche del tipo **sì/no**.
*   $x_j = 1$ se la decisione $j$ viene intrapresa (Sì).
*   $x_j = 0$ se la decisione $j$ non viene intrapresa (No).

Esempi classici includono:
*   **Analisi di investimenti**: Devo o no investire nel progetto $i$? ($x_i \in \{0, 1\}$).
*   **Selezione di siti**: Una determinata località deve essere scelta per un servizio? ($x_{ij} \in \{0, 1\}$).
*   **Spedizione di beni (Routing)**: Uno specifico arco $(i, j)$ in un grafo deve essere selezionato per un veicolo? ($x_{ij} \in \{0, 1\}$).
*   **Assegnamento velivoli**: Lo specifico velivolo $i$ deve coprire la tratta $j$? ($x_{ij} \in \{0, 1\}$).
*   **Schedulazione di attività**: Un'attività deve iniziare all'istante temporale $t$? ($x_t \in \{0, 1\}$). Se l'attività deve iniziare in un solo istante preciso, si applica il vincolo di mutua esclusione $\sum_t x_t = 1$.

---

## Modellazione di Condizioni Logiche

### 1. Condizioni di Contingenza e Mutua Esclusione
*   **Mutua esclusione**: Dati due progetti (o siti) $j_1$ e $j_2$, al più uno può essere selezionato:
    $$x_{j_1} + x_{j_2} \le 1$$
*   **Contingenza (Dipendenza)**: Il progetto $j_2$ può essere selezionato solo se il progetto $j_1$ viene a sua volta selezionato (es. posso costruire un magazzino a Saronno solo se costruisco la fabbrica a Saronno):
    $$x_{j_2} \le x_{j_1}$$
    *   Se $x_{j_1} = 0 \implies x_{j_2} = 0$.
    *   Se $x_{j_1} = 1 \implies x_{j_2} \in \{0, 1\}$.

### 2. Vincoli di tipo "Either-Or" (Almeno uno su due)
Si consideri il caso in cui, dati due vincoli lineari, **almeno uno dei due** deve essere soddisfatto:
1.  $f_1(x_1, \dots, x_n) \le d_1$
2.  $f_2(x_1, \dots, x_n) \le d_2$

Introducendo una variabile binaria $y \in \{0, 1\}$ e un numero positivo molto grande $M$ (Big-M), la condizione si modella come:
$$f_1(x_1, \dots, x_n) \le d_1 + M y$$
$$f_2(x_1, \dots, x_n) \le d_2 + M(1-y)$$

*   Se $y = 0$: il primo vincolo diventa $f_1(x) \le d_1$ (attivo), mentre il secondo diventa $f_2(x) \le d_2 + M$ (disattivato, sempre soddisfatto per $M$ sufficientemente grande).
*   Se $y = 1$: il primo vincolo diventa $f_1(x) \le d_1 + M$ (disattivato), mentre il secondo diventa $f_2(x) \le d_2$ (attivo).

### 3. Dati $N$ vincoli, solo $K$ devono essere soddisfatti ($K < N$)
Generalizzando il concetto di "either-or", si consideri un insieme di $N$ vincoli del tipo $f_i(x_1, \dots, x_n) \le d_i$ per $i = 1, \dots, N$. Se si richiede che **almeno** $K$ di questi vincoli siano soddisfatti contemporaneamente:
$$f_i(x_1, \dots, x_n) \le d_i + M y_i \quad \forall i = 1, \dots, N$$
$$\sum_{i=1}^N y_i = N - K$$
$$y_i \in \{0, 1\} \quad \forall i = 1, \dots, N$$

*   Se $y_i = 1$, il vincolo $i$-esimo viene disattivato ($f_i(x) \le d_i + M$).
*   Il numero di vincoli disattivati deve essere esattamente $N-K$ (o al più $N-K$, scrivendo $\sum y_i \le N-K$), il che garantisce che almeno $K$ vincoli rimangano attivi (avendo $y_i = 0$).

### 4. Funzioni che assumono solo $N$ valori discreti
Si consideri il caso in cui una data funzione (o variabile) debba assumere esattamente uno tra $N$ valori discreti possibili $\{d_1, d_2, \dots, d_N\}$:
$$f(x_1, \dots, x_n) \in \{d_1, d_2, \dots, d_N\}$$

Questo requisito viene modellato introducendo $N$ variabili binarie $y_i \in \{0, 1\}$ soggette a:
$$f(x_1, \dots, x_n) = \sum_{i=1}^N d_i y_i$$
$$\sum_{i=1}^N y_i = 1$$

*Esempio (Windor Glass Co.)*: La capacità utilizzabile per la produzione deve essere pari a $6$, $12$ o $18$ ore, sostituendo il vincolo originale $3x_1 + 2x_2 \le 18$ con:
$$3x_1 + 2x_2 = 6y_1 + 12y_2 + 18y_3$$
$$y_1 + y_2 + y_3 = 1$$
$$y_1, y_2, y_3 \in \{0, 1\}$$

---

## Il Problema del Costo Fisso (Carica Fissa)
Supponiamo che intraprendere un'attività $x \ge 0$ comporti un costo fisso di attivazione $k > 0$ non appena $x > 0$, oltre a un costo variabile unitario $c \cdot x$:
$$f(x) = \begin{cases} k + c x & \text{se } x > 0 \\ 0 & \text{se } x = 0 \end{cases}$$

Questo costo non-lineare può essere modellato in PLI introducendo una variabile binaria di attivazione $y \in \{0, 1\}$ e un valore $M$ molto grande che rappresenta la capacità massima dell'attività $x$:
$$\min \quad z = k y + c x$$
$$\text{s.t.} \quad x \le M y$$
$$y \in \{0, 1\}, \quad x \ge 0$$

*   Se $y = 0 \implies x \le 0 \implies x = 0$ (poiché $x \ge 0$). Il costo totale sarà $z = 0$.
*   Se $y = 1 \implies x \le M$ (l'attività può essere svolta liberamente fino al limite superiore $M$). Il costo totale sarà $z = k + c x$.
Poiché l'obiettivo minimizza $z$, il modello eviterà di porre $y = 1$ a meno che $x$ non debba essere strettamente maggiore di $0$.

---

## Rappresentazione Binaria di Variabili Intere Generiche
Un problema di PLI puro con variabili intere generali $x$ limitate superiormente ($x \in [0, u]$) può essere interamente convertito in un problema a sole variabili binarie.
Sia $K$ l'intero tale che:
$$2^K \le u < 2^{K+1}$$

La variabile intera $x$ può essere espressa come espansione pesata in base 2:
$$x = \sum_{k=0}^K 2^k y_k = y_0 + 2y_1 + 4y_2 + \dots + 2^K y_K$$
$$y_k \in \{0, 1\} \quad \forall k = 0, \dots, K$$

Sostituendo ogni occorrenza di $x$ nel modello con la sua espansione binaria, si ottiene un modello equivalente a sole variabili binarie.

*Esempio*: Dati i vincoli $x_1 \le 5$, $2x_1 + 3x_2 \le 30$ con $x_1, x_2 \in \mathbb{Z}_+$:
*   Per $x_1$: $u_1 = 5 \implies 2^2 \le 5 < 2^3 \implies K = 2$.
    $$x_1 = y_0 + 2y_1 + 4y_2$$
*   Per $x_2$: la capacità teorica massima (se $x_1=0$) è $x_2 \le 10 \implies u_2 = 10 \implies 2^3 \le 10 < 2^4 \implies K = 3$.
    $$x_2 = y_3 + 2y_4 + 4y_5 + 8y_6$$

Sostituendo nei vincoli:
$$y_0 + 2y_1 + 4y_2 \le 5$$
$$2(y_0 + 2y_1 + 4y_2) + 3(y_3 + 2y_4 + 4y_5 + 8y_6) \le 30$$

---

## Difficoltà di Risoluzione e Fallimento dell'Arrotondamento
I problemi di PLI sono significativamente più difficili dei problemi continui (NP-difficili). Il numero di soluzioni ammissibili per $n$ variabili binarie è pari a $2^n$ (crescita esponenziale). La rimozione dei punti frazionari rende inapplicabile il metodo del simplesso poiché viene a mancare la continuità della regione ammissibile e non è garantita l'esistenza di vertici ammissibili.

### Il Rilassamento Continuo
Il rilassamento continuo di un problema PLI consiste nel risolvere lo stesso problema rimuovendo i vincoli di interezza (es. sostituendo $x_j \in \{0, 1\}$ con $0 \le x_j \le 1$). Esso fornisce:
*   Un **Upper Bound ($UB$)** per problemi di massimizzazione.
*   Un **Lower Bound ($LB$)** per problemi di minimizzazione.
Se la soluzione del rilassamento continuo è intera, allora è anche la soluzione ottima del problema intero.

### Perché l'Arrotondamento Fallisce: Contro-esempi Ufficiali

#### Contro-esempio 1: Inammissibilità dell'arrotondamento
Si consideri il problema:
$$\max \quad z = x_2$$
$$\text{s.t.} \quad -x_1 + x_2 \le \frac{1}{2}$$
$$2x_1 + x_2 \le \frac{7}{2}$$
$$x_1, x_2 \in \mathbb{Z}_+$$

1.  **Ottimo del Rilassamento Continuo**: Si ottiene intersecando le due rette di confine:
    $$-x_1 + x_2 = \frac{1}{2} \implies x_2 = x_1 + \frac{1}{2}$$
    $$2x_1 + (x_1 + \frac{1}{2}) = \frac{7}{2} \implies 3x_1 = 3 \implies x_1 = 1 \implies x_2 = \frac{3}{2} = 1.5$$
    La soluzione ottima continua è $x^* = (1, 1.5)$ con valore $z^* = 1.5$.
2.  **Tentativo di Arrotondamento**: Le soluzioni intere più vicine ad arrotondare la variabile frazionaria $x_2 = 1.5$ sono:
    *   Arrotondamento per eccesso: $(1, 2)$. Sostituendo nel primo vincolo: $-1 + 2 = 1 > 0.5$ (**Inammissibile**).
    *   Arrotondamento per difetto: $(1, 1)$. Sostituendo nel secondo vincolo: $2(1) + 1 = 3 \le 3.5$ (Ammissibile, valore $z = 1$).
    *   L'ottimo intero effettivo è in realtà $(1, 1)$ oppure $(2, 1)$ o $(0, 0)$. In questo caso l'arrotondamento per eccesso viola la fattibilità.

#### Contro-esempio 2: Sub-ottimalità estrema
Si consideri il problema:
$$\max \quad z = x_1 + 5x_2$$
$$\text{s.t.} \quad x_1 + 10x_2 \le 20$$
$$x_1 \le 2$$
$$x_1, x_2 \in \mathbb{Z}_+$$

1.  **Ottimo del Rilassamento Continuo**:
    Posto $x_1 = 2$, dalla prima equazione ricaviamo $2 + 10x_2 \le 20 \implies x_2 = 1.8$.
    La soluzione ottima rilassata è $x^*_{\text{LP}} = (2, 1.8)$ con valore $z^*_{\text{LP}} = 2 + 5(1.8) = 11$.
2.  **Tentativo di Arrotondamento**:
    L'arrotondamento all'intero più vicino per $x_2 = 1.8$ è $x_2 \to 2$.
    *   Punto $(2, 2)$: Sostituendo nel vincolo: $2 + 10(2) = 22 > 20$ (**Inammissibile**).
    *   Punto $(2, 1)$ (arrotondando per difetto): Ammissibile, valore $z = 2 + 5(1) = 7$.
3.  **Ottimo Intero Reale**:
    Provando a porre $x_2 = 2 \implies x_1 + 10(2) \le 20 \implies x_1 \le 0 \implies x_1 = 0$.
    Il punto $(0, 2)$ è ammissibile per l'intero e fornisce valore $z^*_{\text{IP}} = 0 + 5(2) = 10$.
    *   Confronto: La soluzione arrotondata ammissibile $(2, 1)$ ha un valore di $7$, mentre l'ottimo intero reale $(0, 2)$ ha un valore di $10$. L'arrotondamento ha causato una perdita di ottimalità del $30\%$, dimostrando che l'arrotondamento può allontanare drasticamente dalla soluzione ottima.
