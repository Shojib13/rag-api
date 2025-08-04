import pytesseract
from PIL import Image
import pdfplumber, docx, sqlite3, pandas as pd

def extract_text(path):
    ext = path.lower().split('.')[-1]
    if ext == 'pdf':
        return _extract_pdf(path)
    elif ext == 'docx':
        return _extract_docx(path)
    elif ext == 'txt':
        return open(path, 'r').read().split('\n')
    elif ext in ['jpg', 'png']:
        return [pytesseract.image_to_string(Image.open(path))]
    elif ext == 'csv':
        return [pd.read_csv(path).to_string()]
    elif ext == 'db':
        return _extract_db(path)
    return []

def _extract_pdf(path):
    chunks = []
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                chunks.append(text)
    return chunks

def _extract_docx(path):
    doc = docx.Document(path)
    return [para.text for para in doc.paragraphs if para.text.strip()]

def _extract_db(path):
    conn = sqlite3.connect(path)
    text_data = []
    for table in pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn)['name']:
        df = pd.read_sql(f"SELECT * FROM {table}", conn)
        text_data.append(df.to_string())
    conn.close()
    return text_data
