from openai import OpenAI
import feedparser
from requests import get

client = OpenAI()

# openai_key ='API Key from OpenAI'
# client = OpenAI(api_key=openai_key)

def scrape_feed(url):
    rss_feed = get(url).text
    feed = feedparser.parse(rss_feed)
    text = ''
    for post in feed['entries']:
        text = f'{text} {post["title"]} - {post["description"]}'
    
    return text

def ai(query, text):
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": f"provide answer from this document {text}"},
        {"role": "user", "content": query}
    ]
    )
    response = completion.choices[0].message.content
    return response

url = 'https://feeds.arstechnica.com/arstechnica/index'
query = 'what is going on in the news'

result_text = scrape_feed(url)
result_ai = ai(query, result_text)

print(result_ai)