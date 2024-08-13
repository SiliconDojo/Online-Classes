from openai import OpenAI
import feedparser
from bs4 import BeautifulSoup
from requests import get

client = OpenAI()

# openai_key ='API Key from OpenAI'
# client = OpenAI(api_key=openai_key)

def build_list(url):
    rss_feed = get(url).text
    feed = feedparser.parse(rss_feed)

    url_list = []
    for post in feed['entries']:
        url_list.append(post['link'])

    return url_list

def scrape(url):
    page = get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    post = soup.find_all('p')
    text =''
    for line in post: #Create a string without HTML tags
        text = f'{text} {line.text}'
    return text

def ai(query):
    completion_post = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a Blogger."},
        {"role": "user", "content": f"Write a 100 word blog post on -- {query}"},
        {"role": "user", "content": f"Do not mention author"},
        {"role": "user", "content": f"Do not mention when post was written"},
    ]
    )
    response_post = completion_post.choices[0].message.content

    completion_title = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a Blogger."},
        {"role": "user", "content": f"Create a Title for a blog post about -- {response_post}"},
    ]
    )
    response_title = completion_title.choices[0].message.content
    
    return response_title, response_post

url = 'https://feeds.arstechnica.com/arstechnica/index'

url_list = build_list(url)

for page in url_list[:5]: #[:5] limits the loop to 5 iterations
    response_bs = scrape(page)
    response_ai = ai(response_bs)

    print(f'{response_ai[0]}\n {response_ai[1]}')

    with open('auto-blog.html', 'a') as file:
        file.write(f'<h1>{response_ai[0]}</h1>')
        file.write(f'<p>{response_ai[1]}<p>')