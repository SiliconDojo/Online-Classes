import requests

mac = 'a8:51:ab:98:8e:52'
try:
    response = requests.get(f'https://www.macvendorlookup.com/api/v2/{mac}').json()
except:
    response = f'{mac} not found'

print(response)

print(f"Company: {response[0]['company']}")