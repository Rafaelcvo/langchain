from langchain_community.llms import Ollama

llm = Ollama(model="llama3")
resp = llm.invoke("A biblioteca do llama3 foi treinado ate que ano?")

print(resp)