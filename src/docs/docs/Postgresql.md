
# PostgreSQL

## Getting Started

```sql
-- Connect to a database
psql -h host -U user -d dbname

-- List all databases
\l

-- Connect to a database within psql
\c dbname

-- List all tables
\dt

-- Describe a table
\d table_name

-- Exit psql
\q
```

## Data Types

```sql
-- PostgreSQL supports the following data types
INTEGER        -- Integer value
SERIAL         -- Auto-incrementing integer
BIGINT         -- Large integer value
REAL           -- Floating-point number
DOUBLE PRECISION -- Double-precision floating-point number
NUMERIC        -- Exact number with selectable precision
CHAR(n)        -- Fixed-length character string
VARCHAR(n)     -- Variable-length character string
TEXT           -- Variable-length character string (no limit)
DATE           -- Calendar date (year, month, day)
TIME           -- Time of day (hours, minutes, seconds)
TIMESTAMP      -- Date and time
BOOLEAN        -- Logical Boolean (true/false)
BYTEA          -- Binary data ("byte array")
```

## Creating Tables

```sql
-- Create a table
CREATE TABLE table_name (
    column1 SERIAL PRIMARY KEY,
    column2 VARCHAR(100) NOT NULL,
    column3 INTEGER DEFAULT 0
);

-- Create a table with a foreign key
CREATE TABLE child_table (
    id SERIAL PRIMARY KEY,
    parent_id INTEGER,
    FOREIGN KEY (parent_id) REFERENCES parent_table(id)
);
```

## Inserting Data

```sql
-- Insert a single row
INSERT INTO table_name (column2, column3) VALUES ('Hello', 123);

-- Insert multiple rows
INSERT INTO table_name (column2, column3) VALUES
('World', 456),
('PostgreSQL', 789);
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

-- Right join
SELECT * FROM table1
RIGHT JOIN table2 ON table1.column = table2.column;

-- Full join
SELECT * FROM table1
FULL JOIN table2 ON table1.column = table2.column;
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
BEGIN;

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
COPY table_name FROM '/path/to/file.csv' DELIMITER ',' CSV HEADER;

-- Export data to a CSV file
COPY table_name TO '/path/to/file.csv' DELIMITER ',' CSV HEADER;
```

## User Management

```sql
-- Create a new user
CREATE USER username WITH PASSWORD 'password';

-- Grant privileges to a user
GRANT ALL PRIVILEGES ON DATABASE dbname TO username;

-- Revoke privileges from a user
REVOKE ALL PRIVILEGES ON DATABASE dbname FROM username;

-- Drop a user
DROP USER username;
```

## Backup and Restore

```bash
-- Backup a database
pg_dump dbname > backup.sql

-- Restore a database
psql dbname < backup.sql
```

