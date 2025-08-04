import os
import uuid
from app.utils import extract_text
from app.vector_store import store_embeddings

async def ingest_file(file):
    file_id = str(uuid.uuid4())
    path = f"data/{file_id}_{file.filename}"
    with open(path, "wb") as f:
        f.write(await file.read())
    text_chunks = extract_text(path)
    store_embeddings(text_chunks, file_id)
    return file_id
