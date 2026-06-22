---
type: theory-note
topic: programmazione-lineare
status: draft
sources:
  - raw_assets/Programmazione Lineare/Ricerca Operativa - Introduzione a PL - 23-24.pdf
reliability: official
---

# Assunzioni della Programmazione Lineare

Per formulare e risolvere legittimamente un problema reale tramite la Programmazione Lineare, devono essere soddisfatte quattro assunzioni matematiche fondamentali relative alla struttura del modello.

## Le Quattro Assunzioni Fondamentali

### 1. Proporzionalità
Il contributo di ogni singola variabile decisoria $x_j$ sia alla funzione obiettivo (costo o profitto) sia all'utilizzo di ciascuna risorsa $i$ nei vincoli deve essere strettamente proporzionale al livello dell'attività $x_j$.
- Matematicamente, questo esclude termini non lineari (come $x_j^2$, $\sqrt{x_j}$) e costi fissi associati all'avvio dell'attività.

### 2. Additività
Il contributo complessivo di tutte le attività alla funzione obiettivo e all'utilizzo delle risorse nei vincoli deve essere pari alla somma dei contributi individuali di ciascuna attività.
- Matematicamente, questo garantisce l'assenza di termini di interazione o cross-prodotto tra le variabili (come $x_1 x_2$). Le attività si dicono indipendenti e additive.

### 3. Continuità / Divisibilità
Le variabili decisionali possono assumere qualsiasi valore reale non negativo, inclusi i valori frazionari.
- Se il problema reale richiede che alcune o tutte le variabili assumano esclusivamente valori interi (es. numero di veicoli, lotti indivisibili), non si può applicare la PL standard ma si deve ricorrere alla **Programmazione Lineare Intera (PLI)**.

### 4. Certezza
Tutti i parametri del modello ($c_j$, $a_{ij}$, $b_i$) sono assunti come valori deterministici noti a priori con assoluta certezza e costanti durante l'intero orizzonte di pianificazione.
- Se vi è incertezza, occorre ricorrere all'ottimizzazione stocastica o all'analisi di sensitività post-ottimo.

## Errori Tipici nella Modellazione

- **Ignorare i costi fissi**: Applicare la PL trascurando la presenza di un costo fisso iniziale per attivare una linea produttiva (che viola l'assunzione di proporzionalità).
- **Trascurare l'interezza**: Ritenere che arrotondare all'intero più vicino la soluzione ottima di un modello continuo di PL sia sempre ottimale o ammissibile.
- **Cross-product nei vincoli**: Inserire relazioni in cui l'efficacia di un'attività dipende dal livello di un'altra (violando l'additività).
- **Coefficienti instabili**: Modellare parametri instabili o variabili senza effettuare analisi di sensitività.

#ropr #programmazione-lineare #teoria #assunzioni
