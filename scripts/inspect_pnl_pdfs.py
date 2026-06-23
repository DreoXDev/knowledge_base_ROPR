import os
from pypdf import PdfReader
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PNL_DIR = ROOT / "raw_assets" / "Programmazione Non Lineare"
OUT_FILE = ROOT / "scripts" / "pnl_inspected_text.txt"

PDFS = [
    "PNL.pdf",
    "PNL 1D.pdf",
    "PNL 2D.pdf",
    "PNL 2D 1.pdf",
    "PNL_non_vincolata.pdf",
    "PNL_nonvincolata.pdf",
    "PNL_vincolata.pdf",
    "Ottimizzazione non lineare vincolata.pdf",
    "PNL Vincolata 4.pdf",
    "20_esercizi_pnl.pdf",
    "esercizi_riepilogo.pdf"
]

def main():
    lines = []
    for name in PDFS:
        path = PNL_DIR / name
        if not path.exists():
            lines.append(f"File not found: {name}")
            continue
        lines.append(f"\n==================== {name} ====================")
        try:
            reader = PdfReader(path)
            lines.append(f"Number of pages: {len(reader.pages)}")
            
            # Print outline / outline-like info if available
            outline = reader.outline
            if outline:
                lines.append("Outline available:")
                def dump_outline(items, depth=0):
                    out = []
                    for item in items:
                        if isinstance(item, list):
                            out.extend(dump_outline(item, depth + 1))
                        else:
                            title = item.get('/Title', 'Untitled')
                            out.append("  " * depth + f"- {title}")
                    return out
                try:
                    lines.extend(dump_outline(outline))
                except Exception as oe:
                    lines.append(f"Could not dump outline: {oe}")
            
            # Extract first 5 pages for each PDF
            for i in range(min(5, len(reader.pages))):
                lines.append(f"\n--- Page {i+1} ---")
                text = reader.pages[i].extract_text()
                if text:
                    lines.append(text.strip())
                else:
                    lines.append("[Empty or scanned image]")
        except Exception as e:
            lines.append(f"Error reading {name}: {e}")
            
    OUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote to {OUT_FILE}")

if __name__ == "__main__":
    main()
