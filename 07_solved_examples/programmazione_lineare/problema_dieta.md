---
materia: ROPR
area: Programmazione Lineare
tipo: esempio-svolto
fonte: esercitazione1_complete.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - formulazione
  - minimizzazione
  - dieta
  - esempio-svolto
---

# Esempio Svolto — Il Problema della Dieta

Questo esempio descrive la formulazione classica del problema della dieta, un modello di programmazione lineare finalizzato alla minimizzazione del costo per soddisfare dei requisiti nutrizionali minimi.

## Testo del Problema

Un nutrizionista deve comporre una dieta bilanciata usando quattro diversi tipi di alimenti ($A_1, A_2, A_3, A_4$). Ciascun alimento contiene nutrienti fondamentali (proteine, carboidrati, grassi) in proporzioni differenti. Il costo unitario di ciascun alimento e i fabbisogni nutrizionali giornalieri minimi sono riassunti nella tabella:

| Nutriente / Alimento | $A_1$ (unità) | $A_2$ (unità) | $A_3$ (unità) | $A_4$ (unità) | Fabbisogno Minimo |
|---|---|---|---|---|---|
| Proteine (g) | $1$ | $3$ | $2$ | $3$ | $2$ g |
| Carboidrati (g) | $4$ | $4$ | $3$ | $2$ | $4$ g |
| Grassi (g) | $3$ | $2$ | $3$ | $4$ | $3$ g |
| **Costo unitario (€)** | **$3$** | **$6$** | **$5$** | **$6$** | |

Si desidera formulare il modello di programmazione lineare per determinare le quantità giornaliere di ciascun alimento da consumare in modo da minimizzare la spesa complessiva, garantendo il fabbisogno minimo di nutrienti.

---

## Formulazione Matematica

### 1. Variabili decisionali
Sia $x_i$ la quantità (espressa in unità) dell'alimento $A_i$ da inserire nella dieta giornaliera ($i = 1, 2, 3, 4$).

### 2. Funzione obiettivo
Minimizzare il costo totale giornaliero:
$$
\min Z = 3x_1 + 6x_2 + 5x_3 + 6x_4
$$

### 3. Vincoli
I vincoli rappresentano i fabbisogni nutrizionali giornalieri minimi (in genere espressi con relazioni di tipo $\ge$, poiché rappresenta una barriera minima obbligatoria):
- **Vincolo sulle Proteine**:
  $$
  x_1 + 3x_2 + 2x_3 + 3x_4 \ge 2
  $$
- **Vincolo sui Carboidrati**:
  $$
  4x_1 + 4x_2 + 3x_3 + 2x_4 \ge 4
  $$
- **Vincolo sui Grassi**:
  $$
  3x_1 + 2x_2 + 3x_3 + 4x_4 \ge 3
  $$

### 4. Dominio
Le variabili decisionali rappresentano quantità fisiche continue che non possono assumere valori negativi:
$$
x_1, x_2, x_3, x_4 \ge 0
$$

---

## Nota Didattica

1. **Direzione dei vincoli**: A differenza dei problemi di pianificazione della produzione (dove i vincoli sono generalmente del tipo $\le$ per via di capacità produttive limitate), nei problemi nutrizionali o di dieta i vincoli sono solitamente del tipo $\ge$. Si richiede infatti di consumare *almeno* una determinata quantità di nutrienti.
2. **Forma Standard**: Il problema è un tipico modello di minimizzazione in forma standard per il duale (ma non per il simplesso primale standard, che richiede vincoli $\le$ e obiettivi $\max$). Per risolverlo con il metodo del simplesso tabellare classico, occorrerebbe introdurre le variabili di surplus e le variabili artificiali (metodo a due fasi o Big M).
