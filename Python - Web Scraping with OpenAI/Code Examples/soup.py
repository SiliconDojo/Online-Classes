from requests import get
from bs4 import BeautifulSoup

page = get('https://arstechnica.com/space/2024/08/china-deploys-first-satellites-for-a-broadband-network-to-rival-starlink/').text

soup = BeautifulSoup(page, 'html.parser')

print(soup.prettify())

# print(soup.title)

# print(soup.title.text)

# print(soup.find_all('p'))

# for line in soup.find_all('p'):
#     print(line.text)

# for line in soup.find_all('a'):
#     print(line.get('href'))