from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os

load_dotenv()

def generate_cat_name():

    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("API key not found. Please set the 'OPENAI_API_KEY' environment variable.")
    else:
        model = ChatOpenAI(api_key=api_key, model="text-embedding-3-small")

    messages = [
        HumanMessage(content="Voce tem um gatinho filho novo e gostaria de dar um nome legal para ele. Mim de uma lista de 5 possiveis nomes.")
    ]

    nomes = model.invoke(messages)

    return nomes

if __name__ == '__main__':

    nomes = generate_cat_name()
    print(nomes)