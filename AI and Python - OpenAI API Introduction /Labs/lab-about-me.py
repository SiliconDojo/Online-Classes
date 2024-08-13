from openai import OpenAI
from requests import get
import os

client = OpenAI()

nationality = get('http://ip-api.com/json/').json() #Geo Data from IP Address API
nationality = nationality['country']

os.system('clear') #Windows = 'cls'

while True:
    query = input('Question: ')
    os.system('clear')
    completion = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {"role": "system", "content": "You Provide Answers to Question."},
        {"role": "user", "content": f"I am from {nationality}"},
        {"role": "user", "content": "Answer in 10 words or less"},
        {"role": "user", "content": query}
    ]
    )
    print(query)
    print(completion.choices[0].message.content)