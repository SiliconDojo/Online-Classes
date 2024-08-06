from openai import OpenAI

client = OpenAI()

query = 'how big is the sun?'

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a surfer."},
    {"role": "user", "content": "Always say 'Dude!'"},
    {"role": "user", "content": "Always say end your reply with 'later man'"},
    {"role": "user", "content": "Answer in 10 words or less"},
    {"role": "user", "content": query}
  ]
)

print(completion.choices[0].message.content)