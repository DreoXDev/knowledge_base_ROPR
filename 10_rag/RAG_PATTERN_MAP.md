# RAG Pattern Map - ROPR

## Come usare questo file

Quando arriva una traccia d'esame, identificare parole chiave, forma del problema e output richiesto.

## Pattern iniziali attesi

| Pattern | Parole chiave | File metodo | Esempi |
|---|---|---|---|
| Modellazione PL | variabili decisionali, vincoli, funzione obiettivo | `10_rag/method_cards/PL_formulazione_modello.md` | `07_solved_examples/programmazione_lineare/wyndor_glass.md` |
| Metodo del simplesso | base, tableau, variabile entrante/uscente | `04_methods/programmazione_lineare/` | `07_solved_examples/programmazione_lineare/` |
| Dualità | duale, primale, prezzi ombra | `05_theory/dualita_sensitivita/` | `07_solved_examples/programmazione_lineare/` |
| Programmazione lineare intera | variabili binarie/intere, branch and bound, cutting planes | `04_methods/programmazione_lineare_intera/` | `07_solved_examples/programmazione_lineare_intera/` |
| Programmazione non lineare | KKT, gradiente, Hessiana, vincoli non lineari | `04_methods/programmazione_non_lineare/` | `07_solved_examples/programmazione_non_lineare/` |

---

## Pattern — Formulazione di un problema di PL

Trigger:
- "formulare il problema"
- "scrivere il modello"
- "variabili decisionali"
- "funzione obiettivo"
- "vincoli"
- "programmazione lineare"

Risposta attesa:
1. Definire le variabili decisionali.
2. Scrivere la funzione obiettivo.
3. Scrivere i vincoli funzionali.
4. Scrivere i vincoli di dominio/non negatività.
5. Specificare se si tratta di max o min.

Fonti:
- `05_theory/programmazione_lineare/02_formulazione_generale_pl.md`
- `07_solved_examples/programmazione_lineare/wyndor_glass.md`

---

## Pattern — Soluzione grafica PL

Trigger:
- "risolvere graficamente"
- "regione ammissibile"
- "disegnare i vincoli"
- "semipiano"
- "rette di livello"
- "ottimo grafico"

Risposta attesa:
1. Disegnare le rette associate ai vincoli.
2. Individuare i semipiani ammissibili.
3. Determinare la regione ammissibile.
4. Calcolare i vertici candidati.
5. Valutare la funzione obiettivo sui vertici oppure usare le rette di livello.
6. Indicare soluzione ottima e valore ottimo.

Fonti:
- `05_theory/programmazione_lineare/03_soluzione_grafica_pl.md`
- `05_theory/programmazione_lineare/04_regione_ammissibile_e_casi.md`

---

## Pattern — Assunzioni PL

Trigger:
- "assunzioni della programmazione lineare"
- "proporzionalità"
- "additività"
- "divisibilità"
- "certezza"
- "quando non posso usare PL"

Risposta attesa:
Spiegare proporzionalità, additività, continuità/divisibilità e certezza. Se le variabili devono essere intere, citare la Programmazione Lineare Intera.

Fonti:
- `05_theory/programmazione_lineare/05_assunzioni_programmazione_lineare.md`

---

## Pattern — Minimum Cost Flow

Trigger:
- "flusso a costo minimo"
- "distribution network"
- "conservazione del flusso"
- "costo di spedizione"
- "rete distributiva"

Risposta attesa:
1. Definire una variabile per ogni arco.
2. Minimizzare la somma costo per flusso.
3. Inserire vincoli di offerta/domanda.
4. Inserire vincoli di conservazione del flusso sui nodi intermedi.
5. Inserire vincoli di capacità e non negatività.

Fonti:
- `07_solved_examples/programmazione_lineare/distribution_network_min_cost_flow.md`
