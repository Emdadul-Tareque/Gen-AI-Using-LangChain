from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=1.0)

#1st prompt 

template1 = PromptTemplate(
    input_variables=['topic'],
    template="write a detailed report on {topic}"
)

template2 = PromptTemplate(
    input_variables=['report'],
    template="Summarize the following report in concise 5 bullet points:\n{report}"
) 

prompt1 = template1.format(topic="Artificial Intelligence")
response1 = model.invoke(prompt1)

prompt2 = template2.format(report=response1.content)
response2 = model.invoke(prompt2) 

print(response2.content)