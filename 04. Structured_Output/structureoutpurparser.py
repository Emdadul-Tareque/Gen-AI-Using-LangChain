# StructuredOutputParser & ResponseSchema
from langchain.output_parsers.structured import StructuredOutputParser
from langchain.output_parsers import ResponseSchema

# Google Gemini LLM
from langchain_google_genai import ChatGoogleGenerativeAI

# PromptTemplate
from langchain.prompts import PromptTemplate

#Load environment variables
from dotenv import load_dotenv

load_dotenv() 

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=1.0)

schema = [
    ResponseSchema(name="fact_1", description="Fact 01 about the topic"),
    ResponseSchema(name="fact_2", description="Fact 02 about the topic"),
    ResponseSchema(name="fact_3", description="Fact 03 about the topic"),
]

parser = StructuredOutputParser.from_response_schemas(schema)
template = PromptTemplate(
    input_variables=["topic"],
    template="Provide three interesting facts about {topic} in the following format:\n{format_instructions}",
    partial_variables={"format_instructions": parser.get_format_instructions()}
)
# prompt = template.format_prompt(topic="Bangladesh")
# response = model.invoke(prompt)
# result = parser.parse(response.content)
# print(result)

chain = template | model | parser
response = chain.invoke({"topic":"Bangladesh"})
print(response)