import os
import requests

response_arp = os.popen('arp -a').readlines()

print(response_arp)

mac_list = []
for line in response_arp:
    host = line.split(' ')
    for item in host:
        if ":" in item:
            mac_list.append(item)

print(mac_list)

for host in mac_list:
    try:
        response = requests.get(f'https://www.macvendorlookup.com/api/v2/{host}').json()
        print(f'{host} - {response[0]['company']}')
    except:
        response = 'not found'
        print(f'{host} - {response}')