
# NumPy

## Installation
```bash
pip install numpy
```

## Basic Usage

### Importing NumPy
```python
import numpy as np
```

## Creating Arrays

### From a List
```python
arr = np.array([1, 2, 3])
```

### From a Tuple
```python
arr = np.array((1, 2, 3))
```

### Using Functions
```python
# Create an array of zeros
zeros = np.zeros((2, 3))

# Create an array of ones
ones = np.ones((2, 3))

# Create an array with a range of values
range_array = np.arange(0, 10, 2)

# Create an array with linearly spaced values
linspace_array = np.linspace(0, 1, 5)
```

## Array Attributes

### Getting Shape and Size
```python
arr.shape
arr.size
```

### Getting Data Type
```python
arr.dtype
```

## Array Operations

### Arithmetic Operations
```python
# Element-wise addition
result = arr1 + arr2

# Element-wise subtraction
result = arr1 - arr2

# Element-wise multiplication
result = arr1 * arr2

# Element-wise division
result = arr1 / arr2
```

### Universal Functions
```python
# Square root
result = np.sqrt(arr)

# Exponential
result = np.exp(arr)

# Sine
result = np.sin(arr)
```

## Indexing and Slicing

### Accessing Elements
```python
element = arr[0]

# 2D array
element = arr[0, 1]
```

### Slicing Arrays
```python
# 1D array
slice = arr[1:4]

# 2D array
slice = arr[0:2, 1:3]
```

## Array Manipulation

### Reshaping Arrays
```python
reshaped = arr.reshape((3, 2))
```

### Flattening Arrays
```python
flattened = arr.flatten()
```

### Transposing Arrays
```python
transposed = arr.T
```

## Statistical Operations

### Basic Statistics
```python
mean = arr.mean()
std_dev = arr.std()
sum = arr.sum()
min_value = arr.min()
max_value = arr.max()
```

### Axis-wise Operations
```python
# Sum along an axis
sum_axis = arr.sum(axis=0)
```

## Example

### Complete Example
```python
import numpy as np

# Create an array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Print the array
print('Array:
', arr)

# Array attributes
print('Shape:', arr.shape)
print('Size:', arr.size)
print('Data type:', arr.dtype)

# Array operations
print('Sum of all elements:', arr.sum())
print('Mean of all elements:', arr.mean())
print('Standard deviation:', arr.std())

# Indexing and slicing
print('Element at (0, 1):', arr[0, 1])
print('First row:', arr[0, :])
print('Second column:', arr[:, 1])

# Reshape the array
reshaped = arr.reshape((3, 2))
print('Reshaped array:
', reshaped)

# Transpose the array
transposed = arr.T
print('Transposed array:
', transposed)
```

For more details, refer to the [NumPy documentation](https://numpy.org/doc/stable/).
