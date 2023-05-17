<!DOCTYPE html>
<html>
<body>
    <h1>SentimentX💰📈🤖</h1>
    <p>SentimentX is a command-line application designed to extract structured data from financial news sources. It retrieves an article from the provided URL(s), extracts its text, and then applies sentiment analysis to the text. The sentiment score, along with other useful article information, is returned in a JSON format.</p>
    <h2>Setup</h2>
    <p>To setup SentimentX, install the requirements by running:</p>
    <code>pip install -r requirements.txt</code>
    <h3>Setting up OpenAI API Key</h3>
    <p>To use SentimentX, you'll need to have an OpenAI API key. Once you have your key, create a new file in the project root directory called <code>.env</code>, and add the following line:</p>
    <code>OPENAI_API_KEY=sk-1sdf2s...</code>
    <p>Replace <code>sk-1sdf2s...</code> with your actual OpenAI API key.</p>
    <h2>Running SentimentX</h2>
    <p>To run SentimentX, use the following command (to pass multiple urls, separate by space):</p>
    <code>python sentimentx.py --url https://www.cnbc.com/2023/05/17/google-to-use-new-ai-models-for-ads-and-to-help-youtube-creators.html https://www.cnbc.com/2023/05/17/amazons-alexa-head-defends-companys-work-on-ai-amid-chatgpt-boom.html</code>
    <p>You can also pass multiple URLs to the --url argument.</p>
    <h2>Sample Output</h2>
    <p>Here is a sample output:</p>
    <pre>
    {
      "authors": ["Jennifer Elias"],
      "date": "2023-05-17T16:30:00.000Z",
      "summary": "Google has approved several ad-related artificial intelligence projects to help advertisers and YouTube creators, internal documents show. The company also plans to automate some customer service for its products using new AI models. Google is working on its own internal Stable Diffusion-like product for image creation.",
      "publisher": "CNBC",
      "title": "Google plans to use new A.I. models for ads and to help YouTube creators, sources say",
      "tickers": ["GOOGL"],
      "sentimentScore": "6",
      "marketImpact": "5"
    }
    </pre>
    <h2>Saving Output to CSV</h2>
    <p>You can save the output to a CSV file by passing the --csv flag along with a filename:</p>
    <code>python sentimentx.py --url https://www.cnbc.com/2023/05/16/elon-musk-cnbc-interview-with-david-faber.html --csv output.csv</code>
</body>
</html>
