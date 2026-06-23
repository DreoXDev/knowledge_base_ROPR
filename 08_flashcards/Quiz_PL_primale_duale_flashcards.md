---
type: flashcards
topic: programmazione_lineare
status: consolidated
sources:
  - raw_assets/AAA - La bibbia di RO.pdf
reliability: non-ufficiale
---

# Flashcard — Quiz PL: Primale e Duale

---

## Q1: Primo controllo su un candidato primale
**D:** Qual è il primo controllo da fare su un vettore candidato per il primale?

**R:** Verificare la **dimensione** ($n$ componenti), poi la **non negatività** ($x \ge 0$), poi la **soddisfazione dei vincoli** ($Ax \le b$).

---

## Q2: Dualità forte
**D:** Quando posso affermare che un candidato primale $x$ e un candidato duale $y$ sono entrambi ottimi?

**R:** Quando sono **entrambi ammissibili** e hanno lo **stesso valore obiettivo**: $c^Tx = b^Ty$.

---

## Q3: Dualità debole
**D:** Cosa afferma la dualità debole?

**R:** Per qualsiasi $x$ primale ammissibile e $y$ duale ammissibile (max primale): $c^Tx \le b^Ty$. Il duale fornisce un bound superiore al primale.

---

## Q4: Dimensione del vettore duale
**D:** Quante componenti ha il vettore duale $y$ se il primale ha $m$ vincoli e $n$ variabili?

**R:** $m$ componenti (una per ogni vincolo del primale).

---

## Q5: Errore classico nei quiz primale/duale
**D:** Qual è l'errore più frequente nelle domande a risposta multipla su primale/duale?

**R:** Dichiarare un punto **ottimo** senza aver prima verificato che sia **ammissibile**. Non si può essere ottimi senza essere ammissibili.

---

## Q6: Vincoli del duale (forma standard)
**D:** Per il primale $\max c^Tx$ s.t. $Ax \le b$, $x \ge 0$, come si scrivono i vincoli del duale?

**R:** $\min b^Ty$ s.t. $A^Ty \ge c$, $y \ge 0$.

---

*Source:* `AAA - La bibbia di RO.pdf` (non ufficiale)
