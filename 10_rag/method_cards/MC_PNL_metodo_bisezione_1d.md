# Method Card: Metodo di Bisezione 1D (Algoritmo Dicotomico)

## Quando usarla
Da utilizzare per eseguire iterazioni del metodo dicotomico di bisezione 1D per trovare lo zero della derivata prima $f'(x) = 0$ (ottimo locale/globale di funzioni concave/convesse) in un intervallo chiuso $[\underline{x}, \bar{x}]$.

## Input tipico dell'esercizio
- Funzione obiettivo $f(x)$ o la sua derivata prima $f'(x)$.
- Intervallo di incertezza iniziale $[\underline{x}_0, \bar{x}_0]$.
- Tolleranza $\epsilon$ o $2\epsilon$.
- Numero di iterazioni richieste.

## Output richiesto
- Tabella delle iterazioni con aggiornamenti degli estremi.
- Intervallo di incertezza finale $[\underline{x}_f, \bar{x}_f]$ di ampiezza inferiore a $2\epsilon$.
- Punto di ottimo approssimato $x^*$ e valore obiettivo $f(x^*)$.

## Procedura in 5 passi
1. **Calcolo del Punto Medio**: Calcolare $x_k = \frac{\underline{x}_k + \bar{x}_k}{2}$.
2. **Valutazione del Segno di $f'(x_k)$**: Calcolare $f'(x_k)$ per determinare la direzione dell'ottimo.
3. **Aggiornamento degli Estremi**:
   - Se stiamo massimizzando una funzione concava:
     - Se $f'(x_k) > 0 \implies \underline{x}_{k+1} = x_k$ (l'ottimo è a destra).
     - Se $f'(x_k) < 0 \implies \bar{x}_{k+1} = x_k$ (l'ottimo è a sinistra).
   - Se stiamo minimizzando una funzione convessa:
     - Se $f'(x_k) > 0 \implies \bar{x}_{k+1} = x_k$ (l'ottimo è a sinistra).
     - Se $f'(x_k) < 0 \implies \underline{x}_{k+1} = x_k$ (l'ottimo è a destra).
4. **Verifica Criterio di Arresto**: Se l'ampiezza dell'intervallo $\bar{x}_{k+1} - \underline{x}_{k+1} \le 2\epsilon$, fermarsi; altrimenti ripetere dal passo 1.
5. **Calcolo Soluzione**: L'ottimo approssimato è $x^* \approx \frac{\underline{x}_{k+1} + \bar{x}_{k+1}}{2}$.

## Errori frequenti
- **Confondere il segno di $f'(x_k)$**: Sbagliare l'estremo da aggiornare. Ricordare che se $f'(x_k) > 0$ in un problema di massimo concavo, la funzione sta ancora salendo verso destra, quindi l'estremo inferiore sale.
- **Valutare $f(x_k)$ invece di $f'(x_k)$**: La bisezione 1D usa solo il segno della derivata prima per tagliare a metà l'intervallo.

## Mini-template di risposta
```markdown
1. Iterazione \(k\): Intervallo corrente \([\underline{x}_k, \bar{x}_k]\).
2. Punto medio: \(x_{k+1} = \frac{\underline{x}_k + \bar{x}_k}{2} = ...\)
3. Derivata: \(f'(x_{k+1}) = ...\)
4. Aggiornamento: Poiché \(f'(x_{k+1})\) è [positivo/negativo], l'intervallo diventa \([..., ...]\).
5. Arresto: \(\bar{x} - \underline{x} = ... \le 2\epsilon\)? [Sì/No].
```
