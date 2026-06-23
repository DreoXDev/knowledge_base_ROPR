---
type: solved_example
topic: programmazione_lineare_intera
status: active
sources: [BB PLI.pdf]
reliability: official
---

# Esempio Svolto: Branch and Bound su PLIM

Esercizio d'esame completo per la risoluzione di un problema di Programmazione Lineare Intera Mista (PLIM) tramite l'albero di Branch and Bound.

---

## Testo del Problema

Risolvere il seguente problema PLIM:

$$
\begin{aligned}
\max \quad & z = 4x_1 - 2x_2 + 7x_3 - x_4 \\
\text{s.t.} \quad & x_1, x_2, x_3 \in \mathbb{Z} \quad (\text{variabili intere}) \\
& x_4 \in \mathbb{R} \quad (\text{variabile continua}) \\
& \text{[Vincoli funzionali del poliedro]}
\end{aligned}
$$

---

## Risoluzione Passo-Passo

Inizializziamo l'incumbent: $Z_I = -\infty$.

### Nodo $P_0$ (Radice)
Risolvendo il rilassamento continuo LP iniziale, si ottiene:
- Soluzione rilassata: $x^{(0)} = \left(\frac{5}{4}, \frac{3}{2}, \frac{7}{4}, 0\right) = (1.25, 1.5, 1.75, 0)$
- Valore di obiettivo: $z(P_0) = 14.5$

*Verifica interezza*: Le variabili $x_1, x_2, x_3$ devono essere intere, ma sono tutte frazionarie. Scegliamo di ramificare sulla prima variabile frazionaria: $x_1$.
Generiamo i vincoli:
- Ramo sinistro: $x_1 \le \lfloor 1.25 \rfloor \implies x_1 \le 1$ (Nodo $P_1$)
- Ramo destro: $x_1 \ge \lceil 1.25 \rceil \implies x_1 \ge 2$ (Nodo $P_2$)

---

### Nodo $P_1$ (Ramo $x_1 \le 1$)
Risolvendo il rilassamento continuo con il vincolo aggiuntivo $x_1 \le 1$:
- Soluzione rilassata: $x^{(1)} = \left(1, \frac{6}{5}, \frac{9}{5}, 0\right) = (1, 1.2, 1.8, 0)$
- Valore di obiettivo: $z(P_1) = 14.2$

*Verifica interezza*: $x_1 = 1$ è intero, ma $x_2 = 1.2$ e $x_3 = 1.8$ sono frazionarie. Il nodo resta aperto.
Ramifichiamo su $x_2$:
- Ramo sinistro: $x_2 \le 1$ (Nodo $P_3$)
- Ramo destro: $x_2 \ge 2$ (Nodo $P_4$)

---

### Nodo $P_2$ (Ramo $x_1 \ge 2$)
Risolvendo il rilassamento continuo con il vincolo aggiuntivo $x_1 \ge 2$:
- Il sotto-problema risulta **inammissibile** (non ci sono soluzioni che soddisfano i vincoli).
- **Stato**: Nodo potato per inammissibilità e chiuso.

---

### Nodo $P_3$ (Ramo $x_1 \le 1, x_2 \le 1$)
Risolvendo il rilassamento continuo con i vincoli aggiuntivi:
- Soluzione rilassata: $x^{(3)} = \left(\frac{5}{6}, 1, \frac{11}{5}, 0\right) \approx (0.83, 1, 2.2, 0)$
- Valore di obiettivo: $z(P_3) \approx 14.17$

*Verifica interezza*: $x_2 = 1$ è intero, ma $x_1 = 0.83$ e $x_3 = 2.2$ sono frazionarie. Il nodo resta aperto.
Ramifichiamo su $x_1$:
- Ramo sinistro: $x_1 \le 0$ (Nodo $P_5$)
- Ramo destro: $x_1 \ge 1$ (Nodo $P_6$)

---

### Nodo $P_4$ (Ramo $x_1 \le 1, x_2 \ge 2$)
Risolvendo il rilassamento continuo con i vincoli aggiuntivi:
- Soluzione rilassata: $x^{(4)} = \left(\frac{5}{6}, 2, \frac{11}{6}, 0\right) \approx (0.83, 2, 1.83, 0)$
- Valore di obiettivo: $z(P_4) \approx 12.17$

Il nodo resta temporaneamente aperto con bound $UB = 12.17$.

---

### Nodo $P_5$ (Ramo $x_1 \le 0, x_2 \le 1 \implies x_1 = 0, x_2 \le 1$)
Risolvendo il rilassamento continuo con i vincoli aggiuntivi:
- Soluzione rilassata: $x^{(5)} = \left(0, 0, 2, \frac{1}{2}\right)$
- Valore di obiettivo: $z(P_5) = 13.5$

*Verifica interezza*:
- $x_1 = 0$ (Intera - OK)
- $x_2 = 0$ (Intera - OK)
- $x_3 = 2$ (Intera - OK)
- $x_4 = 0.5$ (Continua - OK, non vincolata a essere intera)

La soluzione è **intera ammissibile** per il problema PLIM.
Poiché $z(P_5) = 13.5 > Z_I = -\infty$, aggiorniamo l'incumbent:
$$
Z_I = 13.5
$$
**Stato**: Nodo chiuso per ottimalità intera.

---

### Nodo $P_6$ (Ramo $x_1 \ge 1, x_2 \le 1 \implies x_1 = 1, x_2 \le 1$)
Risolvendo il rilassamento continuo:
- Il sotto-problema risulta **inammissibile**.
- **Stato**: Nodo chiuso per inammissibilità.

---

### Esame dei Nodi Aperti e Potatura per Dominanza
L'unico nodo rimasto aperto è $P_4$ con bound $UB(P_4) \approx 12.17$.
Confrontiamo il bound con l'incumbent $Z_I$:

$$
UB(P_4) \approx 12.17 \le Z_I = 13.5
$$

Il nodo $P_4$ viene **potato per dominanza** e chiuso, in quanto non può produrre soluzioni migliori dell'incumbent corrente.

---

## Soluzione Ottima

Tutti i nodi dell'albero sono stati chiusi o potati. La soluzione ottima del problema PLIM è:

$$
x^* = \left(0, 0, 2, \frac{1}{2}\right)
$$

$$
z^* = 13.5
$$

> [!NOTE]
> La variabile continua $x_4^* = 0.5$ assume valore frazionario nella soluzione ottima, il che è perfettamente ammissibile. Inoltre, si noti che non è stato effettuato alcun arrotondamento sul bound di $13.5$, che rappresenta il valore esatto dell'ottimo intero misto.
