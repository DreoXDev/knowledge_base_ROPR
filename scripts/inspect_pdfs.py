from pypdf import PdfReader
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLI_DIR = ROOT / "raw_assets" / "Programmazione Lineare Intera"
PDFS = [
    "branch_and_bound.pdf",
    "BB PLI.pdf",
    "16_esercizi_BB.pdf",
    "Programmazione Lineare Intera_Branch and Bound binario.pdf",
    "9_esercizi_modelli.pdf",
    "Programmazione lineare intera completo.pdf"
]
OUT_FILE = ROOT / "scripts" / "pdf_inspected_text.txt"

def main():
    lines = []
    for name in PDFS:
        path = PLI_DIR / name
        if not path.exists():
            lines.append(f"File not found: {name}")
            continue
        lines.append(f"\n==================== {name} ====================")
        try:
            reader = PdfReader(path)
            lines.append(f"Number of pages: {len(reader.pages)}")
            # Extract first 5 pages for each PDF
            for i in range(min(5, len(reader.pages))):
                lines.append(f"\n--- Page {i+1} ---")
                text = reader.pages[i].extract_text()
                lines.append(text)
        except Exception as e:
            lines.append(f"Error reading {name}: {e}")
            
    OUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote to {OUT_FILE}")

if __name__ == "__main__":
    main()
