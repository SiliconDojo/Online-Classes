from openai import OpenAI

client = OpenAI()

# openai_key ='API Key from OpenAI'

# client = OpenAI(api_key=openai_key)

completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)
print('***')
print(completion)
print('***')
print(completion.choices[0].message)
print('***')
print(completion.choices[0].message.content)
print(completion.usage.total_tokens)

print(type(completion))