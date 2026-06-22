---
materia: ROPR
area: Programmazione Lineare
tipo: esempio-svolto
fonte: Ricerca Operativa - Metodo del Simplesso - 23-24.pdf
stato: completo
priorita: media
tags:
  - ropr
  - programmazione-lineare
  - simplesso
  - casi-particolari
  - esempio-svolto
---

# Esempio Svolto — Casi Particolari del Simplesso

Questo file riporta mini-esempi concreti per riconoscere e gestire i casi particolari d'esame direttamente dal tableau del simplesso.

---

## Caso 1: Soluzioni Ottime Multiple (Ottimi Multipli)

Si consideri il seguente tableau ottimo (MAX Z):

| Base | $Z$ | $x_1$ | $x_2$ | $s_1$ | $s_2$ | RHS |
|---|---|---|---|---|---|---|
| **$Z$** | 1 | 0 | 0 | 2 | 0 | **40** |
| **$x_1$** | 0 | 1 | 2 | 1 | -1 | 10 |
| **$s_2$** | 0 | 0 | 3 | -2 | 1 | 5 |

### Analisi
- Il tableau è **ottimo** poiché non vi sono coefficienti negativi in riga 0 ($0, 0, 2, 0 \ge 0$).
- La variabile non di base **$x_2$ ha coefficiente pari a $0$ in riga 0**.
- Questo indica la presenza di soluzioni ottime multiple. Possiamo trovare un altro vertice ottimo facendo entrare $x_2$ in base.

### Pivot Alternativo
- Entrante: $x_2$ (colonna pivot).
- Rapporti:
  - Riga $x_1$: $10 / 2 = 5$ (min)
  - Riga $s_2$: $5 / 3 = 1.67$ (min)
- Uscente: $s_2$ (pivot = 3).
- Eseguendo il pivot su $3$, il nuovo tableau ottimo sarà:

| Base | $Z$ | $x_1$ | $x_2$ | $s_1$ | $s_2$ | RHS |
|---|---|---|---|---|---|---|
| **$Z$** | 1 | 0 | 0 | 2 | 0 | **40** |
| **$x_1$** | 0 | 1 | 0 | 7/3 | -2/3 | 20/3 |
| **$x_2$** | 0 | 0 | 1 | -2/3 | 1/3 | 5/3 |

### Conclusione
Abbiamo due soluzioni di base ottime distinte:
- Soluzione A: $(x_1^*, x_2^*) = (10, 0)$ con $Z^* = 40$
- Soluzione B: $(x_1^*, x_2^*) = (20/3, 5/3)$ con $Z^* = 40$
La soluzione ottima del problema è data da tutti i punti giacenti sul segmento che le unisce:
$$
x^* = \lambda \begin{pmatrix} 10 \\ 0 \end{pmatrix} + (1-\lambda) \begin{pmatrix} 20/3 \\ 5/3 \end{pmatrix} \quad \text{con } \lambda \in [0, 1]
$$

---

## Caso 2: Funzione Obiettivo Illimitata (Illimitatezza)

Si consideri il seguente tableau intermedio:

| Base | $Z$ | $x_1$ | $x_2$ | $s_1$ | $s_2$ | RHS |
|---|---|---|---|---|---|---|
| **$Z$** | 1 | -3 | 2 | 0 | 4 | **20** |
| **$s_1$** | 0 | -2 | 1 | 1 | 0 | 6 |
| **$s_2$** | 0 | -1 | 3 | 0 | 1 | 4 |

### Analisi
- Entrante: $x_1$ (coefficiente più negativo in riga 0, pari a $-3$).
- Colonna pivot ($x_1$): contiene i coefficienti $-2$ e $-1$.
- **Test dei rapporti**: Poiché tutti i coefficienti nella colonna pivot sono non positivi ($\le 0$), **non è possibile scegliere alcuna variabile uscente** (i rapporti non sono calcolabili).

### Conclusione
Il valore ottimo della funzione obiettivo cresce all'infinito. Il problema è **illimitato** superiormente ($Z^* \to +\infty$).

---

## Caso 3: Degenerazione (Rapporto Minimo Multiplo)

Si consideri il seguente tableau iniziale:

| Base | $Z$ | $x_1$ | $x_2$ | $s_1$ | $s_2$ | RHS |
|---|---|---|---|---|---|---|
| **$Z$** | 1 | -4 | -2 | 0 | 0 | **0** |
| **$s_1$** | 0 | **2** | 1 | 1 | 0 | 8 |
| **$s_2$** | 0 | **2** | 3 | 0 | 1 | 8 |

### Analisi
- Entrante: $x_1$ (coefficiente $-4$ in riga 0).
- Rapporti:
  - Riga $s_1$: $8 / 2 = 4$
  - Riga $s_2$: $8 / 2 = 4$
- **Rapporti minimi identici**: C'è parità nel test dei rapporti minimi. Scegliamo arbitrariamente la riga $s_1$ per l'uscita (pivot = 2).

### Tableau Risultante
Eseguendo il pivot su 2 della riga $s_1$:

| Base | $Z$ | $x_1$ | $x_2$ | $s_1$ | $s_2$ | RHS |
|---|---|---|---|---|---|---|
| **$Z$** | 1 | 0 | 0 | 2 | 0 | **16** |
| **$x_1$** | 0 | 1 | 0.5 | 0.5 | 0 | 4 |
| **$s_2$** | 0 | 0 | 2 | -1 | 1 | **0** |

### Conclusione
Nel nuovo tableau, la variabile di base $s_2$ assume valore pari a $0$. La soluzione è **degenere**. L'iterazione successiva sul pivot non comporterà alcun incremento di $Z$ (che rimarrà a $16$).
