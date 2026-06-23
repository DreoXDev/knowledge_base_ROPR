---
type: solved_example
topic: programmazione_lineare_intera
status: active
sources: [9_esercizi_modelli.pdf]
reliability: official
---

# Esempio Svolto: Localizzazione Asili Nido Montani

Esempio di modellazione PLI per la scelta dei siti in cui aprire asili nido e la pianificazione del personale educativo proporzionale al numero di bambini.

---

## Dati del Problema

- **Insieme dei paesi**: $I$.
- **Bambini residenti nel paese $i \in I$**: $b_i$.
- **Costo trasporto (scuolabus) da paese $i$ a paese $j$**: $c_{ij}$ all'anno.
- **Numero massimo asili da aprire**: $p$.
- **Costo annuo di un educatore**: $g$.
- **Rapporto di legge**: $1$ educatore ogni $q$ bambini.

---

## Modello Matematico (PLI)

### 1. Variabili Decisionali
*   $y_j \in \{0, 1\}$: Vale $1$ se viene aperto un asilo nido nel paese $j \in I$, $0$ altrimenti.
*   $z_{ij} \in \{0, 1\}$: Vale $1$ se i bambini del paese $i$ vengono assegnati all'asilo del paese $j$, $0$ altrimenti.
*   $x_j \ge 0$, intero: Numero di educatori assunti per l'asilo nel paese $j \in I$.

### 2. Funzione Obiettivo
Minimizzare i costi complessivi annui di trasporto (scuolabus) e di personale (educatori):

$$
\min \sum_{i \in I} \sum_{j \in I} c_{ij} z_{ij} + g \sum_{j \in I} x_j
$$

### 3. Vincoli Funzionali

*   **Assegnamento Unico**:
    Tutti i bambini di ciascun paese $i$ devono essere assegnati a un solo asilo nido:
    $$
    \sum_{j \in I} z_{ij} = 1 \quad \forall i \in I
    $$

*   **Apertura del Nido per Assegnamento**:
    I bambini possono essere inviati al paese $j$ solo se in quel paese è stato effettivamente aperto un asilo:
    $$
    z_{ij} \le y_j \quad \forall i, j \in I
    $$

*   **Limite Massimo Asili Aperti**:
    Il numero totale di asili aperti non può superare il budget $p$:
    $$
    \sum_{j \in I} y_j \le p
    $$

*   **Fabbisogno Educatori (1 ogni $q$ bambini)**:
    Il numero totale di bambini frequentanti l'asilo $j$ è $\sum_{i \in I} b_i z_{ij}$. Il numero di educatori $x_j$ deve essere tale da coprire questo volume:
    $$
    x_j \ge \frac{\sum_{i \in I} b_i z_{ij}}{q} \quad \forall j \in I
    $$
    Linearizzato come:
    $$
    q x_j - \sum_{i \in I} b_i z_{ij} \ge 0 \quad \forall j \in I
    $$
    *(Nota: se $y_j = 0$, per i vincoli precedenti si ha $z_{ij} = 0 \ \forall i$, il che implica $x_j \ge 0$. Trattandosi di un problema di minimo, l'ottimizzatore assegnerà $x_j = 0$ per i nodi chiusi).*

### 4. Dominio delle Variabili
$$
y_j \in \{0, 1\} \quad \forall j \in I
$$
$$
z_{ij} \in \{0, 1\} \quad \forall i, j \in I
$$
$$
x_j \ge 0, \text{ intero} \quad \forall j \in I
$$
