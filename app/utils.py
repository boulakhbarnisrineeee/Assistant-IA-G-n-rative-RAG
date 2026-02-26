import fitz  # PyMuPDF


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract raw text from a PDF file.
    """
    doc = fitz.open(pdf_path)
    pages_text = []

    for page in doc:
        pages_text.append(page.get_text("text"))

    doc.close()
    return "\n".join(pages_text)


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100):
    """
    Split text into overlapping chunks.
    """
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks

