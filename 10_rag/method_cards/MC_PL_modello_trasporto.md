# Method Card: Modello di Trasporto (PL)

## Quando usarla
Da usare per formulare problemi di programmazione lineare legati alla logistica e distribuzione, in cui vi sono stabilimenti di produzione (sorgenti) con capacità massima e punti vendita/clienti (destinazioni) con domanda minima da soddisfare.

## Input tipico dell'esercizio
- Insieme di stabilimenti $S_i$ con capacità produttiva massima $c_i$.
- Insieme di punti vendita $P_j$ con domanda minima $d_j$.
- Tabella delle distanze $d_{ij}$ o dei costi unitari di spedizione $c_{ij}$ per ogni coppia $(S_i, P_j)$.

## Output richiesto
- Definizione delle variabili decisionali (quantità trasportata).
- Funzione obiettivo di minimizzazione dei costi totali.
- Vincoli di capacità degli stabilimenti ($\le$).
- Vincoli di domanda dei clienti ($\ge$).
- Vincoli di non negatività.
- Eventuali modifiche al modello base.

## Procedura in 4 passi
1.  **Definizione Variabili**: Definire la quantità da spedire:
    $$x_{ij} = \text{quantità di prodotto spedita da } S_i \text{ a } P_j, \quad \forall i, j$$
2.  **Funzione Obiettivo**: Calcolare i coefficienti di costo $c_{ij}$ (se viene data la distanza, moltiplicare la distanza per la tariffa al km). Formulare l'obiettivo:
    $$\min \sum_i \sum_j c_{ij} x_{ij}$$
3.  **Vincoli**:
    -   **Capacità**: La somma di quanto spedito da ciascuno stabilimento non deve superare la sua capacità:
        $$\sum_j x_{ij} \le c_i \quad \forall i$$
    -   **Domanda**: La somma di quanto ricevuto da ciascun punto vendita deve soddisfare la sua domanda:
        $$\sum_i x_{ij} \ge d_j \quad \forall j$$
4.  **Dominio**: $x_{ij} \ge 0$.

## Modifiche Frequenti (Procedura d'Esame)
-   **Capacità residua / inutilizzata**: La capacità residua dello stabilimento $k$ deve essere $\le R$ $\implies c_k - \sum_j x_{kj} \le R \implies \sum_j x_{kj} \ge c_k - R$.
-   **Vincolo di bilanciamento delle distanze**: La distanza complessiva percorsa dai veicoli dello stabilimento $A$ deve essere $\le$ di una frazione $\gamma$ di quella degli altri stabilimenti:
    $$\sum_j d_{Aj} x_{Aj} \le \gamma \left( \sum_{i \ne A} \sum_j d_{ij} x_{ij} \right)$$

## Errori frequenti
-   **Invertire i vincoli di capacità e domanda**: Utilizzare $\ge$ per le capacità (che invece sono limiti massimi $\le$) o $\le$ per le domande (che sono requisiti minimi $\ge$).
-   **Non linearizzare i vincoli frazionari**: Lasciare termini variabili al denominatore. Portarli sempre al numeratore per via algebrica lineare.
