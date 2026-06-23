---
type: solved-example
topic: programmazione_non_lineare
status: consolidated
sources:
  - raw_assets/Programmazione Non Lineare/PNL 1D.pdf
reliability: official
---

# Esercizio Svolto: Metodo di Newton 1D

## Testo dell'Esercizio

Si consideri la funzione a una variabile:
$$f(x) = 12x - 3x^4 - 2x^6$$

Si richiede di trovare il punto di massimo globale applicando il metodo di Newton 1D a partire da un punto iniziale $x_0 = 1$ con una tolleranza sull'avanzamento $\epsilon = 0.02$.

---

## Analisi e Calcolo delle Derivate

1. **Derivata Prima**:
   $$f'(x) = 12 - 12x^3 - 12x^5$$
2. **Derivata Seconda**:
   $$f''(x) = -36x^2 - 60x^4$$
3. **Concavità**:
   Poiché $f''(x) \le 0$ per ogni $x \in \mathbb{R}$, la funzione $f(x)$ è **strettamente concava** su tutto $\mathbb{R}$. Questo garantisce che il metodo di Newton, se converge stazionariamente ad un punto in cui $f'(x) = 0$, ha trovato l'ottimo globale.

---

## Svolgimento Iterativo Passo-Passo

### Iterazione 0
- **Punto corrente**: $x_0 = 1.0$
- **Valutazione della funzione**:
  $$f(1.0) = 12(1.0) - 3(1.0)^4 - 2(1.0)^6 = 12 - 3 - 2 = 7.0$$
- **Valutazione derivata prima**:
  $$f'(1.0) = 12 - 12(1.0)^3 - 12(1.0)^5 = -12.0$$
- **Valutazione derivata seconda**:
  $$f''(1.0) = -36(1.0)^2 - 60(1.0)^4 = -96.0$$
- **Aggiornamento tramite formula di Newton**:
  $$x_1 = x_0 - \frac{f'(x_0)}{f''(x_0)} = 1.0 - \frac{-12.0}{-96.0} = 1.0 - 0.125 = 0.875$$
- **Verifica criterio di arresto**:
  $$|x_1 - x_0| = |0.875 - 1.0| = 0.125 > 0.02 \quad (\text{si procede})$$

### Iterazione 1
- **Punto corrente**: $x_1 = 0.875$
- **Valutazione della funzione**:
  $$f(0.875) \approx 7.8439$$
- **Valutazione derivata prima**:
  $$f'(0.875) = 12 - 12(0.875)^3 - 12(0.875)^5 \approx -2.1940$$
- **Valutazione derivata seconda**:
  $$f''(0.875) = -36(0.875)^2 - 60(0.875)^4 \approx -62.7330$$
- **Aggiornamento tramite formula di Newton**:
  $$x_2 = x_1 - \frac{f'(x_1)}{f''(x_1)} = 0.875 - \frac{-2.1940}{-62.7330} \approx 0.875 - 0.03497 \approx 0.84003$$
- **Verifica criterio di arresto**:
  $$|x_2 - x_1| = |0.84003 - 0.875| = 0.03497 > 0.02 \quad (\text{si procede})$$

### Iterazione 2
- **Punto corrente**: $x_2 = 0.84003$
- **Valutazione della funzione**:
  $$f(0.84003) \approx 7.8838$$
- **Valutazione derivata prima**:
  $$f'(0.84003) \approx -0.1325$$
- **Valutazione derivata seconda**:
  $$f''(0.84003) \approx -55.2790$$
- **Aggiornamento tramite formula di Newton**:
  $$x_3 = x_2 - \frac{f'(x_2)}{f''(x_2)} = 0.84003 - \frac{-0.1325}{-55.2790} \approx 0.84003 - 0.00240 \approx 0.83763$$
- **Verifica criterio di arresto**:
  $$|x_3 - x_2| = |0.83763 - 0.84003| = 0.00240 \le 0.02 \quad (\text{arresto})$$

---

## Tabella Riassuntiva delle Iterazioni

| Iterazione $k$ | $x_k$ | $f(x_k)$ | $f'(x_k)$ | $f''(x_k)$ | $x_{k+1}$ | $|x_{k+1} - x_k|$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 1.00000 | 7.00000 | -12.00000 | -96.00000 | 0.87500 | 0.12500 |
| 1 | 0.87500 | 7.84390 | -2.19400 | -62.73300 | 0.84003 | 0.03500 |
| 2 | 0.84003 | 7.88380 | -0.13250 | -55.27900 | 0.83763 | **0.00240** |

---

## Conclusione e Risultato d'Esame

L'algoritmo termina all'iterazione 2 poiché il passo di aggiornamento $|x_3 - x_2| = 0.0024 \le 0.02$.

- **Ottimo stazionario trovato**: $x^* \approx 0.8376$
- **Valore massimo ottimo**: $f(x^*) \approx 7.8839$
- **Verifica di convergenza**: Poiché $f''(x^*) \approx -55.2 \prec 0$, il punto è effettivamente un massimo locale. La concavità globale di $f(x)$ assicura che $x^*$ è il punto di **massimo globale**.
- **Confronto**: Il metodo di Newton è giunto a convergenza in sole $3$ iterazioni (valutazioni del punto) rispetto alle $8$ iterazioni necessarie per il metodo di bisezione, mostrando la caratteristica convergenza quadratica.
