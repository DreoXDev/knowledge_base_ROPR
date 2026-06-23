---
type: method
topic: programmazione_non_lineare
status: consolidated
sources:
  - raw_assets/Programmazione Non Lineare/PNL 1D.pdf
reliability: official
---

# Algoritmo Dicotomico di Bisezione (1D)

Il metodo di bisezione è una procedura numerica per trovare lo zero della derivata prima $f'(x) = 0$ (e quindi individuare i punti stazionari di una funzione $f(x)$) all'interno di un intervallo di incertezza noto $[\underline{x}, \bar{x}]$.

---

## Ipotesi di Applicabilità

1. **Continuità e Derivabilità**: La funzione $f(x)$ deve essere continua sull'intervallo chiuso $[\underline{x}, \bar{x}]$ e derivabile sull'intervallo aperto $(\underline{x}, \bar{x})$.
2. **Proprietà di Curvatura (Unimodalità)**:
   - Per un problema di **massimizzazione**, la funzione deve essere strettamente **concava** ($f''(x) \le 0$).
   - Per un problema di **minimizzazione**, la funzione deve essere strettamente **convessa** ($f''(x) \ge 0$).
3. **Segno della Derivata agli Estremi**: La derivata deve cambiare segno agli estremi dell'intervallo:
   - Caso concavo (massimo): $f'(\underline{x}) > 0$ e $f'(\bar{x}) < 0$.
   - Caso convesso (minimo): $f'(\underline{x}) < 0$ e $f'(\bar{x}) > 0$.

---

## Idea Intuitiva

La pendenza (derivata) di $f(x)$ fornisce informazioni sulla direzione in cui si trova il punto di ottimo $x^*$:
- **Problema di Massimo (Funzione Concava)**:
  - Se $f'(x_k) > 0$, la funzione sta crescendo. L'ottimo $x^*$ si trova a destra di $x_k$. Il punto $x_k$ diventa il nuovo estremo inferiore: $\underline{x} = x_k$.
  - Se $f'(x_k) < 0$, la funzione sta decrescendo. L'ottimo $x^*$ si trova a sinistra di $x_k$. Il punto $x_k$ diventa il nuovo estremo superiore: $\bar{x} = x_k$.
- **Problema di Minimo (Funzione Convessa)**:
  - Se $f'(x_k) > 0$, la funzione sta crescendo. L'ottimo $x^*$ si trova a sinistra di $x_k$. Il punto $x_k$ diventa il nuovo estremo superiore: $\bar{x} = x_k$.
  - Se $f'(x_k) < 0$, la funzione sta decrescendo. L'ottimo $x^*$ si trova a destra di $x_k$. Il punto $x_k$ diventa il nuovo estremo inferiore: $\underline{x} = x_k$.

---

## Pseudocodice dell'Algoritmo (Massimizzazione)

```text
Dati: f', intervallo iniziale [x_low, x_high], tolleranza epsilon

while (x_high - x_low) > 2 * epsilon:
    x_k = (x_low + x_high) / 2
    if f'(x_k) == 0:
        return x_k
    if f'(x_k) > 0:
        x_low = x_k
    else:
        x_high = x_k

return (x_low + x_high) / 2
```

---

## Procedura Operativa Passo-Passo

### 1. Inizializzazione
- Impostare $\underline{x}_0 = \underline{x}$ e $\bar{x}_0 = \bar{x}$.
- Scegliere la tolleranza $\epsilon > 0$.
- Impostare $k = 0$.

### 2. Passo Iterativo (Iterazione $k$)
1. **Calcolo del Punto Medio**:
   $$x_k = \frac{\underline{x}_k + \bar{x}_k}{2}$$
2. **Valutazione della Derivata**:
   Calcolare $f'(x_k)$.
3. **Verifica del Criterio di Arresto**:
   Se $\bar{x}_k - \underline{x}_k \le 2\epsilon$, fermarsi. L'ottimo approssimato è $x^* \approx x_k$. L'intervallo finale in cui giace l'ottimo è $[\underline{x}_k, \bar{x}_k]$.
4. **Aggiornamento dell'Intervallo (Massimo)**:
   - Se $f'(x_k) > 0 \implies \underline{x}_{k+1} = x_k$ e $\bar{x}_{k+1} = \bar{x}_k$.
   - Se $f'(x_k) < 0 \implies \underline{x}_{k+1} = \underline{x}_k$ e $\bar{x}_{k+1} = x_k$.
   - Se $f'(x_k) = 0 \implies$ stop, $x^* = x_k$.
5. Incrementare $k = k + 1$ e ripetere.

---

## Struttura della Tabella delle Iterazioni

Durante l'esame, i calcoli vanno presentati in una tabella ordinata:

| Iterazione $k$ | $\underline{x}_k$ | $\bar{x}_k$ | $x_k$ | $f(x_k)$ (Opzionale) | $f'(x_k)$ | $\bar{x}_k - \underline{x}_k$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $0$ | $\underline{x}_0$ | $\bar{x}_0$ | $x_0$ | $f(x_0)$ | $f'(x_0)$ | $\bar{x}_0 - \underline{x}_0$ |

*Nota: Non è necessario calcolare $f(x_k)$ a ogni iterazione per far avanzare l'algoritmo (basta il segno di $f'(x_k)$). È consigliato calcolare $f(x_k)$ solo alla fine o se richiesto esplicitamente.*

---

## Errori Comuni da Evitare

- **Inversione delle regole di aggiornamento**: Aggiornare gli estremi come se fosse un problema di massimo quando si sta minimizzando o viceversa.
- **Calcolo del valore obiettivo invece della derivata**: Ricordarsi che la bisezione 1D cerca lo zero di $f'(x)$, quindi si valuta il segno di $f'(x_k)$, non di $f(x_k)$.
- **Criterio di arresto errato**: Confondere l'intervallo di tolleranza. Il criterio $\bar{x} - \underline{x} \le 2\epsilon$ assicura che la distanza tra il punto medio e l'ottimo sia al massimo $\epsilon$.
