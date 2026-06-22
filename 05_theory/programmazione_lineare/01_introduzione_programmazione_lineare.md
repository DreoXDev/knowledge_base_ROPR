---
type: theory-note
topic: programmazione-lineare
status: draft
sources:
  - raw_assets/Programmazione Lineare/Ricerca Operativa - Introduzione a PL - 23-24.pdf
reliability: official
---

# Introduzione alla Programmazione Lineare

La **Programmazione Lineare (PL)** è un metodo matematico per determinare la migliore allocazione di risorse limitate al fine di raggiungere un obiettivo prefissato (massimizzazione del profitto o minimizzazione del costo). Tutti i modelli di programmazione lineare sono caratterizzati da relazioni lineari tra le variabili.

## Elementi di un modello di PL

Un modello di Programmazione Lineare è composto dai seguenti elementi fondamentali:

- **Variabili Decisionali**: Rappresentano le decisioni che devono essere prese (es. quantità di lotti da produrre). Sono tipicamente indicate con $x_1, x_2, \dots, x_n$.
- **Funzione Obiettivo**: La misura di performance (da massimizzare o minimizzare) espressa come funzione lineare delle variabili decisionali (es. profitto totale $Z$).
- **Vincoli Funzionali**: Limitazioni fisiche o operative espresse come disuguaglianze lineari (o uguaglianze) che restringono i valori possibili delle variabili (es. disponibilità di ore macchina).
- **Vincoli di Non Negatività**: Impongono che le variabili decisionali non assumano valori negativi ($x_j \ge 0$), riflettendo situazioni reali in cui quantità negative non hanno significato fisico.
- **Parametri**: I coefficienti costanti presenti nella funzione obiettivo e nei vincoli (es. profitti unitari, consumi di risorse).

## Esempio Introduttivo

Un classico esempio di formulazione e risoluzione di un problema di PL è il caso [[wyndor_glass|Wyndor Glass Co.]], in cui si decide il mix produttivo ottimale per due nuovi prodotti utilizzando la capacità limitata di tre impianti.

#ropr #programmazione-lineare #teoria #formulazione
