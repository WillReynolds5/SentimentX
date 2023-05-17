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
    [
      {
        "authors": "Jennifer Elias",
        "date": "2023-05-17T16:30:00-0400",
        "summary": "Google plans to use generative AI, fueled by large language models (LLMs), to automate advertising and ad-supported consumer services. The company also plans to automate some customer service for its products using new AI models. Google is working on its own internal Stable Diffusion-like product for image creation.",
        "publisher": "CNBC",
        "title": "Google plans to use new A.I. models for ads and to help YouTube creators",
        "tickers": ["GOOGL"],
        "sentimentScore": "5",
        "marketImpact": "7",
        "url": "https://www.cnbc.com/2023/05/17/google-to-use-new-ai-models-for-ads-and-to-help-youtube-creators.html"
      },
      {
        "authors": ["Annie Palmer"],
        "date": "2023-05-17T10:16:00Z",
        "summary": "Rohit Prasad, Senior VP and Head Scientist for Alexa at Amazon, states that the company will be a major player in generative AI. The company has already sold over 500 million Alexa-powered devices worldwide. Prasad claims that Alexa is at the forefront of AI and is an instantly available personal AI that people can communicate with by voice. Amazon is working on making Alexa more conversational and intelligent by creating a new version of its large language model, Alexa Teacher Model. Amazon may also add AI-like features to Alexa in entertainment and storytelling.",
        "publisher": "CNBC",
        "title": "Amazon's Alexa head says company is 'at the forefront of A.I.' as chatbots explode",
        "tickers": ["AMZN"],
        "sentimentScore": "8",
        "marketImpact": "6",
        "url": "https://www.cnbc.com/2023/05/17/amazons-alexa-head-defends-companys-work-on-ai-amid-chatgpt-boom.html"
      }
    ]
    </pre>
    <h2>Saving Output to CSV</h2>
    <p>You can save the output to a CSV file by passing the --csv flag along with a filename:</p>
    <code>python sentimentx.py --url https://www.cnbc.com/2023/05/16/elon-musk-cnbc-interview-with-david-faber.html --csv output.csv</code>
</body>
</html>
