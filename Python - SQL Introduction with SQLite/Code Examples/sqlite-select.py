import sqlite3

# Connect to an SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Return All Records
query = cursor.execute('SELECT * FROM people') 
query = query.fetchall()
print(query)
print()

#Return a specific number of records
query = cursor.execute('SELECT * FROM people') 
query = query.fetchmany(3)
print(query)
print()

#Return a single record
query = cursor.execute('SELECT * FROM people') 
query = query.fetchone()
print(query)
print()

#Use a Where clause
query = cursor.execute('SELECT * FROM people where age > ?',(20,)) 
query = query.fetchall()
print(query)

# Close the connection
conn.close()