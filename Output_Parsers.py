from dotenv import load_dotenv

# Wrapper for OpenAI chat models.
from langchain_openai import ChatOpenAI

# Creates reusable prompt templates.
from langchain_core.prompts import ChatPromptTemplate

# Converts the model output into a plain string.
from langchain_core.output_parsers import StrOutputParser

# Parses the output into a Pydantic model.
from langchain_core.output_parsers import PydanticOutputParser

# Base class for creating structured response models.
from pydantic import BaseModel, Field

# Load environment variables from the .env file.
load_dotenv()

# Initialize the language model.
llm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0.1
)

# ---------------------------------------------------------------------
# Example 1 - String Output Parser
# ---------------------------------------------------------------------

prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in one paragraph."
)

# Create a chain with a string output parser.
chain = (
    prompt
    | llm
    | StrOutputParser()
)

response = chain.invoke(
    {
        "topic": "Apache Spark"
    }
)

print("\n===== String Output =====\n")
print(response)

# Define the expected response structure.
class Technology(BaseModel):
    name: str = Field(description="Technology name")
    category: str = Field(description="Technology category")
    description: str = Field(description="Short description")
    advantages: list[str] = Field(description="List of advantages")


# Create a parser for the Pydantic model.
parser = PydanticOutputParser(pydantic_object=Technology)

# Create a prompt with format instructions.
prompt = ChatPromptTemplate.from_template(
    """
Provide information about {technology}.

{format_instructions}
"""
)

# Create the chain.
chain = (
    prompt
    | llm
    | parser
)

response = chain.invoke(
    {
        "technology": "Apache Spark",
        "format_instructions": parser.get_format_instructions()
    }
)

print("\n===== Structured Output =====\n")
print(response)

print("\nTechnology Name:")
print(response.name)

print("\nCategory:")
print(response.category)

print("\nDescription:")
print(response.description)

print("\nAdvantages:")
for advantage in response.advantages:
    print(f"- {advantage}")


# ---------------------------------------------------------------------
# Example 3 - Another Structured Example
# ---------------------------------------------------------------------

response = chain.invoke(
    {
        "technology": "Delta Lake",
        "format_instructions": parser.get_format_instructions()
    }
)

print("\n===== Delta Lake =====\n")
print(response)
