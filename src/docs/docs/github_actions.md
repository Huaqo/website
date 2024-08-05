
# GitHub Actions

## Basic Concepts

### Workflow
A configurable automated process made up of one or more jobs.

### Job
A set of steps executed on the same runner.

### Step
A single task that can run commands or actions.

### Runner
A server that runs your workflows when triggered.

## Configuration

### Workflow File Location
Place your workflow files in the `.github/workflows` directory of your repository.

### Workflow File Format
Workflow files are written in YAML.

### Example Workflow File
```yaml
name: CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: |
        pytest
```

## Triggers

### `on` Keyword
Defines the events that trigger the workflow.

#### Common Events
- `push`: Triggered on push.
- `pull_request`: Triggered on pull requests.
- `schedule`: Triggered on a schedule.
- `workflow_dispatch`: Manually triggered.

#### Example
```yaml
on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main
  schedule:
    - cron: '0 0 * * *'
```

## Jobs

### Defining a Job
A job contains a set of steps.

#### Example
```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Check out repository
      uses: actions/checkout@v2
```

### Job Dependencies
Define dependencies between jobs.

#### Example
```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Build
      run: echo "Building..."

  test:
    runs-on: ubuntu-latest
    needs: build
    steps:
    - name: Test
      run: echo "Testing..."
```

## Steps

### Running Commands
Use the `run` keyword to execute commands.

#### Example
```yaml
steps:
- name: Run a one-line script
  run: echo "Hello, world!"
- name: Run a multi-line script
  run: |
    echo "Hello, world!"
    echo "This is GitHub Actions"
```

### Using Actions
Use the `uses` keyword to run an action.

#### Example
```yaml
steps:
- name: Check out repository
  uses: actions/checkout@v2
```

## Runners

### Types of Runners
- `ubuntu-latest`
- `windows-latest`
- `macos-latest`

#### Example
```yaml
jobs:
  build:
    runs-on: ubuntu-latest
```

## Environment Variables

### Setting Environment Variables
Use the `env` keyword to set environment variables.

#### Example
```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    env:
      MY_VAR: "Hello, world!"
    steps:
    - name: Print variable
      run: echo $MY_VAR
```

## Secrets

### Using Secrets
Store sensitive information securely.

#### Example
```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Use secret
      run: echo ${{ secrets.MY_SECRET }}
```

## Matrix Builds

### Defining a Matrix
Run jobs with multiple configurations.

#### Example
```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.6, 3.7, 3.8, 3.9]
    steps:
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: pip install -r requirements.txt
    - name: Run tests
      run: pytest
```

## Caching

### Caching Dependencies
Use the `actions/cache` action to cache dependencies.

#### Example
```yaml
steps:
- uses: actions/cache@v2
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-
```

## Example Workflow

### Complete Example
```yaml
name: CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    - name: Run tests
      run: |
        pytest

  deploy:
    runs-on: ubuntu-latest
    needs: build
    steps:
    - name: Deploy
      run: echo "Deploying..."
```

For more details, refer to the [GitHub Actions documentation](https://docs.github.com/en/actions).
