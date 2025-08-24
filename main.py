from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

load_dotenv()

# Simple Perplexity AI client
llm = ChatOpenAI(
    model="sonar-pro",
    api_key=os.getenv("PERPLEXITY_API_KEY"),
    base_url="https://api.perplexity.ai"
)

# Ask a question
response = llm.invoke("What is the meaning of life?")
print(response.content)