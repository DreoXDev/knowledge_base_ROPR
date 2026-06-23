# Method Card: Condizioni KKT Generali

## Quando usarla
Da usare come quadro teorico e metodologico unificato per trovare i candidati all'ottimalità locale e globale in problemi di programmazione non lineare soggetti a vincoli di uguaglianza e disuguaglianza.

## Input tipico dell'esercizio
- Funzione obiettivo $f(x)$ da minimizzare o massimizzare.
- Vincoli di uguaglianza $g_i(x) = 0, \quad i = 1, \dots, m$.
- Vincoli di disuguaglianza $h_j(x) \le 0, \quad j = 1, \dots, p$.

## Output richiesto
- Formulazione standard del problema.
- Lagrangiana generalizzata: $L(x, \lambda, \mu) = f(x) + \sum \lambda_i g_i(x) + \sum \mu_j h_j(x)$.
- Condizioni di stazionarietà, ammissibilità primale, complementarità degli scarti e ammissibilità duale.
- Candidati stazionari trovati.
- Classificazione e punto di ottimo ottimo finale.

## Procedura in 5 passi
1. **Forma Standard**: Convertire tutti i vincoli di disuguaglianza in forma $h_j(x) \le 0$. Se il problema è di massimo, convertire i moltiplicatori $\mu_j$ affinché siano $\le 0$, oppure riformulare come $\min -f(x)$ con $\mu_j \ge 0$.
2. **Lagrangiana**: Definire la Lagrangiana generalizzata:
   $$L(x, \lambda, \mu) = f(x) + \sum_{i=1}^m \lambda_i g_i(x) + \sum_{j=1}^p \mu_j h_j(x)$$
3. **Condizioni KKT**:
   - **Stazionarietà**: $\nabla_x L(x^*, \lambda^*, \mu^*) = 0$.
   - **Ammissibilità Primale**: $g_i(x^*) = 0$ e $h_j(x^*) \le 0$.
   - **Complementarità**: $\mu_j^* h_j(x^*) = 0$.
   - **Ammissibilità Duale**: $\mu_j^* \ge 0$ (per minimo), $\mu_j^* \le 0$ (per massimo).
4. **Analisi Combinatoria**: Risolvere esplorando le combinazioni di vincoli attivi ($h_j(x) = 0$, $\mu_j$ libero in segno rispetto alla regola) e inattivi ($h_j(x) < 0 \implies \mu_j = 0$).
5. **Filtro e Ottimo**: Escludere i punti non ammissibili o con moltiplicatori incoerenti. Confrontare $f(x)$ sui punti validi per determinare gli ottimi globali.

## Criteri di Controllo (Candidati da Scartare)
- Scartare immediatamente qualsiasi candidato $x^*$ che violi l'ammissibilità primale (ossia se $h_j(x^*) > 0$ per qualche $j$ o $g_i(x^*) \neq 0$).
- Per un problema di **minimo**, scartare i candidati in cui un vincolo attivo presenta un moltiplicatore $\mu_j^* < 0$.
- Per un problema di **massimo**, scartare i candidati in cui un vincolo attivo presenta un moltiplicatore $\mu_j^* > 0$.

## Mini-template di risposta
```markdown
1. Forma standard: \(\min/\max f(x)\) s.t. \(g_i(x) = 0\), \(h_j(x) \le 0\).
2. Lagrangiana: \(L(x, \lambda, \mu) = f(x) + \sum \lambda_i g_i(x) + \sum \mu_j h_j(x)\).
3. Condizioni KKT:
   * \(\nabla_x L = 0\)
   * \(g_i(x) = 0\), \(h_j(x) \le 0\)
   * \(\mu_j h_j(x) = 0\)
   * \(\mu_j \ge 0\) [per min] / \(\mu_j \le 0\) [per max]
4. Risoluzione dei casi ed enumerazione.
5. Ottimo globale in \(x^* = (..., ...)\) con moltiplicatori \(\lambda^* = ...\), \(\mu^* = ...\) e valore \(f(x^*) = ...\).
```

## Esercizi collegati
- `20_esercizi_pnl.pdf`, esercizi 11-20 (vedi [[pnl_vincolata_esercizi_kkt_globali]] e [[pnl_20_esercizi_catalogo]])
- `esercizi_riepilogo.pdf`, esercizio 4 (vedi [[riepilogo_pl_pli_pnl_esercizi_misti]])

