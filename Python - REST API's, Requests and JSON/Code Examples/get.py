from requests import get

response = get('http://www.arstechnica.com').text

print(response)