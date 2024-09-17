from bottle import run, route
import os

@route('/')
def index():
    page =   f'''
                    <h1>Ping Web App</h1>
                    <p>Please Add a Host to the URL to begin pinging</p>
                    <p>Such as http://127.0.0.1:8080/cnn.com</p>
                '''
    return page

@route('/<host>')
def index(host):
    try:
        response = os.popen(f'ping -c 1 {host}').read()
    except:
        response = 'Problem Connecting'
    finally:
        if response == '':
            response = 'Host Could Not Resolve'
    header = '<meta http-equiv="refresh" content="5">'
    page = f''' {header}
                <h1>{host}</h1>
                <pre>{response}</pre>
            '''
    return page

run(host='127.0.0.1', port=8080)