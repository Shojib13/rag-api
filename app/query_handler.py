from transformers import pipeline
from app.vector_store import search
from PIL import Image
from io import BytesIO
import base64
import pytesseract

# Load HuggingFace LLM
generator = pipeline("text-generation", model="google/flan-t5-base")


async def handle_query(question, image_base64=None):
    try:
        if image_base64 and image_base64.strip().lower() != "string":
            img = Image.open(BytesIO(base64.b64decode(image_base64)))
            question += " " + pytesseract.image_to_string(img)

        context_docs = search(question)
        if not context_docs:
            return {"error": "No relevant context found in documents."}

        context = "\n".join([doc["text"] for doc in context_docs])
        prompt = f"Context:\n{context}\n\nQuestion: {question}\n\nAnswer:"


        result = generator(prompt, max_length=512, do_sample=True, temperature=0.7)[0]["generated_text"]

        return {
            "context": context,
            "answer": result.strip(),
            "sources": [doc["file_id"] for doc in context_docs]
        }
    except Exception as e:
        return {"error": str(e)}
