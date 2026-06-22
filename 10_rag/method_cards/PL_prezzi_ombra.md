---
materia: ROPR
area: Programmazione Lineare
tipo: metodo
fonte: Ricerca Operativa - Teoria della Dualità.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - dualita
  - prezzi-ombra
  - analisi-sensitivita
  - method-card
---

# METHOD CARD — Prezzi Ombra e Interpretazione Economica

## Quando usarla
Usare questa card per rispondere a domande d'esame sui prezzi ombra, sul valore marginale delle risorse e sull'interpretazione economica del duale.

## Idee e Definizioni Chiave

1. **Prezzo Ombra (Shadow Price)**: Il prezzo ombra della risorsa $i$-esima (indicato con $y_i^*$) misura il tasso di variazione del valore ottimo della funzione obiettivo $Z^*$ al variare marginale della disponibilità della risorsa $b_i$:
   $$
   y_i^* = \frac{\partial Z^*}{\partial b_i}
   $$
2. **Interpretazione Economica**:
   - $y_i^*$ rappresenta il valore marginale o valore unitario della risorsa $i$. Indica il massimo prezzo che conviene pagare per acquistare una unità aggiuntiva di quella risorsa.
   - All'ottimo, il valore totale delle risorse (valutate ai prezzi ombra) uguaglia il valore ottimale della produzione: $W^* = Z^*$.
3. **Lettura dal Tableau**: Il prezzo ombra $y_i^*$ è leggibile come coefficiente della variabile di slack $s_i$ nella riga 0 del tableau ottimo del simplesso primale (per problemi MAX).

## Risposta da Esame Standard

Il **prezzo ombra** di una risorsa è definito come il tasso incrementale del valore ottimo della funzione obiettivo per unità di incremento della disponibilità della risorsa stessa. Algebricamente coincide con il valore ottimo della corrispondente variabile duale $y_i^*$. Se il prezzo ombra è strettamente positivo ($y_i^* > 0$), significa che la risorsa è scarsa (il vincolo è attivo e lo slack $s_i^* = 0$). Se la risorsa non è completamente utilizzata ($s_i^* > 0$), il suo prezzo ombra è nullo ($y_i^* = 0$).
