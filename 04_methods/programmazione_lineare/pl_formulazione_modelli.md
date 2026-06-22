---
type: method-card
topic: programmazione-lineare
status: draft
sources:
  - raw_assets/Programmazione Lineare/lezione 3 completa.pdf
reliability: official
---

# Method Card — Formulare un Modello di PL da Testo

## Domande Guida per la Modellazione
1. **Qual è l'obiettivo?** (Massimizzare il profitto? Minimizzare il costo? Ridurre gli sprechi?)
2. **Quali sono le decisioni da prendere?** (Quanti lotti produrre? Quanti dipendenti allocare per ogni turno?)
3. **Quali sono i vincoli fisici o tecnologici?** (Capacità degli impianti, fabbisogno giornaliero, disponibilità delle materie prime?)
4. **Quali sono i limiti fisici delle variabili?** (Possono assumere valori negativi? Devono essere intere o continue?)

## Struttura Standard di un Modello
Un modello si presenta formalmente all'esame in questo ordine:

1. **Variabili decisionali**:
   - $x_1 = \text{quantità del prodotto 1... [unità di misura]}$
   - $x_2 = \text{quantità del prodotto 2... [unità di misura]}$
2. **Funzione Obiettivo**:
   - $\max Z = c_1 x_1 + c_2 x_2$ oppure $\min Z = c_1 x_1 + c_2 x_2$
3. **Vincoli funzionali**:
   - specificare il significato a parole accanto ad ogni equazione/disequazione (es. *capacità impianto A*, *richiesta minima giorno $t$*).
4. **Vincoli di dominio**:
   - $x_1, x_2 \ge 0$

## Esempio d'Esame: Turni di Lavoro (Workforce Scheduling)

### Traccia sintetica
Un'azienda ha fabbisogni variabili di personale nei 7 giorni della settimana ($R_1 \dots R_7$). Ogni lavoratore lavora per 5 giorni consecutivi e riposa per 2. Formuliamo il modello che minimizza il personale totale.

### Risoluzione Tipo da Esame

**Variabili decisionali:**
Sia $x_j$ il numero di dipendenti il cui turno di 5 giorni consecutivi inizia il giorno $j$ (con $j = 1 \dots 7$, dove $1 = \text{Lunedì}$, $2 = \text{Martedì}$, ecc.).

**Funzione Obiettivo:**

$$
\min Z = \sum_{j=1}^{7} x_j
$$

**Vincoli:**
- Copertura Lunedì: $x_1 + x_4 + x_5 + x_6 + x_7 \ge R_1$
- Copertura Martedì: $x_1 + x_2 + x_5 + x_6 + x_7 \ge R_2$
- Copertura Mercoledì: $x_1 + x_2 + x_3 + x_6 + x_7 \ge R_3$
- Copertura Giovedì: $x_1 + x_2 + x_3 + x_4 + x_7 \ge R_4$
- Copertura Venerdì: $x_1 + x_2 + x_3 + x_4 + x_5 \ge R_5$
- Copertura Sabato: $x_2 + x_3 + x_4 + x_5 + x_6 \ge R_6$
- Copertura Domenica: $x_3 + x_4 + x_5 + x_6 + x_7 \ge R_7$

**Dominio:**

$$
x_j \ge 0 \quad \text{e intere} \qquad \forall j = 1 \dots 7
$$
