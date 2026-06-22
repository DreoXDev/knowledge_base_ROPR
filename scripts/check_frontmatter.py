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
        base = ROOT / folder
        if not base.exists():
            continue
        for path in base.rglob("*.md"):
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
