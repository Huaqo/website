
# Venv

## Creating a Virtual Environment

```bash
# Create a virtual environment
python -m venv myenv
```

## Activating a Virtual Environment

### On Unix or macOS

```bash
# Activate the virtual environment
source myenv/bin/activate

# Deactivate the virtual environment
deactivate
```

## Virtual Environment Management

### Checking Python Interpreter

```bash
# Check the path of the Python interpreter in the virtual environment
which python
```

### Checking Virtual Environment Path

```python
# Check the path of the virtual environment
import sys
print(sys.prefix)
```

### Creating Isolated Environments

```bash
# Create an isolated environment using venv
python -m venv myenv --without-pip

# Activate the isolated environment and manually install pip
source myenv/bin/activate
curl https://bootstrap.pypa.io/get-pip.py | python
```

## Configuration and Customization

### Customizing the Prompt

```bash
# Customize the prompt of the virtual environment
python -m venv myenv --prompt 'MyEnv'
```

