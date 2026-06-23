---
type: exercise_catalog
topic: programmazione_lineare_intera
status: active
sources: [9_esercizi_modelli.pdf]
reliability: official
---

# Esercizi di Modellazione PLI

Raccolta dei testi ed elementi risolutivi per i 9 esercizi di modellazione.

---

## Esercizio 1: Rimpiazzo Fotocopiatrici
*   **Testo**: Pianificare rimpiazzo e manutenzione fotocopiatrice per 4 anni. Costi manutenzione: anno 1 (500), anno 2 (1000), anno 3 (1500), anno 4 (2100). Sostituzione nuova costa 1600. Minimizzare costo totale formulando come cammino minimo su grafo.
*   **Modello**: Grafo orientato aciclico con nodi che rappresentano lo stato all'inizio di ciascun anno. Nodo 1 (Anno 1), Nodo 6 (Fittizio finale).
*   **Costi Archi**:
    *   Archi di acquisto e manutenzione per il primo anno d'uso: $c(i, i+1) = 1600 + 500 = 2100$ per ogni anno $i$.
    *   Archi di mantenimento per anni d'uso consecutivi: $c(2, 3b) = 1000$ (manutenzione secondo anno d'uso), $c(3, 4d) = 1500$ (manutenzione terzo anno d'uso), ecc.
*   **Soluzione**: Risoluzione come cammino minimo da 1 a 6.

---

## Esercizio 2: Smistamento Automobili
*   **Testo**: Smistamento auto da porti $P_1, P_2, P_3$ a centri $S_1, S_2, S_3, S_4$. Capacità porti: $350, 200, 300$. Richieste centri: $170, 130, 100, 200$. Costi variabili di trasporto + tasse portuali.
*   **Vincoli Speciali**:
    *   $S_3$ rifornito da un solo porto.
    *   Se $P_2$ serve $S_2$, allora deve servire anche $S_4$.
*   **Esempio Svolto Completo**: [pli_modellazione_smistamento_automobili.md](../../07_solved_examples/programmazione_lineare_intera/pli_modellazione_smistamento_automobili.md).

---

## Esercizio 3: Apertura Filiali Assicurazione
*   **Testo**: Aprire $p$ filiali per servire $n$ clienti. Volume lavoro cliente $i$ è $d_i$ ore/mese. Ogni dipendente lavora $L$ ore/mese. Ogni filiale $j$ deve avere dipendenti tra $m_j$ e $M_j$. Assegnare ogni cliente ad una sola filiale, minimizzando i dipendenti assunti.
*   **Variabili**:
    *   $x_{ij} = 1$ se cliente $i$ assegnato a filiale $j$, $0$ altrimenti.
    *   $y_j \in \mathbb{Z}_+$ numero dipendenti assunti nella filiale $j$.
    *   $z_j = 1$ se filiale $j$ aperta, $0$ altrimenti.
*   **Modello**:
    *   Obiettivo: $\min \sum_j y_j$
    *   Assegnamento clienti: $\sum_j x_{ij} = 1 \quad \forall i$
    *   Ore lavorate e dipendenti: $\sum_i d_i x_{ij} \le L y_j \quad \forall j$
    *   Numerosità dipendenti: $m_j z_j \le y_j \le M_j z_j \quad \forall j$
    *   Attivazione filiale: $x_{ij} \le z_j \quad \forall i, j$

---

## Esercizio 4: Asili Nido Montani
*   **Testo**: Aprire al massimo $p$ asili nido nei paesi $i \in I$. Paese $i$ ha $b_i$ bambini. Tutti i bambini di un paese vanno allo stesso nido. Trasporto scolastico costa $c_{ij}$ all'anno. Educatore costa $g$ euro/anno. Rapporto: 1 educatore ogni $q$ bambini. Minimizzare costi di trasporto + personale.
*   **Esempio Svolto Completo**: [pli_modellazione_asili_nido_montani.md](../../07_solved_examples/programmazione_lineare_intera/pli_modellazione_asili_nido_montani.md).

---

## Esercizio 5: Posizionamento Macchine Officina
*   **Testo**: Posizionare 3 macchine $M_1, M_2, M_3$ in 4 spazi $S_1, S_2, S_3, S_4$. $S_2$ non adatto a $M_2$. $S_4$ può ospitare fino a 2 macchine. Minimizzare costo orario di movimentazione.
*   **Variabili**:
    *   $x_{ij} = 1$ se macchina $M_i$ in spazio $S_j$, $0$ altrimenti.
*   **Modello**:
    *   Obiettivo: $\min \sum_i \sum_j c_{ij} x_{ij}$
    *   Ogni macchina in una sola posizione: $\sum_j x_{ij} = 1 \quad \forall i=1, 2, 3$
    *   Capacità posizioni: $\sum_i x_{ij} \le 1 \quad \forall j=1, 2, 3$ e $\sum_i x_{i4} \le 2$
    *   Incompatibilità: $x_{22} = 0$

---

## Esercizio 6 & 7: Rifornimento Agende
*   **Testo**: Cartolerie $C_1, C_2$ acquistano agende da fornitori $F_1, F_2, F_3, F_4$. Costi unitari di trasporto, capacità fornitori, requisiti minimi e stoccaggio. Costo fisso per fornitore.
*   **Vincoli Speciali**:
    *   Al massimo 3 fornitori diversi per $C_1$.
    *   Acquisto minimo da $F_4$ di 40 agende (se scelto).
    *   $F_1$ vende solo in pacchi da 20 agende.
    *   $F_2$ dimezza il costo fisso se l'ordine complessivo è $\ge 60$.
*   **Esempio Svolto Completo**: [pli_modellazione_rifornimento_agende.md](../../07_solved_examples/programmazione_lineare_intera/pli_modellazione_rifornimento_agende.md).

---

## Esercizio 8 & 9: Stendino di Remo
*   **Testo**: Remo deve posizionare 9 indumenti (con lunghezza $L_i$ e peso $P_i$) su 4 file di stendino lunghe $110$ cm.
*   **Vincoli Speciali**:
    *   Bilanciamento pesi: peso complessivo file esterne (1 e 4) $\le$ peso totale file interne (2 e 3).
    *   Minimizzare il numero di file utilizzate.
    *   Vincoli logici aggiuntivi (almeno 5 capi stesi, almeno 2 da mare OR almeno 3 dei primi 4, telo da spiaggia solo se almeno un costume).
*   **Esempio Svolto Completo**: [pli_modellazione_stendino_remo.md](../../07_solved_examples/programmazione_lineare_intera/pli_modellazione_stendino_remo.md).
