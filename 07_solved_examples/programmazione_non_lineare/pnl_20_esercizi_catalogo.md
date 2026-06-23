---
type: solved-example
topic: programmazione_non_lineare
status: consolidated
sources:
  - raw_assets/Programmazione Non Lineare/20_esercizi_pnl.pdf
reliability: official
---

# Catalogo Svolto: 20 Esercizi di Programmazione Non Lineare

Questo file cataloga i 20 esercizi dell'asset `20_esercizi_pnl.pdf`, fornendo per ciascuno il testo, la classificazione dei punti stazionari (per i non vincolati) o le soluzioni KKT e ottimi globali (per i vincolati).

---

## Esercizi 1-10: PNL Non Vincolata (Ricerca e Classificazione Punti Stazionari)

Per tutti questi esercizi la procedura prevede:
1. Calcolo del gradiente $\nabla f(x, y) = 0$ per determinare i punti stazionari.
2. Calcolo dell'Hessiana $H_f(x, y)$ e valutazione nei punti stazionari.
3. Classificazione locale: $\det(H) > 0$ e $\text{tr}(H) > 0 \implies$ Minimo; $\det(H) > 0$ e $\text{tr}(H) < 0 \implies$ Massimo; $\det(H) < 0 \implies$ Sella.

| N° | Funzione Obiettivo $f(x, y)$ | Punti Stazionari | Minimi Locali | Massimi Locali | Punti di Sella |
|---|---|---|---|---|---|
| **1** | $2x^3 - 2x^2y + 3x^2 - 2xy + 3y^2$ | $(0,0)$, $(4, \frac{20}{3})$, $(-1,0)$ | $(0,0)$ | Nessuno | $(4, \frac{20}{3})$, $(-1,0)$ |
| **2** | $-2y^3 + xy^2 + x^2 - 2xy + 3y^2$ | $(0,0)$, $(\frac{1}{2}, 1)$, $(-12,-4)$ | $(0,0)$ | Nessuno | $(\frac{1}{2}, 1)$, $(-12,-4)$ |
| **3** | $(3x-3y)^2 + (-y^2+3x-y)^2 + 1$ | $(0,0)$, $(2,2)$, $(\frac{5}{6}, 1)$ | $(0,0)$, $(2,2)$ | Nessuno | $(\frac{5}{6}, 1)$ |
| **4** | $x^3 - x^2y + 2x^2 - 3xy + y^2 - 2$ | $(0,0)$, $(-\frac{1}{2}, -\frac{5}{8})$, $(-1,-1)$ | $(-\frac{1}{2}, -\frac{5}{8})$ | Nessuno | $(0,0)$, $(-1,-1)$ |
| **5** | $2y^3 + 2xy^2 + 3x^2 + 2xy - y^2 - 3$ | $(0,0)$, $(-2,2)$, $(-\frac{2}{3}, 1)$ | $(-\frac{2}{3}, 1)$ | Nessuno | $(0,0)$, $(-2,2)$ |
| **6** | $(-x-3y)^2 + (-y^2-x-y)^2 - 1$ | $(0,0)$, $(-6,2)$, $(-\frac{5}{2}, 1)$ | $(0,0)$, $(-6,2)$ | Nessuno | $(-\frac{5}{2}, 1)$ |
| **7** | $x^3 - x^2y + 4x^2 + 4xy + 3y^2 - 2$ | $(0,0)$, $(16,32)$, $(-1, \frac{5}{6})$ | $(0,0)$ | Nessuno | $(16,32)$, $(-1, \frac{5}{6})$ |
| **8** | $-4y^3 - 3xy^2 - x^2 + 2xy - 5y^2 + 2$ | $(0,0)$, $(-8, \frac{8}{3})$, $(-\frac{1}{2}, -\frac{1}{3})$ | Nessuno | $(0,0)$ | $(-8, \frac{8}{3})$, $(-\frac{1}{2}, -\frac{1}{3})$ |
| **9** | $(x-4y)^2 + (2x^2-3x-4y)^2 - 5$ | $(0,0)$, $(1,0)$, $(2, \frac{1}{2})$ | $(0,0)$, $(2, \frac{1}{2})$ | Nessuno | $(1,0)$ |
| **10** | $-x^3 + x^2y + 2x^2 - xy - y^2 - 4$ | $(0,0)$, $(3,3)$, $(\frac{3}{2}, \frac{3}{8})$ | Nessuno | $(\frac{3}{2}, \frac{3}{8})$ | $(0,0)$, $(3,3)$ |

---

## Esercizi 11-20: PNL Vincolata (Condizioni KKT e Ottimi Globali)

Per tutti questi esercizi la procedura prevede:
1. Riscrivere i vincoli nella forma standard $h_j(x,y) \le 0$ o $g_i(x,y) = 0$.
2. Costruire la Lagrangiana $L = f + \sum \mu_j h_j + \sum \lambda_i g_i$.
3. Risolvere il sistema KKT per casi di complementarità.
4. Identificare ed escludere i candidati non ammissibili (primale o duale).
5. Confrontare i valori di $f$ per determinare gli ottimi globali. Se la regione $\Omega$ non è limitata, l'ottimo globale potrebbe non esistere (es. la funzione diverge all'infinito lungo percorsi ammissibili).

> [!NOTE]
> La notazione ufficiale del testo distingue le soluzioni del sistema KKT in base al segno dei moltiplicatori $\mu$:
> - **$\mu \le 0$**: Punti candidati all'ottimo sotto la convenzione di massimizzazione (o se la Lagrangiana ha segno meno).
> - **$\mu \ge 0$**: Punti candidati all'ottimo sotto la convenzione di minimizzazione (con vincoli $h_j \le 0$).

| N° | Funzione $f(x, y)$ | Regione Ammissibile $\Omega$ | Candidati KKT ($\mu \le 0$) | Candidati KKT ($\mu \ge 0$) | Minimo Globale | Massimo Globale |
|---|---|---|---|---|---|---|
| **11** | $y - x^2$ | $-x^2 - (y-1)^2 + 1 \le 0$, $-x \le 0$ | $(0,0)$, $(\frac{\sqrt{3}}{2}, \frac{1}{2})$ | $(0,2)$ | Nessuno | Nessuno |
| **12** | $x^2 + y^2$ | $-x^2+y+4 \le 0$, $-x+y-2 \le 0$ | Nessuna | $(\pm\frac{\sqrt{14}}{2}, -\frac{1}{2})$, $(0,-4)$ | $(\pm\frac{\sqrt{14}}{2}, -\frac{1}{2})$ | Nessuno |
| **13** | $x^2 + (y-2)^2$ | $x^2-1 \le 0$, $y^2-1 \le 0$ | $(0,-1)$, $(\pm 1, -1)$ | $(0,1)$ | $(0,1)$ | $(\pm 1, -1)$ |
| **14** | $(x-3)^2 + (y-1)^2$ | $-x \le 0$, $-y \le 0$ | $(3,1)$, $(3,0)$, $(0,1)$, $(0,0)$ | $(3,1)$ | $(3,1)$ | Nessuno |
| **15** | $(x+1)^2 + y^2$ | $x^2+4y^2-4 \le 0$ | $(-1,0)$, $(\pm 2,0)$, $(-\frac{4}{3}, \pm\frac{\sqrt{5}}{3})$ | $(-1,0)$ | $(-1,0)$ | $(2,0)$ |
| **16** | $-x^2 - (y-1)^2$ | $x^2-y \le 0$, $y-4 \le 0$ | $(0,1)$ | $(0,1)$, $(\pm 2,4)$, $(0,0)$, $(0,4)$, $(\pm\frac{\sqrt{2}}{2}, \frac{1}{2})$ | $(\pm 2, 4)$ | $(0,1)$ |
| **17** | $x+y$ | $-x^2-4y^2+4 \le 0$, $x^2+4y^2-16 \le 0$ | $(-\frac{4}{\sqrt{5}}, -\frac{1}{\sqrt{5}})$, $(\frac{8}{\sqrt{5}}, \frac{2}{\sqrt{5}})$ | $(\frac{4}{\sqrt{5}}, \frac{1}{\sqrt{5}})$, $(-\frac{8}{\sqrt{5}}, -\frac{2}{\sqrt{5}})$ | $(-\frac{8}{\sqrt{5}}, -\frac{2}{\sqrt{5}})$ | $(\frac{8}{\sqrt{5}}, \frac{2}{\sqrt{5}})$ |
| **18** | $(x-2)^2 + (y-2)^2$ | $-x^2-y^2+1 \le 0$, $x-4 \le 0$ | $(2,2)$, $(4,2)$, $(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}})$ | $(2,2)$, $(-\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}})$ | $(2,2)$ | Nessuno |
| **19** | $(x-1)^2 + y^2$ | $x^2+4y^2-8 \le 0$, $x^2-4=0$ | $(\pm 2, 0)$, $(\pm 2, \pm 1)$ | $(\pm 2, 0)$ | $(2,0)$ | $(-2, \pm 1)$ |
| **20** | $(x-1)^2 + (y-2)^2$ | $x-y \le 0$, $-x-y \le 0$ | $(1,2)$, $(\frac{3}{2}, \frac{3}{2})$, $(-\frac{1}{2}, \frac{1}{2})$, $(0,0)$ | $(1,2)$ | $(1,2)$ | Nessuno |

---

## Dettagli Analitici degli Esercizi Rilevanti

Per lo svolgimento passo-passo e l'analisi approfondita di questi esercizi, consultare:
- Esercizi non vincolati (1-10): [[pnl_non_vincolata_esercizi_punti_stazionari]]
- Esercizi vincolati (11-20): [[pnl_vincolata_esercizi_kkt_globali]]
