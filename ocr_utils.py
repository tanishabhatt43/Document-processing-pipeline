import pytesseract
from PIL import Image

TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def ocr_image(image_path):
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)

    return {
        "type": "ocr_text",
        "content": text.strip()
    }
