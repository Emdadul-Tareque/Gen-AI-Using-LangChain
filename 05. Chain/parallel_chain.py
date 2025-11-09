#import libraries
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

#load key from dotenv file
load_dotenv()

#make llm 
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="text-generation",
    max_new_tokens=250,
    temperature=1.5,
)

#make a model 
model1 = ChatHuggingFace(llm = llm)
model2 = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

template1 = PromptTemplate(
    template= 'take a short note about {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='Make a quiz in 5 questions about this {topic}',
    input_variables=['topic']
)

template3 = PromptTemplate(
    template='Merge the provided notes and quize into a single document \n note -> {note} and quiz -> {quiz}',
    input_variables=['note', 'quiz']

)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'note': template1 | model1 | parser,
    'quiz': template2 | model2 | parser
})

merge_chain = template3 | model2 | parser 

chain = parallel_chain | merge_chain 

result = chain.invoke({'topic' : 'Genetics'})

print(result)

chain.get_graph().print_ascii()