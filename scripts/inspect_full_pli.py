from pypdf import PdfReader
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = ROOT / "raw_assets" / "Programmazione Lineare Intera" / "Programmazione lineare intera completo.pdf"
OUT_FILE = ROOT / "scripts" / "pli_completo_text.txt"

def main():
    if not PDF_PATH.exists():
        print("File not found")
        return
    reader = PdfReader(PDF_PATH)
    lines = []
    for i, page in enumerate(reader.pages):
        lines.append(f"\n==================== Page {i+1} ====================")
        lines.append(page.extract_text())
    OUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {len(reader.pages)} pages to {OUT_FILE}")

if __name__ == "__main__":
    main()
