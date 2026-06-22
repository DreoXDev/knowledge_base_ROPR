---
materia: ROPR
area: Programmazione Lineare
tipo: esempio-svolto
fonte: Esercitazione 2 PL.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - formulazione
  - miscelazione
  - qualita
  - esempio-svolto
---

# Esempio Svolto — Miscelazione di Benzine (Quality Blending)

Questo esempio illustra come formulare e linearizzare i vincoli di qualità in un tipico problema di miscelazione (blending) industriale.

## Testo del Problema

Una raffineria deve produrre due tipi di benzina: *Regular* e *Premium*. Per farlo, miscela tre diversi tipi di costituenti (stock di grezzo) disponibili, ciascuno con specifiche caratteristiche di pressione del vapore, numero di ottani e disponibilità limitata:

| Costituente ($c$) | Pressione Vapore ($p_c$) | Numero Ottani ($o_c$) | Disponibilità ($d_c$) |
|---|---|---|---|
| Stock 1 | $5$ | $80$ | $4.000$ barili |
| Stock 2 | $7$ | $90$ | $5.000$ barili |
| Stock 3 | $9$ | $100$ | $3.000$ barili |

I requisiti di qualità delle benzine prodotte e i rispettivi prezzi di vendita al barile sono:

| Miscela ($m$) | Pressione Massima ($rp_m$) | Ottani Minimi ($ro_m$) | Prezzo Vendita ($r_m$) |
|---|---|---|---|
| **Regular** | $\le 7$ | $\ge 88$ | € $70$ / barile |
| **Premium** | $\le 6$ | $\ge 93$ | € $85$ / barile |

Gli stock non miscelati possono essere venduti a distributori indipendenti a un prezzo fisso di € 45/barile. Si vuole massimizzare il ricavo totale della raffineria.

---

## Formulazione Matematica

### 1. Insiemi e Indici
- $C = \{1, 2, 3\}$: insieme dei costituenti disponibili ($c \in C$).
- $M = \{R, P\}$: insieme delle miscele finali ($m \in M$).

### 2. Parametri
- $d_c$: disponibilità dello stock $c$ (barili).
- $p_c, o_c$: caratteristiche di pressione e ottani dello stock $c$.
- $rp_m, ro_m$: requisiti qualitativi per la miscela $m$.
- $r_m$: prezzo di vendita al barile della miscela $m$.
- $r_{ind} = 45$: prezzo di vendita al barile degli stock non miscelati.

### 3. Variabili decisionali
- $x_{cm}$: quantità (in barili) di costituente $c$ impiegata nella miscela $m$ ($\forall c \in C, m \in M$).
- $w_c$: quantità (in barili) di costituente $c$ non miscelata e venduta direttamente agli indipendenti ($\forall c \in C$).

### 4. Funzione obiettivo
Massimizzare i ricavi totali ottenuti dalla vendita di Regular, Premium e grezzo residuo:
$$
\max Z = \sum_{c \in C} 70 x_{cR} + \sum_{c \in C} 85 x_{cP} + \sum_{c \in C} 45 w_c
$$

### 5. Vincoli

- **Vincolo di disponibilità fisica** (non possiamo consumare più grezzo di quello in stock):
  $$
  x_{cR} + x_{cP} + w_c = d_c \qquad \forall c \in C
  $$

- **Vincoli di qualità sulla pressione del vapore** (media pesata della pressione dei costituenti $\le$ soglia massima):
  Per Regular ($R$):
  $$
  \frac{\sum_{c \in C} p_c x_{cR}}{\sum_{c \in C} x_{cR}} \le 7 \implies \sum_{c \in C} p_c x_{cR} \le 7 \sum_{c \in C} x_{cR} \implies \sum_{c \in C} (p_c - 7) x_{cR} \le 0
  $$
  Per Premium ($P$):
  $$
  \frac{\sum_{c \in C} p_c x_{cP}}{\sum_{c \in C} x_{cP}} \le 6 \implies \sum_{c \in C} (p_c - 6) x_{cP} \le 0
  $$

- **Vincoli di qualità sul numero di ottani** (media pesata degli ottani $\ge$ soglia minima):
  Per Regular ($R$):
  $$
  \frac{\sum_{c \in C} o_c x_{cR}}{\sum_{c \in C} x_{cR}} \ge 88 \implies \sum_{c \in C} (o_c - 88) x_{cR} \ge 0
  $$
  Per Premium ($P$):
  $$
  \frac{\sum_{c \in C} o_c x_{cP}}{\sum_{c \in C} x_{cP}} \ge 93 \implies \sum_{c \in C} (o_c - 93) x_{cP} \ge 0
  $$

### 6. Dominio
Tutte le quantità devono essere non negative:
$$
x_{cm} \ge 0, \quad w_c \ge 0 \qquad \forall c \in C, m \in M
$$

---

## Nota Fondamentale di Linearizzazione

> [!WARNING]
> I vincoli di qualità espressi originariamente come medie pesate presentano variabili sia al numeratore che al denominatore (es. $\frac{\sum p_c x_{cm}}{\sum x_{cm}} \le rp_m$). Questo rende il vincolo non lineare.
> 
> Per preservare la linearità (requisito essenziale per la PL), si deve **moltiplicare entrambi i membri per il denominatore** (la quantità totale di miscela prodotta), ottenendo relazioni lineari del tipo:
> $$
> \sum_{c \in C} (p_c - rp_m) x_{cm} \le 0
> $$
