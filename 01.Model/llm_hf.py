#import libraries
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

#load key from dotenv file
load_dotenv()

#make llm 
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1",
    task="text-generation",
    max_new_tokens=250,
    temperature=1.5,
    # model_kwargs={"provider": "auto"}
)

#make a model 
model = ChatHuggingFace(llm = llm)
propmt = "write a 5 line poem on bangladesh in bangla"
result = model.invoke(propmt)
print(result.content) 