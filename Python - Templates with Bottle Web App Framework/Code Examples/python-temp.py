from bottle import route, run, template

@route('/')
def index():
    name = 'bob'
    payment = 20
    return template('template-python', name=name, payment=payment)

run(host='localhost', port='8080')