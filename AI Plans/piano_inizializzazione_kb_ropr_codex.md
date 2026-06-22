# Piano Codex/Antigravity - Inizializzazione `knowledge_base_ROPR`

Repo target: <https://github.com/DreoXDev/knowledge_base_ROPR>  
Repo di riferimento: <https://github.com/DreoXDev/knowledge_base_APA>

## Obiettivo generale

Inizializzare la repository `knowledge_base_ROPR` come Knowledge Base completa per lo studio di **Ricerca Operativa e Pianificazione delle Risorse**.

La repo deve avere due funzioni principali:

1. **Vault Obsidian per lo studio**
   - trasformare i `raw_assets` in appunti Markdown leggibili e studiabili;
   - creare note teoriche compatte;
   - creare method card operative per esercizi;
   - creare esempi svolti copiabili;
   - creare flashcard e materiali per NotebookLM;
   - mantenere una struttura navigabile e stabile.

2. **RAG per chat AI durante studio/esame**
   - permettere a una chat AI di usare la repo come fonte primaria;
   - evitare risposte inventate;
   - riconoscere rapidamente il tipo di esercizio;
   - consultare i file giusti;
   - produrre risposte concise, corrette e copiabili sul foglio d'esame.

La repo è attualmente all'inizio e contiene solo `raw_assets/`, con sottocartelle già presenti:

```text
raw_assets/
  Mega/
  Programmazione Lineare/
  Programmazione Lineare Intera/
  Programmazione Non Lineare/
```

Questo piano riguarda **solo l'inizializzazione strutturale** della repo e la preparazione del workflow uniforme di ingestione. L'analisi contenutistica dei singoli asset verrà fatta in passaggi successivi, uno o pochi file per volta.

---

## Principi guida

### 1. Separare sempre fonte raw, analisi, consolidamento e RAG

Non modificare i file originali in `raw_assets/`.

Ogni informazione deve passare idealmente da questi livelli:

```text
raw_assets/                 # fonti originali non toccate
01_sources/                 # inventario e link logici alle fonti
02_transcriptions/          # trascrizioni/estrazioni lavorate
03_exercise_catalog/        # catalogo esercizi e varianti
04_methods/                 # method card operative
05_theory/                  # teoria consolidata da studiare
06_exam_patterns/           # pattern ricorrenti d'esame
07_solved_examples/         # esempi svolti copiabili
08_flashcards/              # flashcard e domande attive
09_ingestion_reports/       # report di analisi asset/batch
10_rag/                     # entrypoint, index, pattern map, policy
AI Chat during Exam/         # prompt finale e istruzioni operative
```

### 2. Ordine di affidabilità delle fonti

In caso di conflitti tra materiali, usare questo ordine:

1. file ufficiali dei professori;
2. esercizi/appelli ufficiali;
3. soluzioni ufficiali o note del corso, se presenti;
4. materiali condivisi su Mega dai compagni;
5. inferenze ricostruite dalla KB;
6. inferenze del modello AI.

Ogni nota importante deve contenere una sezione `Fonti` o almeno riferimenti ai file sorgente da cui è stata estratta.

### 3. Stile Obsidian

Usare Markdown semplice, leggibile e compatibile con Obsidian.

Regole:

- usare `$...$` per formule inline;
- usare `$$...$$` per formule in blocco;
- niente emoji;
- titoli gerarchici puliti;
- esempi e pseudocodice in code block;
- nomi file stabili e descrittivi;
- frontmatter YAML solo dove utile;
- tag Obsidian coerenti.

Esempio frontmatter:

```md
---
type: method-card
topic: programmazione-lineare
status: draft
sources:
  - raw_assets/Programmazione Lineare/...
reliability: official
last_review: 2026-06-22
---
```

### 4. Output finale da esame

Tutto ciò che finisce in `04_methods/`, `06_exam_patterns/`, `07_solved_examples/` e `AI Chat during Exam/` deve essere scritto con l'obiettivo finale di produrre risposte:

- corrette;
- concise;
- da esame universitario;
- copiabili a mano;
- non prolisse;
- con terminologia precisa;
- senza spiegazioni superflue;
- con dichiarazione sintetica di eventuali assunzioni se la traccia/foto è ambigua.

---

## Struttura da creare

Creare questa struttura completa:

```text
knowledge_base_ROPR/
  .obsidian/
    app.json
    appearance.json
    core-plugins.json
    graph.json
  00_meta/
    COURSE_OVERVIEW.md
    SOURCE_RELIABILITY_POLICY.md
    STUDY_ROADMAP.md
    EXAM_STRATEGY.md
    GLOSSARY.md
  01_sources/
    SOURCE_INVENTORY.md
    SOURCE_MAP.md
    OFFICIAL_SOURCES.md
    MEGA_SOURCES.md
    UNCLASSIFIED_SOURCES.md
  02_transcriptions/
    README.md
    official/
    mega/
    exercises/
  03_exercise_catalog/
    README.md
    EXERCISE_INDEX.md
    EXERCISE_TYPES.md
    by_topic/
    by_source/
  04_methods/
    README.md
    programmazione_lineare/
    programmazione_lineare_intera/
    programmazione_non_lineare/
    modellazione/
    algoritmi/
  05_theory/
    README.md
    00_index.md
    programmazione_lineare/
    programmazione_lineare_intera/
    programmazione_non_lineare/
    dualita_sensitivita/
    grafi_reti_flussi/
    teoria_generale/
  06_exam_patterns/
    README.md
    PATTERN_INDEX.md
    PATTERN_MAP.md
    common_mistakes.md
  07_solved_examples/
    README.md
    programmazione_lineare/
    programmazione_lineare_intera/
    programmazione_non_lineare/
    modellazione/
  08_flashcards/
    README.md
    flashcards_ropr_all.md
    flashcards_theory.md
    flashcards_methods.md
    active_recall_questions.md
  09_ingestion_reports/
    README.md
    batch_reports/
    asset_reports/
    final_audit.md
  10_rag/
    RAG_ENTRYPOINT.md
    RAG_RETRIEVAL_INDEX.md
    RAG_PATTERN_MAP.md
    RAG_SOURCE_POLICY.md
    RAG_RESPONSE_STYLE.md
    RAG_GAPS_AND_WARNINGS.md
    method_cards/
  AI Chat during Exam/
    Final Prompt.md
    Exam Assistant Context.md
    Response Templates.md
    Photo Exercise Policy.md
  notebooklm/
    NOTEBOOKLM_CONTEXT.md
    NOTEBOOKLM_SOURCE_GUIDE.md
    NOTEBOOKLM_STUDY_PROMPTS.md
  templates/
    asset_ingestion_template.md
    batch_ingestion_template.md
    theory_note_template.md
    method_card_template.md
    solved_example_template.md
    exercise_catalog_template.md
    flashcard_template.md
    codex_plan_template.md
  scripts/
    inventory_assets.py
    check_links.py
    check_frontmatter.py
    build_rag_index.py
    extract_pdf_text.py
    normalize_filenames.py
  plans/
    README.md
  README.md
  AI_CONTEXT.md
  PROJECT_STATUS.md
  TODO.md
  .gitignore
```

---

## Task 1 - Creare configurazione base Obsidian

Creare `.obsidian/` minimale.

File consigliati:

### `.obsidian/app.json`

```json
{
  "alwaysUpdateLinks": true,
  "newFileLocation": "folder",
  "newFileFolderPath": "05_theory"
}
```

### `.obsidian/core-plugins.json`

```json
[
  "file-explorer",
  "global-search",
  "switcher",
  "graph",
  "backlink",
  "canvas",
  "outgoing-link",
  "tag-pane",
  "page-preview",
  "daily-notes",
  "templates",
  "note-composer",
  "command-palette",
  "markdown-importer",
  "word-count"
]
```

### `.obsidian/appearance.json`

```json
{
  "baseFontSize": 16,
  "cssTheme": "",
  "enabledCssSnippets": []
}
```

---

## Task 2 - Creare README principale

Creare `README.md` con:

```md
# Knowledge Base ROPR

Repository per preparare l'esame di Ricerca Operativa e Pianificazione delle Risorse e usarla come base RAG durante studio, simulazioni ed esame.

## Scopo

Questa repo contiene:

- fonti originali in `raw_assets/`;
- inventario delle fonti;
- appunti teorici in formato Obsidian;
- catalogo esercizi;
- method card operative;
- esempi svolti;
- flashcard;
- prompt finale per chat AI durante l'esame;
- entrypoint RAG per impedire risposte inventate.

## Come usare la repo

Per studiare:

1. partire da `00_meta/STUDY_ROADMAP.md`;
2. consultare `05_theory/00_index.md`;
3. usare `04_methods/` per gli esercizi;
4. ripassare con `08_flashcards/`.

Per usare la repo come RAG:

1. aprire `10_rag/RAG_ENTRYPOINT.md`;
2. usare `10_rag/RAG_RETRIEVAL_INDEX.md`;
3. riconoscere il pattern con `10_rag/RAG_PATTERN_MAP.md`;
4. applicare la method card più vicina;
5. seguire `AI Chat during Exam/Final Prompt.md` per lo stile di risposta.

## Regola guida

Traccia d'esame -> RAG_ENTRYPOINT -> RAG_PATTERN_MAP -> method card -> esempio svolto -> risposta compatta da esame.
```

---

## Task 3 - Creare policy fonti

Creare `00_meta/SOURCE_RELIABILITY_POLICY.md`.

Contenuto richiesto:

```md
# Policy di affidabilità delle fonti

## Ordine di priorità

1. Fonti ufficiali dei professori.
2. Esercizi/appelli ufficiali.
3. Soluzioni ufficiali o dispense collegate al corso.
4. Materiali condivisi su Mega dai compagni.
5. Appunti rielaborati nella KB.
6. Inferenze del modello AI.

## Regole operative

- Non sovrascrivere mai una fonte ufficiale con una fonte Mega se c'è conflitto.
- Se una fonte Mega contiene una soluzione utile ma non confermata, marcarla come `reliability: community`.
- Se un passaggio è ricostruito e non direttamente scritto nella fonte, marcarlo come `inference`.
- Se una formula o procedura è dubbia, aggiungere warning in `10_rag/RAG_GAPS_AND_WARNINGS.md`.
- Ogni method card deve citare almeno una fonte o dichiarare che è una sintesi trasversale.
```

---

## Task 4 - Creare inventario automatico dei raw asset

Creare `scripts/inventory_assets.py`.

Scopo:

- scandire `raw_assets/` ricorsivamente;
- produrre un inventario Markdown;
- indicare path, estensione, dimensione, probabile categoria, affidabilità iniziale;
- creare `01_sources/SOURCE_INVENTORY.md`;
- creare anche un CSV opzionale `01_sources/source_inventory.csv`.

Script proposto:

```python
from pathlib import Path
import csv
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "raw_assets"
OUT_MD = ROOT / "01_sources" / "SOURCE_INVENTORY.md"
OUT_CSV = ROOT / "01_sources" / "source_inventory.csv"

OFFICIAL_HINTS = [
    "programmazione lineare",
    "programmazione lineare intera",
    "programmazione non lineare",
    "lezione",
    "dispensa",
    "esercizi",
    "slide",
]

COMMUNITY_HINTS = [
    "mega",
    "appunti",
    "riassunto",
    "soluzione",
]


def classify_source(path: Path) -> tuple[str, str]:
    text = str(path).lower()

    if "raw_assets/mega" in text.replace("\\", "/"):
        return "community", "materiale condiviso Mega"

    if any(h in text for h in OFFICIAL_HINTS):
        return "official-candidate", "possibile materiale ufficiale o corso"

    if any(h in text for h in COMMUNITY_HINTS):
        return "community-candidate", "possibile materiale condiviso/appunti"

    return "unclassified", "da classificare manualmente"


def human_size(num_bytes: int) -> str:
    units = ["B", "KB", "MB", "GB"]
    size = float(num_bytes)
    for unit in units:
        if size < 1024 or unit == units[-1]:
            return f"{size:.1f} {unit}"
        size /= 1024


def main() -> None:
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)

    files = sorted([p for p in RAW.rglob("*") if p.is_file()])

    rows = []
    for idx, path in enumerate(files, start=1):
        reliability, note = classify_source(path.relative_to(ROOT))
        rows.append({
            "id": f"SRC-{idx:04d}",
            "path": str(path.relative_to(ROOT)).replace("\\", "/"),
            "name": path.name,
            "extension": path.suffix.lower() or "none",
            "size": human_size(path.stat().st_size),
            "reliability": reliability,
            "note": note,
        })

    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys() if rows else ["id", "path"])
        writer.writeheader()
        writer.writerows(rows)

    lines = []
    lines.append("# Inventario fonti ROPR")
    lines.append("")
    lines.append(f"Generato automaticamente: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    lines.append("## Statistiche")
    lines.append("")
    lines.append(f"- File totali: {len(rows)}")
    lines.append("")
    lines.append("## Inventario")
    lines.append("")
    lines.append("| ID | File | Estensione | Dimensione | Affidabilità iniziale | Note |")
    lines.append("|---|---|---:|---:|---|---|")

    for row in rows:
        lines.append(
            f"| {row['id']} | `{row['path']}` | `{row['extension']}` | {row['size']} | {row['reliability']} | {row['note']} |"
        )

    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_MD}")
    print(f"Wrote {OUT_CSV}")


if __name__ == "__main__":
    main()
```

Dopo aver creato lo script, eseguire:

```bash
python scripts/inventory_assets.py
```

Commit atteso:

```text
chore: initialize source inventory workflow
```

---

## Task 5 - Creare template di ingestione asset

Creare `templates/asset_ingestion_template.md`.

```md
# Asset ingestion report - <NOME_ASSET>

## Metadata

- Source ID: `<SRC-XXXX>`
- Path: `<raw_assets/...>`
- Tipo file: `<pdf/docx/md/image/...>`
- Categoria: `<teoria/esercizi/soluzioni/appunti/formulario/altro>`
- Area ROPR: `<PL/PLI/PNL/reti/modellazione/altro>`
- Affidabilità: `<official/community/unclassified>`
- Stato analisi: `<draft/reviewed/consolidated>`

## Sintesi contenuto

Scrivere una sintesi breve del contenuto dell'asset.

## Concetti teorici estratti

- Concetto 1
- Concetto 2
- Concetto 3

## Formule e definizioni importanti

$$
...
$$

## Procedure/metodi operativi

Per ogni metodo individuato:

### Metodo: <nome>

- Quando si usa:
- Input tipico:
- Output richiesto:
- Passaggi:
- Errori comuni:
- File da creare/aggiornare:

## Esercizi presenti

| ID esercizio | Argomento | Tipo | Richiede method card? | Note |
|---|---|---|---|---|
| EX-0001 |  |  | sì/no |  |

## Possibili pattern d'esame

- Pattern 1
- Pattern 2

## Materiale da creare nella KB

- [ ] Nota teoria in `05_theory/...`
- [ ] Method card in `04_methods/...`
- [ ] Esempio svolto in `07_solved_examples/...`
- [ ] Aggiornamento catalogo in `03_exercise_catalog/...`
- [ ] Aggiornamento RAG in `10_rag/...`
- [ ] Flashcard in `08_flashcards/...`

## Warning / dubbi

- Dubbi sulla fonte:
- Parti illeggibili:
- Conflitti con altre fonti:

## Piano operativo per Codex

Elencare esattamente i file da creare/modificare e cosa scriverci.
```

---

## Task 6 - Creare template per batch di asset

Creare `templates/batch_ingestion_template.md`.

```md
# Batch ingestion report - <NOME_BATCH>

## Asset analizzati

| Source ID | Path | Tipo | Affidabilità | Stato |
|---|---|---|---|---|
| SRC-XXXX | `raw_assets/...` |  |  |  |

## Obiettivo del batch

Spiegare perché questi asset sono analizzati insieme.

## Mappa contenuti emersi

| Tema | Fonti | Output KB necessario |
|---|---|---|
|  |  |  |

## Nuove note da creare

- `05_theory/...`
- `04_methods/...`
- `07_solved_examples/...`

## File RAG da aggiornare

- `10_rag/RAG_RETRIEVAL_INDEX.md`
- `10_rag/RAG_PATTERN_MAP.md`
- `10_rag/RAG_GAPS_AND_WARNINGS.md`

## Piano Codex dettagliato

1. Creare/modificare file X.
2. Inserire contenuto Y.
3. Aggiornare indice Z.
4. Eseguire controlli finali.

## Checklist qualità

- [ ] Tutte le fonti sono citate.
- [ ] Le formule usano LaTeX.
- [ ] I metodi sono copiabili da esame.
- [ ] Le parti dubbie sono segnalate.
- [ ] Il RAG punta ai file nuovi.
```

---

## Task 7 - Creare template note teoriche

Creare `templates/theory_note_template.md`.

```md
---
type: theory-note
topic: <topic>
status: draft
sources:
  - <source path>
reliability: <official/community/mixed>
---

# <Titolo>

## Idea principale

Spiegazione compatta.

## Definizioni

### <Definizione>

...

## Formule principali

$$
...
$$

## Interpretazione operativa

Come usare questo concetto negli esercizi.

## Collegamenti

- Method card: [[...]]
- Esempi svolti: [[...]]
- Pattern d'esame: [[...]]

## Errori comuni

- ...

## Fonti

- `raw_assets/...`
```

---

## Task 8 - Creare template method card

Creare `templates/method_card_template.md`.

```md
---
type: method-card
topic: <topic>
status: draft
sources:
  - <source path>
reliability: <official/community/mixed>
---

# Metodo - <Nome metodo>

## Quando si usa

Usare questo metodo quando la traccia chiede...

## Input tipico

- ...

## Output richiesto

- ...

## Procedura da esame

1. ...
2. ...
3. ...

## Formule / modello

$$
...
$$

## Pseudocodice / schema operativo

```text
...
```

## Complessità / condizioni / note

- ...

## Errori comuni

- ...

## Mini-template di risposta

```text
Definisco ...
Il modello è ...
La soluzione si ottiene ...
```

## Collegamenti RAG

- Pattern: [[...]]
- Esempi: [[...]]
- Teoria: [[...]]

## Fonti

- `raw_assets/...`
```

---

## Task 9 - Creare template esempi svolti

Creare `templates/solved_example_template.md`.

```md
---
type: solved-example
topic: <topic>
status: draft
sources:
  - <source path>
reliability: <official/community/mixed>
---

# Esempio svolto - <Titolo>

## Traccia sintetica

Non trascrivere necessariamente tutta la traccia: riportare solo ciò che serve.

## Pattern riconosciuto

- Pattern:
- Method card:

## Soluzione da esame

Scrivere la soluzione nel formato copiabile sul foglio.

## Passaggi di controllo

- ...

## Errori comuni

- ...

## Fonti

- `raw_assets/...`
```

---

## Task 10 - Creare file RAG base

### `10_rag/RAG_ENTRYPOINT.md`

```md
# RAG Entrypoint - ROPR

Questo file è il punto di ingresso per una chat AI che deve usare questa repo come RAG.

## Ordine di consultazione

1. `10_rag/RAG_SOURCE_POLICY.md`
2. `10_rag/RAG_PATTERN_MAP.md`
3. `10_rag/RAG_RETRIEVAL_INDEX.md`
4. `04_methods/` per il metodo operativo
5. `07_solved_examples/` per esempi copiabili
6. `05_theory/` per definizioni e teoremi
7. `10_rag/RAG_GAPS_AND_WARNINGS.md` per warning noti
8. `AI Chat during Exam/Final Prompt.md` per stile finale

## Regola fondamentale

Non inventare procedure, formule o teoremi non presenti nella KB. Se manca una parte, dichiararlo in modo breve e usare la soluzione più standard solo se coerente con le fonti disponibili.
```

### `10_rag/RAG_SOURCE_POLICY.md`

```md
# RAG Source Policy

## Priorità fonti

1. Fonti ufficiali professori.
2. Esercizi/appelli ufficiali.
3. Soluzioni ufficiali.
4. Materiali Mega.
5. Sintesi KB.
6. Inferenze AI.

## Regole per la chat AI

- Se una formula compare in fonti ufficiali, usare quella.
- Se una fonte Mega contraddice una fonte ufficiale, ignorare la fonte Mega.
- Se la traccia è fotografata male, dichiarare l'assunzione minima e procedere.
- Se il pattern non è chiaro, scegliere il pattern più vicino e segnalarlo in una riga.
```

### `10_rag/RAG_PATTERN_MAP.md`

Creare file iniziale vuoto ma strutturato:

```md
# RAG Pattern Map - ROPR

## Come usare questo file

Quando arriva una traccia d'esame, identificare parole chiave, forma del problema e output richiesto.

## Pattern iniziali attesi

| Pattern | Parole chiave | File metodo | Esempi |
|---|---|---|---|
| Modellazione PL | variabili decisionali, vincoli, funzione obiettivo | `04_methods/programmazione_lineare/` | `07_solved_examples/programmazione_lineare/` |
| Metodo del simplesso | base, tableau, variabile entrante/uscente | `04_methods/programmazione_lineare/` | `07_solved_examples/programmazione_lineare/` |
| Dualità | duale, primale, prezzi ombra | `05_theory/dualita_sensitivita/` | `07_solved_examples/programmazione_lineare/` |
| Programmazione lineare intera | variabili binarie/intere, branch and bound, cutting planes | `04_methods/programmazione_lineare_intera/` | `07_solved_examples/programmazione_lineare_intera/` |
| Programmazione non lineare | KKT, gradiente, Hessiana, vincoli non lineari | `04_methods/programmazione_non_lineare/` | `07_solved_examples/programmazione_non_lineare/` |
```

### `10_rag/RAG_RETRIEVAL_INDEX.md`

```md
# RAG Retrieval Index - ROPR

## Query d'esame -> file da consultare

| Query / richiesta | Prima fonte | Seconda fonte | Note |
|---|---|---|---|
| formulare un modello di programmazione lineare | `04_methods/programmazione_lineare/` | `05_theory/programmazione_lineare/` | Da completare dopo ingestion |
| risolvere con simplesso | `04_methods/programmazione_lineare/` | `07_solved_examples/programmazione_lineare/` | Da completare dopo ingestion |
| scrivere il duale | `05_theory/dualita_sensitivita/` | `04_methods/programmazione_lineare/` | Da completare dopo ingestion |
| branch and bound | `04_methods/programmazione_lineare_intera/` | `07_solved_examples/programmazione_lineare_intera/` | Da completare dopo ingestion |
| condizioni KKT | `04_methods/programmazione_non_lineare/` | `05_theory/programmazione_non_lineare/` | Da completare dopo ingestion |
```

### `10_rag/RAG_RESPONSE_STYLE.md`

```md
# RAG Response Style - ROPR

Le risposte devono essere:

- concise;
- complete ma non prolisse;
- scritte in tono da studente universitario preparato;
- copiabili sul foglio d'esame;
- con formule in LaTeX;
- senza divagazioni;
- senza spiegare il processo interno della chat;
- con assunzioni esplicite solo se necessarie.

## Struttura tipica esercizio

1. Definizione variabili / dati.
2. Modello o metodo.
3. Passaggi essenziali.
4. Risultato finale.
5. Controllo/interpretazione se richiesto.
```

### `10_rag/RAG_GAPS_AND_WARNINGS.md`

```md
# Gap e warning RAG

Questo file raccoglie dubbi, conflitti e parti mancanti.

## Warning attivi

| ID | Tema | Problema | Impatto | Stato |
|---|---|---|---|---|
| WARN-0001 | Inizializzazione | Fonti non ancora analizzate | RAG incompleto | aperto |
```

---

## Task 11 - Creare prompt finale per chat AI durante esame

Creare `AI Chat during Exam/Final Prompt.md`.

```md
# Final Prompt - ROPR Exam Assistant

Sei un assistente per l'esame di Ricerca Operativa e Pianificazione delle Risorse.

Devi rispondere usando questa repository come Knowledge Base/RAG. Non devi inventare metodi, formule o teoremi se nella repo sono disponibili fonti più affidabili.

## Fonti da consultare sempre

Prima di rispondere a una traccia:

1. consulta `10_rag/RAG_ENTRYPOINT.md`;
2. riconosci il pattern tramite `10_rag/RAG_PATTERN_MAP.md`;
3. usa `10_rag/RAG_RETRIEVAL_INDEX.md` per scegliere i file;
4. consulta la method card in `04_methods/`;
5. se disponibile, consulta un esempio simile in `07_solved_examples/`;
6. per teoria, consulta `05_theory/`;
7. controlla warning in `10_rag/RAG_GAPS_AND_WARNINGS.md`.

## Stile risposta

Rispondi come uno studente universitario preparato durante uno scritto.

La risposta deve essere:

- completa ma concisa;
- copiabile a mano;
- senza spiegazioni superflue;
- con formule in LaTeX;
- con terminologia precisa;
- senza tono da professore;
- senza lunghi paragrafi introduttivi;
- senza citare file della repo nella risposta finale, a meno che venga richiesto.

## Se arriva una foto

1. Leggi la traccia.
2. Se una parte è illeggibile, dichiaralo in una sola riga.
3. Fai l'assunzione minima necessaria.
4. Risolvi l'esercizio nel formato da esame.
5. Controlla coerenza di formule, vincoli e risultato.

## Formato preferito per esercizi di modellazione

1. Variabili decisionali.
2. Funzione obiettivo.
3. Vincoli.
4. Dominio delle variabili.
5. Breve interpretazione finale se utile.

## Formato preferito per esercizi algoritmici/metodologici

1. Riconoscimento del metodo.
2. Passaggi essenziali.
3. Calcoli/tableau/condizioni.
4. Risultato.
5. Controllo finale.

## Regola anti-allucinazione

Se non trovi un metodo specifico nella KB, dillo brevemente e usa solo il metodo standard più coerente con il tipo di traccia.
```

---

## Task 12 - Creare prompt per NotebookLM

Creare `notebooklm/NOTEBOOKLM_CONTEXT.md`.

```md
# NotebookLM Context - ROPR

Questa Knowledge Base contiene materiali per preparare l'esame di Ricerca Operativa e Pianificazione delle Risorse.

## Obiettivo dello studio

Studiare la materia in modo operativo, con attenzione a:

- teoria essenziale;
- formule;
- metodi di risoluzione;
- modellazione;
- esercizi svolti;
- pattern d'esame.

## Come usare le fonti

Priorità:

1. fonti ufficiali professori;
2. esercizi/appelli ufficiali;
3. soluzioni ufficiali;
4. materiali condivisi dagli studenti;
5. sintesi della KB.

## Cosa voglio ottenere

Quando faccio domande, voglio risposte:

- precise;
- compatte;
- orientate all'esame;
- con formule corrette;
- con esempi se servono;
- senza divagazioni.
```

---

## Task 13 - Creare `AI_CONTEXT.md`

Creare `AI_CONTEXT.md` nella root.

```md
# AI Context - knowledge_base_ROPR

Questa repo è una Knowledge Base per Ricerca Operativa e Pianificazione delle Risorse.

## Obiettivo

La repo deve servire sia come vault Obsidian per lo studio sia come RAG per una chat AI da usare durante simulazioni ed esame.

## Stato iniziale

I file originali sono in `raw_assets/`.

Cartelle raw iniziali:

- `raw_assets/Mega/`
- `raw_assets/Programmazione Lineare/`
- `raw_assets/Programmazione Lineare Intera/`
- `raw_assets/Programmazione Non Lineare/`

## Convenzioni

- Non modificare `raw_assets/`.
- Ogni asset analizzato deve produrre un report in `09_ingestion_reports/`.
- Ogni concetto consolidato deve finire in `05_theory/`.
- Ogni procedura d'esame deve finire in `04_methods/`.
- Ogni esempio utile deve finire in `07_solved_examples/`.
- Ogni file utile al RAG deve essere collegato da `10_rag/`.

## Stile

Markdown Obsidian, formule LaTeX, niente emoji, risposte da esame concise.
```

---

## Task 14 - Creare `PROJECT_STATUS.md` e `TODO.md`

### `PROJECT_STATUS.md`

```md
# Project Status - ROPR KB

## Stato attuale

- [x] Repo creata.
- [x] Raw assets caricati.
- [ ] Struttura KB inizializzata.
- [ ] Inventario fonti generato.
- [ ] Fonti classificate per affidabilità.
- [ ] Prima batch di asset analizzata.
- [ ] RAG iniziale popolato.
- [ ] Prompt finale testato su esercizi.

## Fasi

1. Setup repo.
2. Inventario fonti.
3. Ingestion asset ufficiali.
4. Ingestion asset Mega utili.
5. Consolidamento teoria/metodi.
6. Creazione RAG.
7. Test su esercizi/foto.
8. Audit finale.
```

### `TODO.md`

```md
# TODO - ROPR KB

## Setup

- [ ] Creare struttura cartelle.
- [ ] Creare template.
- [ ] Creare script inventario.
- [ ] Eseguire inventario.
- [ ] Classificare fonti.

## Ingestion

- [ ] Analizzare fonti ufficiali di Programmazione Lineare.
- [ ] Analizzare fonti ufficiali di Programmazione Lineare Intera.
- [ ] Analizzare fonti ufficiali di Programmazione Non Lineare.
- [ ] Analizzare materiali Mega rilevanti.

## Consolidamento

- [ ] Creare note teoria.
- [ ] Creare method card.
- [ ] Creare esempi svolti.
- [ ] Creare flashcard.
- [ ] Aggiornare RAG.

## Esame

- [ ] Scrivere prompt finale.
- [ ] Testare su tracce/foto.
- [ ] Correggere warning.
- [ ] Fare audit finale.
```

---

## Task 15 - Creare script di controllo base

### `scripts/check_links.py`

Obiettivo: trovare link Markdown locali rotti.

Versione semplice:

```python
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MD_FILES = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
WIKI_RE = re.compile(r"\[\[([^\]]+)\]\]")


def main() -> None:
    broken = []

    for md in MD_FILES:
        text = md.read_text(encoding="utf-8", errors="ignore")

        for _, target in LINK_RE.findall(text):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target_path = (md.parent / target).resolve()
            if not target_path.exists():
                broken.append((md.relative_to(ROOT), target))

    if broken:
        print("Broken markdown links:")
        for src, target in broken:
            print(f"- {src}: {target}")
        raise SystemExit(1)

    print("No broken markdown links found.")


if __name__ == "__main__":
    main()
```

### `scripts/check_frontmatter.py`

Obiettivo: controllare che file in cartelle importanti abbiano frontmatter.

```python
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECK_DIRS = [
    "04_methods",
    "05_theory",
    "07_solved_examples",
]


def has_frontmatter(text: str) -> bool:
    return text.startswith("---\n") and "\n---\n" in text[4:]


def main() -> None:
    missing = []
    for folder in CHECK_DIRS:
        for path in (ROOT / folder).rglob("*.md"):
            if path.name.lower() == "readme.md":
                continue
            text = path.read_text(encoding="utf-8", errors="ignore")
            if not has_frontmatter(text):
                missing.append(path.relative_to(ROOT))

    if missing:
        print("Files without frontmatter:")
        for path in missing:
            print(f"- {path}")
        raise SystemExit(1)

    print("Frontmatter check passed.")


if __name__ == "__main__":
    main()
```

---

## Task 16 - Creare `.gitignore`

```gitignore
# OS
.DS_Store
Thumbs.db

# Python
__pycache__/
*.py[cod]
.venv/
venv/

# Generated temporary files
*.tmp
*.bak

# Optional extraction output
_extracted_text_tmp/

# Large local-only exports if needed
local_exports/
```

Non ignorare `raw_assets/`, perché in questa repo i file sorgente devono rimanere versionati se sono già stati caricati.

---

## Task 17 - Creare README per cartelle principali

Creare un `README.md` in ogni cartella principale con scopo e regole.

Esempio per `04_methods/README.md`:

```md
# Methods

Questa cartella contiene method card operative per risolvere esercizi di ROPR.

Ogni method card deve indicare:

- quando si usa il metodo;
- input tipico;
- output richiesto;
- procedura da esame;
- formule principali;
- errori comuni;
- fonti;
- collegamenti a esempi e teoria.

Le method card devono essere concise e direttamente utilizzabili durante simulazioni/esame.
```

Esempio per `05_theory/README.md`:

```md
# Theory

Questa cartella contiene la teoria consolidata da studiare in Obsidian.

Le note devono essere:

- compatte;
- collegate tra loro;
- basate sulle fonti;
- scritte in Markdown con formule LaTeX;
- orientate all'uso negli esercizi.
```

---

## Task 18 - Creare piano di ingestione iniziale

Creare `plans/000_setup_and_ingestion_strategy.md` con questa strategia:

```md
# Strategia di ingestione ROPR

## Fase 1 - Setup

- Creare struttura cartelle.
- Creare template.
- Creare script inventario.
- Generare inventario fonti.
- Classificare fonti in ufficiali, Mega, non classificate.

## Fase 2 - Fonti ufficiali

Analizzare prima le fonti ufficiali in questo ordine:

1. Programmazione Lineare.
2. Programmazione Lineare Intera.
3. Programmazione Non Lineare.

Per ogni asset ufficiale:

- creare report in `09_ingestion_reports/asset_reports/`;
- creare/aggiornare note teoria;
- creare/aggiornare method card;
- creare esempi svolti se presenti;
- aggiornare RAG.

## Fase 3 - Materiali Mega

Usare i materiali Mega solo dopo aver consolidato le fonti ufficiali.

Obiettivi:

- trovare esercizi aggiuntivi;
- trovare soluzioni alternative;
- individuare pattern d'esame;
- creare flashcard o chiarimenti.

## Fase 4 - Consolidamento

- Eliminare duplicati concettuali.
- Unificare notazione.
- Aggiornare indici.
- Creare prompt finale.
- Testare su esercizi.

## Fase 5 - Audit finale

- Controllare link.
- Controllare frontmatter.
- Controllare warning.
- Testare RAG con tracce fotografiche.
```

---

## Task 19 - Creare script placeholder `build_rag_index.py`

Lo script non deve generare contenuti intelligenti da solo, ma aiutare a mantenere l'indice.

Creare `scripts/build_rag_index.py`:

```python
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAG_INDEX = ROOT / "10_rag" / "RAG_RETRIEVAL_INDEX.md"
WATCH_DIRS = ["04_methods", "05_theory", "07_solved_examples", "06_exam_patterns"]


def collect_md_files():
    rows = []
    for folder in WATCH_DIRS:
        base = ROOT / folder
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            if path.name.lower() == "readme.md":
                continue
            rows.append(str(path.relative_to(ROOT)).replace("\\", "/"))
    return rows


def main():
    files = collect_md_files()
    lines = []
    lines.append("# RAG Retrieval Index - ROPR")
    lines.append("")
    lines.append("Indice semi-automatico dei file utili al retrieval.")
    lines.append("")
    lines.append("## File indicizzabili")
    lines.append("")
    for file in files:
        lines.append(f"- `{file}`")
    lines.append("")
    lines.append("## Query d'esame -> file da consultare")
    lines.append("")
    lines.append("| Query / richiesta | Prima fonte | Seconda fonte | Note |")
    lines.append("|---|---|---|---|")
    lines.append("| Da completare manualmente |  |  |  |")

    RAG_INDEX.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Wrote {RAG_INDEX}")


if __name__ == "__main__":
    main()
```

Nota: non usare questo script se `RAG_RETRIEVAL_INDEX.md` è già stato compilato manualmente con contenuti migliori, a meno di volerlo rigenerare.

---

## Task 20 - Commit finale atteso

Dopo aver completato i task:

```bash
python scripts/inventory_assets.py
python scripts/check_links.py
python scripts/check_frontmatter.py
```

Se i controlli passano:

```bash
git add .
git commit -m "chore: initialize ROPR knowledge base structure"
```

---

## Criteri di accettazione

La task è completa quando:

- [ ] la repo contiene tutte le cartelle principali;
- [ ] `README.md` spiega scopo e uso della KB;
- [ ] `.obsidian/` è presente;
- [ ] `AI_CONTEXT.md`, `PROJECT_STATUS.md`, `TODO.md` sono presenti;
- [ ] `01_sources/SOURCE_INVENTORY.md` è generato;
- [ ] `templates/` contiene i template necessari;
- [ ] `10_rag/` contiene entrypoint, policy, retrieval index, pattern map, response style e warning;
- [ ] `AI Chat during Exam/Final Prompt.md` esiste;
- [ ] `notebooklm/` contiene il contesto base;
- [ ] gli script base funzionano;
- [ ] `raw_assets/` non è stato modificato;
- [ ] non sono state inventate note teoriche non ancora analizzate;
- [ ] il commit finale è pulito.

---

## Cosa NON fare in questa fase

- Non analizzare ancora profondamente tutti i PDF.
- Non creare method card complete senza aver letto le fonti.
- Non inventare formule o procedure.
- Non spostare o rinominare i file in `raw_assets/` senza motivo.
- Non cancellare materiali Mega solo perché sembrano duplicati.
- Non generare un RAG finale completo: per ora va creata la struttura.

---

## Prossimo step dopo questo piano

Dopo l'inizializzazione, il workflow consigliato sarà:

1. eseguire inventario;
2. scegliere una piccola batch di fonti ufficiali, preferibilmente `Programmazione Lineare`;
3. mandare gli asset a ChatGPT/Gemini per analisi;
4. generare un `batch_ingestion_report`;
5. far applicare a Codex il piano;
6. ripetere per `Programmazione Lineare Intera`, `Programmazione Non Lineare`, poi `Mega`;
7. fare audit finale e test con foto d'esame.

