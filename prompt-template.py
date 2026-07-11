## Use Prompt Templates instead of writing multiple times,

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} like I'm a beginner."
)

messages = prompt.invoke({"topic":"Delta Lake"})
