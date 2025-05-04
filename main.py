# app/main.py  
from fastapi import FastAPI, UploadFile, File  
from fastapi.responses import JSONResponse  
import os  
import numpy as np  
from langchain.embeddings import OpenAIEmbeddings  
from langchain.vectorstores import FAISS  
from langchain.document_loaders import TextLoader  
from langchain.text_splitter import RecursiveCharacterTextSplitter  
import uvicorn

# Initialize the FastAPI app  
app = FastAPI()  
  
# Set Azure OpenAI configuration  
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")  
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")  
AZURE_OPENAI_MODEL_NAME = "gpt-35-turbo"  
  
# Initialize embeddings model  
embeddings_model = OpenAIEmbeddings(  
    openai_api_key=AZURE_OPENAI_API_KEY,  
    model=AZURE_OPENAI_MODEL_NAME  
)  
  
# Initialize FAISS index  
faiss_index = FAISS(embedding_function=embeddings_model)  
  
@app.post("/upload/")  
async def upload_file(file: UploadFile = File(...)):  
    contents = await file.read()  
    document_text = contents.decode("utf-8")  # Assuming the uploaded file is a text file  
  
    # Split and embed the document  
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)  
    documents = text_splitter.split_text(document_text)  
      
    # Store vectors in FAISS  
    embeddings = embeddings_model.embed_documents(documents)  
    faiss_index.add_texts(documents, embeddings)  
  
    return JSONResponse(content={"message": "File uploaded and processed successfully."})  
  
@app.post("/query/")  
async def query_document(query: str):  
    # Perform the query on the FAISS index  
    results = faiss_index.similarity_search(query)  
    return JSONResponse(content={"results": results})  
  
if __name__ == "__main__":    
    uvicorn.run(app, host="0.0.0.0", port=8000)  