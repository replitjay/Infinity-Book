import fitz
from pathlib import Path


pdf_path = Path("attached_assets/Infinity_Book_Website_Design_Specification_1786978376654.pdf")
out_dir = Path(".agents/outputs/infinity_spec_pages")
out_dir.mkdir(parents=True, exist_ok=True)

doc = fitz.open(pdf_path)
print(f"pages={doc.page_count}")
for index, page in enumerate(doc):
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
    out_path = out_dir / f"page-{index + 1:02d}.png"
    pix.save(out_path)
    print(out_path)