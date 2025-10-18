from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import (AIMessage, HumanMessage)
from dotenv import load_dotenv 

load_dotenv()   
# Gemini model setup
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=1.0)


history = []
# Run a simple query
while True:
    user_input = input("You: ")
    history.append(HumanMessage(content=user_input))
    if user_input.lower() == 'exit':
        print("Exiting the program.")
        break    
    response = model.invoke(history)
    history.append(AIMessage(content=response.content))
    print("AI Response:", response.content)
