
# Json

## Importing the JSON Module

```python
import json
```

## Reading JSON Data

### Reading JSON from a String

```python
json_string = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_string)
print(data)
```

### Reading JSON from a File

```python
with open('data.json', 'r') as file:
    data = json.load(file)
print(data)
```

## Writing JSON Data

### Writing JSON to a String

```python
data = {"name": "John", "age": 30, "city": "New York"}
json_string = json.dumps(data)
print(json_string)
```

### Writing JSON to a File

```python
data = {"name": "John", "age": 30, "city": "New York"}
with open('data.json', 'w') as file:
    json.dump(data, file)
```

## Formatting JSON

### Pretty Print JSON

```python
data = {"name": "John", "age": 30, "city": "New York"}
json_string = json.dumps(data, indent=4)
print(json_string)
```

### Custom Separators

```python
data = {"name": "John", "age": 30, "city": "New York"}
json_string = json.dumps(data, separators=(',', ': '))
print(json_string)
```

## Working with JSON Objects

### Accessing JSON Data

```python
data = {"name": "John", "age": 30, "city": "New York"}
print(data['name'])
print(data.get('age'))
```

### Modifying JSON Data

```python
data = {"name": "John", "age": 30, "city": "New York"}
data['age'] = 31
data['city'] = 'San Francisco'
print(data)
```

### Deleting JSON Data

```python
data = {"name": "John", "age": 30, "city": "New York"}
del data['age']
print(data)
```

## Handling JSON Errors

### Handling JSON Decode Error

```python
json_string = '{"name": "John", "age": 30, "city": "New York"'
try:
    data = json.loads(json_string)
except json.JSONDecodeError as e:
    print(f'Error decoding JSON: {e}')
```

### Handling JSON Encode Error

```python
data = {"name": "John", "age": 30, "city": set([1, 2, 3])}
try:
    json_string = json.dumps(data)
except TypeError as e:
    print(f'Error encoding JSON: {e}')
```

## Custom JSON Encoding and Decoding

### Custom JSON Encoder

```python
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)

data = {"name": "John", "age": 30, "city": set([1, 2, 3])}
json_string = json.dumps(data, cls=CustomEncoder)
print(json_string)
```

### Custom JSON Decoder

```python
def decode_set(dct):
    for key, value in dct.items():
        if isinstance(value, list):
            dct[key] = set(value)
    return dct

json_string = '{"name": "John", "age": 30, "city": [1, 2, 3]}'
data = json.loads(json_string, object_hook=decode_set)
print(data)
```

## JSON with Complex Objects

### Encoding and Decoding Complex Objects

```python
from datetime import datetime

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)

data = {"name": "John", "age": 30, "joined": datetime.now()}
json_string = json.dumps(data, cls=ComplexEncoder)
print(json_string)

def decode_datetime(dct):
    for key, value in dct.items():
        try:
            dct[key] = datetime.fromisoformat(value)
        except (ValueError, TypeError):
            pass
    return dct

data = json.loads(json_string, object_hook=decode_datetime)
print(data)
```

