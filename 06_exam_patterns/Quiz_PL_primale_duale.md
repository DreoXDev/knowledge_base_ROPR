---
type: exam-pattern
topic: programmazione_lineare
status: consolidated
sources:
  - raw_assets/AAA - La bibbia di RO.pdf
reliability: non-ufficiale
---

# Quiz PL — Primale e Duale

## Riconoscimento

Segnali nella traccia:
- "Selezioni la/e risposta/e che ritiene vera/e"
- "soluzione ammissibile per il problema di PL"
- "soluzione ottimale per il problema di PL"
- "soluzione ammissibile per il problema duale"
- "soluzione ottimale per il problema duale"

---

## Procedura Rapida (6 passi)

1. **Identificare** se il vettore candidato è primale ($n$ componenti) o duale ($m$ componenti).
2. **Verificare non negatività** se richiesta dal dominio.
3. **Sostituire nei vincoli** del problema corrispondente.
4. **Calcolare il valore obiettivo** ($c^Tx$ per il primale, $b^Ty$ per il duale).
5. **Costruire / verificare il duale** se non è dato esplicitamente.
6. **Applicare dualità**: se primale e duale sono entrambi ammissibili con stesso valore obiettivo → entrambi ottimi (dualità forte).

---

## Checklist per Ogni Opzione

```
[ ] Il vettore ha la dimensione giusta?
[ ] Rispetta la non negatività?
[ ] Soddisfa tutti i vincoli?
[ ] È primale o duale?
[ ] Il valore obiettivo fornisce un bound valido?
[ ] Può essere ottimo per dualità forte (stessi valori primale/duale)?
```

---

## Dualità: Riepilogo Segni

Per un problema primale $\max c^Tx$ s.t. $Ax \le b$, $x \ge 0$:

$$\text{Duale: } \min b^Ty \quad \text{s.t. } A^Ty \ge c, \quad y \ge 0$$

**Dualità debole**: per qualsiasi $x$ primale ammissibile e $y$ duale ammissibile:
$$c^Tx \le b^Ty$$

**Dualità forte**: se $x^*$ e $y^*$ sono ottimi, allora $c^Tx^* = b^Ty^*$.

---

## Errori Frequenti

- ❌ Dichiarare ottimo un punto non ancora verificato come ammissibile.
- ❌ Confondere dimensione del vettore (primale ha $n$ componenti, duale $m$).
- ❌ Sbagliare i segni dei vincoli del duale.
- ❌ Confondere soluzione frazionaria (del rilassamento) con soluzione intera.
- ❌ Fidarsi delle crocette presenti negli screenshot del PDF.

---

## Template Risposta da Esame

```
Controllo le opzioni una per una.

Il vettore x = (...) ha dimensione [n/m corretta/errata].
Non negatività: [sì/no].
Vincoli primali: sostituendo ottengo [...] → [soddisfatti/violati].
Valore obiettivo primale: c^T x = [...].

Il vettore y = (...) ha dimensione [m/n corretta/errata].
Vincoli duali: sostituendo ottengo [...] → [soddisfatti/violati].
Valore obiettivo duale: b^T y = [...].

Per dualità forte: c^T x [=/</>] b^T y → [ottimi/non ottimi].

Risposte vere: [A, C, ...]
```

---

## Collegamento Method Card

→ [[MC_PL_verifica_soluzione_primale_duale]]
