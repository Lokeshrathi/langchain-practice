## ChatOpenAI - How to communicate with an LLM

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4.1-mini")

response = llm.invoke("Explain Delta Lake")

print(response.content)
