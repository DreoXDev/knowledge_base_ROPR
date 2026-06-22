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
  - trasporto
  - reti-distribuzione
  - esempio-svolto
---

# Esempio Svolto — Reti di Distribuzione (Bell Computers)

Questo esempio mostra come formulare in modo compatto un classico problema di trasporto (reti di distribuzione) su una rete stabilimenti-centri di distribuzione.

## Testo del Problema

La Bell Computers produce personal computer in tre stabilimenti situati a:
1. Portland ($s_1$)
2. San Jose ($s_2$)
3. Pasadena ($s_3$)

I computer devono essere distribuiti a quattro magazzini principali situati a:
1. Chicago ($d_1$)
2. Houston ($d_2$)
3. New York ($d_3$)
4. Denver ($d_4$)

La tabella seguente riporta le capacità massime di offerta di ogni stabilimento, le domande di ciascun magazzino e i costi unitari di trasporto per ciascuna tratta:

| Da \ A | Chicago ($d_1$) | Houston ($d_2$) | New York ($d_3$) | Denver ($d_4$) | Offerta (capacità) |
|---|---|---|---|---|---|
| **Portland ($s_1$)** | € 22 | € 30 | € 25 | € 20 | **10.000** |
| **San Jose ($s_2$)** | € 15 | € 12 | € 20 | € 24 | **15.000** |
| **Pasadena ($s_3$)** | € 28 | € 20 | € 12 | € 18 | **20.000** |
| **Domanda** | **12.000** | **8.000** | **15.000** | **10.000** | |

Si desidera formulare il modello di programmazione lineare compatto che minimizzi il costo totale di trasporto, rispettando le capacità degli stabilimenti e soddisfacendo le richieste dei magazzini.

---

## Formulazione Matematica Compatta

### 1. Insiemi e Indici
- $I = \{1, 2, 3\}$: insieme degli stabilimenti produttivi ($i \in I$).
- $J = \{1, 2, 3, 4\}$: insieme dei centri di distribuzione/magazzini ($j \in J$).

### 2. Parametri
- $c_{ij}$: costo unitario di trasporto dal produttore $i$ al centro $j$ (da tabella).
- $s_i$: capacità di offerta dello stabilimento $i$ ($s_1 = 10k, s_2 = 15k, s_3 = 20k$).
- $d_j$: domanda del magazzino $j$ ($d_1 = 12k, d_2 = 8k, d_3 = 15k, d_4 = 10k$).

### 3. Variabili decisionali
Sia $x_{ij}$ la quantità di computer trasportata dallo stabilimento $i$ al magazzino $j$ ($\forall i \in I, j \in J$).

### 4. Funzione obiettivo
Minimizzare il costo complessivo di trasporto:
$$
\min Z = \sum_{i \in I} \sum_{j \in J} c_{ij} x_{ij}
$$

### 5. Vincoli
- **Vincoli di offerta** (la quantità spedita da ciascuno stabilimento non può superare la sua capacità):
  $$
  \sum_{j \in J} x_{ij} \le s_i \qquad \forall i \in I
  $$
- **Vincoli di domanda** (ciascun magazzino deve ricevere la quantità esatta richiesta):
  $$
  \sum_{i \in I} x_{ij} \ge d_j \qquad \forall j \in J
  $$

### 6. Dominio
Le variabili di trasporto sono continue e non negative:
$$
x_{ij} \ge 0 \qquad \forall i \in I, j \in J
$$

---

## Nota Didattica (Bilanciamento del Problema)

In questo specifico problema, calcolando le somme complessive di offerta e domanda notiamo che:
- Offerta totale: $\sum_{i \in I} s_i = 10.000 + 15.000 + 20.000 = 45.000$ unità.
- Domanda totale: $\sum_{j \in J} d_j = 12.000 + 8.000 + 15.000 + 10.000 = 45.000$ unità.

Poiché l'offerta totale è esattamente uguale alla domanda totale ($\sum s_i = \sum d_j$), il problema si dice **perfettamente bilanciato**. In tali casi, tutti i vincoli di offerta e domanda possono essere scritti in forma di **uguaglianza ($=$)**:
$$
\sum_{j \in J} x_{ij} = s_i \qquad \forall i \in I
$$
$$
\sum_{i \in I} x_{ij} = d_j \qquad \forall j \in J
$$
Questo semplifica l'analisi e garantisce speciali proprietà strutturali (matrice dei vincoli totalmente unimodulare, che assicura soluzioni intere se i termini noti sono interi).
