# SQLite and Python

## Create Table if Not Exist

**Primary Keys and Unique ID**

**ROWID** column is created by default and can be called even though it does not show up in a select * statement.  When rows are deleted the rowid value will be reused by SQLite so it is not good as a permenant identifier.

**PRIMARY KEY** Auto increments by default, but if a row is deleted SQLite will reuse the value of the deleted row.

**AUTOINCREMENT** Forces SQLite to continue iterating up for key values and will not reuse an ID if it is deleted. Use this for anytime a key may need to uniquely identify a record for a period of time.

```
id INTEGER PRIMARY KEY AUTOINCREMENT,
```

**Basic Syntax**

You do not have to assign data types in SQLite and even if you do they will not be strictly enforced by default.

```
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS people(name,age,sex)')
conn.commit()
conn.close()
```

**Assign Data Types**

Simply assigning data types is useful for documentation, but SQLite will generally ignore on insert.

```
CREATE TABLE IF NOT EXISTS people (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    sex TEXT NOT NULL
)
```

**Assign Acceptable Values**

You can set an acceptable list of values that the column can contain.

```
CREATE TABLE IF NOT EXISTS people (
    name TEXT NOT NULL,
    age INTEGER NOT NULL CHECK(age > 0),  -- Strictly INTEGER and age > 0
    sex TEXT NOT NULL CHECK(sex IN ('male', 'female', 'other')) -- Strict set of values
)
```

**Strict Mode**

By adding STRICT at the end of the table creation this will ensure that if you try to insert data of the wrong type the transaction will fail.

```
CREATE TABLE IF NOT EXIST people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
    sex TEXT NOT NULL
) STRICT;
```

## Select

Fetch All Columns and All Records from Table and return the data as a set.

```
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM people")
rows = cursor.fetchall()

conn.close()

```
**Fetch All Record**

Generally what you will use.

```
fetchall()
```

**Fetch a Single Record**

Good when only a single record should exist
```
fetchone()
```

**Fetch a Specific Number of Records**

Good for when you have to process a limited number of results such as 'the last 5 occurences'
```
fetchmany(size)
```

## Insert

```
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute("INSERT INTO people(name,age,sex) VALUES(?,?,?)",('tom', 33, 'boy'))
conn.commit()
conn.close()
```

## Update or Insert

This code either updates a record if one is found with the name 'tom', and if a record does not exist it creates one.

```
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM people WHERE name = ?', ('Tom',))
record = cursor.fetchone()
if record:
    cursor.execute('UPDATE people SET age = ?, sex = ? WHERE name = ?', (35, 'male', 'Tom'))
else:
    cursor.execute('INSERT INTO people (name, age, sex) VALUES (?, ?, ?)', ('Tom', 35, 'male'))

conn.commit()
conn.close()

```
