import os
from typing import Literal, Optional
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

load_dotenv()

model = ChatOpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    model="meta-llama/Llama-3.1-8B-Instruct",
    temperature=0.1,  # Lower temperature reduces JSON formatting mistakes
)


class Review(BaseModel):
    key_themes: list[str] = Field(
        default_factory=list,
        description="Key themes discussed in the review",
    )
    summary: str = Field(
        default="",
        description="A brief summary of the review",
    )
    sentiment: Literal["pos", "neg", "neutral"] = Field(
        default="pos",
        description="Overall sentiment: pos, neg, or neutral",
    )
    pros: list[str] = Field(
        default_factory=list,
        description="List of pros mentioned",
    )
    cons: list[str] = Field(
        default_factory=list,
        description="List of cons mentioned",
    )
    name: Optional[str] = Field(
        default=None,
        description="Name of the reviewer",
    )


# Set up the parser and prompt
parser = PydanticOutputParser(pydantic_object=Review)

prompt = PromptTemplate(
    template=(
        "You are an expert data extractor. Extract the review details into JSON format.\n"
        "{format_instructions}\n\n"
        "Review Text:\n{review}\n"
    ),
    input_variables=["review"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | model | parser

review_text = """I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                  
Review by Nitish Singh
"""

result = chain.invoke({"review": review_text})
print(result)