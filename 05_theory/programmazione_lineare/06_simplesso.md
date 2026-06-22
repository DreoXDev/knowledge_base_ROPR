---
materia: ROPR
area: Programmazione Lineare
tipo: teoria
fonte: Ricerca Operativa - Metodo del Simplesso - 23-24.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - simplesso
  - george-dantzig
---

# Metodo del simplesso

## Introduzione Storica e Scopo
Il **metodo del simplesso** è un algoritmo ideato dal matematico George Dantzig nel 1947. Rappresenta la procedura algebrica generale e fondamentale per la risoluzione dei problemi di Programmazione Lineare (PL).

## Idea Centrale
L'algoritmo opera secondo una logica geometrica ed iterativa:
- Non ispeziona tutti i punti infiniti della regione ammissibile, né calcola tutti i suoi vertici in anticipo.
- Si muove esclusivamente lungo la frontiera della regione ammissibile, passando da una soluzione vertice ammissibile ad una adiacente che migliori (o mantenga invariato) il valore della funzione obiettivo.
- Termina quando si raggiunge un vertice dal quale nessun vertice adiacente offre un valore migliore della funzione obiettivo.

## Test di Ottimalità
Una soluzione vertice ammissibile è ottima se nessuna soluzione vertice adiacente ha un valore della funzione obiettivo migliore.

## Complessità ed Efficienza
- **Caso medio**: Estremamente efficiente nella pratica, risolvendo problemi reali in un numero di iterazioni lineare o quadratico rispetto al numero di vincoli.
- **Caso peggiore**: Ha una complessità computazionale di tipo esponenziale (es. esempio di Klee-Minty), ma nella pratica comune rimane uno degli strumenti più robusti e utilizzati.

## Schema Operativo Generale
1. **Standardizzazione**: Portare il problema in forma aumentata introducendo variabili di slack.
2. **Inizializzazione**: Determinare una soluzione di base ammissibile iniziale.
3. **Test di Ottimalità**: Calcolare i coefficienti ridotti (costi ridotti) nella riga 0.
4. **Iterazione (se non ottimo)**:
   - Selezionare la variabile entrante (massimo miglioramento unitario).
   - Selezionare la variabile uscente (test del rapporto minimo).
   - Effettuare l'operazione di pivot (eliminazione gaussiana).
   - Ripetere dal punto 3.
