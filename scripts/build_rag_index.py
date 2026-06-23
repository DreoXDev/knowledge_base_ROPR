from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
RAG_INDEX = ROOT / "10_rag" / "RAG_RETRIEVAL_INDEX.md"
WATCH_DIRS = ["03_exercise_catalog", "04_methods", "05_theory", "07_solved_examples", "06_exam_patterns"]


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
    
    # Build the file list section
    file_list_lines = ["## File indicizzabili", ""]
    for file in files:
        file_list_lines.append(f"- `{file}`")
    file_list_lines.append("")
    file_list_text = "\n".join(file_list_lines)

    # Read existing file to preserve other sections
    existing_content = ""
    if RAG_INDEX.exists():
        existing_content = RAG_INDEX.read_text(encoding="utf-8")

    if existing_content:
        # We find "## File indicizzabili" and replace until the next "## " header
        # or the end of the file.
        pattern = r"(## File indicizzabili\n.*?(?=\n## |$))"
        # We use re.DOTALL to match newlines as well
        new_content, count = re.subn(pattern, file_list_text, existing_content, flags=re.DOTALL)
        if count == 0:
            # If pattern not found, recreate the whole file
            new_content = build_full_index(file_list_text)
    else:
        new_content = build_full_index(file_list_text)

    RAG_INDEX.write_text(new_content, encoding="utf-8")
    print(f"Wrote {RAG_INDEX}")


def build_full_index(file_list_text):
    lines = [
        "# RAG Retrieval Index - ROPR",
        "",
        "Indice semi-automatico dei file utili al retrieval.",
        "",
        file_list_text,
        "## Query d'esame -> file da consultare",
        "",
        "| Query / richiesta | Prima fonte | Seconda fonte | Note |",
        "|---|---|---|---|",
        "| Da completare manualmente |  |  |  |",
        ""
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    main()
