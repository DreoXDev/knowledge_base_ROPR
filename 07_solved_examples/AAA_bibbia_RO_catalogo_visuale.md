---
type: solved-example
topic: riepilogo_generale
status: consolidated
sources:
  - raw_assets/AAA - La bibbia di RO.pdf
reliability: non-ufficiale
---

# AAA — La bibbia di RO: Catalogo Visuale

> ⚠️ **Avvertenza**: Questo file è composto da screenshot/immagini non OCR. Usarlo come raccolta di pattern e tipi di domanda, **non** come fonte primaria di teoria o risposte. Le crocette presenti negli screenshot originali vanno **ignorate** — rifare sempre la verifica matematica.

Fonte: `raw_assets/AAA - La bibbia di RO.pdf`
Tipo: raccolta non ufficiale di screenshot di quiz/esercizi (82 pagine)
Affidabilità: media per pattern, bassa per teoria

---

## Macro-Indice

| Sezione | Pagine stimate | Tipo domanda | Method card | Note |
|---|---|---|---|---|
| Primale / Duale | 1–11 | Risposta multipla, vero/falso | [MC_PL_verifica_soluzione_primale_duale](../10_rag/method_cards/MC_PL_verifica_soluzione_primale_duale.md) | Verificare dimensione, ammissibilità, valore obiettivo |
| Analisi di sensitività | 12–24 | Intervallo di variazione $\Delta$ | [MC_PL_analisi_sensitivita_da_tableau](../10_rag/method_cards/MC_PL_analisi_sensitivita_da_tableau.md) | Distinguere variazione $c_i$ da $b_i$ |
| Particolari del simplesso | 25–39 | Riconoscimento caso da tableau | [MC_PL_simplesso_casi_particolari](../10_rag/method_cards/MC_PL_simplesso_casi_particolari.md) | Leggere riga obiettivo e base |
| Branch and Bound | 40–49 | Lettura albero, vero/falso | [MC_PLI_branch_and_bound_quiz](../10_rag/method_cards/MC_PLI_branch_and_bound_quiz.md) | Incumbent, potatura, bound |
| Bisezione | 50–52 | Iterazioni numeriche | [MC_PNL_metodo_bisezione_1d](../10_rag/method_cards/MC_PNL_metodo_bisezione_1d.md) | Cambio di segno su $f'(x)$ |
| Gradiente x,y | 53–55 | Una iterazione, line search | [MC_PNL_gradiente_line_search_esatta](../10_rag/method_cards/MC_PNL_gradiente_line_search_esatta.md) | Direzione $-\nabla f$ |
| Newton x,y | 56–61 | Una iterazione, Hessiana | [MC_PNL_newton_non_vincolata](../10_rag/method_cards/MC_PNL_newton_non_vincolata.md) | Sistema $H s = -\nabla f$ |
| KKT | 62–74 | Verifica candidati KKT | [MC_PNL_KKT_generale](../10_rag/method_cards/MC_PNL_KKT_generale.md) | Complementarità, segni $\mu$ |
| Metaeuristiche | 75–82 | Domande teoriche | [MC_Metaeuristiche_quiz](../10_rag/method_cards/MC_Metaeuristiche_quiz.md) | ⚠️ Da validare con fonti ufficiali |

---

## Primale / Duale (pp. 1–11)

**Tipo di domanda**: Dato un vettore $x$ o $y$, selezionare le risposte vere tra:
- soluzione ammissibile per il primale
- soluzione ottimale per il primale
- soluzione ammissibile per il duale
- soluzione ottimale per il duale

**Procedura**:
1. Identificare se il vettore è primale (dimensione $n$) o duale (dimensione $m$).
2. Verificare non negatività (se richiesta).
3. Sostituire nei vincoli primali/duali.
4. Calcolare valore obiettivo.
5. Confrontare valori primale/duale per dualità forte.

**Errori tipici**: punto non ammissibile dichiarato ottimo; dimensione del vettore errata; segni vincoli duale sbagliati.

---

## Analisi di Sensitività (pp. 12–24)

**Tipo di domanda**: Dato un tableau finale, trovare l'intervallo ammissibile di variazione $\Delta$ per un coefficiente $c_i$ o termine noto $b_i$.

**Procedura**:
- Per $c_i$: imporre che i costi ridotti mantengano il segno di ottimalità.
- Per $b_i$: aggiornare $x_B(\Delta) = \bar{b} + \Delta \cdot d \ge 0$ e risolvere le disequazioni.

**Formule chiave**:
$$x_B(\Delta) = \bar{b} + \Delta \cdot d \ge 0 \quad \text{(variazione } b_i\text{)}$$
$$\bar{c}_j(\Delta) \ge 0 \quad \text{(variazione } c_i\text{, per max)}$$

---

## Particolari del Simplesso (pp. 25–39)

**Tipo di domanda**: Dato un tableau finale, riconoscere il caso particolare presente.

| Caso | Segnale nel tableau |
|---|---|
| Ottimo multiplo | Costo ridotto nullo per variabile fuori base |
| Degenerazione | Variabile di base con valore zero |
| Illimitatezza | Colonna variabile entrante senza elementi positivi |
| Non ammissibilità | RHS negativo dopo pivot / Fase 1 con $W^*>0$ |

---

## Branch and Bound (pp. 40–49)

**Tipo di domanda**: Dato un albero B&B, rispondere su incumbent, bound, potatura, soluzione ottima.

**Regole chiave**:
- Soluzione frazionaria → branching
- Soluzione intera ammissibile → aggiorna incumbent
- Bound $\le Z_I$ (per max) → pota per dominanza
- Inammissibile → pota

---

## Bisezione (pp. 50–52)

**Tipo di domanda**: Dato $f(x)$ e intervallo $[a,b]$, eseguire $k$ iterazioni di bisezione su $f'(x)=0$.

**Schema**: $x_{k+1} = \frac{a_k+b_k}{2}$; aggiorna in base al segno di $f'(x_{k+1})$.

---

## Gradiente (pp. 53–55)

**Tipo di domanda**: Una iterazione del metodo del gradiente con line search esatta.

**Schema**: $d_k = -\nabla f(x_k)$; $x(\alpha) = x_k + \alpha d_k$; minimizza $\phi(\alpha)$.

---

## Newton x,y (pp. 56–61)

**Tipo di domanda**: Una iterazione del metodo di Newton in due variabili.

**Schema**: Risolvi $H_f(x_k) s_k = -\nabla f(x_k)$; $x_{k+1} = x_k + s_k$.

---

## KKT (pp. 62–74)

**Tipo di domanda**: Verifica/ricerca candidati KKT per PNL vincolata.

**Schema**: Forma standard → Lagrangiana → sistema KKT → enumerazione casi attivi/inattivi → filtro $\mu_j \ge 0$.

---

## Metaeuristiche (pp. 75–82)

> ⚠️ **Validare con slide ufficiali prima di usare le risposte.**

**Temi ricorrenti (da validare)**:
- Euristiche vs algoritmi esatti
- Ricerca locale e vicinato
- Escape da ottimi locali (simulated annealing, tabu search)
- Intensificazione vs diversificazione
- Algoritmi genetici

Vedi: [[Quiz_metaeuristiche]] e [[MC_Metaeuristiche_quiz]]

---

## Collegamenti

- [[Quiz_PL_primale_duale]]
- [[Quiz_PL_analisi_sensitivita]]
- [[Quiz_simplesso_casi_particolari]]
- [[Quiz_PLI_Branch_and_Bound]]
- [[Quiz_PNL_bisezione_gradiente_newton_KKT]]
- [[Quiz_metaeuristiche]]
