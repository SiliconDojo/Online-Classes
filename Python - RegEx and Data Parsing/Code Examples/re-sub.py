import re

pattern = r'[- ]'
number = '111-222 3333'

result = re.sub(pattern, '', number)
print(result)