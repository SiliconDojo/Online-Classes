from bottle import run, route, post, request, static_file
from openai import OpenAI
import requests
import datetime
import os
import sqlite3

pic_directory = 'dalle_pics'
try:
    os.mkdir(pic_directory)
except:
    pass

client = OpenAI(api_key=' ')

header = f'''
            <h1>Open AI App</h1>
            <p><a href="/">Home</a> <a href="/search">Search</a></p>
        '''

def db_create():
    conn = sqlite3.connect('gallery.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS gallery(prompt,revised_prompt,filename)')
    conn.commit()
    conn.close()

def db_insert(prompt, revised_prompt, filename):
    conn = sqlite3.connect('gallery.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO gallery(prompt,revised_prompt,filename) VALUES(?,?,?)',(prompt,revised_prompt,filename,))
    conn.commit()
    conn.close()
    print(f'ADDED: {prompt}\n{revised_prompt}\n{filename}')

def db_search(query):
    print(f'QUERY: {query}')
    conn = sqlite3.connect('gallery.db')
    cursor = conn.cursor()
    query = f'%{query}%'
    query = cursor.execute('SELECT * FROM gallery where revised_prompt like ?',(query,)) 
    query = query.fetchall()
    conn.close()
    print(query)
    return query

def ai(query):
    response = client.images.generate(
    model="dall-e-3",
    prompt=query,
    size="1024x1024",
    quality="standard",
    n=1,
    )

    image_url = response.data[0].url
    revised_prompt = response.data[0].revised_prompt
    print(response)
    return image_url, revised_prompt

def download(url):
    filename = f'{str(datetime.datetime.now())}.png'

    file_response = requests.get(url)
    file_path = os.path.join(pic_directory, filename)
    with open(file_path, 'wb') as file:
        file.write(file_response.content)

    return filename

@route('/')
def index():
    form =  '''
            <form action="/process" method="post">
                Create Picture: <input type="text" name="query">
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

    filename = download(response[0])
    db_insert(query, response[1], filename)

    body = f''' 
            Prompt: {query}<br>
            <img style="height:400px; width:auto;"src="{response[0]}"><br>
            Revised Prompt: {response[1]}
            '''

    page = f'{header}<br>{body}'

    return page

@route('/search')
def index():
    form =  '''
            <form action="/process_search" method="post">
                Find: <input type="text" name="query">
                <br>
                <input type="submit">
            </form>
            '''
    response = db_search(' ')
    gallery = '<div style="vertical-align:top;">'

    for record in response:
        gallery = f'''
                    {gallery} 
                    <div style="display:inline-block;width:300px;height:auto;vertical-align: top;">
                    <p>{record[0]}</p>
                    <img style="width:100%;height:auto;" src="/{pic_directory}/{record[2]}">
                    <p>{record[1]}</p>
                    </div>
                    '''
    gallery = f'{gallery} </div>'
    
    
    page = f'{header}<br>{form} <hr> {gallery}'

    return page

@post('/process_search')
def index_process():
    query = request.forms.get('query')

    response = db_search(query)
    gallery = '<div style="vertical-align:top;">'

    for record in response:
        filename = os.path.join(pic_directory, record[2])

        gallery = f'''
                    {gallery} 
                    <div style="display:inline-block;width:300px;height:auto;vertical-align: top;">
                    <p>{record[0]}</p>
                    <img style="width:100%;height:auto;" src="{filename}">
                    <p>{record[1]}</p>
                    </div>
                    '''
    gallery = f'{gallery} </div>'

    body = f''' 
            Search Prompt: {query}
            <hr>
            {gallery}
            '''

    page = f'{header}<br>{body}'

    return page

@route('/dalle_pics/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./dalle_pics/')

db_create()
run(host='localhost', port=8080)