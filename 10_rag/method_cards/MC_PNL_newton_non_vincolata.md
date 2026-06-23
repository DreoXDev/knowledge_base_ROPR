# Method Card: Metodo di Newton per PNL Non Vincolata

## Quando usarla
Da usare per eseguire una o più iterazioni del metodo di Newton multivariabile per la ricerca di punti di ottimo non vincolati.

## Input tipico dell'esercizio
- Funzione obiettivo $f(x, y)$.
- Punto di partenza $x_0 = (x_0, y_0)$.
- Numero di iterazioni richieste.

## Output richiesto
- Gradiente e matrice Hessiana nel punto corrente.
- Risoluzione del sistema lineare per la direzione di Newton $d_k$.
- Nuovo punto aggiornato $x_{k+1} = x_k + d_k$.
- Classificazione e stazionarietà del punto ottenuto.

## Procedura in 5-8 passi
1. **Calcolo del gradiente**: Determinare $\nabla f(x_k)$.
2. **Calcolo dell'Hessiana**: Calcolare la matrice delle derivate seconde $H_f(x_k)$.
3. **Impostazione del sistema**: Impostare il sistema lineare:
   $$H_f(x_k) d_k = -\nabla f(x_k)$$
4. **Risoluzione del sistema**: Risolvere per la direzione $d_k = [d_x, d_y]^T$.
5. **Aggiornamento del punto**: Calcolare il nuovo punto con passo unitario:
   $$x_{k+1} = x_k + d_k$$
6. **Verifica della stazionarietà**: Calcolare il gradiente in $x_{k+1}$ e verificare se $\nabla f(x_{k+1}) = 0$.
7. **Giustificazione convergenza rapida**: Se la funzione è quadratica ed $H_f$ è definita positiva/negativa, affermare che $x_1$ è il punto di ottimo globale esatto raggiunto in una sola iterazione.

## Errori frequenti
- **Calcolo esplicito dell'inversa**: Provare a calcolare simbolicamente $[H_f]^{-1}$, operazione che all'esame porta a frequenti errori di calcolo. Risolvere sempre il sistema lineare.
- **Dimenticare il segno meno**: Dimenticare il segno meno a destra del sistema: $H_f d_k = -\nabla f(x_k)$.

## Mini-template di risposta
```markdown
1. Gradiente in \(x_k\): \(\nabla f(x_k) = [..., ...]^T\).
2. Hessiana in \(x_k\): \(H_f(x_k) = \begin{bmatrix} ... & ... \\ ... & ... \end{bmatrix}\).
3. Sistema di Newton:
   \(\begin{bmatrix} ... & ... \\ ... & ... \end{bmatrix} \begin{bmatrix} d_x \\ d_y \end{bmatrix} = -\begin{bmatrix} ... \\ ... \end{bmatrix} \implies d_k = \begin{bmatrix} ... \\ ... \end{bmatrix}\).
4. Aggiornamento: \(x_{k+1} = x_k + d_k = (..., ...)\).
```

## Esercizi collegati
- `esercizi_riepilogo.pdf`, esercizio 3b (vedi [[riepilogo_pl_pli_pnl_esercizi_misti]])

