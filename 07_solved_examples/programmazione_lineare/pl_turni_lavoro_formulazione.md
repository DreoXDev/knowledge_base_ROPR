---
topic: Programmazione Lineare
type: esempio_svolto
source: lezione 3 completa.pdf
status: verificato
---

# Esempio Svolto — Formulazione Turni di Lavoro (Workforce Scheduling)

## Traccia Sintetica
Un ristorante operante 7 giorni su 7 richiede una quantità minima giornaliera di dipendenti in servizio:
- Lunedì: 14
- Martedì: 13
- Mercoledì: 15
- Giovedì: 16
- Venerdì: 19
- Sabato: 18
- Domenica: 11

Ogni dipendente lavora per 5 giorni consecutivi e ha 2 giorni di riposo. Si desidera minimizzare il numero totale di dipendenti assunti.

## Formulazione Matematica

### Variabili Decisionali
Sia $x_j$ il numero di dipendenti che iniziano a lavorare il giorno $j$ (dove $1=\text{Lun}$, $2=\text{Mar}$, $3=\text{Mer}$, $4=\text{Gio}$, $5=\text{Ven}$, $6=\text{Sab}$, $7=\text{Dom}$).

### Funzione Obiettivo
Minimizzare il numero totale di lavoratori assunti:

$$
\min Z = x_1 + x_2 + x_3 + x_4 + x_5 + x_6 + x_7
$$

### Vincoli
Per ciascun giorno della settimana, la somma dei lavoratori il cui turno di 5 giorni copre quel giorno deve soddisfare la richiesta minima:
- **Lunedì** (coperto da turni che iniziano Lun, Gio, Ven, Sab, Dom):
  $$
  x_1 + x_4 + x_5 + x_6 + x_7 \ge 14
  $$
- **Martedì** (coperto da turni che iniziano Lun, Mar, Ven, Sab, Dom):
  $$
  x_1 + x_2 + x_5 + x_6 + x_7 \ge 13
  $$
- **Mercoledì** (coperto da turni che iniziano Lun, Mar, Mer, Sab, Dom):
  $$
  x_1 + x_2 + x_3 + x_6 + x_7 \ge 15
  $$
- **Giovedì** (coperto da turni che iniziano Lun, Mar, Mer, Gio, Dom):
  $$
  x_1 + x_2 + x_3 + x_4 + x_7 \ge 16
  $$
- **Venerdì** (coperto da turni che iniziano Lun, Mar, Mer, Gio, Ven):
  $$
  x_1 + x_2 + x_3 + x_4 + x_5 \ge 19
  $$
- **Sabato** (coperto da turni che iniziano Mar, Mer, Gio, Ven, Sab):
  $$
  x_2 + x_3 + x_4 + x_5 + x_6 \ge 18
  $$
- **Domenica** (coperto da turni che iniziano Mer, Gio, Ven, Sab, Dom):
  $$
  x_3 + x_4 + x_5 + x_6 + x_7 \ge 11
  $$

Dominio delle variabili:

$$
x_j \ge 0 \quad \text{e intere} \qquad \forall j = 1 \dots 7
$$

> [!IMPORTANT]
> Nelle slide originali, l'ultimo vincolo presenta un refuso nel testo (mostra la richiesta pari a 16 per mercoledì ripetutamente). Qui è stata ripristinata la corretta corrispondenza logico-temporale secondo i dati corretti delle slide (Giovedì ha richiesta 16, Mercoledì 15).
