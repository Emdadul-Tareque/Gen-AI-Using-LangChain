from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
load_dotenv()


# Gemini model setup
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=1.0)

# Run a simple query
propmt = "write a 5 line poem on bangladesh in bangla"
result = model.invoke(propmt)

print(result.content)




