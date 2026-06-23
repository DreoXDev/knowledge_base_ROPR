---
type: method_card
topic: programmazione_lineare_intera
status: active
sources: [BB PLI.pdf]
reliability: official
---

# Method Card: Soluzioni Quasi-Ottime e Arresto B&B

## Quando Usarlo
Domande teorico-pratiche sui criteri di arresto del Branch and Bound prima della convergenza assoluta (es. tolleranza assoluta $K$, tolleranza relativa $\alpha$).

## Criteri di Quasi-Ottimalità

### 1. Tolleranza Assoluta ($K$)
Una soluzione $Z_I$ è accettata come quasi-ottima se la distanza dal miglior bound dei nodi aperti $Z_{bound}$ soddisfa:

$$
|Z_{bound} - Z_I| \le K
$$

*   **Massimo**: $Z_{bound} - Z_I \le K \implies Z_{bound} \le Z_I + K$
*   **Minimo**: $Z_I - Z_{bound} \le K \implies Z_{bound} \ge Z_I - K$

### 2. Tolleranza Relativa ($\alpha$)
Una soluzione $Z_I$ è accettata come quasi-ottima se lo scostamento percentuale soddisfa:

$$
\frac{|Z_{bound} - Z_I|}{Z_{bound}} \le \alpha
$$

*   **Massimo**: $Z_{bound} \le \frac{Z_I}{1-\alpha}$
*   **Minimo**: $Z_{bound} \ge \frac{Z_I}{1+\alpha}$

---

## Modifica alla Regola di Potatura per Dominanza
Quando si applica una tolleranza $K$ o $\alpha$, la dominanza consente di chiudere un nodo $P_i$ con bound $Z_{rel}(P_i)$ in anticipo:
*   **Massimo**: Chiudere il nodo se $Z_{rel}(P_i) \le Z_I + K$ (o $Z_{rel}(P_i) \le Z_I / (1-\alpha)$).
*   **Minimo**: Chiudere il nodo se $Z_{rel}(P_i) \ge Z_I - K$ (o $Z_{rel}(P_i) \ge Z_I / (1+\alpha)$).
