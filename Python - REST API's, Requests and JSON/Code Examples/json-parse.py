from requests import get
from json import dumps

ip = '151.101.3.5' #cnn.com

result = get(f'http://ip-api.com/json/{ip}').json()

print(result)
# print(result['city'])

# print(dumps(result, indent=2))
