from bottle import run, route, post, request

from openai import OpenAI

client = OpenAI(api_key=' ')

header = f'''
            <h1>Open AI App</h1>
            <p><a href="/">Home</a></p>
        '''

def ai(query):
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Answer in 30 words or less"},
        {"role": "user", "content": query}
    ]
    )
    #print(completion)
    #print(completion.choices[0].message)
    print(completion.choices[0].message.content)
    response = completion.choices[0].message.content

    return response

@route('/')
def index():
    form =  '''
            <form action="/process" method="post">
                Question: <input type="text" name="query">
                <br>
                <input type="submit">
            </form>
            '''
    page = f'{header}<br>{form}'
    return page

@post('/process')
def index_process():
    query = request.forms.get('query')

    response = ai(query)

    body = f'Query: {query} <br> Response: {response}'

    page = f'{header}<br>{body}'

    return page

run(host='localhost', port=8080)