from requests import get
from json import dumps

response = get(f'http://ip-api.com/json/').json()

#print(response)

country = response['country']
#country = 'canada'

response_geo = get(f'https://restcountries.com/v3.1/name/{country}?fulltext=true').json()

#print(dumps(response_geo, indent=2))

for record in response_geo:
    print(record['name']['common'])
    print(record['capital'][0])

    