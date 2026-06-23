---
type: solved_example
topic: programmazione_lineare_intera
status: active
sources: [9_esercizi_modelli.pdf]
reliability: official
---

# Esempio Svolto: Lo Stendino di Remo (Minimizzazione e Bilanciamento)

Esempio di modellazione PLI per la disposizione ottimale di panni su uno stendino con vincoli di capacità spaziale, bilanciamento fisico dei pesi e logiche combinatorie.

---

## Dati del Problema

- **Indumenti da stendere**:
  1.  Maglietta bianca ($L_1 = 40$ cm, $P_1 = 0.2$ kg)
  2.  Maglietta verde ($L_2 = 45$ cm, $P_2 = 0.25$ kg)
  3.  Felpa ($L_3 = 50$ cm, $P_3 = 0.35$ kg)
  4.  Pantalone lungo ($L_4 = 50$ cm, $P_4 = 0.6$ kg)
  5.  Costume blu ($L_5 = 30$ cm, $P_5 = 0.25$ kg)
  6.  Costume rosso ($L_6 = 25$ cm, $P_6 = 0.25$ kg)
  7.  Telo da spiaggia ($L_7 = 100$ cm, $P_7 = 1.1$ kg)
  8.  Mutande bianche ($L_8 = 30$ cm, $P_8 = 0.2$ kg)
  9.  Mutande nere ($L_9 = 20$ cm, $P_9 = 0.15$ kg)
- **File dello stendino**: $j \in \{1, 2, 3, 4\}$. Lunghezza di ciascuna fila: $110$ cm.

---

## Modello Base: Esercizio 8 (Tutti i panni stesi)

### 1. Variabili Decisionali
*   $x_{ij} \in \{0, 1\}$: Vale $1$ se l'indumento $i \in \{1, \dots, 9\}$ viene steso sulla fila $j \in \{1, 2, 3, 4\}$, $0$ altrimenti.
*   $y_j \in \{0, 1\}$: Vale $1$ se la fila $j$ viene utilizzata, $0$ altrimenti.

### 2. Funzione Obiettivo
Minimizzare il numero totale di file dello stendino utilizzate:

$$
\min \sum_{j=1}^4 y_j
$$

### 3. Vincoli Funzionali

*   **Assegnamento Obbligatorio**:
    Ogni indumento $i$ deve essere steso su esattamente una fila:
    $$
    \sum_{j=1}^4 x_{ij} = 1 \quad \forall i=1, \dots, 9
    $$

*   **Capacità Spaziale delle File**:
    La somma delle lunghezze degli indumenti stesi sulla fila $j$ non può superare la lunghezza della fila ($110$ cm), ed è vincolata all'attivazione della fila $y_j$:
    $$
    \sum_{i=1}^9 L_i x_{ij} \le 110 y_j \quad \forall j=1, \dots, 4
    $$

*   **Bilanciamento del Peso (File esterne $\le$ File interne)**:
    Il peso complessivo sulle file estreme (1 e 4) non deve superare il peso sulle file interne (2 e 3):
    $$
    \sum_{i=1}^9 P_i x_{i1} + \sum_{i=1}^9 P_i x_{i4} \le \sum_{i=1}^9 P_i x_{i2} + \sum_{i=1}^9 P_i x_{i3}
    $$
    Linearizzato come:
    $$
    \sum_{i=1}^9 P_i (x_{i1} + x_{i4} - x_{i2} - x_{i3}) \le 0
    $$

---

## Modello Modificato: Esercizio 9 (Stesa opzionale e logiche)

Nelle varianti dell'Esercizio 9:
- Stendere tutti i panni non è più obbligatorio ($\sum_j x_{ij} \le 1$).
- Si introduce la variabile di stesa del panno $s_i = \sum_{j=1}^4 x_{ij} \in \{0, 1\}$.

### Vincoli Aggiuntivi:

*   **Stesa minima (Almeno 5 indumenti)**:
    $$
    \sum_{i=1}^9 s_i \ge 5
    $$

*   **Condizione logica OR (Almeno 2 capi da mare OR almeno 3 dei primi 4 indumenti)**:
    Introduciamo due variabili binarie di scelta $a, b \in \{0, 1\}$:
    $$
    \sum_{i=5}^7 s_i \ge 2 a \quad (\text{capi da mare: 5, 6, 7})
    $$
    $$
    \sum_{i=1}^4 s_i \ge 3 b \quad (\text{primi 4 indumenti})
    $$
    $$
    a + b \ge 1
    $$

*   **Condizione d'Implicazione (Telo spiaggia steso solo se almeno un costume steso)**:
    $$
    s_7 \le s_5 + s_6
    $$

### 4. Dominio delle Variabili (Modello Modificato)
$$
x_{ij} \in \{0, 1\} \quad \forall i, j
$$
$$
y_j \in \{0, 1\} \quad \forall j
$$
$$
s_i \in \{0, 1\} \quad \forall i
$$
$$
a, b \in \{0, 1\}
$$
