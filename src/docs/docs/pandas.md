
# Pandas

## Installation
```bash
pip install pandas
```

## Basic Usage

### Importing Pandas
```python
import pandas as pd
```

### Creating DataFrames

#### From a Dictionary
```python
data = {'Column1': [1, 2, 3], 'Column2': [4, 5, 6]}
df = pd.DataFrame(data)
```

#### From a CSV File
```python
df = pd.read_csv('path_to_csv_file.csv')
```

### Viewing Data
```python
# Display the first few rows
print(df.head())

# Display basic information
print(df.info())

# Display summary statistics
print(df.describe())
```

## Data Selection

### Selecting Columns
```python
# Select a single column
df['Column1']

# Select multiple columns
df[['Column1', 'Column2']]
```

### Selecting Rows
```python
# Select rows by index
df.iloc[0]  # First row
df.iloc[0:3]  # First three rows

# Select rows by label
df.loc[0]  # First row
df.loc[0:2]  # Rows with labels 0 to 2
```

### Filtering Data
```python
# Filter rows based on a condition
df[df['Column1'] > 2]
```

## Data Cleaning

### Handling Missing Data
```python
# Drop rows with missing values
df.dropna()

# Fill missing values
df.fillna(value)
```

### Renaming Columns
```python
df.rename(columns={'OldName': 'NewName'}, inplace=True)
```

### Changing Data Types
```python
df['Column1'] = df['Column1'].astype('float')
```

## Data Manipulation

### Adding Columns
```python
df['NewColumn'] = df['Column1'] + df['Column2']
```

### Dropping Columns
```python
df.drop(columns=['Column1'], inplace=True)
```

### Grouping Data
```python
# Group by a column and calculate mean
df.groupby('Column1').mean()

# Group by multiple columns and calculate sum
df.groupby(['Column1', 'Column2']).sum()
```

### Sorting Data
```python
# Sort by a single column
df.sort_values(by='Column1')

# Sort by multiple columns
df.sort_values(by=['Column1', 'Column2'], ascending=[True, False])
```

## Merging and Joining

### Concatenation
```python
# Concatenate two DataFrames vertically
pd.concat([df1, df2])

# Concatenate two DataFrames horizontally
pd.concat([df1, df2], axis=1)
```

### Merging
```python
# Merge two DataFrames on a key
pd.merge(df1, df2, on='Key')

# Merge with different join types
pd.merge(df1, df2, on='Key', how='left')  # Left join
pd.merge(df1, df2, on='Key', how='right')  # Right join
pd.merge(df1, df2, on='Key', how='inner')  # Inner join
pd.merge(df1, df2, on='Key', how='outer')  # Outer join
```

## Input/Output

### Reading and Writing CSV Files
```python
# Read a CSV file
df = pd.read_csv('path_to_csv_file.csv')

# Write a DataFrame to a CSV file
df.to_csv('path_to_output_csv_file.csv', index=False)
```

### Reading and Writing Excel Files
```python
# Read an Excel file
df = pd.read_excel('path_to_excel_file.xlsx')

# Write a DataFrame to an Excel file
df.to_excel('path_to_output_excel_file.xlsx', index=False)
```

## Example

### Complete Example
```python
import pandas as pd

# Create a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Display the first few rows
print(df.head())

# Add a new column
df['Age in 10 Years'] = df['Age'] + 10

# Filter rows where Age is greater than 30
filtered_df = df[df['Age'] > 30]

# Group by City and calculate mean Age
grouped_df = df.groupby('City').mean()

# Save the DataFrame to a CSV file
df.to_csv('output.csv', index=False)
```

For more details, refer to the [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/).
