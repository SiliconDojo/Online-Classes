from bottle import run, route
import os

@route('/<host>/<interval:int>')
def index(host, interval):
    command = f'ping -c 1 {host}'

    response = os.popen(command).read()

    # '1 received' for Ubuntu
    if '1 packets received' in response:
        color = 'green'
    else:
        color = 'red'

    page = f'''
                <meta http-equiv="refresh" content="{interval}">
                <h1>Ping App</h1>
                <h3 style="background-color:{color};">{host}</h3>
                <pre>{response}</pre>
            '''

    return page

run(host='localhost', port=8080)