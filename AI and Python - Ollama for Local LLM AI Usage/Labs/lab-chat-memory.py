import ollama

memory = []

def ai(query, memory):
    response = ollama.chat(model='llama2:7b', messages=[
        {
            'role': 'system',
            'content': 'you are a friend',
        },
        {
            'role': 'user',
            'content': 'limit to 50 words',
        },
        {
            'role': 'user',
            'content': f'This is our previous conversation {memory}',
        },
        {
            'role': 'user',
            'content': query,
        },
    ])

    answer = response['message']['content']

    return answer

while True:
    query = input('--- ')
    response = ai(query, memory)
    memory.append(query)
    print(response)