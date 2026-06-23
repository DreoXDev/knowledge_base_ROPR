---
type: method
topic: programmazione_non_lineare
status: consolidated
sources:
  - raw_assets/Programmazione Non Lineare/PNL 1D.pdf
reliability: official
---

# Confronto tra Metodo di Bisezione e Metodo di Newton 1D

Nell'ottimizzazione non lineare unidimensionale, la scelta tra il metodo di bisezione (dicotomico) e il metodo di Newton (di approssimazione) dipende dal bilancio tra la robustezza richiesta e lo sforzo computazionale (calcolo delle derivate).

---

## Tabella Comparativa

| Caratteristica | Metodo di Bisezione | Metodo di Newton 1D |
| :--- | :--- | :--- |
| **Tipo di Algoritmo** | Dicotomico (ricerca a dimezzamento) | Approssimazione (Taylor quadratico locale) |
| **Informazioni Richieste** | Derivata prima $f'(x)$ ed estremi $[\underline{x}, \bar{x}]$ | Derivata prima $f'(x)$ e derivata seconda $f''(x)$ |
| **Punto di Partenza** | Intervallo $[\underline{x}_0, \bar{x}_0]$ con derivate discordi | Singolo punto iniziale $x_0$ |
| **Velocità di Convergenza**| Lineare (lenta ma costante) | Quadratica (molto veloce vicino all'ottimo) |
| **Robustezza** | Elevata (converge sempre sotto le ipotesi) | Bassa (sensibile alla scelta di $x_0$, può divergere) |
| **Rischi Algoritmici** | Nessuno se $f'$ è continua e concava/convessa | Divisione per zero se $f''(x_k) = 0$; cicli infiniti |

---

## Analisi della Convergenza

- **Bisezione**: Ad ogni iterazione, l'ampiezza dell'intervallo di incertezza viene dimezzata:
  $$\Delta x_{k+1} = \frac{1}{2} \Delta x_k$$
  La convergenza è lineare con fattore di riduzione pari a $0.5$.
- **Newton 1D**: Se il punto iniziale $x_0$ è sufficientemente vicino all'ottimo stazionario $x^*$, l'errore $e_k = |x_k - x^*|$ decade secondo la relazione:
  $$e_{k+1} \approx C \cdot e_k^2$$
  La convergenza è quadratica, il che significa che il numero di cifre decimali corrette raddoppia ad ogni iterazione.

---

## Strategia di Selezione all'Esame

- **Scegliere la Bisezione se**:
  - L'esercizio fornisce un intervallo iniziale $[\underline{x}, \bar{x}]$ e una tolleranza $\epsilon$.
  - Il calcolo della derivata seconda $f''(x)$ è estremamente complesso o non definito.
  - È richiesta una garanzia assoluta di convergenza senza rischi di oscillazioni.
- **Scegliere Newton 1D se**:
  - Viene assegnato un punto di partenza specifico $x_0$.
  - Si richiede una convergenza molto rapida in pochissime iterazioni (solitamente $2$ o $3$ passi).
  - La derivata seconda $f''(x)$ è facile da calcolare.

---

## Sintesi Teorica per l'Esame

> [!IMPORTANT]
> **Frase da esame**:
> *"Il metodo di bisezione è un algoritmo dicotomico globalmente convergente (robusto ma lento) che richiede solo la conoscenza della derivata prima; il metodo di Newton è un algoritmo di approssimazione locale a convergenza quadratica (veloce ma instabile) che richiede il calcolo della derivata seconda e può fallire o divergere se inizializzato lontano dal punto di ottimo."*
