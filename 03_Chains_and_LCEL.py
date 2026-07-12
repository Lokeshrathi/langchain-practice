from dotenv import load_dotenv

# Wrapper for OpenAI chat models.
from langchain_openai import ChatOpenAI

# Creates reusable prompt templates with variables.
from langchain_core.prompts import ChatPromptTemplate

# Converts the model output into a plain string.
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from the .env file.
load_dotenv()

# Initialize the language model.
llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

# Create a prompt template.
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple language."
)

# Create an LCEL chain by connecting the components.
chain = (
    prompt
    | llm
    | StrOutputParser()
)

# Execute the chain with the input variables.
response = chain.invoke(
    {
        "topic": "Apache Spark"
    }
)

print(response)
