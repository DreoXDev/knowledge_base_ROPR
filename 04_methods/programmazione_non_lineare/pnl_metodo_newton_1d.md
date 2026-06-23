---
type: method
topic: programmazione_non_lineare
status: consolidated
sources:
  - raw_assets/Programmazione Non Lineare/PNL 1D.pdf
reliability: official
---

# Metodo di Newton in una Variabile (1D)

Il metodo di Newton (noto anche come metodo delle tangenti) è un algoritmo di approssimazione locale per trovare uno zero di un'equazione non lineare, in particolare la derivata prima di una funzione $f'(x) = 0$, per individuare i punti stazionari di $f(x)$.

---

## Approssimazione Quadratica (Sviluppo di Taylor)

Il metodo si basa sull'approssimazione locale al secondo ordine della funzione obiettivo $f(x)$ nell'intorno del punto corrente $x_k$ tramite lo sviluppo di Taylor:

$$f(x_{k+1}) \approx f(x_k) + f'(x_k)(x_{k+1} - x_k) + \frac{1}{2} f''(x_k)(x_{k+1} - x_k)^2$$

Per massimizzare (o minimizzare) questa approssimazione quadratica rispetto a $x_{k+1}$, annulliamo la sua derivata prima rispetto a $x_{k+1}$:

$$\frac{d}{d x_{k+1}} \left[ f(x_k) + f'(x_k)(x_{k+1} - x_k) + \frac{1}{2} f''(x_k)(x_{k+1} - x_k)^2 \right] = f'(x_k) + f''(x_k)(x_{k+1} - x_k) = 0$$

Risolvendo rispetto a $x_{k+1}$, si ottiene la formula di ricorrenza classica di Newton:

$$x_{k+1} = x_k - \frac{f'(x_k)}{f''(x_k)}$$

---

## Procedura Operativa Passo-Passo

### 1. Inizializzazione
- Scegliere un punto iniziale $x_0 \in \mathbb{R}$.
- Definire la tolleranza $\epsilon > 0$.
- Impostare il contatore delle iterazioni $k = 0$.

### 2. Passo Iterativo (Iterazione $k$)
1. **Calcolo delle Derivate**:
   Valutare $f'(x_k)$ e $f''(x_k)$.
   - *Nota di sicurezza*: Se $f''(x_k) = 0$, l'algoritmo fallisce per divisione per zero.
2. **Aggiornamento del Punto**:
   $$x_{k+1} = x_k - \frac{f'(x_k)}{f''(x_k)}$$
3. **Verifica del Criterio di Arresto**:
   - Se $|x_{k+1} - x_k| \le \epsilon$, fermarsi. La soluzione approssimata è $x^* \approx x_{k+1}$.
   - Opzionalmente, verificare se il gradiente è prossimo a zero: $|f'(x_{k+1})| < \delta$.
4. Incrementare $k = k + 1$ e ripetere.

---

## Vantaggi, Svantaggi e Rischi

### Vantaggi
- **Velocità**: Gode di **convergenza quadratica** locale. Quando l'algoritmo è vicino a $x^*$, il numero di cifre decimali esatte raddoppia ad ogni iterazione.

### Svantaggi
- Richiede il calcolo sia della derivata prima $f'(x)$ che della derivata seconda $f''(x)$.

### Rischi e Cause di Fallimento
- **Derivata seconda nulla**: Se $f''(x_k) = 0$, la formula non è definita.
- **Punto iniziale lontano (Divergenza)**: La convergenza è garantita solo localmente (ossia se $x_0$ è vicino a $x^*$). Se $x_0$ è scelto male, l'algoritmo può divergere o entrare in loop oscillatori.
- **Ottimi non desiderati**: Se la funzione ha più punti stazionari, Newton può convergere a un minimo locale, un massimo locale o un punto di sella a seconda di dove viene inizializzato.
