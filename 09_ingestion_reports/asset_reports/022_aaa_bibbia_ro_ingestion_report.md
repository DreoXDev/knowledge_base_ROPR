---
type: ingestion-report
topic: riepilogo_generale
status: consolidated
sources:
  - raw_assets/AAA - La bibbia di RO.pdf
reliability: non-ufficiale
---

# Ingestion Report — AAA: La bibbia di RO

## Metadata

- Source ID: `SRC-0092` (`raw_assets/AAA - La bibbia di RO.pdf`)
- Tipo file: PDF di screenshot/immagini
- Categoria: Raccolta non ufficiale di quiz ed esercizi
- Area ROPR: PL (Primale/Duale, Sensitività, Simplesso), PLI (B&B), PNL (Bisezione, Gradiente, Newton, KKT), Metaeuristiche
- Affidabilità: **Non ufficiale / da validare** — composto quasi interamente da immagini
- Stato analisi: Completato (visual-only ingestion)

> ⚠️ **Nota critica**: Il PDF è formato da screenshot. Il parser testuale non estrae testo affidabile. Usare esclusivamente come eserciziario visuale e catalogo di pattern. Non usare come fonte teorica primaria. Le crocette/annotazioni presenti nelle immagini vanno **ignorate** — rifare sempre il controllo matematico.

## Sintesi Contenuto

Il file contiene 82 pagine di screenshot raccolti su vari argomenti di Ricerca Operativa, suddivisi in 9 macro-sezioni:

| Pagine (stimate) | Sezione | Area | Priorità |
|---|---|---|---|
| 1–11 | Primale / Duale | PL | Alta |
| 12–24 | Analisi di sensitività | PL | Alta |
| 25–39 | Particolari del simplesso | PL | Media-Alta |
| 40–49 | Branch and Bound | PLI | Alta |
| 50–52 | Bisezione | PNL | Media |
| 53–55 | Gradiente x,y | PNL | Media-Alta |
| 56–61 | Newton x,y | PNL | Media-Alta |
| 62–74 | KKT | PNL Vincolata | Alta |
| 75–82 | Metaeuristiche | Metaeuristiche | Media |

> I range di pagina sono approssimativi e vanno verificati manualmente sul PDF originale.

## Argomenti Estratti

- **Primale/Duale**: verifica ammissibilità, valore obiettivo, dualità debole/forte, riconoscimento ottimi tramite confronto valori
- **Sensitività**: lettura tableau finale, intervalli di variazione $c_i$ e $b_i$, condizioni di mantenimento ottimalità/ammissibilità
- **Simplesso**: degenerazione, ottimi multipli, illimitatezza, non ammissibilità, interpretazione tableau
- **B&B**: alberi di enumerazione, incumbent, potatura, scelta incumbent, domande vero/falso su nodi e bound
- **Bisezione**: punto medio, cambio di segno, criteri di arresto, uso sulla derivata $f'(x)=0$
- **Gradiente**: direzione discesa/salita, line search esatta, aggiornamento iterativo
- **Newton x,y**: gradiente, Hessiana, sistema $H s = -\nabla f$, aggiornamento
- **KKT**: vincoli attivi/inattivi, complementarità, segni moltiplicatori, candidati
- **Metaeuristiche**: ricerca locale, vicinato, intensificazione/diversificazione — da validare con fonti ufficiali

## File Creati / Aggiornati

- [AAA_bibbia_RO_catalogo_visuale.md](../../07_solved_examples/AAA_bibbia_RO_catalogo_visuale.md)
- [Quiz_PL_primale_duale.md](../../06_exam_patterns/Quiz_PL_primale_duale.md)
- [Quiz_PL_analisi_sensitivita.md](../../06_exam_patterns/Quiz_PL_analisi_sensitivita.md)
- [Quiz_simplesso_casi_particolari.md](../../06_exam_patterns/Quiz_simplesso_casi_particolari.md)
- [Quiz_PLI_Branch_and_Bound.md](../../06_exam_patterns/Quiz_PLI_Branch_and_Bound.md)
- [Quiz_PNL_bisezione_gradiente_newton_KKT.md](../../06_exam_patterns/Quiz_PNL_bisezione_gradiente_newton_KKT.md)
- [Quiz_metaeuristiche.md](../../06_exam_patterns/Quiz_metaeuristiche.md)
- [MC_PL_verifica_soluzione_primale_duale.md](../../10_rag/method_cards/MC_PL_verifica_soluzione_primale_duale.md)
- [MC_PL_analisi_sensitivita_da_tableau.md](../../10_rag/method_cards/MC_PL_analisi_sensitivita_da_tableau.md)
- [MC_PL_simplesso_casi_particolari.md](../../10_rag/method_cards/MC_PL_simplesso_casi_particolari.md)
- [MC_PLI_branch_and_bound_quiz.md](../../10_rag/method_cards/MC_PLI_branch_and_bound_quiz.md)
- [MC_Metaeuristiche_quiz.md](../../10_rag/method_cards/MC_Metaeuristiche_quiz.md)
- [TC_quiz_PL_primale_duale.md](../../10_rag/topic_cards/TC_quiz_PL_primale_duale.md)
- [TC_quiz_analisi_sensitivita.md](../../10_rag/topic_cards/TC_quiz_analisi_sensitivita.md)
- [TC_quiz_simplesso_casi_particolari.md](../../10_rag/topic_cards/TC_quiz_simplesso_casi_particolari.md)
- [TC_quiz_PLI_Branch_and_Bound.md](../../10_rag/topic_cards/TC_quiz_PLI_Branch_and_Bound.md)
- [TC_quiz_PNL_numerica_KKT.md](../../10_rag/topic_cards/TC_quiz_PNL_numerica_KKT.md)
- [TC_quiz_metaeuristiche.md](../../10_rag/topic_cards/TC_quiz_metaeuristiche.md)
- [Quiz_PL_primale_duale_flashcards.md](../../08_flashcards/Quiz_PL_primale_duale_flashcards.md)
- [Quiz_sensitivita_flashcards.md](../../08_flashcards/Quiz_sensitivita_flashcards.md)
- [Quiz_simplesso_flashcards.md](../../08_flashcards/Quiz_simplesso_flashcards.md)
- [Quiz_BB_flashcards.md](../../08_flashcards/Quiz_BB_flashcards.md)
- [Quiz_PNL_flashcards.md](../../08_flashcards/Quiz_PNL_flashcards.md)
- [Quiz_metaeuristiche_flashcards.md](../../08_flashcards/Quiz_metaeuristiche_flashcards.md)
