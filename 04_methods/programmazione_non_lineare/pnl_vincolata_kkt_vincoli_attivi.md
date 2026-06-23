---
type: method
topic: programmazione_non_lineare
status: consolidated
sources:
  - raw_assets/Programmazione Non Lineare/PNL Vincolata 4.pdf
reliability: official
---

# PNL Vincolata - Condizioni KKT ed Enumerazione dei Vincoli Attivi

Nel contesto della Programmazione Non Lineare (PNL) vincolata da disuguaglianze, le condizioni di Karush-Kuhn-Tucker (KKT) permettono di individuare i punti candidati all'ottimo studiando quali vincoli sono "attivi" (ovvero soddisfatti con uguaglianza $= 0$) e quali sono "inattivi" ($< 0$) nel punto ottimo.

---

## Prerequisiti Teorici

### 1. Forma Standard dei Vincoli
Per un problema di minimizzazione, tutti i vincoli di disuguaglianza devono essere portati nella forma standard:
$$g_i(x) \le 0$$
- Un vincolo del tipo $h(x) \ge b$ deve essere riscritto moltiplicando per $-1$:
  $$b - h(x) \le 0 \implies g_i(x) = -(h(x) - b) \le 0$$

### 2. Lagrangiana
Dato il problema $\min f(x)$ s.t. $g_i(x) \le 0$ per $i = 1, \dots, m$, la funzione Lagrangiana è definita come:
$$L(x, \mu) = f(x) + \sum_{i=1}^m \mu_i g_i(x)$$
dove $\mu_i$ sono i moltiplicatori di Lagrange (o KKT) associati ai vincoli di disuguaglianza.

### 3. Condizioni KKT
Un punto $x^*$ e un vettore di moltiplicatori $\mu^*$ soddisfano le condizioni di ottimalità KKT se:
1. **Stazionarietà**: $\nabla_x L(x^*, \mu^*) = \nabla f(x^*) + \sum_{i=1}^m \mu_i^* \nabla g_i(x^*) = 0$
2. **Ammissibilità Primale**: $g_i(x^*) \le 0 \quad \forall i = 1, \dots, m$
3. **Ammissibilità Duale**: $\mu_i^* \ge 0 \quad \forall i = 1, \dots, m$ (per problemi di minimizzazione)
4. **Complementarità degli Scarti**: $\mu_i^* g_i(x^*) = 0 \quad \forall i = 1, \dots, m$

---

## Vincoli Attivi vs Inattivi e Complementarità

La condizione di complementarità $\mu_i g_i(x) = 0$ impone che per ciascun vincolo si verifichi una delle seguenti situazioni:
- **Vincolo Inattivo**: Se $g_i(x^*) < 0$ (il punto si trova all'interno della regione ammissibile rispetto al vincolo $i$), allora il relativo moltiplicatore deve essere nullo:
  $$\mu_i^* = 0$$
- **Vincolo Attivo**: Se $g_i(x^*) = 0$ (il punto giace sulla frontiera definita dal vincolo $i$), allora il moltiplicatore $\mu_i^*$ può essere strettamente positivo:
  $$\mu_i^* \ge 0$$

---

## Metodo di Enumerazione Combinatoria

Con $m$ vincoli di disuguaglianza, vi sono $2^m$ possibili combinazioni di vincoli attivi/inattivi. Per ciascuna combinazione si imposta un sistema risolutivo:
1. Per i vincoli ipotizzati **inattivi**, si pone direttamente $\mu_i = 0$.
2. Per i vincoli ipotizzati **attivi**, si impone l'uguaglianza $g_i(x) = 0$.
3. Si risolve il sistema di stazionarietà $\nabla_x L = 0$ accoppiato con le equazioni dei vincoli attivi per trovare il punto candidato $x$ e i relativi moltiplicatori non nulli.

---

## Criteri di Scarto dei Candidati all'Esame

Un punto candidato ricavato da una specifica combinazione di vincoli attivi deve essere scartato se:
- **Violazione dell'Ammissibilità Primale**: Il punto viola anche uno solo dei vincoli originari ($g_i(x) > 0$).
- **Violazione dell'Ammissibilità Duale**: Uno dei moltiplicatori associati ai vincoli attivi risulta negativo ($\mu_i < 0$).
- **Incompatibilità del Sistema**: Le equazioni dei vincoli attivi sono geometricamente incompatibili (es. intersezione vuota).

---

## Schema Operativo d'Esame

### Passo 1: Standardizzazione
Riscrivere il problema di minimo con vincoli nella forma standard $g_i(x, y) \le 0$ e stendere la Lagrangiana $L(x, y, \mu)$.

### Passo 2: Stesura delle Condizioni KKT
Scrivere esplicitamente le equazioni di stazionarietà $\frac{\partial L}{\partial x} = 0$ e $\frac{\partial L}{\partial y} = 0$.

### Passo 3: Enumerazione dei Casi
Analizzare sistematicamente i casi, partendo da quelli a minore numero di vincoli attivi (es. 0 vincoli attivi = ottimo non vincolato, poi 1 vincolo attivo, poi coppie di vincoli attivi).

### Passo 4: Risoluzione del Sistema per ciascun Caso
- Porre a zero i moltiplicatori dei vincoli inattivi.
- Risolvere il sistema lineare o non lineare per le coordinate $(x, y)$ e i moltiplicatori rimasti.

### Passo 5: Validazione e Scarto
Controllare se il punto rispetta tutti i vincoli del problema e se i moltiplicatori calcolati hanno il segno corretto ($\ge 0$ per minimo).

### Passo 6: Selezione dell'Ottimo Globale
Valutare $f(x, y)$ su tutti i candidati validi superstiti. Il candidato con il valore obiettivo minimo è l'ottimo globale vincolato.
