---
materia: ROPR
area: Programmazione Lineare
tipo: metodo
fonte: Esercitazione 2 PL.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - formulazione
  - miscelazione
  - linearizzazione
  - method-card
---

# METHOD CARD — Problemi di Miscelazione (Blending)

## Quando usarla

Usare questa card per modellare problemi di miscelazione industriale (es. benzine, mangimi, leghe metalliche) in cui diversi ingredienti/stock vengono uniti per produrre miscele finali soggette a vincoli fisici o chimici di qualità media (es. ottani, viscosità, percentuale di un elemento).

---

## Logica di Modellazione

Nei problemi di miscelazione, le variabili possono rappresentare le **quantità fisiche** (es. barili, tonnellate) di ciascun ingrediente destinato a ciascuna miscela.

### Insiemi e Variabili
Sia $C$ l'insieme dei costituenti ($c \in C$) e $M$ l'insieme delle miscele finali ($m \in M$).
- $x_{cm}$: quantità di costituente $c$ miscelata nel prodotto finale $m$.

La quantità totale di miscela $m$ prodotta sarà:
$$
T_m = \sum_{c \in C} x_{cm}
$$

---

## Vincoli di Qualità Media e Linearizzazione

I requisiti qualitativi sono spesso descritti come medie pesate delle caratteristiche dei costituenti. Ad esempio, se il costituente $c$ ha una concentrazione o valore qualitativo pari a $q_c$ (es. numero di ottani), e la miscela finale $m$ deve garantire un valore minimo pari a $Q_m^{min}$:

### 1. Formato Frazionario (Non Lineare)
$$
\frac{\sum_{c \in C} q_c x_{cm}}{\sum_{c \in C} x_{cm}} \ge Q_m^{min}
$$
Questo vincolo non è lineare perché presenta le variabili decisionali al denominatore.

### 2. Forma Linearizzata (Corretta per la PL)
Moltiplicando entrambi i membri per il denominatore ($\sum_{c \in C} x_{cm} > 0$):
$$
\sum_{c \in C} q_c x_{cm} \ge Q_m^{min} \sum_{c \in C} x_{cm}
$$
Raggruppando i termini a sinistra:
$$
\sum_{c \in C} (q_c - Q_m^{min}) x_{cm} \ge 0
$$

> [!WARNING]
> Ricordare sempre di linearizzare i vincoli di qualità prima di presentare il modello. Lasciare frazioni con variabili al denominatore invalida la linearità del modello, che non sarà più un PL.

---

## Schema da Esame (Template)

**Variabili:**
- $x_{cm}$: quantità di ingrediente $c$ impiegata nella miscela $m$.

**Vincoli di Qualità:**
- Requisito di minimo ($Q_m^{min}$):
  $$
  \sum_{c \in C} (q_c - Q_m^{min}) x_{cm} \ge 0 \qquad \forall m \in M
  $$
- Requisito di massimo ($Q_m^{max}$):
  $$
  \sum_{c \in C} (q_c - Q_m^{max}) x_{cm} \le 0 \qquad \forall m \in M
  $$
