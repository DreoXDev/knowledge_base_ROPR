# Pattern d'Esame: Ottimizzazione Unidimensionale (1D)

## Descrizione del Pattern

Esercizi numerici e quesiti teorici basati sull'ottimizzazione di funzioni a una variabile reale. Tipicamente viene richiesto di determinare analiticamente o numericamente (tramite il metodo di bisezione o il metodo di Newton 1D) i punti di ottimo locale e globale di una funzione concava o convessa.

## Trigger RAG

- "metodo di bisezione"
- "metodo di Newton 1D"
- "algoritmo dicotomico"
- "approssimazione quadratica"
- "punto medio e intervallo di incertezza"
- "tolleranza epsilon"
- "risolvere analiticamente f'(x) = 0"
- "f''(x) <= 0"

## Schema di Risposta Atteso

### Caso 1: Ottimizzazione Analitica (Massimo/Minimo Globale)

1. **Calcolo della Derivata Prima**:
   * Calcolare e scrivere esplicitamente $f'(x)$.
2. **Risoluzione dell'Equazione Stazionaria**:
   * Risolvere $f'(x^*) = 0$ per determinare i punti candidati stazionari.
3. **Studio della Derivata Seconda e Curvatura**:
   * Calcolare $f''(x)$.
   * Verificare la concavità/convessità globale: se $f''(x) \le 0$ per ogni $x$ del dominio, la funzione è **concava** e il punto stazionario è un **massimo globale**. Se $f''(x) \ge 0$, la funzione è **convessa** e il punto è un **minimo globale**.

---

### Caso 2: Ottimizzazione Numerica con Metodo di Bisezione

1. **Verifica Ipotesi**:
   * Verificare che la funzione sia continua e derivabile, ed evidenziare la concavità/convessità.
   * Controllare che agli estremi dell'intervallo iniziale $[\underline{x}_0, \bar{x}_0]$ la derivata prima abbia segno discorde (ad esempio $f'(\underline{x}_0) > 0$ e $f'(\bar{x}_0) < 0$ per un massimo).
2. **Calcolo Iterativo**:
   * Per ciascuna iterazione $k$, calcolare il punto medio $x_{k+1} = \frac{\underline{x}_k + \bar{x}_k}{2}$.
   * Valutare il segno della derivata prima $f'(x_{k+1})$.
   * Aggiornare gli estremi dell'intervallo:
     - Se massimo: se $f'(x_{k+1}) > 0 \implies \underline{x}_{k+1} = x_{k+1}$; se $f'(x_{k+1}) < 0 \implies \bar{x}_{k+1} = x_{k+1}$.
     - Se minimo: se $f'(x_{k+1}) < 0 \implies \underline{x}_{k+1} = x_{k+1}$; se $f'(x_{k+1}) > 0 \implies \bar{x}_{k+1} = x_{k+1}$.
3. **Criterio di Arresto e Conclusione**:
   * Verificare se l'ampiezza dell'intervallo corrente $\bar{x}_k - \underline{x}_k \le 2\epsilon$ (dove $\epsilon$ è la tolleranza).
   * Presentare i calcoli in una tabella riassuntiva che mostra ad ogni riga: $k$, $\underline{x}_k$, $\bar{x}_k$, $x_{k+1}$, $f'(x_{k+1})$, e l'ampiezza $\bar{x}_k - \underline{x}_k$.
   * Concludere dichiarando l'ottimo approssimato $x^*$ e l'intervallo finale.

---

### Caso 3: Ottimizzazione Numerica con Metodo di Newton 1D

1. **Definizione delle Formule**:
   * Scrivere le derivate prima $f'(x)$ e seconda $f''(x)$ della funzione obiettivo.
   * Scrivere la formula di ricorrenza: $x_{k+1} = x_k - \frac{f'(x_k)}{f''(x_k)}$.
2. **Calcolo Iterativo**:
   * Partendo dal punto iniziale $x_0$, calcolare a ogni iterazione i valori numerici di $f'(x_k)$ e $f''(x_k)$.
   * Calcolare il punto successivo $x_{k+1}$ e valutare l'avanzamento assoluto $|x_{k+1} - x_k|$.
3. **Criterio di Arresto**:
   * Arrestarsi all'iterazione $k$ in cui $|x_{k+1} - x_k| \le \epsilon$ (tolleranza).
   * Organizzare i calcoli in una tabella riassuntiva che mostra: $k$, $x_k$, $f'(x_k)$, $f''(x_k)$, $x_{k+1}$, e $|x_{k+1} - x_k|$.
4. **Verifica della Natura del Punto**:
   * Verificare il segno di $f''(x^*)$ per confermare se si tratta di un massimo o di un minimo.
