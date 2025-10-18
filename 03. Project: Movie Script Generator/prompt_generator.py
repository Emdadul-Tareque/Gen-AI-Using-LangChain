from langchain_core.prompts import PromptTemplate 


template = PromptTemplate(
    input_variables=["movie_type", "script_length", "language"],
    template="""Write a {script_length} line {movie_type} movie script in {language})""",
    validate_template=True
) 

template.save("movie_script_prompt.json")
