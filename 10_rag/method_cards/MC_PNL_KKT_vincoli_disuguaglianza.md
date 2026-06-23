# Method Card: Condizioni KKT con Vincoli di Disuguaglianza

## Quando usarla
Da usare per risolvere problemi di ottimizzazione non lineare soggetti a vincoli di disuguaglianza (es. semispazi, poligoni, parabole) tramite l'analisi sistematica di tutte le combinazioni di vincoli attivi/inattivi.

## Input tipico dell'esercizio
- Funzione obiettivo $f(x, y)$ da minimizzare o massimizzare.
- Vincoli di disuguaglianza $g_j(x, y) \le 0$ o $g_j(x, y) \ge 0$.

## Output richiesto
- Regione ammissibile analizzata (compatta o illimitata).
- Funzione Lagrangiana generalizzata.
- Condizioni di stazionarietà, ammissibilità primale, complementarità degli scarti e ammissibilità duale (segno dei moltiplicatori $\mu_j$).
- Analisi per ciascuna combinazione di vincoli attivi e inattivi.
- Tabella riassuntiva dei candidati (validati o scartati con motivazione).
- Punto di ottimo globale definitivo.

## Procedura in 5-8 passi
1. **Forma standard**: Ricondurre i vincoli di disuguaglianza alla forma $h_j(x, y) \le 0$. Se è presente un massimo, mantenere la stessa Lagrangiana ma imporre $\mu_j \le 0$ (oppure massimizzare $-f(x)$ con $\mu_j \ge 0$).
2. **Scrittura della Lagrangiana**: Formulare la Lagrangiana generalizzata:
   $$L(x, y, \mu) = f(x, y) + \sum \mu_j h_j(x, y)$$
3. **Impostazione del sistema KKT**:
   - Stazionarietà: $\nabla_x L = 0$ e $\frac{\partial L}{\partial y} = 0$.
   - Ammissibilità primale: $h_j(x, y) \le 0$.
   - Complementarità: $\mu_j h_j(x, y) = 0$.
   - Ammissibilità duale: $\mu_j \ge 0$ (per minimi) oppure $\mu_j \le 0$ (per massimi).
4. **Analisi combinatoria**: Risolvere il sistema esplorando sistematicamente le $2^m$ combinazioni di vincoli attivi ($h_j = 0$) e inattivi ($\mu_j = 0$).
5. **Filtraggio (Scarto)**: Per ciascun punto ottenuto, verificare se rispetta le disuguaglianze primali e i segni dei moltiplicatori duali.
6. **Confronto**: Valutare $f(x, y)$ nei punti validi per determinare gli ottimi globali.

## Errori frequenti
- **Segno errato dei moltiplicatori per massimo**: Dimenticare che per la massimizzazione i moltiplicatori devono essere non positivi ($\mu_j \le 0$).
- **Saltare la complementarità degli scarti**: Non impostare esplicitamente $\mu_j = 0$ per i vincoli inattivi durante l'esplorazione dei casi.
- **Inversione dei vincoli**: Dimenticare di invertire il segno per i vincoli $\ge$ (es. $x \ge -1 \implies -x-1 \le 0$).

## Esempio minimo ($\min f(x,y)=4(x-1)^2+(y-2)^2$ s.t. $x+y \le 2, x \ge -1, y \ge -1$)
*   **Lagrangiana**: $L = 4(x-1)^2+(y-2)^2+\mu_1(x+y-2)-\mu_2(x+1)-\mu_3(y+1)$
*   **Caso 1 (solo $g_1$ attivo)**: $x+y=2$ and $\mu_2=\mu_3=0 \implies (x,y)=(0.8, 1.2)$, con $\mu_1 = 1.6 > 0$ (valido, ottimo globale con $f=0.8$).
*   **Caso 2 (solo $g_2$ attivo)**: $x=-1$ and $\mu_1=\mu_3=0 \implies (x,y)=(-1, 2)$, con $\mu_2 = -16 < 0$ (scartato).

## Mini-template di risposta
```markdown
1. Vincoli in forma standard: \(h_1(x, y) = ... \le 0\), \(h_2(x, y) = ... \le 0\).
2. Lagrangiana: \(L = f(x, y) + \mu_1 h_1(x, y) + \mu_2 h_2(x, y)\).
3. Sistema KKT per [minimo (\(\mu \ge 0\)) / massimo (\(\mu \le 0\))]:
   * \(\nabla_x L = ... = 0\)
   * \(\frac{\partial L}{\partial y} = ... = 0\)
   * \(\mu_j h_j = 0\), \(\mu_j \text{ sign rule}\)
4. Risoluzione casi:
   * Caso 1 (\(\mu_1=\mu_2=0\)): Punto \(P_0 = (..., ...)\) [ammissibile/non ammissibile]
   * Caso 2 (\(h_1=0, \mu_2=0\)): Punto \(P_1 = (..., ...)\) con \(\mu_1 = ...\) [ammissibile/non ammissibile]
5. Valutazione finale: Minimo/Massimo globale in \((..., ...)\) con valore \(f = ...\).
```
