import os

command = 'ping -c 1 '

while True:
    site = input('Domain Name: ')
    
    site = site.replace(';','')
    response = os.popen(f'{command} {site}').read()

    print(response)