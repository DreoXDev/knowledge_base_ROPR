---
materia: ROPR
area: Programmazione Lineare Intera
tipo: esempio-svolto
fonte: Esercitazione 2 PL.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare-intera
  - set-covering
  - maximum-coverage
  - formulazione
  - esempio-svolto
---

# Esempio Svolto — Set Covering e Maximum Coverage (CALL.spa)

Questo esempio illustra le due formulazioni tipiche per la localizzazione di servizi/antenne: il modello di **Set Covering** (copertura totale a costo minimo) e il modello di **Maximum Coverage** (massimizzazione della copertura con risorse limitate).

## Testo del Problema

La CALL.spa deve localizzare dei ripetitori di telefonia mobile in una regione suddivisa in $36$ zone quadrate ($Z = \{1, \dots, 36\}$). Ciascun ripetitore installato in una zona $i$ copre la zona stessa e le zone adiacenti (confrontando la mappa di adiacenza della regione).
I dati sulla popolazione (utenti potenziali) in ciascuna zona $j$ sono indicati da un parametro $u_j$.

Si vogliono formulare due modelli alternativi:
- **Parte A (Set Covering)**: Coprire tutte le 36 zone minimizzando il numero totale di ripetitori installati.
- **Parte B (Maximum Coverage)**: Scegliere di installare esattamente $5$ ripetitori in modo da massimizzare il numero totale di utenti coperti.

---

## Parte A: Modello di Set Covering

L'obiettivo è garantire la copertura minima a tutta la regione al minor costo.

### 1. Parametri di Adiacenza
Sia $a_{ji}$ la matrice di copertura:
- $a_{ji} = 1$ se un ripetitore installato nella zona $i$ copre la zona $j$ (cioè $j$ coincide con $i$ o è adiacente).
- $a_{ji} = 0$ altrimenti.

### 2. Variabili decisionali
Sia $x_i$ la variabile di installazione binaria ($\forall i \in Z$):
- $x_i = 1$ se si installa un ripetitore nella zona $i$.
- $x_i = 0$ altrimenti.

### 3. Funzione obiettivo
Minimizzare il numero totale di installazioni:
$$
\min Z = \sum_{i \in Z} x_i
$$

### 4. Vincoli
Imporre che ciascuna zona $j$ sia coperta da almeno un ripetitore:
$$
\sum_{i \in Z} a_{ji} x_i \ge 1 \qquad \forall j \in Z
$$

### 5. Dominio
Le variabili sono binarie:
$$
x_i \in \{0, 1\} \qquad \forall i \in Z
$$

---

## Parte B: Modello di Maximum Coverage

L'obiettivo cambia: con un budget fisso per soli 5 ripetitori, vogliamo massimizzare l'utilità (popolazione coperta).

### 1. Variabili decisionali
- $x_i$: variabile binaria di installazione, definita come sopra ($\forall i \in Z$).
- $y_j$: variabile binaria di copertura ($\forall j \in Z$):
  - $y_j = 1$ se la zona $j$ risulta coperta da almeno uno dei ripetitori installati.
  - $y_j = 0$ altrimenti.

### 2. Funzione obiettivo
Massimizzare la popolazione coperta:
$$
\max W = \sum_{j \in Z} u_j y_j
$$

### 3. Vincoli
- **Vincolo di cardinalità (budget)**: Si possono installare esattamente $5$ ripetitori:
  $$
  \sum_{i \in Z} x_i = 5
  $$
- **Vincolo di attivazione della copertura**: La zona $j$ può essere considerata coperta ($y_j = 1$) solo se si installa almeno un ripetitore in una zona $i$ in grado di coprirla:
  $$
  y_j \le \sum_{i \in Z} a_{ji} x_i \qquad \forall j \in Z
  $$

### 4. Dominio
Tutte le variabili sono binarie:
$$
x_i \in \{0, 1\}, \quad y_j \in \{0, 1\} \qquad \forall i, j \in Z
$$

---

## Nota Fondamentale di Modellazione (Variabile $y_j$)

> [!IMPORTANT]
> Nel modello di **Maximum Coverage**, l'introduzione delle variabili di copertura $y_j$ è essenziale per evitare il **doppio conteggio**.
> 
> Se scrivessimo ingenuamente una funzione obiettivo del tipo $\max \sum_{j} u_j \left(\sum_{i} a_{ji} x_i\right)$, il modello massimizzerebbe il numero di ripetitori sovrapposti sulla stessa zona densamente popolata, contando più volte i medesimi utenti.
> 
> Usando $y_j \in \{0,1\}$ limitata dal vincolo $y_j \le \sum a_{ji} x_i$, garantiamo che:
> - Se $\sum a_{ji} x_i = 0$, allora $y_j = 0$ (nessuna copertura).
> - Se $\sum a_{ji} x_i \ge 1$ (la zona è coperta da 1, 2 o più ripetitori), la variabile $y_j$ può assumere valore al massimo $1$, catturando la popolazione $u_j$ della zona **una sola volta** nella funzione obiettivo.
