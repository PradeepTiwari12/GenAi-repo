import os
import warnings
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

# Suppress library warnings
warnings.filterwarnings("ignore", category=UserWarning)

load_dotenv()

# Initialize the model
model = ChatGoogleGenerativeAI(model="gemini-3.6-flash",temperature=0.7, max_output_tokens=200)

# Option A: Using LangChain's string output parser (Recommended LCEL style)
chain = model | StrOutputParser()
result = chain.invoke("famous five food of rohtas in bihar?")
print(result)

# Option B: Or directly extracting the string content if invoking raw model:
# response = model.invoke("What is the capital of India")
# text = response.content[0]["text"] if isinstance(response.content, list) else response.content
# print(text)