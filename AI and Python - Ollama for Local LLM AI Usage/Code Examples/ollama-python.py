import ollama

response = ollama.chat(model='llama2:7b', messages=[
    {
        'role': 'system',
        'content': 'you are a poet',
    },
    {
        'role': 'user',
        'content': 'limit to 50 words',
    },
    {
        'role': 'user',
        'content': 'Why is the sky blue? ',
    },
])

#print(response)
print(response['message']['content'])