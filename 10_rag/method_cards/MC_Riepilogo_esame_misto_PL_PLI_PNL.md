# Method Card: Tabella di Instradamento Riepilogo Esame (PL, PLI, PNL)

## Quando usarla
Da usare in presenza di un compito d'esame misto o di riepilogo generale per identificare istantaneamente l'area matematica del quesito, le method card di riferimento ed i passi risolutivi.

---

## Tabella di Instradamento

| Segnale Testuale nella Traccia | Area Matematica | Tecnica da Applicare | Prima Fonte di Riferimento | Seconda Fonte di Riferimento |
|---|---|---|---|---|
| "stabilimenti", "punti vendita", "spedizioni", "minimizzare i costi di trasporto" | **Programmazione Lineare (PL)** | Modello di trasporto | [[MC_PL_modello_trasporto]] | [[riepilogo_pl_pli_pnl_esercizi_misti]] |
| "problema dello zaino", "Branch and Bound", "$x_i \in \{0, 1\}$", "visita in ampiezza" | **Programmazione Lineare Intera (PLI)** | B&B Zaino Binario | [[MC_PLI_branch_and_bound_zaino]] | [[riepilogo_pl_pli_pnl_esercizi_misti]] |
| "metodo del gradiente con line search esatta", "Newton non vincolato" | **Programmazione Non Lineare (PNL)** | Ottimizzazione non vincolata | [[MC_PNL_gradiente_line_search_esatta]] e [[MC_PNL_newton_non_vincolata]] | [[riepilogo_pl_pli_pnl_esercizi_misti]] |
| "massimi e minimi locali di f(x, y)", "punti stazionari" | **Programmazione Non Lineare (PNL)** | Gradiente nullo + Hessiana | [[MC_PNL_classificazione_hessiana]] | [[pnl_non_vincolata_esercizi_punti_stazionari]] |
| "massimi e minimi globali della funzione f(x, y) sull'insieme", "sistema KKT" | **Programmazione Non Lineare (PNL)** | KKT vincolata per casi | [[MC_PNL_KKT_generale]] | [[pnl_vincolata_esercizi_kkt_globali]] |

---

## Linee Guida Operative d'Esame

1.  **Fase 1: Categorizzazione**: Leggere la traccia e individuare le parole chiave per stabilire se si tratta di PL (continua), PLI (intera/binaria) o PNL (non lineare).
2.  **Fase 2: Selezione della Method Card**: Cliccare sul link della method card associata nella tabella soprastante.
3.  **Fase 3: Svolgimento ed Esame dei Casi**:
    -   Se KKT, impostare la tabella riassuntiva dei casi.
    -   Se B&B, tracciare l'albero di branching.
    -   Se PL, formalizzare accuratamente le variabili e i vincoli lineari.
4.  **Fase 4: Controllo di Coerenza**: Verificare i segni dei moltiplicatori duali e l'ammissibilità dei punti prima di dichiarare la soluzione finale.
