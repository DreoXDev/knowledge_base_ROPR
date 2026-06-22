---
type: method-card
topic: programmazione-lineare
status: draft
sources:
  - raw_assets/Programmazione Lineare/lezione 3 completa.pdf
reliability: official
---

# Method Card — Risoluzione con il Metodo delle Due Fasi

## Quando Usarlo
Quando il modello di PL standard presenta vincoli di tipo $\ge$ o $=$ che impediscono l'individuazione di una base ammissibile di partenza immediata tramite le sole variabili di slack.

## Procedura Operativa

### Fase 1: Ricerca della Base Ammissibile

1. **Standardizzazione dei vincoli**:
   - Aggiungere slack ($s_i \ge 0$) per i vincoli $\le$.
   - Sottrarre surplus ($e_i \ge 0$) ed aggiungere una variabile artificiale ($x_{ai} \ge 0$) per i vincoli $\ge$.
   - Aggiungere una variabile artificiale ($x_{ai} \ge 0$) per i vincoli $=$.
2. **Definizione della funzione obiettivo di Fase 1**:
   Minimizzare la somma delle variabili artificiali introdotte:
   $$
   \min W = \sum x_{ai} \implies \max -W = -\sum x_{ai}
   $$
3. **Costruzione del Tableau di Fase 1**:
   La base iniziale è formata dalle variabili di slack e dalle variabili artificiali.
4. **Annullamento dei coefficienti artificiali nella riga 0**:
   Prima di fare pivot, azzerare i coefficienti delle variabili artificiali nella riga obiettivo ausiliaria sommando alla riga 0 le righe dei vincoli in cui compaiono le artificiali.
5. **Risoluzione con il Simplesso**: Eseguire i pivot finché non si raggiunge l'ottimalità per la Fase 1.
6. **Verifica della Condizione di Ammissibilità**:
   - Se il valore ottimo della Fase 1 è $-W^* = 0$, il problema originale è ammissibile. Procedere alla Fase 2.
   - Se $-W^* < 0$ (ovvero $W^* > 0$), almeno una variabile artificiale è strettamente positiva in base. Il problema originale è **inammissibile** (regione vuota). Stop.

### Fase 2: Ottimizzazione del Problema Originale

1. **Eliminazione delle artificiali**: Cancellare completamente le colonne relative alle variabili artificiali dal tableau ottimo di Fase 1.
2. **Ripristino dell'obiettivo**: Sostituire la riga 0 con la funzione obiettivo originale trasformata in forma di massimizzazione:
   $$
   Z - \sum c_j x_j = 0
   $$
3. **Azzeramento dei costi delle variabili in base**: Se nel tableau ripristinato le variabili di base hanno coefficienti diversi da zero nella riga 0, eliminare tali coefficienti eseguendo operazioni di riga (somma/sottrazione dei vincoli moltiplicati per costanti opportune).
4. **Simplesso finale**: Risolvere il tableau risultante con l'algoritmo del simplesso classico.

## Formato di Risposta da Esame

- **In Fase 1**: Dichiarare esplicitamente la funzione obiettivo ausiliaria e l'operazione preliminare di azzeramento dei costi artificiali.
- **Transizione**: Indicare esplicitamente il valore finale di $W$. Dichiarare: *"Poiché $W^* = 0$, il problema è ammissibile, elimino le artificiali e procedo alla Fase 2"*.
- **In Fase 2**: Mostrare il tableau dopo il ripristino dell'obiettivo originario e dopo il necessario azzeramento dei coefficienti delle variabili in base.
