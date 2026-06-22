---
type: method-card
topic: programmazione-lineare
status: draft
sources:
  - raw_assets/Programmazione Lineare/Ricerca Operativa - Introduzione a PL - 23-24.pdf
reliability: official
---

# Method Card — Formulare un modello di Programmazione Lineare

## Quando usarla
Quando l’esercizio chiede di formulare un problema decisionale reale come modello di Programmazione Lineare (PL).

## Procedura da esame
1. **Identificazione delle decisioni**: Leggere attentamente il testo dell'esercizio per individuare le attività o le quantità sconosciute da decidere.
2. **Definizione delle variabili decisionali**: Assegnare un simbolo matematico (es. $x_j$) ad ogni decisione, esplicitandone l'unità di misura (es. lotti/settimana, ore/giorno).
3. **Definizione dell'obiettivo**: Comprendere se il problema richiede di massimizzare il profitto o minimizzare il costo/tempo.
4. **Formulazione della funzione obiettivo**: Scrivere una combinazione lineare delle variabili decisionali con i rispettivi coefficienti di costo/profitto unitario.
5. **Individuazione dei vincoli**: Identificare tutti i vincoli operativi, fisici o logici presenti nel problema (disponibilità risorse, fabbisogni minimi, limiti di capacità).
6. **Formulazione dei vincoli funzionali**: Esprimere ogni vincolo come uguaglianza o disuguaglianza lineare.
7. **Definizione del dominio delle variabili**: Aggiungere sempre i vincoli di non negatività ($x_j \ge 0$). Se richiesto esplicitamente, specificare l'interezza (PLI).

## Formule / Modello
Formulazione compatta:

$$
\max Z \text{ o } \min Z = \sum_{j=1}^{n} c_j x_j
$$

soggetta a:

$$
\sum_{j=1}^{n} a_{ij}x_j \le b_i \qquad \forall i=1,\dots,m
$$

$$
x_j \ge 0 \qquad \forall j=1,\dots,n
$$

## Output da esame
- **Variabili decisionali**: definizione chiara
- **Funzione obiettivo**: specificando $\max$ o $\min$
- **Vincoli**: specificando il significato di ciascun vincolo
- **Dominio delle variabili**: $x_j \ge 0$
