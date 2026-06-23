---
type: theory-note
topic: programmazione_non_lineare
status: consolidated
sources:
  - raw_assets/Domande aperte RO.pdf
reliability: non-ufficiale
---

# PNL — Domande Aperte sulle Condizioni KKT

Fonte: `raw_assets/Domande aperte RO.pdf` (rielaborato con validazione sulle fonti ufficiali)
Area: Programmazione Non Lineare
Prerequisiti: calcolo multivariabile, moltiplicatori di Lagrange, vincoli

---

## Condizioni KKT (D10)

**Domanda**: Quali sono le condizioni KKT? A cosa servono?

---

### Forma del Problema

$$
\min f(x) \quad \text{(o } \max\text{)}
$$

soggetto a:
$$
g_i(x) = 0, \quad i = 1, \dots, m \quad \text{(vincoli di uguaglianza)}
$$
$$
h_j(x) \le 0, \quad j = 1, \dots, p \quad \text{(vincoli di disuguaglianza in forma standard)}
$$

---

### Lagrangiana

$$
L(x, \lambda, \mu) = f(x) + \sum_{i=1}^{m} \lambda_i g_i(x) + \sum_{j=1}^{p} \mu_j h_j(x)
$$

---

### Le Quattro Condizioni KKT

**1. Stazionarietà**:
$$
\nabla_x L = \nabla f(x^*) + \sum_{i=1}^{m} \lambda_i \nabla g_i(x^*) + \sum_{j=1}^{p} \mu_j \nabla h_j(x^*) = 0
$$

**2. Ammissibilità primale**:
$$
g_i(x^*) = 0 \quad \forall i, \qquad h_j(x^*) \le 0 \quad \forall j
$$

**3. Ammissibilità duale (segno dei moltiplicatori)**:
$$
\mu_j \ge 0 \quad \forall j \quad \text{(per minimizzazione)}
$$
$$
\mu_j \le 0 \quad \forall j \quad \text{(per massimizzazione)}
$$

> Per i moltiplicatori di uguaglianza $\lambda_i$ non c'è vincolo di segno.

**4. Complementarità**:
$$
\mu_j h_j(x^*) = 0 \quad \forall j
$$

Ovvero: o il vincolo $j$ è **attivo** ($h_j(x^*) = 0$), oppure il suo moltiplicatore è nullo ($\mu_j = 0$).

---

### Vincoli Attivi e Inattivi

- **Vincolo attivo** in $x^*$: $h_j(x^*) = 0$.
- **Vincolo inattivo** in $x^*$: $h_j(x^*) < 0$, quindi $\mu_j = 0$ (per complementarità).

---

### A Cosa Servono le KKT

Le condizioni KKT:

1. **Generalizzano** i moltiplicatori di Lagrange ai problemi con vincoli di disuguaglianza.
2. Sono **condizioni necessarie** di ottimalità sotto opportune ipotesi di regolarità (es. LICQ: i gradienti dei vincoli attivi sono linearmente indipendenti).
3. Sono **condizioni sufficienti** se $f$ è convessa (per min) e i vincoli di uguaglianza sono affini, oppure se i vincoli di disuguaglianza $h_j$ sono convessi.
4. Permettono di **enumerare i candidati ottimi** verificando tutte le combinazioni di vincoli attivi/inattivi.

---

### Risposta Modello da Esame

```
Le condizioni KKT generalizzano i moltiplicatori di Lagrange ai problemi
con vincoli di uguaglianza e disuguaglianza. Sono condizioni necessarie
di ottimalità sotto ipotesi di regolarità (es. LICQ).

Dato min f(x) s.t. g_i(x)=0, h_j(x)<=0, si costruisce:
  L = f(x) + sum lambda_i g_i(x) + sum mu_j h_j(x)

Le condizioni sono:
  1. Stazionarietà: grad_x L = 0
  2. Ammissibilità primale: g_i(x*)=0, h_j(x*)<=0
  3. Ammissibilità duale: mu_j >= 0
  4. Complementarità: mu_j * h_j(x*) = 0

Ogni candidato ottimo deve soddisfare le quattro condizioni.
Si enumerano i 2^p casi (vincolo attivo/inattivo) e si filtrano
i candidati che violano ammissibilità primale o duale.
```

---

## Errori da Evitare

- ❌ Dire che le KKT sono sempre condizioni sufficienti: lo sono solo in casi convessi appropriati.
- ❌ Non distinguere il segno dei moltiplicatori per min vs max.
- ❌ Non controllare l'ammissibilità primale dei candidati.
- ❌ Confondere vincoli attivi (usati in KKT) con vincoli inattivi (moltiplicatore nullo).

---

## Collegamenti

- [[MC_PNL_KKT_generale]]
- [[MC_PNL_KKT_vincoli_disuguaglianza]]
- [[MC_PNL_KKT_vincoli_uguaglianza]]
- [[MC_PNL_vincoli_attivi_complementarita]]
