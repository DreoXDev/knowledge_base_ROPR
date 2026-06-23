# Method Card: Moltiplicatori di Lagrange con Vincoli di Uguaglianza

## Quando usarla
Da usare per identificare i punti stazionari di un problema di ottimizzazione non lineare soggetto esclusivamente a vincoli di uguaglianza $g_i(x) = 0$.

## Input tipico dell'esercizio
- Funzione obiettivo $f(x_1, \dots, x_n)$ da minimizzare o massimizzare.
- Vincoli di uguaglianza $g_i(x_1, \dots, x_n) = 0, \quad i = 1, \dots, m$.

## Output richiesto
- Funzione Lagrangiana $L(x, \lambda) = f(x) + \sum \lambda_i g_i(x)$.
- Sistema lagrangiano del primo ordine ($\nabla_x L = 0$ e $g_i(x) = 0$).
- Risoluzione del sistema per trovare le coordinate dei punti candidati $(x^*, \lambda^*)$.
- Classificazione dei punti candidati (confrontando i valori di $f$ o tramite l'Hessiana Orlata).
- Interpretazione geometrica dei gradienti paralleli/ortogonali nel punto ottimo, se richiesta.

## Procedura in 5 passi
1. **Costruzione della Lagrangiana**: Moltiplicare ciascun vincolo $g_i(x) = 0$ per un moltiplicatore $\lambda_i$ e sommarlo alla funzione obiettivo:
   $$L(x, \lambda) = f(x) + \sum_{i=1}^m \lambda_i g_i(x)$$
2. **Derivate Parziali**: Calcolare le derivate parziali di $L$ rispetto a ciascuna variabile decisionale $x_j$ e rispetto a ciascun moltiplicatore $\lambda_i$.
3. **Risoluzione del Sistema**: Impostare a zero le derivate per formare un sistema di $n+m$ equazioni. Risolverlo per determinare i punti candidati stazionari.
4. **Verifica della Regolarità**: Assicurarsi che i gradienti dei vincoli siano linearmente indipendenti (LICQ) nei punti stazionari.
5. **Classificazione dei punti**: Confrontare il valore di $f(x)$ nei diversi punti stazionari vincolati. Se la regione ammissibile è compatta (Teorema di Weierstrass), il punto stazionario con valore di $f$ massimo è il massimo globale vincolato, mentre quello con valore minimo è il minimo globale vincolato.

## Errori frequenti
- **Considerare le condizioni sufficienti**: Dimenticare che $\nabla L = 0$ individua solo punti candidati stazionari; è necessario classificarli.
- **Errori algebrici nel sistema**: Il sistema lagrangiano è spesso non lineare; procedere con cautela semplificando le relazioni prima di sostituire nel vincolo.
- **Segno del moltiplicatore**: Ricordare che i moltiplicatori $\lambda_i$ associati a vincoli di uguaglianza sono liberi in segno (non hanno vincoli di segno come quelli di disuguaglianza).

## Esempio minimo
$$\min/\max \quad f(x, y) = x + y \quad \text{s.t.} \quad x^2 + y^2 = 1$$
*   **Lagrangiana**: $L(x, y, \lambda) = x + y + \lambda(x^2 + y^2 - 1)$.
*   **Sistema**:
    $$\begin{cases} 1 + 2\lambda x = 0 \implies x = -\frac{1}{2\lambda} \\ 1 + 2\lambda y = 0 \implies y = -\frac{1}{2\lambda} \\ x^2 + y^2 = 1 \implies 2\left(-\frac{1}{2\lambda}\right)^2 = 1 \implies \lambda = \pm\frac{\sqrt{2}}{2} \end{cases}$$
*   **Candidati**: $A = \left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$ con $f(A) = \sqrt{2}$, e $B = \left(-\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right)$ con $f(B) = -\sqrt{2}$.
*   **Ottimi**: $A$ è il massimo globale, $B$ è il minimo globale.

## Mini-template di risposta
```markdown
1. Lagrangiana: \(L(x, y, \lambda) = f(x, y) + \lambda g(x, y) = ...\)
2. Condizioni del primo ordine (\(\nabla L = 0\)):
   * \(\frac{\partial L}{\partial x} = ... = 0\)
   * \(\frac{\partial L}{\partial y} = ... = 0\)
   * \(\frac{\partial L}{\partial \lambda} = g(x, y) = 0\)
3. Risoluzione sistema: \(x = ..., y = ... \implies \lambda = ...\)
4. Candidati trovati: \(P_1 = (..., ...)\) con \(\lambda_1 = ...\) e \(P_2 = (..., ...)\) con \(\lambda_2 = ...\)
5. Valutazione: \(f(P_1) = ...\) e \(f(P_2) = ... \implies\) [Minimo/Massimo] globale.
```
