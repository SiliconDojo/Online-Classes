import re

pattern = r'[\w\.-]+@[\w\.-]+\.[\w]{2,6}'

text = '''
        hello bob how are you?
        I was told your email is bob@aol.com.
        Is this right?
        My email is tim@gmail.com
        '''
response = re.search(pattern, text)

print(response)
print(response.group())
print(response.start())
print(response.end())