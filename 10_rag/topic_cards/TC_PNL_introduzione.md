# Topic Card: Introduzione alla Programmazione Non Lineare

- **Definizione**: Ottimizzazione di funzioni non lineari $f(x)$ soggette a vincoli non lineari.
- **Applicazioni Chiave**:
  - *Prezzo Elastico*: $p(x) = d - cx \implies R(x) = dx - cx^2$ (ricavo quadratico).
  - *Economie di Scala*: costi marginali decrescenti dovuti a curve di apprendimento o sconti quantità.
  - *Zaino Quadratico*: include profitto extra $c_{ij}x_i x_j$ se entrambi gli oggetti $i, j$ sono selezionati.
  - *Markowitz*: minimizzazione rischio portafoglio (varianza: forma quadratica $\sum \sigma_{ij}x_i x_j$) dato un rendimento atteso minimo.
- **Confronto con PL**: I punti di ottimo non si trovano necessariamente sui vertici della regione ammissibile, ma possono trovarsi all'interno o lungo i bordi. Non è garantita la convergenza in passi finiti per i metodi iterativi.
- **Fonti principali**: [[pnl_introduzione|Teoria PNL Introduzione]]
