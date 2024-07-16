from datetime import datetime

while True:
    note = input('Note: ')
    timestamp = datetime.now()
    with open('note.csv','a') as file:
        file.write(f'{timestamp},{note}\n')

    with open('note-app.html', 'w') as app:
        app.write('<h1>Note App</h1>\n')
        app.write('<table>')
        with open('note.csv', 'r') as data:
            data = data.readlines()
            for record in data:
                record = record.split(',')
                app.write('<tr>')
                for value in record:
                    app.write(f'<td>{value}</td>')
                app.write('</tr>')
            app.write(('</table>'))