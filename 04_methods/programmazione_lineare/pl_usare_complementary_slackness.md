---
materia: ROPR
area: Programmazione Lineare
tipo: metodo
fonte: Ricerca Operativa - Teoria della Dualità.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - dualita
  - complementary-slackness
  - scarti-complementari
  - ottimalita
  - method-card
---

# METHOD CARD — Utilizzo delle Condizioni di Complementary Slackness

## Quando usarla

Usare questa card per verificare se una data soluzione primale $\mathbf{x}$ è ottima, oppure per determinare la corrispondente soluzione ottima duale $\mathbf{y}^*$ senza risolvere graficamente o con il simplesso il problema duale.

## Condizioni Matematiche (Caso Standard)

Dati il primale (MAX standard) e il duale (MIN standard):
- Vincoli primali: $\sum_{j=1}^{n} a_{ij}x_j \le b_i$ con slack $s_i = b_i - \sum_{j=1}^{n} a_{ij}x_j \ge 0$
- Vincoli duali: $\sum_{i=1}^{m} a_{ij}y_i \ge c_j$ con surplus $v_j = \sum_{i=1}^{m} a_{ij}y_i - c_j \ge 0$

Le condizioni di complementarità (Complementary Slackness) stabiliscono che:
1. $$y_i \cdot s_i = 0 \qquad \forall i = 1, \dots, m$$
2. $$x_j \cdot v_j = 0 \qquad \forall j = 1, \dots, n$$

### Significato Logico
- Se una risorsa primale non è completamente consumata (slack $s_i > 0$), il suo valore marginale è nullo (variabile duale $y_i = 0$).
- Se una variabile primale è attiva a livello positivo ($x_j > 0$), il corrispondente vincolo duale deve essere soddisfatto all'uguaglianza (surplus $v_j = 0$).

---

## Procedura Operativa Passo-Passo

### 1. Scrivere i Modelli Primale e Duale
Formulare chiaramente entrambi i problemi associando le variabili duali $y_i$ ai vincoli primali.

### 2. Sostituire la Soluzione Primale $\mathbf{x}$ nei Vincoli Primali
- Calcolare i valori di slack $s_i = b_i - A_i x$ per ogni vincolo primale $i$.
- Identificare quali vincoli primali sono **inattivi** ($s_i > 0$) e quali sono **attivi** ($s_i = 0$).

### 3. Applicare le Condizioni ai Vincoli Primali
- Per ogni vincolo primale inattivo ($s_i > 0$), imporre che la corrispondente variabile duale sia nulla:
  $$s_i > 0 \implies y_i = 0$$

### 4. Applicare le Condizioni alle Variabili Primali
- Per ogni variabile primale strettamente positiva ($x_j > 0$), imporre che il corrispondente vincolo duale sia attivo (valga come uguaglianza):
  $$x_j > 0 \implies \sum_{i=1}^{m} a_{ij}y_i = c_j$$

### 5. Risolvere il Sistema Lineare Duale
- Costruire il sistema composto dalle equazioni ricavate al punto 3 ($y_i = 0$) e al punto 4 ($\sum a_{ij}y_i = c_j$).
- Risolvere il sistema per determinare il vettore delle variabili duali candidate $\mathbf{y}$.

### 6. Verificare l'Ammissibilità della Soluzione Duale $\mathbf{y}$
- **Verifica del segno**: Controllare che tutte le componenti $y_i$ rispettino i vincoli di segno del problema duale (es. $y_i \ge 0$).
- **Verifica dei vincoli**: Controllare che $\mathbf{y}$ soddisfi tutti i vincoli duali (anche quelli corrispondenti a variabili primali $x_j = 0$).

### 7. Trarre le Conclusioni
- Se la soluzione $\mathbf{y}$ trovata è **ammissibile** per il duale, allora per il teorema della dualità debole/forte sia $\mathbf{x}$ che $\mathbf{y}$ sono **soluzioni ottime** dei rispettivi problemi.
- Se il sistema non ha soluzioni o la soluzione $\mathbf{y}$ viola l'ammissibilità duale, la soluzione primale $\mathbf{x}$ **non è ottima**.
