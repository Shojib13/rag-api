from pathlib import Path

readme_text = """
# 🔍 Gemini RAG API – Retrieval-Augmented Generation with FastAPI

This project implements a smart **Retrieval-Augmented Generation (RAG)** API using **Google Gemini 2.5 Pro**, **FastAPI**, and **FAISS**. It accepts documents like PDFs, Word files, text, or images, then answers natural language questions using semantic search and Gemini.

---

## 🚀 Features

- 📄 Supports PDF, DOCX, TXT, CSV, DB, JPG/PNG with OCR
- 🔎 Semantic search using SentenceTransformers + FAISS
- 🧠 Uses **Gemini 2.5 Pro** via `google-generativeai`
- 🖼️ OCR with pytesseract for image-based input
- ⚡ FastAPI-powered REST endpoints with Swagger UI
- 💡 Simple and extensible codebase

---

## 📁 Project Structure

rag-api/
├── app/
│ ├── main.py # FastAPI app
│ ├── ingestion.py # Document parsing
│ ├── query_handler.py # Gemini + FAISS logic
│ ├── utils.py # OCR, extraction tools
│ ├── vector_store.py # FAISS index mgmt
│ └── config.py # .env loader
├── data/ # Uploaded/parsed files
├── .env.example # Safe API key template
├── .gitignore
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### 1. Clone and enter the project


git clone https://github.com/your-username/rag-api.git
cd rag-api

2. Create and activate a virtual environment



python -m venv venv
venv\\Scripts\\activate   # On Windows

3. Install dependencies

pip install -r requirements.txt
4. Configure environment variables
Create a .env file based on the example:



cp .env.example .env
Then add your Gemini API key:



GEMINI_API_KEY=your-api-key-here
▶️ Run the App
bash


uvicorn app.main:app --reload
Then visit http://127.0.0.1:8000/docs

📮 API Endpoints
/upload - Upload document
Method: POST

Form: file (PDF, DOCX, TXT, etc.)

Returns: file_id

/query - Ask a question
Method: POST

Form:

question (string)

image_base64 (optional)

Returns: answer, sources, and context

🧪 Sample Questions
"What does this PDF say about payment?"

"Summarize the contract in this image."

"What are the dates listed in the document?"

🛠 Technologies
FastAPI

Google Gemini 2.5 Pro (google-generativeai)

SentenceTransformers (MiniLM)

FAISS for vector search

pytesseract for OCR

🛡️ License
MIT — use it freely and responsibly.
