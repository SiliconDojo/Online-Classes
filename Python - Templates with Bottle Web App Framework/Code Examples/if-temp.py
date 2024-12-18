from bottle import route, run, template

@route('/')
def index():
    name = 'tim'
    age = 50
    return template('template-if', name=name, age=age)

run(host='localhost', port='8080')