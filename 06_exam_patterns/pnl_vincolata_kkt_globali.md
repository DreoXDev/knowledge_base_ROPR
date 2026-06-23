# Pattern d'Esame: KKT e Ottimalità Globale (PNL Vincolata)

## Descrizione del Pattern
Esercizi che richiedono di determinare i punti di massimo e minimo globale di una funzione obiettivo $f(x, y)$ su una regione ammissibile $\Omega$ definita da vincoli di disuguaglianza, impostando le condizioni KKT e risolvendo sistematicamente per casi.

---

## Trigger RAG
- "trovare massimi e minimi globali della funzione f(x,y) sull'insieme"
- "soluzioni del sistema KKT con moltiplicatori non negativi"
- "risolvere il sistema KKT associato al problema"
- "verificare l'esistenza di massimi e minimi globali"

---

## Schema di Risoluzione Atteso

1.  **Analisi Preliminare della Regione $\Omega$**:
    -   Stabilire se l'insieme è chiuso e limitato (**compatto**).
    -   Se compatto, citare il **Teorema di Weierstrass** per garantire che massimo e minimo globale esistono.
    -   Se illimitato, analizzare il limite della funzione obiettivo lungo direzioni ammissibili per valutare se diverge a $+\infty$ (massimo non esistente) o $-\infty$ (minimo non esistente).
2.  **Standardizzazione dei Vincoli**:
    -   Riscrivere tutti i vincoli di disuguaglianza nella forma standard $h_j(x, y) \le 0$.
3.  **Scrittura della Lagrangiana**:
    -   $L(x, y, \mu) = f(x, y) + \sum \mu_j h_j(x, y)$
4.  **Sistema KKT**:
    -   Stazionarietà: $\nabla_{x, y} L = 0$.
    -   Ammissibilità primale: $h_j(x, y) \le 0$.
    -   Complementarità: $\mu_j h_j(x, y) = 0$.
    -   Segno dei moltiplicatori (Ammissibilità duale):
        -   **Per minimo**: $\mu_j \ge 0$.
        -   **Per massimo**: $\mu_j \le 0$ (o invertire il segno della funzione obiettivo).
5.  **Risoluzione Combinatoria per Casi**:
    -   Analizzare separatamente i casi con vincoli attivi ($h_k = 0$) e inattivi ($\mu_j = 0$).
6.  **Confronto e Conclusioni**:
    -   Confrontare il valore della funzione obiettivo $f(x, y)$ su tutti i candidati validi.

---

## Esempi di Riferimento
- [[pnl_vincolata_esercizi_kkt_globali]]: 10 esercizi svolti analiticamente con cerchi, ellissi, semispazi ed insiemi illimitati.

---

## Mini-template di Risposta per lo Scritto
```markdown
1. Regione ammissibile \(\Omega\): [compatta \(\implies\) Weierstrass garantisce ottimi globali / illimitata].
2. Lagrangiana:
   \(L(x, y, \mu_1, \mu_2) = f(x, y) + \mu_1 h_1(x, y) + \mu_2 h_2(x, y)\)
3. Sistema KKT per [Minimo (\(\mu_j \ge 0\)) / Massimo (\(\mu_j \le 0\))]:
   * \(\frac{\partial L}{\partial x} = ... = 0\)
   * \(\frac{\partial L}{\partial y} = ... = 0\)
   * \(\mu_j h_j = 0, \quad h_j \le 0\)
4. Risoluzione dei casi:
   * Caso 1 (\(\mu_1 = \mu_2 = 0\)): Punto \(P_1 = (..., ...)\) [ammissibile/scartato]
   * Caso 2 (\(h_1 = 0, \mu_2 = 0\)): Punto \(P_2 = (..., ...)\) con \(\mu_1 = ...\) [ammissibile/scartato]
5. Valutazione finale:
   \(f(P_1) = ...\), \(f(P_2) = ... \implies\) Minimo globale in \(... = ...\), Massimo globale in \(... = ...\).
```
