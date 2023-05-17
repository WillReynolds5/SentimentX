import os

import argparse
import requests
from typing import Any
from langchain import OpenAI
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from bs4 import BeautifulSoup

from chain import extract_data_chain

load_dotenv()

def remove_css_and_outer_html(html):
    # Parse the HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Remove all <style> tags
    for style in soup.find_all('style'):
        style.decompose()

    # Extract only the body contents
    body_contents = str(soup.body)

    return body_contents

class SentimentX:

    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set")

        self.llm = ChatOpenAI()

    def extract_signal(self, data: str) -> Any:
        # placeholder for the actual function implementation
        output = extract_data_chain(self.llm, data)
        return output

    def get_article_content(self, url: str) -> str:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.get_text(strip=True)


    def run(self, url: str, csv: str = None):
        content = self.get_article_content(url)
        data = self.extract_signal(content)
        # save the json to csv file
        if csv:
            with open(csv, 'w') as f:
                f.write(data)

        return data

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='SentimentX - News Article Sentiment Analysis.')
    parser.add_argument('--url', type=str, required=True, help='URL to the news article.')
    parser.add_argument('--csv', type=str, required=False, help='Saves the json to a csv file instead of printing to stdout.')
    args = parser.parse_args()

    sentimentx = SentimentX()
    sentimentx.run(args.url)


# python sentimentx.py --url https://www.cnbc.com/2023/05/16/elon-musk-cnbc-interview-with-david-faber.html
