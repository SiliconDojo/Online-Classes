
while True:
    name = input('Your Name: ')
    print(f'Hello {name}')

    if 'bob' in name:
        print('Its great to meet you')
    elif 'sue' in name:
        print('Glad you could make it!')
    elif name == 'phil':
        print('Phil is the man!!!')
    else:
        print('Happy to meet you')