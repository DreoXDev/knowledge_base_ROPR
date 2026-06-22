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
  - tableau
  - esempio-svolto
  - interpretazione
---

# Esempio Svolto — Interpretazione e Operazioni su un Tableau Generico

Questo esempio mostra come leggere le informazioni fondamentali da un tableau del simplesso generico e come determinare algebricamente l'iterazione successiva.

## Il Tableau in Esame (MAX Z)

Si consideri il seguente tableau intermedio d'esame per un problema di massimizzazione:

| Base | $Z$ | $x_1$ | $x_2$ | $x_3$ | $s_1$ | $s_2$ | RHS |
|---|---|---|---|---|---|---|---|
| **$Z$** | 1 | -2 | 0 | 4 | 0 | 3 | **45** |
| **$s_1$** | 0 | 3 | 0 | 1 | 1 | -2 | 12 |
| **$x_2$** | 0 | 2 | 1 | -1 | 0 | 1 | 8 |

---

## 1. Lettura dello Stato Corrente

### Identificazione delle Variabili di Base e Fuori Base
- **Variabili di Base**: Sono le variabili associate alle colonne che compongono la matrice identità (riorganizzata). In questo caso:
  - $s_1$ (colonna con $1$ in riga 1, $0$ altrove)
  - $x_2$ (colonna con $1$ in riga 2, $0$ altrove)
- **Variabili Fuori Base**: Le restanti variabili, che vengono poste a zero:
  - $x_1 = 0$
  - $x_3 = 0$
  - $s_2 = 0$

### Valori delle Variabili e della Funzione Obiettivo
La soluzione di base corrente si legge direttamente dalla colonna **RHS**:
- $s_1 = 12$
- $x_2 = 8$
- $x_1 = 0, \ x_3 = 0, \ s_2 = 0$
- Valore corrente della funzione obiettivo: $Z = 45$.

---

## 2. Determinazione dell'Iterazione Successiva

### Scelta della Variabile Entrante
- Nel problema di massimo, cerchiamo il coefficiente più negativo nella riga 0.
- I coefficienti delle variabili in riga 0 sono:
  - $x_1$: **-2**
  - $x_2$: 0
  - $x_3$: 4
  - $s_1$: 0
  - $s_2$: 3
- Il valore minimo negativo è $-2$, associato alla variabile **$x_1$**.
- Quindi, la variabile **$x_1$ entra in base** (la colonna pivot è la colonna di $x_1$).

### Scelta della Variabile Uscente (Test del Rapporto Minimo)
- Calcoliamo i rapporti sulla colonna pivot ($x_1$) dividendo la colonna RHS per i soli coefficienti **strettamente positivi**:
  - Riga $s_1$: coeff. in colonna pivot = $3$ ($> 0$). Rapporto: $12 / 3 = 4$.
  - Riga $x_2$: coeff. in colonna pivot = $2$ ($> 0$). Rapporto: $8 / 2 = 4$.
- **Parità dei Rapporti**: Entrambe le righe hanno lo stesso rapporto minimo ($4$).
- Scegliamo arbitrariamente **$s_1$ come variabile uscente** (la riga pivot è la riga di $s_1$).
- **Nota**: Poiché c'è stata parità, la variabile $x_2$ diventerà pari a zero pur rimanendo in base al passo successivo (degenerazione).
- **Elemento Pivot**: $3$ (intersezione riga $s_1$, colonna $x_1$).

---

## 3. Esecuzione del Pivot algebrico

Normalizziamo la riga pivot dividendo la riga $s_1$ per $3$:
$$
R_1 \leftarrow R_1 / 3 \implies [0, 1, 0, 1/3, 1/3, -2/3, 4]
$$
Azzeriamo la colonna pivot $x_1$ sulle altre righe:
- Riga 0: $R_0 \leftarrow R_0 + 2 R_1$
  $$
  [-2 + 2(1), 0 + 0, 4 + 2(1/3), 0 + 2(1/3), 3 + 2(-2/3), 45 + 2(4)] = [0, 0, 14/3, 2/3, 5/3, 53]
  $$
- Riga 2: $R_2 \leftarrow R_2 - 2 R_1$
  $$
  [2 - 2(1), 1 - 0, -1 - 2(1/3), 0 - 2(1/3), 1 - 2(-2/3), 8 - 2(4)] = [0, 1, -5/3, -2/3, 7/3, 0]
  $$

### Nuovo Tableau Risultante

| Base | $Z$ | $x_1$ | $x_2$ | $x_3$ | $s_1$ | $s_2$ | RHS |
|---|---|---|---|---|---|---|---|
| **$Z$** | 1 | 0 | 0 | 14/3 | 2/3 | 5/3 | **53** |
| **$x_1$** | 0 | 1 | 0 | 1/3 | 1/3 | -2/3 | 4 |
| **$x_2$** | 0 | 0 | 1 | -5/3 | -2/3 | 7/3 | 0 |

### Analisi del Tableau Risultante
- Tutti i coefficienti in riga 0 sono non negativi ($0, 0, 14/3, 2/3, 5/3 \ge 0$).
- Il tableau è **ottimo**.
- Soluzione Ottima: $x_1^* = 4$, $x_2^* = 0$ (variabile di base degenere), $x_3^* = 0$, $s_1^* = 0$, $s_2^* = 0$ con valore ottimo **$Z^* = 53$**.
