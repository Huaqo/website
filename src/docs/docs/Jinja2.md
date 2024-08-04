
# Jinja2

## Basic Syntax

### Variable Interpolation

```jinja2
{{ variable }}
```

### Expressions

```jinja2
{{ 1 + 2 }}
{{ "Hello" ~ "World" }}
{{ variable | length }}
```

## Template Inheritance

### Base Template

```jinja2
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}My Website{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>
```

### Child Template

```jinja2
{% extends "base.html" %}

{% block title %}Home Page{% endblock %}

{% block content %}
<h1>Welcome to the Home Page</h1>
<p>This is the content of the home page.</p>
{% endblock %}
```

## Control Structures

### If Statement

```jinja2
{% if user %}
    Hello, {{ user }}!
{% else %}
    Hello, Guest!
{% endif %}
```

### For Loop

```jinja2
<ul>
    {% for item in items %}
    <li>{{ item }}</li>
    {% endfor %}
</ul>
```

### Macros

```jinja2
{% macro input(name, value='', type='text') %}
    <input type="{{ type }}" name="{{ name }}" value="{{ value }}">
{% endmacro %}

<p>{{ input('username') }}</p>
```

## Filters

### Applying Filters

```jinja2
{{ "hello world" | capitalize }}
{{ [1, 2, 3] | sum }}
```

### Custom Filters

```python
def reverse_filter(s):
    return s[::-1]

env.filters['reverse'] = reverse_filter
```

```jinja2
{{ "hello" | reverse }}
```

## Include and Import

### Include Template

```jinja2
{% include "header.html" %}
<p>Main content goes here...</p>
{% include "footer.html" %}
```

### Import Macros

```jinja2
{% import "macros.html" as macros %}
<p>{{ macros.input('username') }}</p>
```

## Template Comments

```jinja2
{# This is a comment #}
```

## Escaping

### Autoescaping

```jinja2
{% autoescape true %}
    {{ user_input }}
{% endautoescape %}
```

### Manual Escaping

```jinja2
{{ user_input | escape }}
```

## Setting Variables

```jinja2
{% set username = "John Doe" %}
<p>Hello, {{ username }}!</p>
```

## Loop Controls

### Loop Variables

```jinja2
{% for item in items %}
    {{ loop.index }} - {{ item }}
{% endfor %}
```

### Break and Continue

```jinja2
{% for item in items %}
    {% if item == "skip" %}
        {% continue %}
    {% endif %}
    {% if item == "stop" %}
        {% break %}
    {% endif %}
    {{ item }}
{% endfor %}
```

## Whitespace Control

```jinja2
{% raw %}
{% for item in items %}
    {{ item }}
{% endfor %}
{% endraw %}
```

```jinja2
{{- variable -}}
{%+ tag -%}
```

## Extending Jinja2

### Custom Functions

```python
def custom_function():
    return "Hello from custom function"

env.globals['custom_function'] = custom_function
```

```jinja2
<p>{{ custom_function() }}</p>
```

### Custom Tests

```python
def is_even(n):
    return n % 2 == 0

env.tests['even'] = is_even
```

```jinja2
{% if variable is even %}
    <p>{{ variable }} is even</p>
{% endif %}
```

