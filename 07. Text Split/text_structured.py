from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('ML.pdf')

docs = loader.load()
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300,
    chunk_overlap=0,
)

response = splitter.split_documents(docs)

print(len(response))

for text in response:
    print(text.page_content, "\n_____________________________________________")


