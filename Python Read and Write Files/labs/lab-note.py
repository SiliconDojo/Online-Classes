filename = 'note.html'

with open(filename, 'w') as file:
    file.write('<h1>Note App</h1>\n')

while True:
    update = input('Add an Update: ')
    with open(filename, 'a') as file:
        file.write(f'<p>{update}</p>\n')