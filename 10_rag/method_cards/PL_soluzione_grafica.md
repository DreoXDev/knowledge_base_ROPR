---
type: method-card
topic: programmazione-lineare
status: draft
sources:
  - raw_assets/Programmazione Lineare/Ricerca Operativa - Introduzione a PL - 23-24.pdf
reliability: official
---

# Method Card — Risolvere graficamente un problema di PL

## Quando usarla
Quando il problema di PL presenta esattamente **due variabili decisionali** ($x_1, x_2$) e se ne richiede la risoluzione o l'analisi ottimale grafica.

## Procedura da esame
1. **Disegno delle rette associate**: Convertire ogni disuguaglianza del tipo $a_{i1}x_1 + a_{i2}x_2 \le b_i$ nell'equazione di una retta $a_{i1}x_1 + a_{i2}x_2 = b_i$ e tracciarla sul piano cartesiano individuando due punti di intersezione con gli assi.
2. **Determinazione dei semipiani ammissibili**: Scegliere un punto di prova (es. $(0,0)$) per stabilire la porzione di piano in cui la disequazione è soddisfatta.
3. **Costruzione della regione ammissibile**: Intersecare tutti i semipiani e i quadranti positivi ($x_1 \ge 0, x_2 \ge 0$) per ricavare il poliedro delle soluzioni ammissibili.
4. **Individuazione dei vertici**: Calcolare le coordinate dei vertici (punti estremi del poliedro) risolvendo i sistemi lineari a due variabili formati dalle rette dei vincoli che si intersecano.
5. **Rappresentazione della pendenza della funzione obiettivo**: Disegnare una linea di livello ponendo $c_1x_1 + c_2x_2 = 0$ (o un altro valore costante comodo).
6. **Ricerca dell'ottimo**: Traslare parallelamente la retta nella direzione del gradiente $\nabla Z = (c_1, c_2)^T$ per la massimizzazione, o nella direzione opposta per la minimizzazione. L'ultimo vertice o segmento toccato costituisce la soluzione ottima.
7. **Calcolo della soluzione**: Sostituire le coordinate del vertice ottimo nella funzione obiettivo per ricavare $Z^*$.

## Casi Speciali
- **Inammissibile**: I semipiani non si intersecano (regione vuota).
- **Illimitato**: La regione è aperta nella direzione di miglioramento della funzione obiettivo.
- **Infinite soluzioni**: La retta della funzione obiettivo è parallela al lato ottimale del poliedro.
