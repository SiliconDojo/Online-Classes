from bottle import run, route, template, static_file

@route('/')
def index():
    name = 'bob'

    return template('template-static', name=name)

@route('/static/<filename:path>')
def send_static(filename):
    print(filename)
    return static_file(filename, root='./static/')

run(host='localhost', port='8080')