---
type: method-card
topic: programmazione_lineare
status: consolidated
sources:
  - raw_assets/AAA - La bibbia di RO.pdf
reliability: non-ufficiale
---

# Method Card: Casi Particolari del Simplesso

## Quando Usarla

Quando la traccia presenta un tableau del simplesso (finale o intermedio) e chiede di identificare il caso particolare presente o di spiegare cosa accade.

---

## Degenerazione

**Definizione**: Una variabile di **base** ha valore $\bar{x}_B = 0$.

**Come riconoscerla**: Nel tableau, una variabile con colonna identità ha RHS = 0.

**Conseguenza**: Il simplesso potrebbe fare pivot senza migliorare $Z$ (rischio di cycling).

**Risposta da esame**:
```
La variabile x_k è in base con x_k = 0.
La soluzione di base è degenere. Possibile cycling senza antiblocking.
```

---

## Ottimi Multipli

**Definizione**: Esistono più vertici (o un intero spigolo) con lo stesso valore ottimo $Z^*$.

**Come riconoscerli**: Nel tableau **ottimo**, una variabile **fuori base** ha costo ridotto $\bar{c}_j = 0$.

**Conseguenza**: Si può eseguire un pivot su $x_j$ e raggiungere un altro vertice ottimo senza peggiorare $Z$.

**Risposta da esame**:
```
Il tableau è ottimo. La variabile x_j (fuori base) ha costo ridotto nullo.
=> Esistono ottimi multipli. Il pivot su x_j porta a un altro vertice ottimo.
```

---

## Problema Illimitato

**Definizione**: La funzione obiettivo può crescere (massimizzazione) o decrescere (minimizzazione) senza limite.

**Come riconoscerlo**: Esiste una variabile candidata entrante (costo ridotto nel verso corretto), ma la sua colonna nel tableau non ha **nessun coefficiente positivo** (per max) → nessun rapporto minimo valido.

**Risposta da esame**:
```
La variabile x_j ha costo ridotto [negativo per min / positivo per max]:
candidata entrante.
La colonna di x_j ha tutti i coefficienti [<= 0 / >= 0]:
il rapporto minimo non è definito.
=> Il problema è ILLIMITATO (Z* -> [+inf / -inf]).
```

---

## Problema Non Ammissibile

**Definizione**: La regione ammissibile è vuota.

**Come riconoscerlo**: Alla fine della Fase 1 del metodo delle due fasi, il valore ottimo della funzione ausiliaria $W^* > 0$ (almeno una variabile artificiale è rimasta in base con valore positivo).

**Risposta da esame**:
```
Al termine della Fase 1: W* = [...] > 0.
Variabile artificiale a_i in base con valore positivo.
=> La regione ammissibile è VUOTA. Il problema originale è NON AMMISSIBILE.
```

---

## Come Riconoscerli da Tableau — Tabella Riassuntiva

| Caso | Dove guardare | Segnale |
|---|---|---|
| Degenerazione | RHS variabili di base | Almeno un RHS = 0 |
| Ottimi multipli | Riga obiettivo (tableau ottimo) | $\bar{c}_j = 0$ per var. fuori base |
| Illimitatezza | Colonna variabile entrante | Tutti i coefficienti $\le 0$ (per max) |
| Non ammissibilità | Fine Fase 1 | $W^* > 0$ |

---

## Collegamento Pattern

→ [[Quiz_simplesso_casi_particolari]]
