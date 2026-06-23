# Pattern d'Esame: Gradiente e Newton a Confronto

## Descrizione del Pattern
Esercizi algoritmici in cui si richiede di calcolare un'iterazione del metodo del gradiente (con line search esatta) e un'iterazione del metodo di Newton multivariabile a partire da un punto dato, verificando la stazionarietà/ottimalità dei punti intermedi e finali.

## Trigger RAG
- "metodo del gradiente" + "line search in modo esatto"
- "metodo di Newton a partire dal punto"
- "verificare se i punti trovati sono punti di minimo/massimo"
- "ortogonalità consecutiva"
- "convergenza in una iterazione"

## Schema di Risposta Atteso

1. **Iterazione del Metodo del Gradiente**:
   * Calcolare il gradiente $\nabla f(x_k)$.
   * Dichiarare la direzione corretta: $d_k = -\nabla f(x_k)$ per minimizzazione, oppure $d_k = \nabla f(x_k)$ per massimizzazione.
   * Impostare la coordinata parametrica $x(\alpha) = x_k + \alpha d_k$.
   * Riscrivere la funzione obiettivo $\phi(\alpha) = f(x(\alpha))$.
   * Derivare e porre a zero: $\phi'(\alpha) = 0 \implies \alpha_k$.
   * Scrivere le coordinate del nuovo punto $x_{k+1} = x_k + \alpha_k d_k$.
2. **Iterazione del Metodo di Newton**:
   * Valutare l'Hessiana $H_f(x_k)$ nel punto di partenza.
   * Impostare il sistema di Newton $H_f(x_k) d_k = -\nabla f(x_k)$ per trovare la direzione $d_k$ (invece di invertire direttamente l'Hessiana).
   * Eseguire l'aggiornamento con passo unitario: $x_{k+1} = x_k + d_k$.
3. **Verifica Ottimalità e Analisi**:
   * Valutare il gradiente nei punti intermedi ottenuti. Se il gradiente non è nullo, escludere che il punto sia ottimo locale.
   * Se il gradiente si annulla, studiare la segnatura dell'Hessiana nel punto.
   * Giustificare se il metodo di Newton raggiunge l'ottimo globale esatto in un passo citando la natura quadratica della funzione (se applicabile).
