from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

loader = PyPDFLoader("ML.pdf")
docs = loader.load()
content = docs[0].page_content

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
prompt = PromptTemplate(
    template='Write summary of this pdf in 30 words \n {outline}',
    input_variables=['outline']
)
parser = StrOutputParser()

chain = prompt | model | parser

response = chain.invoke({'outline': content})

print(response)