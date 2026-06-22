---
topic: Programmazione Lineare
type: esempio_svolto
source: lec_w4_completa.pdf
status: verificato
---

# Esempio Svolto — Costruzione del Duale (Caso Tool.Spa)

## Traccia Sintetica
Dato il problema primale Tool.Spa, scriverne il problema duale associando ad ogni vincolo la relativa variabile duale.

## Problema Primale (MAX)

$$
\max Z = 130x_c + 100x_p
$$

soggetto a:

$$
1.5x_c + x_p \le 27 \qquad (u_1 \ge 0)
$$

$$
x_c + x_p \le 21 \qquad (u_2 \ge 0)
$$

$$
0.3x_c + 0.5x_p \le 9 \qquad (u_3 \ge 0)
$$

$$
x_c \le 15 \qquad (u_4 \ge 0)
$$

$$
x_p \le 16 \qquad (u_5 \ge 0)
$$

$$
x_c, x_p \ge 0
$$

## Costruzione del Duale (MIN)

1. **Associazioni**: Ad ognuno dei 5 vincoli primali di tipo $\le$ associamo una variabile duale non negativa: $u_1, u_2, u_3, u_4, u_5 \ge 0$.
2. **Funzione Obiettivo**: I coefficienti sono i termini noti (RHS) del primale:

$$
\min Z' = 27u_1 + 21u_2 + 9u_3 + 15u_4 + 16u_5
$$

3. **Vincoli**: Si traspone la matrice del primale:
   - Per $x_c$ (coefficiente in obiettivo 130, variabile primale $\ge 0$):
     $$
     1.5u_1 + u_2 + 0.3u_3 + u_4 \ge 130
     $$
   - Per $x_p$ (coefficiente in obiettivo 100, variabile primale $\ge 0$):
     $$
     u_1 + u_2 + 0.5u_3 + u_5 \ge 100
     $$

## Modello Duale Completo

$$
\min Z' = 27u_1 + 21u_2 + 9u_3 + 15u_4 + 16u_5
$$

soggetto a:

$$
1.5u_1 + u_2 + 0.3u_3 + u_4 \ge 130
$$

$$
u_1 + u_2 + 0.5u_3 + u_5 \ge 100
$$

$$
u_1, u_2, u_3, u_4, u_5 \ge 0
$$

## Risposta da Esame
Il problema duale di Tool.Spa è:
$\min Z' = 27u_1 + 21u_2 + 9u_3 + 15u_4 + 16u_5$
soggetto a:
- $1.5u_1 + u_2 + 0.3u_3 + u_4 \ge 130$
- $u_1 + u_2 + 0.5u_3 + u_5 \ge 100$
- $u_1, u_2, u_3, u_4, u_5 \ge 0$.
