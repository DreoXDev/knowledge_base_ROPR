---
type: theory
topic: programmazione_lineare_intera
status: active
sources: [BB PLI.pdf]
reliability: official
---

# Soluzioni Quasi-Ottime e Criteri di Arresto

Nei problemi di programmazione lineare intera di grandi dimensioni, la ricerca della soluzione ottima esatta con il Branch and Bound può richiedere tempi computazionali proibitivi o memoria eccessiva. È quindi comune arrestare l'algoritmo in anticipo accettando una soluzione **quasi-ottima**.

## Definizione di Soluzione Quasi-Ottima

Una soluzione intera ammissibile (incumbent $Z_I$) è definita **quasi-ottima** con un certo grado di tolleranza se il suo valore dista dal valore ottimo reale $Z^*$ al massimo di una certa quantità prefissata.

### 1. Tolleranza Assoluta ($K$)
Si accetta come ottimale una soluzione incumbent $Z_I$ se è garantito che disti meno di una costante assoluta $K > 0$ dal valore ottimo reale $Z^*$.
- Per problemi di massimo:
  $$
  Z^* - K \le Z_I \le Z^*
  $$
- Per problemi di minimo:
  $$
  Z^* \le Z_I \le Z^* + K
  $$

Poiché il valore ottimo reale $Z^*$ è ignoto durante l'esecuzione dell'algoritmo, si utilizza la stima ottimistica data dal miglior bound corrente tra i nodi aperti ($Bound_{best}$):
- Per problemi di massimo ($Bound_{best} = \max UB_{aperti}$):
  $$
  Bound_{best} - Z_I \le K
  $$
- Per problemi di minimo ($Bound_{best} = \min LB_{aperti}$):
  $$
  Z_I - Bound_{best} \le K
  $$

Se questa condizione è soddisfatta, l'algoritmo si arresta dichiarando $Z_I$ quasi-ottima.

### 2. Tolleranza Relativa ($\alpha$)
Si definisce quasi-ottima una soluzione $Z_I$ il cui scostamento percentuale rispetto all'ottimo reale sia inferiore a una frazione $\alpha \in (0, 1)$ (es. $\alpha = 0.05$ per una tolleranza del $5\%$).
- Per problemi di massimo:
  $$
  (1-\alpha) Z^* \le Z_I \le Z^* \implies (1-\alpha) Bound_{best} \le Z_I
  $$
- Per problemi di minimo:
  $$
  Z^* \le Z_I \le (1+\alpha) Z^* \implies Z_I \le (1+\alpha) Bound_{best}
  $$

---

## Criteri di Arresto del Branch and Bound

L'introduzione delle tolleranze modifica la regola di **potatura per bound (dominanza)**. Un nodo aperto $P_i$ con bound $Z_{rel}(P_i)$ può essere potato (chiuso) se:
- Massimo: $Z_{rel}(P_i) \le Z_I + K$ (oppure $Z_{rel}(P_i) \le Z_I / (1-\alpha)$).
- Minimo: $Z_{rel}(P_i) \ge Z_I - K$ (oppure $Z_{rel}(P_i) \ge Z_I / (1+\alpha)$).

Altri criteri di arresto comuni nelle implementazioni reali includono:
- **Limite di tempo**: Interruzione dopo un numero fissato di secondi (CPU time).
- **Limite di memoria/nodi**: Interruzione dopo aver generato un numero massimo di nodi o superato una soglia di RAM.
- **Assenza di miglioramenti**: Interruzione se l'incumbent $Z_I$ non migliora da un certo numero di iterazioni.

> [!IMPORTANT]
> Quando l'algoritmo viene interrotto per limiti di tempo, memoria o tolleranza, la soluzione incumbent corrente **non è garantita essere l'ottimo globale**. Tuttavia, l'intervallo dell'ottimo $[Z_I, Bound_{best}]$ (o viceversa) fornisce una misura precisa della massima deviazione possibile dall'ottimo reale.
