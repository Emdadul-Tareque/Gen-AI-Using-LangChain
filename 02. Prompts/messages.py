from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    ChatMessage,
)

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv() 

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=1.0) 

messages = [
    SystemMessage(content = "Your are Programmer assistant. Answer concisely."),
    HumanMessage(content = "write a program which can sort a list of numbers in python.")
]

response = model.invoke(messages)
messages.append(AIMessage(content=response.content))
print(messages)