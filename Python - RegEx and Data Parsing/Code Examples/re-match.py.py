import re

pattern = r'hello'
text = 'hello world'

match = re.match(pattern, text)
if match:
    print('Match found:', match.group())
else:
    print('No match found')