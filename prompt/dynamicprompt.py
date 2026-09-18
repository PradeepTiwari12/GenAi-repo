import os
import streamlit as st
from dotenv import find_dotenv, load_dotenv
from langchain_core.prompts import load_prompt
from langchain_openai import ChatOpenAI

# Load .env file automatically even if it is in the root directory
load_dotenv(find_dotenv())

st.header("Research Tool")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis",
    ],
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"],
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)",
    ],
)

# Connect to Hugging Face Serverless Router
model = ChatOpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    model="meta-llama/Llama-3.1-8B-Instruct",
    temperature=0.3,
)

template = load_prompt("template.json")

if st.button("Summarize"):
    with st.spinner("Generating summary via Hugging Face..."):
        chain = template | model
        result = chain.invoke(
            {
                "paper_input": paper_input,
                "style_input": style_input,
                "length_input": length_input,
            }
        )
        st.write(result.content)