# Pattern d'Esame: Studio di Funzione PNL Non Vincolata

## Descrizione del Pattern
Domande teorico-pratiche volte a determinare i punti stazionari di una funzione di due variabili, valutarne la convessità/concavità globale su $\mathbb{R}^2$ e classificare la natura di tali punti (minimi, massimi, selle).

## Trigger RAG
- "punti stazionari di"
- "convessa o concava nello spazio R2"
- "punti di minimo locale e massimo locale"
- "Hessiana semidefinita"
- "matrice Hessiana definita positiva"

## Schema di Risposta Atteso

1. **Ricerca dei Punti Stazionari**:
   * Scrivere esplicitamente le derivate parziali del primo ordine $\frac{\partial f}{\partial x}$ e $\frac{\partial f}{\partial y}$.
   * Impostare il sistema $\nabla f(x, y) = 0$ e indicare tutti i punti soluzioni candidati.
2. **Determinazione della Matrice Hessiana**:
   * Calcolare le derivate parziali di secondo ordine.
   * Scrivere la matrice Hessiana generale $H_f(x, y)$.
3. **Analisi di Convessità/Concavità Globale**:
   * Spiegare se la matrice Hessiana è semidefinita/definita positiva o negativa per ogni punto dello spazio $\mathbb{R}^2$ per stabilire se la funzione è convessa, concava, o nessuna delle due.
   * Se in un punto qualsiasi l'Hessiano ha determinante negativo, dichiarare che la funzione non è né convessa né concava in $\mathbb{R}^2$.
4. **Classificazione dei Punti Stazionari**:
   * Per ciascun punto stazionario, valutare la segnatura di $H_f$ tramite determinante e traccia (in 2D).
   * Se $\det(H_f) > 0$: minimo locale (se $\text{tr}(H_f) > 0$) o massimo locale (se $\text{tr}(H_f) < 0$).
   * Se $\det(H_f) < 0$: punto di sella.
   * Se $\det(H_f) = 0$: dichiarare che il test è inconclusivo e utilizzare una manipolazione analitica (es. restrizione a una retta o completamento del quadrato) per concludere.
