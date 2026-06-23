# Pattern d'Esame: Classificazione Punti Stazionari ed Hessiana (PNL Non Vincolata)

## Descrizione del Pattern
Esercizi in cui viene fornita una funzione obiettivo a due variabili $f(x, y)$ non vincolata e si richiede di trovare tutti i punti stazionari e classificarli localmente (minimi, massimi locali o punti di sella) tramite la matrice Hessiana.

---

## Trigger RAG
- "trovare massimi e minimi locali della funzione"
- "classificare i punti stazionari di"
- "determinare la natura dei punti critici"
- "matrice Hessiana definita positiva/negativa"

---

## Schema di Risoluzione Atteso

1.  **Calcolo del Gradiente**:
    Calcolare analiticamente le derivate parziali prime:
    $$\nabla f(x, y) = \begin{bmatrix} \frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \end{bmatrix}$$
2.  **Risoluzione del Sistema $\nabla f(x, y) = 0$**:
    Impostare e risolvere il sistema non lineare. Prestare attenzione a raccogliere a fattor comune le variabili per evitare di perdere soluzioni (es. l'origine).
3.  **Costruzione della Matrice Hessiana**:
    Calcolare le derivate parziali seconde e definire la matrice:
    $$H_f(x, y) = \begin{bmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{bmatrix}$$
4.  **Valutazione Locale per ciascun Punto Critico**:
    Per ogni soluzione stazionaria $P^* = (x^*, y^*)$, calcolare $\det(H_f(P^*))$ e $\text{tr}(H_f(P^*))$:
    -   Se $\det(H) > 0$ e $\text{tr}(H) > 0$ (o $f_{xx} > 0$) $\implies$ **Minimo locale**.
    -   Se $\det(H) > 0$ e $\text{tr}(H) < 0$ (o $f_{xx} < 0$) $\implies$ **Massimo locale**.
    -   Se $\det(H) < 0$ $\implies$ **Punto di sella**.
    -   Se $\det(H) = 0$ $\implies$ **Test inconclusivo** (la matrice è semidefinita).
5.  **Dichiarazione dei Risultati**:
    Elencare i punti trovati suddivisi per categoria.

---

## Esempi di Riferimento
- [[pnl_non_vincolata_esercizi_punti_stazionari]]: contiene 10 esercizi svolti analiticamente con polinomi a due variabili.

---

## Mini-template di Risposta per lo Scritto
```markdown
1. Gradiente:
   \(\nabla f(x, y) = \begin{bmatrix} f_x \\ f_y \end{bmatrix} = \begin{bmatrix} ... \\ ... \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}\)
   Risolvendo il sistema si ottengono i punti stazionari: \(P_1 = (..., ...)\), \(P_2 = (..., ...)\).

2. Matrice Hessiana generale:
   \(H_f(x, y) = \begin{bmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{bmatrix} = \begin{bmatrix} ... & ... \\ ... & ... \end{bmatrix}\)

3. Valutazione nei punti:
   * Per \(P_1 = (..., ...)\):
     \(H_f(P_1) = \begin{bmatrix} ... & ... \\ ... & ... \end{bmatrix} \implies \det(H) = ... > 0\), \(\text{tr}(H) = ... > 0 \implies\) Minimo Locale.
   * Per \(P_2 = (..., ...)\):
     \(H_f(P_2) = \begin{bmatrix} ... & ... \\ ... & ... \end{bmatrix} \implies \det(H) = ... < 0 \implies\) Punto di Sella.
```
