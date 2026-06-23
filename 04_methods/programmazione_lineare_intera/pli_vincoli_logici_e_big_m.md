---
type: method
topic: programmazione_lineare_intera
status: active
sources: [modelli_PLI.pdf]
reliability: official
---

# Vincoli Logici e Linearizzazione Big-M

## Quando Usarla
Questa metodologia si applica per formulare relazioni logiche tra variabili continue/intere (quantità prodotta o trasportata $x_i$) e variabili binarie (scelta di attivazione/produzione $y_i \in \{0, 1\}$). 
Tipici casi d'esame includono vincoli del tipo: "se un prodotto viene realizzato, la produzione deve rispettare una quantità minima e una capacità massima".

## Modello Generale (Attivazione e Capacità)
Sia $x_i$ la quantità prodotta del bene $i$ e $y_i \in \{0, 1\}$ la variabile binaria associata alla decisione di produrre o meno il bene $i$.

### 1. Vincolo di Attivazione Superiore (Capacità Massima)
Per imporre che $x_i$ sia nulla qualora non si decida di produrre il bene $i$ ($y_i = 0$), e che sia limitata da una capacità massima $U_i$ se attiva ($y_i = 1$):

$$
x_i \le U_i y_i
$$

*   Se $y_i = 0 \implies x_i \le 0 \implies x_i = 0$ (per via della non negatività).
*   Se $y_i = 1 \implies x_i \le U_i$.

### 2. Vincolo di Produzione Minima (Soglia Inferiore)
Per imporre che, qualora si scelga di produrre ($y_i = 1$), la quantità prodotta debba essere almeno pari a un limite minimo $L_i > 0$:

$$
L_i y_i \le x_i
$$

*   Se $y_i = 0 \implies x_i \ge 0$ (nessun vincolo inferiore stringente).
*   Se $y_i = 1 \implies x_i \ge L_i$.

Combinando entrambi i vincoli si ottiene il dominio condizionato:
$$
y_i \in \{0, 1\}, \quad x_i \in \{0\} \cup [L_i, U_i]
$$
espressa linearmente dalle disuguaglianze:
$$
L_i y_i \le x_i \le U_i y_i
$$

## Uso del parametro Big-M
Quando non è noto a priori un limite fisico superiore $U_i$ sulla variabile $x_i$, si utilizza una costante sufficientemente grande $M$ (tecnica del Big-M):

$$
x_i \le M y_i
$$

### Come Scegliere $M$
Il valore di $M$ deve essere grande abbastanza da non tagliare fuori alcuna soluzione ottima ammissibile quando $y_i = 1$, ma il più piccolo possibile per non indebolire il rilassamento continuo.
*   *Esempio*: Se la produzione totale è limitata dalla capacità complessiva di risorse disponibili $C$ e ciascuna unità richiede $a_i$ risorse, una scelta sensata è $M = C / a_i$.

## Errori Comuni da Evitare
*   **Utilizzare un valore di $M$ sproporzionatamente grande senza motivazione**: Questo porta a instabilità numerica e rende il rilassamento continuo estremamente debole (gap di dualità elevato).
*   **Dimenticare il vincolo di lower bound**: Se il testo specifica "se produco, ne produco almeno $L$", è necessario il vincolo $L y_i \le x_i$, non basta $x_i \le M y_i$.
*   **Invertire il verso del vincolo**: Scrivere $x_i \ge M y_i$ per la capacità massima.
