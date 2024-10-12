# Bottle Web App Framework

## Static Route

```
from bottle import run, route

@route('/')
def index():
    message = '<h1>Hello World</h1>'
    return message

@route('/about')
def about():
    message = '<h1>I am so cool!!!</h1>'
    return message

run(host='localhost', port=8080)
```

## Dynamic Route

```
from bottle import run, route

@route('/name/<name>')
def index(name):
    message = f'<h1>Hello {name}</h1>'
    return message

@route('/name/<name>/<age:int>')
def name_age(name, age):
    message = f'<h1>Hello {name} you are {age} years old</h1>'
    return message

@route('/<message>')
def name_age(message):
    message = message
    return message

run(host='localhost', port=8080)
```

## POST
```
from bottle import run, route, post

@route('/')
def index():
    form =  '''
            <form action="/process" method="post">
               Value: <input type="text" name="value">
               <input type="submit">
            </form>
    return form

@post('/process')
def process():
    value = request.forms.get('value')
    return value

run(host='localhost', port=8080)
```

## GET

```
from bottle import run, route, get, request

@route('/')
@get('/')
def index():
    color = request.query.get('color')

    form =  '''
                <a href="/?color=red">Red</a>
                <br>
                <a href="/?color=green">Green</a>
                <br>
                <a href="/?color=yellow">Yellow</a>
                <br>
            '''
    page = f'''
                <h1>Web App</h1>
                <body style="background-color:{color};">
                {form}
                </body>
            '''
    return page

run(host='localhost', port=8080)
```

## Static Files

Make sure that permissions are setup properly so that users can access the folder and files. 

```
from bottle import run, route, static_file

@route('/')
def index():
    file = 'image.png'
    page = f'''
                <link rel="stylesheet" type="text/css" href="/static/style.css">
                <body>
                    <h1>Static File</h1>
                    <img style="height:300px; width:auto;" src="/static/{file}">
                    <p>This is an embedded picture</p>
                </body>
            '''
    return page

@route('/static/<filename:path>')
def send_static(filename):
    print(filename)
    return static_file(filename, root='./static/')

run(host='localhost', port=8080)
```


## Templates

```
from bottle import run, route, template

@route('/hello')
def hello():
    return template('hello_template')

@route('/hello-var/<name>')
def hello_var(name):
    return template('hello_var_template', name=name)

run(host='localhost', port=8080)
```

Template Files should be in a folder called **views** in your root directory

**hello_template.tpl**
```
<h1>Hello World</h1>

<p>This is a template</p>

<p>Templates are HTML files that you can add variables values to</p>
```

**hello_var_template.tpl**
```
<h1>Hello {{ name }}</h1>

%if name == 'bob':
    <h1>{{ name }} is awesome!!!</h1>
%else:
    <h1>{{ name }} is not as cool as Bob!</h1>
%end
```

## Run Bottle with Gunicorn

Install Gunicorn
```
python3 -m pip install gunicorn
```

Create App Instance Using default_app()
**web-test.py**
```
from bottle import route, default_app

@route('/')
def index():
    return "Hello, Bottle app is running without calling run()!"

@route('/hello')
def hello():
    return "Hello dude how ya doing??"

app = default_app()
```

Run Gunicorn. Point to Script and App Instance
```
gunicorn -w 4 web-test:app
```


