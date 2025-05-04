# genai-faq-chatbot
A GPT-powered FAQ chatbot built with FastAPI and OpenAI. It retrieves the closest matching FAQ and generates a refined response using Generative AI. Deployed on Azure App Service.

# 🧠 GenAI FAQ Chatbot

A GPT-powered FAQ chatbot built with **FastAPI** and **OpenAI**.  
It matches user questions with a list of predefined FAQs and enhances responses using Generative AI.  
Deployed on **Azure App Service**.

---

## 🚀 Demo

🌐 [Live App on Azure](https://your-azure-url-here) *(update once deployed)*  
📽️ Demo video: *optional link*

---

## 📚 Features

- Loads FAQs from a JSON file
- Matches user queries with closest FAQ
- Uses OpenAI GPT-3.5 to enhance the response
- REST API endpoint (`/ask`) for querying
- Deployed on Azure using CI/CD (or manual deploy)

---

## 🧩 Tech Stack

- **Backend:** FastAPI
- **AI Model:** OpenAI (gpt-3.5-turbo)
- **Matching:** Simple keyword search (can be improved with embeddings)
- **Deployment:** Azure App Service
- **Optional:** LangChain for modularity

---

## 🧪 API Usage

### `POST /ask`

```json
Request:
{
  "question": "How do I reset my password?"
}

Response:
{
  "response": "To reset your password, click on 'Forgot Password' on the login screen..."
}
