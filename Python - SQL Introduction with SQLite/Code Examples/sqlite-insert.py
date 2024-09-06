import sqlite3

# Connect to an SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create table
cursor.execute('CREATE TABLE IF NOT EXISTS people(name,age,sex)')

# Insert a row of data
cursor.execute("INSERT INTO people(name,age,sex) VALUES(?,?,?)",('tom', 33, 'boy'))

# Save (commit) the changes
conn.commit()

# Close the connection
conn.close()