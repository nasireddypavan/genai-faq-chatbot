# app/main.py

from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from app.rag_pipeline import process_pdf_and_answer

app = FastAPI()

# Allow local frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ask")
async def ask_question(
    pdf_file: UploadFile = File(...),
    query: str = Form(...)
):
    contents = await pdf_file.read()
    response = process_pdf_and_answer(contents, query)
    return {"answer": response}
