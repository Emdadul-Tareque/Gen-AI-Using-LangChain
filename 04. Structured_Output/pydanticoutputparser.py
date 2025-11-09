from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=1.0)

class Person(BaseModel):
    Course: str = Field(description="Name of the person")
    Module: int = Field(description= "Age of the person")
    Feedback: str = Field(description= "Name of city the person belongs to")


parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="Generate the name, age and city of a fiction {place} person \n {format_instruction}",
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}

)

# prompt = template.invoke({'place':'bangladesh'})
# result = model.invoke(prompt)
# final_result = parser.parse(result.content)
# print(final_result)

chain = template | model| parser 

final_result = chain.invoke({'place': 'srilanka'}) 

print(final_result)