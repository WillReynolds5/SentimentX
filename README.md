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
    <p>To run SentimentX, use the following command:</p>
    <code>python sentimentx.py --url https://www.cnbc.com/2023/05/16/elon-musk-cnbc-interview-with-david-faber.html https://www.bbc.com/news/business-57139414</code>
    <p>You can also pass multiple URLs to the --url argument.</p>
    <h2>Sample Output</h2>
    <p>Here is a sample output:</p>
    <pre>
{
    "authors": ["Susan Heavey", "Doina Chiacu", "Andrea Shalal"],
    "date": "2023-05-17T18:12:00.000Z",
    "summary": "President Joe Biden and top U.S. congressional Republican Kevin McCarthy on Wednesday underscored their determination to reach a deal soon to raise the federal government's $31.4 trillion debt ceiling and avoid an economically catastrophic default.",
    "publisher": "Reuters",
    "title": "Biden, McCarthy push forward towards deal on US debt ceiling",
    "tickers": [],
    "sentimentScore": "5",
    "marketImpact": "7"
}
    </pre>
    <h2>Saving Output to CSV</h2>
    <p>You can save the output to a CSV file by passing the --csv flag along with a filename:</p>
    <code>python sentimentx.py --url https://www.cnbc.com/2023/05/16/elon-musk-cnbc-interview-with-david-faber.html --csv output.csv</code>
</body>
</html>
