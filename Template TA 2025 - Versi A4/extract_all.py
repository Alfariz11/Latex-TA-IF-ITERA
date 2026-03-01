import PyPDF2, os, sys

paper_dir = "PAPER"
out_dir = "extracted_texts"
os.makedirs(out_dir, exist_ok=True)

files = sorted([f for f in os.listdir(paper_dir) if f.endswith('.pdf')])
print(f"Found {len(files)} PDFs")

for i, fname in enumerate(files):
    safe_name = fname.replace('.pdf','').replace(' ','_')[:60] + '.txt'
    outpath = os.path.join(out_dir, safe_name)
    if os.path.exists(outpath):
        print(f"[{i+1}/{len(files)}] SKIP (exists): {fname[:60]}")
        continue
    try:
        reader = PyPDF2.PdfReader(os.path.join(paper_dir, fname))
        text = ""
        for page in reader.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
        with open(outpath, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"[{i+1}/{len(files)}] OK ({len(reader.pages)}p): {fname[:60]}")
    except Exception as e:
        print(f"[{i+1}/{len(files)}] ERROR: {fname[:60]} -> {e}")

print("DONE")
