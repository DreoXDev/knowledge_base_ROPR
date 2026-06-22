---
topic: Programmazione Lineare
type: esempio_svolto
source: lezione 3 completa.pdf
status: verificato
---

# Esempio Svolto — Due Fasi con Variabile Libera e Problema Illimitato

## Traccia Sintetica
Risolvere il seguente problema di PL:

$$
\min Z = -3x + 2y
$$

soggetto a:

$$
x + y \ge 1
$$

$$
-x + y \le 2
$$

$$
x - 3y \le 3
$$

$$
y \ge 0
$$

*Nota: La variabile $x$ è libera (non ha vincolo di segno esplicito).*

## Risoluzione

### 1. Gestione della Variabile Libera
Sostituiamo la variabile libera $x$ con $x = x_1 - x_2$ (con $x_1, x_2 \ge 0$).
Trasformiamo l'obiettivo in massimizzazione: $\max -Z = 3x_1 - 3x_2 - 2y$.

Il modello diventa:

$$
\max -Z = 3x_1 - 3x_2 - 2y
$$

soggetto a:

$$
x_1 - x_2 + y \ge 1
$$

$$
-x_1 + x_2 + y \le 2
$$

$$
x_1 - x_2 - 3y \le 3
$$

$$
x_1, x_2, y \ge 0
$$

### 2. Forma Standard Aumentata
Aggiungiamo:
- surplus $s_1$ e artificiale $x_a$ nel vincolo 1;
- slack $s_2$ nel vincolo 2;
- slack $s_3$ nel vincolo 3.

$$
x_1 - x_2 + y - s_1 + x_a = 1
$$

$$
-x_1 + x_2 + y + s_2 = 2
$$

$$
x_1 - x_2 - 3y + s_3 = 3
$$

con tutte le variabili $\ge 0$.

### 3. Fase 1 (Minimizzazione delle Artificiali)
Obiettivo: $\max -W = -x_a$.
La base iniziale ammissibile di Fase 1 è $x_a = 1, s_2 = 2, s_3 = 3$.
Risolvendo la Fase 1, si ottiene la soluzione ottima di Fase 1:

$$
(x_1, x_2, y, s_1, s_2, s_3, x_a) = (1, 0, 0, 0, 3, 2, 0)
$$

Poiché $W^* = 0$, il problema originale è ammissibile. Si cancella la colonna di $x_a$ e si passa alla Fase 2.

### 4. Fase 2 (Risoluzione del Problema Originale)
Ripristiniamo la funzione obiettivo originaria $\max -Z = 3x_1 - 3x_2 - 2y$.
Poiché $x_1$ è in base, azzeriamo il suo costo nella riga 0.
Durante il simplesso di Fase 2, si riscontra la variabile entrante (es. $x_2$ o $s_1$) per cui la colonna corrispondente nei vincoli non presenta alcun coefficiente positivo ($> 0$).

## Risultato Finale
Il problema è **illimitato** inferiormente ($Z^* \to -\infty$ nel problema di minimo originale, ovvero $-Z^* \to +\infty$ in massimizzazione).

## Risposta da Esame
La variabile libera $x$ viene sostituita con $x_1-x_2$. Al termine della Fase 1 si ottiene una soluzione di base ammissibile con $W^*=0$. In Fase 2, l'algoritmo rileva che tutti i coefficienti nei vincoli in corrispondenza della colonna della variabile entrante sono non positivi; pertanto il problema è illimitato.
