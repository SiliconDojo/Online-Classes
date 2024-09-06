import sqlite3

conn = sqlite3.connect('note.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS note(title,message)')
conn.commit()
conn.close()

def insert():
    conn = sqlite3.connect('note.db')
    cursor = conn.cursor()
    title = input('Note Title: ')
    message = input('Note Message: ')
    cursor.execute('INSERT INTO note(title,message) VALUES(?,?)',(title,message))
    conn.commit()
    conn.close()
    print(f'ADDED: {title}: {message}')

def fetch():
    conn = sqlite3.connect('note.db')
    cursor = conn.cursor()
    value = input('Search Query: ')
    query = cursor.execute('SELECT * FROM note where message like ?',(f'%{value}%',)) 
    query = query.fetchall()
    conn.close()
    print(query)

while True:
    action = input('Action (search/ insert): ')
    if action.lower() == 'search':
        fetch()
    elif action.lower() == 'insert':
        insert()
    elif action.lower() == 'exit':
        break
    else:
        print(f'{action} command not understood')