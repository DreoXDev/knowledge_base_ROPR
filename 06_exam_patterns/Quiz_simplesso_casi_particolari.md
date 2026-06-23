---
type: exam-pattern
topic: programmazione_lineare
status: consolidated
sources:
  - raw_assets/AAA - La bibbia di RO.pdf
reliability: non-ufficiale
---

# Quiz PL — Casi Particolari del Simplesso

## Riconoscimento

Segnali nella traccia:
- "tableau finale"
- "ultima iterazione"
- "ottimo multiplo" / "ottimi alternativi"
- "problema illimitato"
- "problema non ammissibile"
- "degenerazione"

---

## Checklist da Tableau Finale

```
[ ] La riga obiettivo soddisfa il criterio di ottimalità?
    → Massimo: tutti i costi ridotti <= 0
    → Minimo:  tutti i costi ridotti >= 0
[ ] Esiste una variabile fuori base con costo ridotto NULLO?
    → Sì: OTTIMI MULTIPLI (pivot alternativo disponibile)
[ ] Esiste una variabile di base con valore RHS = 0?
    → Sì: DEGENERAZIONE
[ ] La colonna della variabile entrante ha tutti gli elementi <= 0?
    → Sì: PROBLEMA ILLIMITATO
[ ] I termini noti (RHS) sono tutti >= 0?
    → No: base non ammissibile (caso raro al tableau finale)
```

---

## Casi Particolari — Identificazione e Risposta

### Ottimo Multiplo
**Segnale**: Nel tableau ottimo, esiste almeno una variabile **fuori base** con costo ridotto $\bar{c}_j = 0$.

**Risposta da esame**:
```
Il tableau è ottimo (tutti i costi ridotti [<=/>= 0]).
La variabile x_j fuori base ha costo ridotto nullo.
=> Esistono ottimi multipli. Si può fare pivot su x_j per ottenere
   un altro vertice ottimo con lo stesso valore Z*.
```

### Degenerazione
**Segnale**: Nel tableau corrente, una variabile di base ha valore RHS = 0.

**Risposta da esame**:
```
La variabile x_k è in base con valore x_k = 0.
=> Soluzione di base degenere. Potrebbero verificarsi iterazioni
   del simplesso senza miglioramento della funzione obiettivo (cycling).
```

### Problema Illimitato
**Segnale**: Esiste una variabile entrante (costo ridotto nel verso giusto) ma la sua colonna nel tableau non ha **nessun elemento positivo** (per problemi di massimo) o negativo (per minimo).

**Risposta da esame**:
```
La variabile x_j è candidata entrante (costo ridotto [< 0 per min / > 0 per max]).
Tutti i coefficienti nella colonna di x_j sono [<= 0 / >= 0]:
nessun rapporto minimo valido => il problema è ILLIMITATO (Z* -> +inf / -inf).
```

### Non Ammissibilità
**Segnale**: Alla fine della Fase 1, la funzione ausiliaria $W^* > 0$ (variabili artificiali non azzerate).

**Risposta da esame**:
```
Al termine della Fase 1, W* = [...] > 0.
=> Esistono variabili artificiali in base con valore > 0.
=> La regione ammissibile è VUOTA: il problema è non ammissibile.
```

---

## Errori Frequenti

- ❌ Dichiarare ottimo multiplo senza verificare che il tableau sia già ottimo.
- ❌ Confondere degenerazione (variabile base = 0) con non ammissibilità.
- ❌ Dire "illimitato" senza verificare il segno del costo ridotto della variabile entrante.
- ❌ Leggere male la base (una variabile con colonna non identità).

---

## Collegamento Method Card

→ [[MC_PL_simplesso_casi_particolari]]
