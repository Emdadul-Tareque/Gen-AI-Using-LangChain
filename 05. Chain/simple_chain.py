from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.output_parsers.structured import StructuredOutputParser
from langchain.output_parsers import ResponseSchema
from dotenv import load_dotenv 
load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

# template = PromptTemplate(
#     template= 'write a paragraph about {topic} in 50 words',
#     input_variables=['topic']
# )

# parser = StrOutputParser()

# chain = template | model | parser 

# result = chain.invoke({'topic': 'cricket'})

# print (result)

#schema 

schema = [
    ResponseSchema(name='fact_01', description='Fact_01 about the topic'),
    ResponseSchema(name='fact_02', description='Fact_02 about the topic'),
    ResponseSchema(name='fact_02', description='Fact_03 about the topic')
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Write about the {topic} in 20 words  in the following format: \n {format_instruction}',
    input_variables=['topic'],
    partial_variables= {'format_instruction': parser.get_format_instructions()}

)

chain = template | model | parser

result = chain.invoke({'topic': 'AI'})
# print(result)

chain.get_graph().print_ascii()