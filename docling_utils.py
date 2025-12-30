from docling.document_converter import DocumentConverter

converter = DocumentConverter()

def process_with_docling(file_path):
    result = converter.convert(file_path)
    return result.document.export_to_dict()
