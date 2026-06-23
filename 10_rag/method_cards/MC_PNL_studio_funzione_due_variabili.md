# Method Card: Studio di Funzione PNL Non Vincolata

## Quando usarla
Da usare per esercizi di ottimizzazione non vincolata in cui si richiede di studiare una funzione di due variabili, trovarne i punti stazionari, valutarne la convessità/concavità globale su $\mathbb{R}^2$ e classificare la natura dei punti stazionari (minimi, massimi, selle).

## Input tipico dell'esercizio
- Funzione analitica di due variabili $f(x, y)$ (solitamente polinomiale).

## Output richiesto
- Elenco dei punti stazionari.
- Valutazione della convessità/concavità globale su $\mathbb{R}^2$.
- Classificazione di ciascun punto stazionario (minimo locale/globale, massimo locale/globale, sella).

## Procedura in 5-8 passi
1. **Calcolo del gradiente**: Trovare il vettore gradiente $\nabla f(x, y) = [\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}]^T$.
2. **Uguagliamento a zero**: Impostare il sistema $\nabla f(x, y) = 0$ e risolverlo per identificare i punti stazionari.
3. **Calcolo dell'Hessiana**: Determinare la matrice Hessiana $H_f(x, y)$ calcolando le derivate parziali seconde.
4. **Analisi convessità globale**: Verificare se $H_f(x, y)$ è definita/semidefinita positiva o negativa per *ogni* punto dello spazio. Se in qualche punto $\det(H_f) < 0$, la funzione non è globalmente né convessa né concava.
5. **Classificazione locale**: Valutare $H_f$ in ciascun punto stazionario $P^*$:
   - Se $\det(H_f) > 0$ e $\text{tr}(H_f) > 0 \implies$ minimo locale.
   - Se $\det(H_f) > 0$ e $\text{tr}(H_f) < 0 \implies$ massimo locale.
   - Se $\det(H_f) < 0 \implies$ punto di sella.
   - Se $\det(H_f) = 0 \implies$ test inconclusivo.
6. **Risoluzione casi degeneri**: Se $\det(H_f) = 0$, analizzare il comportamento locale lungo curve (es. restrizione a rette come $y=x$) o riscritture algebriche per concludere se sella o ottimo.

## Errori frequenti
- **Hessiana semidefinita conclusa a priori**: Dichiarare che un punto è ottimo locale basandosi solo su un autovalore nullo senza analisi aggiuntiva.
- **Dimenticare l'ottimalità globale**: Non collegare la convessità globale al fatto che un minimo locale sia anche globale.

## Mini-template di risposta
```markdown
1. Gradiente: \(\nabla f(x, y) = [..., ...]^T = 0 \implies P^* = (..., ...)\).
2. Matrice Hessiana: \(H_f(x, y) = \begin{bmatrix} ... & ... \\ ... & ... \end{bmatrix}\).
3. Studio globale: Poiché \(\det(H_f) = ...\), la funzione [è / non è] convessa/concava.
4. Classificazione: In \(P^*\), \(\det(H_f(P^*)) = ...\) e \(\text{tr}(H_f(P^*)) = ...\), quindi \(P^*\) è [minimo locale / massimo locale / sella].
```
