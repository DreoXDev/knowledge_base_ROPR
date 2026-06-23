---
type: solved_example
topic: programmazione_lineare_intera
status: active
sources: [Programmazione lineare intera completo.pdf]
reliability: official
---

# Esempio Svolto: Lombardia Manufacturing Co. (Modellazione PLI e Logica)

Problema decisionale aziendale che illustra l'uso di variabili decisionali binarie per modellare vincoli di budget, mutua esclusione e relazioni di contingenza logica (dipendenza decisionale).

---

## Dati del Problema

L'azienda **Lombardia Manufacturing Company** sta considerando l'opportunità di espandersi costruendo una nuova fabbrica e un nuovo magazzino, disponendo di un budget di investimento totale pari a **10 milioni di euro**.

Le alternative decisionali sono strutturate come segue:
1.  **Nuova fabbrica**: può essere costruita a **Saronno** oppure a **Gallarate** (o in entrambe le località).
2.  **Nuovo magazzino**: può essere costruito a **Saronno** oppure a **Gallarate** (al più uno dei due magazzini può essere costruito).
3.  **Vincolo di contingenza**: un magazzino può essere collocato in una città solo se la corrispondente fabbrica viene costruita in quella stessa città.

Valori attesi del Valore Attuale Netto (VAN) e capitali richiesti per ciascun investimento:

| Decisione | Variabile | Valore Attuale Netto ($Z_j$ in mln €) | Capitale Richiesto ($C_j$ in mln €) |
|---|---|---|---|
| Fabbrica a Saronno | $x_1$ | $9$ | $6$ |
| Fabbrica a Gallarate | $x_2$ | $5$ | $3$ |
| Magazzino a Saronno | $x_3$ | $6$ | $5$ |
| Magazzino a Gallarate | $x_4$ | $4$ | $2$ |

---

## Formulazione Matematica del Modello

### 1. Variabili Decisionali
Tutte le scelte sono di tipo sì/no, modellate con variabili binarie:
*   $x_1 \in \{0, 1\}$: $1$ se si costruisce la fabbrica a Saronno, $0$ altrimenti.
*   $x_2 \in \{0, 1\}$: $1$ se si costruisce la fabbrica a Gallarate, $0$ altrimenti.
*   $x_3 \in \{0, 1\}$: $1$ se si costruisce il magazzino a Saronno, $0$ altrimenti.
*   $x_4 \in \{0, 1\}$: $1$ se si costruisce il magazzino a Gallarate, $0$ altrimenti.

### 2. Funzione Obiettivo
Massimizzare il Valore Attuale Netto (VAN) complessivo atteso:
$$
\max \quad z = 9x_1 + 5x_2 + 6x_3 + 4x_4
$$

### 3. Vincoli del Problema

*   **Vincolo di Budget**:
    Il capitale totale investito non deve superare i 10 milioni di euro:
    $$
    6x_1 + 3x_2 + 5x_3 + 2x_4 \le 10
    $$

*   **Vincolo di Mutua Esclusione**:
    Si può costruire al più un solo magazzino:
    $$
    x_3 + x_4 \le 1
    $$

*   **Vincoli di Contingenza (Dipendenza Logica)**:
    Il magazzino può essere collocato a Saronno solo se a Saronno viene costruita la fabbrica:
    $$
    x_3 \le x_1
    $$
    *(Infatti, se $x_1 = 0 \implies x_3 = 0$. Se $x_1 = 1 \implies x_3 \in \{0, 1\}$.)*

    Il magazzino può essere collocato a Gallarate solo se a Gallarate viene costruita la fabbrica:
    $$
    x_4 \le x_2
    $$
    *(Infatti, se $x_2 = 0 \implies x_4 = 0$. Se $x_2 = 1 \implies x_4 \in \{0, 1\}$.)*

### 4. Dominio delle Variabili
$$
x_1, x_2, x_3, x_4 \in \{0, 1\}
$$

---

## Analisi e Risoluzione

Trattandosi di sole 4 variabili binarie, lo spazio delle soluzioni possibili è limitato a $2^4 = 16$ combinazioni totali. 

Analizziamo le soluzioni che rispettano i vincoli di contingenza ($x_3 \le x_1$ e $x_4 \le x_2$) e di mutua esclusione ($x_3 + x_4 \le 1$):

1.  **Nessuna costruzione**:
    *   $x = (0,0,0,0) \implies \text{Costo} = 0 \le 10 \implies z = 0$ (Ammissibile).
2.  **Una sola fabbrica**:
    *   Fabbrica Saronno: $x = (1,0,0,0) \implies \text{Costo} = 6 \le 10 \implies z = 9$ (Ammissibile).
    *   Fabbrica Gallarate: $x = (0,1,0,0) \implies \text{Costo} = 3 \le 10 \implies z = 5$ (Ammissibile).
3.  **Fabbrica e rispettivo magazzino**:
    *   Saronno (Fabbrica + Magazzino): $x = (1,0,1,0) \implies \text{Costo} = 6 + 5 = 11 > 10$ (**Inammissibile per budget**).
    *   Gallarate (Fabbrica + Magazzino): $x = (0,1,0,1) \implies \text{Costo} = 3 + 2 = 5 \le 10 \implies z = 5 + 4 = 9$ (Ammissibile).
4.  **Due fabbriche**:
    *   Fabbriche Saronno + Gallarate: $x = (1,1,0,0) \implies \text{Costo} = 6 + 3 = 9 \le 10 \implies z = 9 + 5 = 14$ (Ammissibile).
5.  **Due fabbriche e un magazzino**:
    *   Fabbriche Saronno + Gallarate, Magazzino Gallarate: $x = (1,1,0,1) \implies \text{Costo} = 6 + 3 + 2 = 11 > 10$ (**Inammissibile per budget**).
    *   Fabbriche Saronno + Gallarate, Magazzino Saronno: $x = (1,1,1,0) \implies \text{Costo} = 6 + 3 + 5 = 14 > 10$ (**Inammissibile per budget**).

La soluzione ottima intera del problema è **$x^* = (1,1,0,0)$**, ovvero costruire sia la fabbrica di Saronno sia quella di Gallarate senza magazzini, ottenendo un valore ottimale di $z^* = 14$.
