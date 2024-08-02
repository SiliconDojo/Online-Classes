import os
from time import sleep

site = ['cnn.com', 'fox.com', 'tacobell.com', 'notarealsite.tv']
header = '<meta http-equiv="refresh" content="5">'

def status(site):
    color = 'red'
    command = f'ping -c 1 {site}'
    response = os.popen(command).read()

    if '1 packets received' in response:
        color = 'green'

    return response, color

while True:
    os.system('clear')
    page = header
    for item in site:
        result = status(item)
        page = f''' 
                    {page}
                    <h2 style="background-color:{result[1]};">{item}</h2>
                    <pre>{result[0]}</pre>
                '''

    try:
        with open('dashboard.html', 'w') as file:
            file.write(page)
    except:
        print('ERROR - Writing to File')

    sleep(1)