---
materia: ROPR
area: Programmazione Lineare
tipo: esempio-svolto
fonte: esercitazione1_complete.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - formulazione
  - produzione
  - esempio-svolto
---

# Esempio Svolto — Pianificazione della Produzione (TOOL.spa)

Questo esempio illustra la formulazione e l'analisi di un problema di pianificazione della produzione a due variabili decisionali.

## Testo del Problema

La TOOL.spa produce chiavi inglesi e pinze in acciaio speciale. Il processo prevede l'uso di acciaio, ore-macchina per la lavorazione e ore-macchina per l'assemblaggio. I requisiti unitari di risorsa, la disponibilità e i profitti sono mostrati nella tabella seguente:

| Risorsa / Prodotto | Chiavi (migliaia) | Pinze (migliaia) | Disponibilità Risorsa |
|---|---|---|---|
| Acciaio speciale (t) | $1.5$ | $1.0$ | $27$ t |
| Lavorazione (ore) | $1.0$ | $1.0$ | $21$ ore |
| Assemblaggio (ore) | $0.3$ | $0.5$ | $9$ ore |
| **Profilo Unitario (€)** | **$130$** | **$100$** | |

Inoltre, il dipartimento vendite indica che la richiesta massima di mercato è pari a:
- $15$ mila chiavi inglesi.
- $16$ mila pinze.

Si vuole determinare il piano di produzione ottimo per massimizzare il profitto totale.

---

## Formulazione Matematica

### 1. Variabili decisionali
- $x_c$: quantità di chiavi inglesi prodotte (espressa in migliaia di unità).
- $x_p$: quantità di pinze prodotte (espressa in migliaia di unità).

### 2. Funzione obiettivo
Massimizzare il profitto complessivo (espresso in migliaia di euro):
$$
\max Z = 130x_c + 100x_p
$$

### 3. Vincoli
Raggruppati per tipologia:
- **Vincoli sulle risorse (capacità)**:
  - Consumo acciaio:
    $$
    1.5x_c + x_p \le 27 \qquad \text{(acciaio disponibile)}
    $$
  - Tempo lavorazione:
    $$
    x_c + x_p \le 21 \qquad \text{(ore lavorazione)}
    $$
  - Tempo assemblaggio:
    $$
    0.3x_c + 0.5x_p \le 9 \qquad \text{(ore assemblaggio)}
    $$
- **Vincoli di mercato (domanda massima)**:
  - Domanda chiavi:
    $$
    x_c \le 15
    $$
  - Domanda pinze:
    $$
    x_p \le 16
    $$

### 4. Dominio
Le variabili sono continue e non negative:
$$
x_c, x_p \ge 0
$$

---

## Soluzione Ottima e Analisi

La soluzione ottima del problema (ricavabile per via grafica o con il simplesso) è:
- **Produzione ottima**:
  - $x_c^* = 12$ (cioè 12.000 chiavi).
  - $x_p^* = 9$ (cioè 9.000 pinze).
- **Profitto ottimo**:
  - $Z^* = 2460$ (cioè € 2.460.000).

### Interpretazione delle Risorse (Scarti)
Sostituendo la soluzione ottima nei vincoli ricaviamo lo stato delle risorse:
1. **Acciaio**: $1.5(12) + (9) = 18 + 9 = 27$ t (Risorsa satura, slack $s_1 = 0$).
2. **Lavorazione**: $(12) + (9) = 21$ ore (Risorsa satura, slack $s_2 = 0$).
3. **Assemblaggio**: $0.3(12) + 0.5(9) = 3.6 + 4.5 = 8.1$ ore su $9$ disponibili (Risorsa non satura, slack $s_3 = 0.9$ ore).
4. **Domanda chiavi**: $12 < 15$ (Limite di mercato non saturo).
5. **Domanda pinze**: $9 < 16$ (Limite di mercato non saturo).

**Conclusione**: Acciaio e ore lavorazione sono i colli di bottiglia (risorse critiche) con prezzo ombra positivo. Le ore assemblaggio e la domanda massima di mercato non vincolano la soluzione all'ottimo (prezzo ombra nullo).
