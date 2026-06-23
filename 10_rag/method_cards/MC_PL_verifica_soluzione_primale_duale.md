---
type: method-card
topic: programmazione_lineare
status: consolidated
sources:
  - raw_assets/AAA - La bibbia di RO.pdf
reliability: non-ufficiale
---

# Method Card: Verifica Soluzione Primale / Duale

## Quando Usarla

Quando la traccia presenta un vettore candidato e chiede di stabilire se è:
- soluzione ammissibile per il primale
- soluzione ottimale per il primale
- soluzione ammissibile per il duale
- soluzione ottimale per il duale

---

## Procedura

### Passo 1 — Identificare il tipo di vettore
- Vettore di dimensione $n$ (numero di variabili del primale) → candidato **primale**.
- Vettore di dimensione $m$ (numero di vincoli del primale) → candidato **duale**.

### Passo 2 — Verificare ammissibilità

**Candidato primale $x$**:
1. Non negatività: $x \ge 0$.
2. Soddisfa i vincoli primali: $Ax \le b$ (o $=$ o $\ge$ secondo la forma del problema).

**Candidato duale $y$** (per primale $\max c^Tx$ s.t. $Ax \le b$, $x \ge 0$):
1. Non negatività: $y \ge 0$.
2. Soddisfa i vincoli duali: $A^Ty \ge c$.

### Passo 3 — Calcolare il valore obiettivo
- Primale: $z_P = c^Tx$.
- Duale: $z_D = b^Ty$.

### Passo 4 — Applicare la dualità

**Dualità debole**: per qualsiasi $x$ ammissibile e $y$ ammissibile:
$$z_P = c^Tx \le b^Ty = z_D \quad \text{(per max primale)}$$

**Dualità forte**: se $z_P = z_D$ e entrambi ammissibili → **entrambi ottimi**.

---

## Controlli

| Controllo | Risposta positiva |
|---|---|
| Dimensione corretta? | Sì |
| Non negatività? | Sì |
| Tutti i vincoli soddisfatti? | Sì |
| Ammissibile | ✓ |
| Valore obiettivo $=$ bound duale? | Sì → ottimo |

---

## Uso della Dualità

- Se $x$ ammissibile e $y$ ammissibile con $c^Tx = b^Ty$ → entrambi ottimi (nessun simplesso necessario).
- Se $x$ non ammissibile → non può essere ottimo.
- Non fidarsi delle crocette negli screenshot: ricalcolare.

---

## Output da Esame

```
Il vettore x = (...) è [ammissibile / non ammissibile] per il primale
perché [soddisfa/viola il vincolo ...].
Valore obiettivo primale: z_P = c^T x = [...].

Il vettore y = (...) è [ammissibile / non ammissibile] per il duale
perché [soddisfa/viola il vincolo ...].
Valore obiettivo duale: z_D = b^T y = [...].

Per dualità forte: z_P [= / ≠] z_D → [ottimi / non ottimi].
```

## Collegamento Pattern

→ [[Quiz_PL_primale_duale]]
