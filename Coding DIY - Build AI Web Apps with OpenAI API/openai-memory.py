from bottle import run, route, post, request, redirect

from openai import OpenAI

import sqlite3

client = OpenAI(api_key=' ')

injection_rules = '''
                    limit answers to under 50 words
                    '''
header = f'''
            <h1>Open AI App</h1>
            <p><a href="/">Home</a> <a href="/memory">Memory<a></p>
        '''

def db_create():
    conn = sqlite3.connect('memory.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS memory(query,response)')
    conn.commit()
    conn.close()

def db_insert(query, response):
    conn = sqlite3.connect('memory.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO memory(query,response) VALUES(?,?)',(query,response))
    conn.commit()
    conn.close()
    print(f'ADDED: {query}: {response}')

def db_fetch():
    conn = sqlite3.connect('memory.db')
    cursor = conn.cursor()
    query = cursor.execute('SELECT * FROM memory') 
    query = query.fetchall()
    conn.close()
    return query

def db_injection():
    conn = sqlite3.connect('memory.db')
    cursor = conn.cursor()
    query = cursor.execute('SELECT query FROM memory where query like "%I want you%"') 
    query = query.fetchall()
    conn.close()
    print(query)
    return query

def ai(query):
    injection_rules = str(db_injection())
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

@route('/memory')
def rules():
    response = db_fetch()

    body = '<table>'
    for value in response:
        body = f'{body} <tr><td>{value[0]}</td><td>{value[1]}</td></tr>'
    body = f'{body} </table>'

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

    db_insert(query, response)

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

db_create()
run(host='localhost', port=8080)