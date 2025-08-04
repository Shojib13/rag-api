from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
index = faiss.IndexFlatL2(384)
documents = []

def store_embeddings(text_chunks, file_id):
    embeddings = model.encode(text_chunks)
    index.add(np.array(embeddings).astype('float32'))
    documents.extend([{"text": t, "file_id": file_id} for t in text_chunks])

def search(query):
    embedding = model.encode([query])
    D, I = index.search(np.array(embedding).astype('float32'), 5)
    return [documents[i] for i in I[0]]
