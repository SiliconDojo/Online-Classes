import os
from time import sleep

site = 'cnn.com'

def status(site):
    command = f'ping -c 1 {site}'
    response = os.popen(command).read()

    return response

while True:
    os.system('clear')
    result = status(site)

    print(site)
    print(result)

    sleep(1)