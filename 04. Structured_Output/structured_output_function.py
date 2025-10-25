from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

prompt = """3 Idiots is a 2009 Indian Hindi-language coming-of-age satirical comedy-drama film written, 
edited and directed by Rajkumar Hirani, co-written by Abhijat Joshi and produced by Vidhu Vinod Chopra. 
The film stars Aamir Khan, R. Madhavan and Sharman Joshi in the title roles, while Kareena Kapoor, 
Boman Irani, Mona Singh and Omi Vaidya play supporting roles. Narrated through two parallel timelines, 
one in the present and the other set ten years earlier, the story follows the friendship of three students 
at an Indian engineering college and is a satire about the intrinsic paternalism under the Indian education system.
"""

# Use Pydantic model instead of TypedDict
class MovieInfo(BaseModel):
    title: str = Field(description="Movie title")
    director: str = Field(description="Director of the movie")
    release_year: int = Field(description="Year of release")
    genre: str = Field(description="Genre of the movie")

# Gemini model setup
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=1.0)

# Use structured output with Pydantic model
structured_model = model.with_structured_output(MovieInfo)

# Invoke the model
response = structured_model.invoke(prompt)

print(response)
