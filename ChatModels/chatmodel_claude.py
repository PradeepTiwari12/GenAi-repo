

import os
from dotenv import load_dotenv, find_dotenv
from langchain_anthropic import ChatAnthropic

# Automatically finds and loads .env from parent folders
load_dotenv(find_dotenv())

model = ChatAnthropic(
    model="claude-3-5-haiku-20241022",
    temperature=0
)

result = model.invoke("What is the capital of India")
print(result.content)