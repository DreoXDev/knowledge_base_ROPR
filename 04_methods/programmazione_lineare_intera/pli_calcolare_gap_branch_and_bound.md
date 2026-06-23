---
type: method
topic: programmazione_lineare_intera
status: active
sources: [BB PLI.pdf]
reliability: official
---

# Metodo: Calcolare il Gap di Ottimalità

Questo metodo descrive le formule per calcolare il gap di ottimalità (assoluto e relativo) tra la migliore soluzione ammissibile disponibile (incumbent) e la valutazione ottimistica teorica (miglior bound tra i nodi aperti).

---

## Formule Generali del Gap

Siano:
- $Z_I$: Il valore della funzione obiettivo per la migliore soluzione intera ammissibile corrente (incumbent).
- $Z_{bound}$: Il miglior bound teorico (ottimistico) dei nodi aperti:
  - Per problemi di massimo: $Z_{bound} = \max_{P_j \in \text{aperti}} Z_{rel}(P_j)$.
  - Per problemi di minimo: $Z_{bound} = \min_{P_j \in \text{aperti}} Z_{rel}(P_j)$.

### 1. Gap Assoluto ($Gap_{abs}$)
Misura la massima distanza assoluta tra il valore ottimo reale $z^*$ e l'incumbent $Z_I$.

- **Problema di Massimo**:
  $$
  Gap_{abs} = Z_{bound} - Z_I
  $$

- **Problema di Minimo**:
  $$
  Gap_{abs} = Z_I - Z_{bound}
  $$

Un $Gap_{abs} = 0$ certifica l'ottimalità globale esatta di $Z_I$.

### 2. Gap Relativo ($Gap_{rel}$)
Misura lo scostamento percentuale massimo dell'incumbent rispetto all'ottimo reale.

- **Problema di Massimo**:
  $$
  Gap_{rel} = \frac{Z_{bound} - Z_I}{Z_bound} \quad (\text{se } Z_{bound} > 0)
  $$
  oppure rispetto all'incumbent per convenzione di molti solver (es. Gurobi/Cplex):
  $$
  Gap_{rel} = \frac{Z_{bound} - Z_I}{|Z_I|} \quad (\text{se } Z_I \neq 0)
  $$

- **Problema di Minimo**:
  $$
  Gap_{rel} = \frac{Z_I - Z_{bound}}{Z_bound} \quad (\text{se } Z_{bound} > 0)
  $$
  oppure:
  $$
  Gap_{rel} = \frac{Z_I - Z_{bound}}{|Z_I|} \quad (\text{se } Z_I \neq 0)
  $$

---

## Esempio di Applicazione

Si consideri un problema di **minimo** in cui:
- La migliore soluzione intera trovata ha valore $Z_I = 14.0$.
- L'albero ha due nodi aperti: $P_3$ con $LB = 13.6$ e $P_5$ con $LB = 13.7$.

### Passaggio 1: Trovare il miglior bound dei nodi aperti
Essendo un problema di minimo, il miglior bound (ottimistico) è il **minimo** $LB$ tra i nodi aperti:

$$
Z_{bound} = \min(13.6, 13.7) = 13.6
$$

### Passaggio 2: Calcolare il Gap Assoluto

$$
Gap_{abs} = Z_I - Z_{bound} = 14.0 - 13.6 = 0.4
$$

L'ottimo reale $z^*$ giace nell'intervallo $[13.6, 14.0]$.

### Passaggio 3: Calcolare il Gap Relativo

$$
Gap_{rel} = \frac{14.0 - 13.6}{13.6} = \frac{0.4}{13.6} \approx 0.0294 \quad (2.94\%)
$$
oppure rispetto all'incumbent:
$$
Gap_{rel} = \frac{14.0 - 13.6}{14.0} = \frac{0.4}{14.0} \approx 0.0286 \quad (2.86\%)
$$
