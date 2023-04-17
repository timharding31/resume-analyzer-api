from io import BytesIO
from typing import Optional
from PyPDF2 import PdfReader
from fastapi import UploadFile


def get_text_from_pdf(upload_file: Optional[UploadFile] = None) -> str or None:
    if upload_file == None:
        return None
    pdf: PdfReader = PdfReader(BytesIO(upload_file.file.read()))
    return '\n'.join(page.extract_text() for page in pdf.pages)
