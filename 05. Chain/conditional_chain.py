from langchain_google_genai import ChatGoogleGenerativeAI 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv 
load_dotenv() 

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash') 
parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment : Literal['positve', 'negative']  = Field(description='Give the sentiment of the feedback')

parser1 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template= 'classify the sentiment following the feedback text into positve or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser1.get_format_instructions()}
) 

classifier_chain = prompt1 | model | parser1 


prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive response \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative response \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x : x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x : x.sentiment == 'negative', prompt3 | model | parser ),
    RunnableLambda( lambda x : "didn't find sentiment" )
)

chain = classifier_chain | branch_chain 

result = chain.invoke ({'feedback': 'This is a terrable phone'})

print(result)
  
                                            