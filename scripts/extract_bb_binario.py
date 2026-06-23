from pypdf import PdfReader
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PDF_PATH = ROOT / "raw_assets" / "Programmazione Lineare Intera" / "Programmazione Lineare Intera_Branch and Bound binario.pdf"
TEXT_OUT = ROOT / "scripts" / "bb_binario_text.txt"
OUTLINE_OUT = ROOT / "scripts" / "bb_binario_outline.txt"

def main():
    if not PDF_PATH.exists():
        print(f"Error: {PDF_PATH} does not exist.")
        return

    reader = PdfReader(PDF_PATH)
    text_lines = []
    outline_lines = []

    print(f"Extracting {len(reader.pages)} pages...")
    for idx, page in enumerate(reader.pages):
        page_num = idx + 1
        text = page.extract_text()
        
        # Save full text
        text_lines.append(f"\n==================== Page {page_num} ====================")
        text_lines.append(text)
        
        # Extract first non-empty line as outline title
        first_line = "Empty Page"
        for line in text.split("\n"):
            line_str = line.strip()
            if line_str:
                first_line = line_str
                break
        outline_lines.append(f"{page_num} ==================== | {first_line}")

    TEXT_OUT.write_text("\n".join(text_lines), encoding="utf-8")
    OUTLINE_OUT.write_text("\n".join(outline_lines), encoding="utf-8")
    print("Done! Extracted text and outline.")

if __name__ == "__main__":
    main()
