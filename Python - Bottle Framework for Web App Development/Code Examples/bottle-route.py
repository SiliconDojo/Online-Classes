from bottle import run, route

@route('/')
def index():
    message = '<h1>Hello World</h1>'
    return message

run(host='localhost', port=8080)