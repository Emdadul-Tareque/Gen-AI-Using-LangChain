from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=1.0)
# Define the output parser
output_parser = StrOutputParser()

template1 = PromptTemplate(
    input_variables=['topic'],
    template="write a detailed report on {topic}"
)

template2 = PromptTemplate(
    input_variables=['report'],
    template="Summarize the following report in 5 lines:\n{report}"
) 

chain = template1| model| output_parser | template2 | model | output_parser

response = chain.invoke({'topic': 'Climate Change'})

print(response)