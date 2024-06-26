from langchain_core.messages import AIMessage, SystemMessage
from langchain_core.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

llm = ChatOpenAI(temperature=0.5, model_name="gpt-4o")

# You can modify these!
AI_CONTENT = """
I should use the full pdp url that the tool provides me. 
Always include query parameters
"""
SYSTEM_CONTENT = """
You are a shopping assistant. 
You help humans find the best product given their {input}. 
"""
messages = [
    SystemMessage(content=SYSTEM_CONTENT),
    HumanMessagePromptTemplate.from_template("{input}"),
    AIMessage(content=AI_CONTENT),
]

prompt = ChatPromptTemplate.from_messages(messages)
agent = prompt | llm | StrOutputParser()

agent_executor = agent
