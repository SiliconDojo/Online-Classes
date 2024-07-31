from requests import get
from json import dumps

result = get('https://restcountries.com/v3.1/name/belgium').json()

print(result)

#print(dumps(result, indent=2))

# print(result[0]['name']['official'])
# print(result[0]['capital'])
# print(result[0]['capital'][0])

#print(result[0]['name']['nativeName']['deu']['official'])