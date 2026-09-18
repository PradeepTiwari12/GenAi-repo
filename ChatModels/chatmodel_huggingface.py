import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    model="meta-llama/Llama-3.1-8B-Instruct",
    temperature=0.1,
)

response = model.invoke("name ten female pornstar ")
print(response.content)