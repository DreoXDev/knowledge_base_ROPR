---
type: solved-example
topic: programmazione-lineare
status: draft
sources:
  - raw_assets/Programmazione Lineare/Ricerca Operativa - Introduzione a PL - 23-24.pdf
reliability: official
---

# Esempio Svolto — Wyndor Glass Co.

## Traccia Sintetica

La Wyndor Glass Co. produce vetrate e porte in vetro di alta qualità. Dispone di tre stabilimenti con capacità produttiva limitata. Si vuole determinare il mix produttivo settimanale ottimale di due nuovi prodotti (prodotto 1: porte con telaio in alluminio; prodotto 2: finestre con telaio in legno) per massimizzare il profitto totale.

I dati relativi ai tempi di produzione unitari (in ore per lotto) e alle disponibilità settimanali (in ore) sono:
- Stabilimento 1 (lavorazione alluminio): Prodotto 1 impiega 1 ora; Prodotto 2 impiega 0 ore; disponibilità di 4 ore.
- Stabilimento 2 (lavorazione legno): Prodotto 1 impiega 0 ore; Prodotto 2 impiega 2 ore; disponibilità di 12 ore.
- Stabilimento 3 (assemblaggio e finitura): Prodotto 1 impiega 3 ore; Prodotto 2 impiega 2 ore; disponibilità di 18 ore.

Il profitto unitario stimato è di 3000 € per il Prodotto 1 e 5000 € per il Prodotto 2.

## Formulazione Matematica

### Variabili Decisionali
- $x_1$: Numero di lotti del Prodotto 1 prodotti settimanalmente.
- $x_2$: Numero di lotti del Prodotto 2 prodotti settimanalmente.

### Funzione Obiettivo
Massimizzare il profitto totale settimanale (espresso in migliaia di euro):

$$
\max Z = 3x_1 + 5x_2
$$

### Vincoli
- Vincolo Impianto 1:

$$
x_1 \le 4
$$

- Vincolo Impianto 2:

$$
2x_2 \le 12
$$

- Vincolo Impianto 3:

$$
3x_1 + 2x_2 \le 18
$$

- Vincoli di non negatività:

$$
x_1, x_2 \ge 0
$$

## Modello Completo

$$
\max Z = 3x_1 + 5x_2
$$

soggetto a:

$$
x_1 \le 4
$$

$$
2x_2 \le 12
$$

$$
3x_1 + 2x_2 \le 18
$$

$$
x_1, x_2 \ge 0
$$

## Soluzione Ottima Grafica

Risolvendo graficamente il problema nel piano cartesiano $(x_1, x_2)$:
- L'area ammissibile è definita dai vertici $(0,0)$, $(4,0)$, $(4,3)$, $(2,6)$, $(0,6)$.
- Muovendo le rette di livello della funzione obiettivo $3x_1 + 5x_2 = K$ nella direzione di massimo profitto, l'ultimo punto di contatto con la regione ammissibile è il vertice $(2,6)$.
- La soluzione ottima è quindi:

$$
(x_1^*, x_2^*) = (2, 6)
$$

- Il profitto ottimo è:

$$
Z^* = 3(2) + 5(6) = 36 \text{ (migliaia di €)}
$$

## Risposta da Esame

Il modello di PL è dato da $\max Z = 3x_1 + 5x_2$ con vincoli $x_1 \le 4$, $2x_2 \le 12$, $3x_1+2x_2 \le 18$, $x_1,x_2 \ge 0$. La soluzione ottima si ottiene nel vertice $(2,6)$ con valore ottimo $Z=36$.

#ropr #programmazione-lineare #esempio
