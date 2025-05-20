import json
from PyPDF2 import PdfReader

def extract_pdf_text(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def main(pdf_path, json_path):
    text = extract_pdf_text(pdf_path)
    # For demo: No table extraction, just text as header
    data = {
        "header": text,
        "List_items": []  # Table extraction not implemented here
    }
    with open(json_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Extracted text saved to {json_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python extract_pdf_to_json.py <pdf_path> <json_path>")
    else:
        main(sys.argv[1], sys.argv[2])