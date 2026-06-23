# MC - Produzione e Stoccaggio Multi-periodo

## Quando Usarla
Per pianificare la produzione e i livelli di magazzino su più periodi di tempo consecutivi (es. mesi, settimane) per soddisfare una domanda nota riducendo al minimo i costi complessivi di produzione e stoccaggio.

## Variabili Tipiche
*   $x_t \ge 0$: Quantità prodotta nel periodo $t$.
*   $s_t \ge 0$: Livello di scorte (magazzino) alla fine del periodo $t$.
*   $y_t \in \{0, 1\}$: Decisione binaria di produzione nel periodo $t$ (se sono presenti costi fissi di setup).

## Modello Template
$$
\min \quad \sum_{t=1}^T (p_t x_t + h_t s_t + f_t y_t)
$$
$$
\text{s.t.} \quad s_t = s_{t-1} + x_t - d_t \quad \forall t = 1, \dots, T
$$
$$
L_t y_t \le x_t \le U_t y_t \quad \forall t = 1, \dots, T
$$
$$
s_t \le S \quad \forall t = 1, \dots, T
$$
$$
x_t \ge 0, \quad s_t \ge 0, \quad y_t \in \{0, 1\} \quad \forall t = 1, \dots, T
$$
con $s_0 = I_0$ (parametro scorta iniziale).

## Procedura da Esame
1.  Definire la sequenza temporale dei periodi $t = 1, \dots, T$.
2.  Dichiarare le variabili di produzione $x_t$ e magazzino $s_t$. Se ci sono costi fissi, introdurre le binarie $y_t$.
3.  Scrivere l'equazione di bilancio del magazzino per ogni periodo $t$.
4.  Inserire i vincoli di capacità produttiva e stoccaggio massimo.
5.  Impostare il valore noto di $s_0$.

## Mini Esempio
Orizzonte di 2 mesi. Domanda $d_1 = 20, d_2 = 30$. Scorta iniziale $s_0 = 5$.
*   Mese 1: $s_1 = 5 + x_1 - 20 \implies s_1 = x_1 - 15$
*   Mese 2: $s_2 = s_1 + x_2 - 30$

## Errori Comuni
*   Sbagliare l'indice temporale dell'equazione di bilancio (es. scrivere $s_t = s_{t+1} + \dots$).
*   Non considerare che le scorte non possono essere negative ($s_t \ge 0$), il che impedisce ritardi involontari nella consegna.

## Fonti
*   `modelli_PLI.pdf`, Sezione 2.5
