# RAG Pattern Map - ROPR

## Come usare questo file

Quando arriva una traccia d'esame, identificare parole chiave, forma del problema e output richiesto.

## Pattern iniziali attesi

| Pattern | Parole chiave | File metodo | Esempi |
|---|---|---|---|
| Modellazione PL | variabili decisionali, vincoli, funzione obiettivo | `04_methods/programmazione_lineare/pl_formulazione_modelli.md` | `07_solved_examples/programmazione_lineare/wyndor_glass.md` |
| Metodo del simplesso | base, tableau, variabile entrante/uscente | `04_methods/programmazione_lineare/pl_simplesso_tabellare.md` | `07_solved_examples/programmazione_lineare/pl_simplesso_esempio_40_50.md` |
| Dualità (Costruzione) | duale, primale, metodo SOB, sensible odd bizarre | `04_methods/programmazione_lineare/pl_costruire_duale_standard.md` | `07_solved_examples/programmazione_lineare/pl_duale_vincoli_misti.md` |
| Dualità (Ottimalità & Slackness) | complementary slackness, verificare ottimalità, scarti complementari | `04_methods/programmazione_lineare/pl_usare_complementary_slackness.md` | `10_rag/method_cards/PL_complementary_slackness.md` |
| Prezzi Ombra | prezzi ombra, valore marginale, leggere tableau | `04_methods/programmazione_lineare/pl_leggere_variabili_duali_da_tableau.md` | `10_rag/method_cards/PL_prezzi_ombra.md` |
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
- "metodo sensible odd bizarre"
- "metodo SOB"

Risposta attesa:
1. Invertire l'ottimizzazione ($\max \leftrightarrow \min$).
2. Associare variabili duali ai vincoli primali definendone il segno (standard o SOB).
3. Scrivere la funzione obiettivo usando i termini noti (RHS) primali.
4. Trasporre la matrice dei coefficienti dei vincoli.
5. Definire il verso dei vincoli duali in base al segno delle variabili primali (standard o SOB).

Fonti:
- `04_methods/programmazione_lineare/pl_costruire_duale_standard.md`
- `04_methods/programmazione_lineare/pl_costruire_duale_sensible_odd_bizarre.md`
- `10_rag/method_cards/PL_costruzione_duale.md`
- `10_rag/method_cards/PL_sensible_odd_bizarre.md`
- `05_theory/programmazione_lineare/11_regole_costruire_duale.md`
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

---

## Pattern — Domanda teorica sul simplesso

Trigger:
- "spiega il simplesso"
- "teoria del simplesso"
- "vertice ammissibile"
- "frontiera del vincolo"
- "iperpiano"
- "perché il simplesso controlla i vertici"
- "vertici adiacenti"
- "degenerazione"
- "soluzione di base degenere"

Risposta attesa:
- Spiegare il concetto geometrico o algebrico richiesto in modo definitorio.
- Mostrare formule in LaTeX o tabelle esplicative.
- Mantenere la risposta concisa e focalizzata sulla teoria d'esame.

Fonti:
- `10_rag/method_cards/PL_teoria_simplesso.md`
- `10_rag/method_cards/PL_vertici_frontiere_iperpiani.md`
- `10_rag/method_cards/PL_vertici_adiacenti_ottimalita.md`
- `05_theory/programmazione_lineare/17_teoria_simplesso.md`
- `05_theory/programmazione_lineare/12_geometria_simplesso.md`
- `05_theory/programmazione_lineare/13_forma_aumentata_soluzioni_base.md`
- `05_theory/programmazione_lineare/18_vertici_adiacenti_cammino_simplesso.md`
- `05_theory/programmazione_lineare/19_degenerazione_simplesso.md`
- `05_theory/programmazione_lineare/20_proprieta_vertici_ammissibili.md`

---

## Pattern: verificare ottimalità con dualità e complementary slackness

Trigger:
- "dimostrare che è ottima"
- "usare dualità"
- "dualità debole"
- "dualità forte"
- "valori primale duale coincidono"
- "complementary slackness"
- "scarti complementari"
- "verificare ottimalità"

Risposta attesa:
1. Verificare l'ammissibilità della soluzione primale $\mathbf{x}$ nei vincoli primali.
2. Calcolare gli scarti primali $s_i$.
3. Impostare il sistema duale usando le condizioni di complementarità ($s_i > 0 \implies y_i = 0$ e $x_j > 0 \implies A_j^T y = c_j$).
4. Risolere il sistema per trovare le variabili duali candidate $\mathbf{y}$.
5. Verificare l'ammissibilità delle variabili duali candidate (segni coerenti e vincoli rispettati).
6. Se ammissibile, confermare l'ottimalità per dualità forte/debole.

Fonti:
- `04_methods/programmazione_lineare/pl_usare_complementary_slackness.md`
- `10_rag/method_cards/PL_complementary_slackness.md`
- `10_rag/method_cards/PL_dualita_teoria.md`
- `05_theory/programmazione_lineare/24_complementary_slackness.md`
- `05_theory/programmazione_lineare/22_dualita_debole_forte.md`

---

## Pattern: prezzi ombra e lettura variabili duali dal tableau

Trigger:
- "prezzi ombra"
- "valore marginale"
- "interpretazione economica"
- "variabili duali dal tableau"
- "leggere duale dal tableau"
- "coefficiente slack riga 0"

Risposta attesa:
1. Individuare la riga 0 del tableau ottimo del simplesso primale.
2. Identificare i coefficienti sotto le colonne delle variabili di slack $s_i$ nella riga 0.
3. Assegnare a ciascuna variabile duale $y_i^*$ il coefficiente di $s_i$.
4. Spiegare il prezzo ombra come valore marginale della risorsa: variazione di $Z^*$ per unità aggiuntiva di risorsa $b_i$.

Fonti:
- `04_methods/programmazione_lineare/pl_leggere_variabili_duali_da_tableau.md`
- `10_rag/method_cards/PL_prezzi_ombra.md`
- `05_theory/programmazione_lineare/23_prezzi_ombra_interpretazione.md`

---

## Pattern: modellazione PLI (assegnamento)

Trigger:
- "ogni attività a un solo impiegato"
- "ogni impiegato una sola attività"
- "assegnamento ottimale"
- "accoppiamento perfetto"

Risposta attesa:
1. Definire le variabili binarie $x_{ij} \in \{0, 1\}$.
2. Scrivere la funzione obiettivo di minimo costo.
3. Scrivere i vincoli di assegnamento (somma per riga e somma per colonna uguali a 1).
4. Dichiarare il dominio.

Fonti:
- `10_rag/method_cards/MC_PLI_assegnamento_costo_minimo.md`
- `07_solved_examples/programmazione_lineare_intera/pli_assegnamento_costo_minimo.md`

---

## Pattern: modellazione PLI (cammino minimo)

Trigger:
- "percorso più veloce"
- "cammino da s a t"
- "percorso a costo minimo"

Risposta attesa:
1. Definire le variabili binarie sugli archi $x_{ij} \in \{0, 1\}$.
2. Scrivere la funzione obiettivo di minimo costo.
3. Scrivere le equazioni di bilancio dei nodi (sorgente $-1$, destinazione $1$, intermedi $0$).
4. Dichiarare il dominio.

Fonti:
- `10_rag/method_cards/MC_PLI_cammino_costo_minimo.md`
- `07_solved_examples/programmazione_lineare_intera/pli_cammino_costo_minimo.md`

---

## Pattern: modellazione PLI (flusso a costo minimo)

Trigger:
- "offerta, domanda, spedire lungo archi"
- "capacità degli archi"
- "flusso di costo minimo"

Risposta attesa:
1. Definire le variabili di flusso $x_{ij} \ge 0$ intere.
2. Scrivere la funzione obiettivo.
3. Scrivere i vincoli di conservazione del flusso ai nodi e di capacità degli archi.
4. Dichiarare il dominio.

Fonti:
- `10_rag/method_cards/MC_PLI_flusso_costo_minimo.md`
- `07_solved_examples/programmazione_lineare_intera/pli_flusso_costo_minimo.md`

---

## Pattern: modellazione PLI (vincoli di alternativa, contingenza e logici)

Trigger:
- "se produco allora almeno L unità"
- "costo fisso di attivazione"
- "se scelgo allora almeno"
- "vincoli logici"
- "either-or"
- "K su N"
- "magazzino solo se fabbrica"
- "contingenza"

Risposta attesa:
1. Definire le variabili continue/intere di livello $x_i$ e le binarie di attivazione $y_i \in \{0, 1\}$.
2. Scrivere la funzione obiettivo includendo il costo fisso.
3. Scrivere i vincoli logici (e.g. $x_j \le x_i$ per contingenza, o Big-M disgiuntivo per either-or).
4. Dichiarare il dominio.

Fonti:
- `10_rag/method_cards/MC_PLI_vincoli_logici_big_m.md`
- `10_rag/method_cards/MC_PLI_logica_vincoli_binari.md`
- `07_solved_examples/programmazione_lineare_intera/pli_produzione_vincoli_alternativa.md`
- `07_solved_examples/programmazione_lineare_intera/pli_modellazione_smistamento_automobili.md`
- `07_solved_examples/programmazione_lineare_intera/pli_modellazione_asili_nido_montani.md`
- `07_solved_examples/programmazione_lineare_intera/pli_modellazione_rifornimento_agende.md`
- `07_solved_examples/programmazione_lineare_intera/pli_modellazione_stendino_remo.md`
- `07_solved_examples/programmazione_lineare_intera/pli_modellazione_lombardia_manufacturing.md`

---

## Pattern: modellazione PLI (produzione e stoccaggio)

Trigger:
- "produzione nei mesi"
- "domanda del periodo"
- "magazzino"
- "scorte iniziali"

Risposta attesa:
1. Definire le variabili di produzione $x_t$, magazzino $s_t$ ed eventuali binarie $y_t$.
2. Scrivere la funzione obiettivo (costi di produzione + stoccaggio + setup).
3. Scrivere l'equazione di bilancio $s_t = s_{t-1} + x_t - d_t$ con $s_0 = I_0$.
4. Scrivere i vincoli di capacità e il dominio.

Fonti:
- `10_rag/method_cards/MC_PLI_produzione_stoccaggio.md`
- `07_solved_examples/programmazione_lineare_intera/pli_produzione_stoccaggio.md`

---

## Pattern: modellazione PLI (facility location)

Trigger:
- "depositi, centri, costo fisso, capacità"
- "aprire magazzini"
- "servire clienti"

Risposta attesa:
1. Definire le variabili binarie di apertura $y_j \in \{0, 1\}$ e le variabili di servizio $x_{ij} \ge 0$.
2. Scrivere la funzione obiettivo (costi di apertura + trasporto).
3. Scrivere i vincoli di soddisfacimento domanda ($\sum_j x_{ij} = 1$) e i vincoli di capacità ed attivazione ($\sum_i d_i x_{ij} \le U_j y_j$).
4. Dichiarare il dominio.

Fonti:
- `10_rag/method_cards/MC_PLI_facility_location.md`
- `07_solved_examples/programmazione_lineare_intera/pli_facility_location.md`

---

## Pattern: modellazione PLI (knapsack / zaino)

Trigger:
- "investimenti, capitale, ricavo, scelgo/non scelgo"
- "problema dello zaino"
- "budget limitato"

Risposta attesa:
1. Definire le variabili binarie $x_j \in \{0, 1\}$.
2. Scrivere la funzione obiettivo di massimizzazione del valore.
3. Scrivere l'unico vincolo di budget.
4. Dichiarare il dominio.

Fonti:
- `10_rag/method_cards/MC_PLI_knapsack.md`
- `07_solved_examples/programmazione_lineare_intera/pli_investimento_zaino.md`
- `05_theory/programmazione_lineare/10_dualita.md`

---

## Pattern: Branch and Bound per PLIM

Trigger:
- "risolvere il problema PLIM tramite Branch and Bound"
- "variabili intere e continue"
- "rilassamento lineare del problema misto"
- "albero di branching per variabili continue"

Risposta attesa:
1. Dichiarare esplicitamente quali variabili sono vincolate a essere intere ($x_j \in \mathbb{Z}$) e quali sono continue ($y_k \in \mathbb{R}$).
2. Compilare la tabella dei nodi con i relativi vincoli aggiunti, la soluzione del rilassamento LP, il bound, lo stato del nodo (aperto/chiuso) e il motivo.
3. Specificare che il branching avviene solo sulle variabili intere frazionarie e che i bound non possono essere arrotondati.
4. Dichiarare la soluzione ottima di tutte le variabili ($x^*$ e $y^*$) e il valore ottimo $z^*$.

Fonti:
- `10_rag/method_cards/MC_PLI_branch_and_bound_plim.md`
- `07_solved_examples/programmazione_lineare_intera/pli_plim_bb_esercizio_svolto.md`
- `05_theory/programmazione_lineare_intera/pli_branch_and_bound_plim.md`

---

## Pattern: Interpretazione Albero Branch and Bound

Trigger:
- "si consideri l'albero di Branch and Bound"
- "stabilire se si tratta di un problema di massimo o di minimo"
- "indicare quale nodo viene selezionato con la regola best bound"
- "calcolare l'intervallo dell'ottimo"
- "quali nodi possono essere potati"

Risposta attesa:
1. Riconoscere il tipo di problema ($\max/\min$) spiegando che i bound decrescono ($\max$) o crescono ($\min$) lungo i rami da padre a figlio.
2. Identificare la migliore soluzione ammissibile corrente (incumbent $Z_I$).
3. Calcolare l'intervallo dell'ottimo $[Z_{bound}, Z_I]$ o $[Z_I, Z_{bound}]$ (dove $Z_{bound}$ è il miglior bound tra i nodi aperti).
4. Sotto Best Bound First, selezionare il prossimo nodo aperto con il bound più promettente.
5. Identificare ed elencare i nodi chiudibili per dominanza rispetto all'incumbent.

Fonti:
- `10_rag/method_cards/MC_PLI_interpretare_albero_branch_and_bound.md`
- `10_rag/method_cards/MC_PLI_gap_ottimalita_branch_and_bound.md`
- `04_methods/programmazione_lineare_intera/pli_interpretare_albero_branch_and_bound.md`
- `05_theory/programmazione_lineare_intera/pli_soluzioni_quasi_ottime.md`

---

## Pattern: binarizzazione di variabili intere (espansione binaria)

Trigger:
- "rappresentazione binaria"
- "espansione binaria di variabili intere"
- "convertire in binarie"
- "variabile intera limitata"
- "passare ad un problema caratterizzato solo da variabili binarie"

Risposta attesa:
1. Determinare il limite superiore $u$ per la variabile intera $x$.
2. Calcolare la massima potenza di due $2^K \le u < 2^{K+1}$.
3. Scrivere l'espressione $x = \sum_{k=0}^K 2^k y_k = y_0 + 2y_1 + 4y_2 + \dots + 2^K y_K$.
4. Se $u \ne 2^{K+1}-1$, aggiungere il vincolo di barriera superiore: $\sum_{k=0}^K 2^k y_k \le u$.
5. Sostituire nel modello e dichiarare $y_k \in \{0, 1\}$.

Fonti:
- `10_rag/method_cards/MC_PLI_rappresentazione_binaria_interi.md`
- `05_theory/programmazione_lineare_intera/pli_logica_e_variabili_binarie.md`

---

## Pattern: Branch and Bound Binario

Trigger:
- "risolvere tramite Branch and Bound binario"
- "branch and bound per variabili binarie"
- "Lombardia Manufacturing branch and bound"
- "arrotondamento all'intero dei bound"
- "fissaggio delle variabili a 0 o 1"

Risposta attesa:
1. Inizializzare l'incumbent $Z_I = -\infty$ (o $+\infty$).
2. Risolvere il rilassamento continuo completo $P_0$ (con $0 \le x_j \le 1$).
3. Giustificare l'arrotondamento all'intero dei bound (es. $\lfloor Z_C \rfloor$ per massimo se i coefficienti della funzione obiettivo sono interi).
4. Disegnare l'albero di branching o presentare la tabella dei nodi con bound reali/arrotondati, stati dei nodi (chiuso per interezza, inammissibilità, dominanza) e l'incumbent corrente.
5. Specificare la soluzione ottima globale $x^*$ e il valore ottimo $z^*$.

Fonti:
- `10_rag/method_cards/MC_PLI_branch_and_bound_binario.md`
- `05_theory/programmazione_lineare_intera/pli_branch_and_bound_binario.md`
- `07_solved_examples/programmazione_lineare_intera/pli_bb_binario_lombardia_manufacturing.md`

---

## Pattern: classificazione punti stazionari non vincolati

Trigger:
- "punti stazionari"
- "classificare i punti stazionari"
- "minimo locale"
- "massimo locale"
- "punto di sella"
- "matrice Hessiana convessa concava"

Risposta attesa:
1. Calcolare le derivate parziali prime e porre il sistema $\nabla f(x, y) = 0$ per trovare i punti stazionari $P^*$.
2. Calcolare le derivate parziali seconde e impostare la matrice Hessiana $H_f(x, y)$.
3. Valutare $H_f(P^*)$ per ciascun punto stazionario.
4. Classificare la matrice tramite determinante e traccia (in 2D) o autovalori:
   - $\det(H_f) > 0$ e $\text{tr}(H_f) > 0 \implies$ minimo locale.
   - $\det(H_f) > 0$ e $\text{tr}(H_f) < 0 \implies$ massimo locale.
   - $\det(H_f) < 0 \implies$ punto di sella.
   - $\det(H_f) = 0 \implies$ caso degenere.
5. Se $H_f(x, y)$ è semidefinita positiva o negativa per ogni $(x, y) \in \mathbb{R}^2$, dichiarare se la funzione è rispettivamente convessa o concava globalmente, rendendo gli ottimi locali anche ottimi globali.

Fonti:
- `10_rag/method_cards/MC_PNL_studio_funzione_due_variabili.md`
- `10_rag/method_cards/MC_PNL_classificazione_hessiana.md`
- `04_methods/programmazione_non_lineare/pnl_non_vincolata_punti_stazionari_hessiana.md`
- `07_solved_examples/programmazione_non_lineare/pnl_non_vincolata_esercizi_base.md`

---

## Pattern: iterazione metodo del gradiente con line search esatta

Trigger:
- "metodo del gradiente con line search esatta"
- "discesa rapida"
- "due iterazioni del metodo del gradiente"
- "passo di line search esatta"

Risposta attesa:
1. Calcolare il gradiente $\nabla f(x_k)$ nel punto corrente.
2. Impostare la direzione $d_k = -\nabla f(x_k)$ (per minimo) o $d_k = \nabla f(x_k)$ (per massimo).
3. Esprimere il punto generico $x(\alpha) = x_k + \alpha d_k$.
4. Sostituire le coordinate nella funzione obiettivo ottenendo $\phi(\alpha) = f(x_k + \alpha d_k)$.
5. Risolvere $\frac{d\phi(\alpha)}{d\alpha} = 0$ per trovare il passo ottimale $\alpha_k$.
6. Calcolare il nuovo punto $x_{k+1} = x_k + \alpha_k d_k$.
7. Verificare l'ortogonalità consecutiva della direzione successiva se richiesto: $\nabla f(x_{k+1})^T d_k = 0$.

Fonti:
- `10_rag/method_cards/MC_PNL_gradiente_line_search_esatta.md`
- `04_methods/programmazione_non_lineare/pnl_metodo_gradiente_line_search_esatta.md`
- `07_solved_examples/programmazione_non_lineare/pnl_non_vincolata_gradiente_newton.md`

---

## Pattern: iterazione metodo di newton multivariabile

Trigger:
- "metodo di Newton a partire dal punto"
- "una iterazione del metodo di Newton"
- "direzione di Newton"

Risposta attesa:
1. Calcolare gradiente $\nabla f(x_k)$ e Hessiana $H_f(x_k)$ nel punto corrente.
2. Impostare il sistema lineare $H_f(x_k) d_k = -\nabla f(x_k)$ (per minimizzazione) o $H_f(x_k) d_k = \nabla f(x_k)$ (per massimizzazione se si mantiene la formulazione standard).
3. Risolvere il sistema lineare per ricavare il vettore direzione $d_k$.
4. Calcolare il nuovo punto con passo unitario: $x_{k+1} = x_k + d_k$.
5. Se la funzione è quadratica ad Hessiana definita positiva/negativa, ricordare che il metodo di Newton raggiunge l'ottimo globale in una sola iterazione.

Fonti:
- `10_rag/method_cards/MC_PNL_newton_non_vincolata.md`
- `04_methods/programmazione_non_lineare/pnl_metodo_newton_non_vincolata.md`
- `07_solved_examples/programmazione_non_lineare/pnl_non_vincolata_gradiente_newton.md`

---

## Pattern: condizioni KKT e risoluzione vincolata

Trigger:
- "condizioni KKT"
- "Karush-Kuhn-Tucker"
- "punti di minimo/massimo di f su region utilizzando condizioni KKT"
- "risolvere il sistema KKT associato"

Risposta attesa:
1. Verificare o ricondurre i vincoli in forma standard $h_j(x) \le 0$ (moltiplicando per $-1$ se necessario).
2. Scrivere la Lagrangiana $L(x, \lambda, \mu)$.
3. Formulare il sistema KKT composto da:
   - Stazionarietà: $\nabla_x L = 0$
   - Ammissibilità primale: $g_i(x) = 0, h_j(x) \le 0$
   - Complementarità degli scarti: $\mu_j h_j(x) = 0$
   - Segno dei moltiplicatori: $\mu_j \ge 0$ (per minimo), $\mu_j \le 0$ (per massimo)
4. Risolvere il sistema impostando e analizzando le diverse combinazioni di vincoli attivi e inattivi.
5. Per ogni punto trovato, verificare i segni dei moltiplicatori per confermarne l'ammissibilità KKT.
6. Valutare $f(x)$ nei punti ammissibili per determinare l'ottimo globale (se la regione è compatta, Weierstrass garantisce l'esistenza degli ottimi).

Fonti:
- `10_rag/method_cards/MC_PNL_KKT_vincoli_disuguaglianza.md`
- `10_rag/method_cards/MC_PNL_KKT_vincoli_uguaglianza.md`
- `04_methods/programmazione_non_lineare/pnl_vincolata_condizioni_KKT.md`
- `04_methods/programmazione_non_lineare/pnl_combinatoria_vincoli_attivi.md`
- `07_solved_examples/programmazione_non_lineare/pnl_vincolata_kkt_esempi.md`

---

## Pattern: PNL 1D - Metodo di bisezione

Trigger:
- "metodo di bisezione"
- "algoritmo dicotomico"
- "intervallo di incertezza"
- "tolleranza epsilon"
- "derivata positiva/negativa"

Risposta attesa:
1. Verificare che la funzione sia continua, derivabile e concava/convessa sull'intervallo.
2. Trovare l'intervallo di partenza $[\underline{x}_0, \bar{x}_0]$ con derivate di segno opposto.
3. Iterativamente calcolare il punto medio $x_k = \frac{\underline{x}_k + \bar{x}_k}{2}$.
4. Valutare il segno di $f'(x_k)$ e aggiornare l'estremo corretto.
5. Mostrare la tabella delle iterazioni fino all'arresto per $\bar{x} - \underline{x} \le 2\epsilon$.
6. Dichiarare l'intervallo finale e il valore ottimo approssimato.

Fonti:
- `10_rag/method_cards/MC_PNL_metodo_bisezione_1d.md`
- `04_methods/programmazione_non_lineare/pnl_metodo_bisezione.md`
- `07_solved_examples/programmazione_non_lineare/pnl_bisezione_funzione_concava.md`

---

## Pattern: PNL 1D - Metodo di Newton

Trigger:
- "metodo di Newton"
- "approssimazione quadratica"
- "formula di Taylor"
- "punto iniziale"
- "derivata seconda"

Risposta attesa:
1. Calcolare analiticamente le derivate prima $f'(x)$ e seconda $f''(x)$.
2. Partire dal punto iniziale $x_0$.
3. Eseguire l'aggiornamento iterativo tramite $x_{k+1} = x_k - \frac{f'(x_k)}{f''(x_k)}$.
4. Verificare il criterio di arresto $|x_{k+1} - x_k| \le \epsilon$.
5. Mostrare la tabella delle iterazioni ed il calcolo dell'avanzamento.
6. Verificare la natura del punto finale controllando il segno della derivata seconda.

Fonti:
- `10_rag/method_cards/MC_PNL_metodo_newton_1d.md`
- `04_methods/programmazione_non_lineare/pnl_metodo_newton_1d.md`
- `07_solved_examples/programmazione_non_lineare/pnl_newton_funzione_1d.md`

---

## Pattern: PNL Vincolata - KKT con vincoli attivi

Trigger:
- "vincoli attivi e non attivi"
- "enumerazione vincoli"
- "moltiplicatori lagrangiani"
- "Lagrangiana con disuguaglianze"

Risposta attesa:
1. Riscrivere i vincoli come $g_i(x) \le 0$ e costruire la Lagrangiana $L = f + \sum \mu_i g_i$.
2. Formulare il sistema KKT di stazionarietà, ammissibilità primale/duale e complementarità.
3. Elencare le $2^m$ combinazioni di vincoli attivi/inattivi.
4. Per ogni combinazione, risolvere il sistema per $(x, y)$ e i moltiplicatori attivi $\mu_i$ (ponendo $\mu_i = 0$ per gli inattivi).
5. Scartare i punti non ammissibili primali o con moltiplicatori negativi ($\mu_i < 0$).
6. Presentare la tabella riassuntiva dei casi e dichiarare l'ottimo globale vincolato confrontando i candidati validi.

Fonti:
- `10_rag/method_cards/MC_PNL_KKT_vincoli_disuguaglianza.md`
- `04_methods/programmazione_non_lineare/pnl_vincolata_kkt_vincoli_attivi.md`
- `07_solved_examples/programmazione_non_lineare/pnl_kkt_esempio_quadratico_3_vincoli.md`

---

## Pattern: PNL Vincolata Generale (Riduzione, Lagrange, KKT)

Trigger:
- "riducendo il numero di variabili libere"
- "moltiplicatori di Lagrange con vincoli di uguaglianza"
- "condizioni KKT per disuguaglianze"
- "vincoli attivi e non attivi"
- "regola di complementarità"
- "regolarità dei vincoli LICQ"

Risposta attesa:
1. Analizzare la natura della regione ammissibile (compattezza, Weierstrass).
2. Scegliere la strategia opportuna:
   - Se riduzione variabili: esplicitare, sostituire, risolvere il problema non vincolato e ripristinare.
   - Se Lagrange: Lagrangiana $L = f + \lambda g$, risolvere $\nabla L = 0$, confrontare.
   - Se KKT: Lagrangiana generalizzata, impostare stazionarietà, ammissibilità primale/duale e complementarità degli scarti, analizzare per casi combinatori, scartare candidati non ammissibili o con moltiplicatori di segno errato, confrontare.
3. Se richiesto, discutere l'interpretazione geometrica (gradienti paralleli/ortogonali) o verificare LICQ.

Fonti:
- `06_exam_patterns/pnl_pattern_vincolata_generale.md`
- `10_rag/method_cards/MC_PNL_riduzione_variabili_libere.md`
- `10_rag/method_cards/MC_PNL_Lagrange_vincoli_uguaglianza.md`
- `10_rag/method_cards/MC_PNL_KKT_generale.md`
- `10_rag/method_cards/MC_PNL_vincoli_attivi_complementarita.md`
- `07_solved_examples/programmazione_non_lineare/pnl_lagrange_cerchio_unitario.md`
- `07_solved_examples/programmazione_non_lineare/pnl_riduzione_variabili_esempio_lineare.md`

---

## Pattern: Massimi/minimi locali PNL (Non Vincolata)

Trigger:
- "Trovare massimi e minimi locali della funzione"
- "classificare i punti stazionari di"

Risposta attesa:
1. Calcolare il gradiente $\nabla f(x, y)$ ed annullarlo.
2. Risolvere il sistema per i punti stazionari.
3. Calcolare la matrice Hessiana $H_f(x, y)$ e valutarla nei punti.
4. Classificare tramite determinante e traccia.

Fonti:
- `06_exam_patterns/pnl_non_vincolata_classificazione_hessiana.md`
- `10_rag/method_cards/MC_PNL_classificazione_hessiana.md`
- `07_solved_examples/programmazione_non_lineare/pnl_non_vincolata_esercizi_punti_stazionari.md`
- `07_solved_examples/programmazione_non_lineare/pnl_20_esercizi_catalogo.md`

---

## Pattern: Massimi/minimi globali PNL vincolata (KKT)

Trigger:
- "Trovare massimi e minimi globali della funzione"
- "sull'insieme"
- "sistema KKT"

Risposta attesa:
1. Analizzare la compattezza (Weierstrass).
2. Riscrivere in forma standard $h_j(x, y) \le 0$.
3. Impostare la Lagrangiana generalizzata ed il sistema KKT.
4. Risolvere analizzando le combinazioni di vincoli attivi/inattivi.
5. Verificare ammissibilità primale e duale (segno dei moltiplicatori $\mu_j$).
6. Valutare $f(x,y)$ per identificare gli ottimi globali.

Fonti:
- `06_exam_patterns/pnl_vincolata_kkt_globali.md`
- `10_rag/method_cards/MC_PNL_KKT_generale.md`
- `07_solved_examples/programmazione_non_lineare/pnl_vincolata_esercizi_kkt_globali.md`
- `07_solved_examples/programmazione_non_lineare/pnl_20_esercizi_catalogo.md`

---

## Pattern: Zaino Branch and Bound in Ampiezza

Trigger:
- "problema dello zaino"
- "Branch and Bound con strategia di visita in ampiezza"

Risposta attesa:
1. Ordinare per efficienza decrescente $v_i/p_i$.
2. Calcolare bound tramite rilassamento continuo.
3. Ramificare a livelli successivi (visita in ampiezza).
4. Potare per interezza, dominanza o inammissibilità.

Fonti:
- `10_rag/method_cards/MC_PLI_branch_and_bound_zaino.md`
- `07_solved_examples/riepilogo_pl_pli_pnl_esercizi_misti.md`

---

## Pattern: Modello di Trasporto PL

Trigger:
- "stabilimenti", "punti vendita", "capacità", "domanda", "costi di spedizione"

Risposta attesa:
1. Definire le variabili $x_{ij}$.
2. Scrivere la funzione obiettivo di minimo costo.
3. Inserire vincoli di capacità stabilimenti ($\le$) e domanda punti vendita ($\ge$).

Fonti:
- `10_rag/method_cards/MC_PL_modello_trasporto.md`
- `07_solved_examples/riepilogo_pl_pli_pnl_esercizi_misti.md`

---

## Pattern: Riepilogo Strategico PL/PLI/PNL

Trigger:
- "Esercizi di riepilogo su Programmazione Lineare Intera e Programmazione Non Lineare"
- Quesiti d'esame misti

Risposta attesa:
1. Identificare la tipologia di esercizio (trasporto, zaino, Newton/gradiente, KKT).
2. Instradare verso la method card corretta.
3. Applicare la checklist strategica per lo scritto.

Fonti:
- `06_exam_patterns/riepilogo_esame_pl_pli_pnl.md`
- `10_rag/method_cards/MC_Riepilogo_esame_misto_PL_PLI_PNL.md`
- `07_solved_examples/riepilogo_pl_pli_pnl_esercizi_misti.md`

---

## Pattern: Quiz PL — Verifica Soluzione Primale/Duale

Trigger:
- "soluzione ammissibile per il primale"
- "soluzione ottimale per il duale"
- "dualità forte" / "dualità debole"
- "seleziona le risposte vere" + PL

Risposta attesa:
1. Verificare dimensione, non negatività, vincoli per ogni candidato.
2. Calcolare valore obiettivo primale e duale.
3. Applicare dualità forte se i valori coincidono.

Fonti:
- `06_exam_patterns/Quiz_PL_primale_duale.md`
- `10_rag/method_cards/MC_PL_verifica_soluzione_primale_duale.md`
- `10_rag/topic_cards/TC_quiz_PL_primale_duale.md`

Nota: fonte non ufficiale — ricalcolare, non fidarsi delle crocette.

---

## Pattern: Quiz PL — Analisi di Sensitività da Tableau

Trigger:
- "analisi di sensitività"
- "intervallo ammissibile di variazione" + "$\Delta$"
- "tableau finale" + "$c_i$" o "$b_i$"
- "mantenere ottimalità" / "mantenere ammissibilità"

Risposta attesa:
1. Leggere base e RHS dal tableau finale.
2. Distinguere variazione $c_i$ da $b_i$.
3. Scrivere le disequazioni in $\Delta$ e risolverle.

Fonti:
- `06_exam_patterns/Quiz_PL_analisi_sensitivita.md`
- `10_rag/method_cards/MC_PL_analisi_sensitivita_da_tableau.md`
- `10_rag/topic_cards/TC_quiz_analisi_sensitivita.md`

Nota: fonte non ufficiale — ricalcolare le disequazioni.

---

## Pattern: Quiz PL — Casi Particolari del Simplesso

Trigger:
- "ottimo multiplo" / "ottimi alternativi"
- "degenerazione" / "degenere"
- "problema illimitato" / "illimitatezza"
- "non ammissibile" + tableau

Risposta attesa:
1. Leggere riga obiettivo: soddisfa ottimalità?
2. Cercare variabile fuori base con costo ridotto nullo (ottimo multiplo).
3. Cercare variabile base con valore zero (degenerazione).
4. Cercare colonna entrante senza elementi positivi (illimitatezza).

Fonti:
- `06_exam_patterns/Quiz_simplesso_casi_particolari.md`
- `10_rag/method_cards/MC_PL_simplesso_casi_particolari.md`
- `10_rag/topic_cards/TC_quiz_simplesso_casi_particolari.md`

---

## Pattern: Quiz PLI — Branch and Bound (lettura albero)

Trigger:
- "incumbent" + "potatura"
- "Best Bound First"
- "albero B&B" + "vero/falso"
- "prossimo nodo da sviluppare"

Risposta attesa:
1. Identificare tipo (max/min) e incumbent $Z_I$.
2. Verificare ogni potatura (dominanza / interezza / inammissibilità).
3. Determinare prossimo nodo da sviluppare.

Fonti:
- `06_exam_patterns/Quiz_PLI_Branch_and_Bound.md`
- `10_rag/method_cards/MC_PLI_branch_and_bound_quiz.md`
- `10_rag/topic_cards/TC_quiz_PLI_Branch_and_Bound.md`

---

## Pattern: Quiz PNL — Bisezione, Gradiente, Newton, KKT

Trigger:
- "bisezione" + "iterazione" o "punto medio"
- "metodo del gradiente" + "line search" + "una iterazione"
- "Newton" + "Hessiana"
- "KKT" + "vincoli attivi" + "moltiplicatori"

Risposta attesa: usare la checklist unificata del pattern.

Fonti:
- `06_exam_patterns/Quiz_PNL_bisezione_gradiente_newton_KKT.md`
- `10_rag/method_cards/MC_PNL_metodo_bisezione_1d.md`
- `10_rag/method_cards/MC_PNL_gradiente_line_search_esatta.md`
- `10_rag/method_cards/MC_PNL_newton_non_vincolata.md`
- `10_rag/method_cards/MC_PNL_KKT_generale.md`
- `10_rag/topic_cards/TC_quiz_PNL_numerica_KKT.md`

---

## Pattern: Quiz Metaeuristiche

Trigger:
- "metaeuristiche"
- "ricerca locale" / "vicinato"
- "simulated annealing" / "tabu search" / "algoritmo genetico"
- "intensificazione" / "diversificazione"

Risposta attesa: definizione sintetica validata con slide ufficiali.

Fonti:
- `06_exam_patterns/Quiz_metaeuristiche.md`
- `10_rag/method_cards/MC_Metaeuristiche_quiz.md`
- `10_rag/topic_cards/TC_quiz_metaeuristiche.md`

⚠️ Nota: fonte non ufficiale — validare con slide ufficiali.






