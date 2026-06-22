---
type: theory-note
topic: programmazione-lineare
status: draft
sources:
  - raw_assets/Programmazione Lineare/Ricerca Operativa - Introduzione a PL - 23-24.pdf
reliability: official
---

# Soluzione Grafica di un Problema di PL

La risoluzione grafica è una metodologia intuitiva usata per risolvere problemi di Programmazione Lineare nel piano cartesiano.

## Quando si usa

Questo metodo è applicabile in modo diretto esclusivamente quando il modello contiene al massimo **due variabili decisionali** ($x_1, x_2$), consentendone la rappresentazione grafica bidimensionale.

## Passaggi Operativi

1. **Formulazione**: Definire il modello matematico completo (funzione obiettivo, vincoli e domini).
2. **Costruzione delle rette associate**: Per ogni vincolo di disuguaglianza (es. $a_{i1}x_1 + a_{i2}x_2 \le b_i$), individuare la retta associata ponendo l'uguaglianza ($a_{i1}x_1 + a_{i2}x_2 = b_i$).
3. **Identificazione dei semipiani**: Determinare quale semipiano soddisfa la disuguaglianza. A questo scopo si può usare un *punto di prova* (tipicamente l'origine $(0,0)$, se non appartiene alla retta). Se il punto soddisfa la disuguaglianza, il semipiano ammissibile è quello contenente il punto; altrimenti è quello opposto.
4. **Regione ammissibile**: Intersecare tutti i semipiani definiti dai vincoli funzionali e dai vincoli di non negatività ($x_1 \ge 0, x_2 \ge 0$). L'intersezione costituisce lo spazio delle soluzioni ammissibili.
5. **Rette di livello**: Disegnare la retta associata alla funzione obiettivo per un valore arbitrario di $Z$ (es. $c_1x_1 + c_2x_2 = K$). Questa rappresenta una *linea di livello*.
6. **Ottimizzazione**: Spostare parallelamente la linea di livello nella direzione di crescita del profitto (per problemi di massimizzazione) o di decrescita del costo (per problemi di minimizzazione).
7. **Ottimo grafico**: Trovare l'ultimo punto (o l'insieme di punti) della regione ammissibile toccato dalla retta di livello durante la traslazione. Tale punto rappresenta la soluzione ottima.

## Concetti Chiave

- **Retta associata**: La frontiera lineare definita dal vincolo.
- **Semipiano**: La regione di spazio delimitata dalla retta associata in cui il vincolo di disuguaglianza è soddisfatto.
- **Rette di livello**: Famiglia di rette parallele della forma $c_1x_1 + c_2x_2 = Z$. La direzione di miglioramento è data dal vettore dei coefficienti di costo $\nabla Z = (c_1, c_2)^T$.

#ropr #programmazione-lineare #teoria #grafico
