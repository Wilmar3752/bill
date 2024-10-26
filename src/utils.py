# Function to load and extract text from a PDF file using PyPDFLoader
from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path):
    try:
        return PyPDFLoader(file_path)
    except Exception as e:
        print(f"Error loading PDF: {e}")
        return None

def extract_text_from_pdf(file_path):
    # Load the PDF document
    loader = load_pdf(file_path)

    doc = loader.load()
    content = doc[0].page_content
    return content

