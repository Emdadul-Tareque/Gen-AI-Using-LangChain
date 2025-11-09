from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

prompt = PromptTemplate(
    template="write the summary of this poem in 30 words \n {poem}",
    input_variables=["poem"]

)
parser = StrOutputParser()

loader = TextLoader('AI.txt')
docs = loader.load()

chain = prompt | model | parser


response = chain.invoke({"poem": docs[0].page_content})

print(response)