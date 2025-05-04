# app/vectordb.py

import faiss
import numpy as np
import os
import pickle

INDEX_DIR = "faiss_index/"

def create_or_load_faiss(embeddings: list[list[float]], chunks: list[str], session_id: str):
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)

    # Save index and metadata
    index_file = os.path.join(INDEX_DIR, f"{session_id}.index")
    meta_file = os.path.join(INDEX_DIR, f"{session_id}_meta.pkl")

    index.add(np.array(embeddings).astype("float32"))

    with open(meta_file, "wb") as f:
        pickle.dump(chunks, f)

    faiss.write_index(index, index_file)

    return index, chunks


def retrieve_similar_chunks(query: str, index, chunks: list[str], top_k: int = 4):
    from app.embedder import get_embeddings

    query_embedding = get_embeddings([query])[0]
    query_vector = np.array([query_embedding]).astype("float32")

    D, I = index.search(query_vector, top_k)
    return [chunks[i] for i in I[0] if i < len(chunks)]
