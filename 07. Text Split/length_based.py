from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('ML.pdf')
docs = loader.load()

# print(docs[0])

# text = """
# Artificial intelligence (AI) is technology that enables computers and machines to simulate human learning, comprehension, problem solving, decision making, creativity and autonomy.
# Applications and devices equipped with AI can see and identify objects. They can understand and respond to human language. They can learn from new information and experience. They can make detailed recommendations to users and experts. They can act independently, replacing the need for human intelligence or intervention (a classic example being a self-driving car).
# But in 2024, most AI researchers, practitioners and most AI-related headlines are focused on breakthroughs in generative AI (gen AI), a technology that can create original text, images, video and other content. To fully understand generative AI, it’s important to first understand the technologies on which generative AI tools are built: machine learning (ML) and deep learning.
# """


# splitter = CharacterTextSplitter(
#     chunk_size = 100,
#     chunk_overlap = 0,
#     separator=''
# )

# response = splitter.split_text(text)
# count = 1
# for text in response:
#     print(count, " ", text)
#     count += 1 

# print(response[0])

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator=''
)

response = splitter.split_documents(docs)

# count = 1
# for text in response:
#     print(count, " ", text)
#     count += 1 

print(response[0].page_content)
print(response[0].metadata)