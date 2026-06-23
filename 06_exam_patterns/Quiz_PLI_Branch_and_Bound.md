---
type: exam-pattern
topic: programmazione_lineare_intera
status: consolidated
sources:
  - raw_assets/AAA - La bibbia di RO.pdf
reliability: non-ufficiale
---

# Quiz PLI — Branch and Bound

## Riconoscimento

Segnali nella traccia:
- "Branch and Bound"
- "albero di enumerazione"
- "bound" / "incumbent" / "$Z_I$"
- "variabili binarie" / "zaino"
- Domande vero/falso su nodi, potatura, soluzione ottima

---

## Tavola Situazione → Azione

| Situazione al nodo | Azione |
|---|---|
| Soluzione del rilassamento è **frazionaria** | Branching sulla variabile frazionaria |
| Soluzione del rilassamento è **intera** e ammissibile | Aggiorna incumbent $Z_I$ se migliore; pota per interezza |
| Bound **peggiore** dell'incumbent ($UB \le Z_I$ per max) | Pota per dominanza |
| Sotto-problema **non ammissibile** | Pota per inammissibilità |
| Bound **promettente** ($UB > Z_I$) e soluzione frazionaria | Mantieni aperto, fai branching |

---

## Procedura di Lettura di un Albero B&B

1. **Identifica il tipo** di problema (max o min).
2. **Trova l'incumbent $Z_I$**: migliore soluzione intera trovata finora.
3. **Calcola intervallo ottimo**:
   - Massimo: $[Z_I, \max UB_{\text{aperti}}]$
   - Minimo: $[\min LB_{\text{aperti}}, Z_I]$
4. **Verifica le potature**: controlla che ogni nodo chiuso rispetti la regola corretta.
5. **Best Bound First**: il prossimo nodo aperto da sviluppare ha il bound più promettente.

---

## Calcolo del Bound (Zaino 0/1)

Ordina per efficienza $v_j/p_j$ decrescente. Il bound superiore continuo (rilassamento) si calcola:
$$UB = \sum_{\text{interi}} v_j + \frac{C_{\text{residua}}}{p_{\text{critico}}} \cdot v_{\text{critico}}$$

---

## Checklist per Rispondere ai Quiz B&B

```
[ ] Ho identificato il tipo (max/min)?
[ ] Ho trovato l'incumbent corrente Z_I?
[ ] Ogni potatura è giustificata (dominanza / interezza / inammissibilità)?
[ ] Il bound di ogni nodo è calcolato con il rilassamento continuo?
[ ] Non ho aggiornato Z_I con una soluzione frazionaria?
[ ] Ho letto correttamente i vincoli aggiuntivi dei rami?
```

---

## Errori Frequenti

- ❌ Aggiornare $Z_I$ con una soluzione **frazionaria**.
- ❌ Potare un nodo con bound ancora **promettente** ($UB > Z_I$ per max).
- ❌ Confondere bound di massimo e minimo (le disuguaglianze si invertono).
- ❌ Leggere male l'albero (vincoli aggiuntivi sui rami).
- ❌ Fidarsi delle crocette/annotazioni presenti negli screenshot.

---

## Template Risposta da Esame

```
Incumbent corrente: Z_I = [...]
Nodi aperti con UB > Z_I: [elenco]

Nodo X: UB = [...] [> / <=] Z_I = [...] => [aperto / potato per dominanza]
Nodo Y: soluzione intera [Z = ...] > Z_I => Z_I aggiornato a [...]
Nodo Z: inammissibile => potato

Soluzione ottima: x* = (...), Z* = [...]
```

---

## Collegamento Method Card

→ [[MC_PLI_branch_and_bound_quiz]]
