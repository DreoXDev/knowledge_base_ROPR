---
type: method_card
topic: programmazione_lineare_intera
status: active
sources: [BB PLI.pdf]
reliability: official
---

# Method Card: Branch and Bound per PLIM

## Quando Usarlo
Problemi di ottimizzazione lineare in cui una parte delle variabili ($x_j$) è vincolata a assumere valori interi/binari e un'altra parte ($y_k$) è continua (Programmazione Lineare Intera Mista).

## Procedura d'Esame

1. **Rilassamento Lineare Continuo**:
   * Risolvere il rilassamento LP continuo (tutte le variabili, incluse quelle intere, sono trattate come continue).
2. **Controllo Interezza**:
   * Verificare il valore delle sole variabili vincolate ad essere intere ($x_j$).
   * Se tutte le $x_j$ sono intere, la soluzione è **intera ammissibile** per il PLIM, indipendentemente dal fatto che le variabili continue ($y_k$) assumano valori frazionari.
   * Se almeno una variabile intera $x_j$ assume valore frazionario $v$, eseguire il branching.
3. **Ramificazione (Branching)**:
   * Scegliere una variabile intera frazionaria $x_j$.
   * Generare due rami aggiungendo rispettivamente i vincoli:
     $$x_j \le \lfloor v \rfloor$$
     e
     $$x_j \ge \lceil v \rceil$$
   * **IMPORTANTE**: Non ramificare mai sulle variabili continue.
4. **Calcolo dei Bound**:
   * Risolvere i rilassamenti continui nei nodi figli.
   * **IMPORTANTE**: Non arrotondare mai il bound frazionario del rilassamento continuo. Nel PLIM, il valore ottimo può essere frazionario.
5. **Chiusura dei Nodi**:
   * Chiudere per *inammissibilità* se il rilassamento è inammissibile.
   * Chiudere per *ottimalità intera* se tutte le $x_j$ sono intere (aggiornando l'incumbent $Z_I$ se migliore).
   * Chiudere per *dominanza* se il bound del rilassamento è peggiore o uguale all'incumbent $Z_I$.
