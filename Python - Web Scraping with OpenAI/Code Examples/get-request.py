from requests import get

result = get('https://arstechnica.com/space/2024/08/china-deploys-first-satellites-for-a-broadband-network-to-rival-starlink/').text

print(result)

with open('ars.html', 'w') as file:
    file.write(result)