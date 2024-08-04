
# SQLite CLI

## Getting Started

```sql
-- Open a database file
sqlite3 database.db

-- Open an in-memory database
sqlite3 :memory:
```

## Basic Commands

```sql
-- Show all tables
.tables

-- Show the schema of a table
.schema table_name

-- Exit SQLite
.quit
```

## Data Types

```sql
-- SQLite supports the following data types
NULL    -- The value is a NULL value
INTEGER -- A signed integer
REAL    -- A floating point value
TEXT    -- A text string
BLOB    -- A binary large object
```

## Creating Tables

```sql
-- Create a table
CREATE TABLE table_name (
    column1 INTEGER PRIMARY KEY,
    column2 TEXT NOT NULL,
    column3 REAL DEFAULT 0.0
);

-- Create a table with a foreign key
CREATE TABLE child_table (
    id INTEGER PRIMARY KEY,
    parent_id INTEGER,
    FOREIGN KEY (parent_id) REFERENCES parent_table(id)
);
```

## Inserting Data

```sql
-- Insert a single row
INSERT INTO table_name (column1, column2) VALUES (1, 'Hello');

-- Insert multiple rows
INSERT INTO table_name (column1, column2) VALUES
(2, 'World'),
(3, 'SQLite');
```

## Querying Data

```sql
-- Select all rows
SELECT * FROM table_name;

-- Select specific columns
SELECT column1, column2 FROM table_name;

-- Select with a condition
SELECT * FROM table_name WHERE column1 = 1;

-- Select with sorting
SELECT * FROM table_name ORDER BY column1 DESC;

-- Select with a limit
SELECT * FROM table_name LIMIT 10;
```

## Updating Data

```sql
-- Update specific rows
UPDATE table_name SET column2 = 'Updated' WHERE column1 = 1;

-- Update all rows
UPDATE table_name SET column2 = 'Updated';
```

## Deleting Data

```sql
-- Delete specific rows
DELETE FROM table_name WHERE column1 = 1;

-- Delete all rows
DELETE FROM table_name;
```

## Joins

```sql
-- Inner join
SELECT * FROM table1
INNER JOIN table2 ON table1.column = table2.column;

-- Left join
SELECT * FROM table1
LEFT JOIN table2 ON table1.column = table2.column;

-- Cross join
SELECT * FROM table1
CROSS JOIN table2;
```

## Aggregate Functions

```sql
-- Count rows
SELECT COUNT(*) FROM table_name;

-- Sum values
SELECT SUM(column1) FROM table_name;

-- Average values
SELECT AVG(column1) FROM table_name;

-- Minimum value
SELECT MIN(column1) FROM table_name;

-- Maximum value
SELECT MAX(column1) FROM table_name;

-- Group by
SELECT column2, COUNT(*) FROM table_name GROUP BY column2;
```

## Transactions

```sql
-- Begin a transaction
BEGIN TRANSACTION;

-- Commit a transaction
COMMIT;

-- Rollback a transaction
ROLLBACK;
```

## Indexes

```sql
-- Create an index
CREATE INDEX index_name ON table_name (column1);

-- Create a unique index
CREATE UNIQUE INDEX unique_index_name ON table_name (column1);

-- Drop an index
DROP INDEX index_name;
```

## Views

```sql
-- Create a view
CREATE VIEW view_name AS
SELECT column1, column2 FROM table_name WHERE column1 = 1;

-- Select from a view
SELECT * FROM view_name;

-- Drop a view
DROP VIEW view_name;
```

## Importing and Exporting Data

```sql
-- Import data from a CSV file
.mode csv
.import file.csv table_name

-- Export data to a CSV file
.mode csv
.headers on
.output file.csv
SELECT * FROM table_name;
.output stdout
```

