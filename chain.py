import re

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
    ResponseSchema(name="tickers", description="list of tickers mentioned in the article, empty list if none"),
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
    """ Extract structured data from a news article using the langchain API.

    Args:
        llm: langchain API object
        data: news article text
    Returns:
        extracted_data: structured data extracted from the news article
    """

    texts = text_splitter.split_text(data)
    docs = [Document(page_content=t) for t in texts]
    extracted_data = None
    for doc in docs:
        if extracted_data:
            _input = refine_prompt.format_prompt(article=doc.page_content, json_data=extracted_data)
            output = llm(_input.to_messages())
            cleaned_output = clean_model_output(output.content)
            extracted_data = output_parser.parse(cleaned_output)
        else:
            _input = prompt.format_prompt(article=doc.page_content)
            output = llm(_input.to_messages())
            cleaned_output = clean_model_output(output.content)
            extracted_data = output_parser.parse(cleaned_output)

    return extracted_data


def clean_model_output(text: str) -> str:
    """ Clean the output from the langchain API.

    Args:
        text: output from the langchain API
    Returns:
        cleaned_text: cleaned output from the langchain API
    """

    pattern = re.compile('.*?', re.DOTALL)
    matches = pattern.findall(text)[0]

    if matches:
        llm_block = matches[0]
        print(llm_block)
        return llm_block
    else:
        print('No code block found in text.')
        raise ValueError('No code block found in text.')
