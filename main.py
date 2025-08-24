from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]  # Fixed: added colon for proper type annotation


llm = ChatOpenAI(
    model="sonar-pro",
    api_key=os.getenv("PERPLEXITY_API_KEY"),
    base_url="https://api.perplexity.ai"
)

parser = PydanticOutputParser(pydantic_object=ResearchResponse)
 
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use neccessary tools. 
            Wrap the output in this format and provide no other text\n{format_instructions}
            """,
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

agent = create_tool_calling_agent(
    llm=llm,  # Fixed: lowercase 'llm'
    prompt=prompt,
    tools=[]
)

agent_executor = AgentExecutor(agent=agent, tools=[], verbose=True)
raw_response = agent_executor.invoke({"query": "What is the meaning of friendship and relationship"})
print("Raw Response:")
print(raw_response)
print("\n" + "="*50 + "\n")

# Fix: The output is already a string, not a list with text
structured_response = parser.parse(raw_response.get("output"))

print("Structured Response:")
print(structured_response)