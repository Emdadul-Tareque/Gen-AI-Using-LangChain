from langchain_core.prompts import ChatPromptTemplate


chat_template = ChatPromptTemplate([
     ('system', 'You are a {domain} expert'),
    ('human', 'please explain {topic} in detail.')
])
prompt = chat_template.invoke({"domain": "AI" , "topic": "Langchain"})

print(prompt) 