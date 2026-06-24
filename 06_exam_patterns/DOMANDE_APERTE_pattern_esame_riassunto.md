---
type: exam-pattern
topic: teoria_generale
status: consolidated
---

# DOMANDE APERTE — Pattern Risposta da Esame

## Formula Generale

```
Definizione → Formula/Modello → Commento termini → Interpretazione → Osservazione finale
```

Stile: studente preparato, conciso, nessuna frase informale, LaTeX per le formule.

---

## Domande PL

| Domanda tipica | Risposta breve | Approfondimento |
|---|---|---|
| Proprietà vertici ammissibili | 1) ottimo in un vertice; 2) numero finito; 3) ottimalità locale=globale | [[PL_domande_aperte_vertici_basi_dualita]] |
| Soluzione di base ammissibile | $x_B = B^{-1}b \ge 0$; BFS = vertice | [[MC_PL_vertici_soluzioni_base]] |
| Numero max soluzioni di base | $\binom{n+m}{m}$ in forma aumentata | [[MC_PL_vertici_soluzioni_base]] |
| Dualità forte | $c^Tx^* = b^Ty^*$ se entrambi hanno ottimo finito | [[MC_PL_dualita_forte_debole]] |
| Dualità debole | $c^Tx \le b^Ty$ per ogni coppia ammissibile (max primale) | [[MC_PL_dualita_forte_debole]] |
| Complementarità | $y_i(b_i - a_i^Tx^*)=0$ e $x_j(a_j^Ty^* - c_j)=0$ | [[PL_complementary_slackness]] |
| Simplesso — direzione | Variabile entrante: costo ridotto favorevole | [[MC_PL_simplesso_direzione_incremento]] |
| Simplesso — incremento | Test minimo rapporto: $\theta^* = \min_{d_i>0}\bar{x}_{B_i}/d_i$ | [[MC_PL_simplesso_direzione_incremento]] |

---

## Domande PLI

| Domanda tipica | Risposta breve | File |
|---|---|---|
| Rilassamento continuo e TUM | Se matrice TUM e b intero → ottimo intero | [[MC_PL_totale_unimodularita_rilassamento]] |
| B&B — quando si pota | Inammissibilità / bound ≤ incumbent / soluzione intera | [[MC_PLI_branch_and_bound]] |

---

## Domande PNL

| Domanda tipica | Risposta breve | File |
|---|---|---|
| Condizioni KKT (cosa sono) | Cond. necessarie: stazionarietà + amm. primale + amm. duale + complementarità | [[PNL_domande_aperte_KKT]] |
| A cosa servono le KKT | Generalizzano Lagrange ai vincoli di disuguaglianza | [[MC_PNL_KKT_generale]] |
| Sono sufficienti? | No (in generale); sì se f convessa + vincoli convessi (min) | [[MC_PNL_KKT_generale]] |

---

## Domande Reti

| Domanda tipica | Risposta breve | File |
|---|---|---|
| Formulazione trasporto | $\min \sum c_{ij}x_{ij}$, v. offerta e domanda | [[MC_RETI_trasporto_transhipment]] |
| Offerta > domanda | Aggiungere destinazione fittizia con surplus, costo 0 | [[MC_RETI_trasporto_transhipment]] |
| Flusso costo minimo | Bilanciamento per nodo $= b_v$, capacità $u_{ij}$ | [[MC_RETI_flusso_costo_minimo]] |
| Massimo flusso | $\max f$, bilanciamento s/t/transito | [[MC_RETI_massimo_flusso]] |
| Cammino minimo | $x_{ij}\in\{0,1\}$, bilanciamento $\pm 1$ | [[MC_RETI_cammino_minimo]] |

---

## Domande Metaeuristiche

| Domanda tipica | Risposta breve | File |
|---|---|---|
| Cos'è una metaeuristica | Strategia generale, no garanzia ottimo globale | [[MC_METAEURISTICHE_algoritmi_genetici]] |
| Crossover vs mutazione | Crossover: combina; mutazione: modifica casuale | [[MC_METAEURISTICHE_algoritmi_genetici]] |
| SA — temperatura e exploration | T alta → exploration; T bassa → exploitation | [[MC_METAEURISTICHE_simulated_annealing]] |
| SA — formula accettazione (min) | $p = \exp(-\Delta f/T)$ con $\Delta f > 0$ | [[MC_METAEURISTICHE_simulated_annealing]] |
| TS — tabu list | Vieta mosse recenti; aggiornamento FIFO | [[MC_METAEURISTICHE_tabu_search]] |
| TS — criterio di aspirazione | Ignora tabu se migliora il best globale $x^*$ | [[MC_METAEURISTICHE_tabu_search]] |

---

## Errori da Evitare

- ❌ Copiare bozze informali senza riscriverle.
- ❌ Non definire i simboli nelle formule.
- ❌ Confondere condizioni necessarie con sufficienti (KKT, dualità debole).
- ❌ Formula SA senza distinzione min/max.
- ❌ Non specificare il dominio delle variabili nei modelli.
- ❌ Risposta prolissa senza struttura.

---

## Template da Esame

```
[Definizione]:   [1-2 righe precise]
[Formula]:       [LaTeX se necessario]
[Interpretazione]: [1 frase operativa]
[Osservazione]:  [limite, caso speciale, errore comune]
```

→ [[MC_TEORIA_risposta_aperta]]
→ [[Domande_aperte_risposte_modello]]
