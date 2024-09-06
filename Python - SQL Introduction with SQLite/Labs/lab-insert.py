import sqlite3

conn = sqlite3.connect('lab.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS student(name,age,allergy)')
conn.commit()
conn.close()

def insert(name,age,allergy):
    conn = sqlite3.connect('lab.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO student(name,age,allergy) VALUES(?,?,?)',(name,age,allergy))
    conn.commit()
    conn.close()

def fetch():
    conn = sqlite3.connect('lab.db')
    cursor = conn.cursor()
    query = cursor.execute('SELECT * FROM student') 
    query = query.fetchall()
    conn.close()

    return query

while True:
    name = input('Name: ')
    age = input('Age: ')
    allergy = input('Allergy: ')
    insert(name,age,allergy)
    query = fetch()
    print(query)
