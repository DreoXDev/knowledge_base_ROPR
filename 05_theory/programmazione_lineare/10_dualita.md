---
type: theory-note
topic: programmazione-lineare
status: draft
sources:
  - raw_assets/Programmazione Lineare/lec_w4_completa.pdf
reliability: official
---

# La Teoria della Dualità nella Programmazione Lineare

Ad ogni problema di Programmazione Lineare (chiamato **Primale**) è associato un secondo problema di ottimizzazione ad esso strettamente connesso, denominato **Duale**. L'analisi del duale fornisce importanti interpretazioni economiche e geometriche dell'ottimo.

## Intuizione Economica (Prezzi Ombra)

Si consideri un problema primale di massimizzazione del profitto soggetto a vincoli di risorsa.
- Le variabili primali $x_j$ rappresentano i livelli delle attività produttive.
- I vincoli rappresentano la disponibilità delle risorse limitate $b_i$.

Il problema duale associato risponde alla domanda: *"Se volessi vendere o affittare le mie risorse sul mercato invece di usarle per produrre, quale prezzo unitario $p_i$ dovrei chiedere per ciascuna risorsa per rendere l'operazione conveniente?"*
- Le variabili duali $p_i$ assumono quindi il significato di **valore marginale unitario** (o **prezzo ombra**) delle risorse: indicano di quanto aumenterebbe il profitto ottimo $Z^*$ se si avesse a disposizione una unità aggiuntiva della risorsa $i$.

## Esempio Primale-Duale

### Problema Primale (MAX)

$$
\max Z = 40x_1 + 50x_2
$$

soggetto a:

$$
x_1 + 2x_2 \le 40 \qquad (\text{Risorsa 1})
$$

$$
4x_1 + 3x_2 \le 120 \qquad (\text{Risorsa 2})
$$

$$
x_1, x_2 \ge 0
$$

### Problema Duale Associato (MIN)
Associamo la variabile duale $p_1$ al primo vincolo e $p_2$ al secondo:

$$
\min Z' = 40p_1 + 120p_2
$$

soggetto a:

$$
p_1 + 4p_2 \ge 40
$$

$$
2p_1 + 3p_2 \ge 50
$$

$$
p_1, p_2 \ge 0
$$

## Relazioni tra le Soluzioni Ottime

Risolvendo entrambi i problemi, si ottengono le seguenti soluzioni ottime:
- **Primale**: $x_1^* = 24, x_2^* = 8 \implies Z^* = 1360$
- **Duale**: $p_1^* = 16, p_2^* = 6 \implies Z'^* = 1360$

### Teorema della Dualità Forte
Se il problema primale (o il duale) possiede una soluzione ottima finita, allora anche l'altro problema possiede una soluzione ottima finita e i due valori delle funzioni obiettivo all'ottimo coincidono esattamente:

$$
Z^* = Z'^*
$$

## Lettura delle Variabili Duali dal Tableau Ottimo

Non è necessario risolvere da capo il problema duale. Quando si risolve il primale con l'algoritmo del simplesso:
- I valori ottimi delle variabili duali $p_i^*$ (prezzi ombra) si leggono direttamente nella **riga 0 del tableau ottimo** in corrispondenza delle colonne associate alle **variabili di slack ($s_i$)** del primale.

Nell'esempio precedente, nel tableau ottimo finale, sotto la colonna di $s_1$ leggeremo il valore 16 ($p_1^* = 16$) e sotto la colonna di $s_2$ leggeremo il valore 6 ($p_2^* = 6$).

#ropr #programmazione-lineare #teoria #dualita #prezzi-ombra
