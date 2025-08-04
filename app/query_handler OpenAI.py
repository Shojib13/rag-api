import base64
from PIL import Image
from io import BytesIO
import openai
from app.vector_store import search

from app.config import OPENAI_API_KEY

print("Loaded OpenAI Key:", OPENAI_API_KEY)


openai.api_key = OPENAI_API_KEY


async def handle_query(question, image_base64=None):
    try:
        # Append OCR text from image if present
        if image_base64 and image_base64.strip().lower() != "string":
            img = Image.open(BytesIO(base64.b64decode(image_base64)))
            question += " " + pytesseract.image_to_string(img)

        # Vector search
        context_docs = search(question)
        if not context_docs:
            return {"error": "No relevant context found in documents."}

        context = "\n".join([doc["text"] for doc in context_docs])
        prompt = f"Answer the question based on the context below:\n\nContext:\n{context}\n\nQuestion: {question}"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        return {
            "context": context,
            "answer": response['choices'][0]['message']['content'],
            "sources": [doc["file_id"] for doc in context_docs]
        }
    except Exception as e:
        return {"error": str(e)}