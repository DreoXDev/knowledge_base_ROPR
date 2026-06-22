---
type: method-card
topic: programmazione-lineare
status: draft
sources:
  - raw_assets/Programmazione Lineare/lec_w4_completa.pdf
reliability: official
---

# METHOD — Costruzione del Problema Duale

## Quando usarla
Usare questa card per ricavare in modo sistematico il modello duale di un problema primale di Programmazione Lineare con variabili o vincoli misti.

## Procedura Operativa

### 1. Inversione dell'Ottimizzazione
- Se il primale è di massimizzazione ($\max$), il duale sarà di minimizzazione ($\min$).
- Se il primale è di minimizzazione ($\min$), il duale sarà di massimizzazione ($\max$).

### 2. Definizione delle Variabili Duali
Associare una variabile duale ad ogni vincolo funzionale del primale.
- **Primale MAX**:
  - Vincolo $\le$ (canonico) $\implies$ Variabile duale $\ge 0$
  - Vincolo $\ge$ (anticanonico) $\implies$ Variabile duale $\le 0$
  - Vincolo $=$ (uguaglianza) $\implies$ Variabile duale libera
- **Primale MIN**:
  - Vincolo $\ge$ (canonico) $\implies$ Variabile duale $\ge 0$
  - Vincolo $\le$ (anticanonico) $\implies$ Variabile duale $\le 0$
  - Vincolo $=$ (uguaglianza) $\implies$ Variabile duale libera

### 3. Definizione dei Vincoli Duali
Costruire un vincolo duale per ogni variabile decisionale del primale.
- **Primale MAX (Duale MIN)**:
  - Variabile primale $x_j \ge 0$ (canonica) $\implies$ Vincolo duale $j$-esimo $\ge$ (canonico in MIN)
  - Variabile primale $x_j \le 0$ (anticanonica) $\implies$ Vincolo duale $j$-esimo $\le$ (anticanonico in MIN)
  - Variabile primale $x_j$ libera $\implies$ Vincolo duale $j$-esimo $=$ (uguaglianza)
- **Primale MIN (Duale MAX)**:
  - Variabile primale $x_j \ge 0$ (canonica) $\implies$ Vincolo duale $j$-esimo $\le$ (canonico in MAX)
  - Variabile primale $x_j \le 0$ (anticanonica) $\implies$ Vincolo duale $j$-esimo $\ge$ (anticanonico in MAX)
  - Variabile primale $x_j$ libera $\implies$ Vincolo duale $j$-esimo $=$ (uguaglianza)

### 4. Trasposizione della Matrice dei Coefficienti e Scambio di Vettori
- La matrice dei coefficienti del duale è la trasposta $A^T$ del primale.
- La funzione obiettivo del duale ha come coefficienti i termini noti (RHS) del primale.
- I termini noti (RHS) dei vincoli duali sono i coefficienti della funzione obiettivo del primale.
