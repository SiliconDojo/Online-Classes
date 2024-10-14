# SQLite and Python

## Create Table if Not Exist

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


## Insert

```
import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute("INSERT INTO people(name,age,sex) VALUES(?,?,?)",('tom', 33, 'boy'))
conn.commit()
conn.close()
```
