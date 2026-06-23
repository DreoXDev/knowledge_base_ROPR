# Ingestion Report — PNL Teoria Unidimensionale e Non Vincolata

## Metadata

- Source IDs:
  - `SRC-0090` (`raw_assets/Programmazione Non Lineare/PNL 1D.pdf`)
  - `SRC-0091` (`raw_assets/Programmazione Non Lineare/PNL 2D 1.pdf`)
  - `SRC-0092` (`raw_assets/Programmazione Non Lineare/PNL 2D.pdf`)
  - `SRC-0094` (`raw_assets/Programmazione Non Lineare/PNL.pdf`)
  - `SRC-0096` (`raw_assets/Programmazione Non Lineare/PNL_nonvincolata.pdf`)
- Tipo file: PDF
- Categoria: Slide ufficiali dei docenti
- Area ROPR: Programmazione Non Lineare (PNL)
- Affidabilità: Ufficiale (official)
- Stato analisi: Completato (consolidated)

## Sintesi Contenuto

Questi asset introducono i fondamenti dell'ottimizzazione non lineare. Iniziano con le motivazioni applicative (elasticità del prezzo, economie di scala, Markowitz), per poi passare all'ottimizzazione unidimensionale (1D) analitica e numerica (bisezione, Newton 1D) e, infine, all'ottimizzazione multivariabile non vincolata (gradiente con line search esatta, Newton n-D), discutendo le proprietà geometriche ed algebriche di gradiente, matrice Hessiana, autovalori e convessità/concavità.

## Argomenti Estratti

- **Introduzione alla PNL**: Definizione del modello generale di PLN; applicazioni reali come mix di prodotti con prezzo elastico, zaino quadratico, portafoglio di Markowitz.
- **Ottimizzazione Unidimensionale**: Condizioni di ottimalità locali/globali, massimizzazione di funzioni concave ($f'(x^*) = 0$ con $f''(x^*) \le 0$).
- **Algoritmi 1D**: 
  - *Metodo di Bisezione (Dicotomico)*: Ricerca del punto in cui la derivata si annulla riducendo l'intervallo a ogni iterazione.
  - *Metodo di Newton 1D*: Approssimazione lineare locale della derivata per trovare lo zero di $f'(x)$.
- **Estensione n-dimensionale**:
  - *Gradiente ($\nabla f$)*: Vettore delle derivate parziali, direzione di massima crescita.
  - *Matrice Hessiana ($H_f$)*: Matrice simmetrica delle derivate seconde parziali.
  - *Convessità*: $H_f(x)$ definita o semidefinita positiva per ogni $x$ dello spazio $\implies$ convessa.
- **Classificazione dei Punti Stazionari (∇f = 0)**:
  - Hessiana definita positiva ($H_f \succ 0$) $\implies$ minimo locale.
  - Hessiana definita negativa ($H_f \prec 0$) $\implies$ massimo locale.
  - Hessiana indefinita (autovalori discordi) $\implies$ punto di sella.
  - Hessiana semidefinita $\implies$ condizioni del secondo ordine non sufficienti.
- **Algoritmi Multivariabili**:
  - *Metodo del Gradiente (Steepest Descent)*: Direzione di spostamento $d_k = -\nabla f(x_k)$. Line search esatta per calcolare il passo $\alpha_k$ ottimale risolvendo $\min_{\alpha \ge 0} f(x_k + \alpha d_k)$.
  - *Metodo di Newton n-D*: Direzione di spostamento $d_k = -[H_f(x_k)]^{-1} \nabla f(x_k)$ con passo $\alpha_k = 1$.

## File Creati / Aggiornati

- `05_theory/programmazione_non_lineare/00_index.md`
- `05_theory/programmazione_non_lineare/pnl_introduzione.md`
- `05_theory/programmazione_non_lineare/pnl_ottimizzazione_unidimensionale.md`
- `05_theory/programmazione_non_lineare/pnl_ottimizzazione_non_vincolata_multivariabile.md`
- `04_methods/programmazione_non_lineare/pnl_metodo_bisezione.md`
- `04_methods/programmazione_non_lineare/pnl_metodo_newton_1d.md`
- `04_methods/programmazione_non_lineare/pnl_metodo_gradiente_line_search.md`
- `04_methods/programmazione_non_lineare/pnl_metodo_newton_multivariabile.md`

## Warning / Refusi / Incongruenze Rilevate

- **Newton n-D**: Nelle slide viene accennato che si calcola l'inversa dell'Hessiano, ma a livello pratico d'esame (su foglio) si preferisce sempre risolvere il sistema lineare associato $H_f(x_k) d_k = -\nabla f(x_k)$ per evitare il calcolo esplicito della matrice inversa.
- **Divergenza della Line Search**: Viene evidenziato nei criteri di arresto che gli algoritmi di ottimizzazione non lineare possono non convergere in un numero finito di iterazioni, al contrario del simplesso per la PL. È importante indicare i criteri di arresto basati sulla norma del gradiente ($\|\nabla f(x_k)\| < \epsilon$).
