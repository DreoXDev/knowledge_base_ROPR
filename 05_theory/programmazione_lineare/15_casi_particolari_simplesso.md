---
materia: ROPR
area: Programmazione Lineare
tipo: teoria
fonte: Ricerca Operativa - Metodo del Simplesso - 23-24.pdf
stato: completo
priorita: alta
tags:
  - ropr
  - programmazione-lineare
  - simplesso
  - casi-particolari
  - degenerazione
  - illimitatezza
  - ottimi-multipli
---

# Casi particolari del simplesso

Durante l'esecuzione dell'algoritmo del simplesso, possono presentarsi situazioni non standard che influenzano il comportamento del metodo o l'interpretazione dei risultati.

## 1. Tie Breaking (Scelte Arbitrarie e Parità)

### Parità nella scelta della variabile entrante
- Si verifica quando due o più variabili non di base hanno lo stesso coefficiente negativo minimo nella riga 0.
- **Risoluzione**: La scelta può essere fatta in modo del tutto **arbitrario**. La variabile scelta entra in base, mentre l'altra (o le altre) rimarrà fuori base fino alle iterazioni successive.

### Parità nella scelta della variabile uscente
- Si verifica quando il test del rapporto minimo produce un valore identico per due o più righe.
- **Risoluzione**: Si sceglie una riga **arbitrariamente**. La parità nei rapporti minimi è il segnale immediato che la soluzione successiva sarà **degenere**.

## 2. Degenerazione

Una soluzione di base ammissibile si dice **degenere** se almeno una delle sue variabili di base ha valore pari a zero.
- **Origine**: Si verifica quando, al passo precedente, si è avuta parità nel test dei rapporti minimi. La variabile non scelta per uscire viene ridotta a zero, pur rimanendo formalmente in base.
- **Conseguenza**: Il passo di pivot successivo potrebbe produrre uno spostamento di lunghezza zero, mantenendo invariato il valore della funzione obiettivo $Z$. In rari casi teorici, questo può provocare un fenomeno di **ciclaggio** (l'algoritmo ritorna a un tableau già visitato ed entra in un ciclo infinito). Nella pratica d'esame, si continua normalmente a fare pivot finché non si esce dalla degenerazione o si trova l'ottimo.

## 3. Funzione Obiettivo Illimitata (Illimitatezza)

Si verifica quando una variabile entrante può crescere indefinitamente senza che alcun vincolo ne blocchi l'aumento.
- **Segnale nel Tableau**: Scelta la variabile entrante, tutti i coefficienti nella sua colonna pivot sono **non positivi** ($\le 0$). Di conseguenza, non è possibile calcolare il test dei rapporti minimi.
- **Interpretazione**: La regione ammissibile è aperta (non limitata) nella direzione di crescita della funzione obiettivo. Si conclude che il valore ottimo è $Z^* \to +\infty$ (per problemi di massimo) o $Z^* \to -\infty$ (per problemi di minimo).

## 4. Soluzioni Ottime Multiple (Ottimi Multipli)

Si verifica quando un problema ammette infiniti punti che massimizzano o minimizzano la funzione obiettivo.
- **Segnale nel Tableau**: Una volta raggiunto il tableau ottimo (nessun coefficiente negativo in riga 0 per MAX), si osserva che una delle variabili **non di base** ha coefficiente esattamente pari a **zero** nella riga 0.
- **Risoluzione**: Significa che è possibile far entrare quella variabile in base senza alterare il valore di $Z^*$. Facendo un passo di pivot sulla colonna di tale variabile si ricava una seconda soluzione di base ottima distinta.
- **Interpretazione**: Qualsiasi punto giacente sul segmento (o combinazione convessa) che unisce le due soluzioni di base ottime è anch'esso una soluzione ottima.

---

## Tabella Riepilogativa dei Segnali nel Tableau

| Caso Particolare | Segnale nel Tableau | Conseguenza / Soluzione |
|---|---|---|
| **Soluzione Ottima** | Riga 0 $\ge 0$ (per problemi di MAX) | L'algoritmo termina. La soluzione corrente è ottima. |
| **Parità Entrante** | Coefficienti minimi negativi identici in riga 0 | Scelta arbitraria di una delle variabili. |
| **Parità Uscente** | Rapporti minimi identici | Scelta arbitraria. La base successiva sarà degenere. |
| **Degenerazione** | Termine noto (RHS) di una riga di base pari a $0$ | L'iterazione successiva non modifica $Z$. Rischio teorico di ciclaggio. |
| **Problema Illimitato** | Colonna pivot con soli elementi $\le 0$ (nessuna riga pivot) | Fine algoritmo. Funzione obiettivo illimitata ($Z^* \to \infty$). |
| **Ottimi Multipli** | Tableau ottimo con coefficiente nullo per variabile non di base in riga 0 | Esistono infinite soluzioni ottime. Un pivot alternativo mostra l'altro vertice ottimo. |
