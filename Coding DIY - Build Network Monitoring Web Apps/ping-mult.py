from bottle import run, route
import os

@route('/')
def index():
    page =   f'''
                <h1>Ping Web App</h1>
                <p>Please Add a Hosts to the URL to begin pinging</p>
                <p>Such as http://127.0.0.1:8080/cnn.com,fox.com,192.168.1.1</p>
            '''
    return page

@route('/<host>')
def index(host):
    host_list = host.split(',')
    body = ''
    for value in host_list:
        value = value.strip()
        try:
            response = os.popen(f'ping -c 1 {value}').read()
        except:
            response = 'Problem Connecting'
        finally:
            if response == '':
                response = 'Host Could Not Resolve'

        body = f'''
                {body}
                <h1>{value}</h1>
                <pre>{response}</pre>
                '''
    header = '<meta http-equiv="refresh" content="5">'
    page = f''' 
            {header}
            {body}
            '''
    return page

run(host='127.0.0.1', port=8080)