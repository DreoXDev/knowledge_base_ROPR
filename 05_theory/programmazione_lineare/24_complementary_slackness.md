---
materia: ROPR
area: Programmazione Lineare
tipo: teoria
fonte: Ricerca Operativa - Teoria della Dualità.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - simplesso
  - dualita
  - complementary-slackness
  - scarti-complementari
---

# Soluzioni complementari e complementary slackness

La complementary slackness (o condizioni di complementarità degli scarti) è un teorema cardine che stabilisce una connessione precisa tra le variabili di un problema primale e le variabili del corrispondente problema duale.

## 1. Soluzioni Complementari dal Tableau del Simplesso

Durante l'esecuzione del simplesso sul problema primale:
- A ogni iterazione (e quindi a ogni soluzione di base primale $\mathbf{x}$) corrisponde in modo biunivoco una **soluzione complementare duale** $\mathbf{y}$.
- Le componenti di questa soluzione duale $\mathbf{y}$ si leggono nella **riga 0 del tableau** sotto le colonne associate alle variabili di slack ($s_i$) del primale.
- **Proprietà**: Per ogni coppia di soluzioni complementari (anche non ottime), vale l'uguaglianza dei valori delle funzioni obiettivo:
  $$
  Z = W \implies \mathbf{c}\mathbf{x} = \mathbf{y}\mathbf{b}
  $$
- **Ammissibilità e Ottimo**:
  - Se $\mathbf{x}$ non è ottima per il primale, la soluzione duale complementare $\mathbf{y}$ non soddisfa tutti i vincoli duali (è **non ammissibile** per il duale).
  - Nel momento in cui il simplesso raggiunge l'ottimo, i coefficienti in riga 0 diventano tutti $\ge 0$. Ciò significa che la soluzione duale complementare $\mathbf{y}^*$ diventa **ammissibile** per il duale.
  - Poiché $\mathbf{y}^*$ è ammissibile e $\mathbf{c}\mathbf{x}^* = \mathbf{y}^*\mathbf{b}$, per il criterio pratico di ottimalità entrambe le soluzioni sono ottime.

---

## 2. Il Teorema degli Scarti Complementari (Complementary Slackness)

Siano $\mathbf{x}$ una soluzione ammissibile primale e $\mathbf{y}$ una soluzione ammissibile duale.

> **Teorema**: $\mathbf{x}$ e $\mathbf{y}$ sono soluzioni ottime per i rispettivi problemi se e solo se valgono le seguenti relazioni per ogni risorsa $i$ e attività $j$:
> 1. $$ y_i \cdot (b_i - \sum_{j=1}^n a_{ij}x_j) = 0 \qquad \forall i=1,\dots,m $$
> 2. $$ x_j \cdot (\sum_{i=1}^m a_{ij}y_i - c_j) = 0 \qquad \forall j=1,\dots,n $$

### Significato Logico-Geometrico
Introducendo le variabili di slack primali $s_i = b_i - \sum a_{ij}x_j \ge 0$ e le slack duali $e_j = \sum a_{ij}y_i - c_j \ge 0$:
- **Equazione 1**: $y_i \cdot s_i = 0 \implies$ se il vincolo primale $i$ non è saturo ($s_i > 0$), la corrispondente variabile duale deve essere nulla ($y_i = 0$). Se la variabile duale è positiva ($y_i > 0$), il vincolo primale deve essere saturo ($s_i = 0$).
- **Equazione 2**: $x_j \cdot e_j = 0 \implies$ se l'attività primale è attiva ($x_j > 0$), il corrispondente vincolo duale deve essere saturo con l'uguaglianza ($e_j = 0$). Se il vincolo duale non è saturo ($e_j > 0$), l'attività primale deve essere spenta ($x_j = 0$).

---

## 3. Procedura Operativa per gli Esercizi d'Esame

Quando viene fornita una soluzione primale $\mathbf{x}$ e viene chiesto di verificare l'ottimalità o determinare la soluzione duale ottima $\mathbf{y}^*$:

1. **Verificare l'ammissibilità di $\mathbf{x}$** sostituendola nei vincoli primali.
2. **Calcolare gli scarti primali** $s_i = b_i - A_i x$.
3. **Applicare le condizioni di complementarità**:
   - Per ciascun vincolo in cui $s_i > 0$, imporre la variabile duale corrispondente $y_i = 0$.
   - Per ciascuna variabile primale $x_j > 0$, imporre che il corrispondente vincolo duale sia saturo: $\sum_{i=1}^m a_{ij}y_i = c_j$.
4. **Risolvere il sistema lineare** nelle sole variabili duali rimanenti.
5. **Verificare l'ammissibilità della soluzione duale $\mathbf{y}$** ottenuta (controllare il segno delle variabili e che soddisfi tutti i vincoli duali non usati nel sistema).
6. Se la soluzione duale è ammissibile, allora per il teorema degli scarti complementari la coppia $(\mathbf{x}, \mathbf{y})$ è ottima.
