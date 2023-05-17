from langchain.text_splitter import TokenTextSplitter
from langchain.docstore.document import Document
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate

from typing import Any

text_splitter = TokenTextSplitter()

response_schemas = [
    ResponseSchema(name="authors", description="list of authors of the article"),
    ResponseSchema(name="date", description="date published, in ISO format"),
    ResponseSchema(name="summary", description="summary of the article"),
    ResponseSchema(name="publisher", description="organization that published the article"),
    ResponseSchema(name="title", description="title of the article"),
    ResponseSchema(name="tickers", description="list of tickers mentioned in the article"),
    ResponseSchema(name="sentimentScore", description="rate the sentiment of the article (1-10) 1 is terrible negative article and 10 is extremely positive article"),
    ResponseSchema(name="marketImpact", description="rate the market impact score of the article (1-10) 1 is no probable impact and 10 is extremely impactful"),
]

output_parser = StructuredOutputParser.from_response_schemas(response_schemas)


prompt = ChatPromptTemplate(
    messages=[
        HumanMessagePromptTemplate.from_template("Extract the structured data from the news article in the context of a financial analyst.\n{format_instructions}\n{article}")
    ],
    input_variables=["article"],
    partial_variables={"format_instructions": output_parser.get_format_instructions()}
)

# takes the existing json data and the new article text and refines the json data
refine_prompt = ChatPromptTemplate(
    messages=[
        HumanMessagePromptTemplate.from_template("Refine the structured data from the news article in the context of a financial analyst.\n{json_data}\n{article}")
    ],
    input_variables=["article", "json_data"]
)


def extract_data_chain(llm: Any, data: str) -> Any:
    texts = text_splitter.split_text(data)
    docs = [Document(page_content=t) for t in texts]


    extracted_data = None
    for doc in docs:
        if extracted_data:
            _input = refine_prompt.format_prompt(article=doc.page_content, json_data=extracted_data)
            output = llm(_input.to_messages())
            extracted_data = output_parser.parse(output.content)
        else:
            _input = prompt.format_prompt(article=doc.page_content)
            output = llm(_input.to_messages())
            print(output.content)
            extracted_data = output_parser.parse(output.content)

    return extracted_data
