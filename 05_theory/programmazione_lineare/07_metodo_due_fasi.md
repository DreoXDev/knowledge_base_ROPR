---
type: theory-note
topic: programmazione-lineare
status: draft
sources:
  - raw_assets/Programmazione Lineare/lezione 3 completa.pdf
reliability: official
---

# Il Metodo delle Due Fasi

Il metodo delle due fasi viene impiegato per risolvere problemi di Programmazione Lineare quando la forma aumentata non fornisce una base iniziale ammissibile immediata (es. in presenza di vincoli di tipo $\ge$ o $=$).

## Tipi di Variabili Aggiuntive

Nel processo di standardizzazione dei vincoli introduciamo:
- **Slack ($s_i$)**: Aggiunta nei vincoli $\le$ per assorbire la risorsa non utilizzata. Può far parte della base iniziale.
- **Surplus ($e_i$)**: Sottratta nei vincoli $\ge$ per rappresentare l'eccesso rispetto al limite minimo. Non può essere usata nella base iniziale poiché il suo coefficiente è $-1$, che violerebbe la non negatività della base (avendo RHS positivo).
- **Artificiali ($x_a$)**: Variabili fittizie introdotte nei vincoli $\ge$ e $=$ al solo scopo di fornire una variabile di base di partenza ammissibile ($+1$). Devono essere annullate nel risultato finale per garantire l'ammissibilità del problema originario.

## Fase 1 (Minimizzazione delle Artificiali)

L'obiettivo della Fase 1 è trovare una soluzione di base ammissibile per il problema originario eliminando le variabili artificiali.

Si formula un problema ausiliario in cui:
- La funzione obiettivo è la minimizzazione della somma delle variabili artificiali:
  $$
  \min W = \sum x_{ai} \implies \max -W = -\sum x_{ai}
  $$
- I vincoli sono quelli del problema originario (con slack, surplus e artificiali).

Prima di avviare il simplesso, è fondamentale annullare i coefficienti delle variabili artificiali nella riga obiettivo (riga 0) effettuando opportune operazioni di riga con i vincoli in cui compaiono.

### Interpretazione dell'Ottimo di Fase 1

Risolto il problema ausiliario di Fase 1, si esamina il valore ottimo $W^*$:
1. **$W^* = 0$**: Le variabili artificiali sono tutte nulle. Abbiamo trovato una soluzione di base ammissibile per il problema originale. Si può procedere alla Fase 2.
2. **$W^* > 0$**: Non è possibile annullare le variabili artificiali. Il problema originale è **inammissibile** (regione ammissibile vuota). La procedura si arresta.

## Fase 2 (Risoluzione del Problema Originale)

Se la Fase 1 si chiude con $W^* = 0$:
1. **Rimozione**: Rimuovere le colonne delle variabili artificiali dal tableau ottimo di Fase 1.
2. **Ripristino**: Ripristinare la funzione obiettivo originaria nella riga 0.
3. **Annullamento dei costi**: Poiché le variabili attualmente in base potrebbero avere coefficienti non nulli nella riga obiettivo ripristinata, è necessario effettuare operazioni di riga per azzerare tali coefficienti prima di eseguire qualsiasi pivot.
4. **Risoluzione**: Eseguire il simplesso classico fino a raggiungere l'ottimo.

## Casi Speciali
- Se durante la Fase 2 si incontra la condizione di illimitatezza (variabile entrante con tutti coefficienti $\le 0$ nei vincoli), il problema originario è **illimitato**.

#ropr #programmazione-lineare #teoria #due-fasi
