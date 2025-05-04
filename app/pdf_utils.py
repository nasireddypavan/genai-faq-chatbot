# app/pdf_utils.py

import pypdf
import tiktoken

CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

def extract_text_from_pdf(file_path: str):
    reader = pypdf.PdfReader(file_path)
    full_text = ""

    for page in reader.pages:
        full_text += page.extract_text() or ""

    return chunk_text(full_text)


def chunk_text(text: str):
    # Split into overlapping chunks by tokens
    tokenizer = tiktoken.get_encoding("cl100k_base")
    tokens = tokenizer.encode(text)

    chunks = []
    for i in range(0, len(tokens), CHUNK_SIZE - CHUNK_OVERLAP):
        chunk = tokens[i:i + CHUNK_SIZE]
        decoded = tokenizer.decode(chunk)
        chunks.append(decoded)

    return chunks
