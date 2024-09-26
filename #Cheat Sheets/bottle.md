# Bottle Web App Framework

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
