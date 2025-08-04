from fastapi import FastAPI, UploadFile, File, Form
from app.ingestion import ingest_file
from app.query_handler import handle_query
from typing import Optional
import base64

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_id = await ingest_file(file)
    return {"file_id": file_id}

@app.post("/query")
async def query(question: str = Form(...), image_base64: Optional[str] = Form(None)):
    return await handle_query(question, image_base64)


