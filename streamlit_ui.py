# app/streamlit_app.py  
import streamlit as st  
import requests  
  
API_URL = "http://localhost:8000"  # Update this to your FastAPI endpoint if hosted elsewhere  
  
def upload_file(file):  
    # Function to upload the file to the FastAPI backend  
    response = requests.post(f"{API_URL}/upload/", files={"file": file})  
    return response.json()  
  
def query_document(question):  
    # Function to query the document in the FastAPI backend  
    response = requests.post(f"{API_URL}/query/", json={"query": question})  
    return response.json()  
  
def main():  
    st.title("Document QA Bot")  
    st.write("Upload a document and ask a question.")  
  
    uploaded_file = st.file_uploader("Choose a document", type=["txt", "pdf", "docx"])  
      
    if uploaded_file is not None:  
        # Upload the document to the FastAPI backend  
        upload_response = upload_file(uploaded_file)  
        st.success(upload_response['message'])  
  
        question = st.text_input("Enter your question:")  
          
        if st.button("Get Answer"):  
            if question:  
                # Query the document using the provided question  
                query_response = query_document(question)  
                st.write("**Results:**")  
                for result in query_response['results']:  
                    st.write(result)  # Display each result from the query  
            else:  
                st.warning("Please enter a question.")  
  
if __name__ == "__main__":  
    main()  