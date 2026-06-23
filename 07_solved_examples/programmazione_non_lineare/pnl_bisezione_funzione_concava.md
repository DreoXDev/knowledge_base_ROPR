---
type: solved-example
topic: programmazione_non_lineare
status: consolidated
sources:
  - raw_assets/Programmazione Non Lineare/PNL 1D.pdf
reliability: official
---

# Esercizio Svolto: Metodo di Bisezione 1D per Funzione Concava

## Testo dell'Esercizio

Si consideri la funzione a una variabile:
$$f(x) = 12x - 3x^4 - 2x^6$$

Si richiede di trovare il punto di massimo globale nell'intervallo $[0, 2]$ tramite il metodo di bisezione con una tolleranza sull'intervallo di incertezza pari a $2\epsilon = 0.02$ ($\epsilon = 0.01$).

---

## Analisi Preliminare della Funzione

1. **Derivata Prima**:
   $$f'(x) = \frac{d}{dx}(12x - 3x^4 - 2x^6) = 12 - 12x^3 - 12x^5$$
2. **Derivata Seconda**:
   $$f''(x) = \frac{d}{dx}(12 - 12x^3 - 12x^5) = -36x^2 - 60x^4$$
3. **Verifica della Concavità**:
   Poiché $x^2 \ge 0$ e $x^4 \ge 0$ per ogni $x \in \mathbb{R}$, si ha che $f''(x) \le 0$ per ogni $x \in \mathbb{R}$. La funzione $f(x)$ è **strettamente concava** su tutto il suo dominio, quindi ammette un unico punto di massimo globale che corrisponde all'unico punto stazionario interno in cui $f'(x) = 0$.
4. **Segno della Derivata agli Estremi**:
   - Per $\underline{x}_0 = 0$: $f'(0) = 12 > 0$ (funzione crescente).
   - Per $\bar{x}_0 = 2$: $f'(2) = 12 - 12(2^3) - 12(2^5) = 12 - 96 - 384 = -468 < 0$ (funzione decrescente).
   Poiché $f'(0) \cdot f'(2) < 0$, lo zero della derivata prima (l'ottimo $x^*$) si trova all'interno dell'intervallo $[0, 2]$.

---

## Svolgimento Iterativo Passo-Passo

### Iterazione 0
- **Estremi**: $\underline{x}_0 = 0$, $\bar{x}_0 = 2$.
- **Ampiezza intervallo**: $\bar{x}_0 - \underline{x}_0 = 2 > 0.02$ (si procede).
- **Punto medio**:
  $$x_1 = \frac{0 + 2}{2} = 1.0$$
- **Valutazione derivata**:
  $$f'(1.0) = 12 - 12(1)^3 - 12(1)^5 = -12 < 0$$
- **Aggiornamento estremi**: Poiché $f'(1.0) < 0$ (derivata negativa), l'ottimo si trova a sinistra. L'estremo superiore viene aggiornato a $\bar{x}_1 = 1.0$, mentre l'estremo inferiore rimane $\underline{x}_1 = 0$.

### Iterazione 1
- **Estremi**: $\underline{x}_1 = 0$, $\bar{x}_1 = 1.0$.
- **Ampiezza intervallo**: $\bar{x}_1 - \underline{x}_1 = 1.0 > 0.02$ (si procede).
- **Punto medio**:
  $$x_2 = \frac{0 + 1.0}{2} = 0.5$$
- **Valutazione derivata**:
  $$f'(0.5) = 12 - 12(0.5)^3 - 12(0.5)^5 = 12 - 1.5 - 0.375 = 10.125 > 0$$
- **Aggiornamento estremi**: Poiché $f'(0.5) > 0$, l'ottimo si trova a destra. L'estremo inferiore viene aggiornato a $\underline{x}_2 = 0.5$, mentre l'estremo superiore rimane $\bar{x}_2 = 1.0$.

### Iterazione 2
- **Estremi**: $\underline{x}_2 = 0.5$, $\bar{x}_2 = 1.0$.
- **Ampiezza intervallo**: $\bar{x}_2 - \underline{x}_2 = 0.5 > 0.02$ (si procede).
- **Punto medio**:
  $$x_3 = \frac{0.5 + 1.0}{2} = 0.75$$
- **Valutazione derivata**:
  $$f'(0.75) = 12 - 12(0.75)^3 - 12(0.75)^5 \approx 4.090 > 0$$
- **Aggiornamento estremi**: Poiché $f'(0.75) > 0$, l'estremo inferiore viene aggiornato a $\underline{x}_3 = 0.75$, l'estremo superiore rimane $\bar{x}_3 = 1.0$.

### Iterazione 3
- **Estremi**: $\underline{x}_3 = 0.75$, $\bar{x}_3 = 1.0$.
- **Ampiezza intervallo**: $\bar{x}_3 - \underline{x}_3 = 0.25 > 0.02$ (si procede).
- **Punto medio**:
  $$x_4 = \frac{0.75 + 1.0}{2} = 0.875$$
- **Valutazione derivata**:
  $$f'(0.875) = 12 - 12(0.875)^3 - 12(0.875)^5 \approx -2.194 < 0$$
- **Aggiornamento estremi**: Poiché $f'(0.875) < 0$, l'estremo superiore viene aggiornato a $\bar{x}_4 = 0.875$, l'estremo inferiore rimane $\underline{x}_4 = 0.75$.

*(I passaggi successivi seguono lo stesso schema riducendo l'ampiezza dell'intervallo)*

---

## Tabella Riassuntiva delle Iterazioni

| Iterazione $k$ | $\underline{x}_k$ | $\bar{x}_k$ | $x_{k+1}$ | $f(x_{k+1})$ | $f'(x_{k+1})$ | $\bar{x}_k - \underline{x}_k$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0.000000 | 2.000000 | 1.000000 | 7.0000 | -12.0000 | 2.000000 |
| 1 | 0.000000 | 1.000000 | 0.500000 | 5.7813 | 10.1250 | 1.000000 |
| 2 | 0.500000 | 1.000000 | 0.750000 | 7.6948 | 4.0900 | 0.500000 |
| 3 | 0.750000 | 1.000000 | 0.875000 | 7.8439 | -2.1940 | 0.250000 |
| 4 | 0.750000 | 0.875000 | 0.812500 | 7.8672 | 1.3100 | 0.125000 |
| 5 | 0.812500 | 0.875000 | 0.843750 | 7.8829 | -0.3400 | 0.062500 |
| 6 | 0.812500 | 0.843750 | 0.828125 | 7.8815 | 0.5100 | 0.031250 |
| 7 | 0.828125 | 0.843750 | 0.835938 | 7.8839 | 0.0156 | **0.015625** |

---

## Conclusione e Risultato d'Esame

Poiché all'iterazione 7 l'ampiezza dell'intervallo $\bar{x} - \underline{x} = 0.84375 - 0.828125 = 0.015625$ è inferiore alla tolleranza imposta di $0.02$, l'algoritmo si arresta.

- **Ottimo approssimato**: $x^* \approx 0.836$
- **Valore ottimo della funzione**: $f(x^*) \approx 7.884$
- **Intervallo finale di incertezza**:
  $$0.828125 < x^* < 0.84375$$
