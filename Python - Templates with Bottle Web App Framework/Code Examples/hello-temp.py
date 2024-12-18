from bottle import route, run, template

@route('/')
def index():
    return template('hello-template')

run(host='localhost', port='8080')