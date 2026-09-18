import os

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# Define the model
model = ChatOpenAI(
base_url="https://router.huggingface.co/v1",
api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
model="meta-llama/Llama-3.1-8B-Instruct",
temperature=0.1,
)



parser = JsonOutputParser()

template = PromptTemplate(
template='Give me 5 facts about {topic} \n {format_instruction}',
input_variables=['topic'],
partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})
# Iterate through each fact cleanly
for key, fact in result.items():
    print(f"[{key.upper()}] {fact['title']}")
    print(f" -> {fact['description']}\n")