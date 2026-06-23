# Method Card: Metodo di Newton 1D (Algoritmo delle Tangenti)

## Quando usarla
Da utilizzare per eseguire iterazioni del metodo di Newton in una variabile per trovare lo zero della derivata prima $f'(x) = 0$ (punti stazionari di ottimo) con rapidità di convergenza locale quadratica.

## Input tipico dell'esercizio
- Funzione obiettivo $f(x)$.
- Punto iniziale di partenza $x_0$.
- Tolleranza di arresto $\epsilon$ (solitamente riferita all'avanzamento $|x_{k+1} - x_k|$).
- Numero di iterazioni richieste.

## Output richiesto
- Calcolo delle derivate prima $f'(x)$ e seconda $f''(x)$.
- Aggiornamento iterativo del punto tramite la formula di Newton.
- Criterio di arresto e classificazione del punto finale.

## Procedura in 5 passi
1. **Calcolo analitico delle derivate**: Calcolare $f'(x)$ e $f''(x)$.
2. **Valutazione nel punto corrente**: Calcolare i valori numerici di $f'(x_k)$ e $f''(x_k)$.
3. **Calcolo del punto successivo**: Applicare la formula:
   $$x_{k+1} = x_k - \frac{f'(x_k)}{f''(x_k)}$$
4. **Verifica del criterio di arresto**: Calcolare la variazione assoluta $|x_{k+1} - x_k|$. Se $|x_{k+1} - x_k| \le \epsilon$, fermarsi; altrimenti incrementare $k = k+1$ e ripetere dal passo 2.
5. **Classificazione dell'ottimo**: Controllare il segno di $f''(x^*)$ per verificare se si tratta di un massimo ($f'' < 0$) o minimo ($f'' > 0$).

## Errori frequenti
- **Divisione per zero**: Applicare la formula quando $f''(x_k) = 0$. In tal caso il metodo fallisce ed è necessario cambiare punto di partenza o dichiarare il fallimento dell'algoritmo.
- **Dimenticare il segno meno nella formula**: Scrivere erroneamente $x_{k+1} = x_k + \frac{f'}{f''}$.

## Mini-template di risposta
```markdown
1. Derivate: \(f'(x) = ...\) e \(f''(x) = ...\)
2. Iterazione \(k\): \(x_k = ...\)
3. Calcolo: \(f'(x_k) = ...\), \(f''(x_k) = ...\)
4. Aggiornamento: \(x_{k+1} = x_k - \frac{f'(x_k)}{f''(x_k)} = ...\)
5. Controllo errore: \(|x_{k+1} - x_k| = ... \le \epsilon\)? [Sì/No].
```
