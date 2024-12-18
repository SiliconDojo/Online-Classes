from bottle import run, route, template

@route('/')
def index():
    return template('template-include')

run(host='0.0.0.0', port='8080')