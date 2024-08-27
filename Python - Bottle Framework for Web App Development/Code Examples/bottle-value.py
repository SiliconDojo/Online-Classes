from bottle import run, route

@route('/name/<name>')
def index(name):
    message = f'<h1>Hello {name}</h1>'
    return message

@route('/name/<name>/<age:int>')
def name_age(name, age):
    message = f'<h1>Hello {name} you are {age} years old</h1>'
    return message

run(host='localhost', port=8080)