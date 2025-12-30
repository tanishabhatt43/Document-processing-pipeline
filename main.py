import os

def detect_file_type(filename):
    return os.path.splitext(filename)[1].lower()

from fastapi import FastAPI, UploadFile, File
import shutil
import os

from docling_utils import process_with_docling
from ocr_utils import ocr_image
from excel_utils import process_excel

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ext = os.path.splitext(file.filename)[1].lower()

    # Case 1: Docling supported documents
    if ext in [".pdf", ".docx", ".pptx"]:
        output = process_with_docling(file_path)

    # Case 2: Images / scanned files
    elif ext in [".jpg", ".jpeg", ".png"]:
        output = ocr_image(file_path)


    # Case 3: Excel
    elif ext in [".xls", ".xlsx"]:
        output = process_excel(file_path)

    else:
        return {"error": "Unsupported file type"}

    return {
        "filename": file.filename,
        "processed_output": output
    }

