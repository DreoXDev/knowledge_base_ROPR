---
type: solved-example
topic: programmazione-lineare
status: draft
sources:
  - raw_assets/Programmazione Lineare/Ricerca Operativa - Introduzione a PL - 23-24.pdf
reliability: official
---

# Esempio Svolto — Distribution Network (Flusso a Costo Minimo)

## Descrizione del Problema

Si desidera determinare la pianificazione ottima di spedizione di un prodotto da due fabbriche ($F1, F2$) a due magazzini di destinazione ($W1, W2$). La spedizione può avvenire direttamente o transitando attraverso un centro di distribuzione intermedio ($DC$).

I dati del problema includono:
- **Produzione delle fabbriche**: $F1$ produce 50 unità; $F2$ produce 40 unità.
- **Domanda dei magazzini**: $W1$ richiede 30 unità; $W2$ richiede 60 unità.
- **Centro di distribuzione ($DC$)**: È un nodo di transito puro (non consuma né produce).
- **Obiettivo**: Minimizzare il costo totale di spedizione lungo i vari collegamenti stradali (archi della rete).

## Modello Matematico

### Variabili Decisionali
Il problema si modella definendo una variabile decisionale continuo-positiva per ogni arco orientato $(i,j)$ presente nella rete, indicante la quantità di flusso inviata:
- $x_{F1, F2}$: Flusso inviato da $F1$ a $F2$
- $x_{F1, W1}$: Flusso inviato da $F1$ a $W1$
- $x_{F1, DC}$: Flusso inviato da $F1$ a $DC$
- $x_{F2, DC}$: Flusso inviato da $F2$ a $DC$
- $x_{DC, W2}$: Flusso inviato da $DC$ a $W2$
- $x_{W1, W2}$: Flusso inviato da $W1$ a $W2$
- $x_{W2, W1}$: Flusso inviato da $W2$ a $W1$

### Funzione Obiettivo
Minimizzare il costo totale di trasporto ($C_{ij}$ sono i costi unitari di spedizione su ciascun arco):

$$
\min Z = \sum_{(i,j)} C_{ij} x_{ij}
$$

### Vincoli

#### 1. Capacità degli Archi
La quantità di prodotto inviata su ciascun collegamento non può superare la capacità massima dell'arco $u_{ij}$ (se specificata):

$$
x_{F1, F2} \le 10
$$

$$
x_{DC, W2} \le 80
$$

E in generale $x_{ij} \le u_{ij}$ per tutti gli archi capacitati.

#### 2. Conservazione del Flusso (Bilancio nei Nodi)
Per ogni nodo $k$ della rete, la somma dei flussi entranti più la produzione netta (o meno la domanda netta) deve essere uguale alla somma dei flussi uscenti.

- **Nodi di Sorgente (Fabbriche)**:
  - Fabbrica $F1$ (produzione = 50):

$$
x_{F1, F2} + x_{F1, W1} + x_{F1, DC} = 50
$$

  - Fabbrica $F2$ (produzione = 40, ma riceve da $F1$):

$$
x_{F2, DC} - x_{F1, F2} = 40 \implies x_{F1, F2} + 40 = x_{F2, DC}
$$

- **Nodi di Transito (Centro di Distribuzione)**:
  - Centro $DC$ (domanda/offerta netta = 0):

$$
x_{F1, DC} + x_{F2, DC} = x_{DC, W2}
$$

- **Nodi di Destinazione (Magazzini)**:
  - Magazzino $W1$ (domanda = 30):

$$
x_{F1, W1} + x_{W2, W1} - x_{W1, W2} = 30
$$

  - Magazzino $W2$ (domanda = 60):

$$
x_{DC, W2} + x_{W1, W2} - x_{W2, W1} = 60
$$

#### 3. Non Negatività

$$
x_{ij} \ge 0 \qquad \forall (i,j)
$$

---

> [!CAUTION]
> Nella pagina finale del PDF originale alcune formule possono risultare degradate a causa dell'estrazione automatica del testo delle slide. Si consiglia di confrontare sempre con il diagramma grafico della rete per verificare la presenza di vincoli di capacità impliciti e la correttezza dei coefficienti di costo.

#ropr #programmazione-lineare #esempio #flusso-costo-minimo
