# Method Card: Classificazione di Matrici Hessiane (n=2)

## Quando usarla
Da usare per classificare la natura di un punto stazionario di una funzione di due variabili (minimo, massimo, sella, caso inconclusivo) valutando la matrice Hessiana $2 \times 2$ o la convessità/concavità globale su $\mathbb{R}^2$.

## Input tipico dell'esercizio
- Punto stazionario $P^* = (x^*, y^*)$.
- Matrice Hessiana $H_f(x, y) = \begin{bmatrix} A & B \\ B & C \end{bmatrix}$.

## Output richiesto
- Segnatura della matrice Hessiana (definita positiva/negativa, indefinita, semidefinita).
- Classificazione del punto stazionario.

## Procedura in 5-8 passi
1. **Valutazione della matrice**: Sostituire le coordinate di $P^*$ nella matrice Hessiana generale:
   $$H_f(P^*) = \begin{bmatrix} A & B \\ B & C \end{bmatrix}$$
2. **Determinante**: Calcolare $\det(H_f) = AC - B^2$.
3. **Analisi del segno del determinante**:
   - Se $\det(H_f) < 0 \implies$ la matrice è indefinita. Il punto $P^*$ è un **punto di sella**.
   - Se $\det(H_f) > 0 \implies$ procedere al calcolo della traccia.
   - Se $\det(H_f) = 0 \implies$ procedere al passo 6 (caso inconclusivo).
4. **Analisi della traccia**: Calcolare $\text{tr}(H_f) = A + C$ (oppure verificare il segno di $A$):
   - Se $\text{tr}(H_f) > 0$ (o $A > 0$) $\implies$ la matrice è definita positiva ($H_f \succ 0$). Il punto $P^*$ è un **minimo locale stretto**.
   - Se $\text{tr}(H_f) < 0$ (o $A < 0$) $\implies$ la matrice è definita negativa ($H_f \prec 0$). Il punto $P^*$ è un **massimo locale stretto**.
5. **Autovalori espliciti (facoltativo)**: Se richiesto, calcolare gli autovalori risolvendo l'equazione caratteristica:
   $$\lambda^2 - \text{tr}(H_f)\lambda + \det(H_f) = 0$$
6. **Caso semidefinito ($\det = 0$)**: Se $\det(H_f) = 0$, il test del secondo ordine fallisce. La matrice è semidefinita. Per classificare il punto, analizzare la differenza $f(x, y) - f(P^*)$ in un intorno di $P^*$ (es. lungo rette/curve passanti per il punto).

## Errori frequenti
- **Confondere il segno di $B$**: Sbagliare il segno del termine misto $B$ nel calcolare il determinante (ricorda che viene sottratto come $-B^2$, quindi il segno di $B$ non influisce su $\det(H_f)$).
- **Semidefinita trattata come sella**: Concludere frettolosamente che un punto è di sella solo perché $\det(H_f) = 0$. Una matrice semidefinita può comunque corrispondere a un minimo o massimo locale (non stretto) o globale.

## Mini-template di risposta
```markdown
1. Hessiana nel punto \(P^* = (x^*, y^*)\):
   \(H_f(x^*, y^*) = \begin{bmatrix} A & B \\ B & C \end{bmatrix} = \begin{bmatrix} ... & ... \\ ... & ... \end{bmatrix}\).
2. Determinante: \(\det(H_f) = A \cdot C - B^2 = ...\).
3. Traccia (se \(\det > 0\)): \(\text{tr}(H_f) = A + C = ...\).
## Esercizi collegati
- `20_esercizi_pnl.pdf`, esercizi 1-10 (vedi [[pnl_non_vincolata_esercizi_punti_stazionari]] e [[pnl_20_esercizi_catalogo]])
- `esercizi_riepilogo.pdf`, esercizio 3 (vedi [[riepilogo_pl_pli_pnl_esercizi_misti]])

