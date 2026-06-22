---
materia: ROPR
area: Programmazione Lineare
tipo: teoria
fonte: Ricerca Operativa - Teoria della Dualità.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - simplesso
  - dualita
  - prezzi-ombra
  - sensitivita
---

# Prezzi ombra e interpretazione economica

La formulazione del problema duale fornisce un'interpretazione economica diretta e rigorosa dei vincoli e delle risorse del problema primale, collegandosi direttamente all'analisi di sensitività.

## 1. Interpretazione Economica delle Variabili e Parametri

Si consideri un problema di pianificazione della produzione (primale di massimo):

| Parametro / Variabile | Interpretazione Economica nel Primale |
|---|---|
| $x_j$ | Livello di produzione associato all'attività $j$. |
| $c_j$ | Profitto unitario (o contributo alla prestazione) ottenuto dall'attività $j$. |
| $b_i$ | Disponibilità limitata della risorsa $i$ (es. ore macchina, materie prime). |
| $a_{ij}$ | Quantità di risorsa $i$ consumata per produrre una singola unità dell'attività $j$. |
| **$y_i$** | **Valore unitario implicito (prezzo virtuale) attribuito alla risorsa $i$.** |

Nel problema duale ($\min W = \sum b_i y_i$):
- Si cerca di minimizzare il valore totale attribuito alle risorse a disposizione.
- I vincoli duali ($\sum a_{ij} y_i \ge c_j$) impongono che, per ciascun prodotto $j$, il valore complessivo delle risorse consumate per produrlo sia maggiore o uguale al profitto $c_j$ generato. Se così non fosse, converrebbe vendere le risorse sul mercato anziché usarle per la produzione.

---

## 2. Definizione di Prezzo Ombra (Shadow Price)

Nella soluzione ottima, i prezzi virtuali delle risorse assumono un significato fondamentale per l'analisi di sensitività (modifica dei coefficienti in seguito a decisioni manageriali o variazioni di mercato):

> **Definizione**: Il **prezzo ombra** $\Delta_i^*$ della risorsa $i$-esima misura il tasso di variazione del valore ottimo della funzione obiettivo $Z^*$ per unità di incremento della risorsa $b_i$, supponendo che le altre risorse rimangano costanti e che la base ottima non vari.

### Relazione Matematica
Se la disponibilità della risorsa $i$ aumenta di una quantità $\epsilon$ (entro l'intervallo di stabilità della base ottima):
$$
Z^*_{\text{nuovo}} = Z^*_{\text{vecchio}} + y_i^* \cdot \epsilon
$$
dove $y_i^*$ è il valore ottimo della variabile duale corrispondente.

- Se la risorsa non è satura (slack $s_i^* > 0$), il suo prezzo ombra è $0$ (aumentare una risorsa già abbondante non incrementa il profitto).
- Se la risorsa è satura, il suo prezzo ombra $y_i^* > 0$ indica quanto l'azienda sarebbe disposta a pagare al massimo per acquisire un'unità aggiuntiva di tale risorsa.

---

## Risposta da Esame

I prezzi ombra coincidono con le componenti della soluzione ottima del problema duale $\mathbf{y}^* = (y_1^*, \dots, y_m^*)$. Rappresentano il valore marginale delle risorse del problema primale, ovvero l'incremento di profitto ottimo $Z^*$ che si otterrebbe aumentando di una unità la disponibilità della risorsa corrispondente, mantenendo fissa la base. Sono fondamentali per l'interpretazione economica e per l'analisi di sensitività.
