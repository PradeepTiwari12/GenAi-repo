import os
from langchain_community.document_loaders import WebBaseLoader





url = 'https://gemini.google.com/app/e17baa16884d0271?hl=en-GB'
loader = WebBaseLoader(url)

docs = loader.load()


print(len(docs))
print(docs[0].page_content)