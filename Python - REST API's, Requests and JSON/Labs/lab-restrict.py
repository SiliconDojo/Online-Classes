from requests import get

response = get(f'http://ip-api.com/json/').json()

#print(response)

country = response['country']
#country = 'Canada'

if country == 'United States':
    print(f'Welcome In! We love people from {country}')
else:
    print(f'Go Away! We dont like stinky {country} people')
