from langchain_mistralai import ChatMistralAI
from src.ai_bill.prompt import prompt
from src.ai_bill.output_models import Data
from dotenv import load_dotenv
load_dotenv()

llm = ChatMistralAI(model="mistral-large-latest", temperature=0)

runnable = prompt | llm.with_structured_output(schema=Data)
