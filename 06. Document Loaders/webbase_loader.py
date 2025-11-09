from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

url = "https://www.rokomari.com/book/147520/double-standard"
loader = WebBaseLoader(url) 

docs = loader.load()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

prompt = PromptTemplate(
    template="Generate response acording to instruction \n {instruction} from this text {text}",
    input_variables=["instruction", 'text']

)
parser = StrOutputParser()

chain = prompt | model | parser


response = chain.invoke({"instruction":"Write summary in english about the product in 100 words ","text": docs[0].page_content})

print(response)