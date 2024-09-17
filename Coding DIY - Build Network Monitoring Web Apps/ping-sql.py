from bottle import run, route, request, post, redirect
import os
import sqlite3

database = ('ping.db')  
header = ('''
            <h1>Ping App</h1>
            <a href="/">Home<a>
            <a href="/ping">Test</a>
          ''') 

def db_create():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS host(host_list)')
    conn.commit()
    conn.close()

def db_find_host():
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    try:
        query = cursor.execute('SELECT * FROM host where rowid = 1') 
        query = query.fetchone()
        query = query[0]
    except:
        query = ''
    finally:
        conn.close()

    return query

@post('/db_insert')
def db_insert():
    hosts = request.forms.get('hosts')
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    try:
        cursor.execute('UPDATE host set host_list = ? where rowid = 1',(hosts,))
        if cursor.rowcount == 0:
            cursor.execute('INSERT INTO host(host_list) values(?)',(hosts,))
    except:
        print('database problem')
        
    finally:
        conn.commit()
        conn.close()

    redirect('/')

@route('/')
def index():
    host = db_find_host()
    host = host.split('\n')
    host_output = ''
    for item in host:
        item = item.strip()
        host_output = f'{host_output}{item}\n'
    page = f''' 
                {header}
                <form action="/db_insert" method="post">
                    Hosts:
                    <br>
                    <textarea name=hosts rows="50" cols="50">{host_output}</textarea>
                    <br>
                    <input type="submit">
                </form>
            '''
    return page

@route('/ping')
def ping():
    page = f'''
            <meta http-equiv="refresh" content="5">
            {header}
            '''
    hosts = db_find_host()
    print(hosts)
    hosts = hosts.split('\n')

    for item in hosts:
        item = item.strip()
        command = f'ping -c 1 {item}'
        try:
            response = os.popen(command).read()
        except:
            response = 'Problem'
        page = f'''
                {page}
                <h2>{item}</h2>
                <pre>{response}</pre>
                '''
    return page

db_create()

run(host='127.0.0.1', port=8080)