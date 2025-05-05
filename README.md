Sure! Here’s the **full `README.md`** for your GenAI FAQ Chatbot project. You can **copy-paste** this directly into your repository.

---

```markdown
# 💬 GenAI FAQ Chatbot

An intelligent chatbot that answers user questions by understanding the content of uploaded PDF documents using modern GenAI techniques like embeddings, vector databases (FAISS), and GPT-powered language modeling.

---

## 🔍 Overview

This chatbot allows users to upload one or more PDF documents, from which it extracts the content, generates embeddings using Azure OpenAI, and stores these embeddings in a FAISS vector store. When a user submits a query, it performs a similarity search on the vector database to retrieve the most relevant context and sends it along with the query to OpenAI's GPT (or similar LLM) to generate accurate, context-aware answers.

---

## 🧠 Key Features

- 📄 **PDF Upload**: Extracts text content from uploaded PDFs.
- 🧬 **Embeddings**: Generates text embeddings using **Azure OpenAI**.
- 📦 **Vector Store (FAISS)**: Stores and searches embeddings using FAISS for fast retrieval.
- 🗃️ **Context-Aware Responses**: Retrieves relevant content and passes it to GPT to generate precise responses.
- 🌐 **API & UI**: REST API via **FastAPI** and a **Streamlit-based UI** for interaction.
- ☁️ **Deployable**: Designed to be easily deployed on **Azure App Service** with **Azure OpenAI**.

---

## 🏗️ Architecture

```

\[PDF Upload]
↓
\[Text Extraction]
↓
\[Embeddings Generation]
↓
\[FAISS Vector Store]
↓
\[User Query]
↓
\[Similarity Search]
↓
\[Prompt + Retrieved Context]
↓
\[LLM (e.g., GPTo Mini)]
↓
\[Answer]

```

---

## 📁 Project Structure

```

genai-faq-chatbot/
├── app/
│   ├── main.py               # FastAPI backend
│   ├── rag\_pipeline.py       # Core RAG logic (PDF → chunks → embedding → retrieval → answer)
│   ├── pdf\_utils.py          # PDF extraction and text chunking
│   ├── embedder.py           # Embedding generation using Azure OpenAI
│   ├── vectordb.py           # FAISS management
│   └── config.py             # Azure config and env variables
│
├── ui/
│   └── streamlit\_ui.py       # Streamlit frontend UI
│
├── data/                     # Directory for uploaded PDFs
├── faiss\_index/              # FAISS index files
├── requirements.txt
├── start.sh                  # Startup script for FastAPI
├── .env                      # Environment variables for local development
└── README.md                 # This file

````

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/nasireddypavan/genai-faq-chatbot.git
cd genai-faq-chatbot
````

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Set Up Azure OpenAI

Ensure you have the following environment variables set in your Azure environment:

* `AZURE_OPENAI_API_KEY` (Azure API key for OpenAI)
* `AZURE_OPENAI_ENDPOINT` (Azure OpenAI endpoint URL)
* `AZURE_OPENAI_DEPLOYMENT` (Deployment name for embeddings, e.g., `text-embedding-ada-002`)
* `AZURE_CHAT_DEPLOYMENT` (Deployment name for chat completion, e.g., `gpt-35-turbo`)

Alternatively, create a `.env` file with:

```
AZURE_OPENAI_API_KEY=your-key
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
AZURE_OPENAI_DEPLOYMENT=text-embedding-ada-002
AZURE_CHAT_DEPLOYMENT=gpt-35-turbo
```

### 4. Run the App

Start the FastAPI backend server:

```bash
# Optionally set your API key as an environment variable
export $(cat .env | xargs)

# Start backend server
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Run the **Streamlit UI** (optional):

```bash
streamlit run ui/streamlit_ui.py
```

---

## 📦 Dependencies

* **Python 3.8+**
* FastAPI
* Uvicorn
* OpenAI (Azure)
* FAISS
* PyPDF2 (or pdfplumber)
* Tiktoken
* Python-dotenv
* Streamlit
* Requests

---

## ✨ Example Use Case

1. **Upload a PDF**: Upload a company policy document or any other relevant PDF.
2. **Ask a Question**: Ask a question like "What is the leave policy?"
3. **Receive Context-Aware Answer**: The bot retrieves the most relevant section from the PDF and answers based on that context.


## 🔧 Deployment to Azure App Service

1. **Using Docker**:

   * Add a `Dockerfile` in your project root and build the container.
   * Deploy the Docker container to **Azure App Service** using Azure CLI or the Azure portal.

   Example `Dockerfile`:

   ```dockerfile
   FROM python:3.10-slim

   WORKDIR /app
   COPY . /app

   RUN pip install --no-cache-dir -r requirements.txt

   EXPOSE 8000
   CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

2. **Without Docker**:

   * Deploy the FastAPI app directly to **Azure App Service**.
   * Set the **startup command** in Azure to:

     ```bash
     gunicorn app.main:app -k uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
     ```

---

you can try it out here https://genai-faq-chatbot-cxkf2iynnw7qqujinmcw6a.streamlit.app/

