# Method Card: Metodo del Gradiente con Line Search Esatta

## Quando usarla
Da usare per calcolare iterazioni del metodo del gradiente (steepest descent/ascent) con determinazione analitica del passo $\alpha_k$ per funzioni non vincolate.

## Input tipico dell'esercizio
- Funzione obiettivo $f(x, y)$ da minimizzare o massimizzare.
- Punto iniziale $x_0 = (x_0, y_0)$.
- Numero di iterazioni richieste.

## Output richiesto
- Direzione di spostamento ad ogni passo.
- Funzione monodimensionale del passo $\phi(\alpha)$.
- Lunghezza del passo ottimo $\alpha_k$.
- Coordinate dei punti intermedi e finali.

## Procedura in 5-8 passi
1. **Calcolo del gradiente**: Trovare $\nabla f(x_k)$ nel punto corrente.
2. **Scelta della direzione**:
   - Per minimizzazione: $d_k = -\nabla f(x_k)$.
   - Per massimizzazione: $d_k = \nabla f(x_k)$.
3. **Punto parametrico**: Esprimere le coordinate in funzione di $\alpha$: $x_k + \alpha d_k$.
4. **Funzione obiettivo unidimensionale**: Sostituire le coordinate nella funzione obiettivo per ottenere $\phi(\alpha) = f(x_k + \alpha d_k)$.
5. **Calcolo del passo esatto**: Derivare rispetto ad $\alpha$ e porre a zero: $\phi'(\alpha) = 0 \implies \alpha_k$.
6. **Aggiornamento del punto**: Calcolare il nuovo punto $x_{k+1} = x_k + \alpha_k d_k$.
7. **Verifica ortogonalità (facoltativa per controllo)**: Verificare che il nuovo gradiente $\nabla f(x_{k+1})$ sia ortogonale alla direzione corrente: $\nabla f(x_{k+1})^T d_k = 0$.

## Errori frequenti
- **Segno errato della direzione**: Usare la direzione di discesa ($-\nabla f$) per problemi di massimo o viceversa.
- **Errori algebrici nella sostituzione**: Sbagliare i calcoli espandendo i polinomi $\phi(\alpha)$.
- **Ignorare l'ortogonalità consecutiva**: Non verificare che $d_{k+1}^T d_k = 0$ per rilevare tempestivamente errori di calcolo.

## Mini-template di risposta
```markdown
1. Gradiente in \(x_k = (..., ...)\): \(\nabla f(x_k) = [..., ...]^T\).
2. Direzione: \(d_k = \mp \nabla f(x_k) = [..., ...]^T\).
3. Line Search:
   \(x_k + \alpha d_k = [..., ...]^T\).
   \(\phi(\alpha) = f(..., ...) = ... \alpha^2 + ... \alpha + ...\).
   \(\phi'(\alpha) = 0 \implies \alpha_k = ...\).
4. Nuovo punto: \(x_{k+1} = x_k + \alpha_k d_k = (..., ...)\).
```

## Esercizi collegati
- `esercizi_riepilogo.pdf`, esercizio 3a (vedi [[riepilogo_pl_pli_pnl_esercizi_misti]])
