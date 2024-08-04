
# Flask

## Getting Started

### Installation

```bash
# Install Flask using pip
pip install Flask
```

### Basic Application

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
```

## Routing

### Defining Routes

```python
@app.route('/')
def home():
    return 'Home Page'

@app.route('/about')
def about():
    return 'About Page'
```

### Dynamic URL Parameters

```python
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f'Post {post_id}'
```

## HTTP Methods

```python
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'Do the login'
    else:
        return 'Show the login form'
```

## Templates

### Rendering Templates

```python
from flask import render_template

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)
```

### Template File (templates/hello.html)

```html
<!doctype html>
<title>Hello</title>
<h1>Hello, {{ name }}!</h1>
```

## Forms and Request Data

### Handling Form Data

```python
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f'Username: {username}, Password: {password}'
    return render_template('login.html')
```

### Accessing URL Parameters

```python
@app.route('/search')
def search():
    query = request.args.get('query')
    return f'Search query: {query}'
```

## Redirects and Errors

### Redirecting

```python
from flask import redirect, url_for

@app.route('/admin')
def admin():
    return redirect(url_for('home'))
```

### Error Handling

```python
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404
```

## Static Files

### Serving Static Files

```python
# Place static files in the "static" directory
# Access them with the /static/<filename> URL

@app.route('/static-example')
def static_example():
    return '<img src="/static/example.jpg" alt="Example">'
```

## Flask Extensions

### Installing Extensions

```bash
# Install Flask-WTF for form handling
pip install Flask-WTF
```

### Using Flask-WTF

```python
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return f'Username: {form.username.data}, Password: {form.password.data}'
    return render_template('login.html', form=form)
```

### Example Template (templates/login.html)

```html
<!doctype html>
<title>Login</title>
<form method="POST">
    {{ form.hidden_tag() }}
    {{ form.username.label }} {{ form.username(size=20) }}<br>
    {{ form.password.label }} {{ form.password(size=20) }}<br>
    {{ form.submit() }}
</form>
```

## Running the Application

### Running the Development Server

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

### Using app.run()

```python
if __name__ == '__main__':
    app.run(debug=True)
```
