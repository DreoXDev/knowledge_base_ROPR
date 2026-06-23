# Method Card: Condizioni di Ottimalità Unidimensionale (1D)

## Quando usarla
Da usare per risolvere e classificare analiticamente i punti stazionari di una funzione obiettivo $f(x)$ a una variabile reale, e per determinare l'ottimalità globale tramite lo studio della convessità/concavità.

## Input tipico dell'esercizio
- Funzione obiettivo $f(x)$ due volte derivabile.
- Dominio di definizione (es. intero asse reale $\mathbb{R}$ o intervallo limitato $[a, b]$).

## Output richiesto
- Derivata prima $f'(x)$ e derivata seconda $f''(x)$.
- Identificazione dei punti stazionari (soluzioni di $f'(x) = 0$).
- Classificazione dei punti (massimi, minimi, flessi).
- Dichiarazione di ottimalità globale tramite proprietà di curvatura.

## Procedura in 4 passi
1. **Condizione Necessaria del Primo Ordine**: Calcolare $f'(x)$ e risolvere $f'(x^*) = 0$ per trovare tutti i punti stazionari interni candidati.
2. **Condizione Sufficiente del Secondo Ordine**: Calcolare $f''(x)$ e valutarne il segno nei punti stazionari trovati:
   - Se $f''(x^*) < 0 \implies x^*$ è un punto di **massimo locale**.
   - Se $f''(x^*) > 0 \implies x^*$ è un punto di **minimo locale**.
   - Se $f''(x^*) = 0 \implies$ il test è inconclusivo. È necessario studiare il segno delle derivate successive.
3. **Ottimalità Globale**:
   - Se $f''(x) \le 0$ per ogni $x$ nel dominio $\implies f(x)$ è concava e il punto stazionario di massimo locale $x^*$ è un **massimo globale**.
   - Se $f''(x) \ge 0$ per ogni $x$ nel dominio $\implies f(x)$ è convessa e il punto stazionario di minimo locale $x^*$ è un **minimo globale**.
4. **Ottimo agli Estremi (se applicabile)**: Se il dominio è limitato ad un intervallo $[a, b]$, confrontare il valore di $f(x^*)$ con i valori della funzione ai confini $f(a)$ e $f(b)$ per identificare l'ottimo globale effettivo.

## Errori frequenti
- **Dimenticare gli estremi dell'intervallo**: Classificare solo il punto stazionario interno senza verificare se l'ottimo globale si trova sui confini $a$ o $b$ dell'intervallo chiuso di definizione.
- **Assumere ottimalità globale senza dimostrazione**: Dichiarare che un punto di massimo locale è globale senza aver dimostrato che $f''(x) \le 0$ su tutto il dominio.

## Mini-template di risposta
```markdown
1. Derivata prima: \(f'(x) = ...\)
2. Punti stazionari: \(f'(x) = 0 \implies x^* = ...\)
3. Derivata seconda: \(f''(x) = ...\)
4. Valutazione nel punto: \(f''(x^*) = ... < 0 \implies\) massimo locale.
5. Ottimalità globale: Poiché \(f''(x) \le 0 \ \forall x \in \mathbb{R}\), la funzione è concava e \(x^*\) è un massimo globale.
```
