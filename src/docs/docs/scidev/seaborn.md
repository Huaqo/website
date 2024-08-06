
# Seaborn

## Awesome links

- [Python](../languages/python.md)
- [Documentation ->](https://seaborn.pydata.org/)

## Installation
```bash
pip install seaborn
```

## Basic Usage

### Importing Seaborn
```python
import seaborn as sns
import matplotlib.pyplot as plt
```

### Loading Example Datasets
```python
# Load an example dataset
tips = sns.load_dataset('tips')
```

## Plot Types

### Scatter Plot
```python
# Scatter plot with linear regression
sns.lmplot(x='total_bill', y='tip', data=tips)
plt.show()
```

### Line Plot
```python
# Line plot with confidence interval shading
sns.lineplot(x='size', y='total_bill', data=tips)
plt.show()
```

### Bar Plot
```python
# Bar plot with aggregation
sns.barplot(x='day', y='total_bill', data=tips)
plt.show()
```

### Histogram
```python
# Histogram with KDE
sns.histplot(tips['total_bill'], kde=True)
plt.show()
```

### Box Plot
```python
# Box plot with categories
sns.boxplot(x='day', y='total_bill', data=tips)
plt.show()
```

### Violin Plot
```python
# Violin plot with categories
sns.violinplot(x='day', y='total_bill', data=tips)
plt.show()
```

### Heatmap
```python
# Heatmap with annotations
flights = sns.load_dataset('flights')
flights_pivot = flights.pivot('month', 'year', 'passengers')
sns.heatmap(flights_pivot, annot=True, fmt='d')
plt.show()
```

### Pair Plot
```python
# Pair plot with hue
sns.pairplot(tips, hue='sex')
plt.show()
```

### Joint Plot
```python
# Joint plot with scatter and histograms
sns.jointplot(x='total_bill', y='tip', data=tips, kind='scatter')
plt.show()
```

## Customizing Plots

### Adding Titles and Labels
```python
sns.boxplot(x='day', y='total_bill', data=tips)
plt.title('Total Bill by Day')
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill')
plt.show()
```

### Changing the Figure Size
```python
plt.figure(figsize=(10, 6))
sns.boxplot(x='day', y='total_bill', data=tips)
plt.show()
```

### Setting the Style
```python
sns.set_style('whitegrid')
sns.boxplot(x='day', y='total_bill', data=tips)
plt.show()
```

### Removing the Axes
```python
sns.boxplot(x='day', y='total_bill', data=tips)
sns.despine()
plt.show()
```

## Example

### Complete Example
```python
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset
tips = sns.load_dataset('tips')

# Set the style
sns.set_style('whitegrid')

# Create a figure and a set of subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 10))

# Scatter plot with linear regression
sns.lmplot(x='total_bill', y='tip', data=tips, ax=axs[0, 0])
axs[0, 0].set_title('Scatter Plot with Linear Regression')

# Bar plot with aggregation
sns.barplot(x='day', y='total_bill', data=tips, ax=axs[0, 1])
axs[0, 1].set_title('Bar Plot')

# Box plot with categories
sns.boxplot(x='day', y='total_bill', data=tips, ax=axs[1, 0])
axs[1, 0].set_title('Box Plot')

# Heatmap with annotations
flights = sns.load_dataset('flights')
flights_pivot = flights.pivot('month', 'year', 'passengers')
sns.heatmap(flights_pivot, annot=True, fmt='d', ax=axs[1, 1])
axs[1, 1].set_title('Heatmap')

# Show the plots
plt.tight_layout()
plt.show()
```


