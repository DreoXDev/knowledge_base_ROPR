---
type: theory-note
topic: programmazione-lineare
status: draft
sources:
  - raw_assets/Programmazione Lineare/lezione 3 completa.pdf
reliability: official
---

# Formulazione di Modelli di PL e Turni di Lavoro

La modellazione matematica consiste nel tradurre una situazione decisionale reale in un sistema di relazioni algebriche lineari.

## Checklist per la Modellazione

Prima di scrivere le equazioni, rispondere sistematicamente a queste domande guida:

1. **Variabili decisionali**: Quali sono le decisioni da prendere? Quali quantità fisiche dobbiamo determinare?
2. **Funzione obiettivo**: Qual è l'obiettivo del decisore? Vogliamo massimizzare il rendimento/profitto o minimizzare il costo/tempo?
3. **Vincoli**: Quali limiti fisici, economici o tecnologici condizionano le nostre decisioni?
4. **Dominio delle variabili**: Di quale natura sono le variabili? Sono continue (PL) o devono assumere valori interi/binari (PLI)?

## Il Caso dello Scheduling dei Turni (Workforce Scheduling)

Un problema classico di PL riguarda la pianificazione ottimale del personale su turni ciclici settimanali. 

### Struttura del Problema
Un ristorante o un'azienda di servizi opera 7 giorni su 7 con una richiesta minima di personale variabile ogni giorno. Ciascun dipendente lavora per 5 giorni consecutivi e riposa per 2. L'obiettivo è minimizzare il personale totale impiegato.

### Formulazione Matematica Generale (Calendario Ciclico)

Siano $x_j$ le variabili decisionali indicanti il numero di lavoratori che iniziano il loro turno di 5 giorni consecutivi nel giorno $j$ ($j = 1 \dots 7$, dove 1 è lunedì, 2 martedì, ..., 7 domenica).

L'obiettivo è minimizzare il personale totale:

$$
\min Z = \sum_{j=1}^{7} x_j
$$

I vincoli impongono che per ogni giorno $i$ la somma dei dipendenti in servizio sia almeno pari alla richiesta minima $R_i$:

- **Lunedì ($R_1$)**: I dipendenti attivi sono quelli che hanno iniziato lunedì ($x_1$), giovedì ($x_4$), venerdì ($x_5$), sabato ($x_6$), domenica ($x_7$).
  $$
  x_1 + x_4 + x_5 + x_6 + x_7 \ge R_1
  $$
- **Martedì ($R_2$)**:
  $$
  x_1 + x_2 + x_5 + x_6 + x_7 \ge R_2
  $$
- **Mercoledì ($R_3$)**:
  $$
  x_1 + x_2 + x_3 + x_6 + x_7 \ge R_3
  $$
- **Giovedì ($R_4$)**:
  $$
  x_1 + x_2 + x_3 + x_4 + x_7 \ge R_4
  $$
- **Venerdì ($R_5$)**:
  $$
  x_1 + x_2 + x_3 + x_4 + x_5 \ge R_5
  $$
- **Sabato ($R_6$)**:
  $$
  x_2 + x_3 + x_4 + x_5 + x_6 \ge R_6
  $$
- **Domenica ($R_7$)**:
  $$
  x_3 + x_4 + x_5 + x_6 + x_7 \ge R_7
  $$

Dominio:

$$
x_j \ge 0 \qquad j = 1 \dots 7
$$

> [!NOTE]
> All'esame, prestare particolare attenzione ai refusi sui vincoli: verificare che la sequenza dei giorni coperti sia congrua rispetto alla data di inizio turno (scorrimento ciclico di 5 indici consecutivi su 7).

#ropr #programmazione-lineare #teoria #modellazione #turni
