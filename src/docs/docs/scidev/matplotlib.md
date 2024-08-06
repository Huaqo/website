
# Matplotlib

## Awesome links

- [Python](../languages/python.md)
- [User guide ->](https://matplotlib.org/stable/users/index)

## Installation
```bash
pip install matplotlib
```

## Basic Usage

### Importing Matplotlib
```python
import matplotlib.pyplot as plt
```

### Creating a Simple Plot
```python
# Create a simple line plot
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Simple Plot')
plt.show()
```

## Plot Types

### Line Plot
```python
# Line plot with customization
plt.plot(x, y, label='Line 1', color='b', linestyle='-', marker='o')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Line Plot')
plt.legend()
plt.show()
```

### Scatter Plot
```python
# Scatter plot with customization
plt.scatter(x, y, label='Data points', color='r', marker='x')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title('Scatter Plot')
plt.legend()
plt.show()
```

### Bar Plot
```python
# Bar plot with customization
plt.bar(x, height, label='Bars', color='g')
plt.xlabel('x label')
plt.ylabel('Height')
plt.title('Bar Plot')
plt.legend()
plt.show()
```

### Histogram
```python
# Histogram with customization
plt.hist(data, bins=10, label='Data', color='m', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.legend()
plt.show()
```

### Pie Chart
```python
# Pie chart with customization
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Pie Chart')
plt.show()
```

### Box Plot
```python
# Box plot with customization
plt.boxplot(data)
plt.title('Box Plot')
plt.show()
```

## Advanced Plot Customization

### Adding a Grid
```python
plt.plot(x, y)
plt.grid(True)
plt.show()
```

### Adding Annotations
```python
plt.plot(x, y)
plt.annotate('Important Point', xy=(x_point, y_point), xytext=(x_text, y_text),
             arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
```

### Subplots
```python
# Multiple subplots in one figure
fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(x, y)
axs[0, 0].set_title('Subplot 1')

axs[0, 1].scatter(x, y)
axs[0, 1].set_title('Subplot 2')

axs[1, 0].bar(x, height)
axs[1, 0].set_title('Subplot 3')

axs[1, 1].hist(data)
axs[1, 1].set_title('Subplot 4')

plt.tight_layout()
plt.show()
```

### Customizing the Figure Size
```python
plt.figure(figsize=(10, 5))
plt.plot(x, y)
plt.show()
```

## Example

### Complete Example
```python
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a figure and a set of subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Line plot
axs[0, 0].plot(x, y, label='Line 1', color='b', linestyle='-', marker='o')
axs[0, 0].set_title('Line Plot')
axs[0, 0].legend()

# Scatter plot
axs[0, 1].scatter(x, y, label='Data points', color='r', marker='x')
axs[0, 1].set_title('Scatter Plot')
axs[0, 1].legend()

# Bar plot
axs[1, 0].bar(x, y, label='Bars', color='g')
axs[1, 0].set_title('Bar Plot')
axs[1, 0].legend()

# Histogram
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
axs[1, 1].hist(data, bins=4, label='Data', color='m', edgecolor='black')
axs[1, 1].set_title('Histogram')
axs[1, 1].legend()

# Show the plots
plt.tight_layout()
plt.show()
```
