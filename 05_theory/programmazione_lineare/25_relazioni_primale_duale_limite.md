---
materia: ROPR
area: Programmazione Lineare
tipo: teoria
fonte: Ricerca Operativa - Teoria della Dualità.pdf
stato: completo
priorita: media
tags:
  - ropr
  - programmazione-lineare
  - simplesso
  - dualita
  - casi-limite
  - inammissibilita
  - illimitatezza
---

# Relazioni primale-duale e casi limite

Le proprietà di ammissibilità (esistenza di soluzioni) e di limitatezza (funzione obiettivo limitata o illimitata) per una coppia di problemi primale-duale sono strettamente legate.

## 1. Il Teorema di Dualità per i Casi Limite

La dualità debole impone rigidi vincoli sul comportamento reciproco di primale e duale:

1. **Ottimo Finito**: Se un problema ha soluzioni ammissibili e funzione obiettivo limitata (e quindi ha un ottimo finito), allora anche l'altro problema ha soluzioni ammissibili e funzione obiettivo limitata.
2. **Illimitatezza**: Se il problema primale (MAX) ha soluzioni ammissibili ed è illimitato ($Z^* \to +\infty$), allora il problema duale non può avere alcuna soluzione ammissibile (è **inammissibile**).
   - *Spiegazione*: Se il duale avesse una soluzione ammissibile $\mathbf{y}$, per la dualità debole avremmo $\mathbf{c}\mathbf{x} \le \mathbf{y}\mathbf{b}$ per ogni $\mathbf{x}$ ammissibile. Questo impedirebbe a $Z = \mathbf{c}\mathbf{x}$ di crescere all'infinito, contraddicendo l'illimitatezza.
3. **Inammissibilità**: Se un problema è inammissibile (non ha soluzioni ammissibili), l'altro problema può essere:
   - a sua volta inammissibile;
   - oppure illimitato.

---

## 2. Tabella delle Relazioni Possibili

La seguente matrice riassume le combinazioni possibili (Sì) e impossibili (No) tra lo stato del Primale e del Duale:

| Primale \ Duale | Ottimo Finito | Illimitato | Inammissibile |
|---|---|---|---|
| **Ottimo Finito** | **Sì** ($Z^* = W^*$) | No | No |
| **Illimitato** | No | No | **Sì** |
| **Inammissibile** | No | **Sì** | **Sì** |

---

## Risposta da Esame

In una coppia primale-duale, se uno dei due problemi ha ottimo finito, anche l'altro ha ottimo finito e i loro valori ottimi coincidono. Se uno dei due problemi è illimitato, l'altro è necessariamente inammissibile. Se uno dei due problemi è inammissibile, l'altro può essere o inammissibile o illimitato. Non è mai possibile che entrambi i problemi siano contemporaneamente illimitati.
