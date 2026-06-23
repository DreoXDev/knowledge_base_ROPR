---
type: method
topic: programmazione_non_lineare
status: active
reliability: official
---

# Riduzione del Numero di Variabili Libere

Il metodo di riduzione delle variabili libere consente di semplificare un problema di programmazione non lineare vincolato in $n$ variabili, riducendolo a un problema non vincolato (o con meno vincoli) in $n-m$ variabili, sfruttando le relazioni imposte dai vincoli di uguaglianza.

---

## Applicabilità e Condizioni

Il metodo è applicabile quando:
1. Il problema presenta uno o più vincoli di uguaglianza:
   $$g_i(x_1, \dots, x_n) = 0, \quad i = 1, \dots, m$$
2. È possibile esplicitare in modo **univoco** $m$ variabili (dette *variabili dipendenti*) in funzione delle restanti $n-m$ (dette *variabili libere* o *indipendenti*).

### Quando NON è applicabile (o presenta limiti):
- **Esplicitazione non univoca**: Se il vincolo è non lineare (ad esempio $x_1^2 + x_2^2 = 1$), l'esplicitazione di una variabile introduce una radice quadrata con doppio segno ($x_1 = \pm\sqrt{1-x_2^2}$). Questo frammenta il dominio e richiede di studiare separatamente più rami, rendendo il metodo laborioso o non applicabile globalmente.
- **Sistemi non lineari complessi**: Se i vincoli di uguaglianza non sono algebricamente risolvibili in modo analitico per isolare le variabili.

---

## Procedura Operativa Passo-Passo

Sia dato un problema con $n$ variabili e $m$ vincoli di uguaglianza ($m < n$):

### 1. Selezione delle variabili da esplicitare
Scegliere $m$ variabili che compaiono nei vincoli in forma facilmente risolvibile. I vincoli lineari sono i candidati ideali.

### 2. Esplicitazione
Risolvere il sistema di vincoli esprimendo le $m$ variabili scelte in funzione delle restanti $n-m$:
$$x_{k} = \phi_k(x_{m+1}, \dots, x_n), \quad k = 1, \dots, m$$

### 3. Sostituzione nella Funzione Obiettivo
Sostituire le espressioni ottenute nella funzione obiettivo $f(x_1, \dots, x_n)$, ottenendo una nuova funzione ridotta $\tilde{f}$ di $n-m$ variabili:
$$\tilde{f}(x_{m+1}, \dots, x_n) = f\left(\phi_1(\dots), \dots, \phi_m(\dots), x_{m+1}, \dots, x_n\right)$$

### 4. Risoluzione del Problema Ridotto
Risolvere il problema di ottimizzazione non vincolato per la funzione ridotta $\tilde{f}$:
- Calcolare il gradiente $\nabla \tilde{f} = 0$ per trovare i punti stazionari.
- Valutare l'Hessiana $\nabla^2 \tilde{f}$ per classificare i punti (massimi, minimi, sella).

### 5. Ricostruzione della Soluzione Originale
Sostituire i valori delle variabili ottime libere nelle equazioni di esplicitazione (passo 2) per ottenere le coordinate ottime delle variabili eliminate $x^*_1, \dots, x^*_m$.

---

## Esempio Lineare Semplice
*Per i dettagli analitici dei calcoli, fare riferimento a [[pnl_riduzione_variabili_esempio_lineare]].*

Sia il problema:
$$\min \quad f(x_1, x_2) = (x_1 - 2)^2 + 2(x_2 - 1)^2 \quad \text{s.t.} \quad x_1 + 4x_2 = 3$$

1. Si esplicita $x_1$ dal vincolo lineare: $x_1 = 3 - 4x_2$.
2. Si sostituisce nella funzione obiettivo ottenendo una funzione in una sola variabile $x_2$:
   $$\tilde{f}(x_2) = (3 - 4x_2 - 2)^2 + 2(x_2 - 1)^2 = 18x_2^2 - 12x_2 + 3$$
3. Si risolve ponendo la derivata prima a zero: $\tilde{f}'(x_2) = 36x_2 - 12 = 0 \implies x_2^* = \frac{1}{3}$.
4. Poiché $\tilde{f}''(x_2) = 36 > 0$, il punto è di minimo.
5. Si ricava la variabile eliminata: $x_1^* = 3 - 4\left(\frac{1}{3}\right) = \frac{5}{3}$.
   La soluzione ottima è $x^* = \left(\frac{5}{3}, \frac{1}{3}\right)$.

---

## Limiti del Metodo
- **Perdita di informazioni sulla Lagrangiana**: Riducendo il problema, non si ottengono direttamente i valori dei moltiplicatori di Lagrange $\lambda_i$, che contengono informazioni sulla sensibilità del valore ottimo rispetto alle variazioni del vincolo (shadow prices).
- **Vincoli di disuguaglianza**: Il metodo non si estende facilmente in presenza di vincoli di disuguaglianza, a meno che non si sappia a priori quali vincoli sono attivi (riducendoli a uguaglianze). In generale, per i vincoli di disuguaglianza si preferiscono le condizioni di KKT.

Vedi anche:
- [[pnl_metodo_moltiplicatori_lagrange]]
- [[pnl_condizioni_kkt]]
- [[pnl_riduzione_variabili_esempio_lineare]]
