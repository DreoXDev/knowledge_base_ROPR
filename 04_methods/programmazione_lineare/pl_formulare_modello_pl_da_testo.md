---
materia: ROPR
area: Programmazione Lineare
tipo: metodo
fonte: Ricerca Operativa - Introduzione a PL - 23-24.pdf, lezione 3 completa.pdf, esercitazione1_complete.pdf, Esercitazione 2 PL.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - formulazione
  - metodo
  - method-card
---

# METHOD CARD — Formulare un Modello PL da Testo

## Quando usarla

Usare questa card quando la traccia d'esame descrive uno scenario applicativo reale (produzione, dieta, trasporto, miscelazione, ecc.) e richiede di formularne il modello di ottimizzazione lineare (PL o PLI).

## Procedura Operativa Passo-Passo

1. **Capire l'obiettivo e cosa si decide**: Identificare chiaramente lo scopo (minimizzare o massimizzare) e le leve decisionali.
2. **Definire le variabili decisionali**: Assegnare a ciascuna decisione una variabile, specificando indici e **unità di misura** (es. "Sia $x_c$ = migliaia di chiavi inglesi prodotte").
3. **Scrivere la funzione obiettivo**: Esprimere la funzione lineare da ottimizzare usando i coefficienti di costo/ricavo unitari.
4. **Scrivere i vincoli**:
   - Dividere i vincoli per categoria (capacità, domanda, qualità, bilancio, ecc.).
   - Assicurarsi di commentare brevemente ciascuna riga o gruppo di vincoli per spiegare il loro significato reale.
5. **Specificare il dominio delle variabili**: Indicare se le variabili sono continue non negative ($x_i \ge 0$), intere ($x_i \in \mathbb{Z}$), o binarie ($x_i \in \{0, 1\}$).
6. **Controllo di coerenza**: Verificare la congruenza delle unità di misura in ciascun vincolo (es. se la disponibilità è in tonnellate, tutti i termini del vincolo devono essere espressi in tonnellate).

---

## Errori Comuni da Evitare

- **Confondere parametri e variabili**: I parametri sono costanti note fornite dal testo, le variabili sono le quantità incognite da determinare.
- **Dimenticare la non negatività**: Tutte le variabili decisionali fisiche devono essere vincolate a essere $\ge 0$.
- **Incoerenza delle unità di misura**: Sommare grandezze espresse in unità diverse (es. ore con minuti, kg con tonnellate).
- **Mancata linearizzazione nei problemi di miscelazione**: Lasciare frazioni con variabili al denominatore nei vincoli di qualità media.
- **Doppio conteggio nei problemi di maximum coverage**: Non utilizzare variabili di copertura $y_j$ binarie ausiliarie.
- **Omettere il vincolo di interezza o binarietà** nei modelli PLI.

---

## Mini-Template da Esame

```markdown
### 1. Variabili decisionali
Sia $x_j$ ... [unità di misura] per $j \in \{1, \dots, n\}$.

### 2. Funzione Obiettivo
$$
\max / \min Z = \sum_{j=1}^n c_j x_j
$$

### 3. Vincoli
- Vincoli di risorsa:
  $$
  \sum_{j=1}^n a_{ij} x_j \le b_i \qquad \forall i \in I
  $$
- Vincoli di mercato/requisiti:
  $$
  \dots
  $$

### 4. Dominio
$$
x_j \ge 0 \qquad \forall j = 1, \dots, n
$$
```
