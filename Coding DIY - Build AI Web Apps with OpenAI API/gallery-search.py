from bottle import run, route, post, request, static_file
import sqlite3
import os

pic_directory = 'search_pics'
os.makedirs(pic_directory, exist_ok=True)

database = 'gallery-search.db'

header = f'''
            <h1>Open AI App</h1>
            <p><a href="/">Home</a></p>
        '''

def db_create():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS gallery(filename,description)')
    conn.commit()
    conn.close()

def db_search(query):
    print(f'QUERY: {query}')
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    query = f'%{query}%'
    query = cursor.execute('SELECT * FROM gallery where description like ?',(query,)) 
    query = query.fetchall()
    conn.close()
    print(query)
    return query

@route('/search_pics/<filename:path>')
def send_static(filename):
    return static_file(filename, root='./search_pics/')

@route('/')
def index():
    form =  '''
            <form action="/search" method="post">
                Find: <input type="text" name="query">
                <br>
                <input type="submit">
            </form>
            '''
    
    response = db_search(' ')
    gallery = '<div style="vertical-align:top;">'
    for record in response:
        filename = os.path.join(pic_directory, record[0])
        gallery = f'''
                    {gallery} 
                    <div style="display:inline-block;width:300px;height:auto;vertical-align: top;">
                    <img style="width:100%;height:auto;" src="{filename}">
                    <p>{record[1]}</p>
                    </div>
                    '''
    gallery = f'{gallery} </div>'
    
    page = f'{header}<br>{form}<hr>{gallery}'

    return page

@post('/search')
def index_process():
    query = request.forms.get('query')

    response = db_search(query)
    gallery = '<div style="vertical-align:top;">'
    for record in response:
        filename = os.path.join(pic_directory, record[0])
        gallery = f'''
                    {gallery} 
                    <div style="display:inline-block;width:300px;height:auto;vertical-align: top;">
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

db_create()
run(host='localhost', port=8080)