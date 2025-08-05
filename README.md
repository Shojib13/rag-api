# 🔍 Gemini RAG API – Retrieval-Augmented Generation with FastAPI

This project implements a smart **Retrieval-Augmented Generation (RAG)** API using **Google Gemini 2.5 Pro**, **FastAPI**, and **FAISS**. It accepts documents like PDFs, Word files, text, or images, then answers natural language questions using semantic search and Gemini.

---

## 🚀 Features

- 📄 Supports PDF, DOCX, TXT, CSV, DB, JPG/PNG with OCR
- 🔎 Semantic search using SentenceTransformers + FAISS
- 🧠 Uses Gemini 2.5 Pro via `google-generativeai`
- 🖼️ OCR with `pytesseract` for image-based input
- ⚡ FastAPI-powered REST endpoints with Swagger UI
- 💡 Simple and extensible codebase

---

## ⚙️ Setup Instructions

### 1. Clone and enter the project

```bash
git clone https://github.com/your-username/rag-api.git
cd rag-api
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file based on the example:

```bash
cp .env.example .env
```

Add your Gemini API key:

```env
GEMINI_API_KEY=your-api-key-here
```

---

## ▶️ Run the App

```bash
uvicorn app.main:app --reload
```

Then open your browser to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 📮 API Endpoints

### `/upload` – Upload document

- Method: `POST`
- Form: file (`PDF`, `DOCX`, `TXT`, etc.)
- Returns: `file_id`

### `/query` – Ask a question

- Method: `POST`
- Form:
  - `question` (string)
  - `image_base64` (optional)
- Returns: `answer`, `sources`, and `context`

---

## 🧪 Sample Questions

- "What does this PDF say about payment?"
- "Summarize the contract in this image."
- "What are the dates listed in the document?"

---

## 🛠 Technologies

- FastAPI
- Google Gemini 2.5 Pro (`google-generativeai`)
- SentenceTransformers (`MiniLM`)
- FAISS
- pytesseract (OCR)

---

## 🛡️ License

MIT — use it freely and responsibly.
