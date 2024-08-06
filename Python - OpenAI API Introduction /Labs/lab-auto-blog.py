from openai import OpenAI
import os

client = OpenAI()


os.system('clear') #Windows = 'cls'

while True:
    title = input('Title for Blog Post: ').title()
    os.system('clear')
    completion = client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {"role": "system", "content": "You are a blogger."},
        {"role": "user", "content": "Write a 100 word essay"},
        {"role": "user", "content": title}
    ]
    )
    story = completion.choices[0].message.content

    with open('blog.html', 'a') as file:
        file.write(f'<h2>{title}</h2>')
        file.write(f'<p>{story}</p>')
        
    print(title)
    print(story)