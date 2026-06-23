---
type: theory
topic: programmazione_lineare_intera
status: active
sources: [9_esercizi_modelli.pdf, 16_esercizi_BB.pdf]
reliability: official
---

# Tassonomia Tipologie Esercizi (PLI)

Questo file categorizza le tipologie di esercizi presenti nelle raccolte ufficiali, indicando le tecniche di modellazione e le strategie algoritmiche richieste.

## 1. Modellazione PLI Pura e Applicativa

### A. Modelli di Rete e Cammino Minimo
*   **Caratteristiche**: Il problema richiede di pianificare scelte sequenziali (es. acquisto/manutenzione di macchinari negli anni) modellabili come percorso a costo minimo su grafo orientato acyclico (DAG).
*   **Esercizi**: [Modellazione Esercizio 1](by_topic/pli_modellazione_esercizi.md#esercizio-1).

### B. Assegnamento e Smistamento con Vincoli Logici
*   **Caratteristiche**: Invio di merci da origini a destinazioni (trasporto) in presenza di vincoli di attivazione e vincoli condizionali di tipo se-allora (es. se porto A serve porto B, allora...).
*   **Esercizi**: [Modellazione Esercizio 2](by_topic/pli_modellazione_esercizi.md#esercizio-2), [Modellazione Esercizio 5](by_topic/pli_modellazione_esercizi.md#esercizio-5).

### C. Localizzazione e Assegnamento Clienti (Facility Location)
*   **Caratteristiche**: Scelta di quali strutture aprire (con costo fisso) e assegnamento di clienti, considerando vincoli di capacità e/o personale (educatori, dipendenti).
*   **Esercizi**: [Modellazione Esercizio 3](by_topic/pli_modellazione_esercizi.md#esercizio-3), [Modellazione Esercizio 4](by_topic/pli_modellazione_esercizi.md#esercizio-4).

### D. Problemi di Trasporto con Costi Fissi e Sconti
*   **Caratteristiche**: Trasporto di merci con capacità di stoccaggio, lotti discreti di acquisto (es. multipli di 20) e costi fissi attivabili o dimezzabili condizionalmente.
*   **Esercizi**: [Modellazione Esercizio 6](by_topic/pli_modellazione_esercizi.md#esercizio-6), [Modellazione Esercizio 7](by_topic/pli_modellazione_esercizi.md#esercizio-7).

### E. Bin Packing e Bilanciamento Pesi (Stendino)
*   **Caratteristiche**: Suddivisione di oggetti di lunghezze diverse su un numero fisso di file (stendino/bin packing) con l'obiettivo di minimizzare le file utilizzate e vincoli fisici di bilanciamento del peso (momenti/baricentro).
*   **Esercizi**: [Modellazione Esercizio 8](by_topic/pli_modellazione_esercizi.md#esercizio-8), [Modellazione Esercizio 9](by_topic/pli_modellazione_esercizi.md#esercizio-9).

---

## 2. Esercizi Algoritmici

### A. Branch and Bound Standard (2 Variabili)
*   **Caratteristiche**: Risoluzione algebrica di massimizzazioni bidimensionali. Si parte dal rilassamento continuo e si ramifica per interezza visitando in ampiezza.
*   **Esercizi**: [B&B Esercizi 1-11](by_topic/pli_branch_and_bound_esercizi.md#esercizi-standard).

### B. Zaino Binario (Knapsack) con Greedy B&B
*   **Caratteristiche**: Selezione ottima di oggetti sotto vincolo di peso. Calcolo dell'Upper Bound con il rilassamento continuo (greedy continuo) e del Lower Bound con l'euristica dei rendimenti (greedy intero).
*   **Esercizi**: [B&B Esercizi 12-16](by_topic/pli_branch_and_bound_esercizi.md#problemi-dello-zaino).
