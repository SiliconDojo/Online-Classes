from bottle import run, route
import os

latency_quality = {'good': 20, 'usable': 40, 'bad': 50}

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
    command = 'ping -c 1 '
    arg = ' | grep time'
    host_list = host.split(',')
    body = ''
    for host in host_list:
        color = ''
        latency_color = ''
        host = host.strip()
        try:
            response = os.popen(f'{command} {host} {arg}').read()
        except:
            response = 'Problem Connecting'
        else:
            if 'time' in response:
                color = 'green'
            else:
                color = 'red'
            response_list = response.split(' ')
            for value in response_list:
                if 'time' in value:
                    time_list = value.split('=')
                    latency = float(time_list[1])
                    if latency < latency_quality['good']:
                        latency_color = 'lightgreen'
                    elif latency > latency_quality['good'] and latency <= latency_quality['usable']:
                        latency_color = 'yellow'
                    elif latency > latency_quality['usable'] and latency <= latency_quality['bad']:
                        latency_color = 'orange'
                    elif latency > latency_quality['bad']:
                        latency_color = 'red'
                    else:
                        latency_color = 'purple'
        finally:
            if response == '':
                response = 'Host Could Not Resolve'

        body = f''' 
                {body} 
                <h1 style="background-color:{color};">{host}</h1>
                <pre style="background-color:{latency_color}">{response}</pre>
                '''
    
    header = '<meta http-equiv="refresh" content="5">'
    page = f''' 
            {header}
            {body}
            '''
    return page

run(host='127.0.0.1', port=8080)