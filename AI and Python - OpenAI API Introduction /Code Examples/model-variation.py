from openai import OpenAI

client = OpenAI()

query = 'how big is the sun?'

gpt_model = ['gpt-4o', 'gpt-4o-mini', 'gpt-4', 'gpt-3.5-turbo']

for version in gpt_model:
    completion = client.chat.completions.create(
    model=version,
    messages=[
        {"role": "system", "content": "You are a surfer."},
        {"role": "user", "content": "Always say 'Dude!'"},
        {"role": "user", "content": "Always say end your reply with 'later man'"},
        {"role": "user", "content": "Answer in 30 words or less"},
        {"role": "user", "content": "relate it to a bird"},
        {"role": "user", "content": query}
    ]
    )
    print(version)
    print(completion.choices[0].message.content)