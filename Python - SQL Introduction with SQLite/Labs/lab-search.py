import sqlite3

def fetch(name):
    conn = sqlite3.connect('lab.db')
    cursor = conn.cursor()
    query = cursor.execute('SELECT * FROM student where name like ?',(f'%{name}%',)) 
    query = query.fetchall()
    conn.close()

    return query

while True:
    name = input('Name to Search: ')
    query = fetch(name)
    print(query)
    print()

    for record in query:
        print(record)
    print()

    print('Name:\t Age: \t Allergy:')
    for record in query:
        print(f'{record[0]}\t {record[1]}\t {record[2]}')