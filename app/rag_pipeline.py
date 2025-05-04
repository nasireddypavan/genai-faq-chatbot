# app/rag_pipeline.py

from app.pdf_utils import extract_text_from_pdf
from app.embedder import get_embeddings, get_azure_openai_answer
from app.vectordb import create_or_load_faiss, retrieve_similar_chunks
import uuid
import os

TEMP_PDF_DIR = "data/"
INDEX_DIR = "faiss_index/"

def process_pdf_and_answer(pdf_bytes: bytes, query: str) -> str:
    # Save the uploaded PDF temporarily
    session_id = str(uuid.uuid4())
    temp_pdf_path = os.path.join(TEMP_PDF_DIR, f"{session_id}.pdf")
    
    os.makedirs(TEMP_PDF_DIR, exist_ok=True)
    os.makedirs(INDEX_DIR, exist_ok=True)

    with open(temp_pdf_path, "wb") as f:
        f.write(pdf_bytes)

    # 1. Extract and chunk text
    chunks = extract_text_from_pdf(temp_pdf_path)

    # 2. Get embeddings for chunks
    chunk_embeddings = get_embeddings(chunks)

    # 3. Store in FAISS index
    faiss_index, ids = create_or_load_faiss(chunk_embeddings, chunks, session_id)

    # 4. Retrieve top relevant chunks
    top_chunks = retrieve_similar_chunks(query, faiss_index, chunks)

    # 5. Ask GPT using retrieved context
    response = get_azure_openai_answer(query, top_chunks)

    return response
