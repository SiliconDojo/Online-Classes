from bottle import run, route, post, request, redirect

from openai import OpenAI

client = OpenAI(api_key=' ')

header = f'''
            <h1>Open AI App</h1>
            <p><a href="/">Home</a> <a href="/rules">Rules</a></p>
        '''

def injection():
    try:
        with open('rules.txt', 'r') as file:
            file = file.read()
    except:
        file = ''

    return file

def ai(query):
    injection_rules = injection()
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": injection_rules},
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

@route('/rules')
def rules():
    try:
        with open('rules.txt', 'r') as file:
            file = file.read()
    except:
        file = ''
    
    body = f'''
            <form action="/process_rules" method="post">
                <textarea rows="20" cols="50" name="rules">{file}</textarea>
                <br>
                <input type="submit">
            </form>
            '''
    
    page = f'''
            {header}
            <br>
            {body}
            '''
    
    return page

@post('/process')
def index_process():
    query = request.forms.get('query')

    response = ai(query)

    body = f'''
            Query: {query} 
            <br>
            Response: {response}
            '''

    page = f'''
            {header}
            <br>
            {body}
            '''

    return page

@post('/process_rules')
def process_rules():
    rules = request.forms.get('rules')
    print(rules)

    with open('rules.txt', 'w') as file:
        file.write(rules)
    
    redirect('/rules')

run(host='localhost', port=8080)