import ollama

response = ollama.chat(
model='llava',
messages=[
    {
    'role': 'user',
    'content': 'what is in this picture',
    'images': ['image.png'],
    },
],
)
print(response)
print(response['message']['content'])
