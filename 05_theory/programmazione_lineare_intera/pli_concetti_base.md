---
type: theory
topic: programmazione_lineare_intera
status: active
sources: [modelli_PLI.pdf]
reliability: official
---

# Programmazione Lineare Intera - Concetti Base

## Fonte
`modelli_PLI.pdf` (Mauro Passacantando)

## Idea Essenziale
La Programmazione Lineare Intera (PLI) estende la programmazione lineare (PL) imponendo che alcune o tutte le variabili decisionali debbano assumere valori interi. Quando le variabili sono vincolate ad assumere valori in $\{0, 1\}$, si parla di programmazione lineare binaria (o a variabili 0-1), ampiamente utilizzata per modellare decisioni logiche e combinatorie del tipo sì/no.

## Modello Generale di PLI
Un problema di PLI si presenta nella forma:

$$
\max \quad c^T x
$$
$$
\text{s.t.} \quad A x \le b
$$
$$
x \in \mathbb{Z}^n
$$

Se solo una parte delle variabili è vincolata all'integrità, il problema prende il nome di Programmazione Lineare Mista (MIP - Mixed Integer Programming):

$$
x_i \in \mathbb{Z} \quad \forall i \in I
$$
$$
x_j \in \mathbb{R} \quad \forall j \notin I
$$

## Classificazione delle Variabili

*   **Variabili Continue ($x_i \ge 0$)**: Rappresentano quantità divisibili (es. litri di carburante, ore di lavoro, frazioni di flusso).
*   **Variabili Intere ($x_i \in \mathbb{Z}_+$)**: Rappresentano entità indivisibili (es. numero di lotti prodotti, numero di veicoli da acquistare).
*   **Variabili Binarie ($x_i \in \{0, 1\}$)**: Rappresentano decisioni discrete sì/no (es. attivare un impianto, includere un progetto nel budget, assegnare un lavoratore a una macchina).

## Rilassamento Continuo
Il **rilassamento continuo** di un problema di PLI si ottiene eliminando i vincoli di integrità sulle variabili, sostituendoli con i relativi intervalli continui.
Ad esempio, se il dominio originale è $x_i \in \{0, 1\}$, il rilassamento continuo impone $0 \le x_i \le 1$.

Dato che la regione ammissibile del rilassamento continuo contiene interamente la regione ammissibile del problema intero, vale la seguente proprietà fondamentale sull'ottimo:
*   Per un problema di massimo: $Z^*_{\text{continuo}} \ge Z^*_{\text{intero}}$
*   Per un problema di minimo: $Z^*_{\text{continuo}} \le Z^*_{\text{intero}}$

## Errori Comuni da Evitare
*   Arrotondare la soluzione ottima del rilassamento continuo: la soluzione arrotondata potrebbe essere non ammissibile o lontana dall'ottimo intero.
*   Trattare il rilassamento continuo come equivalente al problema intero al di fuori dei casi teorici provati (come la totale unimodularità).
