import pdfplumber
from docx import Document

def extract_text_from_resume(file_path):
    text = ""

    if file_path.lower().endswith('.pdf'):
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"

    elif file_path.lower().endswith('.docx'):
        doc = Document(file_path)
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"

    else:
        text = "Unsupported file format."

    return text.strip()