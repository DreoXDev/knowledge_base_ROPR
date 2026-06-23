---
type: topic-card
topic: programmazione_non_lineare
status: consolidated
sources:
  - raw_assets/AAA - La bibbia di RO.pdf
reliability: non-ufficiale
---

# TC: Quiz PNL — Bisezione, Gradiente, Newton, KKT

## Trigger

Usa questo topic card quando la query contiene:
- "bisezione" + "iterazione" o "intervallo"
- "gradiente" + "line search" o "una iterazione"
- "Newton" + "Hessiana" o "sistema"
- "KKT" + "vincoli attivi" o "moltiplicatori"
- "quiz" + "risposta multipla" + PNL

## File da consultare

1. [Quiz_PNL_bisezione_gradiente_newton_KKT.md](../../06_exam_patterns/Quiz_PNL_bisezione_gradiente_newton_KKT.md) — pattern unificato con checklist
2. [MC_PNL_metodo_bisezione_1d.md](../method_cards/MC_PNL_metodo_bisezione_1d.md)
3. [MC_PNL_gradiente_line_search_esatta.md](../method_cards/MC_PNL_gradiente_line_search_esatta.md)
4. [MC_PNL_newton_non_vincolata.md](../method_cards/MC_PNL_newton_non_vincolata.md)
5. [MC_PNL_KKT_generale.md](../method_cards/MC_PNL_KKT_generale.md)

## Note

- Fonte non ufficiale: ricalcolare sempre, non fidarsi delle crocette negli screenshot.
- Per bisezione: verificare cambio di segno su $f'$ prima di ogni iterazione.
- Per KKT: segno dei moltiplicatori è $\mu_j \ge 0$ per min, $\mu_j \le 0$ per max.
