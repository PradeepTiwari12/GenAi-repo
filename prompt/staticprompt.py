import os
import streamlit as st
from dotenv import find_dotenv, load_dotenv
from langchain_core.prompts import load_prompt
from langchain_openai import ChatOpenAI

# Load .env file automatically even if it is in the root directory
load_dotenv(find_dotenv())

st.header("Research Tool")

paper_input = st.text_input("Enter your prompt")

# Connect to Hugging Face Serverless Router
model = ChatOpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    model="meta-llama/Llama-3.1-8B-Instruct",
    temperature=0.3,
)

template = load_prompt("template.json")

if st.button("Summarize"):
   
        result = model.invoke(
         paper_input
        )
        st.write(result.content)