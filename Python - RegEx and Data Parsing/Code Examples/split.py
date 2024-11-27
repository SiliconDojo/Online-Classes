string = '''hello this is bob at bob@bob.com.  I'm contacting you on behalf of my friend tom who is at (tom@aol.com).  Cindy at cindy@gmail.com gave me your email address to contact you. You can ping me on Linked in at @bob, or @cool_dude.'''

string = string.split(' ')

#print(string)

for word in string:
    if '@' in word:
        print(word)
        print(word.strip('.(),'))