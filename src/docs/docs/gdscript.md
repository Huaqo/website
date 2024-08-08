
# GDScript

## Awesome links

- [Documentation ->](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_basics.html)

## Basic Syntax

### Comments
```gdscript
# Single line comment

"""
Multiline
comment
"""
```

### Variables
```gdscript
var my_variable = 10
var my_string = "Hello, World!"
var my_array = [1, 2, 3]
var my_dictionary = {"key": "value"}
```

### Constants
```gdscript
const MY_CONSTANT = 42
```

## Data Types

### Basic Types
```gdscript
var my_int: int = 10
var my_float: float = 3.14
var my_bool: bool = true
var my_string: String = "Godot"
```

### Vectors and Colors
```gdscript
var my_vector2: Vector2 = Vector2(10, 20)
var my_vector3: Vector3 = Vector3(10, 20, 30)
var my_color: Color = Color(1, 0, 0)  # Red color
```

## Functions

### Defining Functions
```gdscript
func my_function():
    print("Hello, World!")

func add(a: int, b: int) -> int:
    return a + b
```

### Built-in Functions
```gdscript
func _ready():
    print("Node is ready")

func _process(delta):
    print("Frame time: ", delta)
```

## Flow Control

### Conditionals
```gdscript
if my_variable > 10:
    print("Greater than 10")
elif my_variable == 10:
    print("Equal to 10")
else:
    print("Less than 10")
```

### Loops

#### For Loop
```gdscript
for i in range(5):
    print(i)

for item in my_array:
    print(item)
```

#### While Loop
```gdscript
var i = 0
while i < 5:
    print(i)
    i += 1
```

## Classes and Objects

### Defining a Class
```gdscript
extends Node

class_name MyNode

var my_variable: int

func _init():
    my_variable = 10

func my_method():
    print("My variable is: ", my_variable)
```

### Inheritance
```gdscript
extends MyNode

func _ready():
    my_variable = 20
    my_method()
```

## Signals
```gdscript
signal my_signal

func _ready():
    emit_signal("my_signal")

func _on_MyNode_my_signal():
    print("Signal received")
```

### Connecting Signals
```gdscript
func _ready():
    connect("my_signal", self, "_on_MyNode_my_signal")
```

## Input Handling
```gdscript
func _input(event):
    if event is InputEventKey:
        if event.pressed:
            print("Key pressed: ", event.scancode)
```

## Example

### Complete Example
```gdscript
extends Node2D

signal my_signal

var my_variable: int = 10

func _ready():
    connect("my_signal", self, "_on_MyNode2D_my_signal")
    emit_signal("my_signal")
    print("Node is ready")

func _process(delta):
    my_variable += 1
    print("Frame time: ", delta, ", Variable: ", my_variable)

func _on_MyNode2D_my_signal():
    print("Signal received")
```

For more details, refer to the [Godot Engine documentation](https://docs.godotengine.org/en/stable/).
