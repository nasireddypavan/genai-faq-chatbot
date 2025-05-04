# app/embedder.py

import openai
import os
from app.config import (
    AZURE_OPENAI_API_KEY,
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_DEPLOYMENT,
    AZURE_CHAT_DEPLOYMENT,
)

openai.api_key = AZURE_OPENAI_API_KEY
openai.api_type = "azure"
openai.api_base = AZURE_OPENAI_ENDPOINT
openai.api_version = "2023-05-15"  # Check your Azure version

def get_embeddings(texts: list[str]) -> list[list[float]]:
    response = openai.Embedding.create(
        input=texts,
        engine=AZURE_OPENAI_DEPLOYMENT
    )
    return [d["embedding"] for d in response["data"]]


def get_azure_openai_answer(query: str, context_chunks: list[str]) -> str:
    context = "\n\n".join(context_chunks)
    prompt = f"""You are a helpful assistant. Use the following context to answer the question.
    
Context:
{context}

Question: {query}
Answer:"""

    response = openai.ChatCompletion.create(
        engine=AZURE_CHAT_DEPLOYMENT,
        messages=[
            {"role": "system", "content": "You answer questions based on provided documents."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2,
        max_tokens=500
    )

    return response['choices'][0]['message']['content'].strip()
