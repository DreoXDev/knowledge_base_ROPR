# Method Card: Riduzione delle Variabili Libere

## Quando usarla
Da usare per risolvere o semplificare problemi di ottimizzazione non lineare vincolata quando sono presenti uno o più vincoli di uguaglianza semplici (in particolare vincoli lineari) che consentono di esprimere in modo univoco alcune variabili in funzione delle altre.

## Input tipico dell'esercizio
- Funzione obiettivo $f(x_1, \dots, x_n)$ da ottimizzare.
- Uno o più vincoli di uguaglianza $g_i(x_1, \dots, x_n) = 0$.

## Output richiesto
- Relazione di esplicitazione delle variabili dipendenti in funzione delle variabili libere.
- Funzione obiettivo ridotta $\tilde{f}$ a dimensione inferiore.
- Risoluzione del problema non vincolato ridotto ($\nabla \tilde{f} = 0$, classificazione tramite Hessiana ridotta $\nabla^2 \tilde{f}$).
- Coordinate del punto ottimo originale ricostruito e valore ottimo della funzione obiettivo.

## Procedura in 5 passi
1. **Esplicitazione**: Scegliere $m$ variabili e isolarle univocamente dai vincoli di uguaglianza in funzione delle restanti $n-m$ variabili libere.
2. **Sostituzione**: Sostituire le relazioni trovate all'interno della funzione obiettivo $f(x)$ per ottenere la funzione ridotta $\tilde{f}(x_{\text{libere}})$.
3. **Calcolo del gradiente**: Determinare il gradiente della funzione ridotta $\nabla \tilde{f}$ e porlo a zero per individuare i punti stazionari del problema ridotto.
4. **Analisi del secondo ordine**: Calcolare la matrice Hessiana della funzione ridotta $\nabla^2 \tilde{f}$ nei punti stazionari trovati per verificarne la natura (minimo se definita positiva, massimo se definita negativa).
5. **Ricostruzione delle coordinate**: Sostituire i valori delle variabili libere ottime nelle equazioni di esplicitazione (passo 1) per calcolare le coordinate delle variabili eliminate.

## Errori frequenti
- **Esplicitazione non univoca**: Provare a usare il metodo con vincoli quadratici (es. $x^2 + y^2 = 1$) senza gestire il doppio segno della radice quadrata.
- **Dimenticare la ricostruzione**: Trovare il punto ottimo del problema ridotto e dimenticare di ricavare le coordinate ottime delle variabili eliminate.
- **Nessuna verifica di ottimalità**: Non calcolare l'Hessiana della funzione ridotta per dimostrare che il punto trovato sia effettivamente un minimo o un massimo.

## Esempio minimo
$$\min \quad f(x, y) = (x - 2)^2 + 2(y - 1)^2 \quad \text{s.t.} \quad x + 4y = 3$$
*   **Esplicitazione**: $x = 3 - 4y$.
*   **Sostituzione**: $\tilde{f}(y) = (3 - 4y - 2)^2 + 2(y - 1)^2 = 18y^2 - 12y + 3$.
*   **Risoluzione**: $\tilde{f}'(y) = 36y - 12 = 0 \implies y^* = \frac{1}{3}$.
*   **Verifica**: $\tilde{f}''(y) = 36 > 0 \implies$ minimo globale.
*   **Ricostruzione**: $x^* = 3 - 4\left(\frac{1}{3}\right) = \frac{5}{3} \implies P^* = \left(\frac{5}{3}, \frac{1}{3}\right)$, con $f(P^*) = 1$.

## Mini-template di risposta
```markdown
1. Esplicitazione dal vincolo: \(x_k = \phi_k(x_{\neq k})\).
2. Funzione ridotta: \(\tilde{f}(x_{\neq k}) = ...\)
3. Condizione del primo ordine: \(\nabla \tilde{f} = 0 \implies x_{\neq k}^* = ...\)
4. Condizione del secondo ordine: \(\nabla^2 \tilde{f} = ...\) [definita positiva/negativa] \(\implies\) punto di [minimo/massimo].
5. Ripristino variabili: \(x_k^* = \phi_k(x_{\neq k}^*) = ...\)
   Punto di ottimo: \(x^* = (..., ...)\) con valore \(f(x^*) = ...\).
```
