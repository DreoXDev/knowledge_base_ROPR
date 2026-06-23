---
type: method-card
topic: metaeuristiche
status: consolidated
sources:
  - raw_assets/Domande aperte RO.pdf
reliability: non-ufficiale
---

# Method Card: Simulated Annealing

## Quando Usarla

Quando la domanda chiede di descrivere il **Simulated Annealing** (SA), il ruolo della temperatura, il bilanciamento exploration/exploitation, o i criteri di arresto.

---

## Struttura dell'Algoritmo

1. **Inizializzazione**: soluzione corrente $x_c$, temperatura $T = T_0$ (alta).
2. **Estrazione**: campionare casualmente $x_n \in N(x_c)$ (vicinato).
3. **Valutazione**: $\Delta f = f(x_n) - f(x_c)$.
4. **Accettazione**:
   - **Mossa migliorativa** (per min: $\Delta f < 0$): accetta sempre.
   - **Mossa peggiorativa** (per min: $\Delta f \ge 0$): accetta con probabilità:
$$p = \exp\!\left(-\frac{\Delta f}{T}\right)$$
5. **Raffreddamento**: $T \leftarrow \alpha T$ con $0 < \alpha < 1$ (es. ogni $k$ iterazioni).
6. Ripetere fino al criterio di arresto.

> **Per massimizzazione**: $\Delta f = f(x_n) - f(x_c)$, mossa peggiorativa se $\Delta f < 0$, probabilità $p = \exp(\Delta f / T)$.

---

## Temperatura e Exploration/Exploitation

| Temperatura $T$ | Effetto |
|---|---|
| Alta ($T \to \infty$) | $p \to 1$: quasi ogni mossa accettata → **exploration** |
| Bassa ($T \to 0$) | $p \to 0$: solo miglioramenti accettati → **exploitation** |

Il SA inizia con alta temperatura (esplorazione globale) e raffredda progressivamente (sfruttamento locale).

---

## Criteri di Arresto

- $T < T_{\min}$ (temperatura minima raggiunta).
- Numero massimo di iterazioni.
- Numero massimo di iterazioni senza miglioramento della best.
- Nessuna mossa accettata per molte iterazioni consecutive.

---

## Output da Esame

```
Simulated Annealing è ispirato al raffreddamento dei metalli.
Parte da una soluzione iniziale e propone mosse casuali nel vicinato.

Accettazione:
  - mossa migliorativa: sempre accettata
  - mossa peggiorativa (min): accettata con p = exp(-Df/T)

Temperatura T alta => exploration (quasi tutto accettato)
Temperatura T bassa => exploitation (solo miglioramenti)

Raffreddamento: T <- alpha*T ad ogni iterazione.

Criteri di arresto: T < T_min, max iter, max iter senza miglioramento.
Non garantisce l'ottimo globale.
```

---

## Collegamento Pattern

→ [[Domande_aperte_metaeuristiche]]
→ [[Metaeuristiche_domande_aperte]]
