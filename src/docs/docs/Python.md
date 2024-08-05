
# Python

## Basics

```python
# Variable Declaration
a = 10  # Integer
b = 20.5  # Float
c = "Hello World"  # String
d = True  # Boolean

# Data Types
num = 100  # Integer
string = "Hello"  # String
boolean = True  # Boolean
lst = [1, 2, 3]  # List
tup = (1, 2, 3)  # Tuple
dct = {"key": "value"}  # Dictionary
st = {1, 2, 3}  # Set
none = None  # NoneType
```

## Operators

```python
# Arithmetic
sum = 1 + 2  # Addition
diff = 5 - 3  # Subtraction
prod = 2 * 3  # Multiplication
quot = 10 / 2  # Division
mod = 10 % 3  # Modulus

# Assignment
x = 10
x += 5  # x = x + 5
x -= 3  # x = x - 3
x *= 2  # x = x * 2
x /= 2  # x = x / 2

# Comparison
is_equal = (1 == 1)  # True
is_not_equal = (1 != 2)  # True
is_greater = (5 > 3)  # True
is_lesser = (3 < 5)  # True
```

## Control Structures

```python
# Conditional Statements
if a > b:
    # code if true
elif a == b:
    # code if equal
else:
    # code if false

# Loops
# For Loop
for i in range(5):
    # code

# While Loop
while a < 10:
    # code
    a += 1
```

## Functions

```python
# Function Definition
def greet(name):
    return "Hello, " + name

# Function Call
greet("John")
```

## Lists

```python
fruits = ["Apple", "Banana", "Cherry"]

# Access Elements
first_fruit = fruits[0]

# List Methods
fruits.append("Orange")  # Add to end
fruits.pop()  # Remove from end
fruits.remove("Banana")  # Remove specific element
sliced = fruits[1:3]  # Slice list

# Loop through List
for fruit in fruits:
    print(fruit)
```

## Dictionaries

```python
person = {
    "name": "John",
    "age": 30
}

# Access Values
name = person["name"]

# Add/Modify Values
person["email"] = "john@example.com"

# Loop through Dictionary
for key, value in person.items():
    print(key, value)
```

## Strings

```python
string = "Hello, World!"

# String Methods
length = len(string)  # Length
upper = string.upper()  # Uppercase
lower = string.lower()  # Lowercase
split = string.split(",")  # Split

# String Formatting
name = "John"
formatted = f"Hello, {name}!"
```

## File I/O

```python
# Write to File
with open("file.txt", "w") as file:
    file.write("Hello, World!")

# Read from File
with open("file.txt", "r") as file:
    content = file.read()
```

## Classes

```python
# Class Definition
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return "Hello, " + self.name

# Inheritance
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def study(self):
        return self.name + " is studying."

# Create Object
student = Student("John", 20, "A")
print(student.greet())
print(student.study())
```

## Modules

```python
# Importing Modules
import math

# Using Functions from Modules
result = math.sqrt(16)  # 4.0

# Importing Specific Functions
from math import sqrt
result = sqrt(16)  # 4.0
```

## Exception Handling

```python
try:
    # code that might raise an exception
    result = 10 / 0
except ZeroDivisionError:
    # code that runs if exception occurs
    print("Cannot divide by zero")
finally:
    # code that always runs
    print("This is the finally block")
```

## List Comprehensions

```python
# Basic List Comprehension
squares = [x ** 2 for x in range(10)]

# Conditional List Comprehension
evens = [x for x in range(10) if x % 2 == 0]
```

## Lambda Functions

```python
# Lambda Function
add = lambda x, y: x + y
result = add(2, 3)  # 5
```
