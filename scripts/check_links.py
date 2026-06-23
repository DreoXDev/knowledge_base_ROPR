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
            # Strip anchor from target path if present
            target_file = target.split("#")[0]
            if not target_file:
                continue
            target_path = (md.parent / target_file).resolve()
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
