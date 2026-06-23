# Ingestion Report — PNL Teoria Vincolata e Condizioni KKT

## Metadata

- Source IDs:
  - `SRC-0089` (`raw_assets/Programmazione Non Lineare/Ottimizzazione non lineare vincolata.pdf`)
  - `SRC-0093` (`raw_assets/Programmazione Non Lineare/PNL Vincolata 4.pdf`)
  - `SRC-0097` (`raw_assets/Programmazione Non Lineare/PNL_vincolata.pdf`)
- Tipo file: PDF
- Categoria: Slide ufficiali e dispense d'esame
- Area ROPR: Programmazione Non Lineare (PNL) Vincolata
- Affidabilità: Ufficiale (official)
- Stato analisi: Completato (consolidated)

## Sintesi Contenuto

Questi asset trattano lo sviluppo dell'ottimizzazione non lineare in presenza di vincoli di uguaglianza e disuguaglianza. Vengono esposti i tre approcci principali: la riduzione delle variabili libere (riduzione dimensionale), il metodo dei moltiplicatori di Lagrange per vincoli di sola uguaglianza, e la formulazione generale delle condizioni di Karush-Kuhn-Tucker (KKT) per vincoli di disuguaglianza, illustrando dettagliatamente l'algoritmo combinatorio per l'analisi dei vincoli attivi/inattivi.

## Argomenti Estratti

- **Formulazione del Problema Vincolato**:
  - $\min f(x)$ (o $\max f(x)$)
  - Vincoli di uguaglianza: $g_i(x) = 0, \quad i = 1, \dots, m$
  - Vincoli di disuguaglianza: $h_j(x) \le 0, \quad j = 1, \dots, p$
- **Tre Approcci Risolutivi**:
  1. *Riduzione Dimensionale*: Esplicitare alcune variabili tramite vincoli di uguaglianza per sostituirle nella funzione obiettivo (valido solo se esplicitabile univocamente).
  2. *Moltiplicatori di Lagrange*: Introduzione della funzione Lagrangiana per vincoli di uguaglianza:
     $$L(x, \lambda) = f(x) + \sum \lambda_i g_i(x)$$
     Risoluzione ponendo $\nabla L = 0$.
  3. *Condizioni di Karush-Kuhn-Tucker (KKT)*:
     - Condizione di stazionarietà: $\nabla f(x^*) + \sum \lambda_i \nabla g_i(x^*) + \sum \mu_j \nabla h_j(x^*) = 0$
     - Ammissibilità primale: $g_i(x^*) = 0$, $h_j(x^*) \le 0$
     - Segno dei moltiplicatori (Ammissibilità duale):
       - Per minimizzazione con vincoli $h_j(x) \le 0$: $\mu_j \ge 0$.
       - Per massimizzazione con vincoli $h_j(x) \le 0$: $\mu_j \le 0$.
     - Complementarità degli scarti: $\mu_j h_j(x^*) = 0$.
- **Esplorazione dei Vincoli Attivi**:
  - Un vincolo $h_j(x) \le 0$ si dice *attivo* in $x^*$ se $h_j(x^*) = 0$. In questo caso il moltiplicatore $\mu_j$ può essere non nullo.
  - Se un vincolo è *inattivo* ($h_j(x^*) < 0$), per la complementarità si ha necessariamente $\mu_j = 0$.
  - Con $p$ vincoli di disuguaglianza si hanno $2^p$ combinazioni di vincoli attivi/inattivi da analizzare sistematicamente.

## File Creati / Aggiornati

- `05_theory/programmazione_non_lineare/pnl_ottimizzazione_vincolata.md`
- `04_methods/programmazione_non_lineare/pnl_metodo_moltiplicatori_lagrange.md`
- `04_methods/programmazione_non_lineare/pnl_condizioni_kkt.md`
- `04_methods/programmazione_non_lineare/pnl_combinatoria_vincoli_attivi.md`

## Warning / Refusi / Incongruenze Rilevate

- **Segno dei moltiplicatori KKT**: C'è spesso confusione sul segno dei moltiplicatori $\mu$ a seconda che si minimizzi o massimizzi e di come siano scritti i vincoli. Nella KB abbiamo formalizzato la convenzione standard del corso:
  - Problema di **minimo** con vincoli nella forma $h(x) \le 0 \implies \mu \ge 0$.
  - Problema di **massimo** con vincoli nella forma $h(x) \le 0 \implies \mu \le 0$.
  - Qualsiasi altra forma deve essere ricondotta a questa tramite moltiplicazione per $-1$.
