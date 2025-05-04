# ui/streamlit_ui.py

import streamlit as st
import requests
from io import BytesIO

# FastAPI server URL
API_URL = "https://genai-faqbot.azurewebsites.net/ask"  # Change this when deployed

def upload_pdf():
    st.title("GenAI FAQ Chatbot")

    # Upload PDF
    uploaded_pdf = st.file_uploader("Upload PDF", type="pdf")

    if uploaded_pdf:
        # Convert PDF to byte content
        pdf_bytes = uploaded_pdf.read()
        
        # User input for query
        query = st.text_input("Ask your question:")
        
        if query:
            # Call backend API with PDF and query
            response = requests.post(
                API_URL,
                files={"pdf_file": ("uploaded.pdf", pdf_bytes, "application/pdf")},
                data={"query": query},
            )

            if response.status_code == 200:
                st.write("Answer:", response.json().get("answer"))
            else:
                st.error("Error: " + response.json().get("detail", "Unknown error"))

if __name__ == "__main__":
    upload_pdf()
