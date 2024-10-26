from src.ai_bill.ai_model import runnable
from src.utils import extract_text_from_pdf

def main():
    file = input("Ingrese el nombre del archivo que desea analizar:"  )
    content= extract_text_from_pdf(file)
    
    output = runnable.invoke({"text": content})
    return output

if __name__ == '__main__':
    result = main()
    print(result.dict())