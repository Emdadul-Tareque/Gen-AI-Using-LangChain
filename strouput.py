from langchain.output_parsers import StructuredOutputParser, ResponseSchema

# Step 1: Define the output schema
response_schemas = [
    ResponseSchema(name="answer", description="The answer to the user's question"),
    ResponseSchema(name="source", description="The source used to answer the question")
]

# Step 2: Create a StructuredOutputParser from the schemas
parser = StructuredOutputParser.from_response_schemas(response_schemas)

# Step 3: Example text that the parser will process
model_output = """
{
    "answer": "Python is a programming language.",
    "source": "https://www.python.org/"
}
"""

# Step 4: Parse the text
parsed_output = parser.parse(model_output)

# Step 5: Print the parsed output
print(parsed_output)
