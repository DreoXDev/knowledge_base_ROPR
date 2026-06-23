import os
from pypdf import PdfReader
from pathlib import Path

ROOT = Path(r"c:\Users\User\Desktop\Knowledge Bases\knowledge_base_ROPR")
PDF_PATH = ROOT / "raw_assets" / "Programmazione Non Lineare" / "PNL 1D.pdf"
OUT_PATH = ROOT / "scripts" / "pnl_1d_text.txt"

def main():
    if not PDF_PATH.exists():
        print(f"Error: {PDF_PATH} does not exist")
        return
    
    reader = PdfReader(PDF_PATH)
    lines = [f"Number of pages: {len(reader.pages)}"]
    
    for i in range(len(reader.pages)):
        lines.append(f"\n--- Page {i+1} ---")
        text = reader.pages[i].extract_text()
        if text:
            lines.append(text.strip())
        else:
            lines.append("[Empty]")
            
    OUT_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"Extracted {len(reader.pages)} pages to {OUT_PATH}")

if __name__ == "__main__":
    main()
