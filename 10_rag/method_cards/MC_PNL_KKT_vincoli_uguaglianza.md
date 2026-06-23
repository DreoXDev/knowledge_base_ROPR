# Method Card: Condizioni KKT con Vincoli di Uguaglianza

## Quando usarla
Da usare per risolvere problemi di ottimizzazione non lineare soggetti a soli vincoli di uguaglianza (es. cerchi, ellissi, rette).

## Input tipico dell'esercizio
- Funzione obiettivo $f(x, y)$ da minimizzare o massimizzare.
- Vincolo di uguaglianza $g(x, y) = 0$.

## Output richiesto
- Funzione Lagrangiana.
- Sistema KKT (stazionarietà della Lagrangiana e rispetto del vincolo).
- Punti candidati e relativi moltiplicatori $\lambda$.
- Valutazione finale per Weierstrass dei massimi e minimi globali.

## Procedura in 5-8 passi
1. **Verifica Weierstrass**: Dichiarare che la regione ammissibile è compatta (chiusa e limitata) e la funzione è continua, garantendo l'esistenza di massimi/minimi globali.
2. **Scrittura della Lagrangiana**: Formulare la Lagrangiana con moltiplicatore $\lambda$ libero in segno:
   $$L(x, y, \lambda) = f(x, y) + \lambda g(x, y)$$
3. **Calcolo delle derivate**: Trovare $\frac{\partial L}{\partial x}$ e $\frac{\partial L}{\partial y}$.
4. **Impostazione del sistema**: Scrivere il sistema KKT:
   $$\begin{cases} \frac{\partial L}{\partial x} = 0 \\ \frac{\partial L}{\partial y} = 0 \\ g(x, y) = 0 \end{cases}$$
5. **Risoluzione del sistema**: Esplicitare $x$ e $y$ in funzione di $\lambda$ dalle prime due equazioni, oppure ricavare relazioni dirette tra $x$ e $y$ (es. $y = kx$), e sostituire nel vincolo.
6. **Calcolo dei candidati**: Trovare le coordinate dei punti candidati e il relativo valore di $\lambda$.
7. **Confronto e conclusione**: Valutare $f(x, y)$ in tutti i punti trovati. Il valore più basso è il minimo globale vincolato, il più alto è il massimo globale vincolato.

## Errori frequenti
- **Imporre vincoli di segno a $\lambda$**: Trattare $\lambda$ come se dovesse essere non negativo. I moltiplicatori dei vincoli di uguaglianza sono liberi in segno.
- **Dimenticare Weierstrass**: Risolvere l'esercizio senza motivare teoricamente l'esistenza globale dei punti ottimi.

## Mini-template di risposta
```markdown
1. Regione compatta, Weierstrass garantisce massimi e minimi globali.
2. Lagrangiana: \(L(x, y, \lambda) = f(x, y) + \lambda g(x, y)\).
3. Sistema KKT:
   \(\begin{cases} \frac{\partial L}{\partial x} = 0 \\ \frac{\partial L}{\partial y} = 0 \\ g(x, y) = 0 \end{cases} \implies \begin{cases} ... \\ ... \\ ... \end{cases}\)
4. Risoluzione: Punti candidati \(P_1 = (..., ...)\) con \(\lambda = ...\) e \(P_2 = (..., ...)\) con \(\lambda = ...\).
5. Ottimalità: \(f(P_1) = ...\) (Massimo globale), \(f(P_2) = ...\) (Minimo globale).
```
