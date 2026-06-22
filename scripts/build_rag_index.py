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
