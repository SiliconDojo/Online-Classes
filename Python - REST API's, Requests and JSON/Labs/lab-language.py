from requests import get
from json import dumps

while True:
    language = input('What Language: ')
    response = get(f'https://restcountries.com/v3.1/lang/{language}')
    response_json = response.json()

    #print(dumps(response, indent=2))

    # with open('out.txt', 'w') as file:
    #     file.write(dumps(response, indent=2))

    status = response.status_code
    if status == 200:
        for country in response_json:
            print(f'{country['name']['common']}')
    else:
        print(f'Language {language} not found - {status}')

