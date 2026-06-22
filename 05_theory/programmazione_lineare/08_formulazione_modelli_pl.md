---
materia: ROPR
area: Programmazione Lineare
tipo: teoria
fonte: Ricerca Operativa - Introduzione a PL - 23-24.pdf, lezione 3 completa.pdf, esercitazione1_complete.pdf, Esercitazione 2 PL.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - teoria
  - modellazione
  - turni
---

# Formulazione di Modelli di Programmazione Lineare

La modellazione matematica consiste nel tradurre una situazione decisionale reale in un sistema di relazioni algebriche lineari (variabili, funzione obiettivo, vincoli).

## Checklist per la Modellazione

Prima di scrivere le equazioni, rispondere sistematicamente a queste domande guida:
1. **Variabili decisionali**: Quali sono le decisioni da prendere? Quali quantità fisiche dobbiamo determinare?
2. **Funzione obiettivo**: Qual è l'obiettivo del decisore? Vogliamo massimizzare il rendimento/profitto o minimizzare il costo/tempo?
3. **Vincoli**: Quali limiti fisici, economici o tecnologici condizionano le nostre decisioni?
4. **Parametri, indici e insiemi**: Quali sono i dati fissi del problema e come sono strutturati (es. stabilimenti, clienti, giorni)?
5. **Dominio delle variabili**: Di quale natura sono le variabili? Sono continue (PL) o devono assumere valori interi o binari (PLI)?

---

## Tipologie di Vincoli Comuni

1. **Vincoli di Capacità / Offerta**: Limitano l'uso delle risorse dall'alto (in genere di tipo $\le$). Esempio: ore di lavoro macchina o quantità di materia prima disponibile.
2. **Vincoli di Domanda / Requisito**: Impongono il raggiungimento di un livello minimo di servizio o produzione (in genere di tipo $\ge$). Esempio: fabbisogno nutrizionale minimo in una dieta.
3. **Vincoli di Bilancio / Flusso**: Impongono che la quantità in ingresso sia uguale a quella in uscita. Esempio: conservazione del flusso nei nodi di trasporto.
4. **Vincoli di Qualità (Miscelazione)**: Definiscono requisiti sulla composizione di un prodotto (es. numero di ottani). Sono spesso espressi come medie pesate e vanno linearizzati moltiplicando per il totale.
5. **Vincoli di Copertura (Set Covering / Maximum Coverage)**: Impongono la copertura di aree o clienti tramite variabili binarie (es. installazione di ripetitori).
6. **Vincoli di Dominio (Non negatività / Interezza)**: Specificano i valori ammissibili per le variabili ($x \ge 0$, $x \in \mathbb{Z}$, $x \in \{0,1\}$).

---

## Template da Esame — Formulazione PL / PLI

Per le risposte d'esame, strutturare la formulazione seguendo questo schema:

### 1. Variabili decisionali
Sia $x_j$ ... (specificare l'indice $j$ e l'unità di misura, es. "migliaia di unità").

### 2. Funzione obiettivo
$$
\max / \min Z = \dots
$$

### 3. Vincoli
Raggruppati e commentati:
$$
\sum a_{ij} x_j \le b_i \qquad \forall i \qquad \text{(vincoli di capacità risorsa } i\text{)}
$$

### 4. Dominio
$$
x_j \ge 0 \quad (\text{oppure } x_j \in \{0, 1\}, \text{ ecc.})
$$

### 5. Breve Interpretazione
Il modello massimizza/minimizza [obiettivo] rispettando i vincoli di [risorse/limiti].

---

## Il Caso dello Scheduling dei Turni (Workforce Scheduling)

Un problema classico di PL riguarda la pianificazione ottimale del personale su turni ciclici settimanali.

### Struttura del Problema
Un'azienda opera 7 giorni su 7 con una richiesta minima di personale variabile ogni giorno. Ciascun dipendente lavora per 5 giorni consecutivi e riposa per 2. L'obiettivo è minimizzare il personale totale impiegato.

### Formulazione Matematica Generale (Calendario Ciclico)

Siano $x_j$ le variabili decisionali indicanti il numero di lavoratori che iniziano il loro turno di 5 giorni consecutivi nel giorno $j$ ($j = 1 \dots 7$, dove 1 è lunedì, 2 martedì, ..., 7 domenica).

L'obiettivo è minimizzare il personale totale:
$$
\min Z = \sum_{j=1}^{7} x_j
$$

I vincoli impongono che per ogni giorno $i$ la somma dei dipendenti in servizio sia almeno pari alla richiesta minima $R_i$:
- **Lunedì ($R_1$)**:
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
> All'esame, prestare particolare attenzione ai vincoli: verificare che la sequenza dei giorni coperti sia congrua rispetto alla data di inizio turno (scorrimento ciclico di 5 indici consecutivi su 7).

