import re

pattern = r'[\w\.-]+@[\w\.-]+\.+[\w]{3}'

text = '''hello this is bob at bob@bob.com.  I'm contacting you on behalf of my friend tom who is at tom@aol.com.  Cindy at cindy@gmail.com gave me your email address to contact you. You can ping me on Linked in at @bob, or @cool_dude.'''

response = re.findall(pattern, text)

print(response)
