
# SQLite3

## Awesome links

- [Python](../languages/python.md)
- [Documentation ->](https://docs.python.org/3/library/sqlite3.html)

## Getting Started

### Importing the SQLite3 Module

```python
import sqlite3
```

### Connecting to a Database

```python
# Connect to a database (creates the database if it doesn't exist)
conn = sqlite3.connect('example.db')

# Create a cursor object
cur = conn.cursor()
```

### Closing the Connection

```python
# Commit the changes
conn.commit()

# Close the connection
conn.close()
```

## Creating Tables

### Creating a Table

```python
cur.execute('''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL)''')
conn.commit()
```

## Inserting Data

### Inserting a Single Row

```python
cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 30))
conn.commit()
```

### Inserting Multiple Rows

```python
users = [('Bob', 25), ('Charlie', 35), ('David', 40)]
cur.executemany("INSERT INTO users (name, age) VALUES (?, ?)", users)
conn.commit()
```

## Querying Data

### Selecting All Rows

```python
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)
```

### Selecting with Conditions

```python
cur.execute("SELECT * FROM users WHERE age > ?", (30,))
rows = cur.fetchall()
for row in rows:
    print(row)
```

### Using Named Parameters

```python
cur.execute("SELECT * FROM users WHERE name = :name", {"name": "Alice"})
rows = cur.fetchall()
for row in rows:
    print(row)
```

## Updating Data

### Updating Rows

```python
cur.execute("UPDATE users SET age = ? WHERE name = ?", (28, 'Alice'))
conn.commit()
```

## Deleting Data

### Deleting Rows

```python
cur.execute("DELETE FROM users WHERE name = ?", ('Bob',))
conn.commit()
```

## Using Transactions

### Starting a Transaction

```python
conn.execute("BEGIN TRANSACTION")
```

### Committing a Transaction

```python
conn.commit()
```

### Rolling Back a Transaction

```python
conn.rollback()
```

## Using Context Managers

### Automatically Committing Transactions

```python
with sqlite3.connect('example.db') as conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Eve', 22))
```

## Advanced Features

### Creating an In-Memory Database

```python
conn = sqlite3.connect(':memory:')
cur = conn.cursor()
```

### Using Row Factory for Named Columns

```python
conn.row_factory = sqlite3.Row
cur = conn.cursor()
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row['name'], row['age'])
```

### Executing Script

```python
cur.executescript('''
    DROP TABLE IF EXISTS users;
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL);
    INSERT INTO users (name, age) VALUES ('Alice', 30);
    INSERT INTO users (name, age) VALUES ('Bob', 25);
''')
conn.commit()
```

## Error Handling

### Handling Exceptions

```python
try:
    cur.execute("SELECT * FROM non_existing_table")
except sqlite3.Error as e:
    print("An error occurred:", e.args[0])
```

