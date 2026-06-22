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
