---
type: method
topic: programmazione_lineare_intera
status: active
sources: [modelli_PLI.pdf]
reliability: official
---

# Modellare Problemi con Variabili Binarie

## Quando Usarla
Questa metodologia si applica quando la traccia d'esame prevede scelte discrete di tipo sì/no (es. attivare un impianto, includere o meno un'attività, coprire o meno una determinata area con un budget definito).

## Dichiarazione delle Variabili
Una variabile decisionale binaria viene associata ad ogni opzione selezionabile:

$$
x_j = \begin{cases}
1 & \text{se si sceglie/attiva l'opzione } j \\
0 & \text{altrimenti}
\end{cases}
$$

È fondamentale definire esplicitamente il dominio nei modelli scritti:
$$
x_j \in \{0, 1\} \quad \forall j \in J
$$

## Esempi Tipici di Modellazione

### 1. Assegnamento
Assegnare lavoratori ad attività in modo che ciascun lavoratore svolga esattamente un'attività e ciascuna attività sia svolta da un solo lavoratore:
$$
x_{ij} = \begin{cases} 1 & \text{se il lavoratore } i \text{ svolge l'attività } j \\ 0 & \text{altrimenti} \end{cases}
$$
*   Ogni lavoratore $i$ fa una sola attività:
    $$
    \sum_{j=1}^n x_{ij} = 1 \quad \forall i
    $$
*   Ogni attività $j$ è svolta da un solo lavoratore:
    $$
    \sum_{i=1}^n x_{ij} = 1 \quad \forall j
    $$

### 2. Scelta d'Investimento (Zaino Binario)
Selezionare un sottoinsieme di progetti per massimizzare il rendimento totale senza superare un budget $C$:
$$
\max \sum_{j=1}^n v_j x_j
$$
$$
\text{s.t.} \quad \sum_{j=1}^n p_j x_j \le C
$$
$$
x_j \in \{0, 1\} \quad \forall j
$$

### 3. Apertura Impianti (Facility Location)
Decidere quali depositi aprire per servire un insieme di clienti:
$$
y_j = \begin{cases} 1 & \text{se si apre il deposito } j \\ 0 & \text{altrimenti} \end{cases}
$$
$$
x_{ij} = \begin{cases} 1 & \text{se il cliente } i \text{ è servito dal deposito } j \\ 0 & \text{altrimenti} \end{cases}
$$

## Errori Comuni da Evitare
*   Scrivere $x_j \ge 0$ intera invece di $x_j \in \{0, 1\}$: se il dominio deve essere binario, va indicato esplicitamente.
*   Scrivere vincoli con costanti non lineari.
*   Dimenticare di collegare le variabili di scelta $y_j$ alle variabili di flusso $x_{ij}$ (vincoli di attivazione e capacità).
