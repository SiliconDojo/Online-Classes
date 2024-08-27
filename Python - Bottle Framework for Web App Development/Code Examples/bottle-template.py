from bottle import run, route, template

@route('/hello')
def hello():
    return template('hello_template')

@route('/hello-var/<name>')
def hello_var(name):
    return template('hello_var_template', name=name)

run(host='localhost', port=8080)