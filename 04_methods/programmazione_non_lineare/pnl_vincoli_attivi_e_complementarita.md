---
type: method
topic: programmazione_non_lineare
status: active
reliability: official
---

# Vincoli Attivi, Inattivi e Condizioni di Complementarità

Nei problemi di ottimizzazione vincolata con vincoli di disuguaglianza, lo stato dei vincoli nel punto ottimo gioca un ruolo cruciale nella determinazione e classificazione dei punti stazionari tramite le condizioni di Karush-Kuhn-Tucker (KKT).

---

## Vincoli Attivi vs Vincoli Inattivi

Dato un vincolo di disuguaglianza espresso nella forma standard $h_j(x) \le 0$ e un punto ammissibile $x^*$:

### 1. Vincolo Attivo (Active Constraint)
Un vincolo si dice **attivo** in $x^*$ se il punto giace sulla frontiera definita dal vincolo:
$$h_j(x^*) = 0$$
- In questo caso, il vincolo limita effettivamente lo spazio di movimento ammissibile nella direzione di discesa (o salita) della funzione obiettivo.
- Il moltiplicatore associato $\mu_j^*$ può essere strettamente maggiore di zero ($\mu_j^* > 0$ per un minimo, $\mu_j^* < 0$ per un massimo) o nullo (in casi degeneri).

### 2. Vincolo Inattivo (Inactive/Relaxed Constraint)
Un vincolo si dice **inattivo** (o non attivo) in $x^*$ se il punto giace strettamente all'interno della regione ammissibile definita dal vincolo:
$$h_j(x^*) < 0$$
- In questo caso, localmente il vincolo non esercita alcuna restrizione e si comporta come se non ci fosse.
- Di conseguenza, il moltiplicatore di KKT associato deve essere nullo:
  $$\mu_j^* = 0$$

> [!WARNING]
> Nelle slide dell'asset *Ottimizzazione non lineare vincolata.pdf* è presente un'imprecisione testuale nel capoverso descrittivo: il caso in cui il vincolo è soddisfatto all'uguaglianza ($h_j(x^*) = 0$) va formalmente considerato come **vincolo attivo**.

---

## Condizione di Complementarità degli Scarti

La complementarità (o *complementary slackness*) impone che per ogni vincolo di disuguaglianza valga:
$$\mu_j^* \cdot h_j(x^*) = 0, \quad j = 1, \dots, p$$

Questa condizione esclude la possibilità che sia il vincolo sia il moltiplicatore siano contemporaneamente diversi da zero:
- Se $h_j(x^*) < 0$ (inattivo) $\implies \mu_j^* = 0$.
- Se $\mu_j^* \neq 0$ (moltiplicatore non nullo) $\implies h_j(x^*) = 0$ (attivo).

Operativamente, negli esercizi di esame, questo consente di studiare il problema suddividendolo in casi combinatori (es. considerando a turno attivi o inattivi i vari vincoli).

---

## Interpretazione Geometrica

Graficamente, per un problema di minimo:
1. Se il vincolo è **attivo** ($h_j(x^*) = 0$), il gradiente della funzione obiettivo $\nabla f(x^*)$ e il gradiente del vincolo $\nabla h_j(x^*)$ devono essere opposti in direzione (con segno dipendente dal moltiplicatore $\mu_j^* \ge 0$):
   $$\nabla f(x^*) + \mu_j^* \nabla h_j(x^*) = 0 \implies \nabla f(x^*) = -\mu_j^* \nabla h_j(x^*)$$
   Questo significa che non è possibile scendere ulteriormente senza uscire dalla regione ammissibile (la direzione di discesa $-\nabla f(x^*)$ punta verso l'esterno, indicata da $\nabla h_j(x^*)$).
2. Se il vincolo è **inattivo** ($h_j(x^*) < 0$), l'ottimo si comporta come un ottimo libero rispetto a quel vincolo ($\mu_j^* = 0$).

---

## Qualificazione dei Vincoli (LICQ)

Per garantire la validità delle condizioni KKT nel punto ottimo, i vincoli attivi devono soddisfare una condizione di qualificazione. La più comune è la **LICQ (Linear Independence Constraint Qualification)**:

I gradienti dei vincoli di uguaglianza e dei vincoli di disuguaglianza attivi nel punto $x^*$:
$$\{\nabla g_i(x^*)\}_{i=1}^m \cup \{\nabla h_j(x^*)\}_{j \in \mathcal{A}(x^*)}$$
devono essere vettori **linearmente indipendenti**, dove $\mathcal{A}(x^*)$ indica l'insieme degli indici dei vincoli di disuguaglianza attivi in $x^*$.

Se LICQ fallisce, le condizioni KKT potrebbero non valere nel punto di ottimo (ovvero potrebbero non esistere moltiplicatori che soddisfano il sistema KKT).

---

Vedi anche:
- [[pnl_condizioni_kkt]]
- [[pnl_vincolata_kkt_vincoli_attivi]]
- [[pnl_combinatoria_vincoli_attivi]]
