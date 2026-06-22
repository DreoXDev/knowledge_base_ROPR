---
materia: ROPR
area: Programmazione Lineare
tipo: metodo
fonte: Esercitazione 2 PL.pdf, Ricerca Operativa - Introduzione a PL - 23-24.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - soluzione-grafica
  - metodo
  - method-card
---

# METHOD CARD — Risoluzione Grafica di Problemi di PL

## Quando usarla

Usare questa card quando il problema di Programmazione Lineare presenta esattamente **due variabili decisionali** ($x, y$ oppure $x_1, x_2$) e se ne richiede la risoluzione o l'analisi ottima per via grafica.

## Procedura Operativa Passo-Passo

1. **Tracciare le rette dei vincoli**:
   - Trasformare ciascuna disuguaglianza $a_{i1}x + a_{i2}y \le b_i$ in un'equazione di uguaglianza $a_{i1}x + a_{i2}y = b_i$.
   - Individuare due punti comodi (es. le intersezioni con gli assi cartesiani) e tracciare la retta sul piano cartesiano.
2. **Determinare i semispazi di ammissibilità**:
   - Scegliere un punto di prova non giacente sulla retta (in genere l'origine $(0,0)$).
   - Se la disuguaglianza è soddisfatta nel punto, la regione ammissibile per quel vincolo contiene il punto; in caso contrario, si trova sull'altro lato della retta.
3. **Individuare la Regione Ammissibile (Poliedro)**:
   - Trovare l'intersezione di tutti i semispazi di ammissibilità definiti dai vincoli funzionali e dai vincoli di non negatività ($x \ge 0, y \ge 0$).
4. **Calcolare i Vertici**:
   - Identificare i punti di intersezione che definiscono la frontiera della regione ammissibile.
   - Trovare le coordinate esatte risolvendo i sistemi lineari a due variabili formati dalle rette che si intersecano in corrispondenza di ciascun vertice.
5. **Rappresentare la direzione della Funzione Obiettivo**:
   - Tracciare la retta di livello della funzione obiettivo ponendo $Z = c_1x + c_2y = 0$ (o pari a una costante comoda).
   - Determinare la direzione di miglioramento tracciando il vettore gradiente $\nabla Z = (c_1, c_2)^T$.
6. **Ricercare l'Ottimo**:
   - Traslare parallelamente la retta di livello nella direzione del gradiente (per massimizzazione) o nella direzione opposta (per minimizzazione).
   - L'ultimo punto o segmento della regione ammissibile toccato dalla retta in transizione identifica la soluzione ottima.
7. **Calcolare il valore ottimo $Z^*$**:
   - Sostituire le coordinate del vertice ottimo nella funzione obiettivo.

---

## Esempio Applicativo d'Esame

### Modello
$$
\max Z = 40x + 50y
$$
soggetto a:
$$
\begin{aligned}
(1) \quad x + 2y &\le 40 \\
(2) \quad 4x + 3y &\le 120
\end{aligned}
$$
con $x, y \ge 0$.

### Risoluzione
1. **Rette associate ai vincoli**:
   - Per vincolo (1): $x + 2y = 40$. Punti di intersezione: $(40, 0)$ e $(0, 20)$.
   - Per vincolo (2): $4x + 3y = 120$. Punti di intersezione: $(30, 0)$ e $(0, 40)$.
2. **Determinazione dei vertici del poliedro**:
   - $A = (0, 0)$
   - $B = (30, 0)$ (intersezione del vincolo 2 con l'asse $x$)
   - $C$: intersezione tra vincolo (1) e vincolo (2). Risolvendo il sistema:
     $$
     \begin{cases}
     x + 2y = 40 \implies x = 40 - 2y \\
     4(40 - 2y) + 3y = 120 \implies 160 - 5y = 120 \implies y = 8
     \end{cases}
     \implies x = 40 - 16 = 24
     $$
     Quindi $C = (24, 8)$.
   - $D = (0, 20)$ (intersezione del vincolo 1 con l'asse $y$).

3. **Valutazione della funzione obiettivo nei vertici**:
   - $Z(A) = 0$
   - $Z(B) = 40(30) + 50(0) = 1200$
   - $Z(C) = 40(24) + 50(8) = 960 + 400 = 1360$ (Massimo)
   - $Z(D) = 40(0) + 50(20) = 1000$

### Risultato Ottimo
La soluzione ottima è situata al vertice $C = (24, 8)$ con valore ottimo della funzione obiettivo $Z^* = 1360$.
