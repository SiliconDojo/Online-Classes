data = input('Add a note: ')
with open('test.html','a') as file:
    file.write(data)
    # file.write(f'{data}\n')
    # file.write(f'<p>{data}</p>')
    # file.write(f'<h1>{data}</h1>\n')
