# RAG Pattern Map - ROPR

## Come usare questo file

Quando arriva una traccia d'esame, identificare parole chiave, forma del problema e output richiesto.

## Pattern iniziali attesi

| Pattern | Parole chiave | File metodo | Esempi |
|---|---|---|---|
| Modellazione PL | variabili decisionali, vincoli, funzione obiettivo | `04_methods/programmazione_lineare/pl_formulazione_modelli.md` | `07_solved_examples/programmazione_lineare/wyndor_glass.md` |
| Metodo del simplesso | base, tableau, variabile entrante/uscente | `04_methods/programmazione_lineare/pl_simplesso_tabellare.md` | `07_solved_examples/programmazione_lineare/pl_simplesso_esempio_40_50.md` |
| Dualità | duale, primale, prezzi ombra | `10_rag/method_cards/METHOD_PL_DUALE.md` | `07_solved_examples/programmazione_lineare/pl_duale_vincoli_misti.md` |
| Programmazione lineare intera | variabili binarie/intere, branch and bound, cutting planes | `04_methods/programmazione_lineare_intera/` | `07_solved_examples/programmazione_lineare_intera/` |
| Programmazione non lineare | KKT, gradiente, Hessiana, vincoli non lineari | `04_methods/programmazione_non_lineare/` | `07_solved_examples/programmazione_non_lineare/` |

---

## Pattern: formulazione modello PL da testo

Trigger:
- "formulare il problema"
- "minimizzare il numero di dipendenti"
- "turni"
- "risorse"
- "workforce scheduling"

Risposta attesa:
1. Definire le variabili decisionali.
2. Scrivere la funzione obiettivo ($\min$ o $\max$).
3. Scrivere i vincoli funzionali con indicazione del significato a fianco.
4. Scrivere i vincoli di dominio/non negatività.

Fonti:
- `04_methods/programmazione_lineare/pl_formulazione_modelli.md`
- `07_solved_examples/programmazione_lineare/pl_turni_lavoro_formulazione.md`

---

## Pattern: simplesso tabellare

Trigger:
- "risolvere con simplesso"
- "forma tabellare"
- "entra in base"
- "esce di base"
- "tableau"

Risposta attesa:
1. Scrivere il modello aumentato con variabili di slack.
2. Disegnare il tableau iniziale con la riga 0 azzerata.
3. Indicare la variabile entrante, la uscente e l'elemento pivot per ogni iterazione.
4. Disegnare i tableau intermedi.
5. All'ottimo, specificare il valore ottimo di $Z^*$ e delle variabili decisionali.

Fonti:
- `04_methods/programmazione_lineare/pl_simplesso_tabellare.md`
- `07_solved_examples/programmazione_lineare/pl_simplesso_esempio_40_50.md`
- `07_solved_examples/programmazione_lineare/pl_simplesso_max_3x_5y.md`
- `07_solved_examples/programmazione_lineare/pl_tool_spa_simplesso.md`

---

## Pattern: metodo delle due fasi

Trigger:
- "due fasi"
- "variabile artificiale"
- "base iniziale ammissibile"
- "Fase 1"
- "surplus"

Risposta attesa:
1. Standardizzare il modello introducendo slack, surplus e variabili artificiali.
2. Formulare e risolvere la Fase 1 di minimizzazione delle artificiali.
3. Se $W^* = 0$, rimuovere le artificiali, ripristinare la funzione obiettivo originaria, azzerare i costi delle variabili in base e procedere con la Fase 2.
4. Se $W^* > 0$, dichiarare il problema originale non ammissibile.

Fonti:
- `04_methods/programmazione_lineare/pl_metodo_due_fasi.md`
- `07_solved_examples/programmazione_lineare/pl_due_fasi_esempio_base.md`

---

## Pattern: problema illimitato

Trigger:
- "illimitato"
- "nessuna variabile uscente"
- "tutti i coefficienti della colonna entrante sono negativi"
- "illimitatezza"

Risposta attesa:
1. Spiegare che la variabile selezionata per entrare in base può crescere indefinitamente poiché nessun vincolo ne limita l'aumento.
2. Dimostrare che la colonna pivot del tableau presenta tutti elementi non positivi ($\le 0$).
3. Concludere che $Z^* \to +\infty$ (massimizzazione) o $Z^* \to -\infty$ (minimizzazione).

Fonti:
- `07_solved_examples/programmazione_lineare/pl_due_fasi_problema_illimitato.md`
- `07_solved_examples/programmazione_lineare/pl_simplesso_max_3x_5y.md`

---

## Pattern: problema non ammissibile

Trigger:
- "non ammissibile"
- "Fase 1 ottima con artificiali positive"
- "regione vuota"

Risposta attesa:
1. Risolvere la Fase 1 del metodo delle due fasi.
2. Dimostrare che il tableau finale ottimo di Fase 1 ha valore $W^* > 0$ (presenza di variabili artificiali positive in base).
3. Concludere che non esistono soluzioni che soddisfano simultaneamente tutti i vincoli.

Fonti:
- `07_solved_examples/programmazione_lineare/pl_due_fasi_problema_non_ammissibile.md`

---

## Pattern: cammino minimo su grafo

Trigger:
- "cammino minimo"
- "grafo orientato"
- "pesato"
- "origine e destinazione"
- "conservazione del flusso"
- "bilancio nei nodi"

Risposta attesa:
1. Definire le variabili binarie sugli archi $x_{ij} \in \{0, 1\}$.
2. Scrivere la funzione obiettivo $\min Z = \sum c_{ij} x_{ij}$.
3. Scrivere i vincoli di conservazione del flusso (origine $=1$, destinazione $=-1$, intermedi $=0$).

Fonti:
- `10_rag/method_cards/METHOD_PL_CAMMINO_MINIMO.md`
- `07_solved_examples/programmazione_lineare/pl_cammino_minimo_formulazione.md`

---

## Pattern: costruzione duale

Trigger:
- "scrivere il duale"
- "costruire il duale"
- "problema primale"
- "prezzi ombra"
- "trasposta"
- "variabili libere"
- "vincoli misti"

Risposta attesa:
1. Invertire l'ottimizzazione ($\max \leftrightarrow \min$).
2. Associare variabili duali ai vincoli primali definendone il segno.
3. Scrivere la funzione obiettivo usando i termini noti (RHS) primali.
4. Trasporre la matrice dei coefficienti dei vincoli.
5. Definire il verso dei vincoli duali in base al segno delle variabili primali.

Fonti:
- `10_rag/method_cards/METHOD_PL_DUALE.md`
- `07_solved_examples/programmazione_lineare/pl_tool_spa_duale.md`
- `07_solved_examples/programmazione_lineare/pl_duale_vincoli_misti.md`

---

## Pattern — Risoluzione PL con simplesso tabellare

Trigger:
- "risolvi con il simplesso"
- "continua il tableau"
- "scegli variabile entrante/uscente"
- "pivot"
- "forma tabellare"
- "soluzione di base"

Risposta attesa:
1. Scrivere o riconoscere il tableau.
2. Indicare variabile entrante.
3. Indicare variabile uscente con rapporto minimo.
4. Eseguire pivot o almeno descrivere l'operazione.
5. Ripetere fino al criterio di ottimalità.
6. Leggere soluzione finale e valore ottimo.

Fonti:
- `04_methods/programmazione_lineare/pl_simplesso_tabellare.md`
- `07_solved_examples/programmazione_lineare/pl_simplesso_wyndor.md`

---

## Pattern — Casi particolari del simplesso

Trigger:
- "ottimi multipli"
- "illimitato"
- "degenerazione"
- "tie breaking"
- "nessuna variabile uscente"
- "coefficiente nullo in riga 0"

Risposta attesa:
- Identificare il segnale nel tableau.
- Dichiarare il caso.
- Spiegare in una riga la conseguenza.
- Se richiesto, continuare con un pivot alternativo.

Fonti:
- `04_methods/programmazione_lineare/pl_casi_particolari_simplesso.md`
- `07_solved_examples/programmazione_lineare/pl_simplesso_casi_particolari.md`
